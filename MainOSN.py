import pymssql as pm
import subprocess as sp

server = '"Len2"'
vibor = f""""select AdventureWorks2019.sys.schemas.name as Schema_Name, AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name from AdventureWorks2019.sys.tables Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id"""""
path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
p = sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
var = p.decode(encoding='ascii').split('\r')
var.pop(1)
var.pop(-1)
Bame = tuple(var[0].split())
var.pop(0)
for i in range(len(var)):
    var[i] = tuple(var[i].split())
var = tuple(var)


def truncate(out_table_name:str, connect):
    cursor = connect.cursor()
    cursor.execute(f'''Truncate table {out_table_name}''')
    connect.commit()
    print('Done Truncate')


def insert(in_table_name:str, out_table_name:str,connect):
    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {in_table_name} SELECT * FROM {out_table_name}''')
    connect.commit()
    print('Done insert')


def in_many(in_table_name:str, values:tuple, connect):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection to insert')
    except:
        print('No connection with insert')
    else:
        cursor = connect.cursor()
        sql = f"""INSERT {in_table_name} VALUES (%s, %s, %s, %s)"""
        cursor.executemany(sql, values)
        conn.commit()
        print('Done insert')


def sozd(in_table_name:str,connection):
    a = []
    for po in range(len(Bame)):
        a.append(Bame[po] + ' NVARCHAR(50)')
    name_col = str(a)[1:-1].replace("'", '')
    check = sp.check_output(f'''{path} -connection "HEIN-LENOVO7" -sql "IF OBJECT_ID (N'{in_table_name}', N'U') IS  NULL SELECT 0 AS res ELSE SELECT 1 AS res" -output result''')
    che = check.decode(encoding='ascii').split('\r')
    if (che[2].split()[0]) == '0':
        cursor = connection.cursor()
        cursor.execute(f"""IF OBJECT_ID('{in_table_name}', 'U') IS NULL CREATE TABLE {in_table_name}({name_col});""")
        connection.commit()
        print(f'Create {in_table_name}')
    else:
        return


def tabl(inn:str, outt:str):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL2')
    except:
        print('No connection with MSSQL2')
    else:
        sozd(inn, conn)
        sozd(outt, conn)
        truncate(inn, conn)
        insert(inn, outt, conn)
        truncate(outt, conn)
        in_many(outt, var, conn)


tabl('TestBD.dbo.Yesterdayt','TestBD.dbo.Todayt')

