import uuid


class MessageDB:
    menagerDB = None

    @classmethod
    def __init__(cls, menagerDB):
        cls.menagerDB = menagerDB

    def createTable(self, menagerDB):
        sql = '''
                CREATE TABLE MESSAGE (
                    ID UUID PRIMARY KEY,
                    MESSAGE VARCHAR(1000) NOT NULL
                )
            '''
        menagerDB.cursor.execute(sql)
        menagerDB.db.commit()
        return

    @classmethod
    def saveMessage(cls, message):
        message = str(message).replace("'", '"')
        sql = '''
                INSERT INTO MESSAGE(ID, MESSAGE)
                VALUES('{}', '{}');
            '''
        cls.menagerDB.cursor.execute(sql.format(uuid.uuid1(), str(message)))
        cls.menagerDB.db.commit()