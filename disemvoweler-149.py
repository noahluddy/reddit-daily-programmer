# https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

def disem(str):
    result = ''
    rem_vowels = ''
    vowels = 'aeiou'
    for c in str:
        if c not in vowels and not c.isspace():
            result += c
        elif not c.isspace():
            rem_vowels += c
    print(result + '\n' + rem_vowels)

def main():
    phrase = input('\nPlease enter a line: ')
    disem(phrase)
    choice = input('\nAgain? ')
    if choice != 'n':
        main()
    quit()

main()  # Need to actually call the main() method!
