# Elo
Python Elo Ranking System

API:

calculate_new_elos
Calculates the new Elo ratings for two players after a match. This will be the method 

new_elo1, new_elo2 = calculate_new_elos(1500, 1500, 1)


Player
A player in an Elo system.

__init__(self, name: str, elo: int)
Creates a new player with a given name and Elo rating.

player = Player("Alice", 1500)

record_match(self, opponent_name: str, outcome: str, new_elo: int)
Records a match for the player against an opponent, specifying the outcome and updating the Elo rating.

player.record_match("Bob", "Alice", 1520)

Elo
The Elo rating system.

__init__(self, k_factor: int = 32)
Creates a new Elo system with a specified K-factor.

add_player(self, name: str, elo: int = 1500)
Adds a new player to the Elo system with a specified name and initial Elo rating.

elo.add_player("Alice", 1500)

record_match(self, name1: str, name2: str, outcome: str)
Records a match between two players in the Elo system and updates their Elo ratings.

elo.record_match("Alice", "Bob", "Alice")
