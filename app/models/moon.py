from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="moons")

    @classmethod
    def from_dict(cls,data_dict):
        return cls(name=data_dict["name"],
        description=data_dict["description"], 
        size=data_dict["size"])
    
    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            size = self.size
        ) 