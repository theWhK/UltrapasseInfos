import csv
from datetime import datetime

def esc(code):
    return f'\033[{code}m'

print(esc('31;1;4') + 'Informações Consolidadas do Ultrapasse' + esc(0))

# Pergunta se deseja filtrar por data
gonna_filter_data = input('Deseja filtrar por data? (S/N) ').upper() or 'N'

# Se for filtrar por data, pergunta qual a data inicial e final
if gonna_filter_data == 'S':
    date_initial = input('Data inicial (dd/mm/aaaa): ')
    date_initial = datetime.strptime(date_initial, '%d/%m/%Y')
    date_final = input('Data final (dd/mm/aaaa): ')
    date_final = datetime.strptime(date_final, '%d/%m/%Y')

# Pergunta se deseja filtrar por placa
gonna_filter_plate = input('Deseja filtrar por placa? (S/N) ').upper()

# Se for filtrar por placa, pergunta qual a placa
if gonna_filter_plate == 'S':
    desired_plates = input('Placa(s), separadas por ponto-e-vírgula: ').split(';')
    print(desired_plates)

print('===============================')

with open('./../data/in/Extrato Ultrapasse.csv', encoding="utf8", mode='r') as csv_file:
    # Lê o arquivo
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Abre o dicionário de placas
    plate_dict = {}

    # Armazena a contagem de linhas
    line_count = 0

    # Itera sobre as linhas do arquivo
    for row in csv_reader:
        # Pula a primeira linha
        if line_count == 0:
            line_count += 1
            continue

        # Pega a placa
        plate = row[0]

        # Pega a data
        date = datetime.strptime(row[4], '%d-%m-%Y')

        # Sinalização se haverá ou não a inclusão da linha
        include = True

        # Se for filtrar por data, verifica se a data está dentro do intervalo
        if gonna_filter_data == 'S':
            if date <= date_initial or date >= date_final:
                include = False

        # Se for filtrar por placa, verifica se a placa é a mesma
        if gonna_filter_plate == 'S':
            if plate not in desired_plates:
                include = False

        if include:
            # Verifica se a placa já está no dicionário
            if plate not in plate_dict:
                # Se não estiver, adiciona a placa
                plate_dict[plate] = 0

            # Soma o valor do pedágio
            plate_dict[plate] += float(row[8].replace(",", "."))

        # Incrementa a contagem de linhas
        line_count += 1

    # Abre a variável do valor total
    totalCost = 0.0

    # Imprime cada linha
    for key, value in plate_dict.items():
        print(f'Placa: {key} - Valor: R$ {round(value, 2)}')
        totalCost += round(value, 2)

    # Imprime o total
    print(f'Total: R$ {round(totalCost, 2)}')