## Trabalho Engenharia de Software ##
  Este trabalho proposto da matéria de Engenharia de Software.
   Consiste no desenvolvimento de um SAS (Software as a Service) utilizando
   plataformas como Heroku (https://www.heroku.com) e frameworks web como por exemplo django (https://www.djangoproject.com) e
   ruby on rails (https://rubyonrails.org)

## Sobre o projeto proposto ##
  O projeto que estamos realizando foi proposto por outro grupo consiste na construção de um sistema de localização
   e cadastro de Coffee Breaks.

## Stakeholders ##
  Existe apenas um tipo de stakeholder denominado Usuário do sistema.
  Este usuário pode entrar no sistema para cadastrar um Coffee Break com o objetivo de alimentar o sistema e ajudar outros usuários.
  Ele também pode entrar no sistema para procurar um Coffee Break na sua região.

## O objetivo ##
  Armazenar e disponibilizar localizações em que Coffee Breaks estão acontecendo para que os usuários possam
  se alimentar de forma gratuita, se deslocando o mínimo possível.

## Sobre a arquitetura do projeto ##
  * Framework escolhido: Django
  * SGBD escolhido: PostgreSQL
  * Heroku: https://coffebreak.herokuapp.com/CoffeeBreak/

  A escolha do framework Python Django foi feita por causa da familiaridade da maior parte dos membros do grupo com a linguagem de programação Python
  diminuindo, assim, o tempo necessário para o aprendizado.
  Já a escolha do SGBD PostgreSQL foi feita por ser uma ferramenta open source, de fácil utilização, configuração e conexão com a linguagem Python.

## Histórias de usuário / Storyboards ##
  * Me cadastrar no sistema para me autenticar no sistema; Storyboard: coffeeBreak/LoFis/login.jpg e coffeeBreak/LoFis/cadastro.jpg (MVP)
  * Me autenticar no sistema para cadastrar e/ou encontrar um coffee break; Storyboard: coffeeBreak/LoFis/login.jpg e coffeeBreak/LoFis/dashboard.jpg (MVP)
  * Encontrar palestras com coffee break num raio determinado pelo usuário para ter acesso a elas;
  * Cadastrar uma palestra com Coffee Break usando endereço para poder ser encontrado; coffeeBreak/LoFis/login.jpg , coffeeBreak/LoFis/dashboard.jpg e coffeeBreak/LoFis/novoCB.jpg (MVP)
  * Cadastrar uma palestra com Coffee Break usando localização para poder ser encontrado; coffeeBreak/LoFis/login.jpg , coffeeBreak/LoFis/dashboard.jpg e coffeeBreak/LoFis/novoCB.jpg
  * Como sistema que após o termino de qualquer coffee break o evento desapareça para que os usuários não corram risco de irem em uma coffee break que já acabou;
  * Ver coffee breaks que eu cadastrei que irão acontecer para poder gerenciar os coffee breaks; Storyboard: coffeeBreak/LoFis/login.jpg , coffeeBreak/LoFis/dashboard.jpg e coffeeBreak/LoFis/seusCB.jpg
  * Cancelar um coffee break para remover o coffee break do sistema; Storyboard: coffeeBreak/LoFis/login.jpg , coffeeBreak/LoFis/dashboard.jpg e coffeeBreak/LoFis/seusCB.jpg (MVP)
  * Ver no mapa a posição do coffee break para ter uma noção da localização;
  * Ver no street view o local do coffee break para ter uma noção da localização;
  * Avaliar o coffee break para que os outros usuários saibam a qualidade do coffee break;
  * Comentar um coffee break para que as outras pessoas vejam.

## MVP ##
 Minimal Viable Product

  * O usuário deve poder se cadastrar no sistema - ok!
  * O usuário deve conseguir se logar no sistema - ok!
  * O usuario deve poder visualizar os coffee breaks cadastrados - ok!
  * O usuario deve poder cadastrar coffee breaks - ok!

## Cenários ##
 Fluxo normal (1)
  * O usuário entra no site e deseja se cadastrar.
  * O usuário clica no botão "Cadastro", preenche os dados corretamente e e clica em "Cadastrar".
  * O usuário está de volta à tela inicial e agora pode se logar com o usuário criado.

 Fluxo normal (2)
  * O usuário já possui cadastro e irá fazer login.
  * O usuário preenche seus dados corretamente e clica em "Login".
  * O usuário está no dashboard de coffee breaks.

 Fluxo normal (3)
  * O usuário está no dashboard e deseja cadastrar um novo coffee break.
  * O usuário clica no botão "+".
  * O usuário está na tela de cadastro de coffee breaks.
  * O usuário preenche corretamente os dados do coffee breaks e clica em "Tudo certo".
  * O usuário está de volta ao dashboard e o novo coffee break está lá.

 Fluxo que causa execessões (1)
  * O usuário está na tela inicial e deseja fazer login, mas não possui cadastro.
  * O usuário insere dados que não estão cadastrados no sistema.
  * o sistema avisa ao usuário que o usuário está incorreto.

 Fluxo que causa excessões (2)
  * O usuário está logado e no dashboard e deseja criar um novo coffee break.
  * O usuário digita a data no formato incorreto.
  * O usuário permanece na tela de cadastro de coffe break e o sistema avisa que o formato está incorreto.

## Relatório de experiência no uso das técnicas ##
  Práticas de Negócio usadas: (1)

    * Cliente no time
    * Metáforas
    * “Semana de 40 horas”

  Práticas de Desenvolvimento usadas: (2)

    * Projeto simples
    * Refatoração
    * Programação em pares
    * Padrões de codificação
    * Integração contínua

## Decisões de projeto ##

  Optou-se por desenvolver as histórias de usuários mais simples e que seriam MVP para conseguir entregar o protótipo do sistema a tempo e funcionando.

## Lições aprendidas ##

    Planejar o horizonte de tempo e marcar as iterações são fundamentais para o bom andamento do trabalho. (1)
    A divisão de tarefas de acordo com a facilidade, habilidade e experiência de cada membro da equipe ajuda a ter eficiência no resultado. (2)
    Ter o cliente no time é muito importante se quiser usar o paradigma ágil de desenvolvimento. (3)


## Data de entrega ##

  **26/11/2017**
