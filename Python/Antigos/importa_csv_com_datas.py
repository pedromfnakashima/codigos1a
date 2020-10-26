import pandas as pd
import numpy as np
from pandas.compat import StringIO

csv = r'''Alguma linha inútil
Outra linha inútil
"a";"b";"c";"d";"e";"f";"g";"h";"i"
"20190101";"x";"1";"0,6";"x";"1";"Sim";"R$ 5,20";"3/11/2018"
"20190102";"x";"3";"0,1";"nada consta";"2";"Não";"R$ 2,10";"4/8/2015"
"20190103";"x";"5";"0,4";"y";"3";"Positivo";"R$ -4,35";"11/12/1995"
"20190101";"y";"1";"0,3";"nada consta";"4";"Não";"R$ abc";"23/4/2004"
"20190102";"y";"3";"0,5";"não encontrado";"5";"Sim";"R$ 1,57";"1/1/2008"
"20190103";"y";"5";"0,2";"z";"6";"Negativo";"R$ 0,8";"7/10/1984"
Linha final inútil
Outra linha final inútil
'''

#f1 = lambda x: float(x.replace(",",".").replace("R$ ",""))

f1 = lambda x: pd.to_numeric(x.replace("R$ ","").replace(",","."), errors="coerce")
f2 = lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce')

df = pd.read_csv(StringIO(csv),
                 header=2,
                 skipfooter=2,
                 delimiter = ';',
                 decimal = ",",
                 usecols=["a", "b", "c", "d", "e", "f", "g", "h", "i"],
                 dtype = {"f": "str"},
                 na_values = ["nada consta", "não encontrado"],
                 parse_dates=["a"], # só funciona quando está no formato padrão
                 true_values=["Sim", "Positivo"],
                 false_values=["Não", "Negativo"],
                 engine = "python",
                 converters={"h":f1, "i":f2})

df.dtypes


pd.to_numeric("2,4".replace(",",".").replace("R$ ",""), errors="coerce")
type(pd.to_numeric("2,4".replace(",",".").replace("R$ ",""), errors="coerce"))

dia1 = pd.to_datetime("3/11/2018", format='%d/%m/%Y', errors='coerce')
dia2 = pd.to_datetime("1/11/2018", format='%d/%m/%Y', errors='coerce')
nascimento = pd.to_datetime("11/12/1984", format='%d/%m/%Y', errors='coerce')
nascimento




dia1 = pd.to_datetime("1/11/2018 23:00:00", format='%d/%m/%Y %H:%M:%S', errors='coerce')
dia2 = pd.to_datetime("6/11/2018 15:00:00", format='%d/%m/%Y %H:%M:%S', errors='coerce')
dia3 = pd.to_datetime("6/11/2020 15:00:00", format='%d/%m/%Y %H:%M:%S', errors='coerce')


dia1
dia2
dia2 - dia1
dia3 - dia1
(dia3 - dia1).components

dia3 = dia2 + pd.to_timedelta('1 days 06:05:01.00003')
dia3 = dia1 + pd.to_timedelta('0 days 06:05:01')
dia3
dia3.hour
dia3.minute

import datetime
datetime.now()

nascimento = datetime.strptime("11/12/1984 3:00", "%d/%m/%Y %H:%M")
agora = datetime.now()

agora - nascimento
type(agora - nascimento)

datas1 = pd.date_range(pd.Timestamp("2018-03-10 09:00"),
                    periods=3, freq='Y')

datas2 = pd.to_datetime([1, 2, 3], unit='D',
                        origin=pd.Timestamp('2019-06-09'))

pd.to_timedelta(np.arange(24), unit='h')
pd.to_timedelta(np.arange(5), unit='d')

# idade. Pacote útil por conta de anos bissextos
import datetime
from dateutil.relativedelta import relativedelta

a = '2019-06-09 20:27:00'
b = '1984-12-11 03:00:00'

inicio = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
fim = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

diff = relativedelta(inicio, fim)

print(diff)

print(f"""A diferença é de:
    {diff.years} anos,
    {diff.months} meses,
    {diff.days} dias,
    {diff.hours} horas,
    {diff.minutes} minutos,
    {diff.seconds} segundos""")
    
##





