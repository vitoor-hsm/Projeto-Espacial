from APP import db

class Missoes(db.Model):
    __tablename__ = 'missoes'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True) 
    name_mission = db.Column(db.String(255))     #-> Nome da Missão
    date_launch = db.Column(db.Date)             #-> Data de Lançamento
    destiny = db.Column(db.String(255))          #-> Destino
    mission_status = db.Column(db.String(255))   #-> Estado da Missão
    crew = db.Column(db.String(255))             #-> Tripulação
    charge = db.Column(db.String(255))           #-> Carga Util
    mission_duration = db.Column(db.Time)        #-> Duração da Missão
    mission_cost = db.Column(db.Numeric(10,2))   #-> Custo da Missão
    mission_report = db.Column(db.String(255))   #-> Status da Missão

    def __init__(self, name_mission, date_launch, destiny, mission_status, crew, charge, mission_duration, mission_cost, mission_report):
        self.name_mission = name_mission
        self.date_launch = date_launch
        self.destiny = destiny
        self.mission_status = mission_status
        self.crew = crew
        self.charge = charge
        self.mission_duration = mission_duration
        self.mission_cost = mission_cost
        self.mission_report = mission_report
    
    #SALVAR AS MISSÕES
    
    def salvar(self):
        print("adicionando no Banco")
        db.session.add(self)
        db.session.commit()
        
    
    #ATUALIZAR AS MISSÕES

    def update_missoes(self, id, name_mission, date_launch, destiny, mission_status, crew, charge, mission_duration, mission_cost, mission_report):

        db.session.query(Missoes).filter(Missoes.id==id).update({"name_mission":name_mission, "date_launch":date_launch, "destiny":destiny, "mission_status":mission_status,
                                                                    "crew":crew, "charge":charge, "mission_duration":mission_duration, "mission_cost":mission_cost, "mission_report":mission_report})
        db.session.commit()
    
    #DELETAR AS MISSÕES

    def delete_missoes(self, id):
        db.session.query(Missoes).filter(Missoes.id==id).delete()
        db.session.commit()

    
    def serializar(self):
        return {
            "id": self.id,
            "name_mission": self.name_mission, 
            "date_launch": self.date_launch.strftime('%Y-%m-%d'), 
            "destiny": self.destiny, 
            "mission_status": self.mission_status, 
            "crew": self.crew,
            "charge": self.charge,
            "mission_duration": self.mission_duration.strftime('%H:%M'),
            "mission_cost": self.mission_cost,
            "mission_report": self.mission_report
        }
    
    
def consultar_missoes():
    return db.session.query(Missoes).all()




