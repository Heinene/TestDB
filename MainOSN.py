import pymssql as pm
import subprocess as sp
import datetime

def union(out_table_name: str, in_table_name_one: str, in_table_name_two: str, connect):

    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {out_table_name} Select * from {in_table_name_one} union Select * from {in_table_name_two}''')
    cursor.close()
    print(f'Done union {out_table_name} = {in_table_name_one} + {in_table_name_two}')
def dobavlenie(today_table_name: str, yesterday_table_name: str, out_table_name: str, connect):
    cursor = connect.cursor()
    cursor.execute(
        f'''INSERT INTO {out_table_name} select * from {today_table_name} except select * from {yesterday_table_name}''')
    cursor.close()
    print(f'Done dobavlenie {out_table_name}= {today_table_name} - {yesterday_table_name}')
def udalenie(today_table_name: str, yesterday_table_name: str, out_table_name: str, connect):
    cursor = connect.cursor()
    cursor.execute(
        f'''INSERT INTO {out_table_name} select * from {yesterday_table_name} except select * from {today_table_name}''')
    cursor.close()
    print(f'Done udalenie {out_table_name} = {yesterday_table_name} - {today_table_name}')
def sozdanie_schem(schema_name:str, connect):
    try:
        cursor = connect.cursor()
        cursor.execute(f"""CREATE SCHEMA {schema_name};""")
        print(f'Create {schema_name}')
        cursor.close()
    except:
        print('no sozd schema')
        connect.rollback()
        cursor.close()
        pass
def sozdanie(in_table_name: str, connect):
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
        print(f'no sozd table {in_table_name}')
        connect.rollback()
        cursor.close()
        pass
def sozdanie_date (in_table_name:str,connect):
    try:
        cursor = connect.cursor()
        cursor.execute(f"""CREATE TABLE {in_table_name} (NAME NVARCHAR(150) , UNIQUE (NAME))""")
        print(f'Create {in_table_name}')
        cursor.close()
        return in_table_name
    except:
        print(f'no sozd table {in_table_name}')
        connect.rollback()
        cursor.close()
        return in_table_name
        pass
def sozdanie_coll (in_table_name:str,connect):
    try:
        cursor = connect.cursor()
        date = str(datetime.datetime.now())
        date = date.replace('-', "_").replace(' ', "_").replace(':', "_").replace('.', "_")
        date = 'log' + date
        cursor.execute(f"""ALTER TABLE {in_table_name} ADD {date} NVARCHAR(50)""")
        print(f'Create coll {in_table_name}')
        cursor.close()
        return date
    except:
        print(f'no sozd coll {in_table_name}')
        return date
        connect.rollback()
        cursor.close()
        pass
def truncate(out_table_name: str, connect):
    cursor = connect.cursor()
    cursor.execute(f'''Truncate table {out_table_name}''')
    cursor.close()
    print(f'Done Truncate {out_table_name}')
def insert(in_table_name: str, out_table_name: str, connect):
    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {in_table_name} SELECT * FROM {out_table_name}''')
    cursor.close()
    print(f'Done insert {in_table_name}->{out_table_name}')
def insert_one(in_table_name: str, value: str, connect):
    cursor = connect.cursor()
    cursor.execute(f'''INSERT INTO {in_table_name} (NAME) select BAME from (VALUES {value}) Ta(BAME) except select NAME from {in_table_name}''')
    cursor.close()
    print(f'Done insert {in_table_name}-> values')
