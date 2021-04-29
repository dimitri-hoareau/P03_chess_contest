import operator

class Tournament:
    
    def __init__(self):

        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turn = 6
        self.turn = []
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
        self.matches = []

 
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

        return tournament


    def create_match(player_1, player_2):
        match = Match()

        match.player_1.append(player_1)
        match.player_2.append(player_2)

        return match


    def create_turn():
        tournament_instance = create_tournament()
        sorted_players_by_rank = sorted(tournament_instance.players, key=operator.attrgetter('rank'))

        # for element in sorted_players_by_rank:
        #     print(element.first_name)
        #     print(element.rank)

        def first_turn():
            turn = Turn()
            # total_players = len(sorted_players_by_rank)
            mediane =round(len(sorted_players_by_rank)/2)
            worst_player = mediane

            for index in range(mediane):
                pair = [sorted_players_by_rank[index],sorted_players_by_rank[worst_player]]
                match = create_match(pair[0], pair[1])
                turn.matches.append(match)
                worst_player += 1

            # confirm("end_of_turn")

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
            
            tournament_instance.turn.append(turn)

        def after_first_turn():
            turn = Turn()
            # sorted_players_by_score = sorted(tournament_instance.players, key=operator.attrgetter('score', 'rank'))
            sorted_players_by_score = sorted(sorted_players_by_rank, key=operator.attrgetter('score'), reverse=True)

            # for element in sorted_players_by_score:
            #     print(element.first_name)
            #     print(element.score)

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

            # confirm("end_of_turn")

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
            
            tournament_instance.turn.append(turn)

        first_turn()

        after_first_turn()
        after_first_turn()

        # confirm("begin_of_turn")
        # print(tournament_instance.turn)
        # print(tournament_instance.turn[0].matches)
        # print(tournament_instance.turn[0].matches[0])
        # print(tournament_instance.turn[0].matches[0].match)
        # print(tournament_instance.players[0].score)
        # print(tournament_instance.players[1].score)
        # print(tournament_instance.players[2].score)
        # print(tournament_instance.players[3].score)

        # print(tournament_instance.players[0].players_played)
        # print(tournament_instance.players[1].players_played)
        # print(tournament_instance.players[2].players_played)
        # print(tournament_instance.players[3].players_played)


    test2 = create_turn()

main()


# my_list = [2,3,4,5]
# print(my_list)
# my_list[0] += 2
# print(my_list)



#ajouter id joueur pour identifier
#je pousse l'id du joueur dans le match et pas l'instance entière 
#vue : controlller appelle une fonctionne qui va faire un print

# match = [
#     (["instance", 1],["instance2", 0]),
#     (["instance4", 2],["instance3", 0]),
# ]

# print(match)
# print(sorted(match, key=lambda x: x[1][1]))