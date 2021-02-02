class State:
    def __init__(self, name, snapshots):
        self._name = name
        self._snapshots = snapshots


class Sector:
    def __init__(self, name, customers, sales):
        self._name = name
        self._customers = customers
        self._sales = sales


class Snapshot:
    def __init__(self, date, sectorsData):
        self._date = date
        self._data = sectorsData
