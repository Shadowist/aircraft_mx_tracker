""" Handles any application specific SQL calls. """

import sqlite3
from . import sql_utils


def create_plane_database(tail_number: str) -> None:
    """ Creates the database for the plane. """
    conn: sqlite3.Connection = sql_utils.create_connection(f"databases/{tail_number}")

    _create_tables(conn)


def _create_tables(conn: sqlite3.Connection) -> None:
    logbooks = ["Airframe", "Avionics", "Engine"]
    for logbook in logbooks:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {logbook} (
                "Logbook"           TEXT,
                "Date"              TEXT,
                "Work Description"	TEXT,
                "TTAF"              NUMERIC,
                "Tach"              NUMERIC
            );
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Squawks (
            "Date"          TEXT,
            "Title"         TEXT,
            "Description"   TEXT,
            "Priority"      INTEGER,
            "Status"        INTEGER
        );
    """)
