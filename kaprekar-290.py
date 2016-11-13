# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/

def kaprekar(num):
    sq = str(num**2)
    # sq_str = list(str(sq))  Actually don't need this because of list slicing!
    for i in range(1, len(sq)):
        x, y = int(sq[:i]), int(sq[i:])
        if x + y == num and x != 0 and y != 0:
            return True
    return False

def main():
    ln = input().split(' ')
    lst = []
    for i in range(int(ln[0]), int(ln[1])):
        if kaprekar(i):
            lst.append(i)
    print(lst)
    if input('\nAgain? ') != 'n':
        main()
    quit()

main()
