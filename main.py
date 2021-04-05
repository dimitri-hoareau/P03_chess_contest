class Tournament:
    
    def __init__(self, name, place, date, turn, match_round, player, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.turn = 4
        self.match_round = match_round
        self.player = player
        self.time_control = time_control
        self.description = description


class Player:
    def __init__(self, first_name, last_name, birthday, sex, rank): 
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.rank = rank


class MatchRound:
    pass


class Match:
    pass


def main():
    # player = Player()
    match_round = MatchRound()
    match = Match()

    
    def create_player():
        player_args = {}
        player_args["first_name"] = input("Enter player's first name: ")
        player_args["last_name"] = input("Enter player's last name: ")
        player_args["birthday"] = input("Enter player's birthday: ")
        player_args["sex"] = input("Enter player's sex: ")
        player_args["rank"] = input("Enter player's rank: ")
        return Player(player_args["first_name"], player_args["last_name"], player_args["birthday"], player_args["sex"], player_args["rank"] )

    # test2 = create_player()
    # print(test2.first_name)

    def create_tournament():
        turn = 4
        tournament_args = {}
        tournament_args["name"] = input("Enter tournament's name: ")
        tournament_args["place"] = input("Enter tournament's place: ")
        tournament_args["date"] = input("Enter tournament's date: ")
        tournament_args["time_control"] = input("Enter tournament's time_control: ")
        tournament_args["description"] = input("Enter tournament's description: ")
        # for ...
        player = create_player()

        return Tournament(tournament_args["name"], tournament_args["place"], tournament_args["date"], turn, match_round, player, tournament_args["time_control"], tournament_args["description"] )

    test = create_tournament()
    print(test.name)
    print(test.player.rank)


main()



