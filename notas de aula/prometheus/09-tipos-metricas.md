\[00:00\] Vamos dar sequência no nosso curso. Na última aula, nós falamos sobre a anatomia de uma métrica e você entendeu o que é o _metric name_, o que é o _label_, o que é o _sample_, o que é um _instant vector_, um _range vector_ e um dado _Scalar_.

\[00:26\] Nós abordamos todos esses assuntos e, para complementar isso, é de suma importância que você entenda quais são os tipos de métricas que o Prometheus trabalha.

\[00:37\] Eu vou recorrer à documentação oficial. Para você chegar na documentação oficial, é bem simples, é só ir em “_Help_” no painel superior do Prometheus, você abre em outra aba e você vai estar na documentação.

\[00:50\] Na documentação, você pesquisa por “metric types” e problema resolvido, bem simples, você vai cair exatamente nessa página que eu estou. O Prometheus trabalha com quatro tipos de métrica.

\[01:07\] Tem o tipo “_Counter_”, “_Gauge_”, “_Histogram_” e “_Summary_”. Vamos falar primeiro do “_Counter_". A métrica do tipo _counter_ é uma métrica que é crescente e sempre será incrementada.

\[01:25\] Então, é uma métrica cumulativa. Qual é a desvantagem que temos no _counter_? Se a sua aplicação for reinicializada, essa métrica vai zerar, só que ela vai zerar dentro do seu tempo atual de execução da aplicação.

\[01:46\] Você vai conseguir consultar os resultados anteriores que estão no TSDB em outra série temporal, sem problema, porém, o valor atual da métrica vai ser zerado.

\[01:59\] Não é aconselhável que você usar o tipo de métrica _counter_ para trabalhar com valores que vão variar, que vão subir ou descer. Sempre com valores incrementais.

\[02:14\] Se formos olhar o tipo _counter_ no _endpoint_ de métricas, você vai ver que tem diversos exemplos. Temos aqui a métrica personalizada que nós criamos, `auth_user_success_total`. Posso colocar essa métrica no Prometheus e ela sempre vai ser incrementada.

\[02:40\] Eu posso procurar também o erro, nós também criamos uma métrica para a condição de erro, está aí, `auth_user_error_total`. É legal entender por que nós trabalhamos com o _counter_, já que em um momento vamos ter usuários logados e em outro não.

\[02:58\] Nós trabalhamos com essa métrica porque é interessante você ter um histórico e entender, em um período específico, quantos usuários fizeram _login_, em um _range_ específico de tempo.

\[03:13\] No momento atual da nossa aplicação, nós vamos utilizar uma lógica através de alguns operadores e funções que vão trazer para nós o valor exato do momento da consulta.

\[03:23\] O _counter_ é justificado para esse uso que nós fizemos por conta de você poder ter uma avaliação de uma janela grande de tempo e entender qual era a média de autenticações que você teve em um período tal e quanto você está tendo hoje.

\[03:42\] Esse seria o motivo de termos o tipo de _counter_ para autenticações e erros de autenticação.

\[03:51\] Se eu procurar uma métrica, por exemplo, a do _log_, também é um tipo _counter_ o `logback_events_total`. É legal porque, se você procurar, o próprio Prometheus vai dizer para você qual o tipo da métrica.

\[04:06\] Então, estamos conversados sobre o que é um _counter_. Se você olhar aqui, ele vai contando e fazendo a divisão pelo _log level_, temos aqui `debug`, `error`, `info`, `trace` e `warn`. Ao todo, são cinco níveis de _log_ que conseguimos ter e ele vai contando os eventos que se categorizam sobre o nível de _log_ específico em uma série temporal específica.

\[04:36\] Já entendemos o que é um tipo de métrica _counter_, vamos falar sobre o "_Gauge_". Lembra que eu falei que o _counter_ não deve ser utilizado se a sua métrica for variar, se ela vai ter um valor inferior e depois superior, se ela vai subir e descer?

\[04:54\] O _gauge_ já trabalha nesse ponto, ele é direcionado para valores que vão variar no decorrer da execução do seu sistema. Logicamente, o _gauge_ é uma métrica que se encaixa muito bem para que possamos mensurar consumo de CPU, consumo de memória, número concorrente de requisições em um período de tempo específico e fazer comparações.

