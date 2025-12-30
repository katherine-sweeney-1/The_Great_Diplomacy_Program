#from MySQLdb import _mysql
#import mysql.connector

import pymysql
class Table ():

    def __init__ (self):
        #self.db = _mysql.connect(
        self.db = pymysql.connect(
        #self.db = mysql.connector.connect(
        user = "diplomacy",
        passwd = "password",
        host = 'localhost',
        db = 'tgdp_testing_1'
    )

    def create_table(self, game_and_turn):
            self.db.query("""USE tgdp_testing_1;""")
            #self.db.store_result()
            self.db.query("""
                CREATE TABLE IF NOT EXISTS {} (
                UNIT_ID TEXT,
                Commander TEXT,
                Location TEXT,
                Origin TEXT,
                Destination TEXT,
                Outcome TEXT
                )
                """.format(game_and_turn)
            )
            #self.db.store_result()
            return self.db

    def delete_previous_data(self, game_and_turn):
        self.db.query("""USE tgdp_testing_1;""")
        self.db.query("""
                DELETE from {};
            """.format(game_and_turn)
        )
        #self.db.commit()
        return self.db

    def drop_old_tables(self):
        sql = """USE tgdp_testing_1;"""
        self.db.query(sql)
        sql = """
            DROP TABLE game2_1903_fall;
            """
        self.db.query(sql)
        sql = """
            DROP TABLE game1_1901_fall;
            """
        self.db.query(sql) 
        return self.db 
     
    def save(self, cmds, game_and_turn):
        sql = """USE tgdp_testing_1;"""
        self.db.query(sql)
        for cmd_string in cmds:
            cmd = cmds[cmd_string]
            sql = """
                INSERT INTO {} (UNIT_ID, Commander, Location, Origin, Destination, Outcome) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
                ON DUPLICATE KEY UPDATE UNIT_ID = UNIT_ID;
                """.format(game_and_turn, cmd.unit.id, cmd.human.human, cmd.location.name, cmd.origin.name, cmd.destination.name, cmd.outcome_loc.name)
            self.db.query(sql)
        self.db.commit()
        self.db.close()
        #self.db.store_result()