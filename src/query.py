class Query:

    def __init__(self, db):
        self.db = db

    def select_all(self, target):
        result_list = target.query.all()
        print('info log : select conpleted count=' + str(len(result_list)))
        return result_list

    def select_title(self, target, key, value):
        if key == 'id':
            result = target.query.filter_by(id = value).all()
            print('info log : select conpleted count=' + str(len(result)))
            return result
        elif key == 'name':
            result_list = target.query.filter_by(name = value).all()
            print('info log : select conpleted count=' + str(len(result_list)))
            return result_list
        else:
            print('info log : invalid key')
            return []

    def select_problem(self, target, key, value):
        if key == 'id':
            result = target.query.filter_by(id = value).all()
            print('info log : select conpleted count=' + str(len(result)))
            return result
        else:
            print('info log : invalid key')
            return []

    def insert_recode(self, values):
        self.db.session.add(values)
        self.db.session.commit()
        print('info log : insert conpleted')

    def update_status(self, target, id):
        result = target.query.filter_by(id=id).update({'status': '1'})
        self.db.session.commit()
        print('info log : update conpleted count=' + str(result))

    def delete_recode(self, target, id):
        result = target.query.filter_by(id=id).delete()
        self.db.session.commit()
        print('info log : delete conpleted count=' + str(result))
