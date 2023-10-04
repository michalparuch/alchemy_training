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

with Session(silnik) as moja_sesja:
    # zapytanie = moja_sesja.query(Autor)
    # print(zapytanie.all())
    # wynik = zapytanie.all()
    #
    # for autor in wynik:
    #     print(autor.imie, autor.nazwisko, autor.book)
    #     # print(dir(autor))
    #
    # zapytanie = moja_sesja.query(Ksiazka)
    # print(zapytanie.all())
    # wynik = zapytanie.all()
    #
    # for ksiazka in wynik:
    #     print(ksiazka.ksiazka_id,'\n',ksiazka.tytul,'\n',ksiazka.autor_id,'\n')
    #     # print(dir(ksiazka))
    #
    #
    # zapytanie = moja_sesja.query(Autor.imie, Autor.nazwisko)
    # wynik = zapytanie.all()
    #
    # for autor in zapytanie:
    #     print(f'Cześć jestem {autor.imie} na nazwisko mam {autor.nazwisko}')
    #
    # zapytanie = moja_sesja.query(Ksiazka.tytul).filter(Ksiazka.tytul.startswith('K')).all()
    # print(zapytanie)
    #
    # zapytanie = moja_sesja.query(Ksiazka.tytul).filter(Ksiazka.tytul.endswith('Y')).all()
    # print(zapytanie)


    # query = moja_sesja.query(Ksiazka.tytul, Autor.nazwisko, Autor.imie).join(Autor, Ksiazka.autor_id == Autor.autor_id)
    # print(query)
    #
    # wynik = query.all()
    # print(wynik)
    #
    # query = moja_sesja.query(Gracze.imie, Gracze.nazwisko, Konta.login, Gry.nazwa).join(Konta, Konta.id_gracz==Gracze.id_gracz).\
    #     join(Gracze, Konta.id_gracz == Gracze.id_gracz).join(Gry, Gry.id_gra == Konta.id_gra)
    # wynik = query.all()
    # print(wynik)

    query = moja_sesja.query(Gracze.imie, Gracze.nazwisko).join(Konta,Konta.id_gracz == Gracze.id_gracz, isouter=True).filter(Konta.login.is_(None))
    wynik = query.all()
    print(wynik)

    query = moja_sesja.query(Gracze.imie, Gracze.nazwisko, Konta.login).outerjoin(Konta, Konta.id_gracz == Gracze.id_gracz).order_by(Gracze.imie.desc(),Gracze.nazwisko.desc(), Konta.login.desc())
    wynik = query.all()
    print(wynik)

    query = moja_sesja.query(Gracze.imie, Gracze.nazwisko, sqlalchemy.func.count(Konta.id_konto)).\
        join(Konta, Konta.id_gracz == Gracze.id_gracz).group_by(Gracze.id_gracz).having(sqlalchemy.func.count(Konta.id_konto) > 1)
    wynik = query.all()
    print(wynik)

    query = moja_sesja.query(Gry.nazwa, sqlalchemy.func.count(Konta.id_gra)). \
        join(Konta, Konta.id_gra == Gry.id_gra).group_by(Gry.nazwa).having(
        sqlalchemy.func.count(Konta.id_gra) > 1)
    wynik = query.all()
    priwhent(wynik)