import pymysql

class Ranking:
    def __init__(self,player_name,category,clear_time,updated=None,id=None):
        self.player_name=player_name
        self.category=category
        self.clear_time=clear_time
        self.updated=updated
        self.id=id

def connect():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        database='wikiquiz',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def find_all():
    player_ranking=[]
    with connect() as con:
        with con.cursor() as cursor:
            sql = 'SELECT * FROM ranking ORDER BY clear_time ASC,updated DESC'
            cursor.execute(sql)
            rs = cursor.fetchall()

            for r in rs:
                player_ranking.append(Ranking(r['player_name'],r['category'],r['clear_time'],r['updated'],r['id']))

    return player_ranking

def insert_one(Ranking):
    with connect() as con:
        with con.cursor() as cursor:
            sql='INSERT INTO ranking(player_name,category,clear_time,updated) VALUES(%s,%s,%s,now())'
            cursor.execute(sql,(Ranking.player_name,Ranking.category,Ranking.clear_time))
        con.commit()