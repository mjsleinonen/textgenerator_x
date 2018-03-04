"Text functions for reading input"

def readlines(filename):
    f = open(filename)
    lines = []
    strikes = 0
    while True:
        rline = f.readline()
        if rline == "":
            strikes += 1
        if strikes > 10:
            break    
        lines.append(rline.split())
    return lines

def csum(vec):return [sum(vec[0:i]) for i in range(1,len(vec)+1)]

def clean(lines,drop=[],lowcase=True):
    rlines = [] 
    
    hots = [".",",",":","/","!","?",";",'"',
            "I\x92m","\x92","\x91","\'",")","("]

    for i in lines:
        if i in drop:
            continue
        line = []
        for word in i:
            w = word
            for sign in hots:
                w = w.replace(sign,"")
            if w != "I" and lowcase:    
                w = w.lower()    
            line.append(w)    
            
        rlines.append(line)        
    return rlines

def lsample(vec,n=1):
    l = len(vec)
    if l in [0,1]:
        return vec[0]
    rint = random.randint(0,l-1)
    return vec[rint]