\[05:25\] A utilização do _gauge_ é para valores variáveis. É bem simples. Se dermos uma procurada aqui, “_gauge_”, temos, por exemplo, o estado de _threads_ da JVM. Por exemplo, se eu fizer essa consulta: `jvm_threads_states_threads{application="app-forum-api",state="runnable"}`. Vou tirar o `state=runnable` porque estamos pegando as métricas que estão em estado _runnable_ – ao todo, são `7`.

\[06:00\] Se mudarmos aqui, vou procurar por outro _state_, vou colocar `timed-waiting`, eu tenho `8`. Esses valores vão ser modificados conforme a aplicação for consumida, conforme ela tiver chamadas de funções e esse tipo de coisa.

\[06:19\] Se procurarmos por outra, eu tenho aqui conexões da JDBC em estado `idle`. Deixa eu encontrar outra, aqui também é sobre _thread_, _buffer_. Está aqui, contagem de CPU. `system_cpu_counter`, essa métrica eu não acho interessante porque ela pega o número de núcleos de um CPU, então é uma coisa que, no nosso caso, não vamos ter aplicabilidade.

\[06:47\] Agora aqui, uma métrica bem legal é a utilização do CPU para o processo que a JVM está executando: `process_cpu_usage`. Esse valor vai subir, vai descer, vai variar conforme a execução da nossa aplicação.

\[07:07\] Até aqui, acho que está tranquilo, são dois tipos de métricas bem simples: o _counter_, o valor incremental – se a aplicação for inicializada, ele é zerado; e o _gauge_, uma métrica que vai variar, vai sofrer incremento e decremento no decorrer da execução do sistema.

\[07:28\] Aí chegamos em uma métrica mais complicada, do tipo "_Histogram_". O _hstogram_ traz observações que estão mais relacionadas à duração e ao tamanho de resposta.

\[07:45\] Ele tem uma configuração de alocação de séries temporais em _buckets_. Esses _buckets_ vão corresponder a algumas regras que vamos definir. No nosso caso, nós já definimos, porque criamos uma métrica do tipo _histogram_ quando trabalhamos no _application properties_ e definimos aquela métrica de SLA diretamente no `application.prod.properties` da aplicação.

\[08:15\] Existem N _buckets_, cada _bucket_ tem uma configuração que nós setamos lá no _application properties_, e ele está relacionado à duração de uma requisição e ao tempo de resposta que eu tenho.

\[08:30\] Além disso, o _histogram_ traz para nós a soma total dos eventos observados em questão de tempo – quantos segundos, por exemplo – e traz também a contagem de todos os eventos.

\[08:44\] Para entendermos um pouco melhor isso, podemos procurar aqui `http_server_requests_seconds histogram`. Abaixo dele, temos os _buckets_, você vai ver as linhas do `bucket`, e você vai ver `count` e `sum`.

\[09:06\] Vou pegar uma específica, pode ser essa mesma, `http`. No caso, estou distinguindo por _label_. A métrica é a mesma, o que muda são os _labels_. Além de ter os _labels_ distintos para um _endpoint_ específico, eu tenho o _bucket_ definido em uma regra bem lógica. Você vai entendê-la agora.

\[09:35\] Eu copiei a métrica, que é `http_server_requests_seconds_bucket` e aqui eu tenho todos esses _labels_. Eu não preciso da maioria deles, eu posso retirar toda essa informação e deixar só `status="200",uri="/topicos/(id)"`, aí tem essa regra que é uma condição, `le`.

\[10:06\] “_Less or equal_”, “menor ou igual”. Se olharmos para esse valor aqui, `0.05`, temos que entender que esse valor está em milissegundos, então tenho 50 milissegundos. Se eu executar (`http_server_requests_seconds_bucket{status="200",uri="/topicos/(id)",le="0.05"}`), ele trouxe “409”, então tenho 409 requisições nesse momento, para “topicos/id”, que estão menores ou iguais a 50 milissegundos.

