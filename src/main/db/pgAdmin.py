import psycopg2


class MenagerDB:
    db = None
    cursor = None

    def __init__(self, dataBaseName):
        # self.db = psycopg2.connect("dbname=" + str(dataBaseName) + " user=postgres password=henrique901")
        host = 'ec2-54-83-55-125.compute-1.amazonaws.com'
        db = 'd7g9aq8m04v1dl'
        user = 'jumuxuqmyofhdw'
        port = '5432'
        pw = '77daa1d66905f7d02832b39dfb4bc9896e4fb9cd26bf314bcb4d869b91f78101'
        self.db = psycopg2.connect(dbName = db, user=user, password=pw, host=host, port=port)
        self.cursor = self.db.cursor()
        return
