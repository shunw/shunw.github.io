import re

class transfer_2_hide(object):
    def __init__(self, fl_name, save_flname_same = False):
        self.fl_name = fl_name
        self.data_0 = open(self.fl_name, 'rt', encoding = 'utf-8')
        
        # to change the text in dict format {0:'dafda', 1:'dafaf', 2:'dafdaf', ...} & start the sentence count with 0
        self.data_0_dict = dict()
        self.sen_start_list = list()
        self.text_start_list = list()
        count = 0
        for line in self.data_0:
            # if line.strip().isdigit(): continue
            self.data_0_dict[count] = line.strip()
            if re.match('\d+[.]|\d+$|<hr>', line): self.sen_start_list.append(count)
            if re.match('^[c|j][0-9]', line): self.text_start_list.append(count)
            count += 1
        # print (self.sen_start_list)
        if not save_flname_same: 
            self.save_flname = 'test.md'
        else: 
            self.save_flname = fl_name
    
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
                    if self.data_0_dict[startnum].strip().isdigit(): 
                        del self.data_0_dict[startnum]                    
                        startnum += 1
                        nextnum += 1
                        

                    jp = self.data_0_dict[startnum]
                    
                    if re.match('\d+[.]', jp): 
                        jp = jp.split('.', 1)[-1]
                    
                    ch = self.data_0_dict[nextnum]
                    self.data_0_dict[startnum] = '- ' +  ch + '\n'
                    self.data_0_dict[nextnum] = '    - ' + jp + '\n'
                    
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
        ind_1 = 0
        
        while ind_1 < len(self.text_start_list) - 1:
            ind_2 = ind_1 + 1    
            
            text_ind_1 = self.text_start_list[ind_1]
            text_ind_2 = self.text_start_list[ind_2]

            if re.match('^c', self.data_0_dict[text_ind_1]): 
                c_ind = text_ind_1
                c_content = self.data_0_dict[c_ind]
                j_ind = text_ind_2
                j_content = self.data_0_dict[j_ind]

            elif re.match('^c', self.data_0_dict[text_ind_2]):
                c_ind = text_ind_2
                c_content = self.data_0_dict[c_ind]
                j_ind = text_ind_1
                j_content = self.data_0_dict[j_ind]

            else: 
                print ('something wrong')
            
            self.data_0_dict[text_ind_1] = '- ' + c_content.split(':', 1)[-1].strip() + '\n'
            self.data_0_dict[text_ind_2] = '    - ' + j_content.split(':', 1)[-1].strip()

            ind_1 = ind_1 + 2
            
            
    
    def final_run(self):
        self.transf_sen()

        self.transf_text()
        
        with open(self.save_flname, 'w+', encoding = 'utf-8') as f: 
            for k, v in self.data_0_dict.items():
                f.write(v + '\n')
        f.close()        

if __name__ == '__main__':
    fl_name = input('Input the file name to transfer: ')
    save_fl_same = input('Save it as the same name (True), or save it as test.md (False)? (True or False) ')
    a = transfer_2_hide(fl_name, save_flname_same = (save_fl_same).lower() == 'true')
    a.final_run()

    

    