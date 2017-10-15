
quantity = int(input('How many shirts in the order?\n> '))
while quantity < 12:
    print("Your quantity is too low. The order minimum is 12 shirts.")
    quantity = int(input('How many shirts in the order?\n> '))

designcolors = int(input('How many colors in the design?\n> '))

while designcolors > 4 and quantity < 24:
    print('Designs for orders of less than 23 shirts must have four colors or less.')
    designcolors = int(input('How many colors in the design?\n> '))
    quantity = int(input('How many shirts in the order?\n> '))
    if quantity < 12:
        print("Your quantity is too low. The order minimum is 12 shirts.")

while designcolors > 5 and quantity < 72:
    print('Designs for orders of more than 24 shirts and less than 72 shirts must have five colors of less.')
    designcolors = int(input('How many colors in the design?\n> '))
    quantity = int(input('How many shirts in the order?\n> '))

while designcolors > 7:
    print('Maximum colors per side is 7.')
    designcolors = int(input('How many colors in the design?\n> '))

def colorcounter(a, b):

    color12 = [0, 2.05, 2.8, 3.55, 4.3]
    color24 = [0, 1.05, 1.25, 1.5, 1.65, 1.75]
    color72 = [0, .92, 1.2, 1.4, 1.55, 1.65, 1.75]
    color144 = [0, .85, 1.06, 1.27, 1.43, 1.55, 1.65]
    color240 = [0., .85, 1, 1.2, 1.37, 1.47, 1.58]

    if 12 <= a <= 23:
        c = color12[b]
    if 24 <= a <= 71:
        c = color24[b]
    if 72 <= a <= 143:
        c = color72[b]
    if 144 <= a <= 239:
        c = color144[b]
    if 240 <= a:
        c = color240[b]
    return c

def margin(a):
    return round(a + a * 0.5, 2)

def tax(a):
    return round(a + a * .07, 2)

price = colorcounter(quantity, designcolors)
price += ((designcolors * 11) / quantity)
        # each color requires a screen which costs $11 each
markup = tax(margin(price))

total = markup * quantity

print('Print price per shirt: $', round(markup, 2))
print('Print price of the order: $', round(total, 2))
