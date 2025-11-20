RPG OO — Aventura em Texto
Um jogo de RPG baseado em turnos e orientado a objetos, desenvolvido em Python. O projeto conta com sistema de criação de personagens, combate tático, progressão de nível, inventário e diferentes arquétipos de heróis e inimigos.

Índice
Como Rodar

Estrutura do Projeto

Mecânicas de Jogo

Documentação Técnica (Classes e Funções)

Autores

Como Rodar
Pré-requisitos
Python 3.8 ou superior instalado.

Passo a Passo
Extraia os arquivos do projeto.

Abra o terminal na pasta raiz rpg_base.

Execute o arquivo principal:

Bash

python main.py
(Ou python3 main.py dependendo do seu sistema operacional)

Estrutura do Projeto
O projeto segue uma arquitetura MVC simplificada, onde main.py e jogo.py controlam o fluxo, e a pasta models/ contém a lógica de negócios.

Plaintext

rpg_base/
│
├── main.py              # Ponto de entrada (Entry Point)
├── jogo.py              # Controlador principal (Menus, Save/Load, Gerenciamento)
├── README.md            # Documentação
│
└── models/              # Núcleo da lógica OO
    ├── base.py          # Classes base (Entidade, Atributos, Item)
    ├── personagem.py    # Lógica do Jogador (XP, Skills, Inventário)
    ├── inimigo.py       # Lógica dos Inimigos (Factories, AI Simples)
    ├── missao.py        # Loop de Combate (Turnos)
    └── efeitos.py       # Buffs e Debuffs (Status Effects)
Mecânicas de Jogo
Arquétipos (Classes)
Cada classe possui atributos base e taxas de crescimento (stats ganhos ao subir de nível) diferentes:

Guerreiro: Alta Defesa e Vida. Habilidade: Escudo de Guerra.

Mago: Dano Verdadeiro alto e regen de mana. Habilidade: Amplificação Arcana.

Arqueiro: Focado em Crítico. Habilidade: Foco do Caçador.

Paladino: Tanque com cura. Habilidade: Bênção Divina.

Espadachim: Dano explosivo (Burst). Habilidade: Zandatsu.

Combate
Dano Normal: Reduzido pela Defesa do inimigo.

Dano Verdadeiro: Ignora a defesa (comum em Magos).

Crítico: Multiplica o dano final.

Sangramento: Dano contínuo por turnos (usado pelo Boss).

Documentação Técnica
Abaixo estão as descrições das classes e métodos essenciais para o funcionamento do sistema.

1. models/missao.py (Loop de Batalha)
Responsável por executar a lógica turno a turno.

class Missao:

executar(p: Personagem) -> ResultadoMissao: O coração do jogo. Controla o loop while p.vivo and i.vivo. Gerencia turnos, cooldowns de efeitos, input do jogador (Atacar, Skill, Item) e a resposta do inimigo.

2. models/personagem.py (O Herói)
Herda de Entidade. Contém a lógica específica do jogador.

calcular_dano_base(): Retorna uma tupla (dano_normal, dano_verdadeiro). Verifica buffs ativos (ex: buff de Mago ou Arqueiro) e calcula chance crítica.

habilidade_especial(): Verifica a classe do personagem e instancia o Efeito correspondente (ex: EscudoDeGuerra), aplicando-o na lista efeitos_ativos.

ganhar_xp(valor): Adiciona XP e chama verificar_subir_nivel().

usar_item(nome): Consome um item do inventário para restaurar vida.

3. models/inimigo.py (O Oponente)
Herda de Entidade. Usa o padrão Factory Method para gerar inimigos variados.

Métodos de Fábrica (ex: GoblinNormal, ReiDoBostil, EsqueletoBalisticoCavernal): Métodos estáticos que instanciam inimigos com stats baseados na dificuldade e no nível do jogador.

atacar(): Retorna o dano causado ao jogador.

atacar_especial(): Lógica específica para Bosses (ex: o Boss "Globin" tem chance de aplicar sangramento).

_calcular_multiplicador_nivel: Escala a força do inimigo conforme o nível do jogador aumenta.

4. jogo.py (Controlador)
Gerencia o estado global da sessão.

_gerar_inimigo_aleatorio(): Seleciona um inimigo com base no cenário escolhido (Floresta, Caverna, Ruínas, etc.) e na dificuldade.

menu_criar_personagem(): Interface para definir nome e arquétipo.

_salvar_no_arquivo() / _carregar_do_arquivo(): Persistência de dados usando JSON. Serializa o objeto Personagem e seu inventário.

5. models/efeitos.py (Buffs)
Sistema polimórfico para status temporários.

class Efeito: Classe base. Possui duração em turnos.

aplicar(alvo) / remover(alvo): Métodos abstratos implementados por subclasses (ex: EscudoDeGuerra adiciona DEF ao aplicar e remove ao expirar).

6. models/base.py
Entidade: Classe pai. Possui Vida, Ataque, Defesa e gerencia receber_dano().

Atributos: Dataclass que agrupa todos os stats numéricos (HP, Mana, Crit, etc.).

Autores
Integrantes do grupo responsáveis pelo desenvolvimento:

Philipi Oliveira de Camargo Montini

Otávio Augusto Silva Santos

Artur Santos Silva

Bruno Hora Almeida

Guilherme Gonçalves de Andrade Rocha