class State:
    def __init__(self, name, ):
        self._name = name


class Sector:
    def __init__(self, customers, sales):
        self._customers = customers
        self._sales = sales


class Snapshot:
    def __init__(self, date, sectorsData):
        self._date = date
        self._data = sectorsData
        