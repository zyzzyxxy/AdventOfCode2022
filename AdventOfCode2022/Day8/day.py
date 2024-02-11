import os



def run(input):

    horizontal_lines = input.splitlines()

    rows = horizontal_lines.__len__()
    cols = horizontal_lines[0].__len__()
    outer_nbr = horizontal_lines.__len__()*2 + (horizontal_lines[0].__len__()-2) * 2
    #print (outer_nbr)

    vertical_lines = ['']*cols
    for line in horizontal_lines:
        for i in range(line.__len__()):
            vertical_lines[i] += line[i]

    # visible_trees = []
    # for row in range(1,rows-1):
    #     for col in range(1, cols-1):
    #         tree = int(horizontal_lines[row][col])
    #         h_line = horizontal_lines[row]
    #         v_line = vertical_lines[col]
    #
    #         #check left
    #         visible = True
    #         for i in range(col):
    #             nbr = int(h_line[i])
    #             if(nbr >= tree ):
    #                 visible = False
    #
    #         #check right
    #         if not visible:
    #             visible = True
    #             for i in range(cols-col-1):
    #                 nbr = int(h_line[cols-i-1])
    #                 if (nbr >= tree):
    #                     visible = False
    #         #check up
    #         if not visible:
    #             visible = True
    #             for i in range(row):
    #                 nbr = int(v_line[i])
    #                 if (nbr >= tree):
    #                     visible = False
    #
    #         #check down
    #         if not visible:
    #             visible = True
    #             for i in range(rows - row - 1):
    #                 nbr = int(v_line[rows - i - 1])
    #                 if (nbr >= tree):
    #                     visible = False
    #
    #         if visible:
    #             visible_trees.append(tree)

        #print(visible_trees)
    #tot = outer_nbr + len(visible_trees)
    #print(tot)
        #1595 too low

            # check right

            # check up
            # check down

    visible_trees = []
    max = 0
    for row in range(rows):
        for col in range(cols):
            tree = int(horizontal_lines[row][col])
            h_line = horizontal_lines[row]
            v_line = vertical_lines[col]

            #check left
            left = 0
            visible = True
            for i in range(col):
                left += 1
                nbr = int(h_line[col-i-1])
                if(nbr >= tree ):
                    break

            #check right
            right = 0
            for i in range(cols-col-1):
                right += 1
                nbr = int(h_line[col+i+1])
                if (nbr >= tree):
                    break
        #check up
            up = 0
            for i in range(row):
                up += 1
                nbr = int(v_line[row-i-1    ])
                if (nbr >= tree):
                    break

            #check down
            down = 0
            for i in range(rows - row - 1):
                down += 1
                nbr = int(v_line[row + i + 1])
                if (nbr >= tree):
                    break

            sum = left*right*up*down
            print(sum)
            if sum>max:
                max = sum
    print(max)
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