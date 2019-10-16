import psycopg2
import os

class MenagerDB:
    db = None
    cursor = None

    def __init__(self, dataBaseName):
        host = 'ec2-54-83-55-125.compute-1.amazonaws.com'
        db = 'd7g9aq8m04v1dl'
        user = 'jumuxuqmyofhdw'
        port = '5432'
        pw = '77daa1d66905f7d02832b39dfb4bc9896e4fb9cd26bf314bcb4d869b91f78101'
        DATABASE_URL = os.environ['DATABASE_URL']
        self.db = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cursor = self.db.cursor()
        return
