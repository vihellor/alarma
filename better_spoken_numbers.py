#!/usr/bin/python
from math import floor

num2words = {0: 'Cero ', 1: 'Uno ', 2: 'Dos ', 3: 'Tres ', 4: 'Cuatro ', 5: 'Cinco ',
             6: 'Seis ', 7: 'Siete ', 8: 'Ocho ', 9: 'Nueve ', 10: 'Diez ',
            11: 'Once ', 12: 'Doce ', 13: 'Trece ', 14: 'Catorce ',
            15: 'Quince ', 16: ' ', 17: 'Seventeen ', 18: 'Eighteen ',
            19: 'Nineteen ', 20: 'Veinte ', 30: 'Treinta ', 40: 'Cuarenta ',
            50: 'Cincuenta ', 60: 'Sesenta ', 70: 'Setenta ', 80: 'Ochenta ',
            90: 'Noventa '}
num2cient = {1: 'ciento ', 2: 'Doscientos ', 3: 'Trescientos ', 4: 'Cuatrocientos ', 5: 'Quinientos ',
             6: 'Seiscientos ', 7: 'Setecientos ', 8: 'Ochocientos ', 9: 'Novecientos '}
            
num2month = {0: 'Enero ', 1: 'Febrero ', 2: 'Marzo ', 3: 'Abril ', 4: 'Mayo ', 5: 'Junio ',
             6: 'Julio ', 7: 'Agosto ', 8: 'Septiembre ', 9: 'Octubre ', 10: 'Noviembre ',
            11: 'Diciembre '}
            
num2day = {0: 'Domingo ', 1: 'Lunes ', 2: 'Martes ', 3: 'Miercoles ', 4: 'Jueves ', 5: 'Viernes ',
             6: 'Sabado '}


def n2w(n):
  if n<=15:
    return num2words[n]
  elif n<20:
    words= 'diez y '
    words+= num2words[n%10]
  elif n<100:
    words=num2words[n-n%10]
    if n%10>0:
      words+= 'y ' +num2words[n%10]
    return words
  elif n==100:
    word= 'cien '
  elif n<1000:
    hundreds=(n-n%100)/100
    tens=(n%100)-(n%100)%10
    singles=n-((hundreds*100)+tens)
    words=num2cient[hundreds]
    if tens > 0:
      words+=num2words[tens] + 'y '
    if singles > 0:
      words+=num2words[singles]
    return words
  elif n<1000000:
    thousands=(n-n%1000)/1000
    remainder=n-(thousands*1000)
    words=n2w(thousands)+' mil '
    if remainder>0:
      words+=' '+n2w(remainder)
    return words
  elif n<1000000000:
    millions=(n-n%1000000)/1000000
    remainder=n-(millions*1000000)
    if millions ==1:
      words= 'un millon '
    else:
      words=n2w(millions)+' millones'
    if remainder>0:
      words+=' '+n2w(remainder)
    return words
  else:
    return 'Numero fuera de rango'

def d2w(n):
  if n == 1:
    return 'primero'
  else:
    return n2w(n)
    
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

