from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    @classmethod
    def from_dict(cls,data_dict):
        return cls(name=data_dict["name"],
        description=data_dict["description"], 
        type=data_dict["type"])
    
    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            type = self.type
        ) 