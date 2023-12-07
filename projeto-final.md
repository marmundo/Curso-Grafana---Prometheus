# Introdução

Você foi contratado para fazer o monitoramento de um sistema da empresa Damasceno Inc.

Para facilitar a sua atuação nesse projeto, o CEO Marcelo Damasceno cedeu o [link](http://34.121.40.211:9090) do monitoramento realizado com o Prometheus.

A aplicação que você irá monitorar é baseada em [TNS](https://github.com/grafana/tns). Além de métricas relacionada a aplicação, existem métricas relacionadas ao ambiente de desenvolvimento.

Fique a vontade para explorar as métricas.

# Atividades

Crie uma pasta para cada seção de aquecimento e dashboard RED

## Aquecimento

Você deve criar um dashboard no Grafana para visualizar as seguintes métricas:

1. Exiba quantas requisições estão sendo feitas por segundo.
2. Exiba quantas requisições estão sendo feitas por segundo por classe de status http (1XX, 2XX, 3XX, 4XX, 5XX).
3. Exiba quantas requisições diferentes da classe 2XX estão sendo feitas.
4. Exiba quão a porcentagem do tráfego total está falhando na última hora.
5. Exiba quais métodos http(get, post, put, update, delete) os erros estão acontecendo.

# Construa o Dashoboard RED

Um dashboard RED deve exibir:

- Rate: Número de requisições por segundo
- Errors: Número das requisições que estão falhando
- Duration: A quantidade de tempo de resposta das requisições

Você deve criar uma linhas com os gráficos necessários para o RED para três partes do sistema: Load Balance, App, DataBase.
