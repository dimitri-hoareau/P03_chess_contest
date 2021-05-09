from tinydb import Query

class Player:
    def __init__(self, first_name,rank,id):
        self.id = "" 
        self.first_name = ""
        self.last_name = ""
        self.birthday = ""
        self.sex = ""
        self.rank = 0
        self.score = 0  
        self.players_played = []

    def create(self,player, first_name, rank, players_table):
        serialized_player = {
            'first_name': first_name,
            'rank': rank,
        }

        player.id = players_table.insert(serialized_player) 
        players_table.update({'id': player.id}, doc_ids=[player.id])


    # def update_score(self,player_id, player_score, players_table):
    #     print(player_id)
    #     print(player_score)
    #     players_table.update({'score': player_score}, doc_ids=[player_id])


    