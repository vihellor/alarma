#!/usr/bin/python
from math import floor

num2words = {0: 'Cero ', 1: 'Uno ', 2: 'Dos ', 3: 'Tres ', 4: 'Cuatro ', 5: 'Cinco ',
             6: 'Seis ', 7: 'Siete ', 8: 'Ocho ', 9: 'Nueve ', 10: 'Diez ',
            11: 'Once ', 12: 'Doce ', 13: 'Trece ', 14: 'Catorce ',
            15: 'Quince ', 16: '16 ', 17: 'Diecisiete ', 18: 'Dieciocho ', 19: 'Diecinueve ', 20: 'Veinte ', 30: 'Treinta ', 40: 'Cuarenta ',
            50: 'Cincuenta ', 60: 'Sesenta ', 70: 'Setenta ', 80: 'Ochenta ',
            90: 'Noventa '}

num2clima = {0: ' Tornado ', 1: ' Tormenta tropical ', 2: ' huracan ', 3: ' Tormentas electricas severas ', 
             4: ' Tormentas electricas ', 5: ' Combinación de lluvia y nieve ',
             6: ' Combinación de lluvia y aguanieve ', 7: ' Combinación de nieve y aguanieve ',
             8: ' Llovizna helada ', 9: ' Llovizna ', 10: ' lluvia helada ',
            11: ' Chubasco ', 12: ' Chubasco ', 13: ' Rafaga de nieve ', 14: ' Chubasco ligero de nieve ',
            15: ' Nieve que sopla ', 16: ' Nieve ', 17: ' Granizo ', 18: ' Aguanieve ',
            19: ' Polvo ', 20: ' Niebla ', 21: ' Neblina ', 22: ' Ahumado ',
            23: ' Tempestuoso ', 24: ' Ventosa ', 25: ' Frio ', 26: ' Nublado ',
            27: ' Mayormente nublado ', 28: ' Mayormente nublado ', 29: ' Parcialmente nublado ', 30: ' Parcialmente nublado ',
            31: ' Despejado ', 32: ' Soleado ', 33: ' Claro ', 34: ' Claro ',
            35: ' Mezcla de lluvia y granizo ', 36: ' Caliente ', 37: ' Tormenta electrica aislada ', 38: ' Tormenta electrica dispersa ',
            39: ' Tormenta electrica dispersa ', 40: ' Chubascos dispersas ', 41: ' Fuerte nevada ', 42: ' Parcialmente nublado '
            43: ' Fuerte nevada ', 44: ' Parcialmente nublado ', 45: ' Chubascos tormentosos ', 46: ' Chubascos de nieve '
            47: ' Chubascos tormentosos aislados ', 3200: 'No disponible'}


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
    
def n2c(n):
  try:
    return num2clima[n]
  except KeyError:
    return ' no especificado'


