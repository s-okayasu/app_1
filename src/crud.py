class Crud:

    def __init__(self, db):
        self.db = db

    def create(self, User):
        self.db.session.add(User)
        self.db.session.commit()

    def read(self, User):
        users = User.query.all()
        for recode in User.query.all():
            print(recode.name)
        return users

    #def update():

    #def delete():
