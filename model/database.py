from datetime import datetime, timedelta
import calendar
 
# Reservas iniciais
RESERVAS = [
    {
        "data": '05/03/2024',
        "aula1": True,
        "aula2": True,
        "aula3": False,
        "aula4": False,
        "disciplina": "ProgWeb",
        "professor": "Ramyres Aquino",
        "laboratorio": "A"
    },
    {
        "data": "19/03/2024",
        "aula1": False,
        "aula2": False,
        "aula3": True,
        "aula4": True,
        "disciplina": "Gestão Mobile",
        "professor": "Ramyres Aquino",
        "laboratorio": "A"
    },
    {
        "data": "20/03/2024",
        "aula1": False,
        "aula2": False,
        "aula3": True,
        "aula4": True,
        "disciplina": "Gestão Mobile",
        "professor": "Ramyres Aquino",
        "laboratorio": "B"
    },
    {
        "data": "29/03/2024",
        "aula1": True,
        "aula2": True,
        "aula3": True,
        "aula4": True,
        "disciplina": "Banco de Dados",
        "professor": "Bob",
        "laboratorio": "C"
    }
]
 
# Lista reservas cadastradas
# filtradas por laboratório ou
# por dias
def listarReservas(laboratorio = "", dias = "mes") -> list:
    RESERVAS.sort(key=orderKey)
    
    if laboratorio == "":
        reserva_por_lab = RESERVAS
    else:
        reserva_por_lab = list(filter(lambda r:r["laboratorio"] == laboratorio, RESERVAS))
   
    # filtro semana default
    hoje = datetime.now().replace(hour=0,minute=0,second=0, microsecond=0)
    
    data_inicial = hoje.replace(day=1)
    ultimo_dia_do_mes = calendar.monthrange(hoje.year, hoje.month)[1]
    data_final = hoje.replace(day=ultimo_dia_do_mes)
    
    if dias == 'semana':
        data_inicial = hoje - timedelta(days=hoje.weekday())
        data_final = data_inicial + timedelta(days=6)
 
    reserva_por_dias = list(filter(lambda r: toDate(r["data"]) >= data_inicial and 
                              toDate(r["data"]) <= data_final, 
                              reserva_por_lab))
    return reserva_por_dias 
 
# Adiciona reserva a lista
def addReserva(reserva: dict) -> bool:
    if (reserva["professor"] == "" or
        reserva["disciplina"] == "" or
        reserva["laboratorio"] == "" or
        reserva["data"] == ""):
        return False
 
    if existeColisaoDeReserva(reserva["data"], 
                              reserva["aula1"], 
                              reserva["aula2"], 
                              reserva["aula3"], 
                              reserva["aula4"]):
        return False;
    RESERVAS.append(reserva)
    return True
 
# Verifica colisão de reserva
def existeColisaoDeReserva(data, aula1, aula2, aula3, aula4) -> bool:
    dt = toDate(data)
    for reserva in RESERVAS:
        if (toDate(reserva["data"]) == dt and 
            (reserva["aula1"] == aula1 or
             reserva["aula2"] == aula2 or
             reserva["aula3"] == aula3 or
             reserva["aula4"] == aula4)):
            return True
    return False
 
# Converte string para datetime
# para utilização de funções de
# data
def toDate(dtStr) -> datetime:
    if type(dtStr) == str:
        return datetime.strptime(dtStr,'%d/%m/%Y')
    if type(dtStr) == datetime:
        return dtStr
    return datetime.now()
 
# Modificando formato de data de
# 2024-03-27 para 27/03/2024
def formatDate(dtStr):
    dt = datetime.strptime(dtStr, '%Y-%m-%d')
    return dt.strftime('%d/%m/%Y')
 
def orderKey(e):
    print(e)
    print(e["data"])
    day = int(toDate(e["data"]).day)
    print(day)
    return day
 