# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:56:37 2020

@author: pedro
"""
globals().clear()

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

##############################
###### EXEMLPO 01 ############
##############################
"""  """
globals().clear()
import datetime

d = datetime.date(2016, 7, 24)

""" com 0: gera erro """
d = datetime.date(2016, 07, 24)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
""" que dia será daqui
1 semana """
print(tday + tdelta)
""" que dia foi 1 semana
atrás"""
print(tday - tdelta)
"""
date2 = date1 + timedelta
timedelta = date1 + date2
 """

bday = datetime.date(2020, 12, 11)
till_bday = bday - tday
print(till_bday.days)
print(till_bday.total_seconds())

##############################
###### EXEMLPO 02 ############
##############################
"""  """
globals().clear()
import datetime

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

##############################
###### EXEMLPO 03 ############
##############################
"""  """
globals().clear()
import datetime

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)

print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)

print(dt + tdelta)

##############################
###### EXEMLPO 04 ############
##############################
"""  """
globals().clear()
import datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

##############################
###### EXEMLPO 05 ############
##############################
"""  """
globals().clear()
import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

##############################
###### EXEMLPO 06 ############
##############################
"""  """
globals().clear()
import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)

##############################
###### EXEMLPO 07 ############
##############################
"""  """
globals().clear()
import datetime
import pytz

dt_mtn = datetime.datetime.now()
print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)

##############################
###### EXEMLPO 08 ############
##############################
"""  """
globals().clear()
import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

##############################
###### EXEMLPO 09 ############
##############################
"""
strftime: Datetime p/ String
strptime: String p/ Datetime
"""
globals().clear()
import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.isoformat())

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'October 21, 2020'

print('-----')

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)






##############################
###### EXEMLPO 10 ############
##############################
"""  """
globals().clear()
import datetime













