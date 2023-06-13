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
         output = "{:10} --- {:10}".format(L[i][0], L[i][1])
         print(output)


def main():
    fruit_bowl_list = [
        ["apples", 6],
        ["pears", 8]
    ]

    menu = """
    R: Review fruit
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
            print("Thank you for your time!")
            run = False

main()




