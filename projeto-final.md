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
2. Exiba quantas requisições estão sendo feitas por segundo por classe de status http (1.., 2.., 3.., 4.., 5..).
3. Exiba quantas requisições diferentes da classe 2XX estão sendo feitas.
4. Exiba quão a porcentagem do tráfego total está falhando na última hora.
5. Exiba quais métodos http(get, post, put, update, delete) os erros estão acontecendo.

# Construa o Dashboard RED

Um dashboard RED deve exibir:

- Rate: Número de requisições por segundo
- Errors: Número das requisições que estão falhando
- Duration: A quantidade de tempo de resposta das requisições

Você deve criar uma linhas com os gráficos necessários para o RED para três partes do sistema: Load Balance, App, DataBase.

# Alertas

Crie alguns alertas para serem notificados em um canal de texto do discord ou outra ferramenta que deseje. Relate na descrição do alerta informações para que a equipe possa entender os motivos de estar sendo alertados.

# Compartilhamento do Dashboard

Exporte o diagrama em versão snapshot publicamente para que qualquer um na internet observe a qualidade dos serviços da Damasceno Inc.
