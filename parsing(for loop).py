import re
# single lower alphabet  =  int
# number  = 

with open('e3-example.txt') as t:
    string = t.read()
    print(string)

numbers = re.findall(r'[0-9]+', string)
alpha = re.findall(r'[a-z]+',string)
operators = ["<<","<",">","=","<=",">=","==","!=","%"]
loopCond = ["<<", "i++", ]
datatype = ['int','float','char','bool','double','string']

def parseTree(value):
    if(value in datatype):
        return "DT"
    if(value == "="):
        return "Asop"
    if(value == "cout"):
        return "out"
    if(value in operators):
        return "Op"
    if(value == ","):
        return ","
    if(value in numbers):
        return "num"
    if(value==";"):
        return ";"
    if(value=="<<"):
        return "loop"
    if(value=="i++"):
        return "loop"
    if(value == ")"):
        return ")"
    if(value == "("):
        return "("
    if(value == "}"):
        return "}"
    if(value == "{"):
        return "{"
    if(value == "else"):
        return "else"
    if(value == "for"):
        return "for"
    if(value == '"'):
        return "StrOpen"
    if(value in alpha):          # if(value == alpha):   #right one
        return "ID"
    else:
        return "Error"
    
stri = string.split();
print(stri)

cfg = []

for char in stri:
    cfg.append(parseTree(char))
print(cfg)
check =[]
check.insert(0,False)

def Decl(cfg,i):
    if(cfg[i]=="DT"):
        i=i+1
        if(cfg[i]=="ID"):
            i=i+1
            check.insert(0,True)
            check.insert(1,i)
            return check

def cond(cfg,post):                      # if ( Condition )
    if(cfg[post] == "DT"):      ## can be Data type or identifier or If else condition or comment 
        post=post +1            ## and each one will follow there on set ofconditions
        if(cfg[post] == "ID"):      ## can be Data type or identifier or If else condition or comment 
            post=post +1 
            if(cfg[post]=="Op" or "Asop"):
                post=post+1;
                if(cfg[post]=="num"):
                    check.insert(0,True)
                    check.insert(1,post)
                else: 
                    check.insert(0,False)   
    return check

def sst(cfg,post):
    if(cfg[post]=="DT"):
        Decl(cfg,post)
        if(Decl(cfg,post)[0]==True):
            return check

def else_s(cfg,post):
    if(cfg[post]=="else"):
        post=post+1
        if(body(cfg,post)[0]==True):
            return check;
    
def body(cfg , post):
    if(cfg[post]=="DT"):
         sst(cfg,post)
         if( sst(cfg,post)[0]==True):
            return check
    elif(cfg[post]==";"):
        check.insert(0,True)
        check.insert(1,post)
        return check

def err( *code ):
    print("error code: ", code)

def ifelses():
    i=0
    if(cfg[i]=="for"): # IF Check
        i=i+1
        if(cfg[i]=="("): # ( Check
            i=i+1
            if(cond(cfg,i)[0]==True): # a>b Check
                i=check[1]
                i=i+1
                if(cfg[i]==")"): # ) Check
                    i=i+1

                    if(cfg[i]=="{"): # IF Check
                        i=i+1
                        BracFlag = True
                        
                        body(cfg,i)
                       
                        if(cfg[i]=="}" and BracFlag == True): # IF Check
                            i=i+1
                        else:
                            err("10 - expected } ")
                    else:
                        err("10 - expected { ")
            else:
                err( "20 - condional error")
        else:
                err("10 - expected ( ")
    else:
                err("5 - missing keyword 'for'")

'''   
                    if(cfg[i]=="DT"): #  {} Check
                       # 
                        if(body(cfg,i)[0]==True):# a Check
                            i=check[1]
                            if(body(cfg,i)[0]==True): # ; Check
                                i=check[1]
                                i=i+1
                                }
                    '''
                        
######################## delete Else if
'''
                                if(cfg[i] !="else"): # else Check
                                    print("Accepted")
                                if(cfg[i]=="else"): # else Check
                                    else_s(cfg,i)
                                    if(else_s(cfg,i)[0]==True): # int a; Check
                                        print("Accepted")   
                 
                    if(cfg[i]=="DT"): # int Check
                        body(cfg,i)
                        if(body(cfg,i)[0]==True):# a Check
                            i=check[1]
                            if(body(cfg,i)[0]==True): # ; Check
                                i=check[1]
                                i=i+1
                                if(cfg[i]=="else"): # else Check
                                    else_s(cfg,i)
                                    if(else_s(cfg,i)[0]==True): # int a; Check
                                        print("Accepted")
                            
                '''
ifelses()