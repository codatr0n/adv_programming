import sys

def main(n):
    x = lambda x: int(x)*int(x)
    print(x(n))

if __name__ == '__main__':
    main(sys.argv[1])
    # print(len(sys.argv))