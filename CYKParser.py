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

def doCYK(tokenizedString, grammar):
    linezero = zerothLine(tokenizedString)
    cykArray = [['.' for j in range(len(linezero))] for i in range(len(linezero))]
    
