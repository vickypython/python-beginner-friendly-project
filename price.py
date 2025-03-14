def calculate_discount(price,discount_percent):
    print('Enter the price of the item')
    price=float(input('>'))
    print('Enter the discount rate')
    discount_percent=float(input('>'))
    if discount_percent>=20:
        discount=price*discount_percent/100
        print('You have a discount of',discount)
        print('You will pay',price-discount)
    else:
        return price
calculate_discount(100,20)