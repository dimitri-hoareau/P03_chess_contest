import operator
from datetime import datetime
from tinydb import TinyDB
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.turn import Turn
from view import generate_report

def main():

    db = TinyDB('db.json')
    players_table = db.table('players')
    tournaments_table = db.table('tournament')

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
        player = Player(first_name="", rank=0, id="")
        player.first_name = input("Enter player's first name: ")
        # player.last_name = input("Enter player's last name: ")
        # player.birthday = input("Enter player's birthday: ")
        # player.sex = input("Enter player's sex: ")
        player.rank = input("Enter player's rank: ")
        # player.id = input("Enter player's id: ")
        # print(players_table.all())

        # voir combien de joueur il y a dans la base de donnée , l'id sera la clé, incrémentée de 1, ou mieux récupérer l'id en clé dans le dict
        player.create(player, player.first_name, player.rank, players_table)

        return player

    def create_tournament():
        tournament = Tournament()

        tournament.name =  input("Enter tournament's name: ")
        # tournament.place = input("Enter tournament's place: ")
        # tournament.date = input("Enter tournament's date: ")
        # tournament.time_control = input("Enter tournament's time_control: ")
        # tournament.description = input("Enter tournament's description: ")


        #tournament.get_player_for_tournament(player_id) => while true
        # récuper l'instance sérializée dans un tableau # ou n'envoyer que l'id comme pk etrangere et l'envoyer
        players_list = []
        for index in range(6):
            player_id = input("Enter the id of the player " + str(index + 1) + " for this tournament : ")
            tournament.get_player_for_tournament(player_id, players_table, tournament)
            players_list.append(player_id) 

        tournament.create(tournament, tournaments_table, players_list)
        create_turn(tournament)

        return tournament


    def create_match(player_1, player_2):
        match = Match()

        match.player_1.append(player_1)
        match.player_2.append(player_2)

        return match

    def create_turn(tournament):
        # for element in tournament.players:
        #     print(element.rank)
        sorted_players_by_rank = sorted(tournament.players, key=operator.attrgetter('rank'))
        # for element in sorted_players_by_rank:
        #     print(element.rank)
        def first_round():
            turn = Turn()
            turn.name = "Round 1"
            turn.id = 1
            turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            mediane =round(len(sorted_players_by_rank)/2)
            worst_player = mediane

            for index in range(mediane):
                pair = [sorted_players_by_rank[index],sorted_players_by_rank[worst_player]]
                match = create_match(pair[0], pair[1])
                turn.matches.append(match)
                worst_player += 1
                #faire appel à une focntion qui fait un print et qui sera dans les vues
                print(pair[0].first_name + " will play against " + pair[1].first_name)

            confirm("end_of_turn")

            for index in range(mediane):
                player_1_name = turn.matches[index].player_1[0].first_name
                player_1_score = input("Enter " + player_1_name + "'s score : ")
                turn.matches[index].player_1[0].score += int(player_1_score)
                #score en BDD : inutile ?
                # player_score = turn.matches[index].player_1[0].score
                # player_id = turn.matches[index].player_1[0].id
                # turn.matches[index].player_1[0].update_score(player_id, player_score, players_table)
                turn.matches[index].player_1[0].players_played.append(turn.matches[index].player_2[0])
                turn.matches[index].player_1.append(player_1_score)

                player_2_name = turn.matches[index].player_2[0].first_name
                player_2_score = input("Enter " + player_2_name + "'s score : ")
                turn.matches[index].player_2[0].score += int(player_2_score)
                turn.matches[index].player_2[0].players_played.append(turn.matches[index].player_1[0])
                turn.matches[index].player_2.append(player_2_score)  #pourquoi ????
            
            turn.end_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            tournament.turns.append(turn)
            #envoyer le tour 
            tournament.add_turns_to_tournament(turn, tournaments_table, tournament.id)

        def after_first_round(index):
            turn = Turn()
            turn.name = "Round " + str(index + 2)
            turn.id = index + 2
            turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
            sorted_players_by_score = sorted(sorted_players_by_rank, key=operator.attrgetter('score'), reverse=True)

            total_players = len(sorted_players_by_score)
            # print(total_players)
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
                        if sorted_players_by_score[i] is not not_played_players[0]:
                            pair = [sorted_players_by_score[i],not_played_players[0]]
                            players_already_in_game.extend([sorted_players_by_score[i],not_played_players[0]])
                        else:
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

        # il faut pouvoir arreter le programme quand on veut, pas de sauvegarde a la fin !!!!!!!!!!!!!!!!


        #start the creation of turns
        first_round()
        confirm("begin_of_turn")

        number_of_turn = tournament.number_of_turn -1
        for index in range(number_of_turn):
            after_first_round(index)
            if index < 2:
                confirm("begin_of_turn")

        for player in tournament.players:
            player.players_played = []

    def menu():
        print("Welcome in the chess tournament generator. What do you want to do ?")
        first_action = input("Create some players ? [1]. Create a tournament ? [2]. Resume a tournament ? [3]. Generate a report ? [4] ").lower()

        if first_action == "1":
            number_of_players = int(input("How many players do you want to create : "))
            for index in range(number_of_players):
                create_player()

        elif first_action == "2":
            create_tournament()

        # elif first_action == "3":
        #     resume_tournament()

        elif first_action == "4":
            generate_report()

    menu()

main()






#git ignore : pycache OK ? db.json OK

# le score en BDD ??


# menu pour modifier le classement des joueurs.



#resume tournament !!!!!!
# tout enregistrer, numbre de tours, already played
# et reprendre a nombre de tour + 1