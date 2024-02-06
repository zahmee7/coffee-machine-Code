MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 100,
    "coffee": 100,
    "Money": 0,
}
def money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    quarters = quarters * 0.25

    dimes = int(input("how many dimes?: "))
    dimes = dimes * 0.10

    nickles = int(input("how many nickles?: "))
    nickles = nickles * 0.05

    pennies = int(input("how many pennies?: "))
    pennies = pennies * 0.01
    money2 = float(quarters + dimes + nickles + pennies)
    money2 = format(money2 ,".3f")
    return money2
caffe_on = True
while caffe_on == True:
    order = input("What would you like? (espresso/latte/cappuccino): ".lower())
    if order not in MENU:
        if order == 'report':
            for key, value in resources.items():
                print(f"{key}: {value}")
        elif order == 'off':
            caffe_on = False
    if order in MENU:
        ingredient=MENU[order]["ingredients"]
        cost = MENU[order]["cost"]
        cost = float(cost)
        add_money = float(money())
        if add_money >= cost:
            add_money -= cost
            resources["Money"] += cost
            for key in resources:
                if key in ingredient:
                    if resources[key]>=ingredient[key]:
                        resources[key] -= ingredient[key]
                        print(f"Here is ${add_money} in change.")
                        print(f"Here is your {order} ☕️. Enjoy!")
                    else:
                        lower_re = resources[key]<ingredient[key]
                        lower_re = key
                        print(f"Sorry there is not enough {lower_re} ")
                        break
        else:
            print("Sorry that's not enough money. Money refunded.")
