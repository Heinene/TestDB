# -*- coding: cp866 -*-

import sys
import pymssql as pm
import subprocess as sp
import re
import os
import time

server = 'HEIN-LENOVO7'
database = 'TestBD'
base = 'Base.txt'
resu = 'Result.txt'

# запрос из дбвис скл таблицы с джойнами
def open_file(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'wb') as Log:
        for line in f:
            vibor = """"select AdventureWorks2019.sys.tables.name as DB_Name , AdventureWorks2019.sys.columns.name as Col_Name, AdventureWorks2019.sys.types.name as Type_Name , AdventureWorks2019.sys.schemas.name as Schema_name , AdventureWorks2019.sys.columns.object_id from AdventureWorks2019.sys.tables  Join AdventureWorks2019.sys.columns on AdventureWorks2019.sys.tables.object_id= AdventureWorks2019.sys.columns.object_id join AdventureWorks2019.sys.types on  AdventureWorks2019.sys.types.system_type_id= AdventureWorks2019.sys.columns.system_type_id join AdventureWorks2019.sys.schemas on AdventureWorks2019.sys.tables.schema_id = AdventureWorks2019.sys.schemas.schema_id where AdventureWorks2019.sys.tables.name= 'BusinessEntity'"""""
            coman = f'"select * from {line}"'
            path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
            p = sp.check_output(f'{path} -connection {server} -sql {vibor}" -output result')



    # outputt = open(output_file, 'r+')
    # lines = outputt.readlines()
    # outputt.seek(0)
    # for line in lines:
    #     pattern = re.compile(r'^\d\d:\d\d:\d\d').search(line)
    #     pattern2 = re.compile(r'^select').search(line)
    #     if (pattern or pattern2) is None:

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
        TRUNCATE TABLE Differences
        IF OBJECT_ID('Yesterday', 'U') IS NOT NULL
        TRUNCATE TABLE Yesterday
        IF OBJECT_ID('Today', 'U') IS NOT NULL
        
        TRUNCATE TABLE Today
        
        """)
        conn.commit()

def test (server_name: str, database_name: str) -> None:
    try:
        conn = pm.connect(server=server_name, database=database_name)
        print('Successful connection')
    except:
        print('No connection')
    else:
        cursor = conn.cursor()
        cursor.execute(f"""
            SET IDENTITY_INSERT Today ON
            INSERT INTO Today (BusinessEntityID, rowguid, ModifiedDate) SELECT * FROM AdventureWorks2019.Person.BusinessEntity
            SET IDENTITY_INSERT Today OFF 
               """)
        conn.commit()


if __name__ == "__main__":
    differ(server, database)
    #test(server, database)
    #open_file(base, resu)

