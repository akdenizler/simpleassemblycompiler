import re

#does this count as a compiler???? 

opcodes = {'xor':'00', 'eq':'01', 'add':'10', 'mov':'11'}
registers = {'reg0':'00', 'reg1':'01', 'reg2':'10', 'reg3':'11'}

instruction = [] #holds 8-bit strings

TOKEN_RE = re.compile(r"reg[0-3]|==|[A-Za-z]+", re.ASCII) #regex my love

def strip_comment(line: str) -> str: #ignore comments
    return line.split(";", 1)[0].strip()

def lexer_from_file(path: str): #read assembly instructions
    return [t.lower() for line in open(path, 'r', encoding='utf-8') for code in [strip_comment(line)] if code for t in reversed(TOKEN_RE.findall(code))]

def parse_stuff(): # we take the stuff and then we know the pattern so we just ... yeah
    while tokens:
        instruction.append("00" + registers[tokens[-2]] + registers[tokens[-3]] + opcodes[tokens[-1]])
        del tokens[-3:]
        
def die_ausgabe(): #the output (in german)
    print("\n".join(reversed(instruction)))
        

if __name__ == "__main__":
    tokens = lexer_from_file("text.txt")
    parse_stuff()
    die_ausgabe()

    



