# -*- coding: cp866 -*-

import sys
import pymssql as pm
import subprocess as sp
import re
import os
import time

server = 'HEIN_'
database = 'TestBD'
base = 'Base.txt'
resu = 'Result.txt'


def open_file(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'wb') as Log:
        for line in f:
            coman = f'"select * from {line}"'
            path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
            sp.Popen(f"{path} -connection {server} -sql {coman} -output result", stdout=Log, stderr=sys.stdout, shell=True)


def differ(server_name: str, database_name: str) -> None:
    try:
        conn = pm.connect(server=server_name, database=database_name)
        print('Successful connection')
    except:
        print('No connection')
    else:
        cursor = conn.cursor()
        cursor.execute(f"""
        IF OBJECT_ID('Differences', 'U') IS NOT NULL
        DROP TABLE Differences
        IF OBJECT_ID('Yesterday', 'U') IS NOT NULL
        DROP TABLE Yesterday
        IF OBJECT_ID('Today', 'U') IS NOT NULL
        SELECT * INTO Yesterday FROM Today
        DROP TABLE Today
        SELECT * INTO Today  FROM AdventureWorks2019.Person.BusinessEntity
        SELECT * into Differences from Today WhERE 1=1 AND ModifiedDate NOT IN (SELECT ModifiedDate from YESTERDAY)
        """)
        conn.commit()


if __name__ == "__main__":
    #open_file(base, resu)
    differ(server, database)


# DB='TestBD'
# server = '"Len2"'
# vibor = f""""select {DB}.sys.schemas.name as Schema_Name,  {DB}.sys.tables.name as Table_Name ,  {DB}.sys.columns.name as Col_Name,  {DB}.sys.types.name as Type_Name from  {DB}.sys.tables Join  {DB}.sys.columns on  {DB}.sys.tables.object_id=  {DB}.sys.columns.object_id join  {DB}.sys.types on  {DB}.sys.types.system_type_id=  {DB}.sys.columns.system_type_id join  {DB}.sys.schemas on  {DB}.sys.tables.schema_id =  {DB}.sys.schemas.schema_id"""""
# path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
# p = sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
# var = p.decode(encoding='ascii').split('\r')
# var.pop(1)
# var.pop(-1)
# Bame = tuple(var[0].split())
# var.pop(0)
# print(type(var))
# for i in range(len(var)):
#     var[i] = tuple(var[i].split())
# var = tuple(var)
# print(type(var))




# cursor = conn.cursor()
# cursor.execute(f"""
#     IF OBJECT_ID('TestBD.dbo.Testr', 'U') IS NOT NULL
#     truncate table TestBD.dbo.Testr """)
#
# sql="""INSERT TestBD.dbo.Testr VALUES (%s, %s, %s, %s)"""
# cursor.executemany(sql, var)
#
# conn.commit()



 # try:
    #     vivod1 = sp.check_output(f'''{path} -connection "HEIN-LENOVO7" -sql "IF OBJECT_ID (N'TestBD.dbo.Today', N'U') IS  NULL SELECT 0 AS res ELSE SELECT 1 AS res" -output result''')
    #     vivod2 = sp.check_output(f'''{path} -connection "HEIN-LENOVO7" -sql "IF OBJECT_ID (N'TestBD.dbo.Yesterday', N'U') IS  NULL SELECT 0 AS res ELSE SELECT 1 AS res" -output result''')
    #     vi1 = vivod1.decode(encoding='ascii').split('\r')
    #     vi2 = vivod2.decode(encoding='ascii').split('\r')
    #     a = []
    #     for po in range(len(Bame)):
    #         a.append(Bame[po] + ' NVARCHAR(50)')
    #     name_col = str(a)[1:-1].replace("'", '')
    #     if (vi1[2].split()[0]) == '0':
    #         try:
    #             conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
    #             print('Successful connection with MSSQL_TODAY')
    #         except:
    #             print('No connection with MSSQL_TODAY')
    #         else:
    #             print('Create table')
    #             cursor = conn.cursor()
    #             cursor.execute(f"""IF OBJECT_ID('TestBD.dbo.Today', 'U') IS NULL CREATE TABLE TestBD.dbo.Today({name_col});""")
    #             conn.commit()
    #             cursor.close()
    #             conn.close()
    #     if (vi2[2].split()[0]) == '0':
    #         try:
    #             conn = pm.connect(server="HEIN-LENOVO7", database="TestBD")
    #             print('Successful connection with MSSQL_YESTERDAY')
    #         except:
    #             print('No connection with MSSQL_YESTERDAY')
    #         else:
    #             print('Create table')
    #             cursor = conn.cursor()
    #             cursor.execute(f"""IF OBJECT_ID('TestBD.dbo.Yesterday', 'U') IS NULL CREATE TABLE TestBD.dbo.Yesterday({name_col});""")
    #             conn.commit()
    #             cursor.close()
    #             conn.close()
    #     else:
    #         print('Table exist')
    # except:
    #     print('Problem with DBVIS')
    # else:

# server = '"Len2"'
# #name_table=input()
# vibor = f""""select * from TestBD.dbo.Vigr"""""
# path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
# p=sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')
# var = p.decode(encoding='ascii').split('\r')
# var.pop(1)
# var.pop(-1)
# Bame = tuple(var[0].split())
# a=[]
#
# for i in range (len (Bame)):
#     a.append(Bame[i]+' NVARCHAR(20)')
# pp=str(a)
# pp=pp[1:-1]
# pp=pp.replace("'",'')
# print(pp)
# Bame=tuple(a)
# print(Bame)
# print(type(Bame))


# var.pop(0)
# for i in range(len(var)):
#     var[i] = tuple(var[i].split())
# var = tuple(var)
# o=str(var)
# o=o[1:-1]
# print(o)

# s='abcd'
# a=[]
# s=tuple(s)
# for i in range (len(s)):
#     a.append(s[i]+' NVCHARR,')
# a=tuple(a)
# print(a)
# print(type(a))
#
# print(s)
# print(type(s))