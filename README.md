# 1. Problema de negócio

Meu projeto de Marketplace de Restaurantes aborda as questões centrais de negócio, oferecendo uma solução abrangente para a visualização e análise de dados. Meu objetivo é capacitar os líderes estratégicos com insights acionáveis para aprimorar a tomada de decisões.

Na Fome Zero, atuei como a mente por trás da criação desta plataforma que conecta clientes e restaurantes, simplificando o processo de busca e transação. Ao cadastrar-se na plataforma, os restaurantes fornecem uma gama de informações valiosas, incluindo detalhes de localização, especialidades culinárias, disponibilidade de reservas e opções de entrega, além de uma classificação de satisfação do cliente.

Como parte do meu projeto, desenvolvi um dashboard intuitivo que condensa as principais consultas de negócios, permitindo uma análise rápida e precisa dos dados. Este dashboard serve como uma ferramenta vital para identificar tendências, avaliar o desempenho e explorar oportunidades de crescimento de forma eficiente e eficaz.

As principais perguntas geradas foram essas:

- Geral
    1. Quantos restaurantes únicos estão registrados?
    2. Quantos países únicos estão registrados?
    3. Quantas cidades únicas estão registradas?
    4. Qual o total de avaliações feitas?
    5. Qual o total de tipos de culinária registrados?
- Pais
    1. Qual o nome do país que possui mais cidades registradas?
    2. Qual o nome do país que possui mais restaurantes registrados?
    3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
    registrados?
    4. Qual o nome do país que possui a maior quantidade de tipos de culinária
    distintos?
    5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
    entrega?
    7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
    reservas?
    8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
    registrada?
    9. Qual o nome do país que possui, na média, a maior nota média registrada?
    10. Qual o nome do país que possui, na média, a menor nota média registrada?
    11. Qual a média de preço de um prato para dois por país?
- Cidade
    1. Qual o nome da cidade que possui mais restaurantes registrados?
    2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
    4?
    3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
    2.5?
    4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    Conteúdo licenciado para -
    5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
    distintas?
    6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
    reservas?
    7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
    entregas?
    8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
    aceitam pedidos online?
    
- Restaurantes
    1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    2. Qual o nome do restaurante com a maior nota média?
    3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
    pessoas?
    4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
    média de avaliação?
    5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
    possui a maior média de avaliação?
    6. Os restaurantes que aceitam pedido online são também, na média, os
    restaurantes que mais possuem avaliações registradas?
    7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
    possuem o maior valor médio de um prato para duas pessoas?
    8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
    possuem um valor médio de prato para duas pessoas maior que as churrascarias
    americanas (BBQ)?
- Tipos de Culinária
    1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
    restaurante com a maior média de avaliação?
    2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
    restaurante com a menor média de avaliação?
    3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
    restaurante com a maior média de avaliação?
    4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
    restaurante com a menor média de avaliação?
    5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
    restaurante com a maior média de avaliação?
    6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
    restaurante com a menor média de avaliação?
    7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
    restaurante com a maior média de avaliação?
    8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
    restaurante com a menor média de avaliação?
    9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
    restaurante com a maior média de avaliação?
    10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
    restaurante com a menor média de avaliação?
    11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
    pessoas?
    12. Qual o tipo de culinária que possui a maior nota média?
    13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
    online e fazem entregas?

Como parte do meu projeto, desenvolvi um dashboard intuitivo que condensa as principais consultas de negócios, permitindo uma análise rápida e precisa dos dados. Este dashboard serve como uma ferramenta vital para identificar tendências, avaliar o desempenho e explorar oportunidades de crescimento de forma eficiente e eficaz.

# 2. Premissas do Negócio

O modelo assumido foi de um Marketplace de restaurantes

As principais visões de negócio foram: Países, Cidades, Restaurantes e Tipos culinários

A conversão de valores para dólar foi feita usando a taxa de câmbio do dia 15/02/2024

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as principais visões do modelo de negócio da empresa:

  1. Visão dos países
  2. Visão das cidades
  3. Visão dos restaurantes
  4. Visão dos tipos culinários

Cada visão é representada pelo seguinte conjunto de métricas:

- Visão dos países
    1. Countries with most Cities
    2. Countries with most Restaurants
    3. Countries with most Cuisines types
    4. Countries with most Votes
    5. Higher and Lower Ratings
    6. Average Cost for two by Country
    7. Countries with most Restaurants Gourmets
    8. Countries with most Restaurants that deliver
    9. Countries with most Restaurants that accepts
    10. Countries with most Average Votes
    
- Visão das cidades
    1. Cities with most Restaurants
    2. Cities with best rating Restaurants
    3. Cities with worst rating Restaurants
    4. Cities with the Bigger Average cost for two
    5. Cities with most Cuisines types
    6. Cities with most Restaurants that accepts Table Bookings
    7. Cities with most Restaurants that Deliver
    8. Cities with most Restaurants that Deliver Online
- Visão dos restaurantes
    1. Restaurantes with most Votes
    2. Restaurantes with Better Rating
    3. Restaurantes with Hightest Cost in Dollar
    4. Brazilian Restaurantes with Hightest Rating
    5. Brazilian Restaurantes with Lowest Rating
    6. Accept Table Booking
    7. Dont Accept Table Booking
- Visão dos tipos culinários
    1. The bests
    2. The Worths
    3. Most expensive cuisines

Algumas visões também foram separadas em visões gerais e visões específicas

# 4. Top 3 Insights de dados

  1. Índia tem a grande maioria dos restaurantes porém o custo médio por cliente é baixo
  2. O tipo de culinária italiana e americana tem um custo médio por cliente médio e uma grande gama de restaurantes
  3. Restaurantes que aceitam reserva em média tem um custo por cliente mais elevado e os que aceitam delivery tem na média melhores avaliações que os demais

# 5. O produto final do projeto

Painel online, hospedado em uma Cloud e disponível para acesso em qualquer dispositivo conectado a internet.

O painel pode ser acessado através desse link: 

# 6. Conclusão

O objetivo do meu projeto foi criar um conjunto de gráficos e/ou tabelas que exibissem métricas de forma eficaz.

Durante o desenvolvimento, pude extrair uma variedade de insights valiosos sobre as funcionalidades dos restaurantes e seu impacto no desempenho geral. Identifiquei os principais impulsionadores por trás das avaliações dos clientes, assim como os fatores que contribuem para um preço médio mais elevado em determinados estabelecimentos.

Além disso, pude mapear áreas potenciais para exploração ou expansão de restaurantes existentes, bem como identificar oportunidades para a criação de novos estabelecimentos. Essas descobertas fornecem uma base sólida para decisões estratégicas e orientam o desenvolvimento futuro da Fome Zero.

# 7. Próximos passos

1. Apresentar mais métricas combinando algumas já presentes
2. Criar novos Filtros
3. Adicionar mais perspectivas em cada visão
