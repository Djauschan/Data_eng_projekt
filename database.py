import psycopg2
import pandas as pd

class Database:
    """
    Kapselt die Verbindung zur Postgres-Datenbank und stellt Funktionen zum Abrufen und Bearbeiten von Daten bereit.
    """

    def __init__(self, database, user, password, host, port):
        """
        Initialisiert die Datenbankverbindung.

        Args:
            database: Name der Datenbank
            user: Benutzername für die Datenbank
            password: Passwort für die Datenbank
            host: Hostname der Datenbank
            port: Port der Datenbank
        """
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """
        Stellt eine Verbindung zur Datenbank her.
        """
        self.connection = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def close(self):
        """
        Schließt die Verbindung zur Datenbank.
        """
        if self.connection:
            self.connection.close()

    def execute_and_fetchall(self, query):
        """
        Führt eine SQL-Abfrage aus und gibt alle Ergebnisse zurück.

        Args:
            query: Die SQL-Abfrage

        Returns:
            Eine Liste mit den Ergebnissen der Abfrage
        """
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        column_names = [column[0] for column in self.cursor.description]
        results = self.cursor.fetchall()
        df = pd.DataFrame(results, columns=column_names)
        return df
        