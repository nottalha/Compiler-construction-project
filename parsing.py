import re
# single lower alphabet  =  int
# number  = 
string = "if ( a > b ) int a ; else int a ;"

with open('e2-example.txt') as t:
    string = t.read()
    print(string)
	# text = t.read().split()
numbers = re.findall(r'[0-9]+', string)
alpha = re.findall(r'[a-z]+',string)
operators = ["<",">","=","<=",">=","==","!=","%"]

datatype = ['int','float','char','bool','double','string']

def parseTree(value):
    if(value in datatype):
        return "DT"
    if(value == "="):
        return "Asop"
    if(value in operators):
        return "Op"
    if(value == ","):
        return ","
    if(value in numbers):
        return "Int_const"
    if(value==";"):
        return ";"
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
    if(value == "if"):
        return "if"
    if(value in alpha):          # if(value == alpha):   #right one
        return "ID"
    else:
        return "Error"
    

stri = string.split();
print(stri)

cfg=[]

for char in stri:
    cfg.append(parseTree(char))
print(cfg)
check =[]
check.insert(0,False)

BracFlag = False

def Decl(cfg,i):
    if(cfg[i]=="DT"):
        i=i+1
        if(cfg[i]=="ID"):
            i=i+1
            check.insert(0,True)
            check.insert(1,i)
            return check
          
def cond(cfg,post):                     # if ( Condition )
    if(cfg[post] == "ID"):
        post=post +1
        if(cfg[post]=="Op"):
            post=post+1;
            if(cfg[post]=="ID"):
                check.insert(0,True)
                check.insert(1,post)
                return check
            else: 
                check.insert(0,False)     

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
    #     sst(cfg,post)
         if( sst(cfg,post)[0]==True):
            return check
    elif(cfg[post]==";"):
        check.insert(0,True)
        check.insert(1,post)
        return check
               
def ifelses():
    i=0
    if(cfg[i]=="if"): # IF Check
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

                    if(cfg[i]=="DT"): #  {} Check
                        body(cfg,i)
                        if(body(cfg,i)[0]==True):# a Check
                            i=check[1]
                            if(body(cfg,i)[0]==True): # ; Check
                                i=check[1]
                                i=i+1
                                if(cfg[i]=="}" and BracFlag == True): # IF Check
                                    i=i+1

                                if(cfg[i] !="else"): # else Check
                                    print("Accepted")
                                if(cfg[i]=="else"): # else Check
                                    else_s(cfg,i)
                                    if(else_s(cfg,i)[0]==True): # int a; Check
                                        print("Accepted")                    
                else:
                    print("error")
                '''
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