i : int = 1  # Desde que numero se va a imprimir
while i<=100: # Se repite el ciclo hasta que llegemos al ultimo numero (100)
  cuadrado : int = i**2 # La variable cuadrado se asigna al cuadrado del numero
  print("numero: "+ str(i) + ", "+ "cuadrado: " + str(cuadrado) ) # Se imprime el numero y su cuadrado
  i+=1   # Suma 1 al numero 