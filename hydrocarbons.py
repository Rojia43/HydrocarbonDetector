import re

def IdentifyNumOfCarbons(input):
    global length 
    if(re.search('meth', input)):
        length -= 4
        return 1
    elif(re.search('eth', input)):
        length -= 3
        return 2
    elif(re.search('prop', input)):
        length -= 4
        return 3
    elif(re.search('but', input)):
        length -= 3
        return 4
    elif(re.search('pen', input)):
        length -= 3
        return 5
    elif(re.search('hex', input)):
        length -= 3
        return 6
    elif(re.search('hept', input)):
        length -= 4
        return 7
    elif(re.search('oct', input)):
        length -= 3
        return 8
    elif(re.search('non', input)):
        length -= 3
        return 9
    elif(re.search('dec', input)):
        length -= 3
        return 10
    else:
        print("Invalid input!")
        quit()

def IdentifyNumOfBonds(input):
    global length
    if(re.search('ane', input)):
        length -= 3
        return 1
    elif(re.search('ene', input)):
        length -= 3
        return 2
    elif(re.search('yne', input)):
        length -= 3
        return 3
    else:
        print("Invalid input!")
        quit()

def IdentifyCyclo(input):
    global length
    if(re.search('cyclo', input)):
        length -= 5
        return True

input = input("Type in a simple hydrocarbon's IUPAC name!: ")
length = len(input)
IdentifyNumOfCarbons(input)
IdentifyNumOfBonds(input)
IdentifyCyclo(input)

'''def IdentifySubstituents(input):
    global length
    temp = input[0:length]
    pattern = r'[,-]'
    parts = re.split(pattern, temp)
    print(parts)
    pattern = r'yl'
    matches = [s for s in parts if re.match(pattern, s)]
    print(matches)

IdentifySubstituents(input)'''