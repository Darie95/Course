def rotLeft(a, d, n):
    return a[d:n] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
