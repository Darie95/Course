def balance(expression):
    balanced = "YES"
    if len(expression) % 2 != 0:
        print("NO")
    else:
        opening = []
        for bracket in expression:
            if bracket == ')':
                if len(opening) == 0 or opening[-1] != '(':
                    balanced = "NO"
                    break
                else:
                    opening.pop()
            elif bracket == '}':
                if len(opening) == 0 or opening[-1] != '{':
                    balanced = "NO"
                    break
                else:
                    opening.pop()
            elif bracket == ']':
                if len(opening) == 0 or opening[-1] != '[':
                    balanced = "NO"
                    break
                else:
                    opening.pop()
            else:
                opening.append(bracket)
        if len(opening) != 0:
            balanced = "NO"
            print(balanced)
        else:
            print(balanced)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        balance(expression)