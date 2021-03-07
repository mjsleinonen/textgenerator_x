# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:48:01 2021

@author: Mikko
"""

import os

from numpy import random
from textfunctions import *

class MarkovWords:
    
    #markov-chain-based text generator, .txt as input  
    def __init__(self):
        self.data = []
        self.words = {}
        self.joins = []
    
    def get_data(self,fname,drop=["\n"]):
        words = readlines(fname)
        
        for line in clean(words,drop):
            self.data.append(line)
        #self.data = cleantxt
        
    def get_data_set(self, path):
        pass
    
    def occurences(self,nlast=1):
        #goes trough data, creates connection as dictionaries
        for line in self.data:
            for word in line:    
                if not word in self.words:
                    self.words[word] = {}         
        list1 = []
        list2 = [] 
               
        for line in self.data:
            #print(line)
            index = 0
            for word in line[:-1]:
                one = word
                two = line[index+1]
                if not two in self.words[one]:
                    self.words[one][two] = 1
                else:
                    self.words[one][two] += 1    
                    
                index += 1
            
                
            #print(line)
                if word[-1]==".":
                    list1.append(word)
                    
            list2.append(line[0])
            
        
        self.lastones = []  
        self.firstones = [] 
           
        for i in list1:
            if not i in self.lastones:
                self.lastones.append(i)    
        for i in list2:
            if not i in self.firstones:         
                self.firstones.append(i)
                
        self.calculate_probabilities()

    def anyword(self):
        #pics a random word from the data
        rline = lsample(self.data)
        return(lsample(rline)) 

    def calculate_probabilities(self):
        self.probabilities = {}
        for key in self.words.keys():
            s = sum(self.words[key].values())
            c = csum(list(self.words[key].values()))
            
            self.probabilities[key] = [i/s for i in c] 
    
    def makeline(self,first,length,empiric=0.9,cutend=True):
        #creates a line based on connections, empiric is for how much weight the
        #number of occurences have
        rlist = []
        rlist.append(first.capitalize())
        word = first
        
        i = 1
        start = False
        while i < length:
            t = 1  
            while self.words[word] == {}:
                if cutend:
                    #rlist[-1]+="."
                    word = self.anyword()
                else:    
                    try:
                        if t > 10:
                            word = self.anyword()
                        k = rlist[-t-1]
                        word = lsample(self.words[k].keys())
                        t = t + 1
                    except:
                        word = self.anyword()

            probs = self.probabilities[word]
            
            odds1 = random.uniform(0,1) 
            if odds1 > (1.0-empiric):
                odds2 = random.uniform(0,1)
                ii = 0
                for nexti in self.words[word]: 
                    #print "x",word,odds2 
                    if float(probs[ii]) > odds2:
                        _nexti = nexti
                        if start:
                            _nexti = nexti.capitalize()
                            start = False
                        if nexti[-1]==".":
                            start = True
                        rlist.append(_nexti)
                        word = nexti
                        break
                    ii += 1         
            else:
                #print word,self.words[word]
                nexti = lsample(list(self.words[word].keys()))
                _nexti = nexti
                if start:
                    _nexti = nexti.capitalize()
                    start = False
                if nexti[-1]==".":
                    start = True
                word = nexti
                rlist.append(_nexti)
            i += 1 
        
        return rlist
        
    def stats(self):
        print("total number of words :",len(self.words.keys()))
        wsum = 0
        ii = 0
        de = 0
        for i in self.words.keys():
            if self.words[i] == {}:
                de += 1
            wsum += sum(self.words[i].values())
            ii += 1 
        print("average connections : %.2f"%(float(wsum)/ii))
        print("number of deadends :",de)
        
path = ""



























