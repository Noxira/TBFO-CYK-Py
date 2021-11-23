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