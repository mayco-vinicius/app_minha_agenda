#!\bin\pythn3

from os import getenv
from bottle import debug, run, get, post, request, redirect, template
from dotenv import load_dotenv
from model import database

load_dotenv()

PORT = getenv("RESERVA_PORT", 8084)

PIN = getenv("RESERVA_PIN", 1234)

@get("/")
def mostra():
    reservas = database.listarReservas(laboratorio="")
    #print(reservas)
    return template('index', dados=reservas)

@get("/cadastro")
def mostra_cadastro():
    return template("cadastro")



run(port=PORT, reloader=True)