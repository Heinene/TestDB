import sys
import pymssql as pm
import subprocess as sp
import re
import os
import time

server = '"Len2"'

vibor = """"select AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name , AdventureWorks2019.sys.schemas.name as Schema_name , AdventureWorks2019.sys.columns.object_id from AdventureWorks2019.sys.tables  Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on  AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id where AdventureWorks2019.sys.tables.name= 'BusinessEntity'"""""
path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
p=sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
var = p.decode(encoding='ascii').split('\r')

var.pop(1)
var.pop(-1)
Bame = tuple(var[0].split())
print(Bame)
var.pop(0)
for i in range(len(var)):
    var[i] = tuple(var[i].split())
var = tuple(var)
o=str(var)
o=o[1:-1]


def tabl ():
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection')
    except:
        print('No connection')
    else:
        cursor = conn.cursor()
        cursor.execute(f"""
        IF OBJECT_ID('TestBD.dbo.Vigr', 'U') IS NOT NULL
        truncate table TestBD.dbo.Vigr
        INSERT TestBD.dbo.Vigr VALUES {o}
""")
        conn.commit()


if __name__ == "__main__":
    tabl()



    #for i in range (len (var)):
        #var[i]=tuple(var[i].split())
    #print(type(var))
    #print(type(var[0]))
    #print(type(var[1]))
    #print(type(var[2]))
    #print(type(var[3]))
    #print(var)
    #print(var[0])
    #print(var[1])
    #print(var[2])
    #print(var[3])
    #p=var[2].split()
    #print(var)
    #b=tuple(var[3].split())
    #print(type(b))
    #print(b)
    #print(u)
    #print(*p, sep=', ')
    #print(*(f'"{x}"' for x in p), sep=', ')
    #print(*var[0].split())
    #print(var[1].split())

