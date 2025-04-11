# IP-Project
## 🎮 Descrição do Projeto
O Projeto da disciplina de Introdução à Programação do semestre 2024.2 consiste na construção de um sistema interativo em ambiente 2D. Nele, o usuário controla um objeto com a finalidade de coletar outros objetos dispostos na tela, que serão registrados e exibidos ao usuário. O projeto é estruturado com base na **Programação Orientada a Objetos** e na linguagem **Python**.
## 👾 Sobre o Jogo
> inspirações, tutoriais, dinâmica

O (Nome do Jogo) é um jogo 2D estilo top-down shooter, que consiste no controle de um player, representado por um estudante de Matemática Discreta que precisa salvar seu professor Nivan. O jogo possui três fases, que são desbloqueadas após um combate contra Navin, um mago muito poderoso que sequestrou o professor e ataca o jogador com o poder da "matemática". A cada fase, uma nova arma é coletada, de forma que ela será guardada no inventario do player e poderá ser usada na próxima fase para derrotar Navin definitivamente e, assim, salvar Nivan dos absurdos matemáticos.

**Galeria de imagens**

**FASE 1**
![FASE 1](i.imgur.com/ghGQ6kP.png)

## 🖲️ Contribuidores e Funções
- Davi Matoso <a href="https://github.com/DaviMatoso">(GitHub)</a>
  - Criação das armas utilizadas pelo personagem
  - Dinâmica de dano ao personagem

- Isabella Mendes <a href="https://github.com/isabellamdsr">(GitHub)</a>
  - Implementação dos objetos coletáveis
  - Modularização do código
  - Documentação do projeto

- Luan Romero <a href="https://github.com/luanromerolcc">(GitHub)</a>
  - Criação dos sprites do personagem, das armas coletáveis e dos ataques
  - Criação dos cenários
  - Criação da soundtrack
  - Implementação de efeitos sonoros

- Sérgio Tavares <a href="https://github.com/teamfortr3ss2">(GitHub)</a>
  - Modularização do código
  - Apresentação do projeto

- Jesper Ian <a href="https://github.com/j-iann">(GitHub)</a>
  - Movimentação do inimigo
  - Ataques do inimigo
  - Interação com a tela inicial

- Arthur Jorge <a href="https://github.com/Arfhum">(GitHub)</a>
  - Movimentação do personagem pelo mapa
  - Implementação das colisões com o mapa e transição de fases
  - Modularização do código
  - Ataques do inimigo

No entanto, é importante destacar que toda a equipe trabalhou em conjunto para correção de eventuais erros e organização do código.

## ✏️ Organização do Projeto
O código foi dividido em módulos para uma melhor organização:
- **Main:** Módulo principal que inicia o jogo. Por uma questão de organização, ele importa os módulos de cada fase do jogo;
- **fase1:** Módulo que engloba outros módulos, definindo o funcionamento da primeira fase;
- **fase2:** Módulo que engloba outros módulos, definindo o funcionamento da segunda fase;
- **fase3:** Módulo que engloba outros módulos, definindo o funcionamento da terceira fase;
- **moduloConfig:** Contém as configurações fixas do jogo, como dimensões da tela, configurações da soundtrack e da parte gráfica;
- **moduloDesenho:** Define uma classe de desenho para as imagens que aparecerão na tela;
- **moduloPlayer:** Define a classe do jogador e contém os atributos a ele relacionados, como imagem, hitbox, vida e perda/recuperação de vida, métodos de movimentação e de colisão com o cenário / ataques do inimigo;
- **moduloColetaveis:** Define a classe dos coletáveis. Possui atributos de imagem (que deve sumir após o item ser coletado), identifição de colisão com o player e as especificações de cada item coletado;
- **moduloBala:** Criação das balas de cada arma de ataque do player, definindo imagem, movimentação, velocidade, ângulo e dano;
- **moduloArmaAtiva:** Módulo que "ativa" o funcionamento da arma atual, escolhida dependendo da tecla do teclado pressionada;
- **moduloProjetil:** Módulo que contém os ataques do inimigo (projéteis que caem em direção ao chão e podem acertar o player, explosão em área), definindo imagem e especificações do ataque utilizado;
- **moduloNAVIN:** Define as especificações do inimigo, como sua imagem, movimentação e dinâmica de dano tomado.

