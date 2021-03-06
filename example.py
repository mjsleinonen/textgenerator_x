
def example(filename,arg1,arg2,drop,first="I"):

    print("--"*10)
    mw = MarkovWords()
    mw.getdata(filename,drop)
    mw.occurences(nlast=3)
    mw.stats()
    print("--"*10)
    string = " ".join(mw.makeline(first,arg1,empiric=arg2,cutend=False)))
    print(string) 
    
    
i = input("give filename from homedir.\n")
example(r1,100,10,drop) 
    
