i = 0

def bien_parenthesee(chaine):
    global i
    if i < len(chaine)-1:
        i += 1
        while chaine[i-1] in "([{<":
            #print("passé dans le while (" + chaine[i-1] + ")")
            if chaine[i-1] == "(" and bien_parenthesee(chaine) != ")":
                #print("pb ()")
                return "_"
            elif chaine[i-1] == "[" and bien_parenthesee(chaine) != "]":
                #print("pb []")
                return "_"
            elif chaine[i-1] == "{" and bien_parenthesee(chaine) != "}":
                #print("pb {}")
                return "_"
            elif chaine[i-1] == "<" and bien_parenthesee(chaine) != ">":
                #print("pb <>")
                return "_"
            i += 1
    return chaine[i-1]


def epure_code(chaine):
    code_epure = ["" for i in range(200)]
    j = 0
    for i in range(len(chaine)):
        if chaine[i] in "()[]{}<>":
            code_epure[j] = chaine[i]
            j += 1

    return "".join(code_epure) + "\n"


chaine = "#include <stdio.h> int main(){int liste[2] = {1, 4}; return (liste[0] + liste[1]);}\n" #input()

chaine = input()

chaine = epure_code(chaine)

test = bien_parenthesee(chaine)

#print("(dernier caractère :", test + ")")
#print("(valeur de i :", str(i) + ")")

if test == "\n":
   print("yes")
else:
   print("no")