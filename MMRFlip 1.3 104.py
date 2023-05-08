import json
import socket
import random
import time

## Obtain friend from the after-life ##
print("In Memory of an Exceptional Student and Programmer; ")
print("Welcome to MMRFlip Version 1.3")
data = {}
turn_counter = 0

    ## DEFINE PLAYERS ##

class Player:
    def __init__(self, name, rating, saved_data=None):
        self.name = name
        self.rating = rating

        if saved_data:
            self.games_won = saved_data['games_won']
            self.games_lost = saved_data['games_lost']
        else:
            self.games_won = 0
            self.games_lost = 0

    def get_rank(self):
        return get_rank(self.rating)

    def update_results(self, result):
        if result == 1:
            self.games_won += 1
        else:
            self.games_lost += 1

    def win_ratio(self):
        total_games = self.games_won + self.games_lost
        return self.games_won / total_games if total_games > 0 else 0

    def display_hud(self, opponent):
            # Print separator line
        print("-" * 60)
        print(f"{self.name}'s HUD:")
        print(f"MMR: {self.rating:.2f}")
        print(f"Games Won: {self.games_won}")
        print(f"Games Lost: {self.games_lost}")
        print(f"Win Ratio: {self.win_ratio():.2%}")
        print(f"Opponent MMR: {opponent.rating:.2f}")

        ## CUSTOM PLAYER NAMES

    def create_players(file_name, data):
        while True:
            player1_name = input("Enter a name for Player 1: ").strip()
            player2_name = input("Enter a name for Player 2: ").strip()

            if player1_name.lower() == player2_name.lower():
                print("Error: Both players cannot have the same name. Please enter different names.")
                continue

            saved_data_player1 = data.get(player1_name, None)
            saved_data_player2 = data.get(player2_name, None)

            player1 = Player(player1_name, 1200, saved_data=saved_data_player1)
            player2 = Player(player2_name, 1200, saved_data=saved_data_player2)

            return player1, player2

    # ELO

def get_rank(rating):
    if rating >= 0 and rating < 100:
        return 'Iron 1'
    elif rating >= 100 and rating < 200:
        return 'Iron 2'
    elif rating >= 200 and rating < 300:
        return 'Iron 3'
    elif rating >= 300 and rating < 400:
        return 'Bronze 1'
    elif rating >= 400 and rating < 500:
        return 'Bronze 2'
    elif rating >= 500 and rating < 600:
        return 'Bronze 3'
    elif rating >= 600 and rating < 700:
        return 'Silver 1'
    elif rating >= 700 and rating < 800:
        return 'Silver 2'
    elif rating >= 800 and rating < 900:
        return 'Silver 3'
    elif rating >= 900 and rating < 1000:
        return 'Gold 1'
    elif rating >= 1000 and rating < 1100:
        return 'Gold 2'
    elif rating >= 1100 and rating < 1200:
        return 'Gold 3'
    elif rating >= 1200 and rating < 1300:
        return 'Platinum 1'
    elif rating >= 1300 and rating < 1400:
        return 'Platinum 2'
    elif rating >= 1400 and rating < 1500:
        return 'Platinum 3'
    elif rating >= 1500 and rating < 1600:
        return 'Diamond 1'
    elif rating >= 1600 and rating < 1700:
        return 'Diamond 2'
    elif rating >= 1700 and rating < 1800:
        return 'Diamond 3'
    elif rating >= 1800 and rating < 1900:
        return 'Ascendant'
    elif rating >= 1900 and rating < 2000:
        return 'Immortal'
    elif rating >= 2000 and rating < 2400:
        return 'Radiant'
    else:
        return 'Invalid MMR'

 ## Update elo
def update_elo(player1, player2, result, k=128):
    expected1 = 1 / (1 + 10 ** ((player2.rating - player1.rating) / 400))
    expected2 = 1 / (1 + 10 ** ((player1.rating - player2.rating) / 400))

    new_player1_rating = player1.rating + k * (result - expected1)
    new_player2_rating = player2.rating + k * ((1 - result) - expected2)

    return new_player1_rating, new_player2_rating

    # RUN SERVER

def create_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    return server_socket

