import random
import requests
def random_planets ():
    planet_number = random.randint(1, 60)
    url = f'https://swapi.dev/api/planets/{planet_number}/'
    response = requests.get(url)
    planet = response.json()

    if planet['diameter'] == 'unknown':
        planet['diameter'] = 0  # sometimes API returns 'unknown' - unknown always loses/scores 0

    if planet['population'] == 'unknown':
        planet['population'] = 0

    if planet['orbital_period'] == 'unknown':
        planet['orbital_period'] = 0

    return {
    'name': planet['name'].title(),
    'diameter': int(planet['diameter']), #cast to int as API always produces string
    'population': int(planet['population']),
    'orbital period': int(planet['orbital_period']),
    }

def play_game():
    def run():
        my_score = 0
        opponent_score = 0

        for rounds in range(1, 4):
            print(f'Round {rounds}\n')

            my_planet = random_planets()
            print(f"You were given {(my_planet['name'])}")

            # print(my_planet['diameter']) #to check unknown is being converted to 0
            # print(my_planet['population'])
            # print(my_planet['orbital period'])

            print(f"Diameter: {(my_planet['diameter'])}")
            print(f"Population: {(my_planet['population'])}")
            print(f"Orbital period: {(my_planet['orbital period'])}\n")

            stat_choice = input('Which stat do you want to use? (diameter, population, orbital period) ')

            if stat_choice == 'diameter':
                print(f"Diameter: {(my_planet['diameter'])}")
            elif stat_choice == 'population':
                print(f"Population: {(my_planet['population'])}")
            elif stat_choice == 'orbital period':
                print(f"Orbital period: {(my_planet['orbital period'])}")

            opponent_planet = random_planets()
            print(f"\nYour opponent was given {(opponent_planet['name'])}")

            if stat_choice == 'diameter':
                print(f"Diameter: {(opponent_planet['diameter'])}")
            elif stat_choice == 'population':
                print(f"Population: {(opponent_planet['population'])}")
            elif stat_choice == 'orbital period':
                print(f"Orbital Period: {(opponent_planet['orbital period'])}")

            my_stat = my_planet[stat_choice]
            opponent_stat = opponent_planet[stat_choice]

            if my_stat > opponent_stat:
                my_score = my_score + 1
                opponent_score = opponent_score + 0
                print('\nYou win the round!\n')

            elif my_stat < opponent_stat:
                my_score = my_score + 0
                opponent_score = opponent_score + 1
                print('\nYou lose the round!\n')

            else:
                print('\nDraw!\n')
                my_score = my_score + 0
                opponent_score = opponent_score + 0

        print('--------------------\nEnd of Game\n--------------------\n')

        print(f'Your Final Score: {my_score}')
        print(f"Your Opponent's Final Score: {opponent_score}\n")

        if my_score > opponent_score:
            print('You win the game!\n')
        elif my_score < opponent_score:
            print('Your opponent wins the game!\n')
        else:
            print('The game was a draw\n')
        
    run()

play_game()

play_again = input('Want to play again? (yes/no)')
if play_again == 'yes':
    play_game()
else:
    exit


