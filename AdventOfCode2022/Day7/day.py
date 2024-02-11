import os


def get_dir_content(input):

    lines = input.splitlines()
    current_dir = None
    dirs_with_content = {}
    path = []
    for line in lines:
        words = line.strip().split()
        if(words[1] == 'cd'):
            if(words[2] == '..'):
                path.pop()
            else:
                path.append(words[2])

        if('$ cd ' in line and not '$ cd ..' in line):
            dir = line.split('$ cd')[1].strip()
            current_dir = "/".join(path)
            dirs_with_content[current_dir] = []
        elif(line[0] == '$'):
            pass
        else:
            dirs_with_content[current_dir].append(line)

    for item in dirs_with_content.items():
        print(item[0])
        for i in item[1]:
            print('\t' + i)

    return dirs_with_content


def get_dir_size(item, dirs_with_content):
    size = 0
    path = item[0]
    for val in item[1]:
        if('dir' in val):
            dir = path + "/" +val.split('dir')[1].strip()

            new_item = (dir, dirs_with_content[dir])
            size += get_dir_size(new_item, dirs_with_content)
        else:
            s = int(val.split(" ")[0].strip())
            size += s

    return size



def get_size_dict(dirs_with_content):
    dirs_sizes = {}

    for item in dirs_with_content.items():
        dirs_sizes[item[0]] = get_dir_size(item, dirs_with_content)

    return dirs_sizes




def run(input):
    dirs_with_content = get_dir_content(input)
    size_dict = get_size_dict(dirs_with_content)

    print(size_dict)
    totsize = 0
    for val in size_dict.values():
        totsize += val

    free = 70000000 - size_dict['/']

    least_to_delete = 30000000 - free

    cand = []
    for val in size_dict.values():
        if val >= least_to_delete:
            cand.append(val)
    cand.sort()
    print(cand)
    print(cand[0])


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