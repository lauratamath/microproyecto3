import numpy as np
import numpy_financial as npf
from colorama import Fore, Style

proyectoHotel = [
  (-800, 50),
  (-800, 100),
  (-700, 150),
  (300, 200),
  (400, 200),
  (500, 200),
  (2000, 8440)
]

proyectoCentroComercial = [
  (-600, 50),
  (-200, 50),
  (-600, 100),
  (250, 150),
  (350, 150),
  (400, 150),
  (1600,6000)
]

def simulate(valInicial, valores, low, high):
  array = [valInicial]
  for value in valores:
    array.append(np.random.normal(loc=value[0], scale=value[1], size=1)[0])

  array.append(np.random.uniform(low=low, high=high, size=1)[0])
  return array

valorPresenteCC = []
valorPresenteHotel = []
valorPresente = 0.1

# 100 iteraciones
for _ in range(100):
  simulacionCC = simulate(
    valInicial=-900,
    valores=proyectoCentroComercial,
    low=1600,
    high=6000
  )
  valorPresenteCC.append(npf.npv(valorPresente, simulacionCC))

for _ in range(100):
  simulacionHotel = simulate(
    valInicial=-800,
    valores=proyectoHotel,
    low=2000,
    high=8440
  )
  valorPresenteHotel.append(npf.npv(valorPresente, simulacionHotel))


promCC = np.mean(valorPresenteCC)
desvEstandarCC = np.std(valorPresenteCC)

promHotel = np.mean(valorPresenteHotel)
desvEstandarHotel = np.std(valorPresenteHotel)

print(Fore.GREEN + ">>>>>>>  100 iteraciones" + Style.RESET_ALL)
print(Fore.MAGENTA +'Valores del CC'+ Style.RESET_ALL)
print('Promedio:', round(float(promCC), 2))
print('Desviacion Estandar:', round(float(desvEstandarCC), 2))
print('Rango: [' + str(round(float((promCC - desvEstandarCC)), 2)), '-', 
  str(round(float((promCC + desvEstandarCC)), 2)) + ']')

print(Fore.CYAN + '\nValores del hotel' + Style.RESET_ALL)
print('Promedio:', round(float(promHotel), 2))
print('Desviacion Estandar:', round(float(desvEstandarHotel), 2))
print('Rango: [' + str(round(float((promHotel - desvEstandarHotel)), 2)), '-', 
  str(round(float((promHotel + desvEstandarHotel)), 2)) + ']\n')


## 1000 iteraciones 
for _ in range(1000):
  simulacionCC = simulate(
    valInicial=-900,
    valores=proyectoCentroComercial,
    low=1600,
    high=6000
  )
  valorPresenteCC.append(npf.npv(valorPresente, simulacionCC))

for _ in range(1000):
  simulacionHotel = simulate(
    valInicial=-800,
    valores=proyectoHotel,
    low=2000,
    high=8440
  )
  valorPresenteHotel.append(npf.npv(valorPresente, simulacionHotel))


promCC = np.mean(valorPresenteCC)
desvEstandarCC = np.std(valorPresenteCC)

promHotel = np.mean(valorPresenteHotel)
desvEstandarHotel = np.std(valorPresenteHotel)

print(Fore.GREEN + ">>>>>>>  1000 iteraciones" + Style.RESET_ALL)
print(Fore.MAGENTA +'Valores del CC' + Style.RESET_ALL)
print('Promedio:', round(float(promCC), 2))
print('Desviacion Estandar:', round(float(desvEstandarCC), 2))
print('Rango: [' + str(round(float((promCC - desvEstandarCC)), 2)), '-', 
  str(round(float((promCC + desvEstandarCC)), 2)) + ']')

print(Fore.CYAN + '\nValores del hotel' + Style.RESET_ALL)
print('Promedio:', round(float(promHotel), 2))
print('Desviacion Estandar:', round(float(desvEstandarHotel), 2))
print('Rango: [' + str(round(float((promHotel - desvEstandarHotel)), 2)), '-', 
  str(round(float((promHotel + desvEstandarHotel)), 2)) + ']\n')

## 10000 iteraciones 
for _ in range(10000):
  simulacionCC = simulate(
    valInicial=-900,
    valores=proyectoCentroComercial,
    low=1600,
    high=6000
  )
  valorPresenteCC.append(npf.npv(valorPresente, simulacionCC))

for _ in range (1000):
  simulacionHotel = simulate(
    valInicial=-800,
    valores=proyectoHotel,
    low=2000,
    high=8440
  )
  valorPresenteHotel.append(npf.npv(valorPresente, simulacionHotel))


promCC = np.mean(valorPresenteCC)
desvEstandarCC = np.std(valorPresenteCC)

promHotel = np.mean(valorPresenteHotel)
desvEstandarHotel = np.std(valorPresenteHotel)

print(Fore.GREEN + ">>>>>>>  10000 iteraciones" + Style.RESET_ALL)
print(Fore.MAGENTA +'Valores del CC' + Style.RESET_ALL)
print('Promedio:', round(float(promCC), 2))
print('Desviacion Estandar:', round(float(desvEstandarCC), 2))
print('Rango: [' + str(round(float((promCC - desvEstandarCC)), 2)), '-', 
  str(round(float((promCC + desvEstandarCC)), 2)) + ']')

print(Fore.CYAN + '\nValores del hotel' + Style.RESET_ALL)
print('Promedio:', round(float(promHotel), 2))
print('Desviacion Estandar:', round(float(desvEstandarHotel), 2))
print('Rango: [' + str(round(float((promHotel - desvEstandarHotel)), 2)), '-', 
  str(round(float((promHotel + desvEstandarHotel)), 2)) + ']\n')