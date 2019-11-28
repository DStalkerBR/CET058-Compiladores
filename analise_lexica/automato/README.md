---
Universidade Estadual de Santa Cruz
Disciplina: Compiladores
Discente: Jhonata de Araújo Nascimento
---

# Implementação de um Analisador Léxico

Algoritmo que utiliza um autômato AFD para reconhecer expressões matemáticas no formato:

```
a + b - c
a * c - a
a - b / c
```

## Como funciona
O algoritmo utiliza um AFD com *tokens* previamente definidos para a analise léxica. (Identificador, Soma, Subtração, Multiplicação e Divisão)

Onde é lida uma letra da entrada e baseado na tabela de transições, um dicionário neste caso, é feita a mudança de estado. 

Se o estado final em que se encontrar for um estado de aceitação, então a cadeia lida até aquele ponto é um lexema válido que pode ter um *token* atribuído.

## Como executar

```
python3 automato.py 
```
Passando um arquivo de entrada:

```
python3 automato.py arquivo_de_entrada
```
## Dificuldades
Houve um pouco de dificuldade inicial em como implementar o autômato em código e como estabelecer o que exatamente definiria o reconhecimento de um lexema válido, porem foi facilmente resolvido com a utilização dos estados de aceitação do autômato.

Inicialmente havia a ideia de permitir a utilização de expressões regulares (do tipo [A-Za-Z]) para definir os autômatos, tornando possível abranger casos diferentes mais facilmente, mas foi descartada devido a sua complexidade, além de não ser realmente necessário para o escopo da atividade solicitada.