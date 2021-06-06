from tinydb import Query
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
        self.turns = []
        self.players = []
        self.time_control = ""
        self.description = ""

    def get_player_for_tournament(self, player_id, players_table, tournament):
        PlayerToFind = Query()
        serialized_player = players_table.search(PlayerToFind.id == int(player_id))
        player_instance = Player(first_name="", last_name="", birthday="", sex="", rank=0, id="")
        player_instance.first_name = serialized_player[0]['first_name']
        player_instance.last_name = serialized_player[0]['last_name']
        player_instance.birthday = serialized_player[0]['birthday']
        player_instance.sex = serialized_player[0]['sex']
        player_instance.rank = serialized_player[0]['rank']
        player_instance.id = serialized_player[0]['id']
        player_instance.score = serialized_player[0]['score']

        tournament.players.append(player_instance)

    def deserialized_player(self, players_list):
        instancinstancied_players_list = []
        for player in players_list:
            player_instance = Player(first_name="", last_name="", birthday="", sex="", rank=0, id="")
            player_instance.first_name = player['first_name']
            player_instance.last_name = player['last_name']
            player_instance.birthday = player['birthday']
            player_instance.sex = player['sex']
            player_instance.rank = player['rank']
            player_instance.id = player['id']
            player_instance.score = player['score']
            player_instance.players_played = player['players_played']
            instancinstancied_players_list.append(player_instance)
        return instancinstancied_players_list

    def sort_players_by_rank(self, tournament):
        sorte_players = sorted(tournament.players, key=operator.attrgetter('rank'))
        players_list_sorted = []
        for player in sorte_players:
            players_list_sorted.append(player.id)
        return players_list_sorted

    def create(self, tournament, tournaments_table, players_list, players_table):
        serialiazed_player_list = []
        for player in players_list:
            serialiazed_player = players_table.get(doc_id=player)
            serialiazed_player_list.append(serialiazed_player)

        serialized_tournament = {
            'name': tournament.name,
            'place': tournament.place,
            'date': tournament.date,
            'players': serialiazed_player_list,
            'turns': [],
            'number_of_turns': 4,
            'time_control': tournament.time_control,
            'description': tournament.description
        }
        tournament.id = tournaments_table.insert(serialized_tournament)
        tournaments_table.update({'id': tournament.id}, doc_ids=[tournament.id])

    def update_score_and_players_played(self, turn, tournaments_table, tournament_id):
        if type(tournament_id) is tuple:
            tournament_id = tournament_id[0]

        table_player = tournaments_table.get(doc_id=tournament_id)['players']
        updated_table_player = []
        turn_matches = turn.matches
        for match in turn_matches:
            for player in table_player:
                if player["id"] == match.match[0][0].id:
                    opposant_player_id = match.match[1][0].id
                    player["score"] += int(float(match.match[0][1]))
                    player["players_played"].append(opposant_player_id)
                    updated_table_player.append(player)

                elif player["id"] == match.match[1][0].id:
                    opposant_player_id = match.match[0][0].id
                    player["score"] += int(float(match.match[1][1]))
                    player["players_played"].append(opposant_player_id)
                    updated_table_player.append(player)
        tournaments_table.update({'players': updated_table_player}, doc_ids=[tournament_id])

    def update_rank(self, tournaments_table, tournament_id, player_id, player_rank):
        if type(tournament_id) is tuple:
            tournament_id = tournament_id[0]
        table_player = tournaments_table.get(doc_id=tournament_id)['players']
        updated_table_player = []
        for player in table_player:
            if player["id"] == player_id:
                player["rank"] = player_rank
                updated_table_player.append(player)

            else:
                updated_table_player.append(player)

        tournaments_table.update({'players': updated_table_player}, doc_ids=[tournament_id])

    def add_turns_to_tournament(self, turn, tournaments_table, tournament_id):
        if type(tournament_id) is tuple:
            tournament_id = tournament_id[0]
        turn_matches = turn.matches

        matches = []

        for match in turn_matches:
            serialiazed_match = {
                match.match[0][0].last_name + " " + match.match[0][0].first_name + " (" + str(match.match[0][0].id) + ")": match.match[0][1],
                match.match[1][0].last_name + " " + match.match[1][0].first_name + " (" + str(match.match[1][0].id) + ")": match.match[1][1]
            }
            matches.append(serialiazed_match)

        serialiazed_turn = {
          'name': turn.name,
          'match': matches,
          'start_date': turn.start_date,
          'end_date': turn.end_date
        }

        table_turns = tournaments_table.get(doc_id=tournament_id)['turns']
        table_turns.append(serialiazed_turn)
        tournaments_table.update({'turns': table_turns}, doc_ids=[tournament_id])

    def deserialize_turns(self, serialized_turns):
        instance_turn_list = []
        for turn in serialized_turns:
            instance_turn = Turn()
            instance_turn.name = turn["name"]
            instance_turn.matches = turn["match"]
            instance_turn.start_date = turn["start_date"]
            instance_turn.end_date = turn["end_date"]
            instance_turn_list.append(instance_turn)

        return instance_turn_list
