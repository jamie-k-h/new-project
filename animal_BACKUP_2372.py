import sys

def cat():
    print('Meow!')

def default():
    print('Hello')

def dog():
    print('Woof!')

def main():
<<<<<<< HEAD
    if sys.argv[1] == 'cat':
        cat()
    else:
         default()
=======
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()
>>>>>>> dog

if __name__=='__main__':
    main()
