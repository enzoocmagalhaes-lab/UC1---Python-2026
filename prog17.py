temp = int(input('Digite a temperatura: '))
if temp < 18:
    print('A temperatura está frio')
elif temp >= 18 and temp <= 30:
    print('A temperatura está agradavel')
elif temp > 30:
    print('A temperatura está no calor')