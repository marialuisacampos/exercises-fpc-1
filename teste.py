def exponenciacao(base, expoente):
  resultado = base
  for e in range(1, expoente):
    resultado *= base
  return resultado

print(exponenciacao(-1, 3))