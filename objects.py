import datetime

class Idea(object):
    def __init__(self, iden, barrid, company, author, market, position, thesis, metadata):
        self.iden = iden
        self.created = datetime.now()
        self.barrid = barrid
        self.company = company
        self.author = author
        self.market = market
        self.position = position
        self.thesis = thesis
        self.metadata = metadata

class User(object):
    def __init__(self, iden, username, password, born, status):
        self.iden = iden
        self.username = username
        self.password = password
        self.born = datetime.now()
        self.status = status
