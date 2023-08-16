import random



play_game = True

while play_game:
    blackjack_continue = input("Do you want to play a game of blackjack. Type 'y' or 'n'. ")
    if blackjack_continue == 'n':
        break
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_cards = []
    computer_cards.append(computer_card1)
    computer_cards.append(computer_card2)

    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_cards = []
    user_cards.append(user_card1)
    user_cards.append(user_card2)

    sum_user = sum(user_cards)
    sum_computer = sum(computer_cards)
    get_cards = True

    if sum_computer == 21:
        print(f"Your final hand: {user_cards}, final score: {sum_user}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum_computer}")
        print("You lose")
        get_cards = False

    if sum_user == 21:
        print(f"Your final hand: {user_cards}, final score: {sum_user}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum_computer}")
        print("You Win")
        get_cards = False

    if sum_computer == 21 and sum_user == 21:
        print(f"Your final hand: {user_cards}, final score: {sum_user}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum_computer}")
        print("You lose")
        get_cards = False

    if 11 in user_cards and sum_user > 21:
        user_cards.remove(11)
        user_cards.append(1)
        sum_user = sum(user_cards)
    if 11 in computer_cards and sum_computer > 21:
        computer_cards.remove(11)
        computer_cards.append(1)
        sum_computer = sum(computer_cards)

    print(f"Computer first card: {computer_cards[0]}")
    print(f"User cards: {user_cards}, current score: {sum_user}")
    sum_user2 = sum_user

    while get_cards:
        should_continue = input("Type 'y' to get another card, type 'n' to pass. ").lower()

        if should_continue == 'n':
            break
        user_card3 = random.choice(cards)
        user_cards.append(user_card3)
        sum_user2 = sum(user_cards)
        if 11 in user_cards and sum_user2 > 21:
            user_cards.remove(11)
            user_cards.append(1)
            sum_user2 = sum(user_cards)
        print(f"Computer first card: {computer_cards[0]}")
        print(f"User cards: {user_cards}, current score: {sum_user2}")

        if sum_user2 > 21:
            print("You went over. You lose.")
            break
        if sum_user2 == 21:
            print("You got a blackjack. You win.")
            break

    if sum_user2 < 21:
        while get_cards:
            if sum_computer < 17:
                computer_card3 = random.choice(cards)
                computer_cards.append(computer_card3)
                sum_computer2 = sum(computer_cards)
            else:
                sum_computer2 = sum_computer
            if 11 in computer_cards and sum_computer > 21:
                computer_cards.remove(11)
                computer_cards.append(1)
                sum_computer = sum(computer_cards)
            if sum_computer2 >= 17:
                break
        if sum_computer2 > 21:
            print(f"Your final hand: {user_cards}, final score: {sum_user2}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer2}")
            print("The computer went over. You win.")
        elif sum_computer2 == 21:
            print(f"Your final hand: {user_cards}, final score: {sum_user2}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer2}")
            print("the computer got a blackjack. You lose.")
        elif sum_computer2 > sum_user2:
            print(f"Your final hand: {user_cards}, final score: {sum_user2}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer2}")
            print("You lose")
        elif sum_computer2 == sum_user2:
            print(f"Your final hand: {user_cards}, final score: {sum_user2}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer2}")
            print("It's a tie")
        elif sum_computer2 < sum_user2:
            print(f"Your final hand: {user_cards}, final score: {sum_user2}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer2}")
            print("You win")
