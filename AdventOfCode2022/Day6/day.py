import os

def get_markers(lines):
    res = []

    for line in lines:
        s = set()
        for counter in range(len(line)-4):
            a, b, c, d, e, f, g, h, i, j, k, l, m, n = line[counter:counter+14]
            vals = line[counter:counter+14]
            s.update(vals)
            if(len(s)==14):
                res.append(counter+14)
                break
            else:
                s.remove(a)

    return res




def run(input):
    lines = input.splitlines()

    res = get_markers(lines)
    print(res)

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