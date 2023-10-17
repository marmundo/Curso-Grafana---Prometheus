\[00:00\] Vamos dar sequência no nosso curso. Agora vamos criar mais dois painéis. O primeiro vai ser o estado e o número das conexões com a base de dados.

\[00:18\] Vou adicionar um painel e a métrica que vamos trabalhar aqui é a `hikaricp_connections_active`, essa vai ser a primeira métrica. Esse painel vai ter três métricas ao todo.

\[00:36\] Aqui, vou trabalhar com os _labels_ `{application=”$application”, instance=”$instance”, job=”app-forum-api”` e, além disso, vamos configurar o nosso `pool=”$pool”}`.

\[01:20\] É legal você olhar para a parte superior esquerda porque você consegue verificar, na parte esquerda superior, as variáveis junto com o _labels_. Temos essa métrica e essa métrica traz, basicamente, o número de conexões que estão em estado ativo.

\[01:48\] Temos a primeira, aqui, vou colocar como legenda "_active_", esse é o estado ativo. Vou copiar e vamos adicionar uma nova _query_ que, ao invés de olhar para o _active_, vai olhar para o _idle_, `hikaricp_connections_idle`.

\[02:17\] Então, é _idle_, já temos as conexões em estado _idle_, em estado de espera. Vou colocar como "_idle_" a legenda e vamos adicionar outra _query_ que vai ser o estado pendente, o "pending".

\[02:40\] Todas essas métricas existem na JVM. Já entrou o `pending` em estado pendente, temos três métricas sendo "plotadas" nesse gráfico, três séries temporais distintas.

\[02:58\] Vou manter o “Time series”, vou colocar o título como “CONNECTION STATE” e descrição como “Estado das conexões com o database”.

\[03:23\] Descendo, vou colocar a legenda em um formato tabular. Posso colocá-la do lado direito, fica legal também, vamos fazer uma experiência com isso. Nos valores da legenda, vou colocar o mínimo, o máximo, o último e o total – apesar de o total ser totalmente irrelevante para nós porque ele só vai fazer um contador.

\[04:03\] Vou até tirar o total para não gerar confusão. Então, mínimo, máximo e último. Aqui, vou trabalhar com a opacidade, vou deixar em 10. Eu gosto dessa configuração, você não precisa fazer assim. Se você achar outro jeito mais interessante, tudo bem, isso é só o _layout_ mesmo, o que é importa é a métrica e o gráfico sendo "plotado".

\[04:28\] Aqui, vou colocar uma opacidade no gradiente; vou tirar os pontos, não gosto dos pontos; não vou trabalhar no “Eixo X” ou “Eixo Y”; a unidade não vai fazer diferença, vou deixar “_Short_” porque são números inteiros.

\[04:54\] Não vou trabalhar com “_Threshold_”, é um gráfico. Está feito esse painel. Ele é bem interessante para nós. Tenho o “CONNECTION STATE” criado, vou descê-lo e diminuí-lo. Está bagunçado, mas já vamos corrigir, vai ficar legal.

