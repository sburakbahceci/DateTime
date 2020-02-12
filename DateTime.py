from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

tarih=datetime(2020,12,1)

suan=datetime.now()
print(tarih-suan)