import operator

class Tournament:
    
    def __init__(self):

        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turn = 4
        self.turn = []
        self.players = []
        self.time_control = ""
        self.description = ""

    # def add_player(self, player_instance):
    #     self.players.append(player_instance)



class Player:

    def __init__(self): 
        self.first_name = ""
        self.last_name = ""
        self.birthday = ""
        self.sex = ""
        self.rank = 0


class Turn:
    
    def __init__(self):
        self.matches = []

 
class Match:
    
    def __init__(self):
        self.player_1 = []
        self.player_2 = []


def main():

    def confirm(action):
        """
        Ask user to enter Y or N (case-insensitive).
        :return: True if the answer is Y.
        :rtype: bool
        """
        answer = ""
        if action == "end_of_turn":
            while answer not in ["y"]:
                answer = input("Is the turn completed? [Y/N] ").lower()
        else:
            while answer not in ["y"]:
                answer = input("Do you want to start a new turn? [Y/N] ").lower()

        return answer == "y"


    def create_player():
        player = Player()
        player.first_name = input("Enter player's first name: ")
        # player.last_name = input("Enter player's last name: ")
        # player.birthday = input("Enter player's birthday: ")
        # player.sex = input("Enter player's sex: ")
        player.rank = input("Enter player's rank: ")
        return player

    def create_tournament():
        tournament = Tournament()

        # tournament.name =  input("Enter tournament's name: ")
        # tournament.place = input("Enter tournament's place: ")
        # tournament.date = input("Enter tournament's date: ")
        # tournament.time_control = input("Enter tournament's time_control: ")
        # tournament.description = input("Enter tournament's description: ")

        for index in range(4):
            player_instance = create_player()
            tournament.players.append(player_instance)

        return tournament


    def create_match(player_1, player_2):
        match = Match()

        match.player_1.append(player_1)
        match.player_2.append(player_2)

        return match


    def create_turn():
        tournament_instance = create_tournament()

        def first_turn():
            turn = Turn()
            sorted_players_by_rank = sorted(tournament_instance.players, key=operator.attrgetter('rank'))
            total_players = len(sorted_players_by_rank)
            mediane =round(len(sorted_players_by_rank)/2)
            best_player = 0
            worst_player = mediane

            for index in range(mediane):
                pair = [sorted_players_by_rank[best_player],sorted_players_by_rank[worst_player]]
                match = create_match(pair[0], pair[1])
                turn.matches.append(match)
                best_player += 1
                worst_player += 1

            confirm("end_of_turn")

            match_number = 0
            for index in range(mediane):
                player_1_name = turn.matches[match_number].player_1[0].first_name
                player_1_score = input("Enter " + player_1_name + "'s score : ")
                turn.matches[match_number].player_1.append(player_1_score)

                player_2_name = turn.matches[match_number].player_2[0].first_name
                player_2_score = input("Enter " + player_2_name + "'s score : ")
                turn.matches[match_number].player_2.append(player_2_score)
                match_number += 1
            
            tournament_instance.turn.append(turn)

        # def after_first_turn():
        #     turn = Turn()
        #     sorted_players_by_score = sorted(tournament_instance.players, key=operator.attrgetter('rank'))

            
            

            
        first_turn()
        confirm("begin_of_turn")
        print(tournament_instance.turn)













    test2 = create_turn()

main()


# my_list = [2,3,4,5]
# print(my_list)
# my_list[0] += 2
# print(my_list)
