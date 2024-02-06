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
profit = 0
resources = {
    "water": 300,
    "milk": 100,
    "coffee": 100,
}
def is_resource_enough (ingredients):
    for key in ingredients:
        if ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key} ")
            return False
    return True


def add_money():
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


def get_piad(money_recive , drink_cost):
    if money_recive >= drink_cost:
        global profit
        change = round(money_recive - drink_cost , 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_caffe(drink_name, ingredients):
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

turn_on = True
while turn_on ==True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice =="off":
        turn_on = False
    elif choice =="report":
        print(f"water : {resources['water']}ml" )
        print(f"milk : {resources['milk']}ml" )
        print(f"coffee : {resources['coffee']}g")
        print(f"coffee : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink['ingredients']):
            payment = add_money()
            if get_piad(payment , drink["cost"]):
                make_caffe(choice , drink['ingredients'])


