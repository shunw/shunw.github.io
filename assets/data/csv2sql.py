import csv, sqlite3, re

class csv2sqlite(object):
    def __init__(self, fl_name): 
        handle = open(fl_name)
        self.raw_data = csv.reader(handle, delimiter = ',')
        self.con = sqlite3.connect('time_data.db')
        self.cur = self.con.cursor()

    def item_info(self): 
        # to get the item id for the mai_time table
        item_data = self.cur.execute('''
        select * from item_lkup
        ''')

        self.item_map = dict()

        for i in item_data:
            self.item_map[i[1]] = i[0]
            # {item_id: level}

    def time_deal(self, time_data):
        # input 2018-07-26 15:00:50 
        # output 2018-07-26T15:00:50+08:00
        time_list = time_data.split(' ')
        return time_list[0] + 'T' + time_list[1] + '+08:00'


    def csv_info(self):
        row_ind = 0
        
        self.data = list()
        
        # to delete some useless information
        for line in self.raw_data:
            if 'Started' not in line and (row_ind == 0): continue
            if (not line) and row_ind != 0: break
            self.data.append(line)
            row_ind += 1

        # to make dict 
        c = 0
        self.to_db = list()
        for item in self.data:
            if c == 0: 
                s_ind = item.index('Started')
                f_ind = item.index('Finished')
                c_ind = item.index('Category')
                cmt_ind = item.index('Comments')
                
                c += 1
            else: 
                # (item_id, start, end, comment)
                s_time = self.time_deal(item[s_ind])
                f_time = self.time_deal(item[f_ind])
                temp = (self.item_map[item[c_ind]], s_time, f_time, item[cmt_ind])
                self.to_db.append(temp)

        self.cur.executemany('''
        insert into main_time (item_id, start, end, comment) values (?, ?, ?, ?);
        ''', self.to_db)


        
        
        
    def final_run(self):
        
        self.item_info()
        
        self.csv_info()

        self.con.commit()
        self.con.close()
    
    

if __name__ == '__main__':
    test = csv2sqlite('raw_data.csv')
    test.final_run()

