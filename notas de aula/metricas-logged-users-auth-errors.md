\[00:00\] Vamos dar sequência no nosso curso, agora vamos trabalhar criando mais dois painéis.

\[00:10\] Vamos em “_Add panel_”. Agora vamos trabalhar com uma métrica que diz respeito ao número de usuários autenticados no último minuto.

\[00:25\] No campo "metrics browser", vou colocar `user`, já conseguimos buscar, vai ser `auth_user_success_total`. No caso, se eu colocar essa métrica aqui, ela já vai me trazer um valor, só que não é o valor que eu quero demonstrar no meu _dash_, eu quero um painel com números.

\[00:48\] O que eu preciso aqui? Eu quero olhar para o último minuto, não quero olhar a totalidade, não quero olhar um contador que sempre vai estar sendo incrementado, porque ele não vai refletir a realidade da minha API.

\[01:03\] Alguns usuários já não vão estar mais logados, então quero pegar somente a autenticação do último minuto para entender quantos usuários estão autenticados naquele minuto.

\[01:15\] Para esse caso, é interessante, primeiro, se eu definir o meu _range time_, eu não vou ter informações sendo plotadas aqui. Por quê? Porque eu preciso de um dado _Scalar_ ou de um _instant vector_.

\[01:31\] Quando eu trabalho com um tempo especificado na minha consulta, eu formo um _range vector_ e um _range vector_ não tem como formar um gráfico. Então, eu vou ter que trabalhar com uma função.

\[01:46\] Vou utilizar o `increase` porque quero a taxa de crescimento dessa métrica no último minuto, `increase(auth_user_success_total[1m])`. Você pode se perguntar: “Você vai ter que utilizar o `sum` para fazer uma agregação?”, não é necessário nesse caso, o valor vai ser o mesmo, porque estou trabalhando apenas com uma série temporal, a partir do momento que uso o `increase`.

\[02:09\] Então, eu não preciso fazer uma agregação nesse caso. Está aqui, a visualização que eu vou escolher é “Stat” também. Estou com “9.82”, a taxa de crescimento de autenticação foi essa.

\[02:28\] É um número quebrado, vou arredondar isso. O título que vamos usar é “USERS LOGGED”, “usuários logados”. A descrição é “Usuários logados no último minuto”.

\[02:50\] O cálculo vai ser o último valor não nulo. O campo é numérico. A coloraçãom vou tirar o “_Graph mode_” para ficar só o número. Em “_Standard options_”, a unidade que vamos utilizar é uma unidade “_Short_” mesmo.

\[03:14\] Se eu quiser tirar um número decimal, eu posso colocar um valor “0” e ele vai arredondar. Essa métrica é uma aproximação do que temos de usuários autenticados no último minuto.

\[03:28\] Não é o valor exato do cálculo que o Prometheus faz olhando a taxa de crescimento do último minuto porque ele se baseia em uma série temporal, então o dado sempre vai ser um número quebrado, sempre vai ser um _float_.

\[03:46\] Não tenho “_Threshold_” aqui, vou manter um verde mais escuro. Então, já temos um painel com o número de usuários logados no último minuto. Vou formatá-lo, vou diminuir, está muito grande.

\[04:09\] Assim está mais interessante, pronto. Vamos adicionar mais um painel. Esse painel vai ser uma métrica relacionada aos erros de autenticação, é `auth_user_error_total`.

\[04:23\] Temos o mesmo paradigma de antes, eu quero pegar o meu último minuto e vou trabalhar com a minha taxa de crescimento, vai ser `increase` para `[1m]` e vamos seguir com o mesmo trabalho que fizemos na métrica anterior.

\[04:47\] Vai ser uma visualização “_Stat_”, o título do painel vou colocar como “AUTH ERRORS”, vou colocar como “Erros de autenticação no último minuto”, essa é a descrição. Quando alguém posicionar o mouse sobre a métrica, você vai ver a descrição, então é legal para alguém recém-chegado, que não entende a composição do _dash_, para se encontrar.

\[05:19\] O cálculo vai ser em cima do último valor não nulo; vou tirar a coloração gráfica para manter só o número; na unidade, vou trabalhar também com o “_Short_” – se eu colocar “_None_”, ele não muda nada, com valor de “_String_”, ele iria colocar todo o número completo, o que não é interessante, então vamos manter o “_Short_”.

\[05:52\] Vou tirar a casa decimal e aqui, sim, vou colocar um “_Threshold_”. Vamos imaginar que, em 1 minuto, se tivermos 50 erros de autenticação, teremos um problema. Como não vamos simular 50 erros de autenticação em 1 minuto, eu vou colocar aqui que 5 erros de autenticação é uma situação um pouco estranha.

\[06:26\] Vou abrir de novo o “_Threshold_”. E que 10 erros de autenticação já significa que talvez exista um problema no nosso _database_, porque a aplicação tem uma regra de negócio que vai validar o que o usuário enviou com os dados que estão no _database_, então ela vai fazer uma consulta para devolver um _token_ para esse usuário.

\[06:52\] Vou deixar o “_Threshold_” dessa forma e está feito. Agora, já temos quatro painéis, são bem simples. deixa só eu dar uma reforçada nessa cor verde e trabalhar com um verde mais escuro.

\[07:12\] Até dado momento, está tudo tranquilo, já vamos começar a trabalhar com algumas coisas mais complexas, mas, por hora, vamos seguindo dessa maneira.

\[07:22\] Na próxima aula, já vamos trabalhar com dois outros painéis: um que reflete as informações de _log_, o _log level_, e outro que vai olhar para o _pool_ de conexões da JDBC. Nos vemos na próxima aula.
