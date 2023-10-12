""" Main file that handles sql calls
"""
import sqlite3
from typing import TypeVar, Type

T = TypeVar('T', bound='sql_manager')


class sql_manager():
    _conn: sqlite3.Connection

    def __init__(self):
        pass

    @classmethod
    def open_file(cls: Type[T], db_file: str) -> T:
        new_obj = cls()
        new_obj.create_connection(db_file)
        return new_obj

    def create_connection(self, db_file: str) -> None:
        try:
            self._conn = sqlite3.connect(db_file)
        except sqlite3.Error as error:
            print(error)

    def execute(self, cmd: str) -> sqlite3.Cursor:
        cur = self._conn.cursor()
        res = cur.execute(cmd)

        return res

    def execute_commit(self, cmd: str) -> sqlite3.Cursor:
        res = self.execute(cmd)
        self._conn.commit()

        return res

    def commit(self):
        self._conn.commit()
