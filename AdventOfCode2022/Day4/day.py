import os


def get_pairs_from_line(line):
    units = str(line).split(",")
    print(units)
    first = units[0].split("-") 
    second = units[1].split("-") 
    tuple1 = (int(first[0]),int(first[1]))
    tuple2 = (int(second[0]),int(second[1]))
    pair = (tuple1, tuple2)
    return pair


def get_pairs(input):
    lines = input.splitlines()
    pairs = list(map(get_pairs_from_line, lines))
    return pairs


def get_amount_encloes_pairs(pairs):
    sum = 0
    pairs_hit = []
    for p in pairs:
        if(p[0][0] <= p[1][0] and  p[0][1] >= p[1][1]):
            sum+=1
            pairs_hit.append(p)
        elif(p[1][0] <= p[0][0] and  p[1][1] >= p[0][1]):
            sum+=1
            pairs_hit.append(p)
    return sum

def get_amount_overlap_pairs(pairs):
    sum = 0
    pairs_hit = []
    for p in pairs:
        val1 = p[0][0]
        val2 = p[0][1]
        val3 = p[1][0]
        val4 = p[1][1]
        if(val3 >= val1 and val3 <= val2):
            sum+=1
            pairs_hit.append(p)
        elif(val4 >= val1 and val4 <= val2):
            sum+=1
            pairs_hit.append(p)
        elif(val1 >= val3 and val1 <= val4):
            sum+=1
            pairs_hit.append(p)
        elif(val2 >= val3 and val2 <= val4):
            sum+=1
            pairs_hit.append(p)
    return sum

def run(input):
    input.replace(" ", "")
    pairs = get_pairs(input)
    amount = get_amount_overlap_pairs(pairs)
    print(amount)

    return input

#556 too high




if __name__ == "__main__":
    os.getcwd()
    f = open("./input", 'r')
    text = f.read()
    f.close()

    result = run(text)

    f = open("./output", "w")
    f.write(result)
    f.close()