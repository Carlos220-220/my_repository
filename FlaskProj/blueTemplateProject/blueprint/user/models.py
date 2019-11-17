from blueprint import db


class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        session = db.session()
        session.add(self)
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(self)
        session.commit()


class User(Model):
    u_name = db.Column(db.String(32))
    u_email = db.Column(db.Text)
    u_password = db.Column(db.String(32))
