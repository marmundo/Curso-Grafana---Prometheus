\[00:00\] Sejam bem-vindos à nossa aula 2 do curso. Agora, vamos configurar o Actuator e enfim tornar a nossa aplicação observável – ou, pelo menos, iniciar esse trajeto.

\[00:16\] Aqui foi onde paramos na aula anterior, nós conseguimos implantar o ambiente e subir a aplicação. A primeira coisa que eu peço a você é que você dê uma olhada na documentação do Actuator. É só você digitar no Google “Actuator” e você vai encontrar em um dos primeiros resultados a documentação do Spring dizendo como você vai habilitar o Actuator [link](https://docs.spring.io/spring-boot/docs/1.4.0.M2/reference/html/production-ready.html).

\[00:48\] O Actuator entra como uma dependência. No nosso caso, estamos utilizando o Maven. Vou copiar essa dependência. Se estiver usando Gradle, é outra forma de implantação, mas, no nosso caso, é o Maven.

\[01:08\] Vou copiar isso, vou abrir o Eclipse e, no Eclipse, vou abrir o arquivo `pom.xml`. Tem diversas dependências configuradas aqui, você deve encontrar algum espaço para colocar essa configuração, eu vou colocar aqui:

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

\[01:45\] Vou manter a indentação e está certo. Tenho essa dependência já configurada, vou salvar e, no automático, o Maven já vai descarregar essa dependência através do Eclipse.

\[02:08\] O processo é bem simples. Tendo feito isso, é necessário que façamos alguns ajustes na nossa aplicação. Nesse caso, não vamos mexer no código da aplicação agora. No painel à esquerda, vamos em `src/main/resources`, vamos no `application-prod.properties` e aqui tem diversas configurações.

\[02:32\] Tem a porta em que a aplicação sobre, tem a configuração do Redis, tem a configuração do MySQL, tem o JPA para conexão e tem o _token_ `jwt`, porque essa aplicação usa um _token_.

\[02:47\] Para algumas ações de excluir um tópico, criar um tópico, é necessário ter um _token_ que é gerado através de uma autenticação. Estamos falando de uma API Rest.

\[03:02\] O que vou fazer agora? Deixa eu pegar uma cola para não ter que digitar tudo isso:

    # actuator
    management.endpoint.health.show-details=always
    management.endpoints.web.exposure.include=health,info,metrics

Em qualquer espaço que você encontrar, pode colocar `actuator`. A primeira linha que eu inseri aqui foi o `management.endpoint.health.show-details`.

\[03:23\] Está como `always`, então vai mostrar todos os detalhes, e aqui eu tenho o `web.exposure`. Aqui está um asterisco; se eu deixar com asterisco, ele vai basicamente colocar todas as informações relacionadas a JVM e tudo que estiver relacionado à aplicação, ao gerenciamento da aplicação pela JVM.

\[03:46\] Isso, para mim, não vai ser muito interessante – você pode até fazer esse teste. Quem eu vou disponibilizar é um _endpoint_ chamado `health`, um _endpoint_ chamado `info` e um _endpoint_ chamado `metrics`. Então: `management.endpoints.web.exposure.include=health,info,metrics`.

\[04:01\] Esses três estão de bom tamanho, são o que nós precisamos. O nosso foco vai estar sobre o `metrics`, mas o `health` é legal se você tem um _endpoint_ que pode ser usado para _health check_, dependendo de onde você estiver rodando a sua aplicação.

\[04:21\] E o `info` é legal porque você consegue ter as informações dessa aplicação, informações interessantes para você, não para o público externo. `health`, `info` e `metrics` são internos, não devem ser expostos publicamente.

\[04:42\] Essa aplicação, quando estiver rodando na _stack_ do Docker Compose, vai estar com esses _endpoints_ fechados. Para acessarmos essa aplicação, vamos ter que passar por um _proxy_ que também vai ser implantado no próximo capítulo.

\[05:00\] Tendo cumprido esses pré-requisitos, eu vou para o Terminal. A aplicação está rodando, nós a subimos pelo Eclipse. Vou fechar essa janela e, como já estou no diretório da aplicação, vou rodar um `mvn clean package` para "rebuildar" essa aplicação.

\[05:23\] O processo é bem simples. Como eu disse na aula anterior, você pode fazer isso pelo Eclipse, mas eu prefiro fazer aqui. Nos contêineres, não é necessário mexer. Eu não subi em modo _daemon_, então ele está trazendo o _status_ dos contêineres.

\[05:41\] Vou dar um _zoom_ no Terminal em que a aplicação está sendo "buildada". Rodou direito, vamos agora para o Eclipse. No Eclipse, vou no `start.sh` novamente e vou rodar a aplicação.

\[06:03\] Vamos deixá-la subir aqui. Se você olhar, essa linha da inicialização, só para você ter uma ideia, de repente você está no Windows e o `bin/bash` não vai funcionar para você.

\[06:16\] Você pode rodar isso na linha de comando do `cmd` do próprio Windows, contanto que você esteja posicionado no _path_ em que está o `app`. Você tem que estar dentro do diretório `app`, aí você pode chamar o Java dessa maneira que ele vai encontrar, dentro de `target`, o `forum`.

\[06:37\] Você só vai ter que fazer isso no Windows, colocar uma contrabarra (`target\forum`) e não a barra (`/`), porque o Windows não entende a barra que, no Linux, faz distinção entre um diretório e outro. No MacOS, isso não muda nada.

\[06:54\] Voltando, a aplicação subiu, foi "startada" e, por fim, eu tenho “topicos”, tenho “[http://localhost:8080/topicos/”](http://localhost:8080/topicos/%E2%80%9D) e um ID qualquer. Agora tenho “[http://localhst:8080/actuator”](http://localhst:8080/actuator%E2%80%9D). Aqui está o Actuator expondo para nós _health_. Aqui tenho _health_ mais um _path_ específico, mas ele é herdado desse _health_ aqui que foi configurado no `application properties`.

\[07:38\] Está aqui, eu tenho esse _endpoint_ `health`, tenho o _endpoint_ `health-path` que veio herdado do `health`, tenho o `info`, e tenho o `metrics`. Tenho o `metrics` com uma métrica específica, o `metric name`, e tenho o `metrics` puro.

\[07:59\] Então, o que vou fazer aqui? Vou abrir o _health_, vamos dar uma olhada no _health_. Está aqui, esse é o _health_ que pode ser usado como _health check_, então `status: UP`. Ele olha, inclusive, a comunicação que a aplicação depende, no caso, o `My SQL`, está conectado.

\[08:16\] Olha o espaço em disco. Tem o `redis` também `UP`. Então, esse `health` é importantíssimo para a questão de _health check_ e para você entender, em um momento imediato, se alguma dependência está com problema.

\[08:35\] Se ele não conectar com o Redis, vai bater aqui; se não conectar com o MySQL, vai bater aqui também, porque isso não depende da aplicação conectar no banco para ser exibido.

\[08:48\] Já demos uma olhada no _health_, vamos dar uma olhada no _info_, o que eu encontro dentro do _info_. O `app`, qual é o nome, a descrição, a versão, como ele está codificado e a versão do Java. Isso é bem legal.

\[09:06\] O que nós conseguimos, na parte mais importante, em _metrics_, o que conseguimos ver? Muita coisa. Aqui tenho a exposição de todas as métricas da JVM. Se você verificar, você tem o uso de CPU, você tem o _log_ no `logback`, você tem a questão de `threads`, de memória, você consegue encontrar o `garbage collector`.

\[09:39\] Você consegue pegar o _pool_ de conexões da JDBC com o banco, conexões pendentes, com _timeout_, utilizadas, tempo de criação, enfim, diversas métricas.

\[09:55\] Essas métricas, se eu pegar o nome desse, eu consigo chegar nesse _endpoint_ com o nome de uma métrica naquela métrica específica. Por exemplo, vou pegar o `hikaricp.connections`, vou chamar esse _endpoint_, que é o mesmo. Vou colocar o “[http://localhost:8080/actuator/metrics/hikaricp.connections”](http://localhost:8080/actuator/metrics/hikaricp.connections%E2%80%9D) e está aqui, o valor é 10.

\[10:24\] Então, eu consigo chegar nessas métricas. Nós conseguimos colocar as métricas da JVM aqui, elas estão expostas, porém, não estão no formato esperado. Nós não conseguimos identificar e usar essas métricas através do Prometheus, que é o nosso objetivo.

\[10:47\] Então, na próxima aula, vamos configurar o Micrometer e ele vai fazer esse meio de campo, vai tornar essas métricas legíveis para o Prometheus. Te vejo na próxima aula.
