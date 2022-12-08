import pymssql as pm
import subprocess as sp
import datetime

server = '"Len2"'
vibor = """"select AdventureWorks2019.sys.schemas.name as Schema_name, AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name from AdventureWorks2019.sys.tables Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id"""""
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


def tabl():
    try:
        vivod1 = sp.check_output(
            f'''{path} -connection "HEIN-LENOVO7" -sql "IF OBJECT_ID (N'TestBD.dbo.Today', N'U') IS  NULL SELECT 0 AS res ELSE SELECT 1 AS res" -output result''')
        vi1 = vivod1.decode(encoding='ascii').split('\r')
        if (vi1[2].split()[0]) == '0':
            try:
                conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
                print('Successful connection with MSSQL1')
            except:
                print('No connection with MSSQL1')
            else:
                print('Create table')
                a = []
                for po in range(len(Bame)):
                    a.append(Bame[po] + ' NVARCHAR(50)')
                name_col = str(a)[1:-1].replace("'", '')
                cursor = conn.cursor()
                cursor.execute(
                    f"""IF OBJECT_ID('TestBD.dbo.Today', 'U') IS NULL CREATE TABLE TestBD.dbo.Today({name_col});""")
                conn.commit()
                cursor.close()
                conn.close()
        else:
            print('Table exist')
    except:
        print('Problem with DBVIS')
    else:
        try:
            conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
            print('Successful connection with MSSQL2')
        except:
            print('No connection with MSSQL2')
        else:
            print('Zapoln table')
            a = str(datetime.date.today())
            gg = ('Log_za_' + a).replace('-', '_')
            cursor = conn.cursor()
            cursor.execute(f'''
            DROP TABLE TestBD.dbo.{gg}
            SELECT * INTO TestBD.dbo.{gg} FROM TestBD.dbo.Today
            truncate table TestBD.dbo.Today''')
            sql = """INSERT TestBD.dbo.Today VALUES (%s, %s, %s, %s)"""
            cursor.executemany(sql, var)
            conn.commit()


tabl()
