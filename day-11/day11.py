# imports
from math import floor
from copy import deepcopy
from sympy.ntheory.modular import crt

# monkey class
class Monkey:
    # constructor
    def __init__(self, starting, divisor, is_add, n2, t, f):
        self.items = starting
        self.divisor = divisor
        self.is_add = is_add
        self.number_2 = n2
        self.true_monkey = t
        self.false_monkey = f
        self.inspected = 0

    # return the number of inspected items
    def get_inspected(self):
        return self.inspected

    # perform operation
    def calc_worry(self, n1):
        n2 = self.number_2 if self.number_2 != 'old' else n1
        return n1+n2 if self.is_add else n1*n2

    # check divisibility
    def is_divisible(self, worry):
        return worry % self.divisor == 0

    # get number of monkey to throw to
    def get_monkey(self, is_divisible):
        return self.true_monkey if is_divisible else self.false_monkey

    # get the monkeys current list of items
    def get_items(self):
        return self.items

    # update inspected, and clears the items list
    def clear_items(self):
        self.inspected += len(self.items)
        self.items = []

    # update the list of items if an item is throw
    def update_items(self, item):
        self.items.append(item)

# function that will perform chinese remainder theorem in order to reduce an item
def clean_item(item, moduli):
    remainders = []
    for module in moduli:
        remainders.append(item % module)
    if 0 not in remainders:
        return crt(moduli, remainders)[0]
    else:
        return item

# function that will simulate the monkey Keep Away game. return monkey buiness score
def keep_away(monkey_list, num_rounds, is_worried, moduli):
    for i in range(0, num_rounds):
        # each monkey will inspect their elements
        for monkey in monkey_list:
            items = monkey.get_items()
            for item in items:
                worry = item
                worry = monkey.calc_worry(worry)
                worry = floor(worry/3) if not is_worried else clean_item(worry, moduli)
                is_divisible = monkey.is_divisible(worry)
                monkey_to_throw = monkey.get_monkey(is_divisible)
                monkey_list[monkey_to_throw].update_items(worry)
            monkey.clear_items()
    
    # generate the list of the number of inspected for each monkey.
    # return the product of the two largest inspected values
    inspected_arr = [monkey.get_inspected() for monkey in monkey_list]
    inspected_arr.sort()
    return(inspected_arr[-1]*inspected_arr[-2])

def main():
    # open file
    f = open("puzzle.txt", "r")
    monkeys = f.read().split('\n\n')
    
    # next, we need to establish our monkeys
    monkey_list, moduli = [], []
    monkeys = [monkey.split('\n') for monkey in monkeys]
    for monkey in monkeys:
        starting = monkey[1].strip().split(' ')[2:]
        starting = [int(num[:2]) for num in starting]
        operation_arr = monkey[2].strip().split(' ')[4:]
        is_add = True if operation_arr[0] == '+' else False
        n2 = int(operation_arr[1]) if operation_arr[1] != 'old' else operation_arr[1]
        divisor = int(monkey[3].strip().split(' ')[-1])
        moduli.append(divisor)
        true_monkey = int(monkey[4].strip().split(' ')[-1])
        false_monkey = int(monkey[5].strip().split(' ')[-1])
        monkey_list.append(Monkey(starting, divisor, is_add, n2, true_monkey, false_monkey))

    # create a copy of monkey_list for part 2
    monkey_list_copy = [deepcopy(monkey) for monkey in monkey_list]
    moduli.sort(reverse=True)

    # play keep away for both instances
    print(keep_away(monkey_list, 20, False, moduli))
    print(keep_away(monkey_list_copy, 10000, True, moduli))

    # close file
    f.close()

if __name__ == "__main__":
    main()