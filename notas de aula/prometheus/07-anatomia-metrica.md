\[00:00\] Vamos dar sequência no nosso curso. Agora que já temos o consumidor da nossa API, vamos conseguir ter uma visibilidade melhor sobre as métricas, mas, para que possamos realmente fazer bom uso do que estamos fazendo, é muito importante que você entenda como é uma métrica para o Prometheus.

\[00:26\] No _browser_, vamos no “localhost/metrics”, vou atualizar, você vai ver que muita métrica foi gerada por conta daquele `client` que nós rodamos. Inclusive, alguns erros 500 vão se detectados, porque o _script_ começou a ser executado pelo `client` antes de o MySQL estar realmente atendendo às requisições, então gerou uma quantidade de erros 500 em `/topicos`.

\[01:03\] Foi só durante a subida, agora está certo. Você vai notar o seguinte – vou diminuir para você identificar cada métrica em uma linha única –, os valores estão aumentando porque a aplicação está sendo consumida.

\[01:25\] Aqui tem um `/topicos/{id}`. Se descermos um pouco, vamos ver que `/topicos` está aqui; temos também as métricas de usuários, então, até dado momento, eu tenho 70 autenticações com sucesso.

\[01:47\] Tenho também autenticações com erro, 38 até agora. Voltando ao que interessa, se olharmos para uma métrica, vou procurar pela métrica de _log_, que talvez seja a mais simples de explicar no momento.

\[02:08\] Vamos pegar essa métrica aqui, `logback_events_total`. Toda métrica tem três componentes básicos. O primeiro é o _metric name_, é o nome da métrica. Aqui, o _metric name_ que nós temos é o `logback_events_total`. Se eu executo essa consulta no Prometheus, eu tenho alguns retornos.

\[02:34\] Se eu pegar um desses retornos específicos - o primeiro, por exemplo - e fazer essa consulta, eu tenho só o retorno dessa consulta específica com esses atributos. Vamos entender o que são esses atributos e o que é o retorno da consulta.

\[02:56\] Então, tenho o _metric name_, que nesse caso é o `logback_events_total`, e logo após o _metric name_ tenho _labels_, rótulos. Esses rótulos vão identificar qual é a série temporal que você quer consultar.

\[03:15\] Até agora vimos duas entidades aqui: _metric name_ e _labels_. Podem existir vários _labels_ configurados, eles vão estar nessa configuração similar a uma variável, de chave-valor, `{application=”app-forum-api”,instance="app-forum-api:8080",job-"app-forum-api",level="debug"}`.

\[03:39\] À direita dos _labels_, eu tenho o _sample_, que é o resultado dessa consulta, que está aqui, `0`. Se eu mudar alguns desses _labels_, por exemplo, eu não quero olhar o _level_ `debug` do _log_, eu quero olhar o `info`: `logback_events_total{application=”app-forum-api”,instance="app-forum-api:8080",job-"app-forum-api",level="info"}`. Vamos fazer a consulta dele, eu tenho 43 como retorno, meu _sample_ como 43.

\[04:04\] Já entendemos que existe _metric name_, que existe _label_ e que existe o _sample_, que é o resultado da consulta sobre aquela métrica com aquele _metric name_ e aqueles _labels_ específicos.

\[04:21\] Isso está fácil de entender. Agora nós entramos no ponto de quais são os tipos de dados que uma métrica pode ter – qual tipo de dado é aquela métrica? No Prometheus, temos quatro tipos de dados.

\[04:40\] Temos o _instant vector_, que é um vetor instantâneo; temos o _range vector_, que é um vetor de uma série temporal; temos um dado do tipo _Scalar_, que é um _float_ simples, um ponto flutuante; e temos o _spring_, que basicamente não é utilizado, a própria documentação do Prometheus diz isso, que não é comumente utilizado.

\[05:10\] Vamos só focar nos três tipos de dados mais utilizados no Prometheus e são eles que vamos utilizar até o último momento desse curso. O que é um _instant vector_? É um vetor instantâneo, esse vetor está sendo exibido agora para vocês na tela, ao executar `logback_events_total`.

