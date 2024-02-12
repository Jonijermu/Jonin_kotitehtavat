import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def haeTiedot(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


input1 = haeTiedot(input("Syötä ICAO-koodi\n"))
input2 = haeTiedot(input("Syötä ICAO-koodi\n"))

if input1 != None or input2 != None:
    koordinaatit1 = (input1[0], input1[1])
    koordinaatit2 = (input2[0], input2[1])

    valimatka = geodesic(koordinaatit1, koordinaatit2).kilometers
    print(f"Lentokenttien välinen välimatka on: {valimatka}")
else:
    print("Virhe: kenttiä ei löytynyt")