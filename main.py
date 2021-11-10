# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

math.sqrt(49)
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:" ,mid, ", mid_number", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'



def locate_card(cards, query):
    # create a variable position with value 0
    position = 0
    print('cards:', cards)
    print('query', query)
    # set up loop if len of cards in case its an empty array
    while position < len(cards):

        #check if element at the current position matches the query
        if cards[position] == query:
            return position
        #increment for next card
        position += 1
        # check if we searched all the cards
    if position == len(cards):
        # return -1 if not found the card
        return -1

def locate_card2(cards, query):
    # create a variable for domain of search with lo as start and hi as length of array
    lo, hi = 0, len(cards)-1

    # set up loop if len of cards in case its an empty array
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        #check if element at the current position matches the query
        if result == 'found':
            return mid
        #increment for next card
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
        # check if we searched all the cards
    return -1

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

tests = []

# query in the middle 1
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests.append(test)
# quesry at end 2
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query at begining 3
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query doesn't contain 4
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards empty 5
tests.append({
    'input': {
        'cards': [],
        'query': 4
    },
    'output': -1
})
# number can repeat in cards 6
tests.append({
    'input': {
        'cards': [4, 2, 2, 1, 1, -1],
        'query': 4
    },
    'output': 0
})
# the query can repeat 7
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ** with dictionary takes the dictionary and testes it the way you type (test['input']['cards'], test['input']['query']) == test['output']
    result = locate_card(**test['input']) == test['output']


    print(evaluate_test_cases(locate_card2, tests))

    large_test = {
        'input': {
            'cards': list(range(10000000, 0, -1)),
            'query': 2
        },
        'output': 9999998
    }
    result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
    print("Result: {}\n\033[1;30;42mPASSED\033[0m: {}\nExecution Time: {} ms".format(result, passed, runtime))

