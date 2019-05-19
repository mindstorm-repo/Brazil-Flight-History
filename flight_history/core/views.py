import csv, datetime

from django.http import JsonResponse
from django.shortcuts import render

from .models import Airport, Flight


def import_history(request):
    file_path = '/projects/mindstorm/brazil_flight_history/data/'

    for year in range(2000, 2019):
        for month in range(1, 13):

            try:
                file = file_path + f'{year}/VRA_{year}{month}.csv'

                with open(file, encoding="ISO-8859-1") as f:
                    reader = csv.reader(f, delimiter=',')
                    next(reader, None)  # skip header

                    for row in reader:

                        line = row[3]
                        if line != 'N':  # not national flight
                            continue

                        flight_status = row[10]
                        if flight_status == 'Realizado':
                            flight_status = 'R'
                        else:
                            flight_status = 'C'

                        code = row[11]
                        if code == 'N/A':
                            code = None

                        instance = Flight.objects.get_or_create(
                            icao=row[0],
                            number=row[1],
                            di=row[2],
                            line=line,
                            departure=row[4],
                            arrival=row[5],
                            departure_date=convert_datetime(row[6]),
                            departure_date_real=convert_datetime(row[7]),
                            arrival_date=convert_datetime(row[8]),
                            arrival_date_real=convert_datetime(row[9]),
                            status=flight_status,
                            code=code
                        )

                        print(f'{year}/{month} - {row[4]} -> {row[5]} saved!')


            except FileNotFoundError:
                print('Dados do mês {month} de {year} não foram encontrados.'.format(
                    month=month, year=year))

        print('------------')

    return JsonResponse({}, safe=False)


def convert_datetime(date_str):
    if date_str == '':
        converted = None
    else:
        converted = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')

    return converted
