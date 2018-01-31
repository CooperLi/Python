def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)
running = True
while running:
    something = input('Enter text: ')
    if something == 'quit':
        running = False
    if is_palindrome(something):
        print('Yes, it is a palindrome')
    else:
        print('No, it is not a palindrome')

