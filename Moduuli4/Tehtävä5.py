user_id = input('Anna käyttäjätunnus: ')
password = input('Anna salasana: ')
tries = 0

while True:
    if user_id != 'python' or password != 'rules':
        user_id = input('Anna käyttäjätunnus: ')
        password = input('Anna salasana: ')
        tries += 1
        if tries >= 5:
            print('Pääsy evätty')
            break
        elif user_id == 'python' and password == 'rules':
            break
print('Tervetuloa')