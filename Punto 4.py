Poblacion_A_en_millones : float = 25   # Poblacion inicial de pais A
Poblacion_B_en_millones : float = 18.9 # Poblacion inicial de pais B
Año = 2022  # Año de inicio
while Poblacion_A_en_millones>Poblacion_B_en_millones: # Se repite el ciclo hasta que la poblacion del pais B supere la poblacion del pais A 
  Poblacion_A_en_millones += 0.02 # Se aumenta la poblacion por la tasa de crecimiento del pais A
  Poblacion_B_en_millones += 0.03 # Se aumenta la poblacion por la tasa de crecimiento del pais B
  if Poblacion_A_en_millones<Poblacion_B_en_millones:  # Si la poblacion del pais B supera la del pais A se rompe el ciclo
    break
  Año +=1 # Se aumenta el año por 1
print("La población del país B superará a la de A en: " + str(Año)) # Se imprime en que año la poblacion del pais B supero la del pais A