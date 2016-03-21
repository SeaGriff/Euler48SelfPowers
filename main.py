""" Solves project euler problem 48.
"""

# Constants
NUM_DIGITS = 10
SEQUENCE_LENGTH = 1000

def main():
    result = 0
    for i in range(1,SEQUENCE_LENGTH + 1):
        result += pow(i, i, 10**NUM_DIGITS)
    result %= 10**NUM_DIGITS
    print(result, len(str(result)))

if __name__ == "__main__":
    main()