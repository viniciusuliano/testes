import datetime


def semana_dias(f_data):
    f_data = datetime.datetime.strptime(f_data, '%Y-%m-%d').date()

    ultimo_dia_mes_seguinte = datetime.date(
        f_data.year, f_data.month+2, 1) - datetime.timedelta(days=1)
    semana_dias = []

    while f_data <= ultimo_dia_mes_seguinte:
        if f_data.weekday() not in [5, 6]:
            semana_dias.append(f_data.strftime('%Y-%m-%d'))
        f_data += datetime.timedelta(days=1)
    return semana_dias


while True:
    data_input = input('Insira uma data no formato YYYY-MM-DD: ')
    try:
        dias = semana_dias(data_input)
        if len(dias) == 0:
            print('Não existem dias úteis nesse périodo.')
        else:
            print('[DIAS ÚTEIS]:')
            for dia in dias:
                print(dia)
        break
    except ValueError:
        print('Data inválida. Por favor digite no formato [YYYY-MM-DD].')
