import random

class MarkovWords:
    
    #markov-chain-based text generator, .txt as input  
    def __init__(self):
        self.data = []
        self.words = {}
        self.joins = []
    
    def getdata(self,fname,drop):
        words = readlines(fname)
        cleantxt =  clean(words,drop)
        for i in cleantxt:
            self.data.append(i)
        #self.data = cleantxt
    
    def occurences(self,nlast=1):
        #goes trough data, creates connection as dictionaries
        for line in self.data:
            for word in line:    
                if not word in self.words:
                    self.words[word] = {}         
        list1 = []
        list2 = [] 
               
        for line in self.data:
            index = 0
            for word in line[0:-1]:
                one = word
                two = line[index+1]
                if not two in self.words[one]:
                    self.words[one][two] = 1
                else:
                    self.words[one][two] += 1    
                    
                index += 1
            for i in line[-nlast:-1]:
                list1.append(i)
            #print(line)
            list2.append(line[0])  
        
        self.lastones = []  
        self.firstones = [] 
           
        for i in list1:
            if not i in self.lastones:
                self.lastones.append(i)    
        for ii in list2:
            if not ii in self.firstones:         
                self.firstones.append(ii)

    def anyword(self):
        #pics a random word from the data
        rline = lsample(self.data)
        return lsample(rline)        
    
    def makeline(self,first,length,empiric=0.7,cutend=False):
        #creates a line based on connections, empiric is for how much weight the
        #number of occurences have
        rlist = []
        rlist.append(first)
        word = first
        
        i = 1
        while i < length:
            
            t = 1  
            while self.words[word] == {}:
                if cutend:
                    rlist.append(".")
                    word = self.anyword()
                    continue
                else:    
                    try:
                        if t > 10:
                            word = self.anyword()
                        k = rlist[-t-1]
                        word = lsample(self.words[k].keys())
                        t = t + 1
                    except:
                        word = self.anyword()    
                
            s = sum(self.words[word].values())
            c = csum(list(self.words[word].values()))
            odds1 = random.uniform(0,1) 
            if odds1 > empiric:
                odds2 = random.uniform(0,1)
                ii = 0
                for nexti in self.words[word]: 
                    #print "x",word,odds2 
                    if float(c[ii])/s > odds2:
                        rlist.append(nexti)
                        word = nexti
                        break
                    ii += 1         
            else:
                #print word,self.words[word]
                nexti = lsample(list(self.words[word].keys()))
                word = nexti
                rlist.append(nexti)
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
        print("number of dead-ends :",de)
