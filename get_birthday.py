#!/bin/python
# -*- coding: utf-8 -*-
import time
import better_spoken_numbers as bsn

from apcontent import alarmpi_content

class birthday(alarmpi_content):

  def build(self):
    birthday = None

    today = float(time.strftime("%m.%d"))
    
    if self._birthday(today):
      birthday = self._name()

    if birthday is None:
      birthday = self._default()
    else:
      birthday = 'Hoy es cumpleaños de ' + birthday 

    if self.debug:
      print birthday

    self.content = birthday

  def _default(self):
    if 'default' in self.sconfig:
      return self.sconfig['default']
    else:
      return ''

  def _birthday(self, today):
    if 'birthday' in self.sconfig:
      return today == float(self.sconfig['birthday'])
    else:
      self.sconfig['name'] = "Problema en la configuración del cumpleaños.  " + \
                             self._name() + \
                             "  no tiene un cumpleaños configurado."
      return True

  def _name(self):
    if 'name' in self.sconfig:
      return self.sconfig['name']
    return 'Unconfigured name'
