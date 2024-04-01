n : int = int(input("Ingrese numero de 2 a 50: ")) # El usuario ingresa un numero  
divs : int = 1 # Se empieza el divisor desde 1, ya que el divisible mas pequeño que un numero puede tener  
while n>=2 and n<=50: # Si el numero esta entre 2 y 50 entra al ciclo
  if n%divs == 0 : # Se imprime el divisor si el modulo es igual a 0
    print(str(divs) + " es divisor de " + str(n))   
  divs +=1 # Se suma 1 al posible divisor
  if divs >= n : # Se finaliza el ciclo si el divisor es igual a el numero, ya que es el ultimo divisor posible
    break