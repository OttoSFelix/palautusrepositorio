class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score, self.player2_score = self.add_score(self.player1_score, player_name, self.player2_score)
        else:
            self.player2_score, self.player1_score = self.add_score(self.player2_score, player_name, self.player1_score)

    def add_score(self, player_score, player_name, opponent_score):
        if player_score == 'A':
            player_score = 'W'
            opponent_score = 'L'
        elif player_score == 'D':
            player_score = 'A'
            opponent_score = -1
        elif player_score < 3 and player_score != -1:
            player_score += 1
        elif player_score == -1:
            player_score = 'D'
            opponent_score = 'D'
        else:
            if player_score == opponent_score:
                player_score = 'A'
                opponent_score = -1
            else:
                player_score = 'W'
                opponent_score = 'L'
        return (player_score, opponent_score)

    def get_score(self):
        score = ""
        temp_score = 0

        scorebook = {
            (0, 0): "Love-All",
            (1, 1): "Fifteen-All",
            (2, 2): "Thirty-All",
            (3, 3): "Deuce",
            (1, 0): "Fifteen-Love",
            (0, 1): "Love-Fifteen",
            (2, 0): "Thirty-Love",
            (0, 2): "Love-Thirty",
            (3, 0): "Forty-Love",
            (0, 3): "Love-Forty",
            (2, 1): "Thirty-Fifteen",
            (1, 2): "Fifteen-Thirty",
            (3, 1): "Forty-Fifteen",
            (1, 3): "Fifteen-Forty",
            (3, 2): "Forty-Thirty",
            (2, 3): "Thirty-Forty",
            ('A',-1): 'Advantage player1',
            (-1,'A'): 'Advantage player2',
            ('D','D'): 'Deuce',
            ('W','L'): 'Win for player1',
            ('L','W'): 'Win for player2' 

        }


        score = scorebook[(self.player1_score, self.player2_score)]
        return score
