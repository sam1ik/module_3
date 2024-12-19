# Задача 'Счетчик вызовов'
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_1 = str(string)
    res = (len(string_1), string_1.upper(), string_1.lower())
    count_calls()
    return res

def is_contains(string, list_to_search):
    string_2 = str(string)
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string_2:
            res = True
            break
        else:
            res = False
            continue
    return res

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) #Urban ˜ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
