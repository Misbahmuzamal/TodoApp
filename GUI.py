
menu={
    "pizza":300,
    "pasta":600,
    "burger":500,
    "tea":80,
    "icecream":350
}
total_order=0
print("Welcome to Python Resturent App")
print("Pizza=300 \n pasta=600 \n burger=500 \n tea=80\nicecream=350")
while True:
    item1=input("select the food from the menu you want to order:")
    if item1 in menu:
        print(f"{item1} add in your order")
        total_order+=menu[item1]
        add_another=input("can you add more food in your order(yes/no):")
        if add_another == "yes":
            item2=input("select the food")
            print(f"{item2} add in your order")
            total_order += menu[item2]
        elif add_another == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        break
    else:
        print(f"{item1} is not available on menu")

print(f"the bill of your order is {total_order}")
