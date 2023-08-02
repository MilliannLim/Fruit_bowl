def get_string(m):
    user_input = input(m).strip()
    return user_input

def get_option(m):
    user_input = input(m).strip().upper()
    return user_input

def get_integer(m):
    user_input = int(input(m))
    return user_input

def review_fruit(L):
     for i in range(0, len(L)):
         output = "{:<3} : {:10} --- {:10}".format(i,L[i][0], L[i][1])
         print(output)


def add_new_fruit(L):
    fruit = get_string("What new fruit would you like to add?")
    amount = get_integer("How many would you like to add?")
    new_list = [fruit, amount]
    L.append(new_list)

def add_amount(L):
    review_fruit(L)
    index_num = get_integer("Please choose fruit option number")
    fruit = L[index_num]
    print(fruit)
    amount = get_integer("How many would you like to add?")
    fruit[1] += amount
    print(fruit)

def eat_amount(L):
    review_fruit(L)
    index_num = get_integer("Please choose fruit option number")
    fruit = L[index_num]
    print(fruit)
    amount = get_integer("How many would you like to eat?")
    fruit[1] -= amount
    print(fruit)


def main():
    fruit_bowl_list = [
        ["apples", 6],
        ["pears", 8]
    ]

    menu = """
    R: Review fruit
    N: Add new fruit
    A: Add more fruit
    E: Eat fruit
    Q: Quit
    """
    run = True
    while run is True:
        print(menu)
        choice = get_option("Please select your option: ->")
        print("." * 100)
        if choice == "R":
            review_fruit(fruit_bowl_list)
        if choice == "Q":
            print("Thank you for eating fruit from my fruitbowl!")
            run = False
        if choice == "N":
            add_new_fruit(fruit_bowl_list)
        if choice == "A":
            add_amount(fruit_bowl_list)
        if choice == "E":
            eat_amount(fruit_bowl_list)

main()




