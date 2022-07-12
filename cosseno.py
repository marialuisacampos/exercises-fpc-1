def exponenciacao(base, expoente):
  resultado = base
  for e in range(1, expoente):
    resultado *= base
  return resultado

def cosseno(x):
  fatorial_anterior = 1
  resultado_final = 0

  for i in range(50):
    z = i * 2
    if (i == 0):
      resultado_final += 1
      print(f'Resultado final {i} = {resultado_final}')
    else:
      fatorial_atual = z * (z - 1) * fatorial_anterior
      fatorial_anterior = fatorial_atual
      resultado_final += (exponenciacao(-1, i) / fatorial_atual) * exponenciacao(x, z)
      print(f'Resultado final {i} = {resultado_final}')

  return resultado_final

x = float(input('Digite o grau em radianos:'))
total = cosseno(x)
print("%.4f"%total)