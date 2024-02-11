import os

def run(input):

    lines = input.splitlines()

    x_arr = []
    x = 1
    size = lines.__len__()
    for line in lines:
        if line[0] != 'n':
            cmd, val = line.split()
            print(cmd, val)
            n = int(val)
            print(x,n, x+n)
            x_arr.append(x)
            x_arr.append(x)
            x = x + n

        else:
            x_arr.append(x)


    start = 20
    totsum = 0
    sums = []
    screen = []
    counter = 0
    for i in range(6):
        row = []
        for i in range(40):

            reg = x_arr[counter]
            #sums.append(i*x_arr[i-1])
            #print(i)
            if i == reg or i == reg - 1 or i == reg + 1:
                row.append('#')
            else:
                row.append('.')

            counter += 1
        screen.append(row)

    print(sums)
    print(totsum)
    print(6*40)
    for row in screen:
        print("".join(row))


    return input





if __name__ == "__main__":
    os.getcwd()
    f = open("./input", 'r')
    text = f.read()
    f.close()

    result = run(text)

    b = ['x' for i in range(10)]
    print(b)

    f = open("./output", "w")
    f.write(result)
    f.close()