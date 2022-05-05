class Query:

    def __init__(self, db):
        self.db = db

    def select_all(self, target):
        result_list = target.query.all()
        return result_list

    def select_title(self, target, name):
        result_list = target.query.filter_by(name = name).all()
        print('info log : select conpleted count=' + str(len(result_list)))
        return result_list

    def insert(self, values):
        self.db.session.add(values)
        self.db.session.commit()
        print('info log : insert conpleted' + str(values))

    #def update():

    #def delete():