def in_many(in_table_name: str, values: tuple, connect):
    cursor = connect.cursor()
    sql = f"""INSERT {in_table_name} VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(sql, values)
    cursor.close()
    print(f'Done many insert {in_table_name}')
def one_many(in_table_name: str, values: tuple, connect):
    cursor = connect.cursor()
    sql = f"""INSERT {in_table_name} (NAME) VALUES (%s)"""
    cursor.executemany(sql, values)
    cursor.close()
    print(f'Done one insert {in_table_name}')
def obrabotka(variable: str) -> tuple:
    variable = f.decode(encoding='ascii').split('\r')
    variable.pop(1)
    variable.pop(-1)
    variable.pop(0)
    for i in range(len(variable)):
        variable[i] = tuple(variable[i].split())
    return variable
def list_table(first:str,second:str,connect)->list:
    cursor = connect.cursor()
    a = []
    cursor.execute(f'''SELECT * FROM {first}''')
    for i in cursor:
        a.append(i)
    b = []
    cursor.execute(f'''SELECT * FROM {second}''')
    for i in cursor:
        b.append(i)
    table_list = [item for item in a if item not in b]
    table_list=tuple(table_list)
    return table_list
    cursor.close()
def obedn(in_table_name:str, connect):
    a = []
    cursor = connect.cursor()
    cursor.execute(f"""select * from {in_table_name}""")
    for i in cursor:
        a.append('.'.join(i))
    b = []
    for i in a:
        b.append("('"+''.join(i)+"')")
    b=str(b).replace('"','')
    b=b[1:-1]
    return b
    cursor.close()

def dob_stat(Today_name:str, Yesterday_name:str, connect):
    a = []
    cursor = connect.cursor()
    cursor.execute(f"""select NAME1 from (select concat (t.Schema_Name,'.', t.Table_name, '.',t.Col_name,'.',t.Type_name) as NAME1, '0' as VV from TestBD.Differ.Today_TestBD t join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name
union 
select concat (t.Schema_Name,'.', t.Table_name, '.',t.Col_name,'.',t.Type_name) , '1' from TestBD.Differ.Today_TestBD t left join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name where y.Col_name is NULL
union  
select concat (y.Schema_Name,'.', y.Table_name, '.',y.Col_name,'.',t.Type_name) , '-1' from TestBD.Differ.Today_TestBD t right join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name where t.Col_name is NULL 
)as b left join TestBD.Differ.fff on NAME=b.NAME1 where NAME is NULL""")
    for i in cursor:
        a.append(i)
    return a

def get_nazv (Today_name:str, Yesterday_name:str, connect):
    a = []

    cursor = connect.cursor()
    cursor.execute(f"""select NAME1, vv from (select concat (t.Schema_Name,'.', t.Table_name, '.',t.Col_name,'.',t.Type_name) as NAME1, '0' as VV from TestBD.Differ.Today_TestBD t join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name
union 
select concat (t.Schema_Name,'.', t.Table_name, '.',t.Col_name,'.',t.Type_name) , '1' from TestBD.Differ.Today_TestBD t left join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name where y.Col_name is NULL
union  
select concat (y.Schema_Name,'.', y.Table_name, '.',y.Col_name,'.',t.Type_name) , '-1' from TestBD.Differ.Today_TestBD t right join TestBD.Differ.Yesterday_TestBD y on t.Schema_Name= y.Schema_Name and t.Table_name= y.Table_name and t.Col_name= y.Col_name and t.type_name=y.type_name where t.Col_name is NULL 
)as b left join TestBD.Differ.fff on NAME=b.NAME1 """)
    for i in cursor:
        a.append(i)
    return a

def dob_nazv(in_table_name: str,col:str,data_raw, connect):
    cursor = connect.cursor()
    for i in data_raw:
        p="'"+i[0]+"'"
        cursor.execute(f'''INSERT INTO {in_table_name}({col}) values ({p})''')

    cursor.close()
    print(f'Done insert {in_table_name}->{data_raw}')
def tabl(schema:str, yesterday: str, today: str,data:str):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL TABL')
    except:
        print('No connection with MSSQL TABL')
    else:
        sozdanie_schem(schema,conn)
        sozdanie(yesterday, conn)
        sozdanie(today, conn)
        # sozdanie_date(data, conn)
        # sozdanie_coll(data, conn)

        conn.commit()

        # truncate(yesterday, conn)
        insert(yesterday, today, conn)
        # truncate(today, conn)
        # in_many(today, var, conn)
        # p=obedn(today, conn)
        # #print(p)
        # insert_one(data,p,conn)
        # insert_one(data)
        #
        # conn.commit()
        # print(get_nazv('dd', 'ddd', conn))
        # p= dob_stat('dd','ddd',conn)
        # for i in p:
        #     print(i[0].replace('/n',''))
        # print(dob_stat('dd','ddd',conn)[0][0])
        # dob_nazv(data,'NAME',dob_stat('dd','ddd',conn),conn)
        conn.commit()
def sql_differ(yesterday: str, today: str, doba: str, udal: str):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL SQL_DIFFER')
    except:
        print('No connection with MSSQL SQL_DIFFER')
    else:
        sozdanie(doba, conn)
        sozdanie(udal, conn)
        truncate(doba, conn)
        truncate(udal, conn)
        dobavlenie(today, yesterday, doba, conn)
        udalenie(today, yesterday, udal, conn)
        conn.commit()
def lis_differ(first: str, second: str):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL LIST_DIFFER')
    except:
        print('No connection with MSSQL LIST_DIFFER')
    else:
        sozdanie(first, conn)
        sozdanie(second, conn)
        truncate(first, conn)
        truncate(second, conn)
        in_many(first,list_table(f'TestBD.{schema_name}.Today_{DB}',f'TestBD.{schema_name}.Yesterday_{DB}',conn),conn)   #dobavl
        in_many(second,list_table(f'TestBD.{schema_name}.Yesterday_{DB}', f'TestBD.{schema_name}.Today_{DB}',conn),conn) #ubavl
        conn.commit()
def uni(first_table: str, second_table: str, all: str):
    try:
        conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
        print('Successful connection with MSSQL UNION')
    except:
        print('No connection with MSSQL UNION')
    else:
        sozdanie(all, conn)
        union(all, second_table, first_table, conn)
        conn.commit()


with open('DB_name.txt', 'r') as f:
    for line in f:
        schema_name='Differ'
        DB = line
        DB = DB.replace("\n", "")
        server = '"LEN2"'
        # vibor = f""""select AdventureWorks2019.sys.schemas.name as Schema_name, AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name from AdventureWorks2019.sys.tables Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id"""
        vibor = f""""select {DB}.sys.schemas.name as Schema_Name, {DB}.sys.tables.name as Table_Name , {DB}.sys.columns.name as Col_Name, {DB}.sys.types.name as Type_Name from {DB}.sys.tables Join {DB}.sys.columns on {DB}.sys.tables.object_id= {DB}.sys.columns.object_id join {DB}.sys.types on {DB}.sys.types.system_type_id= {DB}.sys.columns.system_type_id join {DB}.sys.schemas on {DB}.sys.tables.schema_id = {DB}.sys.schemas.schema_id"""""
        path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
        p = sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
        var = p.decode(encoding='ascii').split('\r')
        var.pop(1)
        var.pop(-1)
        Bame = tuple(var[0].split())
        var.pop(0)
        for i in range(len(var)):
            var[i] = f'{DB}' + var[i]
            var[i] = tuple(var[i].split())
        var = tuple(var)
        tabl(schema_name, f'TestBD.{schema_name}.Yesterday_{DB}', f'TestBD.{schema_name}.Today_{DB}', f'TestBD.{schema_name}.LOGG_{DB}')
        sql_differ(f'TestBD.{schema_name}.Yesterday_{DB}', f'TestBD.{schema_name}.Today_{DB}', f'TestBD.{schema_name}.DobavSQL_{DB}', f'TestBD.{schema_name}.UdalSQL_{DB}')
        lis_differ(f'TestBD.{schema_name}.DobavList_{DB}', f'TestBD.{schema_name}.UdalList_{DB}')
        uni(f'TestBD.{schema_name}.Today_{DB}',f'TestBD.{schema_name}.Yesterday_{DB}',f'TestBD.{schema_name}.All_{DB}')

