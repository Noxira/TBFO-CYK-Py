import os
import sys
import Tokenizer
import CYKParser as cyk

""" main """

if len(sys.argv) == 1:
    print('Tidak ada input file python!')
    exit()
else:
    statements = """"""
    if os.path.isfile(sys.argv[1]):
        file = open(sys.argv[1], 'r')
        read_content = file.read()
        statements = statements + read_content
        file.close()

        result = """"""
        line = int(1)
        for token in Tokenizer.tokenize(statements):
            # if token.line != line:
            #     line += 1
            #     result += '\n'
            result += token.type + ' '
        # result = re.sub()
        # print(result)
        fileRes = open('tokenized.txt', 'a')
        fileRes.truncate(0) #removes whatevers inside
        fileRes.write(result)
        fileRes.close()
        tknstr = cyk.makeTokenizedString()
        checksyntax = cyk.doCYK(tknstr,'CNF.txt')
        if (checksyntax == True):
            print('Program Accepted!!')
        else:
            print('Syntax Error!')
    else:
        print('file '+sys.argv[1]+' tidak ditemukan!')

[
    [['IF'], ['BOOLEAN', 'EXPRESSION_IN_PAREN', 'EXPRESSION_IN_BRACKET', 'EXPRESSION', 'S', 'S'], ['COMP'], ['BOOLEAN', 'EXPRESSION_IN_PAREN', 'EXPRESSION_IN_BRACKET', 'EXPRESSION', 'S', 'S'], ['COLON'], ['RETURN'], ['BOOLEAN', 'EXPRESSION_IN_PAREN', 'EXPRESSION_IN_BRACKET', 'EXPRESSION', 'S', 'S']], 
    [[], ['EXPRESSION9', 'EXP_COMP_EXP25'], [], [], [], ['RETURN_METHOD', 'S']], 
    [[], ['EXPRESSION', 'EXPRESSION_IN_PAREN', 'EXPRESSION_IN_BRACKET', 'S', 'EXP_COMP_EXP', 'EXPRESSION_IN_PAREN'], [], [], []], 
    [['IF_METHOD32'], [], [], []], 
    [['IF_METHOD', 'S'], [], []], 
    [[], []], 
    [[]]
]