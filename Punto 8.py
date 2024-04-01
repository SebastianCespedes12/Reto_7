def calculo_primo(n:int)->int: 
  j:int =2 # Se declarar e inicializa la variable j desde 2, ya que es el divisible mas pequeño que un numero puede tener sin contar 1
  primo_si: bool = True # Se inicializa la variable como Verdadera
  while j<n: # Se repite el ciclo mientras el posible divisor sea menor a el numero 
    if n%j == 0: # Si el modulo del numero y el divisor es igual a 0 tiene otro divisor ademas 1 y si mismo, entonces no es primo
      primo_si = False  # Se inicializa a Falso ya que no es primo
      break # Se rompe el ciclo ya que solo basta un divisor para no ser primo
    j+=1 # se suma 1 a j en cada paso
  if n == 1: # si el numero es 1, no es primmo 
    primo_si= False 
  if primo_si == True : # Si nunca se cambio a falso se imprime que el numero es primo
    print(str(n) + " es primo") 

i: int =1  # Desde que numero se van a imprimir los primos
x: int =100 # Hasta que numero se van a imprimir los primos
while i<=x: # Se repite el ciclo hasta que se llegue al limite superior
  calculo_primo(i) # Se comprueba si es primo para un numero
  i+=1  # Se suma 1 al limite inferior