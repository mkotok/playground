from __future__ import division, print_function
import itertools
import multiprocessing
import time


def evaluate(exp):
    stack = []
    for op in exp:
        try:
            stack.append(float(op))
        except ValueError:
            op2 = str(stack.pop())
            op1 = str(stack.pop())
            op = op.replace('^', '**')
            z = eval(op1 + op + op2)
            stack.append(z)

    assert len(stack) == 1
    return stack[0]


def solve24(nums):
    for x, y, z in itertools.product("+-*/^", repeat=3):
        for a, b, c, d in itertools.permutations(nums):
            exps = [
                [a,b,c,d,x,y,z],  # needed for 3388
                [a,b,c,x,d,y,z],
                [a,b,c,x,y,d,z],
                [a,b,x,c,d,y,z],  # needed for 1479
                [a,b,x,c,y,d,z],  # needed for 1277
            ]
            for exp in exps:
                try:
                    res = evaluate(exp)
                except ZeroDivisionError:
                    continue
                if round(res, 5) == 24:
                    return ' '.join(map(str, exp))
    return None


def solve24wrapper(case):
    print('.', end='')
    return solve24(case)

###############################################################################

# tests = ['9445', '1727', '5754', '1466', '2373', '8797', '1626', '7941', '6422', '5797', '3388']
# for nums in tests:
#     ans = solve24(nums)
#     print(nums, ans)

# print(solve24('3388'))
# print(solve24('1479'))
# print(solve24('1277'))

print(solve24([0,1,2,5]))

###############################################################################
# digits = range(10)
# ndigits = 4
# cases = list(itertools.combinations_with_replacement(digits, ndigits))

# pool = multiprocessing.Pool(4)
# answers = pool.map(solve24wrapper, cases)
# # answers = map(solve24wrapper, cases)

# print('')
# with open('answers24game.csv', 'w') as f:
#     for case, ans in zip(cases, answers):
#         x = ','.join(map(str, case))
#         y = str(ans)
#         f.write(x + ',' + y + '\n')
