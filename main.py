# -*- coding: cp866 -*-

import sys
import pymssql as pm
import subprocess as sp
import re
import os
import time

server = os.environ['Local_server']
database = 'TestBD'
base = 'Base.txt'
resu = 'Result.txt'


def open_file(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'wb') as Log:
        for line in f:
            coman = f'"select * from {line}"'
            path = '"C:\Program Files\DbVisualizer\dbviscmd.bat"'
            sp.Popen(f"{path} -connection {server} -sql {coman}", stdout=Log, stderr=sys.stdout, shell=True)
        f.close()
        Log.close()

        time.sleep(5)

        outputt = open(output_file, 'r+')
        lines = outputt.readlines()
        outputt.seek(0)
        for line in lines:
            pattern = re.compile(r'^\d\d:\d\d:\d\d').search(line)
            pattern2 = re.compile(r'^select').search(line)
            if (pattern or pattern2) is None:
                outputt.write(line)
            outputt.truncate()
        outputt.close()


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
    open_file(base, resu)
    differ(server, database)

