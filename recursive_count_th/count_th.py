'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    pattern = 'th'
    x = len(pattern)
    if word == "":
        return 0
    if word[0: x] == pattern:
        return count_th(word[x - 1:]) + 1
    return count_th(word[x - 1:])
