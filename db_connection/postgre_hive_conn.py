import getpass
import psycopg2 as ps
from sqlalchemy import create_engine
from pyhive import hive


class DB:
    def __init__(self, hostname='localhost', port=8888, 
                 db='geo', 
                 hive=False, dialect='postgresql',
                 username='imaksimov',  password='password'):
        self.username = username
        self.password = password
        if hive:
            self.engine = hive.Connection(host=host, port=10000, username=username)
        else:
            self.engine = create_engine('%s://%s:%s@%s:%s/%s' % (dialect, self.username,
                                                                 self.password, hostname, str(port), db))
            self.conn = ps.connect(host=hostname, database=db, user=self.username,
                                   password=self.password, port=port)
            self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()
