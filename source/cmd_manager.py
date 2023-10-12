""" Contains all the sql scripts to be used """

from .sql_manager import sql_manager
from pathlib import Path
import csv
import os
from datetime import datetime


def create_plane_database(tail_number: str, mx_csv: str = "", overwrite=False) -> None:
    """ Creates the database for the plane. """
    if overwrite:
        try:
            os.remove(f"databases/{tail_number}")
        except OSError:
            pass

    sql: sql_manager = sql_manager.open_file(f"databases/{tail_number}")

    _create_tables(sql)

    if mx_csv:
        _import_mx_from_csv(mx_csv, sql)


def _create_tables(sql: sql_manager) -> None:
    logbooks = ["Airframe", "Avionics", "Engine", "Propeller"]
    for logbook in logbooks:
        sql.execute(f"""
            CREATE TABLE IF NOT EXISTS {logbook} (
                "Tail Number"       TEXT,
                "Logbook"           TEXT,
                "Date of Service"   TEXT,
                "Work Description"  TEXT,
                "TTAF"              NUMERIC,
                "Tach"              NUMERIC
            );
        """)

    sql.execute("""
        CREATE TABLE IF NOT EXISTS Squawks (
            "Date"          TEXT,
            "Title"         TEXT,
            "Description"   TEXT,
            "Priority"      INTEGER,
            "Status"        INTEGER
        );
    """)


def _import_mx_from_csv(filename: str, sql: sql_manager):
    path = Path(filename)
    if not path.exists():
        raise Exception("Path does not exist!")

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for index, row in enumerate(reader):
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
("Tail Number", "Logbook", "Date of Service", "Work Description", "TTAF", "Tach")
VALUES(
    "{row['Tail Number']}",
    "{row['Logbook Type']}",
    date("{date}"),
    "{desc}",
    {ttaf},
    {tach}
)
"""
            sql.execute(cmd)
    sql.commit()


def get_logs(sql: sql_manager, logbook: str):
    cmd = f'''
SELECT ROWID, "Date of Service", TTAF, Tach, "Work Description" FROM {logbook}
'''

    return sql.execute(cmd).fetchall()


def save_log(sql: sql_manager, logbook: str, id: int, values: tuple):
    cmd = f'''
UPDATE {logbook}
SET "Date of Service"="{values[0]}", TTAF={values[1]}, Tach={values[2]}, "Work Description"="{values[3]}"
WHERE ROWID={id};
'''

    sql.execute_commit(cmd)
