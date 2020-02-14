class Team():

    def __init__(self, positions, players=None):
        self._positions = positions
        self._players = players if players else {}
        self._salary = 0
        self._points = 0
        for player in self._players:
            self._salary += player._salary
            self._points += player._points
    
    def __str__(self):
        return "=======\n{}".format("\n".join([str(self._players[player]["player"]) for player in self._players]))
    
    def player_in_team(self, player):
        ids = [team_player_id for team_player_id in self._players]
        return player._id in ids

    def add_player(self, player, pos):
        self._players[player._id] = {"pos": pos, "player": player}
        self._salary += player._salary
        self._points += player._points

    def remove_player(self, player, pos):
        self._players.pop(player._id, None)
        self._salary -= player._salary
        self._points -= player._points