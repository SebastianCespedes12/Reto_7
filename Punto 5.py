n: int = int(input("Ingrese numero natural: ")) #Se ingresa el numero para dar el factorial
N=n # Se guarda el valor inicial en el valor N
Factorial : int = 1 # El factorial se empieza por 1
while n >= 1 : # Se repite el ciclo mientras que el numero sea mayor o igual a 1 
  Factorial *= n	# El factorial se multiplica por el numero
  n-=1 # El numero se resta por uno y se repite el ciclo
print("El factorial de " +str(N)+" es "+str(Factorial))  # Se imprime el numero y su factorial 