\[05:30\] Quando eu olho para essa métrica, `logback_events_total`, ela me retorna um vetor. Esse vetor está aqui embaixo, cada uma dessas linhas seria um índice desse vetor. Eu teria o índice 0, 1, 2, 3 e 4. Vamos simplificar dessa maneira.

\[05:52\] Cada um desses elementos que estão dentro desse vetor é uma série temporal. Eu tenho aqui 5 séries temporais que estão armazenadas nessa métrica `logback_events_total` e, quando eu faço uma consulta para essa métrica, esse vetor retorna para mim.

\[06:20\] O que gera esses vetores e como eu faço a distinção entre cada um? Através de _levels_, são os _labels_ que vão fazer essa distinção. Se olharmos para essa série temporal específica, vou pegar novamente o `debug`, você vai notar o seguinte.

\[06:45\] Qual é a diferença de uma para outra? É o _level_. Essa métrica está relacionada ao _log_, e o _log_ tem níveis de _logs_ específicos que a JVM consegue externalizar através do Actuator e o Prometheus acaba fazendo a interface através do Micrometer.

\[07:07\] Nós conseguimos ter acesso à essa informação através de uma métrica com um _label_ de _level_ distinto. Então, tivemos, na subida da aplicação, uma quantidade de _info_, uma quantidade de erros e uma quantidade de _warnings_. Não tivemos _log level_ de _debug_ aqui, nem de _trace_.

\[07:30\] Isso é um _instant vector_, um vetor de tempo. Se você olhar em “_Evaluation time_”, você vai ver o momento da consulta. Então, falamos sobre o primeiro tipo de dado que é o _instant vector_.

\[07:48\] Agora, vamos falar sobre o _range vector_. Para chegarmos nesse ponto do _range vector_, eu vou tirar tudo e colocar 1 minuto,`[1m]`, entre colchetes - `logback_events_total[1m]`. A partir do momento que eu faço isso, estou trabalhando com o _range vector_.

\[08:12\] Notem que teve uma transformação aqui, eu estou olhando justamente para esse _timestamp_, posso tirá-lo e refazer a consulta, vai dar na mesma. O que estou trazendo é o último minuto dentro desse _timestamp_.

\[08:32\] Esse foi o _timestamp_ de execução da consulta, eu quero o último minuto. No último minuto, eu tenho essas informações que voltaram. Notem que o _range vector_ não seria uma matriz, não temos um vetor multidimensional, mas temos, em cada série temporal, um “vetor” que traz um valor específico a cada _scrape time_ do Prometheus.

\[09:08\] Vamos lembrar a nossa configuração. Já vimos isso em uma aula anterior. Se eu abrir aqui e for em “_Configuration_”, você vai ver que o nosso _job_ `app-forum-api` tem o `scrape` de `5s`. Então, a cada 5 segundos o Prometheus vai lá e bate no _endpoint_ para trazer as métricas.

\[09:34\] Justamente aqui, em 1 minuto, nós tivemos essa quantidade aqui, 12 consultas, cada uma a 5 segundos, o que equivale a 60 segundos de trabalho do Prometheus buscando métricas.

\[09:56\] Alguns estão com valores e outros não, não está dando para pegarmos uma mudança aqui nesses valores, mas normalmente vamos enxergar mudanças.

\[10:04\] Aqui tem uma notação meio estranha, que é o _unix timestamp_. Se você quiser entender o que é isso, no Linux é fácil – se você estiver no Windows, deve ter uma forma fácil de você fazer no PowerShell, ou você vai no _browser_ e dá uma "googlada" “unix timestamp” que você vai encontrar um jeito de converter.

\[10:23\] Vou te mostrar, só para você entender um pouco mais. Se eu rodar um `date -d` e colocar o _timestamp_, o Linux converte para mim e eu vejo que essa consulta rodou às 23:39, está certo, com o horário configurado.

\[10:46\] Se eu quiser ir um pouco mais além, só para confirmar para você, eu posso declarar uma variável que vai ser um `array`, e vou colocar quatro valores para ficar mais simples. Tenho um, dois, três e, por fim, o quarto.

