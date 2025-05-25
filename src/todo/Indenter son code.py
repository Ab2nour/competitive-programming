i = 0


def indenter(chaine, nv_indentation):
    global i
    if i < len(chaine) - 1:
        if chaine[i] == "{":
            print("   " * nv_indentation, end="")
            print("{")

            if chaine[i + 1] == "}":
                i += 1
                print("   " * nv_indentation, end="")
                print("}")
                indenter(chaine, nv_indentation)

            elif chaine[i + 1] == "{":
                i += 1
                indenter(chaine, nv_indentation + 1)

        elif chaine[i] == "}":
            if chaine[i + 1] == "}":
                i += 1
                print("   " * (nv_indentation - 1), end="")
                print("}")
                indenter(chaine, nv_indentation - 1)
            elif chaine[i + 1] == "{":
                i += 1
                indenter(chaine, nv_indentation)


test = "{{}{{}}}{}\n"

test = input()

indenter(test, 0)
