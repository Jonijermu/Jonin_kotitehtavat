talvi = {1,2,3}
Kevät = {4,5,6}
Kesä = {7,8,9}
Syksy = {10,11,12}

numero = int(input('anna kuukausi numerona 1-12: '))
if numero in talvi:
    print('Talvi')
if numero in Kevät:
    print('Kevät')
if numero in Kesä:
    print('Kesä')
if numero in Syksy:
    print('Syksy')
else:
    print('et antanut numeroa 1-12 väliltä')