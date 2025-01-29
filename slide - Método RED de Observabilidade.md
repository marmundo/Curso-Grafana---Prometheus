---
marp: true
theme: default
---


# Método RED de Observabilidade

---

# O que é o Método RED?

O método RED é uma abordagem para monitoramento e observabilidade de sistemas, focado em três métricas principais:

- **Rate**: Taxa de requisições por segundo.
- **Errors**: Número de erros por segundo.
- **Duration**: Tempo de duração das requisições.

---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<div class="mermaid">
graph TD
    A[Requisições] --> B[Rate: Taxa de requisições/s]
    A --> C[Errors: Erros/s]
    A --> D[Duration: Duração das requisições]
    B --> E[Monitoramento Contínuo]
    C --> E
    D --> E
    E --> F[Saúde do Sistema]
</div>

---

# Porque usar o método RED

1. Foco nas Métricas Essenciais
    - O RED elimina a complexidade ao focar em apenas três métricas-chave:
        - Rate: Quantas requisições estão sendo processadas?
        - Errors: Quantas estão falhando?
        - Duration: Quanto tempo estão levando?

2. Detecção Rápida de Problemas
    - Com o RED, você pode identificar rapidamente:
        - Picos de tráfego (Rate).
        - Aumento de falhas (Errors).
        - Degradação de desempenho (Duration).
---

# Porque usar o método RED

3. Tomada de Decisão Baseada em Dados
    - As métricas do RED fornecem insights claros para:
        - Escalar recursos.
        - Corrigir erros.
        - Melhorar a experiência do usuário.

4. Adaptável a Qualquer Sistema
    - O RED pode ser aplicado em:
        - Microsserviços.
        - Aplicações monolíticas.
        - Sistemas distribuídos.

---

# Componentes do Método RED

## 1. Rate (Taxa)
- Mede o número de requisições por unidade de tempo.
- Exemplo: Requisições por segundo (RPS).

---
# Componentes do Método RED

## 2. Errors (Erros)
- Contabiliza o número de requisições que falharam.
- Exemplo: Erros por segundo (EPS).

---
# Componentes do Método RED

## 3. Duration (Duração)
- Mede o tempo que as requisições levam para serem processadas.
- Exemplo: Latência em milissegundos.

---
# Origem do Método RED

O método RED foi popularizado pelo **Google SRE (Site Reliability Engineering)** como parte de suas práticas de monitoramento e observabilidade. Ele é uma evolução do **Método USE (Utilization, Saturation, Errors)**, focado em recursos de infraestrutura, adaptado para sistemas baseados em serviços.

---

# Contexto Histórico

- Surgiu da necessidade de monitorar sistemas distribuídos e microsserviços.
- Foi criado para simplificar a observabilidade, focando em métricas que refletem diretamente a experiência do usuário.


---

# Origem do Método RED

### Influências:
- Baseado em princípios do **SRE** e **Monitoramento Orientado a Serviços**.
- Amplamente adotado por empresas como Google, Netflix e Amazon.

---

# Benefícios do Método RED

- **Visibilidade**: Proporciona uma visão clara do desempenho do sistema.
- **Detecção Rápida**: Identifica anomalias e problemas em tempo real.
- **Tomada de Decisão**: Facilita a tomada de decisões baseadas em dados.

---

# Exemplo de Aplicação

## Cenário:
- Sistema de e-commerce com alta carga de requisições.

## Métricas RED:
- **Rate**: 500 requisições por segundo.
- **Errors**: 5 erros por segundo.
- **Duration**: 200ms de latência média.

---

# Ferramentas para Implementar o Método RED

- **Prometheus**: Para coleta e armazenamento de métricas.
- **Grafana**: Para visualização e alertas.
- **Jaeger**: Para rastreamento de duração.

---

# Conclusão

O método RED é uma abordagem eficaz para monitoramento e observabilidade, proporcionando uma visão clara e concisa da saúde do sistema. Ao focar em Rate, Errors e Duration, você pode detectar e resolver problemas rapidamente, garantindo a estabilidade e performance do seu sistema.

---

# Perguntas?

Obrigado pela atenção!