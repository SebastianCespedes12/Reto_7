n : int = int(input("Numero  n>=2: ")) # El usuario ingresa un numero mayor o igual que 2
while n>=2 : # Se repite el ciclo mientras quue el numero sea mayor o igual a 2
  if n%2 == 0 : # Si el numero es par se imprime si mismo
    print(n) 
  else : # Si el numero es impar se le resta uno para volverse par e imprimirse
    print(n-1)
  n-=2  # Se resta 2 al numero ya que par-2 = par anterior