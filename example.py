
def example(filename,arg1,arg2,drop,first="I"):

    print("--"*10)
    mw = MarkovWords()
    mw.getdata(filename,drop)
    mw.occurences(nlast=3)
    mw.stats()
    print("--"*10)
    string = ""
    ii = 0  
    for i in mw.makeline(first,arg1,empiric=arg2,cutend=False):
        ii += 1
        string += " "+i 
        if ii > 10 or i == ".":
            string += "\n"
            ii = 0
    print(string) 
    
    
i = input("give filename from homedir.\n")
example(r1,100,10,drop) 
    
