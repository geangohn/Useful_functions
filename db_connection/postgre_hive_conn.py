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
        
    def copy(self, df, table, schema='public', if_exists='fail'):
        """Запись в базу в ~100 раз быстрее, чем .to_sql
        Построчно записывает датафрейм в базу
        """
        output = 'temp_copy_upload.csv'
        copy_sql = """COPY \"%s\".\"%s\" ("%s") FROM stdin WITH CSV HEADER DELIMITER as '\t' QUOTE '"' """ % \
                   (schema, table, '","'.join(df.columns))
        df.head(0).to_sql(table, self.engine, schema=schema, index=False, if_exists=if_exists)
        df.to_csv(output, sep='\t', index=False, escapechar='"')
        with open(output, 'r') as f:
            self.cur.copy_expert(sql=copy_sql, file=f)
        os.remove(output)
        self.commit()
        
        
# example
from Useful_functions import DB
db = DB(db='database')
# df = ...
db.copy(df, table='table_name', schema='schema_name', if_exists='replace')
