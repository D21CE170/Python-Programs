from unittest import result


def SWAP (B):
    OUTPUT = ''

    for PARAGRAPH in B:
        if PARAGRAPH.isupper()==True:
            OUTPUT += (PARAGRAPH.lower())
        else :
            OUTPUT += (PARAGRAPH.upper())
    return OUTPUT

if __name__ == '__main__':
    B = input()
    RESULT = SWAP(B)
    print(RESULT)