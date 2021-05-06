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

    def create(self, first_name, rank, id, players_table):
        serialized_player = {
            'first_name': first_name,
            'rank': rank,
            'id': id
        }
        players_table.insert(serialized_player)
