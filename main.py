counter = 0
left_available = False
right_available = True


def default_screen():
    print(
        """
        ****************************
        ****************************

        ( ͡° ͜ʖ ͡°)

        ****************************
        ****************************
    """)


def one_right_screen():
    print(
        """
        ****************************
        ****************************

                ( ͡° ͜ʖ ͡°)

        ****************************
        ****************************
    """)


def two_right_screen():
    print(
        """
        ****************************
        ****************************

                        ( ͡° ͜ʖ ͡°)

        ****************************
        ****************************
    """)


def three_right_screen():
    print(
        """
        ****************************
        ****************************

                            ( ͡° ͜ʖ ͡°)

        ****************************
        ****************************
    """)


def stuck_in_woods_screen():
    print(
        """
        ****************************
        ***************        *****

                    (╯⏒◞ ⏒）╯︵ ┻━┻

        ****************************
        ****************************
    """)


def instructions():
    global counter
    global left_available
    global right_available
    input_amount = 0
    while input_amount < 8:
        user_input = input('Where you want to go? (right or left): ')
        input_amount += 1
        if user_input == 'right' and counter == 0:
            counter += 1
            one_right_screen()
        elif user_input == 'right' and counter == 1:
            counter += 1
            two_right_screen()
        elif user_input == 'right' and counter == 2:
            counter += 1
            three_right_screen()
        elif user_input == 'left':
            print('Can\'t go left')
        else:
            stuck_in_woods_screen()
    print('You must be upset :))')

def play_game():
    default_screen()
    instructions()


play_game()
