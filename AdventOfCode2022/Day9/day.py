import os

class dot():
    x = 0
    y = 0

    def is_touching(self, dot2):
        if abs(self.x-dot2.x) >1 :
            return False
        if abs(self.y-dot2.y) >1 :
            return False
        return True

    def update_tail(self, head):
        #update x
        if head.x < self.x:
            self.x -= 1
        elif head.x > self.x:
            self.x += 1

        if head.y < self.y:
            self.y -= 1
        elif head.y > self.y:
            self.y += 1


def print_dots(dots):
    d = '....................................................'
    grid = [d]*50
    offset = 20
    print()
    for i in range(dots.__len__()):
        dot = dots[i]
        line_index = grid.__len__() - dot.y - 1 - offset
        print('lineindex',line_index)
        new_line = list(grid[line_index])
        new_line[dot.x + offset] = str(i)
        grid[dot.y] = "".join(new_line)


    for row in grid:
        print(row)



def run(input):

    commands = input.splitlines()

    #head = dot()
    dots = []
    #tail = dot()

    for i in range(10):
        dots.append(dot())

    start = (0, 0)

    visited = []
    visited.append(start)
    print(visited)

    for command in commands:
        #move head
        direction, steps = command.strip().split()
        steps = int(steps)
        for i in range(steps):
            head = dots[0]
            #update head
            if direction == 'R':
                dots[0].x +=1
            if direction == 'L':
                dots[0].x -= 1
            if direction == 'U':
                dots[0].y += 1
            if direction == 'D':
                dots[0].y -= 1
            #print(head.x, head.y)

            #update tail
            #Check touching
            for i in range(dots.__len__()-1):
                if not dots[i].is_touching(dots[i+1]):
                    dots[i+1].update_tail(dots[i])
            pos = (dots[-1].x, dots[-1].y)
            if pos not in visited:
                visited.append(pos)
       # print_dots(dots)

        print(visited.__len__())

        pass

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