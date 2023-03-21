# Favorite Pokemon Stats

This Flask web application retrieves and displays information about 5 favorite Pokemon using data from the PokeAPI (https://pokeapi.co/). The application fetches the following details for each Pokemon:
```
Name
Height
Weight
Color
2 random moves
Base happiness
```
Additionally, the application calculates the average, mean, and median base happiness for the selected Pokemon.
## Installation
Follow these steps to set up the application:
Clone the repository
```
git clone https://github.com/MitaliSengupta/pokemon-stats-api.git
cd pokemon-stats-api
```
Create and activate a virtual environment:
On Linux and MacOS:
```
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```
python -m venv venv
venv\Scripts\activate
```
Install the required Python packages:
```
pip install -r requirements.txt
```
## Usage
To run the application, execute the following command:
```
flask run
```
The application will be accessible at http://localhost:5000/
## Customize
To customize the favorite pokemon list, modify the favorite_pokemon list in the flask application file:
```
favorite_pokemon = ['pikachu', 'charmander', 'bulbasaur', 'squirtle', 'mew']
```
Replace the existing Pokemon names with your preferred choices, and the application will fetch and display data for the updated list.
