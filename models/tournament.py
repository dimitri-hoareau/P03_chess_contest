from tinydb import Query, table
from models.player import Player

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

        tournament.players.append(player_instance)

    def create(self, tournament, tournaments_table, players_list):

    #FOR serialized match : key is plauer id and value is player score

        
        serialized_tournament = {
            'name': tournament.name,
            'players': players_list,
            'turns': []
        }
        tournament.id = tournaments_table.insert(serialized_tournament) 
        tournaments_table.update({'id': tournament.id}, doc_ids=[tournament.id])
        # tournaments_table.insert(serialized_tournament)


    # def add_turns_to_tournament(self,tournaments_table, turn_list, tournament_id):
    def add_turns_to_tournament(self,turn, tournaments_table, tournament_id):
        # serialiazed_match = {
        #     'player_1': turn.matches[0].id
        # }
        # print(serialiazed_match)
        turn_matches = turn.matches
        # print(turn_matches)
        # print(turn_matches[0].match[0][0].id) 
        # print(turn_matches[0].match[0][1])
        # print(dir(turn_matches[0]))

        
        serialiazed_match = {
            turn_matches[0].match[0][0].id : turn_matches[0].match[0][1],
            turn_matches[0].match[1][0].id : turn_matches[0].match[1][1]
        }

        serialiazed_turn = {
          'name': turn.name,
          'match': serialiazed_match,
          'start_date': turn.start_date,
          'end_date':turn.end_date
        }
        print(tournaments_table.get(doc_id=tournament_id))

        table_turns = tournaments_table.get(doc_id=tournament_id)['turns']
        print(table_turns)
        table_turns.append(serialiazed_turn)
        # print(serialiazed_turn)
        # print (tournaments_table)

        tournaments_table.update({'turns': table_turns}, doc_ids=[tournament_id])

