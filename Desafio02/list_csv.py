def list_from_csv():
    import csv

    with open('../src/Informações.CSV') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        csv_reader.__next__()

        print(f'{"Id":^2}{"Nome":^20}{"Telefone":^8}  {"Idade":^3}')
        print('-' * 40)
        for row in csv_reader:
            print(f'{row[0]:^2}{row[1]:^20}{row[2]:^8}   {row[3]:^3}')
            print('-' * 40)


if __name__ == '__main__':
    list_from_csv()
