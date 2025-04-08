# IP-Project
## 🎮 Descrição do Projeto
O Projeto da disciplina de Introdução à Programação do semestre 2024.2 consiste na construção de um sistema interativo em ambiente 2D. Nele, o usuário controla um objeto com a finalidade de coletar outros objetos dispostos na tela, que serão registrados e exibidos ao usuário. O projeto é estruturado com base na **Programação Orientada a Objetos** e na linguagem **Python**.
## 👾 Sobre o Jogo
> inspirações, tutoriais, dinâmica

O (Nome do Jogo) é um jogo 2D estilo top-down shooter, que consiste no controle de um player, representado por um estudante de Matemática Discreta que precisa salvar seu professor Nivan. O jogo possui três fases, que são desbloqueadas após um combate contra Navin, um mago muito poderoso que sequestrou Nivan e ataca o jogador com o poder da matemática. A cada fase, uma nova arma é coletada, de forma que ela será guardada no inventario do player e poderá ser usada na próxima fase para derrotar Navin definitivamente e, assim, salvar Nivan.

> screenshot das fases e do jogo funcionando
## 🖲️ Contribuidores e Funções
- Davi Matoso <a href="https://github.com/DaviMatoso">(GitHub)</a>

- Isabella Mendes <a href="https://github.com/isabellamdsr">(GitHub)</a>
  - Implementação dos objetos coletáveis
  - Documentação do projeto

- Luan Romero <a href="https://github.com/luanromerolcc">(GitHub)</a>

- Sérgio Tavares <a href="https://github.com/teamfortr3ss2">(GitHub)</a>

- Jesper Ian <a href="https://github.com/j-iann">(GitHub)</a>

- Arthur Jorge <a href="https://github.com/Arfhum">(GitHub)</a>
## ✏️ Organização do Projeto
O código foi dividido em módulos para uma melhor organização:
- **Main:** Módulo principal que inicia o jogo. Por uma questão de organização, ele importa os módulos de cada fase do jogo;
- **fase1:** Módulo que engloba outros módulos, definindo o funcionamento da primeira fase;
- **fase2:** Módulo que engloba outros módulos, definindo o funcionamento da segunda fase;
- **moduloConfig:** Contém as configurações fixas do jogo, como dimensões da tela, configurações da soundtrack e da parte gráfica;
- **moduloDesenho:** Define uma classe de desenho para as imagens que aparecerão na tela;
- **moduloPlayer:** Define a classe do jogador e contém os atributos a ele relacionados, como imagem, hitbox, vida e perda/recuperação de vida, métodos de movimentação e colisão;
- **moduloColetaveis:** Define a classe dos coletáveis. Possui atributos de imagem (que deve sumir após o item ser coletado), identifição de colisão com o player e as especificações de cada item coletado;
- **moduloBala:** Criação das balas de cada arma de ataque do player, definindo imagem, movimentação, ãngulo e dano;
- **moduloArmaAtiva:** Módulo que "ativa" o funcionamento da arma atual, escolhida dependendo da tecla pressionada;
- **moduloProjetil:** Módulo que contém os ataques do inimigo, definindo imagem e forma de ataque;
- **moduloNAVIN:** Define as especificações do inimigo, como sua imagem, movimentação e dinãmica de dano tomado.

## 📚 Ferramentas Utilizadas
- **Pygame** - Framework de desenvolvimento de jogos
- **Aseprite** - Criação e animação de cenários e elementos gráficos
- **FL Studio** - Produção da soundtrack do jogo
- **Trello** - Gerenciamento de tarefas entre o grupo

> justificativas
## 📌 Instalação e Execução
