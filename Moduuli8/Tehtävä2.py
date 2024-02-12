import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def mika_maa(maa_tunnus):
    sql = f"SELECT iso_country, type FROM airport WHERE iso_country ='{maa_tunnus}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for rivi in result:
          print(f'Lentokenttä on {rivi} ')

maa_tunnus = input('Anna Maatunnus: ')
mika_maa(maa_tunnus)