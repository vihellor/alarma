#!/bin/python
# -*- coding: utf-8 -*-
import time
import better_spoken_numbers as bsn

from apcontent import alarmpi_content

class greeting(alarmpi_content):
  def build(self):
    diaSem=str(bsn.n2d(int(time.strftime("%d"))))
    diaMes=str(bsn.d2w(int(time.strftime("%d"))))
    mes=str(bsn.n2m(int(time.strftime("%m"))))

    now = diaSem + ' ' +  diaMes + ' de ' + mes + ',' + time.strftime(" %I %M %p")

    if int(time.strftime("%H")) < 12:
      period = 'os dias'
    if int(time.strftime("%H")) >= 12:
      period = 'as tardes'
    if int(time.strftime("%H")) >= 17:
      period = 'as noches'

    # reads out good morning + my name
    gmt = 'Buen' + period + ', '

    # reads date and time 
    day = ' Hoy es ' + now + '.  '

    greeting = gmt + self.sconfig['name'] + day

    if self.debug:
      print greeting

    self.content = greeting
