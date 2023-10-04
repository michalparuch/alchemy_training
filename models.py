import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# class Gry(Base):
#     # nazwa faktycznej tabei w bazie danych
#     __tablename__ = "gry"
#
#     # gra_id = sqlalchemy.Column('gra_id', sqlalchemy.SmallInteger, primary_key=True, autoincrement=True)
#     gra_id = sqlalchemy.Column('gra_id', sqlalchemy.SmallInteger, primary_key=True)
#     title = sqlalchemy.Column('title', sqlalchemy.String(180))
#     genre = sqlalchemy.Column('genre', sqlalchemy.String(20))
#     price = sqlalchemy.Column('price', sqlalchemy.DECIMAL(4, 2))
#     release = sqlalchemy.Column('release', sqlalchemy.Date)


# class Uczen(Base):
#     __tablename__ = 'uczen'
#     uczen_id = sqlalchemy.Column('uczen_id', sqlalchemy.SmallInteger, primary_key=True)
#     imie = sqlalchemy.Column('imie', sqlalchemy.String(50))
#     nazwisko = sqlalchemy.Column('nazwisko', sqlalchemy.String(50))
#     data_urodzenia = sqlalchemy.Column('data_ur', sqlalchemy.Date)
#
# class Miasto(Base):
#     __tablename__ = 'miasto'
#
#     miasto_id = sqlalchemy.Column('miasto_id',sqlalchemy.SMALLINT, primary_key=True)
#     kraj_id = sqlalchemy.Column('kraj_id', sqlalchemy.SMALLINT, sqlalchemy.ForeignKey('kraj.kraj_id'))
#
#     miasto = sqlalchemy.orm.relationship('Kraj', overlaps="miasto")
#
# class Kraj(Base):
#     __tablename__ = 'kraj'
#
#     kraj_id = sqlalchemy.Column('kraj_id',sqlalchemy.SMALLINT, primary_key=True)
#
#     miasto = sqlalchemy.orm.relationship('Miasto', overlaps='kraj')
#
# class Autor(Base):
#     __tablename__ = 'autor'
#
#     autor_id = sqlalchemy.Column('autor_id', sqlalchemy.SMALLINT,primary_key=True)
#     imie = sqlalchemy.Column('imie', sqlalchemy.String(50))
#     nazwisko = sqlalchemy.Column('nazwisko', sqlalchemy.String(50))
#     book = sqlalchemy.orm.relationship('Ksiazka', overlaps='autor')
#
# class Ksiazka(Base):
#     __tablename__ = 'ksiazka'
#
#     ksiazka_id = sqlalchemy.Column('ksiazka_id', sqlalchemy.SMALLINT,primary_key=True)
#     tytul = sqlalchemy.Column('tytul', sqlalchemy.String(100))
#     wydawnictwo = sqlalchemy.Column('wydawnictwo', sqlalchemy.String(100))
#     data_premiery = sqlalchemy.Column('data_premiery', sqlalchemy.Date)
#     liczba_stron = sqlalchemy.Column('liczba_stron', sqlalchemy.Integer)
#     autor_id = sqlalchemy.Column('autor_id', sqlalchemy.SMALLINT, sqlalchemy.ForeignKey('autor.autor_id'))
#
#     autor = sqlalchemy.orm.relationship('Autor',overlaps="book")
#
# class Gracze_new(Base):
#     __tablename__ = 'gracze_new'
#     gracz_id = sqlalchemy.Column('gracz_id', sqlalchemy.Integer, primary_key=True)
#     nickname = sqlalchemy.Column('nickname', sqlalchemy.String(50))
#
#     konto = sqlalchemy.orm.relationship('Konta_new')
#
# class Konta_new(Base):
#     __tablename__ = 'konta_new'
#     konto_id = sqlalchemy.Column('konto_id', sqlalchemy.Integer, primary_key=True)
#     gracz_id = sqlalchemy.Column('gracz_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('gracze_new.gracz_id'))
#     gra_id = sqlalchemy.Column('gra_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('gry_new.gra_id'))
#     data = sqlalchemy.Column('data', sqlalchemy.Date)
#
#     gracze = sqlalchemy.orm.relationship('Gracze_new')
#     gry = sqlalchemy.orm.relationship('Gry_new')
#
# class Gry_new(Base):
#     __tablename__ = 'gry_new'
#     gra_id = sqlalchemy.Column('gra_id', sqlalchemy.Integer, primary_key=True)
#     tytul = sqlalchemy.Column('tytul', sqlalchemy.String(100))
#
#     konta = sqlalchemy.orm.relationship('Konta_new')

#
class Gracze(Base):
    __tablename__ = "gracze"

    id_gracz = sqlalchemy.Column("id_gracz", sqlalchemy.Integer, primary_key=True)
    imie = sqlalchemy.Column("imie", sqlalchemy.String(100), nullable=False)
    nazwisko = sqlalchemy.Column("nazwisko", sqlalchemy.String(100), nullable=False)

    konto = sqlalchemy.orm.relationship("Konta")


class Gry(Base):
    __tablename__ = "gry"

    id_gra = sqlalchemy.Column("id_gra", sqlalchemy.Integer, primary_key=True)
    nazwa = sqlalchemy.Column("nazwa", sqlalchemy.String(1000), nullable=False)
    test = sqlalchemy.Column("test", sqlalchemy.String(10), nullable=True)
    konto = sqlalchemy.orm.relationship("Konta")


class Konta(Base):
    __tablename__ = 'konta'

    id_konto = sqlalchemy.Column("id_konto", sqlalchemy.Integer, primary_key=True)
    login = sqlalchemy.Column("login", sqlalchemy.String(100), nullable=False)
    id_gracz = sqlalchemy.Column("id_gracz", sqlalchemy.Integer, sqlalchemy.ForeignKey("gracze.id_gracz"), nullable=False)
    id_gra = sqlalchemy.Column("id_gra", sqlalchemy.Integer, sqlalchemy.ForeignKey("gry.id_gra"), nullable=False)

    gra = sqlalchemy.orm.relationship("Gry", overlaps="konto")
    gracz = sqlalchemy.orm.relationship("Gracze", overlaps="konto")

