import re

def makeListOfGrammar(file):
    """
    S -> AB
    A -> CD | CF
    B -> c | EB
    C -> a
    D -> b
    E -> c
    F -> AD

    Nanti hasilnya
    [['S', ['A B']], ['A', ['C D', 'C F']], ['B', ['c', 'E B']], ['C', ['a']], ['D', ['b']], ['E', ['c']], ['F', ['A D']]

    biar gampang ngeceknya di CYK
    """
    file = open(file, 'r')
    lines = file.readlines()
    file.close()

    grammar = []
    for line in lines:
        templateGrammar = [0, 0]
        templateRHS = []
        tempLine = line.strip()
        hasAtleastOneRHS = False

        #copies the left hand side
        stringLHS = ''
        idx = 0
        while(tempLine[idx] != ' '):
            stringLHS += tempLine[idx]
            idx += 1
        templateGrammar[0] = stringLHS

        #sets it so that the idx is now on the first non space character RHS
        idx += 4

        # Copies the right hand side
        stringRHS = ''
        for i in range(idx, len(tempLine)):
            if (tempLine[i] != '|'):
                stringRHS += tempLine[i]
            elif (tempLine[i] == '|'):
                hasAtleastOneRHS = True
                templateRHS.append(stringRHS[:(len(stringRHS) - 1)])    #adds it to the db
                stringRHS = ''                                          #resets the string
        if hasAtleastOneRHS:
            templateRHS.append(stringRHS[1:])
        else:
            templateRHS.append(stringRHS)                               #all these are shitty implementations on fixing spaces
        templateGrammar[1] = templateRHS
        grammar.append(templateGrammar)
    # print(grammar)
    return grammar

def zerothLine(tokenizedString):
    zerothLine = []
    string = ''
    for i in range(len(tokenizedString)):
        if (tokenizedString[i] != ' '):
            string += tokenizedString[i]
        else:
            zerothLine.append(string)
            string = ''
    zerothLine.append(string)
    return zerothLine

def makeTokenizedString():
    file = open('tokenized.txt', 'r')
    tokenizedString = file.read()
    file.close()
    # print(tokenizedString)
    tokenizedString = re.sub('OLCOMMENT ', '', tokenizedString)
    tokenizedString = re.sub(' OLCOMMENT', '', tokenizedString)
    tokenizedString = re.sub(' COMMENT', '', tokenizedString)
    tokenizedString = re.sub('COMMENT ', '', tokenizedString)
    print(tokenizedString)
    return tokenizedString[:(len(tokenizedString)-1)] #removes the space on the end

def doCYK(tokenizedString, grammarFile):
    """
    masukannya tokenizedString sama source file grammarnya (contoh formatting grammar ada di testg.txt).
    Returns True kalo salah satu hasil di ujungnya S. 
    """
    grammar = makeListOfGrammar(grammarFile)
    linezero = zerothLine(tokenizedString)
    cykArray = []
    matched = []
    # https://web.cs.ucdavis.edu/~rogaway/classes/120/winter12/CYK.pdf (naming reference)
    # [['S', ['A B']], ['A', ['C D', 'C F']], ['B', ['c', 'E B']], ['C', ['a']], ['D', ['b']], ['E', ['c']], ['F', ['A D']]
    for i in range(len(linezero)): # ['a', 'a', 'a', 'b', 'b', 'b', 'c']
        matchedEl = []
        for rule in grammar: # ['S', ['A B']]
            for RHS in rule[1]: # ['A B']
                if linezero[i] == RHS:
                    matchedEl.append(rule[0]) #appends the LHS to the matched array
        matched.append(matchedEl)
    cykArray.append(matched)
    #FIRST LINE DONE HORRAY, we now go on

    for i in range(1, len(linezero)):            # Traverses downwards so we make the other lines
        matched = []                            
        for j in range(len(linezero)-i):         # Traverses to the right so we start from the left to the right
            matchedEl = set()
            for x in range(i):                      # on that point, we check the possible symbol boxes for checking
                for startSymbol in cykArray[x][j]:
                    stringCheck = ''
                    # print(i, j, x)
                    for endSymbol in cykArray[i-x-1][j+x+1]:
                        stringCheck = startSymbol + ' ' + endSymbol
                        # print(stringCheck)
                        for rule in grammar: # ['S', ['A B']]
                            for RHS in rule[1]: # ['A B']
                                if stringCheck == RHS:
                                    matchedEl.add(rule[0]) #appends the LHS to the matched array
                                    # print(matchedEl)
            matched.append(matchedEl)
        cykArray.append(matched)
    print(cykArray)

    hasSolutions = False
    for solutions in cykArray[len(linezero)-1][0]:
        if solutions == 'S':
            hasSolutions = True
    return hasSolutions



# print(doCYK("ID OPEN_PAREN TYPE_STR2 CLOSE_PAREN", "grammar.txt")) #make grammar di sini https://www.xarg.org/tools/cyk-algorithm/