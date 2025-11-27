# Roteiro de Estudo: Monitoramento com Prometheus

## Objetivo do Roteiro

Aprender a utilizar o Prometheus para monitorar aplicações web Flask, compreendendo conceitos de métricas, instrumentação de código com a biblioteca `prometheus-flask-exporter` e visualização de dados de performance em tempo real.

---

## ⚠️ CONCEITOS IMPORTANTES

**Antes de começar, entenda a diferença entre teste de carga e monitoramento:**

- **Locust**: Ferramenta para GERAR carga (simular usuários)
- **Prometheus**: Ferramenta para COLETAR e ARMAZENAR métricas
- **Grafana**: Ferramenta para VISUALIZAR métricas (dashboards)

**Neste roteiro:**

- Vamos instrumentar o `app_teste.py` (do roteiro de Locust) para expor métricas
- Configurar o Prometheus para coletar essas métricas
- Aprender a consultar métricas usando PromQL
- Integrar com Grafana para visualização

---

## Parte 1: Instalação do Prometheus Flask Exporter

### Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes do Python)
- O arquivo `app_teste.py` do roteiro de Locust
- Docker instalado (para Prometheus e Grafana)

### Passo 1.1: Verificar Python e pip

```bash
python --version
pip --version
```

### Passo 1.2: Criar ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv_prometheus
venv_prometheus\Scripts\activate

# Linux/Mac
python3 -m venv venv_prometheus
source venv_prometheus/bin/activate
```

### Passo 1.3: Instalar dependências

```bash
pip install flask prometheus-flask-exporter
```

### Passo 1.4: Verificar instalação

```bash
pip show prometheus-flask-exporter
```

---

## Parte 2: Entendendo o Prometheus

### O que é o Prometheus?

Prometheus é um sistema de monitoramento e alertas open-source que:

- Coleta métricas via HTTP (modelo pull)
- Armazena dados em formato de séries temporais
- Possui linguagem de consulta própria (PromQL)
- Suporta alertas e integração com Grafana

### Tipos de Métricas

1. **Counter**: Valor que só aumenta (ex: total de requisições)
2. **Gauge**: Valor que pode subir ou descer (ex: usuários ativos)
3. **Histogram**: Distribuição de valores (ex: latência de requisições)
4. **Summary**: Similar ao histogram, com percentis pré-calculados

### Formato das Métricas

```
# HELP http_requests_total Total de requisições HTTP
# TYPE http_requests_total counter
http_requests_total{method="GET", endpoint="/produtos", status="200"} 1523
```

---

## Parte 3: Instrumentando o app_teste.py

### Passo 3.1: Versão básica com prometheus-flask-exporter

**Arquivo: `app_teste_prometheus.py`**

```python
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
import time
import random

app = Flask(__name__)

# Inicializa o Prometheus Metrics
# Isso automaticamente expõe métricas no endpoint /metrics
metrics = PrometheusMetrics(app)

# Informações estáticas sobre a aplicação
metrics.info('app_info', 'Informações da aplicação', version='1.0.0', app_name='ecommerce_teste')

# Simulando banco de dados de produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "estoque": 10},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "estoque": 100},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "estoque": 50},
    {"id": 4, "nome": "Monitor", "preco": 800.00, "estoque": 20},
]

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo ao E-commerce de Teste"})

@app.route('/produtos')
def listar_produtos():
    # Simula latência do banco de dados
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify(produtos)

@app.route('/produto/<int:produto_id>')
def detalhes_produto(produto_id):
    time.sleep(random.uniform(0.05, 0.15))
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/carrinho', methods=['POST'])
def adicionar_carrinho():
    time.sleep(random.uniform(0.2, 0.4))
    dados = request.json
    return jsonify({
        "mensagem": "Produto adicionado ao carrinho",
        "produto_id": dados.get("produto_id"),
        "quantidade": dados.get("quantidade", 1)
    })

