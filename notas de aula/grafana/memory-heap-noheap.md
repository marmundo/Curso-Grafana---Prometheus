\[00:00\] Vamos dar sequência ao nosso curso. Nessa aula, vamos começar a criar métricas que vão analisar o consumo de CPU e de memória. Vamos verificar como está a saturação dos recursos enquanto nossa aplicação é executada e consome a infraestrutura que a está suportando.

\[00:24\] Vou recolher a nossa _row_ de “API RED” para não ficar com muita informação, e vamos criar o nosso primeiro painel relacionado a isso. A métrica que vou utilizar é a métrica `jvm_memory_used_bytes`.

\[00:49\] Vamos colocar os _labels_ `{application=”$application”, instance=”$instance”, job=”app-forum-api”}`. Além disso, vamos trabalhar com a área de memória que vamos estar observando, que vai ser a `area=”heap”}`.

\[01:22\] Já tenho esse retorno aqui. Tenho três séries temporais relacionadas à alocação de memória _heap_ e o que vai dividir essas séries temporais é o ID. Tenho o `PS Eden Space`, tenho o `PS Old Gen` e tenho o `PS Survivor Space`.

\[01:44\] Até aqui, está bem legal, só que preciso fazer uma agregação desses valores. Então, vou trabalhar com o `sum` que vocês já conhecem muito bem, é a nossa função de agregação.

\[01:57\] Tenho essa métrica sendo retornada para mim, porém, esse valor é percentual e eu quero um valor inteiro, então vou multiplicá-lo por 100 para eu ter um retorno mais interessante. Vou colocar `*100`ao final da consulta.

\[02:14\] Agora, o que vou fazer é dividir esse valor, vou pegar basicamente a métrica inteira e vou fazer uma divisão por ela mesma, só que sem multiplicá-la por 100.

\[02:41\] A diferença é que vou fazer uma pequena alteração. Ao invés de pegar o `used_bytes`, vou pegar o `jvm_memory_max_bytes`, a quantidade máxima: `sum(jvm_memory_used_bytes{application=”$application”, instance=”$instance”, job=”app-forum-api”, area=”heap”}) *100 / sum(jvm_memory_max_bytes{application=”$application”, instance=”$instance”, job=”app-forum-api”, area=”heap”})`.

\[02:59\] Eu começo agora a ter um retorno interessante desse valor para mim. Em “_Time series_”, vamos trabalhar com o “_Gauge_”. Por quê? Esse é um valor que vai variar, vai ser incrementado e decrementado.

\[03:21\] Atualmente, estou em “2.2%. Vamos colocar o título como “HEAP USED” e a descrição será “Memória heap utilizada”.

\[03:42\] Está bem grande esse valor, está com 72;2% e, provavelmente, eu posso estar cometendo uma pequena falha nesse cálculo. Deixa eu olhar a métrica direito.

\[04:15\] Agora tivemos uma modificação que foi quando o próprio _scrape time_ do Prometheus rodou, ele pegou um novo valor e a métrica andou. Em 72%, estava muito baixo, eu estava achando estranho.

\[04:35\] O valor mínimo que vamos ter é 0, o máximo é 100. Valores decimais vou deixar, não vou mexer nisso; o “_Color scheme_” é do “_Threshold_”, então vou colocar que 80% é um problema e que 100% é um problema ainda maior, então vou colocá-lo como roxo.

\[05:10\] No momento, ele está em 91%, está sendo bem utilizada a alocação _heap_ dela, até mais do que eu esperava, e está certo, é isso mesmo que eu queria.

\[05:26\] Então, já temos um painel com o uso de memória _heap_ e agora, vou copiar essa consulta porque vamos criar um outro painel que é bem similar a esse.

\[05:46\] Qual a diferença? Ele vai trabalhar com outra área de memória, com a alocação `nonheap`. Será então `sum(jvm_memory_used_bytes{application=”$application”, instance=”$instance”, job=”app-forum-api”, area=”nonheap”}) *100 / sum(jvm_memory_max_bytes{application=”$application”, instance=”$instance”, job=”app-forum-api”, area=”nonheap”})`. Não tem legenda, basicamente é isso mesmo que eu queria.

\[06:11\] Aqui, vou chamar de “NON HEAP USED”. E a descrição ficará como “Memória non heap utilizada”. Vamos descer, valor de legenda não vou colocar, não tem muito o que mexer nisso, vamos tirar do “_Time series_” e levar para “_Gauge_”.

\[06:50\] O cálculo vai em cima do último valor não nulo, está certo. Aqui está para mostrar as marcas de _threshold_, vou manter para ficar igual ao outro. Não coloquei unidade no outro, mas não vai fazer diferença para nós.

\[07:13\] O valor mínimo é 0, o valor máximo é 100. Descendo, vou deixar o _base_ em verde, meu 80 em vermelho e vou colocar basicamente uma configuração igual ao que fizemos no painel de memória _heap_, apesar de serem coisas bem distintas.

\[07:49\] Eu poderia trabalhar até com o valor percentual, o que ficaria melhor. Na unidade, vou olhar como vamos ficar se trabalharmos com o percentual. Ficou interessante, o ideal é utilizarmos essa configuração de percentual de 0 a 100.

\[08:17\] Está feito, vou só ajustar o nosso “HEAP USED”. Vou editá-lo, vou na unidade e vou trabalhar com “Percentual”. Felizmente, deu uma caída na utilização, 69,6%.

\[08:43\] Só mais um detalhe para ambos ficarem bem similares, vou colocar um verde escuro e está certo. Então, tenho aqui “HEAP USED” e “NON HEAP USED”. Estamos observando como está o tratamento de memória _heap_ e _non heap_.

![Indicador *heap used*, mostrando o valor 73.3%. Indicador *non-heap used*, mostrando 10,9%.](https://caelum-online-public.s3.amazonaws.com/2522-monitoramento/Transcri%C3%A7%C3%A3o/Aula+03/Imagens/grafana_09.png)

\[09:01\] Na próxima aula, vamos olhar para o CPU. Nos vemos na próxima aula.
