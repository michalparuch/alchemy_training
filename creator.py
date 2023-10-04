import sqlalchemy
from sqlalchemy.orm import Session

from models import Base, Gracze, Gry, Konta

login = 'root'
password = 'Kina23usxy5'
host = '127.0.0.1'
port = '3306'
db_name = 'zabawa'

connection_string = f'mysql+mysqlconnector://{login}:{password}@{host}:{port}/{db_name}'

print(connection_string)

silnik = sqlalchemy.create_engine(connection_string)
Base.metadata.create_all(silnik)

# with sqlalchemy.orm.Session(silnik) as moja_sesja:
#     autorek = Autor(autor_id = 10, imie = 'Andrzej', nazwisko ='Sapkowski')
#     autorek = Autor(autor_id = 11, imie='Jan', nazwisko='Kowal')
#
#     moja_sesja.add(autorek)
#
#     ksiazeczka = Ksiazka(ksiazka_id=1, tytul ='Wiedzmin: Krew Elfow', autor_id = 10)
#     moja_sesja.add(ksiazeczka)
#
#     ksiazeczka = Ksiazka(tytul='K :)')
#     moja_sesja.add(ksiazeczka)
#     moja_sesja.commit()

with sqlalchemy.orm.Session(silnik) as moja_sesja:
    gracze = [
        ["Jola", "A"],
        ["Kasia", "B"],
        ["Marcin", "J"],
        ["Zofia", "K"],
        ["Marian", "Z"],
    ]

    gry = [
        ["League of Legends"],
        ["Szachy"],
        ["Fortnite"],
        ["Rocket League"],
        ["DOOM"],
        ["Pasjans Pajak"],
    ]

    konta = [
        [1, 3, "Drzewo"],
        [4, 2, "Dewastator"],
        [2, 1, "Krzeslo"],
        [5, 1, "Quake"],
        [2, 4, "Admin"],
    ]

    for imie, nazwisko in gracze:
        item = Gracze(imie=imie, nazwisko=nazwisko)
        moja_sesja.add(item)

    for gra in gry:
        item = Gry(nazwa=gra[0])
        moja_sesja.add(item)

    for gracz, gra, login in konta:
        item = Konta(id_gracz=gracz, id_gra=gra, login=login)
        moja_sesja.add(item)

    moja_sesja.commit()