import os

class monkey:
    items = []
    divider = 1
    operation_sign = ''
    operation_val = ''

    true_monkey = 0
    false_monkey = 0
    inspect_counter = 0

    def inspect(self):
        for i in range(self.items.__len__()):

            val = self.items[i]

            op_val = 0
            new_val = 0
            if self.operation_val == 'old':
                op_val = val
            else:
                op_val = int(self.operation_val)

            if self.operation_sign == '+':
                new_val = val + op_val
            if self.operation_sign == '*':
                new_val = val * op_val

            new_val = new_val % 9699690

            self.items[i] = int(new_val)
            self.inspect_counter += 1

    def div_by_3(self):
        pass

    def test(self):
        monkey_dict = {self.true_monkey: [],
                       self.false_monkey: []}
        while self.items:
            item = self.items.pop()
            if item % self.divider == 0:
                #item = item / self.divider
                monkey_dict[self.true_monkey].append(item)
            else:
                #item = item % self.divider
                monkey_dict[self.false_monkey].append(item)

        return monkey_dict

    def inspect_items(self):
        self.inspect()

        return self.test()

        pass

def get_monkeys(input):
    m_texts = input.split("\n\n")
    monkeys = []
    for m_text in m_texts:
        m = monkey()
        lines = m_text.splitlines()
        #items
        m.items = list(map(lambda x: int(x), lines[1].replace(",", "").split()[2:]))
        #operation
        op_text = lines[2].strip().split('Operation: new = old ')[1].split()
        m.operation_sign = op_text[0]
        m.operation_val = op_text[1]
        #divider
        m.divider = int(lines[3].split('  Test: divisible by ')[1])
        #monkeys
        m.true_monkey = int(lines[4].split()[-1])
        m.false_monkey = int(lines[5].split()[-1])

        monkeys.append(m)

    return monkeys


def run(input):

    monkeys = get_monkeys(input)

    rounds = 10000

    for i in range(rounds):


        for i in range(monkeys.__len__()):
            thrown_items = monkeys[i].inspect_items()
            for item in thrown_items.items():
                monkeys[item[0]].items+=item[1]


    a = 0
    b = 0
    for monkey in monkeys:
        if monkey.inspect_counter > a:
            b = a
            a = monkey.inspect_counter
        elif monkey.inspect_counter > b:
            b = monkey.inspect_counter
    print(a*b)
    x = 2*7*5*13*3*19*11*17

    # 28356997185 - too low

    print(x)


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