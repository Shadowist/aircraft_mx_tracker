""" Handles any application specific SQL calls. """

import sqlite3
from . import sql_utils
from pathlib import Path
import csv
import os
from datetime import datetime


def create_plane_database(tail_number: str, mx_csv: str = "", overwrite=False) -> None:
    """ Creates the database for the plane. """
    if overwrite:
        os.remove(f"databases/{tail_number}")

    conn: sqlite3.Connection = sql_utils.create_connection(f"databases/{tail_number}")

    _create_tables(conn)

    if mx_csv:
        _import_mx_from_csv(mx_csv, conn)


def _create_tables(conn: sqlite3.Connection) -> None:
    logbooks = ["Airframe", "Avionics", "Engine", "Propeller"]
    for logbook in logbooks:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {logbook} (
                "Tail Number"       TEXT,
                "Logbook"           TEXT,
                "Date of Service"   TEXT,
                "Work Description"  TEXT,
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


def _import_mx_from_csv(filename: str, conn: sqlite3.Connection):
    path = Path(filename)
    if not path.exists():
        raise Exception("Path does not exist!")

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            cur = conn.cursor()

            desc = row['Work Description'].replace('"', '\'')
            ttaf = -1
            tach = -1
            date = datetime.strptime(row['Date of Service'], '%b %d, %Y')

            try:
                ttaf = float(row['TTAF'])
            except ValueError:
                pass

            try:
                tach = float(row['TTAF'])
            except ValueError:
                pass

            cmd = f"""
INSERT INTO "{row['Logbook Type']}"
VALUES(
    "{row['Tail Number']}",
    "{row['Logbook Type']}",
    date("{date}"),
    "{desc}",
    {ttaf},
    {tach}
)
"""
            cur.execute(cmd)
    conn.commit()
