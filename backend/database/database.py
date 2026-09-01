import sqlite3
import os


DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "composite.db"
)


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            density REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS processes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM materials")

    if cursor.fetchone()[0] == 0:

        materials = [
            ("Carbon Fiber", 1600),
            ("Glass Fiber", 2500),
            ("Kevlar Fiber", 1440),
            ("Carbon Fiber/Epoxy", 1550)
        ]

        cursor.executemany(
            "INSERT INTO materials (name, density) VALUES (?, ?)",
            materials
        )

    cursor.execute("SELECT COUNT(*) FROM processes")

    if cursor.fetchone()[0] == 0:

        processes = [
            (
                "Hand Layup",
                "Manual placement of reinforcement and resin"
            ),
            (
                "Vacuum Infusion",
                "Resin is drawn into reinforcement using vacuum"
            ),
            (
                "Compression Molding",
                "Composite material is formed under pressure"
            ),
            (
                "Filament Winding",
                "Fibers are wound around a rotating mold"
            )
        ]

        cursor.executemany(
            "INSERT INTO processes (name, description) VALUES (?, ?)",
            processes
        )

    connection.commit()
    connection.close()