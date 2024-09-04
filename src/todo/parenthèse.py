def bien_parenthesee_old(chaine, i):
    if i < len(chaine):
        while chaine[i] == "(":
            if bien_parenthesee(chaine, i+1) != ")":
                return "_"
            if (i+2 < len(chaine)):
                i += 2
            else:
                i += 1
                break
        return chaine[i]

i = 0

def bien_parenthesee(chaine):
    global i

    print(i)
    if i+1 < len(chaine):
        i += 1
        while chaine[i] in "([{<":
            if chaine[i] == "(" and bien_parenthesee(chaine) != ")":
                return "_"
            elif chaine[i] == "[" and bien_parenthesee(chaine) != "]":
                return "_"
            elif chaine[i] == "{" and bien_parenthesee(chaine) != "}":
                return "_"
            elif chaine[i] == "<" and bien_parenthesee(chaine) != ">":
                return "_"
            if (i+2 < len(chaine)):
                i += 2
            elif (i+1 < len(chaine)):
                i += 1
                print("on sort")
                break
    return chaine[i]

def epure_code(chaine):
    code_epure = ["" for i in range(200)]
    j = 0
    for i in range(len(chaine)):
        if chaine[i] in "()[]{}<>":
            code_epure[j] = chaine[i]
            j += 1

    return "".join(code_epure)


interessant = "()[]{}<>"
interessant2 = "([{<"

test = "(())()coucou"

a = bien_parenthesee(test)