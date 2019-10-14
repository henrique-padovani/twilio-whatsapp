import psycopg2


class MenagerDB:
    db = None
    cursor = None

    def __init__(self, dataBaseName):
        self.db = psycopg2.connect("dbname=" + str(dataBaseName) + " user=postgres password=henrique901")
        self.cursor = self.db.cursor()
        return
