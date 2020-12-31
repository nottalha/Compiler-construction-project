import re
keywords = {"scanf","%d","#include","main()","<stdio.h>","cout",
"auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while","printf","else",
"namespace","std","<iostream>"}

operators = {"+","-","*","/","<",">","=","<=",">=","==","!=","++","--","%"}

delimiters = {'(',')','{','}','[',']','"',"'",';','#',',',''}

comments = ['##', '###', 'comment', 'commentEnd']		

datatype = ['int','float','char','bool','double','string']



def detect_keywords(text):
	arr = [] 
	for word in text:
		if word in keywords:
			arr.append(word)
	return list(set(arr))

def detect_comment(text):
	arr = []
	str1 = ''
	count = 0
	
	for word in text:
		count=count +1
		if(word == comments[0]):
			for f in text[count:]:
				if(f == comments[1]):
						break
				else:
					str1 = str1 +" "+ f
					continue
			arr.append(str1)
			str1 = " "		
				

	return list(set(arr))
'''			
		if(word == comments[1]):
			for word in '*/':
				if(word == '*/'):
						break
				else:
						arr.append(word)
						print(word)
'''
	#		if(word == comments[1]):
	#				for word in text:
	#						if(word != '*/'):
	#									arr.append(word)
	#						else:
	#   							continue

def listingOfComment(text):
	arr = []
	
	for word in text:
			for w in word.split():
				arr.append(w)
	return list(set(arr))

def detect_operators(text):
	arr = []
	for word in text:
		if word in operators:
			arr.append(word)
	return list(set(arr))

def detect_datatype(text):
	arr = [] 
	for word in text:
		if word in datatype:
			arr.append(word)
	return list(set(arr))

def detect_delimiters(text):
	arr = []
	for word in text:
		if word in delimiters:
			arr.append(word)
	return list(set(arr))

def detect_num(text):
	arr = []
	for word in text:
		try:
			a = int(word)
			arr.append(word)
		except:
			pass
	return list(set(arr))
"""
this is original function for detecting identifier
def is_identifier(token):
    if token[0] in numbers or token in keywords:
        return False
    else:
        return identifier(token)


def identifier(token):
    if len(token)<2 and (token[0] in alphabets or token[0] in numbers or token[0] == "_"):
        return True
    elif token[0] in alphabets or token[0] in numbers or token[0] == "_":
        return identifier(token[1:])
    else:
        return False
"""
def detect_identifiers(text):
	k = detect_keywords(text)
	o = detect_operators(text)
	d = detect_delimiters(text)
	n = detect_num(text)
	m = listingOfComment(detect_comment(text))
	not_ident = k + o + d + n + m
	arr = []
	for word in text:
		if word not in not_ident:
			arr.append(word)
	return arr



with open('e1-example.txt') as t:
	text = t.read().split()

''''




'''
print("Keywords: ",detect_keywords(text))
print("DataType: ",detect_datatype(text))
print("Operators: ",detect_operators(text))
print("Numbers: ",detect_num(text))
# print("checking", listingOfComment(detect_comment(text)))

print("Delimiters: ",detect_delimiters(text))

# print("Identifiers: ",detect_identifiers(text))
print("comments: ",detect_comment(text))