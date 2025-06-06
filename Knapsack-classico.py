itens = [ 
    (4,12),
    (2,2),
    (2,1),
    (1,1),
    (10,4)

]

capacidade_mochila = 15 
n = len(itens)
dp = [[0] * (capacidade_mochila + 1) for _ in range(n + 1)] 

for i in range(1, n + 1):
  valor, peso = itens[i-1] 
  for j in range(capacidade_mochila + 1): 
    if peso <= j:
      dp[i][j] = max(dp[i-1][j], valor + dp [i - 1][j - peso])
    else:
      dp[i][j] = dp[i-1][j] 

print(f"Valor maximo: ${dp[n][capacidade_mochila]}")

j = capacidade_mochila 

for i in range(n,0,-1):
  if dp[i][j] != dp[i-1][j]:
    valor, peso = itens[i-1] 
    print(f"Item {i}: Peso = {peso}, Valor = {valor}")
    j -= peso


      
  
