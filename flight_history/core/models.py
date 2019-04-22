from django.db import models


class Airport(models.Model):
    icao = models.CharField(max_length=4, unique=True)
    iata = models.CharField(max_length=3, unique=True)
    name = models.TextField()
    alias = models.TextField(null=True)
    city = models.TextField()
    state = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aeropoto'


class Flight(models.Model):

    AUTHORIZATION_CODE = (
        (0, 'Voo regular'),
        (1, 'Voo extra com HOTRAN'),
        (2, 'Voo extra sem HOTRAN'),
        (3, 'Voo de retorno'),
        (4, 'Inclusão de etapa em um voo previsto em HOTRAN'),
        (5, 'Voo cargueiro'),
        (6, 'Voo de serviço'),
        (7, 'Voo de fretamento'),
        (9, 'Voo charter'),
        ('A', 'Voo de instrução'),
        ('B', 'Voo de experiência')
    )

    TYPE_LINE = (
        ('N', 'Nacional'),
        ('I', 'Internacional'),
        ('R', 'Regional'),
        ('H', 'Sub-regional'),
        ('E', 'Especial'),
        ('C', 'Cargueiro'),
        ('G', 'Cargueiro internacional'),
        ('L', 'Rede postal')
    )

    FLIGHT_STATUS = (
        ('C', 'Cancelado'),
        ('R', 'Realizado'),
    )

    icao = models.CharField(max_length=3, verbose_name='Empresa Área')
    number = models.IntegerField(verbose_name='Número do Vôo')
    di = models.CharField(max_length=1, choices=AUTHORIZATION_CODE,
                          default=0, verbose_name='Código de Autorização')
    line = models.CharField(max_length=1, choices=TYPE_LINE,
                            default='N', verbose_name='Código da Linha')

    departure = models.ForeignKey(
        'Airport', related_name='departure_airpot', on_delete=models.CASCADE, verbose_name='Aeroporto de Origem')
    arrival = models.ForeignKey(
        'Airport', related_name='arrival_airpot', on_delete=models.CASCADE, verbose_name='Aeroporto de Destino')

    departure_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Partida Prevista')
    departure_date_real = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Partida Real')
    arrival_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Chegada Prevista')
    arrival_date_real = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Chegada Real')

    status = models.CharField(max_length=1, choices=FLIGHT_STATUS, default='R', verbose_name='Situação')

    code = models.CharField(max_length=2, blank=True, null=True)
