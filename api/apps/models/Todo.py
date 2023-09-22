from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'Todo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def __init__(self, **kwargs):
        # initialisation of the model
        super(Todo, self).__init__(**kwargs)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "complete": self.complete
        }


def create():
    db.drop_all()
    db.create_all()
