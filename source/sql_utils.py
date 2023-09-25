""" Main file that handles sql calls
"""
import sqlite3 as sql


def create_connection(db_file) -> sql.Connection:
    """ Creates a connection (initializes file if needed)"""
    conn = None
    try:
        conn = sql.connect(db_file)
        print(sql.version)
    except sql.Error as error:
        print(error)
    return conn
