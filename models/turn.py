from datetime import datetime
from models.match import Match
import operator

class Turn:
    
    def __init__(self):
        self.id = 0
        self.name = ""
        self.matches = []
        self.start_date = ""
        self.end_date = ""

    def create_match(self, player_1, player_2):
        match = Match()

        match.player_1.append(player_1)
        match.player_2.append(player_2)

        return match

    def first_round(self, turn, sorted_players_by_rank, tournament, tournaments_table):
        turn.name = "Round 1"
        turn.id = 1
        turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
        mediane =round(len(sorted_players_by_rank)/2)
        worst_player = mediane

        for index in range(mediane):
            pair = [sorted_players_by_rank[index],sorted_players_by_rank[worst_player]]
            match = self.create_match(pair[0], pair[1])
            turn.matches.append(match)
            worst_player += 1
            #faire appel à une focntion qui fait un print et qui sera dans les vues
            print(pair[0].first_name + " will play against " + pair[1].first_name)

        for index in range(mediane):
            player_1_name = turn.matches[index].player_1[0].first_name
            player_1_score = input("Enter " + player_1_name + "'s score : ")
            turn.matches[index].player_1[0].score += int(player_1_score)
            turn.matches[index].player_1[0].players_played.append(turn.matches[index].player_2[0].id)
            turn.matches[index].player_1.append(player_1_score)

            player_2_name = turn.matches[index].player_2[0].first_name
            player_2_score = input("Enter " + player_2_name + "'s score : ")
            turn.matches[index].player_2[0].score += int(player_2_score)
            turn.matches[index].player_2[0].players_played.append(turn.matches[index].player_1[0].id)
            turn.matches[index].player_2.append(player_2_score)  
        
        turn.end_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
        tournament.turns.append(turn)
        tournament.add_turns_to_tournament(turn, tournaments_table, tournament.id)
        tournament.update_score(turn, tournaments_table, tournament.id)



    def after_first_round(self, index, tournament, sorted_players_by_rank, tournaments_table):
        turn = Turn()
        turn.name = "Round " + str(index + 2)
        turn.id = index + 2
        turn.start_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
        sorted_players_by_score = sorted(sorted_players_by_rank, key=operator.attrgetter('score'), reverse=True)

        total_players = len(sorted_players_by_score)
        mediane =round(len(sorted_players_by_score)/2)
        players_already_in_game = []

        print("sorted players by score turn/68")

        for i in range(total_players):
            # quand on reprend un tournoi, le tableau est vide 
            print(sorted_players_by_score[i].players_played)
            pair = []
            if sorted_players_by_score[i] in players_already_in_game:
                continue
            else:
                total_players_iterations = total_players - 1
                for j in range(total_players_iterations):
                    break_loop = False
                    if ((i + (j + 1)) <= (len(sorted_players_by_score) - 1)) and (sorted_players_by_score[i + (j + 1)].id not in sorted_players_by_score[i].players_played) and (sorted_players_by_score[i + (j + 1)] not in players_already_in_game):
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

            match = self.create_match(pair[0], pair[1])
            turn.matches.append(match)
            print(pair[0].first_name + " will play against " + pair[1].first_name)

        # confirm("end_of_turn")
        print("end of turn")

        for index in range(mediane):
            player_1_name = turn.matches[index].player_1[0].first_name
            player_1_score = input("Enter " + player_1_name + "'s score : ")
            turn.matches[index].player_1[0].score += int(player_1_score)
            turn.matches[index].player_1[0].players_played.append(turn.matches[index].player_2[0].id)
            turn.matches[index].player_1.append(player_1_score)

            player_2_name = turn.matches[index].player_2[0].first_name
            player_2_score = input("Enter " + player_2_name + "'s score : ")
            turn.matches[index].player_2[0].score += int(player_2_score)
            turn.matches[index].player_2[0].players_played.append(turn.matches[index].player_1[0].id)
            turn.matches[index].player_2.append(player_2_score) 

        turn.end_date = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
        tournament.turns.append(turn)
        tournament.add_turns_to_tournament(turn, tournaments_table, tournament.id)
        tournament.update_score(turn, tournaments_table, tournament.id)


    def turns_count(self,turns_left, tournament, sorted_players_by_rank, tournaments_table):
        # pass

        for index in range(turns_left):
            for player in sorted_players_by_rank:
                print(player.id)
            self.after_first_round(index, tournament, sorted_players_by_rank, tournaments_table)
            if index < 2: # 2 doit etre dynamique
                # confirm("begin_of_turn")
                print("*************************************")

        # for player in tournament.players:
        #     player.players_played = []

    
