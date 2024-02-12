import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def hae_lentokenttä(icao):
    sql = f"SELECT ident, name, iso_country FROM airport WHERE ident ='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for rivi in result:
          print(f'Lentokenttä on {rivi} ')

icao = input('Anna lentokentän ICAO-koodi: ')
hae_lentokenttä(icao)



