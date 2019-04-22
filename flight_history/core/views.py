from django.shortcuts import render

from .models import Airport, Flight


for year in range(2000, 2019):
    for month in range(1, 13):

        try:
            file = '/projects/mindstorm/brazil_flight_history/data/{year}/VRA_{year}{month}.csv'.format(
                year=year, month=month)

            with open(file, encoding="ISO-8859-1") as f:
                reader = csv.reader(f)
                next(reader, None)  # skip header

                for row in reader:
                    row = next(reader, None)

                    line = row[3]
                    if line != 'N':
                        continue

                    flight_status = row[10]
                    if flight_status == 'Realizado':
                        flight_status = 'R'
                    else:
                        flight_status = 'C'

                    code = row[11]
                    if code == 'N/A':
                        code = None

                    try:
                        airport_departure = Airport.objects.get(icao=row[4])
                        airport_arrival = Airport.objects.get(icao=row[5])

                        instance = Flight.objects.get_or_create(
                            icao=row[0],
                            number=row[1],
                            di=row[2],
                            line=line,
                            departure=airport_departure,
                            arrival=airport_arrival,
                            departure_date=row[6],
                            departure_date_real=row[7],
                            arrival_date=row[8],
                            arrival_date_real=row[9],
                            status=flight_status,
                            code=code
                        )

                    except Airport.DoesNotExist:
                        print('Aeroporto não existe!')

        except FileNotFoundError:
            print('Dados do mês {month} de {year} não foram encontrados.'.format(
                month=month, year=year))
