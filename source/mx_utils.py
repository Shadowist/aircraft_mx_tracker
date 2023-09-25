""" Handles any application specific SQL calls. """

import sqlite3
from . import sql_utils


def create_plane_database(tail_number: str):
    """ Creates the database for the plane. """
    conn: sqlite3.Connection = sql_utils.create_connection(f"databases/{tail_number}")

    _create_engine_log_table(conn, tail_number)
    _create_avionics_log_table(conn, tail_number)
    _create_airframe_log_table(conn, tail_number)


def _create_engine_log_table(conn: sqlite3.Connection, tail_number: str):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS "Engine" (
            "Date"	TEXT,
            "Work Description"	TEXT,
            "TTAF"	NUMERIC,
            "Tach"	NUMERIC
        );
    """)


def _create_avionics_log_table(conn: sqlite3.Connection, tail_number: str):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS "Avionics" (
            "Date"	TEXT,
            "Work Description"	TEXT,
            "TTAF"	NUMERIC,
            "Tach"	NUMERIC
        );
    """)


def _create_airframe_log_table(conn: sqlite3.Connection, tail_number: str):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS "Airframe" (
            "Date"	TEXT,
            "Work Description"	TEXT,
            "TTAF"	NUMERIC,
            "Tach"	NUMERIC
        );
    """)
