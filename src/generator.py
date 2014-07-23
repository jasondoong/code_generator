'''
Created on Jul 22, 2014

@author: jason
'''


from data import *
from fileUtil import *
from stringUtil import *
from config import *

class Generator:

    def __init__(self):
        self.before_code_string = ''
        self.after_code_string = ''
        self.code = ''
        self.line_it = None

    def execute(self):
        self.template = readfile('./template.txt')
        self.process_each_line()
    
    def process_each_line(self):
        self.line_it = iter(self.template)
        while True:
            try:
                line = self.line_it.next()
                self.process_line(line)
            except StopIteration:
                break
    
    def process_line(self, line):
        if self.is_contains_code(line):
            self.code_mode_process(line)
        else:
            print line,
    
    def is_contains_code(self, line):
        return SYMBOL_BEGIN in line
    
    def code_mode_process(self,line):
        self.extract_code(line)
        self.process_string_before_code()
        self.process_code()    
        self.process_after_code_string()
    
    
    def extract_code(self, line):
        if SYMBOL_END in line :
            self.extract_one_line_code(line)
        else:
            self.extract_multi_line_code(line)
    
    def process_string_before_code(self):
        if self.before_code_string != '':
            print self.before_code_string,
    
    def process_code(self):
        exec self.code
    
    def process_after_code_string(self):
        if self.is_string_null(self.after_code_string):
            return
        '''
          Notice: String after code may contains another code
                      ex: <py> print 'public'</py> static <py> print func_name</py> {
        '''
        self.process_line(self.after_code_string)
    
    def extract_one_line_code(self, line):
        self.before_code_string = line.split(SYMBOL_BEGIN)[0]
        self.code = find_between(line, SYMBOL_BEGIN, SYMBOL_END)
        self.after_code_string = get_substring_after(line, SYMBOL_END)
        
    def extract_multi_line_code(self, line):
        self.before_code_string = line.split(SYMBOL_BEGIN)[0]
        self.code = get_substring_after(line,SYMBOL_BEGIN) + '\r\n'
        while True:
            line = self.line_it.next()
            if SYMBOL_END not in line :
                self.code = self.code + line + '\r\n'
            else:
                self.code = self.code + get_substring_before(line, SYMBOL_END) +'\r\n'
                self.after_code_string = get_substring_after(line, SYMBOL_END)
                break

    def is_string_null(self, input_string):
        if input_string == '':
            return True
        if len(input_string)==1:
            if ord(input_string)==10:
                return True
        return False

if __name__ == '__main__':
    Generator().execute()
