import os

rock = 1
paper = 2
scissor = 3
loss = 0
draw = 3
win = 6

score_dict = {'rock' : 1, 'paper' : 2 , 'scissor' : 3, 'loss': 0, 'draw': 3, 'win': 6}
rps_win_dict = {'rock':'scissor', 'paper':'rock', 'scissor':'paper'}
elf_dict = {'A':'rock', 'B':'paper', 'C':'scissor' }
strat_dict = {'X':'rock', 'Y':'paper', 'Z':'scissor' }
#X lose, Y draw, Z win



def rock_paper_scissor_score(elf_hand, my_hand):
    global score_dict
    #elf win
    if(rps_win_dict[elf_hand] == my_hand):
        return 0
    if(rps_win_dict[my_hand] == elf_hand):
        return 6

    return 3


def get_hand(elf_hand, param):
    my_hand = ''
    if(param == 'Y'):
        my_hand = elf_hand
    if(param == 'X'):
        my_hand = rps_win_dict[elf_hand]
    if(param == 'Z'):
        items = rps_win_dict.items()
        for item in items:
            if(item[1] == elf_hand):
                my_hand = item[0]

    return my_hand


def get_score(line):
    score = 0

    #Check hand
    values = line.split(" ")
    elf_hand = elf_dict[values[0]]

    my_hand = get_hand(elf_hand, values[1])
    hand_score = score_dict[my_hand]

    #Check round
    round_score = rock_paper_scissor_score (elf_hand, my_hand)


    score += hand_score
    score += round_score


    return score

def get_totalscore(input):
    lines = input.splitlines()
    score = 0
    for line in lines:
        score += get_score(line)
    return score


def run(input):
    score = get_totalscore(input)
    print(score)
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