import csv

print('Informações Consolidadas do Ultrapasse:')

with open('./../data/in/Extrato Ultrapasse.csv', 'r') as csv_file:
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

        # Verifica se a placa já está no dicionário
        if plate not in plate_dict:
            # Se não estiver, adiciona a placa
            plate_dict[plate] = 0

        # Soma o valor do pedágio
        plate_dict[plate] += float(row[8].replace(",", "."))

        # Incrementa a contagem de linhas
        line_count += 1

    # Imprime cada linha
    for key, value in plate_dict.items():
        print(f'Placa: {key} - Valor: R$ {round(value, 2)}')
