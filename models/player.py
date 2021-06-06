class Player:
    def __init__(self, first_name, last_name, birthday, sex, rank, id):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.birthday = ""
        self.sex = ""
        self.rank = 0
        self.score = 0
        self.players_played = []

    def create(self, player, first_name, last_name, birthday, sex, rank, players_table):
        serialized_player = {
            'first_name': first_name,
            'last_name': last_name,
            'birthday': birthday,
            'sex': sex,
            'rank': int(rank),
            'score': 0,
            'players_played': [],
        }

        player.id = players_table.insert(serialized_player)
        players_table.update({'id': player.id}, doc_ids=[player.id])