![Gráfico "*Connection state*". O eixo X mostra a passagem do tempo, de minuto em minuto, o eixo Y apresenta os valores 0, 5 e 10. A linha amarela (que representa "*idle*") é estável no número 10, exceto uma leve queda perto de 23:25. A linha verde ("*active*") está estável em 0, exceto por um leve aumento, também perto de 23:21. A linha azul ("*pending*") permanece no 0 por todo o período mostrado no gráfico.](https://caelum-online-public.s3.amazonaws.com/2522-monitoramento/Transcri%C3%A7%C3%A3o/Aula+02/grafana_03.png)

\[05:37\] Está o “CONNECTION STATE”, vamos criar mais um painel. Vou adicionar mais um painel e esse painel vai ser o “Connection Timeout”, vai ser o número de conexões que estão em _timeout_.

\[05:56\] Vou colocar o `hikaricp_connections_timeout_total`, essa métrica. Vou trabalhar com `{application=”$application”, instance=”$instance”, job=”app-forum-api”`.

\[06:28\] É isso, não tem muito o que fazer aqui, e o _pool_, não posso me esquecer, que é a nossa variável `pool=”$pool”}`. Eu tenho essa informação, só que vou trabalhar novamente com um “_Stat_” aqui.

\[06:51\] Vou colocar “DB TIMEOUT” como título e, para descrição, “Conexões com o database em timeout”. Você pode colocar uma descrição melhor se você quiser, não tem problema.

\[07:24\] Aqui, é um contador. Estamos pegando o `timeout_total`, ele traz o total para nós, isso não é legal, então vamos fazer uma mudança nisso, vou colocar um _range time_ de `[1m]` e vou trabalhar com o `increase`.

\[07:47\] Só para pegar a taxa de crescimento dele por minuto. Vai estar “0” porque não estamos com o _timeout_ em nenhuma conexão. Vamos trabalhar dessa forma.

\[08:02\] Aqui, em “_Color mode_”, vou tirar o “_Graph_”; em “Unidade”, novamente estamos trabalhando com o número inteiro, então não tem o que mudar. Tendo 5 conexões de _timeout_ em um minuto – até menos –, nós podemos considerar que temos um problema.

\[08:32\] Vou deixar 5 aqui e está certo. Está feito esse “DB Timeout”, o nome ficou estranho, vou tentar aumentar, “DB CONNECTION TIMEOUT”.

\[08:54\] Voltando aqui, tenho esse painel que foi criado. Posso trabalhar com ele, agora vou descer, posso diminuir um pouco aqui para ficar mais interessante, só para deixarmos o _layout_ mais enxuto.

![*Layout* com todos os gráficos criados dentro de API BASIC. Temos "Uptime", "Start Time", "Users Logged", "Auth Errors", "JDBC pool", "DB connection timeout", "Connection state" e "Warn and Error log".](https://caelum-online-public.s3.amazonaws.com/2522-monitoramento/Transcri%C3%A7%C3%A3o/Aula+02/Imagens/grafana_04.png)

\[09:30\] Tenho o meu “ERROR LOG” aqui, vou editá-lo e vou mudar a disposição das estatísticas dele. Vamos agora colocar a prova isso. Vou parar o MySQL e vou causar o caos completo porque vou derrubar o Redis. Vamos ver o que vai acontecer.

\[10:17\] O “JDBC Pool” caiu na hora, essa métrica é alimentada por _scrape_. Como ela é um _counter_, ele traz na hora a informação para nós. “DB Connection Timeout” também vai ser alimentado, mas está por minuto, então é só nós esperarmos um pouco para ver a mudança dele.

\[10:35\] Aqui, já começamos a ver que as conexões que estavam em _idle_ já baixaram, as pendentes já tiveram um crescimento – tem uma pendente – e agora o “DB Connection Timeout” já começa a ser alterado.

\[10:54\] Vou até fazer uma edição nele, na parte de decimal, vou deixar como “0” só para eu ter um número mais interessante a ser exibido e não gerar dúvida para vocês.

\[11:10\] Então, já está com duas conexões em “Timeout” e já temos os _warns_ com 19, o total de _warns_ que tivemos na aplicação até agora, desde a subida, foi 73; temos 24 erros; temos “Auth errors” 0, porque ninguém consegue tentar autenticar; nenhum usuário logado; e o _pool_ de conexões JDBC está lá embaixo.

\[11:41\] Está aqui a prova de que a nossa métrica funciona bem. Só mais um ajuste em “DB Connection Timeout”, vou no “_Threshold_”, vou subi-lo, já sei que, se eu tiver “2” conexões ganhando _timeout_, eu estou com problema dentro desse nosso cenário que é um laboratório.

\[12:03\] Aqui é mais para entendermos e termos o primeiro contato com a composição de um _dashboard_. Vou agora subir a aplicação, acho que está de bom tamanho o nosso teste, já validamos, está tudo certo.

\[12:19\] Vou começar subindo o `mysql` e agora vou subir o `redis`. Pronto, agora tudo vai voltar ao normal, a aplicação vai se restabelecer e nós encerramos esse capítulo por aqui, com a composição desses primeiros painéis.

\[12:44\] Fizemos o _basic_, mas, no próximo capítulo, já vamos estar lidando com métricas que correspondem à experiência do usuário final. Vamos falar um pouco de _golden signals_, vamos falar de uma metodologia chamada RED e de outra metodologia chamada USE, mas o nosso foco será na metodologia RED que é direcionada à experiência do usuário final.

\[13:13\] Então, é isso, nos vemos na próxima aula.
