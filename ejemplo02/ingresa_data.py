from os import replace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club,Jugador

import json

engine = create_engine('sqlite:///base001.db')

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos
clubs = open("data/datos_clubs.txt", "r",encoding='utf-8')
jugadores = open("data/datos_jugadores.txt", "r",encoding='utf-8')
# Obtencion de los clubes
clubes = session.query(Club).all()

for d in clubs:
    cadena = d.split(";")
    a = cadena[len(cadena)-1].split("\n")
    cadena[len(cadena)-1] = a[0]
    mis_clubs = Club(nombre= cadena[0],deporte = cadena[1],fundacion = cadena[-1])
    session.add(mis_clubs)

for x in jugadores:
    cadena2 = x.split(";")
    a = cadena2[len(cadena2)-1].split("\n")
    cadena2[len(cadena2)-1] = a[0]
    
    for club in clubes:
        if(cadena2[0] == club.nombre):
            a = club.id

    mis_judadores = Jugador(nombre= cadena2[3], dorsal = cadena2[2], posicion = cadena2[1], club_id = a)
    session.add(mis_judadores)


session.commit()