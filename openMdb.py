import pyodbc
path = r'G:\corpus\corpus\data\recip1m\data.mdb'
conn1 = pypyodbc.connect(u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path)
cur1 = conn1.cursor()
print(list(cur1.tables()))


