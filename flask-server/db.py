import psycopg2 
from psycopg2 import Error

class Database:
    def __init__(self, db, user, password, port, host):
        self.db = db
        self.user = user
        self.password = password
        self.port = port
        self.host = host
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(
                                            database=self.db,
                                            user=self.user,
                                            password=self.password,
                                            port=self.port,
                                            host=self.host
                                        )
        self.cursor = self.connection.cursor()
    
    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

try:
    db = Database(
                    db="jz",
                    user="jeffreyzhu",
                    password="myPassword",
                    host="127.0.0.1",
                    port="5432"
                )    
    db.connect()
    createLogTableQuery =   ''' 
                                CREATE TABLE IF NOT EXISTS logs(
                                    score INT DEFAULT 0,
                                    timestamp TIMESTAMP NOT NULL,
                                    log_id SERIAL PRIMARY KEY
                                    user_id INT REFERENCES users(uid)
                                )
                            '''                    
    db.execute_query(createLogTableQuery)
    print("Created table for Logs")
except(Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    if (db.connection):
        db.cursor.close()
        db.connection.close()
        print("PostgreSQL connection is closed")

