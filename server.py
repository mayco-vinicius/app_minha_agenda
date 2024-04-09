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
    reservas = database.listarReservas()
    #print(reservas)
    return template('index', dados=reservas)

@get("/cadastro")
def mostra_cadastro():
    return template("cadastro")

@post("/cadastro")
def cadastrar_reserva():
    # Obter os dados do formulário
    nome = request.forms.get("nome")
    disciplina = request.forms.get("disciplina")
    laboratorio = request.forms.get("laboratorio")
    data = request.forms.get("data")
    aula1 = "aula1" in request.forms
    aula2 = "aula2" in request.forms
    aula3 = "aula3" in request.forms
    aula4 = "aula4" in request.forms
    pin = request.forms.get("pin")

    # Verificar se o PIN está correto
    if pin != PIN:
        return "PIN incorreto. Por favor, tente novamente."

    # Criar um dicionário para a nova reserva
    nova_reserva = {
        "data": data,
        "aula1": aula1,
        "aula2": aula2,
        "aula3": aula3,
        "aula4": aula4,
        "disciplina": disciplina,
        "professor": nome,  # Considerando o nome como o professor
        "laboratorio": laboratorio
    }

    database.RESERVAS.append(nova_reserva)
    redirect("/")


run(port=PORT, reloader=True)