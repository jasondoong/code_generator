'''
Created on Jul 22, 2014

@author: jason
'''


from data import *

syntax_begin = '<py>'
syntax_end = '</py>'

before_code_string = ''
after_code_string = ''
code = ''

line_it = None

def execute():
    template = readfile('./template.txt')
    process_each_line(template)

def process_each_line(template):
    global line_it
    line_it = iter(template)
    while True:
        try:
            line = line_it.next()
            process_line(line)
        except StopIteration:
            break

def process_line(line):
    if is_contains_code(line):
        code_mode_process(line)
    else:
        print line,

def is_contains_code(line):
    global syntax_begin
    return syntax_begin in line

def code_mode_process(line):
    extract_code(line)
    process_string_before_code()
    process_code()    
    process_after_code_string()


def extract_code(line):
    global syntax_begin
    global syntax_end
    
    if syntax_end in line :
        extract_one_line_code(line)
    else:
        extract_multi_line_code(line)

def process_string_before_code():
    global before_code_string
    if before_code_string != '':
        print before_code_string,

def process_code():
    global code
    exec code

def process_after_code_string():
    global after_code_string
    if is_string_null(after_code_string):
        return
    '''
      String after code may contains another code
      ex: <py> print 'public'</py> static <py> print func_name</py> {
    '''
    process_line(after_code_string)

def extract_one_line_code(line):
    global syntax_begin
    global syntax_end
    global before_code_string
    global code
    global after_code_string
    
    before_code_string = line.split(syntax_begin)[0]
    code = find_between(line, syntax_begin, syntax_end)
    after_code_string = get_substring_after(line, syntax_end)
    
def extract_multi_line_code(line):
    global syntax_begin
    global syntax_end
    global before_code_string
    global code
    global after_code_string
    
    before_code_string = line.split(syntax_begin)[0]
    code = get_substring_after(line,syntax_begin) + '\r\n'
    while True:
        line = line_it.next()
        if syntax_end not in line :
            code = code + line + '\r\n'
        else:
            code = code + get_substring_before(line, syntax_end) +'\r\n'
            after_code_string = get_substring_after(line, syntax_end)
            break

def is_string_null(input_string):
    if input_string == '':
        return True
    if len(input_string)==1:
        if ord(input_string)==10:
            return True
    return False

def get_substring_before(whole_string, keyword):
    return whole_string.split(keyword)[0]

def get_substring_after(whole_string, keyword):
    try:
        start = whole_string.index( keyword ) + len( keyword )
        end = len(whole_string)
        return whole_string[start:end]
    except ValueError:
        return ""

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def readfile(path):
    out = []
    f = open(path, 'r')
    for line in f:
        out.append(line)
    return out

if __name__ == '__main__':
    execute()