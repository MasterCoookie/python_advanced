'''
The argparse module allowes to add required and non-required
arguments to be passed while running the program using the console.
In this example the num argument is required and -o (saving the output to a
file) is optional.
The -v and -q args are mutually exclusive, meaning that its either one or the other,
never both.
'''
import argparse

def fib(number):
    '''Calculates the given fibonacci number'''
    a_num, b_num = 0, 1
    for _ in range(number):
        a_num, b_num = b_num, a_num + b_num
    return a_num

def main():
    '''The main function'''
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("num",
                        help="The fibonacci number you wish to calculate",
                        type=int)
    parser.add_argument("-o", "--output",
                        help="Output resoult to a file.",
                        action="store_true")

    args = parser.parse_args()

    result = fib(args.num)

    if args.verbose:
        print(f"The {args.num}th fib number is {result}")
    elif args.quiet:
        print(result)
    else:
        print(f"Fib({args.num}) = {result}")

    if args.output:
        file = open("fibonacci.txt", "a")
        file.write(str(result) + '\n')

if __name__ == '__main__':
    main()
