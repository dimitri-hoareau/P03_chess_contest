from tinydb import Query
from models.player import Player

class Tournament:
    
    def __init__(self):

        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turn = 4
        self.turns = [] # mettre des id aux tours
        self.players = []
        self.time_control = ""
        self.description = ""

    def get_player_for_tournament(self,player_id, players_table, tournament): 
        PlayerToFind = Query()
        serialized_player = players_table.search(PlayerToFind.id == str(player_id)) #gérer si on entre un mauvais id, message et recommencer (while true ?)
        player_instance = Player(first_name="", rank=0, id="")
        player_instance.first_name = serialized_player[0]['first_name']
        player_instance.rank =serialized_player[0]['rank']
        player_instance.id = serialized_player[0]['id']

        tournament.players.append(player_instance)

    def create(self, name, tournaments_table):
        serialized_tournament = {
            'name': name
            # 'players': tournament.players
            # ou alors juste l'id du player
        }
        tournaments_table.insert(serialized_tournament)