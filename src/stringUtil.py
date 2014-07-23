'''
Created on 2014/7/23

@author: jason
'''
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