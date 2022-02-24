
import pandas as pd


inventory =[{'product':'bakawadi', 'price': 20, 'brand': 'haldiraam'},
{'product':'chips', 'price': 40, 'brand': 'balaji'},
{'product':'potato chivda', 'price': 30, 'brand': 'parle'},
{'product':'punjabi tadka', 'price': 60, 'brand': 'britania'},
{'product':'chitos', 'price': 10, 'brand': 'nestle'}]

inventory = pd.DataFrame(inventory)

# function to find number of coins to return to customers
def check(num):
    ll = []
    change = num
    coins = [5,2,1, 0.5, 0.2, 0.1]
    while change>0:
        for i in coins:
            if change//i >0:
                no_of_coins = change//i
                change = change%i
                ll.append([i]*no_of_coins)
    return [final for sublist in ll for final in sublist]

#   displaying inventory
list_products = inventory['product'].tolist()
print(list_products)
# input from customers
selection = input('Select Product : ')
money = int(input("Deposite Money "))

cost = inventory[inventory['product'] == selection]['price'].values[0]
change = int(money - inventory[inventory['product'] == selection]['price'])


# condition1
if selection not in list_products:
    print('ERROR....Wrong Product Name.....  >> RESTART')
# condition 2
elif money < cost:
    print('enter more money >> RESTART')
# else condition
else:
    print('You selected : ', selection)
    print('You paid : ', money)
    print('Your change : ', change)
    print('Collect Coins : ', check(change))
