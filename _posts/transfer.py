import re

class transfer_2_hide(object):
    def __init__(self, fl_name):
        self.fl_name = fl_name
        self.data_0 = open(self.fl_name, 'rt', encoding = 'utf-8')
        
        # to change the text in dict format {0:'dafda', 1:'dafaf', 2:'dafdaf', ...} & start the sentence count with 0
        self.data_0_dict = dict()
        self.sen_start_list = list()
        self.text_start_list = list()
        count = 0
        for line in self.data_0:
            self.data_0_dict[count] = line.strip()
            if re.match('^[0-9+]|<hr>', line): self.sen_start_list.append(count)
            if re.match('^[c|j][0-9]', line): self.text_start_list.append(count)
            count += 1

    
    def transf_sen(self):
        # to change the one by one
        for ind, num in enumerate(self.sen_start_list[:-2]):
            valid_ind_temp = list()
            valid_ind_temp.append(ind)
            startnum = num
            nextnum = num + 1
            next_point = self.sen_start_list[ind + 1]

            while nextnum < next_point:
                if self.data_0_dict[nextnum]: 
                    jp = self.data_0_dict[startnum]
                    if re.match('^[0-9+]', jp): 
                        jp = jp.split('.', 1)[-1]
                    ch = self.data_0_dict[nextnum]
                    self.data_0_dict[startnum] = '- ' +  ch
                    self.data_0_dict[nextnum] = '    - ' + jp
                    
                    startnum = nextnum + 1
                    
                    while startnum < next_point: 
                        if self.data_0_dict[startnum]: 
                            break
                        else: 
                            startnum += 1
                    
                    nextnum = startnum + 1
                else: 
                    nextnum += 1
        
    
    def transf_text(self):
        pass
    
    def final_run(self):
        self.transf_sen()
        # f = open('test.md', 'wb', encoding = 'utf-8')
        # for k, v in self.data_0_dict.items():
        #     print (v)
        #     f.write(v)

        with open('test.md', 'w+', encoding = 'utf-8') as f: 
            for k, v in self.data_0_dict.items():
                f.write(v + '\n')
        f.close()        

if __name__ == '__main__':
    a = transfer_2_hide('2019-01-29-jp31.md')
    a.final_run()
    