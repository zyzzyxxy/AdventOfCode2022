import os
import networkx as nx

def run(input):
    G = nx.Graph
    print(input)

    lines = input.splitlines()
    for col in range(lines.__len__()):
        for row in range(lines[0].__len__()):
            char = lines[col][row]
            print(char, ord(char))
            val = ord(char) - 97
            id = (col+1) * (row+1)
            print(id)
            attr = {"val":val, "row":row, "col":col}
            G.add_node(id, attr)





    return input





if __name__ == "__main__":
    os.getcwd()
    f = open("./input", 'r')
    text = f.read()
    f.close()

    result = run(text)

    f = open("./output", "w")
    f.write(result)
    f.close()