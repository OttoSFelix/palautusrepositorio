import requests
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']

    def is_finnish(self):
        if self.nationality == 'FIN':
            return True
    
    def total(self):
        return self.goals + self.assists

    
    def __str__(self):
        return (f'{self.name}  {self.team}  {self.goals} + {self.assists} = {self.goals + self.assists}')
    
class PlayerReader:
    def __init__(self, url):
        self.url = url
        response = requests.get(url).json()


        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            
            self.players.append(player)
    def return_players(self):
        return self.players



class PlayerStats:
    def __init__(self, reader=PlayerReader):
        self.reader = reader
        

    def total(self, player):
        return player.goals + player.assists
    
    def top_scorers_by_nationality(self, nat):
        lista = []
        for player in self.reader.return_players():
            if player.nationality == nat:
                lista.append(player)
    

        lista.sort(key=self.total, reverse=True)
        return lista
                
        

