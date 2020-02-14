class Player:

    @classmethod
    def fromCSV(cls, csv_string):
        parts = csv_string.split(",")
        name = parts[2]
        positions = parts[4].split("/")
        salary = float(parts[5])
        points = float(parts[8])
        team = parts[7]
        id = parts[3]
        return cls(name, id, team, positions, salary, points)

    def __init__(self, name, id, team, positions, salary, points):
        self._name = name
        self._team = team
        self._positions = positions
        self._salary = salary
        self._points = points
        self._id = id

    def __str__(self):
        return "{} ({}) - {} - {} - {}".format(self._name, self._team, "/".join(self._positions), self._salary, self._points)
    
    def plays_position(self, position):
        return position in self._positions
