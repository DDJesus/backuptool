import sys
import pyodbc
import os
import glob

import config
from os.path import join
import win32com.shell.shell as shell


def make_backup(filename):
    filepath = (os.getcwd() + "\\" + filename)
    conn_info = "DRIVER={SQL Server};SERVER=%s;DATABASE=master;UID=%s;PWD=%s" % (config.login["SERVER"],
                                                                                 config.login["USER"],
                                                                                 config.login["PASS"])
    cnct_str = pyodbc.connect(conn_info, autocommit=True)
    cur = cnct_str.cursor()
    cur.execute(
        """BACKUP DATABASE [%s] TO  DISK = N'%s' WITH NOFORMAT, NOINIT,  
        NAME = N'%s-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10""" % (config.login["DATABASE"],
                                                                                       filepath,
                                                                                       config.login["DATABASE"]))
    while cur.nextset():
        pass
    print("make_backup completed successfully")


def restore_backup(filename, db_name):
    filepath = (os.getcwd() + "\\" + filename)
    print(filepath)
    conn_info = "DRIVER={SQL Server};SERVER=%s;DATABASE=master;UID=%s;PWD=%s" % (config.login["SERVER"],
                                                                                 config.login["USER"],
                                                                                 config.login["PASS"])
    cnct_str = pyodbc.connect(conn_info, autocommit=True)
    cur = cnct_str.cursor()
    cur.execute(
        """RESTORE DATABASE [%s] FROM  DISK = N'%s' WITH  FILE = 1, NOUNLOAD, REPLACE, STATS = 5""" % (db_name, filepath))
    while cur.nextset():
        pass
    print("restore_backup completed successfully")

if "-h" in sys.argv:
    with open("help.txt", "r") as help:
        for line in help:
            print(line)
elif len(sys.argv) > 1:
    for cmdarg in sys.argv[1:]:
        if cmdarg == "-b":
            filename = input("Name of file: ")
            make_backup(filename)
            print("Backup successful. Exiting...\n\n")
        elif cmdarg == "-r":
            filename = input("Name of file: ")
            db_name = input("Name of Restored Database: ")
            restore_backup(filename, db_name)
            print("Restore backup successful. Exiting...")
        else:
            print("Invalid arguments. Please use 'python backupfile.py -h' for help.\n")
else:
    print("Not enough arguments. Please use 'python backupfile.py -h' for help.\n")
