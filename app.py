import random
import statistics
import requests
from flask import Flask, render_template

app = Flask(__name__)

favorite_pokemon = ['pikachu', 'mew', 'gengar', 'squirtle', 'clefable']


@app.route('/')
def index():
    stats_data = favorite_pokemon_stats()
    return render_template('index.html', **stats_data)


@app.route('/api/v1/favorite-pokemon-stats')
def favorite_pokemon_stats():
    results = []
    base_happiness_list = []
    for pokemon in favorite_pokemon:
        pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
        species_data = requests.get(pokemon_data["species"]["url"]).json()

        move_names = []
        for move in pokemon_data["moves"]:
            move_names.append(move["move"]["name"])
        selected_moves = random.sample(move_names, 2)

        base_happiness = species_data["base_happiness"]
        base_happiness_list.append(base_happiness)

        results.append({
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "moves": selected_moves,
            "color": species_data["color"]["name"],
            "base_happiness": base_happiness
        })

    avg_base_happiness = sum(base_happiness_list) / len(base_happiness_list)
    mean_base_happiness = statistics.mean(base_happiness_list)
    median_base_happiness = statistics.median(base_happiness_list)

    stats_data = {
        "pokemon_data": results,
        "average_base_happiness": avg_base_happiness,
        "mean_base_happiness": mean_base_happiness,
        "median_base_happiness": median_base_happiness
    }
    return stats_data


if __name__ == "__main__":
    app.run()