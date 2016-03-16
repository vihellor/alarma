#!/usr/bin/python
from math import floor

num2words = {0: 'Cero ', 1: 'Uno ', 2: 'Dos ', 3: 'Tres ', 4: 'Cuatro ', 5: 'Cinco ',
             6: 'Seis ', 7: 'Siete ', 8: 'Ocho ', 9: 'Nueve ', 10: 'Diez ',
            11: 'Once ', 12: 'Doce ', 13: 'Trece ', 14: 'Catorce ',
            15: 'Quince ', 16: '16 ', 17: 'Diecisiete ', 18: 'Dieciocho ', 19: 'Diecinueve ', 20: 'Veinte ', 30: 'Treinta ', 40: 'Cuarenta ',
            50: 'Cincuenta ', 60: 'Sesenta ', 70: 'Setenta ', 80: 'Ochenta ',
            90: 'Noventa '}

num2clima = {0: ' Tornado ', 1: ' Tormenta tropical ', 2: ' huracan ', 3: ' Tormentas electricas severas ', 
             4: ' Tormentas electricas ', 5: ' Combinacion de lluvia y nieve ',
             6: ' Combinacion de lluvia y aguanieve ', 7: ' Combinacion de nieve y aguanieve ',
             8: ' Llovizna helada ', 9: ' Llovizna ', 10: ' lluvia helada ',
            11: 'Once ', 12: 'Doce ', 13: 'Trece ', 14: 'Catorce ',
            15: 'Quince ', 16: 'Veinte ', 3200: 'No disponible'}

num2cient = {1: 'ciento ', 2: 'Doscientos ', 3: 'Trescientos ', 4: 'Cuatrocientos ', 5: 'Quinientos ',
             6: 'Seiscientos ', 7: 'Setecientos ', 8: 'Ochocientos ', 9: 'Novecientos '}
            
num2month = {0: 'Enero ', 1: 'Febrero ', 2: 'Marzo ', 3: 'Abril ', 4: 'Mayo ', 5: 'Junio ',
             6: 'Julio ', 7: 'Agosto ', 8: 'Septiembre ', 9: 'Octubre ', 10: 'Noviembre ',
            11: 'Diciembre '}
            
num2day = {0: 'Domingo ', 1: 'Lunes ', 2: 'Martes ', 3: 'Miercoles ', 4: 'Jueves ', 5: 'Viernes ',
             6: 'Sabado '}


def n2w(n):
  return n

def d2w(n):
  if n == 1:
    return 'primero'
  else:
    return n
    
def n2m(n):
  try:
    return num2month[n-1]
  except KeyError:
    return 'mes fuera de rango'
    
def n2d(n):
  try:
    return num2day[n]
  except KeyError:
    return 'dia fuera de rango'


