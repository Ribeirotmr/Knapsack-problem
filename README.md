# Problema da Mochila (Knapsack Problem)

## Introdução

O problema da mochila é um problema clássico de otimização. Imagine que você tem uma mochila com capacidade limitada de peso, e vários itens, cada um com um certo peso e valor. Seu objetivo é escolher quais itens colocar na mochila de forma que o valor total dos itens seja o maior possível, sem ultrapassar o limite de peso.

Esse problema aparece em várias situações reais, como alocação de recursos, seleção de projetos e até em logística.

## Formulação matemática

Matematicamente, o problema é representado assim:

$$
\text{maximizar } \sum_{j=0}^{N-1} v_j x_j
$$

Sujeito a:

$$
\sum_{j=0}^{N-1} w_j x_j \leq W
$$

Onde:
- $N$ = número de itens
- $v_j$ = valor do item $j$
- $w_j$ = peso do item $j$
- $W$ = capacidade total da mochila
- $x_j \in \{0,1\}$ indica se o item foi escolhido (1) ou não (0)

## Formulação binária

Cada possível solução é representada por uma sequência de bits:

$$
x = <x_0, x_1, ..., x_{N-1}>
$$

Se $x_j = 1$, o item está na mochila. Se $x_j = 0$, ele não está.

Por exemplo, se temos 4 itens, a solução $x = 1010$ significa que selecionamos o item 0 e o item 2.

## Função de custo

A função de custo é o total de valor dos itens escolhidos:

$$
v(x) = \sum_{j=0}^{N-1} v_j x_j
$$

Mas precisamos garantir que o peso não ultrapasse $W$. Se ultrapassar, podemos penalizar essa solução, para que ela não seja considerada boa no processo de otimização.

## Comparação: Solução Clássica vs. Quântica

### **Solução Clássica**

Na computação clássica, existem vários algoritmos para resolver o problema da mochila:

- **Força bruta:** Testar todas as combinações possíveis (complexidade $O(2^N)$).
- **Programação dinâmica:** Resolve casos do problema com complexidade $O(N \cdot W)$.
- **Algoritmos aproximados:** Encontram boas soluções mais rápido, mas não garantem a melhor possível.

A medida que o número de itens cresce, o tempo cresce exponencialmente para métodos exatos.

### **Solução Quântica (QAOA)**

Na computação quântica, utilizamos algoritmos como o **QAOA (Quantum Approximate Optimization Algorithm)** para encontrar boas soluções.

Como funciona:
- Cada qubit representa se um item foi escolhido ou não ($x_j$).
- A função objetivo e as restrições são transformadas em **Hamiltonianos**, que controlam a evolução do sistema quântico.
- O sistema explora simultaneamente várias combinações graças à **superposição quântica**, procurando aquela com maior valor sem ultrapassar o limite de peso.
- Usamos portas quânticas para penalizar estados inválidos (que excedem o peso).

Vantagens da abordagem quântica:
- Pode explorar muitas soluções em paralelo.
- Tem potencial para resolver certos problemas de otimização mais rápido do que métodos clássicos (principalmente em larga escala, no futuro com computadores quânticos mais avançados).

## Como representar na computação quântica?

As variáveis clássicas $x_j$ são mapeadas para qubits. Cada $x_j$ vira um operador quântico:

$$
x_j = \dfrac{1}{2}(1 - Z_j)
$$

Onde $Z_j$ é o operador de Pauli-Z, que mede se o qubit está no estado $\vert 0 \rangle$ ou $\vert 1 \rangle$.

### Hamiltoniano da função objetivo:

$$
H_v = \sum_{j=0}^{N-1} v_j \dfrac{1}{2}(1 - Z_j)
$$

### Hamiltoniano da restrição (penalidade se ultrapassar peso):

$$
H_p = -a \cdot \max(0, w(x) - W)
$$

O Hamiltoniano total é:

$$
H_C = H_v + H_p
$$

O sistema é então evoluído utilizando dois tipos de operadores:
- **Operador de fase (U_C):** Relacionado à função objetivo (maximizar o valor).
- **Operador de mistura (U_B):** Permite a transição entre diferentes estados (explorar soluções).

## Vantagem da Quantização

- A abordagem quântica permite testar muitas combinações de forma paralela devido à **superposição**, algo impossível na computação clássica.
- Além disso, o **emaranhamento** permite que as escolhas dos itens sejam correlacionadas, facilitando encontrar soluções que fazem mais sentido considerando a restrição.

## Conclusão

O problema da mochila é um exemplo perfeito para mostrar como algoritmos quânticos podem ser aplicados à otimização. Enquanto na computação clássica dependemos de métodos exatos ou heurísticos, na computação quântica usamos propriedades como superposição e emaranhamento para explorar rapidamente muitas soluções.

Atualmente, os computadores quânticos ainda são limitados, mas pesquisas e simulações mostram que algoritmos como o QAOA têm potencial para superar abordagens clássicas em certos tipos de problemas de otimização no futuro.

