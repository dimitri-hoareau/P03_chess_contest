import operator
from datetime import datetime

class Tournament:
    
    def __init__(self):

        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turn = 4
        self.turns = []
        self.players = []
        self.time_control = ""
        self.description = ""

    # def add_player(self, player_instance):
    #     self.players.append(player_instance)



class Player:
    def __init__(self):
        self.id = "" 
        self.first_name = ""
        self.last_name = ""
        self.birthday = ""
        self.sex = ""
        self.rank = 0
        self.score = 0  #faire une fonction ?
        self.players_played = []


class Turn:
    
    def __init__(self):
        self.name = ""
        self.matches = []
        self.start_date = ""
        self.end_date = ""

 
class Match:
    
    def __init__(self):
        self.player_1 = []
        self.player_2 = []
        self.match = self.player_1, self.player_2, 


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
        # player.id = input("Enter player's id: ")
        return player

    def create_tournament():
        tournament = Tournament()

        # tournament.name =  input("Enter tournament's name: ")
        # tournament.place = input("Enter tournament's place: ")
        # tournament.date = input("Enter tournament's date: ")
        # tournament.time_control = input("Enter tournament's time_control: ")
        # tournament.description = input("Enter tournament's description: ")

        for index in range(6):
            player_instance = create_player()
            tournament.players.append(player_instance)

        for index in range(tournament.number_of_turn):
            print("****************tour ******" + str(index))
            create_turn(tournament)

        def display_report:
            print("list of players")
            for player in tournament.players:
                print(player)
                
            print("list of turns")
            for turn in tournament.turns:
                print(turn.name)

            print("list of matches")
            for match in tournament.turns.matches:
                print(match.player_1[0].first_name, match.player_2[0].first_name )

        return tournament


    def create_match(player_1, player_2):
        match = Match()

        match.player_1.append(player_1)
        match.player_2.append(player_2)

        return match

    def create_turn(tournament):
        sorted_players_by_rank = sorted(tournament.players, key=operator.attrgetter('rank'))

        def first_round():
            turn = Turn()
            turn.name = "Round 1"
            turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            mediane =round(len(sorted_players_by_rank)/2)
            worst_player = mediane

            for index in range(mediane):
                pair = [sorted_players_by_rank[index],sorted_players_by_rank[worst_player]]
                match = create_match(pair[0], pair[1])
                turn.matches.append(match)
                worst_player += 1
                print(pair[0].first_name + " will play against " + pair[1].first_name)

            confirm("end_of_turn")

            for index in range(mediane):
                player_1_name = turn.matches[index].player_1[0].first_name
                player_1_score = input("Enter " + player_1_name + "'s score : ")
                turn.matches[index].player_1[0].score += int(player_1_score)
                turn.matches[index].player_1[0].players_played.append(turn.matches[index].player_2[0])
                turn.matches[index].player_1.append(player_1_score)

                player_2_name = turn.matches[index].player_2[0].first_name
                player_2_score = input("Enter " + player_2_name + "'s score : ")
                turn.matches[index].player_2[0].score += int(player_2_score)
                turn.matches[index].player_2[0].players_played.append(turn.matches[index].player_1[0])
                turn.matches[index].player_2.append(player_2_score)  #pourquoi ????
            
            turn.end_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            tournament.turns.append(turn)

        def after_first_round(index):
            turn = Turn()
            turn.name = "Round " + str(index + 2)
            turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            sorted_players_by_score = sorted(sorted_players_by_rank, key=operator.attrgetter('score'), reverse=True)

            total_players = len(sorted_players_by_score)
            mediane =round(len(sorted_players_by_score)/2)
            players_already_in_game = []

            for i in range(total_players):
                pair = []
                if sorted_players_by_score[i] in players_already_in_game:
                    continue
                else:
                    total_players_iterations = total_players - 1
                    for j in range(total_players_iterations):
                        break_loop = False
                        #variable pour chaque statement ?
                        if ((i + (j + 1)) <= (len(sorted_players_by_score) - 1)) and (sorted_players_by_score[i + (j + 1)] not in sorted_players_by_score[i].players_played) and (sorted_players_by_score[i + (j + 1)] not in players_already_in_game):
                            pair = [sorted_players_by_score[i],sorted_players_by_score[i + (j + 1)]]
                            players_already_in_game.extend([sorted_players_by_score[i],sorted_players_by_score[i + (j + 1)]])
                            break_loop = True
                        
                        if break_loop:
                            break

                    if len(pair) == 0:
                        setted_not_played_players = set(sorted_players_by_score) - set(players_already_in_game)
                        not_played_players = list(setted_not_played_players)
                        pair = [sorted_players_by_score[i],not_played_players[1]]
                        players_already_in_game.extend([sorted_players_by_score[i],not_played_players[1]])
                        break_loop = True

                match = create_match(pair[0], pair[1])
                turn.matches.append(match)
                print(pair[0].first_name + " will play against " + pair[1].first_name)

            confirm("end_of_turn")

            for index in range(mediane):
                player_1_name = turn.matches[index].player_1[0].first_name
                player_1_score = input("Enter " + player_1_name + "'s score : ")
                turn.matches[index].player_1[0].score += int(player_1_score)
                turn.matches[index].player_1[0].players_played.append(turn.matches[index].player_2[0])
                turn.matches[index].player_1.append(player_1_score)

                player_2_name = turn.matches[index].player_2[0].first_name
                player_2_score = input("Enter " + player_2_name + "'s score : ")
                turn.matches[index].player_2[0].score += int(player_2_score)
                turn.matches[index].player_2[0].players_played.append(turn.matches[index].player_1[0])
                turn.matches[index].player_2.append(player_2_score) 

            turn.end_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            tournament.turns.append(turn)

        first_round()
        confirm("begin_of_turn")

        number_of_turn = tournament.number_of_turn -1
        for index in range(number_of_turn):
            after_first_round(index)
            if index < 2:
                confirm("begin_of_turn")

        for player in tournament.players:
            player.players_played = []

    create_tournament()

main()


#faire les classements par ordre alphabétique et rank
# différences les acteurs / les joueurs ?
#liste tournois ? créer une méthode au dessus ?
#liste match ? pas de nom, les instances ?