class Tournament:
    
    def __init__(self, player):

        self.name = ""
        self.place = ""
        self.date = ""
        self.turn = 4
        self.match_round = ""
        self.players = {}
        self.time_control = ""
        self.description = ""

    def create_player(self, player_number, player_instance):
        self.players[player_number] = player_instance


class Player:

    def __init__(self): 
        self.first_name = ""
        self.last_name = ""
        self.birthday = ""
        self.sex = ""
        self.rank = 0


class MatchRound:
    pass


class Match:
    pass


def main():
    player = Player()
    tournament = Tournament(player)
    match_round = MatchRound()
    match = Match()

    def create_player():
        player.first_name = input("Enter player's first name: ")
        player.last_name = input("Enter player's last name: ")
        player.birthday = input("Enter player's birthday: ")
        player.sex = input("Enter player's sex: ")
        player.rank = input("Enter player's rank: ")
        return player

    def create_tournament():

        tournament.name =  input("Enter tournament's name: ")
        tournament.place = input("Enter tournament's place: ")
        tournament.date = input("Enter tournament's date: ")
        tournament.time_control = input("Enter tournament's time_control: ")
        tournament.description = input("Enter tournament's description: ")

        for index in range(2):
            player_number = "player_" + str(index + 1)
            player_instance = create_player()
            print(player_instance)
            tournament.create_player(player_number, player_instance)

        return tournament

    test = create_tournament()
    print(test.players["player_1"].sex)

main()



