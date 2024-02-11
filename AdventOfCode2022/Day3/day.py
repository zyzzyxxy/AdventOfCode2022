import os


def get_overlapping(rucksacks):
    items = []
    for line in rucksacks:
        length = len(line)
        hsize = int(len(line)/2)
        comp1 = line[0:hsize]
        comp2 = line[hsize:]
        letter_set = set()
        for letter in comp1:
            if(letter in comp2):
                letter_set.add(letter)
        items.extend( list(letter_set))


    return items


def get_prio_scores(overlapping_items):
    #generate score list
    prio = {chr(i + 96): i for i in range(1, 27)}
    prio_upper_case = {chr(i + 64-26): i for i in range(27, 53)}
    prio.update(prio_upper_case)

    sum = 0

    for item in overlapping_items:
        sum += prio[item]

    return sum


def get_group_items(rucksacks):
    counter = 0

    items = []
    running = True
    arr_len = len(rucksacks)
    while running:
        letter_set = set()
        for letter in rucksacks[counter]:
            if letter in rucksacks[counter+1] and letter in rucksacks[counter+2]:
                letter_set.add(letter)
        items.extend(letter_set)

        counter += 3
        if counter >= arr_len:
            running=False


    return items



def run(input):



    rucksacks = input.splitlines()
    #overlapping_items = get_overlapping(rucksacks)
    overlapping_items = get_group_items(rucksacks)
    sum = get_prio_scores(overlapping_items)
    
    print(sum)


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