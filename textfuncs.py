

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:05:04 2021

@author: Mikko
"""

"Text functions for reading input"

import random

def readlines(filename,remove_indents=True):
    with open(filename) as f:
        lines = f.read().splitlines()
    if remove_indents:
        lines = [line.replace("\n","") for line in lines if line!="\n"]
    lines = [line.split(" ") for line in lines]
    return(lines)


def csum(vec):return [sum(vec[0:i]) for i in range(1,len(vec)+1)]

def clean(lines,drop=["\n"],lowcase=True):
    rlines = [] 
    
    remove = [":","/","!","?",";",'"',
            "I\x92m","\x92","\x91","\'",")","("]

    for i in lines:
        #print(i)
        if i in drop:
            continue
        line = []
        for word in i:
            w = word
            for sign in remove:
                w = w.replace(sign,"")
            if w != "I" and lowcase:    
                w = w.lower()    
            line.append(w)    
            
        rlines.append(line)        
    return rlines

def lsample(vec,drop=".",n=1):
    _vec = [word for word in vec] 
    l = len(_vec)
    if l in [0,1]:
        return _vec[0]
    rint = random.randint(0,l-1)
    return _vec[rint]
