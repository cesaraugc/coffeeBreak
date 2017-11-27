## Trabalho Engenharia de Software - Grupo 4 ##
  Este trabalho proposto da matéria de Engenharia de Software consiste no desenvolvimento de um SAS (Software as a Service) utilizando plataformas como Heroku (https://www.heroku.com) e frameworks web como por exemplo django (https://www.djangoproject.com) e ruby on rails (https://rubyonrails.org)

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
  * Avaliar o coffee break para que os outros usuários sa

## Planejamento das iterações e resultados ##
  O desenvolvimento iterativo é aquele que, de pouco em pouco, vai refinando o projeto até estar por completo. 
  Planejamos a iteração criando histórias de usuário e metas com pontuações de menores (para os mais simples) e maiores (para os mais complexos). O objetivo desse tipo de desenvolvimento foi de nos organizarmos e entregarmos o trabalho final no prazo estimado.
  Como resultado desta metodologia sentimos que começamos a trabalhar neste projeto mais cedo que o habitual, tendo tempo de nos reunir com os clientes afim de conversar, adquirir Lo-Fis e histórias de usuários personalizados por eles, deste modo, descobrir que tipo de projeto eles mais gostariam de receber. 
