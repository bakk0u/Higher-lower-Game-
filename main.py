    from art import logo, vs
    from game_data import data
    import random
    import os
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    user_choice = ""
    def select_opponent():
        global data
        first_data = data[random.randint(0, 49)]
        second_data = data[random.randint(0, 49)]
        return first_data, second_data
    def compare(opponent1 , opponent2):
        if opponent1["follower_count"] > opponent2["follower_count"]:
            return 'A'
        elif opponent1["follower_count"] < opponent2["follower_count"]:
            return 'B'
    def start_game():
        global user_choice
        global A, B
        global correct
        global score
        A, B = select_opponent()
        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
        print(vs)
        print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        if user_choice == compare(A, B):
            clear()
            score += 1
            print(logo)
            print(f"You are right! Current score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            correct = False
    correct = True
    print(logo)
    start_game()
    while correct:
        start_game()
