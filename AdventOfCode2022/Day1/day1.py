import os


def get_list(input):
    elves = input.split("\n\n")
    elf_list = []
    counter = 0
    for elf in elves:
        e = {}
        counter += 1
        e[counter] = elf.splitlines()
        elf_list.append(e)

    return elf_list


def highest_cal(elf_list):
    highest = 0
    elf_cals = []
    for elf in elf_list:
        cal = 0
        lines = list(elf.values())
        for line in lines[0]:
            print(line)
            cal += int(line)
        elf_cals.append(cal)
        if cal > highest:
            highest = cal
    elf_cals.sort()

    ##2nd answer here
    print(sum(elf_cals[-3:]))
    return highest


def run(input):
    elf_list = get_list(input)
    high_cal = highest_cal(elf_list)
    print(high_cal)

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