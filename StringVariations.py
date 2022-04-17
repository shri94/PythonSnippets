def exploringVariousSplits(text):
    print('List of words is text:', text.split(' '))

def splitByDelimiter(text, delimiter):
    print(text.split(delimiter))

def reverseString(text):
    print(text[::-1])

if __name__ == '__main__':
    text = "If sep is not specified or is None, a different splitting\
    algorithm is applied: runs of consecutive whitespace are regarded\
    as a single separator, and the result will contain no empty strings\
    at the start or end if the string has leading or trailing whitespace.\
    Consequently, splitting an empty string or a string consisting of\
    just whitespace with a None separator returns []."

    exploringVariousSplits(text)

    splitByDelimiter(text, ',')
    
    reverseString(text)
