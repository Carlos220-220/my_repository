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


class Course(Model):
    c_name = db.Column(db.String(32))
    description = db.Column(db.Text)
    picture = db.Column(db.String(32))
    show_number = db.Column(db.Integer)
    c_time_number = db.Column(db.Integer)
    state = db.Column(db.Integer, default=1)  # 课程状态 0 即将上线, 1 上线,默认上线
    c_type = db.Column(db.Integer, default=0)  # 课程类型 0 免费, 1 限时免费, 2 VIP会员

    def __repr__(self):
        return self.c_name