@app.route('/checkout', methods=['POST'])
def checkout():
    # Simula processamento de pagamento
    time.sleep(random.uniform(0.5, 1.0))
    return jsonify({
        "mensagem": "Compra realizada com sucesso",
        "pedido_id": random.randint(1000, 9999)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Passo 3.2: Executar e verificar métricas

**Terminal 1 - Iniciar o servidor:**

```bash
python app_teste_prometheus.py
```

**Terminal 2 - Verificar métricas:**

```bash
curl http://localhost:5000/metrics
```

Você verá métricas como:

```
# HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds histogram
flask_http_request_duration_seconds_bucket{endpoint="/produtos",method="GET",status="200",le="0.005"} 0.0
flask_http_request_duration_seconds_bucket{endpoint="/produtos",method="GET",status="200",le="0.01"} 0.0
...
flask_http_request_total{endpoint="/produtos",method="GET",status="200"} 15.0
```

---

## Parte 4: Métricas Personalizadas

### Passo 4.1: Adicionando métricas customizadas

**Arquivo: `app_teste_prometheus_custom.py`**

```python
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge, Histogram, Summary
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# === MÉTRICAS CUSTOMIZADAS ===

# Counter: conta eventos que só aumentam
vendas_total = Counter(
    'ecommerce_vendas_total',
    'Total de vendas realizadas',
    ['metodo_pagamento']
)

produtos_carrinho = Counter(
    'ecommerce_produtos_carrinho_total',
    'Total de produtos adicionados ao carrinho',
    ['produto_id']
)

# Gauge: valor que pode subir ou descer
usuarios_ativos = Gauge(
    'ecommerce_usuarios_ativos',
    'Número de usuários ativos no momento'
)

estoque_produto = Gauge(
    'ecommerce_estoque_produto',
    'Quantidade em estoque por produto',
    ['produto_id', 'produto_nome']
)

# Histogram: distribuição de valores com buckets
tempo_checkout = Histogram(
    'ecommerce_checkout_duracao_seconds',
    'Tempo de processamento do checkout',
    buckets=[0.1, 0.25, 0.5, 0.75, 1.0, 2.0, 5.0]
)

# Summary: percentis pré-calculados
tempo_busca = Summary(
    'ecommerce_busca_duracao_seconds',
    'Tempo de busca de produtos'
)

# Informações da aplicação
metrics.info('app_info', 'Informações da aplicação', version='1.0.0', app_name='ecommerce_teste')

# Simulando banco de dados de produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "estoque": 10},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "estoque": 100},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "estoque": 50},
    {"id": 4, "nome": "Monitor", "preco": 800.00, "estoque": 20},
]

# Inicializa métricas de estoque
for produto in produtos:
    estoque_produto.labels(
        produto_id=str(produto['id']),
        produto_nome=produto['nome']
    ).set(produto['estoque'])

@app.route('/')
def home():
    usuarios_ativos.inc()  # Incrementa usuários ativos
    return jsonify({"mensagem": "Bem-vindo ao E-commerce de Teste"})

@app.route('/produtos')
@tempo_busca.time()  # Decorator para medir tempo automaticamente
def listar_produtos():
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify(produtos)

@app.route('/produto/<int:produto_id>')
def detalhes_produto(produto_id):
    with tempo_busca.time():  # Context manager para medir tempo
        time.sleep(random.uniform(0.05, 0.15))
        produto = next((p for p in produtos if p["id"] == produto_id), None)
        if produto:
            return jsonify(produto)
        return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/carrinho', methods=['POST'])
def adicionar_carrinho():
    time.sleep(random.uniform(0.2, 0.4))
    dados = request.json
    produto_id = dados.get("produto_id", 0)
    
    # Incrementa contador de produtos no carrinho
    produtos_carrinho.labels(produto_id=str(produto_id)).inc()
    
    return jsonify({
        "mensagem": "Produto adicionado ao carrinho",
        "produto_id": produto_id,
        "quantidade": dados.get("quantidade", 1)
    })

@app.route('/checkout', methods=['POST'])
def checkout():
    inicio = time.time()
    
    # Simula processamento de pagamento
    time.sleep(random.uniform(0.5, 1.0))
    
    dados = request.json or {}
    metodo = dados.get("metodo_pagamento", "credito")
    
    # Registra métricas
    vendas_total.labels(metodo_pagamento=metodo).inc()
    tempo_checkout.observe(time.time() - inicio)
    
    # Simula redução de estoque
    produto_id = dados.get("produto_id", 1)
    for produto in produtos:
        if produto['id'] == produto_id:
            produto['estoque'] -= 1
            estoque_produto.labels(
                produto_id=str(produto['id']),
                produto_nome=produto['nome']
            ).set(produto['estoque'])
    
    return jsonify({
        "mensagem": "Compra realizada com sucesso",
        "pedido_id": random.randint(1000, 9999)
    })

@app.route('/logout')
def logout():
    usuarios_ativos.dec()  # Decrementa usuários ativos
    return jsonify({"mensagem": "Logout realizado"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## Parte 5: Configurando o Prometheus Server

### Passo 5.1: Criar arquivo de configuração

**Arquivo: `prometheus.yml`**

```yaml
global:
  scrape_interval: 15s  # Coleta métricas a cada 15 segundos
  evaluation_interval: 15s  # Avalia regras a cada 15 segundos

scrape_configs:
  # Monitoramento do próprio Prometheus
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Monitoramento da aplicação Flask
  - job_name: 'flask_app'
    static_configs:
      - targets: ['host.docker.internal:5000']  # Para Docker no Windows/Mac
      # Use 'localhost:5000' se rodar Prometheus diretamente
    metrics_path: /metrics
    scrape_interval: 5s  # Coleta mais frequente para a aplicação
```

### Passo 5.2: Executar Prometheus com Docker

```bash
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

**Para Windows (PowerShell):**

```powershell
docker run -d `
  --name prometheus `
  -p 9090:9090 `
  -v ${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml `
  prom/prometheus
```

### Passo 5.3: Verificar Prometheus

1. Acesse: `http://localhost:9090`
2. Vá em **Status > Targets**
3. Verifique se `flask_app` está com status **UP**

---

## Parte 6: Consultando Métricas com PromQL

### Interface do Prometheus

Acesse `http://localhost:9090` e use a aba **Graph** para executar consultas.

### Consultas Básicas

**1. Total de requisições:**

```promql
flask_http_request_total
```

**2. Requisições por endpoint:**

```promql
flask_http_request_total{endpoint="/produtos"}
```

**3. Taxa de requisições por segundo (últimos 5 minutos):**

```promql
rate(flask_http_request_total[5m])
```

**4. Latência média (últimos 5 minutos):**

```promql
rate(flask_http_request_duration_seconds_sum[5m]) / rate(flask_http_request_duration_seconds_count[5m])
```

**5. Percentil 95 de latência:**

```promql
histogram_quantile(0.95, rate(flask_http_request_duration_seconds_bucket[5m]))
```

**6. Total de vendas por método de pagamento:**

```promql
ecommerce_vendas_total
```

**7. Estoque atual por produto:**

```promql
ecommerce_estoque_produto
```

**8. Usuários ativos:**

```promql
ecommerce_usuarios_ativos
```

### Consultas Avançadas

**Taxa de erros (requisições com status 5xx):**

```promql
sum(rate(flask_http_request_total{status=~"5.."}[5m])) / sum(rate(flask_http_request_total[5m])) * 100
```

**Requisições por segundo por endpoint:**

```promql
sum by (endpoint) (rate(flask_http_request_total[1m]))
```

**Top 3 endpoints mais lentos:**

```promql
topk(3, rate(flask_http_request_duration_seconds_sum[5m]) / rate(flask_http_request_duration_seconds_count[5m]))
```

---

## Parte 7: Integrando com Grafana

### Passo 7.1: Executar Grafana com Docker

```bash
docker run -d \
  --name grafana \
  -p 3000:3000 \
  grafana/grafana
```

### Passo 7.2: Configurar Data Source

1. Acesse: `http://localhost:3000`
2. Login: `admin` / `admin` (altere a senha)
3. Vá em **Configuration > Data Sources**
4. Clique em **Add data source**
5. Selecione **Prometheus**
6. URL: `http://host.docker.internal:9090`
7. Clique em **Save & Test**

### Passo 7.3: Criar Dashboard

1. Vá em **Create > Dashboard**
2. Clique em **Add visualization**
3. Selecione o data source **Prometheus**

**Painel 1: Requisições por Segundo**

- Query: `sum(rate(flask_http_request_total[1m]))`
- Visualization: Time series
- Title: "Requisições por Segundo"

**Painel 2: Latência P95**

- Query: `histogram_quantile(0.95, rate(flask_http_request_duration_seconds_bucket[5m]))`
- Visualization: Gauge
- Title: "Latência P95"

**Painel 3: Total de Vendas**

- Query: `sum(ecommerce_vendas_total)`
- Visualization: Stat
- Title: "Total de Vendas"

**Painel 4: Estoque por Produto**

- Query: `ecommerce_estoque_produto`
- Visualization: Bar gauge
- Title: "Estoque por Produto"

---

## Parte 8: Exercícios Práticos

### Exercício 1: Métricas Básicas

1. Execute o `app_teste_prometheus.py`
2. Acesse `/metrics` e identifique:
   - Quantas requisições foram feitas?
   - Qual o tempo médio de resposta?
   - Quais endpoints foram acessados?

### Exercício 2: Métricas Customizadas

1. Adicione uma métrica Counter para contar buscas por termo
2. Adicione uma métrica Gauge para rastrear itens no carrinho
3. Teste as novas métricas

### Exercício 3: Integração Locust + Prometheus

1. Execute o `app_teste_prometheus_custom.py`
2. Execute o Locust para gerar carga
3. Observe as métricas no Prometheus enquanto o teste roda
4. Perguntas:
   - Como a latência muda com mais usuários?
   - Qual endpoint é mais afetado?

### Exercício 4: Alertas com PromQL

Crie consultas PromQL para detectar:

1. Taxa de erros acima de 5%
2. Latência P95 acima de 1 segundo
3. Estoque abaixo de 5 unidades

### Exercício 5: Dashboard Completo

Crie um dashboard no Grafana com:

1. Painel de requisições por endpoint
2. Painel de latência (média, P50, P95, P99)
3. Painel de taxa de erros
4. Painel de métricas de negócio (vendas, carrinho)

---

## Parte 9: Troubleshooting

### Problema: "Target is down" no Prometheus

**Soluções:**

- Verifique se a aplicação Flask está rodando
- Confirme que o endpoint `/metrics` está acessível
- Para Docker, use `host.docker.internal` em vez de `localhost`

### Problema: Métricas não aparecem

**Soluções:**

- Verifique se o `PrometheusMetrics` foi inicializado
- Acesse diretamente `http://localhost:5000/metrics`
- Verifique erros no console do Flask

### Problema: Grafana não conecta ao Prometheus

**Soluções:**

- Use `http://host.docker.internal:9090` para containers
- Verifique se os containers estão na mesma rede
- Teste a conexão com "Save & Test"

### Problema: Métricas customizadas não registram

**Soluções:**

- Verifique se as labels estão corretas
- Confirme que os métodos `.inc()`, `.set()`, `.observe()` estão sendo chamados
- Reinicie a aplicação após mudanças

---

## Recursos Adicionais

### Documentação Oficial

- Prometheus: https://prometheus.io/docs/
- prometheus-flask-exporter: https://github.com/rycus86/prometheus_flask_exporter
- Grafana: https://grafana.com/docs/

### Tutoriais Recomendados

- https://prometheus.io/docs/prometheus/latest/getting_started/
- https://grafana.com/tutorials/grafana-fundamentals/

### Ferramentas Complementares

- **AlertManager**: Para gerenciamento de alertas
- **Pushgateway**: Para métricas de jobs batch
- **Node Exporter**: Para métricas do sistema operacional

---

## Checklist de Conclusão

Ao final deste roteiro, você deve ser capaz de:

- [ ] Instalar e configurar o prometheus-flask-exporter
- [ ] Instrumentar uma aplicação Flask com métricas
- [ ] Criar métricas customizadas (Counter, Gauge, Histogram, Summary)
- [ ] Configurar e executar o Prometheus Server
- [ ] Escrever consultas PromQL básicas e avançadas
- [ ] Integrar Prometheus com Grafana
- [ ] Criar dashboards de monitoramento
- [ ] Identificar gargalos através de métricas
- [ ] Compreender a diferença entre tipos de métricas
- [ ] Correlacionar testes de carga com métricas de monitoramento

---

## Projeto Final

### Desafio: Monitoramento Completo de E-commerce

**Objetivo:** Criar um sistema completo de monitoramento para o cenário de Black Friday

**Requisitos:**

1. Aplicação Flask instrumentada com métricas de:
   - Performance (latência, throughput)
   - Negócio (vendas, conversão, abandono de carrinho)
   - Infraestrutura (uso de recursos)

2. Prometheus configurado com:
   - Scrape de múltiplos targets
   - Recording rules para métricas derivadas
   - Alerting rules para condições críticas

3. Dashboard Grafana com:
   - Visão geral de saúde da aplicação
   - Métricas de negócio em tempo real
   - Painel de alertas

4. Documentação incluindo:
   - Arquitetura do monitoramento
   - Descrição de cada métrica
   - Runbook para resposta a alertas

5. Teste integrado:
   - Execute Locust para gerar carga
   - Capture screenshots das métricas
   - Analise correlação entre carga e performance

---

## Considerações Finais

### Boas Práticas de Monitoramento:

- Use labels de forma consistente e padronizada
- Não crie métricas com cardinalidade muito alta
- Documente o significado de cada métrica
- Configure alertas com thresholds apropriados
- Mantenha dashboards organizados e focados

### Os 4 Sinais Dourados (Golden Signals):

1. **Latência**: Tempo de resposta das requisições
2. **Tráfego**: Volume de requisições
3. **Erros**: Taxa de falhas
4. **Saturação**: Uso de recursos

---

**Professor:** Marcelo Damasceno de Melo

**Disciplina:** Avaliação de Desempenho de Sistemas

**Data:** Novembro 2025

---

**Dúvidas?** Consulte a documentação oficial

**Bons estudos!**