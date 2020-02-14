class Team():

    def __init__(self, positions, players=None):
        self._positions = positions
        self._players = players if players else []