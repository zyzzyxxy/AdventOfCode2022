import os



def get_stack(input):
    avoid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    stack = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [],7: [], 8: [], 9: [] }
    for line in input.splitlines():
        if(len(line) <= 1):
            break;
        try:
            for i in range(0,10):
                try:
                    symbol = line[2+i*4-1]
                    if(symbol not in avoid):
                        stack[i+1].extend(symbol)
                    print(i, symbol)
                except:
                    pass

        except:
            print("exception")
    print(stack)
    return stack


def get_commands(input):
    lines = input.splitlines()
    for i in range(len(lines)):
        if("move" in lines[i]):
            return lines[i:]


def execute_commands(stack, commands):

    for command in commands:
        splitted = command.split(" ")
        amount, source, target = int(splitted[1]), int(splitted[3]), int(splitted[5])
        blocks = stack[source][:amount]
        #blocks.reverse()
        stack[source] = stack[source][amount:]
        t = stack[target]
        blocks.extend(t)
        stack[target] = blocks

        print("hi")

    return stack

def run(input):
    stack = get_stack(input)
    commands = get_commands(input)
    new_stack = execute_commands(stack, commands)

    res_string = ""
    for item in new_stack.items():
        try:
            res_string += item[1][0]
        except:
            pass
    print(res_string)

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