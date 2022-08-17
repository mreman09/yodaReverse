import random
import string

patience = random.randint(1, 10)


def master_yoda_whisperer(sentance):
    yoda = sentance.split()
    answer = yoda[::-1]
    return ' '.join(answer)


def yoda_tired(session):
    if patience >= session:
        if patience - session < 1:
            print('Talk longer I cannot, time near for me')
        print(patience)
        print(session)
        talk_session(session)
    else:
        print('Tired have become\nLost you must get')
        print('May the 4th be with you')


def talk_session(session):
    sentence = input('Enter what you want Yoda to say: \n')
    if sentence.lower() == 'bye':
        print('May the 4th be with you')
    else:
        print("\n " + master_yoda_whisperer(sentence) + "\n")
        session = session + 1
        yoda_tired(session)


print("\nHow would Yoda say it? ")
session = 0
talk_session(session)

code = [0, 'x']
nm = 0
if nm == code[0]:
    code.pop(0)
    print(len(code))
else:
    print('not same')


def spy_game(nums):
    checker = [0, 0, 7, 'x']
    for item in nums:
        if item == checker[0]:
            checker.pop(0)
    if len(checker) == 1:
        return True
    else:
        return False


spy_game([0, 5, 7, 0, 6, 7])
spy_game([0, 2, 7, 6, 7])
spy_game([0, 2, 7, 6, 7])


def conunt_primes(num):
    if num < 2:
        return 0

    prime = [2]
    x = 3

    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    print(prime)
    return len(prime)


conunt_primes(1000)


def square(num):
    return num ** 2


outerscope = 60


def global_change_example():
    global outerscope
    print(f'outerscope is {outerscope}')
    outerscope = '420'
    print(f'I just locally changed global outerscope to {outerscope} ')


global_change_example()


def ran_check(num, low, high):
    if num > low and num < high:
        print('True')
    else:
        print('Flase')

    if num in range(low, high + 1):
        print('Correcto mondo')
    else:
        print('falseamondo')


ran_check(3, 2, 4)
ran_check(4, 2, 3)
ran_check(123, 1, 1234)


def capitalise_checker(s):
    d = {'capitalise': 0, 'lowercase': 0}
    for char in s:
        if char.isupper():
            d['capitalise'] += 1
        elif char.islower():
            d['lowercase'] += 1
        else:
            pass

    print(f'Original string was {s}')
    print(f'Lowecase count is: {d["lowercase"]}')
    print(f'Uppercase count is: {d["capitalise"]}')


sentance_for_checker = 'There is Going to Be Six Capitalise Letter'

capitalise_checker(sentance_for_checker)


def unique_list(lister):
    myset = set(lister)
    print(myset)

    return list(myset)


repeat_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 6, 7, 8, 88, 8]

unique_list(repeat_list)
repeat_list = unique_list(repeat_list)
print(repeat_list)


def multipleyer(numbers):
    sum = 1

    for number in numbers:
        sum = number * sum

    print(sum)


multipleyer([100, 30, 12])


def check_Alph(str):
    alphabet = string.ascii_lowercase
    alph = set(alphabet);
    str = str.replace(' ', '')
    str = str.lower()
    str = set(str)
    return str == alph


panagram = 'A quick brown fox jumps over the lazy dog'

print(check_Alph(sentance_for_checker))
print(check_Alph(panagram))