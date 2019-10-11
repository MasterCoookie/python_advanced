'''
Templates are used to build a number of strings using, you guessed it,
templates. Variables in templates are preceded with a $ sign.

May be useful for ex. while writing a programme that renames pictures

The placeholder can be specified using {} ex ("The ${place}yard")
'''
from string import Template

class MyTemplate(Template):
    '''The $ can be changed to any character by editing the delimiter property'''
    delimiter = '#'

def main():
    '''The name speaks for itself.'''
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))

    template = MyTemplate("#qty x #item = #price$")
    total = 0
    print("Cart: ")
    for data in cart:
        print(template.substitute(data))
        total += data["price"]
    print("Total: ", total, '$')

if __name__ == '__main__':
    main()