## 📚 Ferramentas Utilizadas
- **Pygame** - Framework de desenvolvimento de jogos
- **Aseprite** - Criação e animação de cenários e elementos gráficos
- **FL Studio** - Produção da soundtrack do jogo
- **Trello** - Gerenciamento de tarefas entre o grupo
- **VSCode** - Editor de código-fonte

A biblioteca pygame foi escolhida por conter recursos que facilitaram o funcionamento do jogo de forma mais direta, possibilitando a integração efetiva entre os elementos escolhidos.
Utilizamos o site <a href="https://www.pygame.org/docs/">*pygame.org*</a> como referência para a base do código e implementação das funções do jogo.

## 🔍 Conceitos Aplicados
- **Programação Orientada a Objetos e Herança:** Utilizamos os conceitos vistos em POO em basicamente todos os módulos. Foram criadas classes para o player, inimigo, coletáveis, etc (cada um com seus próprios atributos e métodos). Objetos que se repetiam em seu funcionamento, como os coletáveis, utilizaram conceitos de herança. Dessa forma, vimos a importância do POO projetos maiores como esse jogo, facilitando a organização e o compartilhamento de caracteristícas comuns.
- **Condicionais:** Utilizadas com muita frequência durante o código, pois guiavam o que iria acontecer de acordo com a gameplay. Tinham muitas funcionalidades, como checar colisões entre o player e os projéteis e mapa, checar se as armas já foram coletadas para serem utilizadas, se a vida do inimigo estava zerada, etc.
- **Loops:** Técnica utilizada para manter o código sempre atualizado, de acordo com a interação do jogador com o jogo.
- **Listas:** Utilizamos como forma de armazenamento de elementos, como spritesheets e armas.
- **Funções:** De extrema importância pro funcionamento do código, visto que as funções princiáis armazenavam as informações de cada fase e as demais o mantinham funcionando.

## 💡 Desafios e Lições Aprendidas
- **Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**
  - Não implementar uma técnica de modularização efetiva desde o início do projeto, no código base. Isso causou confusão entre o grupo, que sentiu dificuldade em entender as mudanças feitas no código pelos outros membros e na localização de partes específicas do código, pela grande quantidade de informação no mesmo espaço. Para resolver esse problema, o grupo se reuniu presencialmente, entendeu as mudanças feitas e dividiu as tarefas de cada um e o código em módulos mais específicos, de acordo com o que cada um estava trabalhando.
- **Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**
  - O processo de produção coletiva do código, além da dificuldade em utilizar o Git/GitHub. Como nenhum dos integrantes do grupo possuia familiaridade com a plataforma, no início do projeto era comum que houvesse muito conflito entre o código que estava sendo trabalhado por cada pessoa, resultando em processos de merge mais trabalhosos e uma evolução mais lenta. O desafio foi superado por meio da comunicação entre o grupo: foi criado um grupo no Whatsapp para atualizar das mudanças que estavam sendo feitas no projeto, novas ideias e planejamento dos próximos passos. Além disso, reuniões entre o grupo no Discord e a interação com os monitores responsáveis foi essencial para um melhor direcionamento.
- **Quais as lições aprendidas durante o projeto?**
  - Aprendizado de novas estratégias de organização de código, maior domínio dos conceitos de Programação Orientada a Objetos por meio de aulas, tutoriais e prática dentro do código, melhor dinâmica de trabalho em equipe e divisão de tarefas, através da colaboração e comunicação entre o grupo (fator fundamental para a evolução do projeto), contato com novas ferramentas, como o Aseprite (parte gráfica), Trello e Discord (organização e reuniões do grupo) e Git/GitHub (hospedagem e desenvolvimento do código)
## 📌 Instalação e Execução
