from flask import render_template, request, jsonify
from APP import app
from APP.MODELS.Missoes import Missoes, consultar_missoes
from datetime import datetime, date, time
from flask_restful import Resource, reqparse, inputs


##Argumentos Para Criar##

argumentos = reqparse.RequestParser()
argumentos.add_argument("missionName", type=str)
argumentos.add_argument("launchDate", type=inputs.date)
argumentos.add_argument("destination", type=str)
argumentos.add_argument("mission_status", type=str)
argumentos.add_argument("crew", type=str)
argumentos.add_argument("payload", type=str)
argumentos.add_argument("mission_duration", type=str)
argumentos.add_argument("mission_cost", type=float)
argumentos.add_argument("mission_report", type=str)

##Argumentos Para Atualizar##

argumentos_atualizar = reqparse.RequestParser()
argumentos_atualizar.add_argument("id", type=int)
argumentos_atualizar.add_argument("missionName", type=str)
argumentos_atualizar.add_argument("launchDate", type=inputs.date)
argumentos_atualizar.add_argument("destination", type=str)
argumentos_atualizar.add_argument("mission_status", type=str)
argumentos_atualizar.add_argument("crew", type=str)
argumentos_atualizar.add_argument("payload", type=str)
argumentos_atualizar.add_argument("mission_duration", type=str)
argumentos_atualizar.add_argument("mission_cost", type=float)
argumentos_atualizar.add_argument("mission_report", type=str)

##Argumentos para Deletar##

argumentos_delecao = reqparse.RequestParser()
argumentos_delecao.add_argument("id", type=int)

class MissaoApi(Resource):
    def get(self):
        missoes = consultar_missoes()
        missoes_serializadas = []
        for missao in missoes:
            missoes_serializadas.append(missao.serializar())
        return jsonify(json_list=missoes_serializadas)

    def post(self):
        try:
            data = argumentos.parse_args()
            nova_missao = Missoes(
                name_mission = data ['missionName'],
                date_launch = data["launchDate"].date(),
                destiny = data ['destination'],
                mission_status = data ['mission_status'],
                crew = data ['crew'], 
                charge = data ['payload'],
                mission_duration = datetime.strptime(data["mission_duration"], "%H:%M").time(), 
                mission_cost = data ['mission_cost'], 
                mission_report = data ['mission_report'],
            )
            nova_missao.salvar()   
            return {"message": "Mission create successfully"},200
        except Exception as e:
            return {"status":500, "msg":f"{e}"},500
    
    def put(self):
        try:
            data = argumentos_atualizar.parse_args()
            Missoes.update_missoes(
                self,
                id = data ['id'],
                name_mission = data ['missionName'],
                date_launch = data["launchDate"].date(),
                destiny = data ['destination'],
                mission_status = data ['mission_status'],
                crew = data ['crew'], 
                charge = data ['payload'],
                mission_duration = datetime.strptime(data['mission_duration'], "%H:%M").time(), 
                mission_cost = data ['mission_cost'], 
                mission_report = data ['mission_report'],
            )
            return {"message": "Mission update successfully"},200
        except Exception as e:
            return {"status":500, "msg":f"{e}"},500  
     
    def delete(self):
        try:
            data = argumentos_delecao.parse_args()
            Missoes.delete_missoes(self, data["id"])
            return {"message": "Mission delete successfully"},200
        except Exception as e:
            return {"status":500, "msg":f"{e}"},500       