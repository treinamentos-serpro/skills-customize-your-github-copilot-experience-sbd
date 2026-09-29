# 📘 Atividade: Busca Binária em Java

## 🎯 Objetivo

Implemente e teste a busca binária em Java para localizar valores em arrays ordenados, praticando índices, limites e análise de eficiência de algoritmos.

## 📝 Tarefas

### 🛠️ Implementar a Busca Binária

#### Descrição
Crie uma classe `BinarySearch` e implemente uma busca binária iterativa para um array de inteiros em ordem crescente. A busca deve retornar o índice do valor procurado ou `-1` quando ele não estiver no array.

#### Requisitos
O programa concluído deve:

- Definir o método `public static int binarySearch(int[] values, int target)`
- Usar os limites inicial e final do intervalo de busca para calcular o índice do meio
- Reduzir o intervalo pela metade a cada comparação
- Retornar o índice correto quando o alvo existir e `-1` quando não existir


### 🛠️ Tratar Limites e Casos Especiais

#### Descrição
Revise as condições do loop e teste os casos em que os limites do intervalo mudam. Considere que um array pode estar vazio e que pode haver valores repetidos.

#### Requisitos
O programa concluído deve:

- Tratar um array vazio sem lançar uma exceção
- Encontrar valores no início, no meio e no fim do array
- Retornar `-1` para valores menores que o primeiro ou maiores que o último elemento
- Funcionar com valores repetidos, retornando qualquer índice válido que contenha o alvo

Use estes exemplos para verificar sua implementação:

```text
Array:  [-8, -2, 0, 4, 9, 15]
Alvo:   4   -> resultado esperado: 3
Alvo:   7   -> resultado esperado: -1
Array:  []  -> resultado esperado para qualquer alvo: -1
```


### 🛠️ Verificar a Eficiência do Algoritmo

#### Descrição
Teste a busca com arrays de tamanhos diferentes e explique como o intervalo de busca muda após cada comparação. Compare esse comportamento com uma busca que verifica os elementos um por um.

#### Requisitos
O programa concluído deve:

- Executar os testes sem bibliotecas externas, usando um método `main` ou testes equivalentes
- Confirmar os resultados para arrays pequenos e para um array maior com pelo menos 1.000 valores ordenados
- Explicar por que a busca binária exige que os valores estejam ordenados
- Comparar o número de verificações com uma busca linear e identificar a complexidade da busca binária como `O(log n)`