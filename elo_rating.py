class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        self.match_history = []

    def record_match(self, opponent_name, outcome, new_elo):
        self.match_history.append((opponent_name, outcome))
        self.elo = new_elo


class Elo:
    def __init__(self, k_factor=32):
        self.players = {}
        self.k_factor = k_factor

    # Add a player to the system, if you want to add two people with the same name, either add a number to the end of the name or use IDs instead of names for the players
    def add_player(self, name, elo=1500):
        if name not in self.players:
            self.players[name] = Player(name, elo)
        else:
            raise ValueError("A player with this name already exists in the system.")

    def record_match(self, name1, name2, outcome):
        # Get player objects
        player1 = self.players[name1]
        player2 = self.players[name2]

        # Update Elos
        new_elo1, new_elo2 = calculate_new_elos(player1.elo, player2.elo, outcome, self.k_factor)

        # Record match in players' match history
        player1.record_match(name2, outcome, new_elo1)
        player2.record_match(name1, outcome, new_elo2)
        
        return new_elo1, new_elo2



def calculate_new_elos(elo1, elo2, outcome, k_factor=32):
    # Calculate expected outcomes
    expected_outcome1 = 1 / (1 + 10**((elo2 - elo1) / 400))
    expected_outcome2 = 1 - expected_outcome1

    # Get actual outcomes
    if outcome == 1:    # player1 wins
        actual_outcome1 = 1
        actual_outcome2 = 0
    elif outcome == 2:  # player2 wins
        actual_outcome1 = 0
        actual_outcome2 = 1
    else:               # draw
        actual_outcome1 = 0.5
        actual_outcome2 = 0.5

    # Update Elos
    new_elo1 = elo1 + k_factor * (actual_outcome1 - expected_outcome1)
    new_elo2 = elo2 + k_factor * (actual_outcome2 - expected_outcome2)

    return new_elo1, new_elo2
