from models.tournament import Tournament
import operator
from tinydb import Query


    
def generate_report(players_table, tournaments_table, type_of_list, tournament_id=0):

    if type_of_list == "all_players_by_name":
        print("List of all players by name : ")
        players = players_table.all()
        sorted_players = sorted(players, key=lambda k: k['first_name']) 
        for player in sorted_players:
            #fstring  pour afficher joli
            print(player)
    elif type_of_list == "all_players_by_rank":
        print("List of all players by name : ")
        players = players_table.all()
        sorted_players = sorted(players, key=lambda k: k['rank']) 
        for player in sorted_players:
            print(player)
    elif type_of_list == "tournament_players_by_name":
        tournament = tournaments_table.get(doc_id=tournament_id)
        print("List of players ordered by name for the tournament : " + tournament["name"])
        players = tournament["players"]
        sorted_players = sorted(players, key=lambda k: k['first_name'])
        for player in sorted_players:
            print(player)

    elif type_of_list == "tournament_players_by_rank":
        tournament = tournaments_table.get(doc_id=tournament_id)
        print("List of players ordered by name for the tournament : " + tournament["name"])
        players = tournament["players"]
        sorted_players = sorted(players, key=lambda k: k['rank'])
        for player in sorted_players:
            print(player)

    elif type_of_list == "tournaments_list":
        tournaments = tournaments_table.all()
        print("List of all tournaments : ")
        for tournament in tournaments:
            print(tournament)

    elif type_of_list == "tournaments_turns_list":
        tournament = tournaments_table.get(doc_id=tournament_id)
        print("List of all turns for the tournament : " + tournament["name"])
        for turn in tournament["turns"]:
            print(turn)

    elif type_of_list == "tournaments_matchs_list":
        tournament = tournaments_table.get(doc_id=tournament_id)
        print("List of all matchs for the tournament : " + tournament["name"])
        for turn in tournament["turns"]:
            # nom du joueur plutot que l'id
            print(turn["match"])



#A integrer dans les controllers !!!!
# def confirm(action, tournament_id=None, tournament_players=None):
#     """
#     Ask user to enter Y or N (case-insensitive).
#     :return: True if the answer is Y.
#     :rtype: bool
#     """
#     answer = ""
#     if action == "end_of_turn":
#         while answer not in ["y"]:
#             answer = input("Is the turn completed? [Y/N] ").lower()

#     elif action == "continue_quit_updateRank":
#         print("What do you want to do ?")
#         answer = input("Continue ? [1]. Quit tournament ? [2]. Update a player rank ? [3]").lower()
#         if answer =="1":
#             pass
#         elif answer == "2":
#             print("To resume later the tournament, please note this following id : " + tournament_id)
#             quit()
#         elif answer == "3":
#             player_id = int(input("Enter the id of the player you are looking for for : "))
#             player = players_table.get(doc_id=player_id)

#     return answer == "y"