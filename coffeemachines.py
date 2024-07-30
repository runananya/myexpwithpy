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
     "milk": 200,
    "coffee": 100,
}
is_on=True
def costest(qua,dimes,nickel,pennies):
    quater=0.25
    dime=0.10
    nick=.05
    pen=0.01
    total=qua*quater+dimes*dime+nick*nickel+pennies*pen
    return total
def check_res(user):
    wat=MENU[user]["ingredients"]["water"]
    mil=MENU[user]["ingredients"]["milk"]
    cof=MENU[user]["ingredients"]["coffee"]
    if wat<=resources["water"] and mil<=resources["milk"] and cof<=resources["coffee"]:
        print("Order processing")
        resources["water"]=resources["water"]-wat
        resources["milk"]=resources["milk"]-mil
        resources["coffee"]=resources["coffee"]-cof
        print(resources)
    else:
        print("Can't process order!")
    
while is_on:    
    user=input("What would you like to order : espresso , latte , cappuccino")
    if user=="off":
        is_on=False
    check_res(user)
    if user=="report":
        print(resources)

    order=MENU[user]["cost"]
    print(f"please pay : {order}")
    print("Quantify the coins:")
    qua=int(input("quater: "))
    dimes=int(input("dimes: "))
    nickel=int(input("nickels: "))
    pennies=int(input("pennies: "))
    costs=costest(qua,dimes,nickel,pennies)
    if costs==order:
        print("Thank you for your purchase!")
    elif costs>order:
        change=costs-order
        print(f"Here's your change {change}")
        print("Thank you for your purchase!")
    else:
        print("Insuffient funds!")

