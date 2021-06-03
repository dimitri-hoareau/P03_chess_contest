from models.tournament import Tournament
import operator
from tinydb import Query


    
def generate_report(players_table, tournaments_table, type_of_list, tournament_id=0):

    if type_of_list == "all_players_by_name":
        print("List of all players by name : ")
        players = players_table.all()
        sorted_players = sorted(players, key=lambda k: k['first_name']) 
        for player in sorted_players:
            print(f'{player}')
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
            print(turn["match"])