\[10:36\] Aí eu posso andar nesse valor. Colocamos `le="0.1"`, a 100 milissegundos tem mais, são 411; a 200 milissegundos, 412; a 300, também “412”; a 500, do mesmo jeito; e com 1 segundo, `le="1.0"`, temos até 1 segundo, 415 requisições.

\[11:06\] Se eu tirar esse `le=”1.0”` e executar, ele vai trazer todas as séries temporais que eu tenho relacionadas aos _buckets_. Aqui é acima de 1 segundo, é infinito e além, esse `+inf`, é infinito, é acima de 1 segundo.

\[11:32\] Aqui, temos toda essa configuração retornando para nós. Então, uma métrica do tipo _histogram_ vai nos auxiliar a fazer esse tipo de medição que é importantíssima para entendermos o tempo de resposta da nossa API e, principalmente, se estamos cumprindo o nosso SLA.

\[11:53\] Na verdade, se estamos cumprindo com o nosso SLO, que é o nosso objetivo de nível de serviço que vai ser mensurado com base no nosso SLA. Aqui, entraria o nosso indicador do nosso nível de serviço que, de fato, é a métrica.

\[12:08\] Voltando, eu posso fazer uma modificação, vou fazer direto, posso colocar a soma, `sum`, qual a soma de todos os segundos que eu tenho dessas requisições: `http_server_requests_seconds_sum{status="200",uri="/topicos/(id)"}`.

\[12:23\] Está aqui, trouxe um valor que é difícil de entender sem usar uma função. E posso trazer a contagem, o número total, sem distinções relacionadas a _buckets_ (`http_server_requests_seconds_count{status="200",uri="/topicos/(id)"}`). Tenho 432 requisições.

\[12:41\] Esse é um tipo de métrica _histogram_. Vamos para o último tipo de métrica, que é o "_Summary_". O _summary_ é uma métrica muito similar ao _histogram_ – só um detalhe, voltando no _histogram_, antes de voltar no _summary_, só para finalizar o _histogram_ de forma correta.

\[13:04\] O _histogram_ também é uma métrica cumulativa. Além de ela ser cumulativa, ela tem uma função que é bem interessante utilizarmos, que é o `histogram_quantile`, que trabalha com _quantiles_, então você consegue fazer especificações de _quantiles_ através dessa função e trabalhar bem com ela. Vamos fazer isso mais a frente.

\[13:27\] Voltando para o _summary_. Como eu tinha dito, o _summary_ é uma métrica muito similar ao _histogram_, a própria documentação diz isso, só que ele é mais usualmente utilizado para você ter a duração de uma requisição e o tamanho da resposta que você tem para uma requisição.

\[13:49\] Além disso, você consegue ter tanto o somatório quanto a contagem – o somatório de segundos da métrica e a contagem total de eventos que foram captados na métrica.

\[14:05\] Uma coisa bem legal é que você também pode calcular _quantiles_ configuráveis de uma forma customizada. Você consegue fazer isso dentro de uma janela de tempo e, para você entender melhor desse assunto, já que ele é um pouco complexo e não tem como esgotá-lo em uma aula, eu vou deixar essa página da documentação do Prometheus.

\[14:31\] Entrando nela, é legal você abrir esse _link_ “_Histograms and summaries_” para você ter uma explicação mais detalhada sobre a utilização de _quantiles_ dentro da composição de uma métrica.

\[14:45\] Para você poder fazer uma consulta que seja mais específica e traga o resultado que você precisa, de uma forma que realmente agregue valor para a sua instrumentação e para a sua composição de _dashboard_.

\[15:05\] Esse era o assunto sobre os tipos de métricas que eu tinha para trazer nessa aula, nós vamos ter, na próxima aula, a abordagem a funções e operadores para encerrarmos a parte do PromQL e continuarmos aprofundando nele com uma prática já relacionada à criação de _dashboards_.

\[15:28\] No capítulo seguinte, já vamos estar trabalhando com o Grafana, então já vamos ter uma pegada diferente e vamos acabar aprofundando na linguagem na hora de compor o _dashboard_.

\[15:42\] Então, é isso. Te vejo na próxima aula em que vamos falar sobre funções e operadores. Até mais.