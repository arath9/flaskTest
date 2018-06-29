from . import home
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from app import mysql
from datetime import datetime, timedelta




@home.route('/')
def homepage():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(rawSQL())
    data = cursor.fetchall()
    items_list=[]
    for item in data:
        i = {
            'host':item[0],
            'Cliente':item[1],
            'Categoria':item[2],
            'Cantidad':item[3]
            }
        items_list.append(i)
    return jsonify(items_list)


@home.route('/dashboard')
def dashboard():
    return 'Esto es el dashboard'

def rawSQL():
    dateFormat = '%Y-%m-%d %H:%M:%S'
    initialDate = (datetime.now() - timedelta(minutes=15)).strftime(dateFormat)
    finalDate = datetime.now().strftime(dateFormat)
    staticAtributes='select ProcEjecHost, ProcEjecDescCli, ProcEjecCateg,'
    locateAtributes=" sum(substr(ProcEjecCuerpoMail, locate('Hay ', ProcEjecCuerpoMail) + 4, locate('sesiones activas', ProcEjecCuerpoMail) - (locate('Hay ', ProcEjecCuerpoMail) + 5)))"
    fromAtributes=' from ProcesosEjecutados'
    whereDates=" where ProcEjecFecIni < " + "'" + initialDate + "'" + " and ProcEjecFecIni < " + "'" + finalDate + "'"
    whereAlertType=" and ProcEjecNomProceso like 'ctrllsappx'"
    whereGroupBy=' group by ProcEjecHost, ProcEjecDescCli, ProcEjecCateg order by 4 desc;'
    return staticAtributes + locateAtributes + fromAtributes + whereDates + whereAlertType + whereGroupBy