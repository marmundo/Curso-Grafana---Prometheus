# FastAPI Example Project

Este projeto é um exemplo de aplicação utilizando FastAPI.

## Configuração do Ambiente

### 1. Criação e Execução do Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 2. Instalação das Bibliotecas

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 3. Execução do Arquivo `app.py`

Para iniciar a aplicação, execute o seguinte comando:

```bash
uvicorn app:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação FastAPI.
- `requirements.txt`: Arquivo contendo as dependências do projeto.

## Utilizando Docker Compose

### 1. Construção e Execução dos Containers

Para construir e executar os containers, utilize o comando:

```bash
docker-compose up --build -d
```

### 2. Parada dos Containers

Para parar os containers, utilize o comando:

```bash
docker-compose down
```

A aplicação estará disponível em `http://127.0.0.1:8000`.


## Configurando o Data Source no Grafana

Para configurar um data source no Grafana utilizando a URL `http://host.docker.internal:9090`, siga os passos abaixo:

1. Acesse o Grafana em `http://localhost:3000` e faça login (user:admin, senha:admin).
2. No menu lateral esquerdo, clique em **Configuration** (ícone de engrenagem) e selecione **Data Sources**.
3. Clique no botão **Add data source**.
4. Selecione **Prometheus** como o tipo de data source.
5. No campo **URL**, insira `http://host.docker.internal:9090`.
6. Clique em **Save & Test** para salvar a configuração e testar a conexão.

Se a conexão for bem-sucedida, o Grafana estará configurado para utilizar o Prometheus como data source.