import json
import sqlite3

class sql2json(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.db = self.conn.cursor()
    
    def sql_time(self):
        ### get all the table name 
        # res = self.conn.execute("select name from sqlite_master where type = 'table'")

        ### get column name in the table
        # pragma table_info(category_lkup);

        self.rows = self.db.execute('''
            select item.title, m.start, m.end
            from main_time m, item_lkup item, category_lkup cat
            where item.item_id == m.item_id and item.category_id == cat.category_id
        ''').fetchall()
        
        self.conn.commit()
        self.conn.close()

        js_data = json.dumps( [dict(ix) for ix in self.rows] ) #CREATE JSON
        
        with open('time-data.json', 'w') as outfile:
            outfile.write(js_data)

        
    def final_run(self):
        
        self.sql_time()


if __name__ == '__main__':
    trans = sql2json('./time_data.db')
    trans.final_run()
