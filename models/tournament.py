from tinydb import Query, table
from models.player import Player
from models.turn import Turn
import operator

class Tournament:
    
    def __init__(self):
        self.id = "" 
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turn = 4
        self.turns = [] # mettre des id aux tours
        self.players = []
        self.time_control = ""
        self.description = ""

    def get_player_for_tournament(self,player_id, players_table, tournament): 
        PlayerToFind = Query()
        serialized_player = players_table.search(PlayerToFind.id == int(player_id)) #gérer si on entre un mauvais id, message et recommencer (while true ?)
        player_instance = Player(first_name="", rank=0, id="")
        player_instance.first_name = serialized_player[0]['first_name']
        player_instance.rank =serialized_player[0]['rank']
        player_instance.id = serialized_player[0]['id']
        player_instance.score = serialized_player[0]['score']

        tournament.players.append(player_instance)

    def deserialized_player(self,players_list): 
        instancinstancied_players_list = []
        for player in players_list:
            player_instance = Player(first_name="", rank=0, id="")
            player_instance.first_name = player['first_name']
            player_instance.rank =player['rank']
            player_instance.id = player['id']
            player_instance.score = player['score']
            player_instance.players_played = player['players_played']
            instancinstancied_players_list.append(player_instance)
        return instancinstancied_players_list

        # return player_instance

    #FACTORISER !!!!
    def sort_players_by_rank(self, tournament):
        sorte_players = sorted(tournament.players, key=operator.attrgetter('rank'))
        players_list_sorted = []
        for player in sorte_players:
            players_list_sorted.append(player.id)
        return players_list_sorted


        


    def create(self, tournament, tournaments_table, players_list, players_table):

    #FOR serialized match : key is plauer id and value is player score
        serialiazed_player_list = []
        for player in players_list:
            serialiazed_player = players_table.get(doc_id=player)
            serialiazed_player_list.append(serialiazed_player)


        serialized_tournament = {
            'name': tournament.name,
            # 'players': players_list, #modifier ça !!!
            'players': serialiazed_player_list,
            'turns': [],
            'number_of_turns': 4
        }
        tournament.id = tournaments_table.insert(serialized_tournament) 
        tournaments_table.update({'id': tournament.id}, doc_ids=[tournament.id])
        # tournaments_table.insert(serialized_tournament)


#RENAME update socre and player played

    def update_score(self,turn, tournaments_table, tournament_id):
        if type(tournament_id) is tuple:
            tournament_id = tournament_id[0]

        table_player = tournaments_table.get(doc_id= tournament_id)['players']
        print('table_players / tournament83')
        print(table_player)
        updated_table_player = []
        turn_matches = turn.matches
        for match in turn_matches:
            for player in table_player:
                if player["id"] == match.match[0][0].id:
                    opposant_player_id = match.match[1][0].id
                    player["score"] += int(match.match[0][1])
                    player["players_played"].append(opposant_player_id)
                    updated_table_player.append(player)

                elif player["id"] == match.match[1][0].id:
                    opposant_player_id = match.match[0][0].id
                    player["score"] += int(match.match[1][1])
                    player["players_played"].append(opposant_player_id)
                    updated_table_player.append(player)

        print(updated_table_player)
        tournaments_table.update({'players': updated_table_player}, doc_ids=[tournament_id])



    # def update_score(self,turn, tournaments_table, tournament_id):
    #     if type(tournament_id) is tuple:
    #         tournament_id = tournament_id[0]
    #     matches = []
    #     table_player = tournaments_table.get(doc_id= tournament_id)['players']
    #     updated_table_player = []
    #     turn_matches = turn.matches
    #     for match in turn_matches:
    #         # print(table_player)

    #         # print(updated_table_player)
    #         for player in table_player:
    #             if player["id"] == match.match[0][0].id:
    #                 player["score"] += int(match.match[0][1])
    #                 updated_table_player.append(player)

    #             elif player["id"] == match.match[1][0].id:
    #                 player["score"] += int(match.match[1][1])
    #                 updated_table_player.append(player)

    #     # print(updated_table_player)
    #     tournaments_table.update({'players': updated_table_player}, doc_ids=[tournament_id])

    # def add_turns_to_tournament(self,tournaments_table, turn_list, tournament_id):
    def add_turns_to_tournament(self,turn, tournaments_table, tournament_id):
        if type(tournament_id) is tuple:
            tournament_id = tournament_id[0]
        # serialiazed_match = {
        #     'player_1': turn.matches[0].id
        # }
        # print(serialiazed_match)
        turn_matches = turn.matches

        # print(turn_matches[0].match[0][0].id) 
        # print(turn_matches[0].match[0][1])
        # print(dir(turn_matches[0]))

        matches = []
        # table_player = tournaments_table.get(doc_id= tournament_id)['players']
        # updated_table_player = []
        for match in turn_matches:
            # print(table_player)

            # print(updated_table_player)
            # for player in table_player:
            #     if player["id"] == match.match[0][0].id:
            #         player["score"] += int(match.match[0][1])
            #         updated_table_player.append(player)

            #     elif player["id"] == match.match[1][0].id:
            #         player["score"] += int(match.match[1][1])
            #         updated_table_player.append(player)



            # tournaments_table.update({'players': table_player}, doc_ids=[tournament_id])


            # player_score_to_update_one.score += match.match[0][1]
            # tournaments_table.players.update({'score': player_score_to_update_one.score}, doc_ids=[match.match[0][0].id])

            # player_score_to_update_two = tournaments_table.players.get(doc_id= match.match[1][0].id)
            # player_score_to_update_two.score += match.match[1][1]
            # tournaments_table.players.update({'score': player_score_to_update_two.score}, doc_ids=[match.match[1][0].id])

   

            serialiazed_match = {
                match.match[0][0].id : match.match[0][1],
                match.match[1][0].id : match.match[1][1]
            }
            matches.append(serialiazed_match)

        # serialiazed_match = {
        #     turn_matches[0].match[0][0].id : turn_matches[0].match[0][1],
        #     turn_matches[0].match[1][0].id : turn_matches[0].match[1][1]
        # }

        serialiazed_turn = {
          'name': turn.name,
          'match': matches,
          'start_date': turn.start_date,
          'end_date':turn.end_date
        }
        # print(tournaments_table.get(doc_id=tournament_id))

        table_turns = tournaments_table.get(doc_id=tournament_id)['turns']
        # print(table_turns)
        table_turns.append(serialiazed_turn)
        # print(serialiazed_turn)
        # print (tournaments_table)

        tournaments_table.update({'turns': table_turns}, doc_ids=[tournament_id])


    def deserialize_turns(self,serialized_turns):
        instance_turn_list = []
        for turn in serialized_turns:
            instance_turn = Turn()
            # turn.id = 0
            instance_turn.name = turn["name"]
            instance_turn.matches = turn["match"]
            instance_turn.start_date = turn["start_date"]
            instance_turn.end_date = turn["end_date"]
            instance_turn_list.append(instance_turn)
            # print(instance_turn_list)

        return instance_turn_list


    # def update_player_score():
