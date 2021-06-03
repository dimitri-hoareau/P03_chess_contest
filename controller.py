import operator
from datetime import datetime
from tinydb import TinyDB
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.turn import Turn
from view import generate_report

db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournament')

def resume(tournament):
    tournament_instance = Tournament()
    print(tournament_instance)
    print(tournament)
    tournament_instance.id = tournament["id"],
    tournament_instance.name = tournament["name"],
    tournament_instance.players = tournament_instance.deserialized_player(tournament["players"])
    tournament_instance.date = tournament["date"],
    tournament_instance.number_of_turns = tournament["number_of_turns"],
    tournament_instance.turns = tournament_instance.deserialize_turns(tournament["turns"]),
    tournament_instance.turns = tournament_instance.turns[0] # because it return a tuple 
    tournament_instance.time_control = tournament["time_control"],
    tournament_instance.description = tournament["description"],

    return tournament_instance

def update_player_rank(tournament=None):

    player_id = int(input("Enter the id of the player you are looking for for : "))
    player_rank = int(input("Enter the the new rank for this player : "))

    #update player table
    players_table.update({'rank': player_rank}, doc_ids=[player_id])

    #update player in tournament instance in base
    tournament.update_rank(tournaments_table, tournament.id, player_id, player_rank)

    #update player in tournament instance
    if type(tournament.id) is tuple:
        tournament.id = tournament.id[0]
    tournament = tournaments_table.get(doc_id=tournament.id)
    for player in tournament["players"]:
        if player["id"] == player_id:
            player["rank"] = player_rank


def confirm(action, tournament=None):
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    if action == "end_of_turn":
        while answer not in ["y"]:
            answer = input("Is the turn completed? [Y/N] ").lower()

    elif action == "continue_quit_updateRank":
        print("This turn is over. What do you want to do ?")
        answer = input("Continue ? [1]. Quit tournament ? [2]. Update a player rank ? [3]").lower()
        if answer =="1":
            pass
        elif answer == "2":
            print("To resume later the tournament, please note this following id : " + str(tournament.id))
            quit()
        elif answer == "3":
            update_player_rank(tournament)
            confirm("continue_quit_updateRank", tournament)
    return answer == "y"

def main():

    def create_player():
        player = Player(first_name="", rank=0, id="", last_name="", birthday="", sex="")

        player.first_name = input("Enter player's first name: ")
        player.last_name = input("Enter player's last name: ")
        player.birthday = input("Enter player's birthday: ")
        player.sex = input("Enter player's sex: ")
        player.rank = input("Enter player's rank: ")

        player.create(player, player.first_name, player.last_name, player.birthday, player.sex, player.rank, players_table)

        return player

    def create_tournament():
        tournament = Tournament()

        tournament.name =  input("Enter tournament's name: ")
        tournament.place = input("Enter tournament's place: ")
        tournament.date = input("Enter tournament's date: ")
        tournament.time_control = input("Enter tournament's time_control: ")
        tournament.description = input("Enter tournament's description: ")

        players_list = []
        for index in range(6):
            player_id = int(input("Enter the id of the player " + str(index + 1) + " for this tournament : "))
            tournament.get_player_for_tournament(player_id, players_table, tournament)

        players_list = tournament.sort_players_by_rank(tournament)
        tournament.create(tournament, tournaments_table, players_list, players_table)
        create_turn(tournament)

        return tournament

    def resume_tournament():

        tournament_id = int(input("Enter the id of the tournament you are looking for for : "))
        tournament = tournaments_table.get(doc_id=tournament_id)
        number_of_turns = len(tournament["turns"])

        if number_of_turns >= tournament["number_of_turns"]:
            print("This tournament is already finished")
        else:
            print("You will resume the tournament : " + tournament["name"] + " from the turn number : " + str(number_of_turns + 1))
            
            tournament_instance = resume(tournament)
            turns_left = tournament_instance.number_of_turns[0] - number_of_turns
            sorted_players_by_rank = sorted(tournament_instance.players, key=operator.attrgetter('rank'))

            try:
                tournament_instance.turns[0].turns_count(turns_left, tournament_instance, sorted_players_by_rank, tournaments_table)
            except:
                create_turn(tournament_instance)


    def create_turn(tournament):

        sorted_players_by_rank = sorted(tournament.players, key=operator.attrgetter('rank'))
        turn = Turn()
        turn.first_round(turn, sorted_players_by_rank, tournament, tournaments_table, confirm)
        turns_left = tournament.number_of_turn -1
        turn.turns_count(turns_left, tournament, sorted_players_by_rank, tournaments_table, confirm)

    def menu():
        print("Welcome in the chess tournament generator. What do you want to do ?")
        first_action = input("Create some players ? [1]. Create a tournament ? [2]. Resume a tournament ? [3]. Generate a report ? [4]. Update a plyer's rank [5] ").lower()

        if first_action == "1":
            number_of_players = int(input("How many players do you want to create : "))
            for index in range(number_of_players):
                create_player()

        elif first_action == "2":
            create_tournament()

        elif first_action == "3":
            resume_tournament()

        elif first_action == "4":
            print("Select the type of report you want to generate : ")
            type_of_report = input("List for all players ? [1]. List for player's tournament ? [2]. List of tournaments ? [3]. Liste of turns ? [4]. Liste of matchs ? [5] ").lower()
            if type_of_report == "1":
                print("What type of list ? ")
                type_of_list = input("Ordered list by name ? [1]. Ordered list by rank ? [2]").lower()
                if type_of_list == "1":
                    generate_report(players_table, tournaments_table, "all_players_by_name")
                elif type_of_list == "2":
                    generate_report(players_table, tournaments_table, "all_players_by_rank")
            elif type_of_report == "2":
                tournament_id = int(input("Enter the id of the tournament you are looking for for : "))
                print("What type of list ? ")
                type_of_list = input("Ordered list by name ? [1]. Ordered list by rank ? [2]").lower()
                if type_of_list == "1":
                    generate_report(players_table, tournaments_table, "tournament_players_by_name", tournament_id)
                elif type_of_list == "2":
                    generate_report(players_table, tournaments_table, "tournament_players_by_rank", tournament_id)
            elif type_of_report == "3":
                generate_report(players_table, tournaments_table, "tournaments_list")
            elif type_of_report == "4":
                tournament_id = int(input("Enter the id of the tournament you are looking for for : "))
                generate_report(players_table, tournaments_table, "tournaments_turns_list", tournament_id)
            elif type_of_report == "5":
                tournament_id = int(input("Enter the id of the tournament you are looking for for : "))
                generate_report(players_table, tournaments_table, "tournaments_matchs_list", tournament_id)
        elif first_action == "5":
            tournament_id = int(input("Enter the id of the tournament you are looking for for : "))

            tournament = tournaments_table.get(doc_id=tournament_id)
            print(tournament)
            tournament_instance = resume(tournament)
            print(tournament_instance)
            update_player_rank(tournament_instance)
            
    menu()

main()







#faire le cours python maintenabale pour pep8


# affichage joli view OK
# update score dès le début OK
#decommenter et mettre toutes les valeurs input OK
#test en version réelle OK
#flake
#readme
#git ignore : pycache OK ? db.json OK + supprimer repo distant