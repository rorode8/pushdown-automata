# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:51:19 2021

@author: rorod
"""
import re

text = '''
while (x < y) {

    while (4 == 2) {

        while (z > a) {

        }

    }

}
'''

text2 = '''
while (x < y) {

    

}
'''

text3 = '''
while (x < 10)

    while (4 = 2) {

        while (z > a)

            while (1 > 1) { }

}
'''

def isToken(token):
    if(token == None):
        return False
    
    if(len(token)==1 and token in 'qwertyuiopasdfghjklzxcvbnm0123456789<>{}()'):
        return True
    elif(token in ['while','==']):
        return True
    else:
        return False
        

pattern = re.compile(r'((while)\s*\((\w|\d)\s*(<|>|==)\s*(\w|\d)\)\s*\{\s*)+(}\s*)+')

tokenizer = re.compile(r'((while)\s*(\()(\w|\d)\s*(<|>|==)\s*(\w|\d)\s*(\))\s*(\{)|\})')

single_tokens = re.compile(r'(while|\(|\)|[a-z]|<|>|==|\d|\{|\})')

matches = single_tokens.finditer(text2)

tokens = []

for match in matches:
    #print(match.group(0))
    for g in match.groups():
        if(isToken(g)):
            print(g)
            tokens.append(g)
        
    
    #print(match.group(1))
print(tokens)