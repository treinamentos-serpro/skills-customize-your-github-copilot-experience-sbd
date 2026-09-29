# 📘 Tarefa: Jogo da Forca

## 🎯 Objective

Pratique conceitos fundamentais de Python, como listas, condicionais, laços e entrada de dados, ao criar um jogo interativo da forca.

## 📝 Tasks

### 🛠️ Seleção de Palavra e Estado do Jogo

#### Descrição
Implemente a lógica inicial do jogo, incluindo uma lista de palavras e uma representação da palavra oculta com espaços ou underscores.

#### Requisitos
O programa completo deve:

- Definir uma lista com palavras possíveis
- Escolher uma palavra aleatoriamente
- Exibir a palavra como `_ _ _` com o mesmo número de letras
- Manter o estado do jogo para rastrear letras adivinhadas e tentativas restantes

### 🛠️ Entrada do Usuário e Validação

#### Descrição
Permita que o jogador insira letras e atualize o progresso do jogo com feedback em tempo real.

#### Requisitos
O programa completo deve:

- Solicitar ao usuário uma letra
- Verificar se a letra faz parte da palavra
- Atualizar a visualização da palavra oculta
- Informar se a tentativa foi correta ou incorreta
- Evitar erros de entrada duplicados ou valores inválidos

### 🛠️ Vitória e Derrota

#### Descrição
Finalize o jogo quando a palavra for completamente revelada ou quando as tentativas acabarem.

#### Requisitos
O programa completo deve:

- Contar tentativas erradas restantes
- Encerrar com mensagem de vitória quando o jogador adivinha a palavra
- Encerrar com mensagem de derrota quando as tentativas acabarem
- Exibir a palavra correta ao final