def connect_to_server(server_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    return client_socket

    # SAVE/LOAD

def load_game_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_game_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

  ## GAME LOGIC (LOGICAL) LOGICNESS

def get_command(player_name):
    return input(f"{player_name}, enter a command (flip, simulate, tier, hud, reset, quit): ").strip().lower()

 ## HIDDEN

def simulate_flips(player1_choice, player2_choice, num_flips):
    results = [play_game(player1_choice, player2_choice) for _ in range(num_flips)]
    return sum(r[0] for r in results), sum(r[1] for r in results)

  ## GAME LOOP GAME LOOP (BREKABLE)

def coin_flip():
    return random.choice(["Heads", "Tails"])

def player_data(player):
    return {"rating": player.rating, "games_won": player.games_won, "games_lost": player.games_lost}

def play_game(player1_choice, player2_choice, turn):
    flip_result = coin_flip()
    if player1_choice == player2_choice:
        return 0.5, 0.5
    if (player1_choice == flip_result) == (turn % 2 == 0):
        return 1, 0
    return 0, 1

    if player1.name in data:
        player1.__dict__.update(data[player1.name])
    if player2.name in data:
        player2.__dict__.update(data[player2.name])

 ## EVEN MORE LOGICAL BULLSHIT - GREAT
 ## Return CMD commands

def main_game_loop(player1, player2, file_name, data):
    data = load_game_data(file_name)
    if player1.name in data:
        player1_info = data[player1.name]
        player1.rating = player1_info['rating']
        player1.games_won = player1_info['games_won']
        player1.games_lost = player1_info['games_lost']

    if player2.name in data:
        player2_info = data[player2.name]
        player2.rating = player2_info['rating']
        player2.games_won = player2_info['games_won']
        player2.games_lost = player2_info['games_lost']

    while True:
        cmd = get_command(player1.name)

        if cmd == "quit":
            print("Thanks for playing!")
            break
            # Print separator line
            print("-" * 60)

        if cmd == "flip":
            # Print separator line
            print("-" * 60)
            if turn_counter % 2 == 1:
                player1_choice, player2_choice = "Heads", "Tails"
            else:
                player1_choice, player2_choice = "Tails", "Heads"

            player1_result, player2_result = play_game(player1_choice, player2_choice, turn_counter)
            player1.update_results(player1_result)
            player2.update_results(player2_result)
            old_rating1, old_rating2 = player1.rating, player2.rating
            new_ratings = update_elo(player1, player2, player1_result)
            player1.rating = new_ratings[0]
            player2.rating = new_ratings[1]
            mmr_gain1, mmr_gain2 = player1.rating - old_rating1, player2.rating - old_rating2
            print(
                f"{player1.name}'s Result: {'Won' if player1_result else 'Lost'}, MMR Change: {mmr_gain1:+.2f}")
            print(
                f"{player2.name}'s Result: {'Won' if player2_result else 'Lost'}, MMR Change: {mmr_gain2:+.2f}")

            # Print separator line
            print("-" * 60)

            # Save the updated data after the game
            data[player1.name] = player_data(player1)
            data[player2.name] = player_data(player2)
            save_game_data(file_name, data)

        elif cmd == "hud":
            player1.display_hud(player2)
            player2.display_hud(player1)
            # Print separator line
            print("-" * 60)
            print(f"{player1.name}'s MMR: {player1.rating:.2f}, {player2.name}'s MMR: {player2.rating:.2f}")
            # Print separator line
            print("-" * 60)

        elif cmd == "tier":
            player1_rank = player1.get_rank()
            player2_rank = player2.get_rank()
            # Print separator line
            print("-" * 60)
            print(f"{player1.name}'s Tier: {player1_rank} ({player1.rating:.2f})")
            print(f"{player2.name}'s Tier: {player2_rank} ({player2.rating:.2f})")
            # Print separator line
            print("-" * 60)

        elif cmd == "reset":
            player1.rating = 1200
            player1.games_won = 0
            player1.games_lost = 0
            player2.rating = 1200
            player2.games_won = 0
            player2.games_lost = 0
            print(f"{player1.name} and {player2.name} MMR and stats have been reset.")
            # Print separator line
            print("-" * 60)

        elif cmd == "quit":
            return False
            # Print separator line
            print("-" * 60)

        elif cmd == "flip" or cmd == "simulate":
            if cmd == "simulate":
                num_simulations = int(input("Enter the number of games to simulate: "))
            else:
                num_simulations = 1

            for _ in range(num_simulations):
                if turn_counter % 2 == 1:
                    player1_choice, player2_choice = "Heads", "Tails"
                else:
                    player1_choice, player2_choice = "Tails", "Heads"

                player1_result, player2_result = play_game(player1_choice, player2_choice, turn_counter)
                player1.update_results(player1_result)
                player2.update_results(player2_result)
                old_rating1, old_rating2 = player1.rating, player2.rating
                new_ratings = update_elo(player1, player2, player1_result)
                player1.rating = new_ratings[0]
                player2.rating = new_ratings[1]
                mmr_gain1, mmr_gain2 = player1.rating - old_rating1, player2.rating - old_rating2
                print(
                    f"{player1.name}'s Result: {'Won' if player1_result else 'Lost'}, MMR Change: {mmr_gain1:+.2f}")
                print(
                    f"{player2.name}'s Result: {'Won' if player2_result else 'Lost'}, MMR Change: {mmr_gain2:+.2f}")

                # Print separator line
                print("-" * 60)

        ## Version

        elif cmd == "ver":
            # Print separator line
            print("-" * 60)
            print("Version: 1.3 104")
            # Print separator line
            print("-" * 60)

        # Add more commands here as needed
def menu():
    while True:
        print("1. Local Game")
        print("2. Host Game")
        print("3. Join Game")
        print("4. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            file_name = "game_data.json"
            data = load_game_data(file_name)
            player1, player2 = Player.create_players(file_name, data)

            try:
                main_game_loop(player1, player2, file_name, data)
            except KeyboardInterrupt:
                print("\nThanks for playing!")

        elif choice == '2':
            print("Hosting a game is not yet supported. Please try another option.")
            continue

        elif choice == '3':
            print("Joining a game is not yet supported. Please try another option.")
            continue

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
# file_name save/load
# Load data from file_name
file_name = "game_data.json"
data = load_game_data(file_name)
# Call create_players function to define player1 and player2
player1, player2 = Player.create_players(file_name, data)

try:
    main_game_loop(player1, player2, file_name, data)
except KeyboardInterrupt:
    print("\nThanks for playing!")

    ### END ###