\[11:26\] Declarei esse `array`, se eu fizer um laço, vou fazer `for i in` e vou iterar esse `array`. Se você não souber Shell, não tem problema, isso é só para você ter a noção de como isso está vinculado ao _scrape time_.

\[11:59\] Vou fazer um laço, um `for` que vai varrer esse _array_, vai varrer cada um desses valores, temos quatro valores, índice 0, 1, 2 e 3. A cada iteração, ele vai encapsular na variável `i`, em um _timestamp_ específico, e vai converter através do _date_.

\[12:18\] Está aí. se você notar, a cada cinco segundos, `02`, `07`, `12` e `17`, ele trouxe um valor para mim, ele fez um _scrape_ e trouxe. Então, quando falamos em _range vector_, estamos falando de um _range_ de tempo dentro de uma série temporal.

\[12:44\] Eu posso facilitar um pouco isso, posso olhar um intervalo específico? Posso, através de uma _subquery_. Eu quero olhar os últimos 5 minutos e quero ver apenas o último minuto. Está aqui, consigo fazer isso: `logback_events_total[5m:1m]`.

\[13:02\] Um minuto ficou muita coisa, quero olhar os 30 segundos. Também consigo: `logback_events_total[5m:30s]`. Então, dentro dos últimos 5 minutos, eu olhei os 30 segundos.

\[13:18\] É bem simples de se trabalhar, vamos ter funções que vamos ver mais a frente que vão aproveitar melhor o _range vector_. Tem um detalhe, estamos vendo uma saída que é tabulada, e se quisermos ir para gráfico?

\[13:34\] Não é possível. Se você ler isso, você vai ver que “houve um erro executando a consulta, o tipo ‘range vector’ é inválido para esse tipo de consulta, tente com um _Scalar_ ou um vetor instantâneo”.

\[13:51\] Isso significa o quê? Que eu não posso formar um gráfico no Prometheus quando eu tiver uma saída que possui mais de um valor. Ou ela tem que ser um _instant vector_ ou um dado Scalar. O dado _Scalar_, só lembrando, é um _float_.

\[14:10\] Vou executar dessa maneira, `logback_events_total`. Eu tive esse retorno, ele formou um gráfico para mim, está bem simples, mas formou o gráfico. Aqui eu tenho uma consulta que traz para mim um _instant vector_. Sendo um _instant vector_ ou sendo um dado _Scalar_, eu consigo retorno.

\[14:40\] Voltando, o que faltou é falarmos sobre o _Scalar_. O dado _Scalar_ é, basicamente, um _float_ que vou encontrar. Posso encontrar qualquer um aqui, por exemplo, deixa eu olhar para alguma coisa de conexões.

\[15:12\] Tenho um dado que vai me retornar um valor que é um _float_ simples e que vai poder ser visualizado. Se eu for para o modo gráfico, eu consigo enxergar também um gráfico.

\[15:35\] Não vamos falar de _string_ porque isso não cabe dentro do nosso conteúdo e dificilmente você vai ver algum caso de uso para _string_ envolvendo o Prometheus. Isso pode ser encontrado na própria documentação.

\[15:51\] Se procurarmos aqui – deixa eu ver no “_Help_”, que já vem direto para cá –, se eu vir na parte básica de consulta, você vai ver o tipo de dado que o Prometheus usa, como ele lida com _string_, como ele lida com _float_, como ele trabalha com _instant vector_ e como ele trabalha com _range vector_.ßßß

\[16:20\] Eu aconselho que você aprofunde mais utilizando essa documentação, ela vai estar na plataforma, vamos estender esse assunto até o final do curso, só que não vamos esgotá-lo. Então, acho muito interessante você consumir a documentação e aprofundar um pouco mais.

\[16:37\] Agora que entendemos a anatomia de uma métrica, entendemos os três componentes – _metric name_, _label_ e o retorno da consulta que é o _sample_.

\[16:52\] E entendemos também os tipos de dados que o Prometheus utiliza, já estamos com o caminho aberto para a próxima aula, em que vamos aprofundar um pouco nesse assunto, vamos falar sobre os tipos de métricas que o Prometheus utiliza.

\[17:13\] Te vejo na próxima aula, até mais.
