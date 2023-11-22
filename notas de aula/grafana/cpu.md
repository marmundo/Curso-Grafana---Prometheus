\[00:00\] Vamos dar sequência ao nosso curso. Nessa aula, vamos falar de CPU. Vamos criar dois painéis relacionados ao uso de CPU.

\[00:13\] Vamos começar criando um painel que vamos conseguir mensurar o uso de CPU. A métrica que vamos utilizar é a `system_cpu_usage`, “utilização de CPU”. No automático, ele já traz para nós um retorno interessante, já "plota" uma métrica.

\[00:37\] Vou colocar os nossos _labels_ `{application=”$application”, instance=”$instance”, job=”app-forum-api”}`. Além disso, não tem mais o que colocar nessa métrica, ela basicamente vai trazer para nós, em tempo real, em _scrape time_, o tempo de cada consulta, vai trazer o valor que precisamos, não vamos trabalhar com mais nada dentro dela.

\[01:16\] Além disso, vamos colocar outra métrica aqui embaixo, na legenda, “System CPU usage”. Vamos adicionar outra _query_ que vai trazer o `process_cpu_usage`.

\[01:58\] Aqui, vamos trabalhar da mesma forma. Vamos colocar os _labels_ `{application=”$application”, instance=”$instance”, job=”app-forum-api”}`. Está certo, não tem mais o que fazer nessa métrica.

\[02:26\] Vou colocar aqui “Proccess CPU Usage” na legenda. Tendo feito isso, vamos partir para a configuração da visualização que vamos ter.

\[02:55\] Vou manter em formato de “_Time series_”; o título, vamos chamar de “CPU”; na descrição, “Utilização de CPU”.

\[03:23\] Na parte de legenda, vou colocar em forma tabular, vou manter embaixo, vamos colocar valores interessantes em termos de unidade. Vamos colocar o valor mínimo, o máximo, a média, o último valor não nulo e o total.

\[04:05\] Trouxe um dado interessante para nós, ficou legal. Antes de mexer na unidade, vou configurar a opacidade, vou tirar a pontuação dele.

\[04:33\] Na unidade, percentual não vai ficar bem, até porque não estamos fazendo cálculo nenhum; o tipo de visualização é “_Short_” mesmo; e não precisa colocar valor mínimo, máximo ou _threshold_.

\[04:55\] Vou colocar um nome mais requintado, “CPU UTILIZATION”, “Utilização de CPU”. Temos a nossa utilização de CPU. Ficou um painel bem grande, deixa eu ver se o diminuo um pouco.

\[05:30\] Está feito. Deixa eu abaixá-lo um pouco mais e, agora sim, está no tamanho legal. Ficou enorme o “Heap”. Está certo.

![Painel *CPU Utilization*. O eixo x mostra a passagem de tempo, de 1 em 1 minuto. O eixo y mostra os valores 0, 0.200, 0.400 e 0.600. A linha verde (referente a *system CPU usage*) oscila entre 0.400 e 0.600. A linha amarela (*process CPU usage*) é relativamente estável, próximo de 0.](https://caelum-online-public.s3.amazonaws.com/2522-monitoramento/Transcri%C3%A7%C3%A3o/Aula+03/Imagens/grafana_10.png)

\[05:48\] Vamos partir para a configuração do nosso segundo painel. Vamos adicionar um novo painel e agora vamos trabalhar com a carga de CPU, a carga de sistema.

\[06:00\] Vamos trabalhar com o `system_load_average_1m`. Essa métrica é legal porque já pega o último minuto. Vou trabalhar com os nossos _labels_ `{application=”$application”, instance=”$instance”, job=”app-forum-api”}`.

\[06:36\] Está feito, não tem muito o que fazer nessa métrica. Na legenda, vou colocar “Load average \[1m\]”.

\[07:01\] Vou adicionar mais uma métrica só para ficar mais bonito, ela não vai fazer nenhuma diferença no nosso caso. É a `system_cpu_count`, é a contagem de CPUs que possuímos.

\[07:20\] Vamos colocar os _labels_ – essa contagem de CPUs inevitavelmente vai acabar pegando o número de CPUs do seu _docker host_, mas você pode estar em uma ocasião e fazer uma manipulação para isso ficar diferente.

\[07:35\] `{application=”$application”, instance=”$instance”, job=”app-forum-api”}`. Está feito. Na legenda, vou colocar “CPU core size”. É o número de CPUs que possuímos.

\[08:08\] O nome que vamos dar para esse painel é “LOAD AVERAGE”. Na descrição, vou colocar “Média de uso de CPU”. A legenda vou colocar tabular, vou mantê-la embaixo.

\[08:33\] Os valores, vamos trabalhar com mínimo, máximo, médio, último valor não nulo e total. Vou trabalhar no _layout_ do painel, então vou colocar opacidade, trabalhar com gradiente, tirar os pontos.

\[09:04\] Está tudo certo, não tem mais o que mudar. A nossa unidade vou manter como “_Short_”, a escola linear mesmo – não mexemos na escala até hoje porque não foi necessário.

\[09:22\] Está feito, está certo. Já tem aqui o “Load Average”. Conseguimos encaixá-lo aqui, ficou bem interessante. O que vamos fazer agora é uma modificação no "CPU UTILZATION" porque ficou muito grande.

\[09:50\] Vou mover para cá, movi a tabela para a direita, vou tirar o médio – mínimo, máximo, o último coletado –, vou tirar o total também.

\[10:17\] Posso diminuí-lo um pouco. No “Load Average”, vou fazer a mesma coisa para economizarmos o tamanho do _dash_ em si, não ocupar tanto espaço. O último coletado até que é legal manter, o total é que não vai fazer muita diferença aqui - vou tirar.

\[11:12\] Acho que assim ficou mais enxuto para nós. Agora, para finalizar, vou criar uma _row_ para alocar isso e vou ter a audácia de colocar que é a “API USE”.

\[11:31\] Não tratamos o USE a fundo porque não era o nosso objetivo, teríamos que olhar para muitos outros aspectos para conseguirmos abranger a importância e o alcance do método USE.

\[11:53\] Teríamos que olhar para IO de disco, teríamos que olhar para a parte de tráfego de rede mais a fundo, tem diversos pontos que pegaríamos com o USE. Então, não coube dentro desse conteúdo, porque o nosso foco é olhar para a experiência do usuário final utilizando o RED.

\[12:12\] O resultado que temos aqui da composição que fizemos nesse _dashboard_ é o “API BASIC”, o “API USE” e o “RED”, que é a parte mais importante para nós até dado momento, e vai seguir assim até a conclusão.

\[12:35\] Encerramos esse capítulo aqui. No próximo capítulo, já vamos tratar dos alertas. Nos vemos no próximo capítulo.
