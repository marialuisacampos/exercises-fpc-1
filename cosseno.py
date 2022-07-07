def exponenciacao(base, expoente):
  resultado = base
  for e in range(1, expoente):
    resultado *= 2
  return resultado

def cosseno(x):
  fatorial_anterior = 1
  resultado_final = 0

  for i in range(50):
    z = i * 2
    if (i == 0):
      resultado_final += 1 * exponenciacao(x, z)
    else:
      fatorial_atual = z * (z - 1) * fatorial_anterior
      fatorial_anterior = fatorial_atual
      resultado_final += (exponenciacao(-1, i) / fatorial_atual) * exponenciacao(x, z)

  return resultado_final
