a : float = float(input("Ingrese numero:")) # El usuario ingresa un numero para adivinar 
b : float = 36.0 # El numero que el usuario debe adivinar
while a!=b : # Se repite el ciclo mientras que los numeros sean distintos
  if b>a: # Si el numero que se debe adivinar es mayor, se imprime que el numero es mayor
    print("El numero es mayor")
    a = float(input("Adivine de nuevo:")) # El usuario vuelve a adivinar
  else :
    print("El numero es menor") # Si el numero que se debe adivinar es menor, se imprime que el numero es menor
    a = float(input("Adivine de nuevo:")) # El usuario vuelve a adivinar
if a == b: # Si los numeros son iguales, se imprime los numeros son iguales
  print("Los numeros son iguales") 