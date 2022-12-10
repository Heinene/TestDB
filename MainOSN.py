import pymssql as pm
import subprocess as sp


def truncate(out_table_name:str, connect):
    cursor = connect.cursor()
    cursor.execute(f'''Truncate table {out_table_name}''')
    cursor.close()
    print('Done Truncate')


def insert(in_table_name:str, out_table_name:str,connect):
    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {in_table_name} SELECT * FROM {out_table_name}''')
    cursor.close()
    print('Done insert1')


def in_many(in_table_name:str, values:tuple, connect):
    cursor = connect.cursor()
    sql = f"""INSERT {in_table_name} VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(sql, values)
    cursor.close()
    print('Done insert2')


def sozd(in_table_name:str,connect):
    try:
        a = []
        for po in range(len(Bame)):
            a.append(Bame[po] + ' NVARCHAR(50)')
        name_col = str(a)[1:-1].replace("'", '')
        cursor = connect.cursor()
        cursor.execute(f"""CREATE TABLE {in_table_name} (DB_Name NVARCHAR(50),{name_col});""")
        print(f'Create {in_table_name}')
        cursor.close()
    except:
        print('werwrf')
        connect.rollback()
        cursor.close()
        pass


def union(out_table_name:str,in_table_name_one:str, in_table_name_two:str,connect):
    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {out_table_name} Select * from {in_table_name_one} union Select * from {in_table_name_two}''')
    cursor.close()
    print('Done insert1')


def tabl(yesterday:str, today:str, all:str ):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL2')
    except:
        print('No connection with MSSQL2')
    else:
        sozd(yesterday, conn)
        sozd(today, conn)
        truncate(yesterday, conn)
        insert(yesterday, today, conn)
        truncate(today, conn)
        in_many(today, var, conn)
        sozd(all, conn)
        union(all,today,yesterday,conn)
        conn.commit()


with open('DB_name.txt','r') as f:
    for line in f:
        DB=line
        DB = DB.replace("\n", "")
        server = '"Len2"'
        #vibor = f""""select AdventureWorks2019.sys.schemas.name as Schema_name, AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name from AdventureWorks2019.sys.tables Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id"""
        vibor = f""""select {DB}.sys.schemas.name as Schema_Name, {DB}.sys.tables.name as Table_Name , {DB}.sys.columns.name as Col_Name, {DB}.sys.types.name as Type_Name from {DB}.sys.tables Join {DB}.sys.columns on {DB}.sys.tables.object_id= {DB}.sys.columns.object_id join {DB}.sys.types on {DB}.sys.types.system_type_id= {DB}.sys.columns.system_type_id join {DB}.sys.schemas on {DB}.sys.tables.schema_id = {DB}.sys.schemas.schema_id"""""
        path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
        p = sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
        var = p.decode(encoding='ascii').split('\r')
        var.pop(1)
        var.pop(-1)
        Bame = tuple(var[0].split())
        var.pop(0)
        for i in range(len(var)):
            var[i]=f'{DB}'+var[i]
            var[i] = tuple(var[i].split())
        var = tuple(var)
        tabl(f'TestBD.dbo.Yesterday_{DB}',f'TestBD.dbo.Today_{DB}','TestBD.dbo.allTable')
