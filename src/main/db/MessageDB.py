import uuid


class MessageDB:
    menagerDB = None

    @classmethod
    def __init__(cls, menagerDB):
        cls.menagerDB = menagerDB

    def deleteTable(self, menagerDB):
        sql = "drop table message cascade"
        menagerDB.cursor.execute(sql)
        menagerDB.db.commit()
        return

    def createTable(self, menagerDB):
        bool_ = self.tableExists(self, menagerDB)
        if bool_:
            self.deleteTable(self, menagerDB)
            sql = '''
                    CREATE TABLE MESSAGE (
                        ID UUID PRIMARY KEY,
                        MESSAGE VARCHAR(1000) NOT NULL
                    )
                '''
            menagerDB.cursor.execute(sql)
            menagerDB.db.commit()
            return
        return
    
    def tableExists(self, menagerDB):
        sql = '''
            select * from information_schema.tables where table_name='{}'"
        '''
        menagerDB.cursor.execute(sql.format('MESSAGE'))
        return bool(menagerDB.cursor.rowcount)

    @classmethod
    def saveMessage(cls, message):
        message = str(message).replace("'", '"')
        sql = '''
                INSERT INTO MESSAGE(ID, MESSAGE)
                VALUES('{}', '{}');
            '''
        cls.menagerDB.cursor.execute(sql.format(uuid.uuid1(), str(message)))
        cls.menagerDB.db.commit()