def Xpow (x , y) :
    val = 1
    for i in range(y) :
        val = x * val
    return val

def BaseToDec (base , toHexa , tab) :
    toHexa = str(toHexa)
    lenght = len(toHexa)
    value = 0
    for i in range(lenght) :
        one = Xpow(base , i) * int(( 10 + tab.index(int(toHexa[(lenght - 1) - i]))) if int(toHexa[(lenght - 1) - i]) in tab else int(toHexa[(lenght - 1) - i]))
        value += one
    return value


def DecToBase (base , toHexa , tab ) :
    quotient = toHexa
    hexa = ""
    while  True :
        modulo = quotient % base
        quotient  = int(quotient / base)
        hexa = str(( tab[ (modulo%10)]  if modulo >= 10  else modulo )) + hexa
        if quotient == 0 :
            break
    return hexa


def toInto(InputBase , Value , OutputBase):
    tab = ["A", "B" , "C" , "D" , "E" , "F"]
    return str(DecToBase(OutputBase , BaseToDec(InputBase , Value , tab) , tab))


"""
    [
        [1,0,0],
        [0,1,0]
    ]
"""


def countVar(toCalc):
    variables = []
    toCalc = str(toCalc).lower()
    i = 0
    for x in toCalc:
        if not(str(x).isspace()):
            if (x <= "z" and x >= "a") and ((((i == len(toCalc) - 1) or not(toCalc[i + 1] <= "z" and toCalc[i + 1] >= "a")) and toCalc[i - 1] == " ") or ((i == 0 or not(toCalc[i - 1] <= "z" and toCalc[i - 1] >= "a")) and toCalc[i + 1] == " ") or (toCalc[i - 1] == "(" and toCalc[i + 1] == ")")):
                    if not(x in variables):
                        variables.append(x)
        i += 1
    return variables

def indexReplace(chaine , index , car):
    return f"{chaine[:index]}{car}{chaine[index + 1:]}"


def AentreZ(x):
    return (x <= "z" and x >= "a")

def analyse(toCalc , line , variables):
    toCalc = str(toCalc).lower()
    i = 0
    for x in toCalc:
        if not(str(x).isspace()):
            if (x <= "z" and x >= "a") and ((((i == len(toCalc) - 1) or not(toCalc[i + 1] <= "z" and toCalc[i + 1] >= "a")) and toCalc[i - 1] == " ") or ((i == 0 or not(toCalc[i - 1] <= "z" and toCalc[i - 1] >= "a")) and toCalc[i + 1] == " ") or (toCalc[i - 1] == "(" and toCalc[i + 1] == ")")):
                toCalc = indexReplace(toCalc , i , line[variables.index(x)])
        i += 1
    return int(eval(toCalc))

def mytable(variables):
    max = ""
    table = []
    print("\n")
    for x in variables:
        max += "1"
    max = int(max)
    max = toInto(2 , max , 10)
    for x in range(int(max) + 1):
        add = []
        res = toInto(10, x, 2)
        for y in res:
            add.append(int(y))
        if len(add) < len(variables):
            for y in range(len(variables) - len(add)):
                add.insert(0 , 0)
        table.append(add)
    return table

def TrulyTable (generator):
    generator = str(generator).lower()
    variables = countVar(generator)
    
    table1 = []
    table2 = []
    string1 = []
    string2 = []
    lines = ""
    count = 0
    k = 0
    table = mytable(variables)
    len_var = len(variables)
    if (len_var/2) > (int)(len_var/2):
        count = (int)(len_var/2) + 1
    else:
        count = (int)(len_var/2)

    for k in range(count):
        string1.append(f"{variables[k]}")
    
    table1 = mytable(string1)

    while count < len_var:
        string2.append(f"{variables[count]}")
        count += 1

    table2 = mytable(string2)

    for t in range(len(string2)):
        lines += f"{string2[t]}"
    
    lines += '\\'
    for t in range(len(string1)):
        lines += f"{string1[t]}"
    
    lenght = len(lines)
    lines += " | "
    for t in range(len(table1)):
        for z in range(len(table1[0])):
            lines += f"{table1[t][z]}"
        lines += " | "
    hr = ""
    for t in range(len(lines) - 1):
        hr += "-"
    lines += "\n"
    lines += hr
    lines += "\n"

    x = 0
    for t in range(len(table2)):
        for z in range(len(table2[0])):
            lines += f"{table2[t][z]}"
        space = ""
        for t in range(lenght - 1):
            space += ' '
        lines += space
        lines += " | "
        len_table = len(table)
        while x < len_table:
            lines += f"{analyse(generator, table[x], variables)}"
            space = ""
            for t in range(len(table1[0]) - 1):
                space += ' '
            lines += space
            x += 2
            lines += " | "
        x = 1
        lines += "\n"
        # lines += hr
        # lines += "\n"
    print("la carte de Karnaugh :\n\n" + lines + "\n\n")
    return 1

Start = input("Veuillez entrer l'expression de la fonction logique\n>>")
TrulyTable(Start.strip())
