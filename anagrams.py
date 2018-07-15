def makeAnagram(a, b):
    result = 0
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)
    for char in a:
        a_dict[char] += 1
    for char in b:
        b_dict[char] += 1
    for char in list(string.ascii_lowercase):
        result += abs(a_dict[char] - b_dict[char])
    print(result)


if __name__ == '__main__':
    a = input()

    b = input()

    makeAnagram(a, b)
