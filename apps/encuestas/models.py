from datetime import date, datetime
from django.db import models


class DatosMujeres(models.Model):

    MEDICION_CHOICES = (
        ('1', 'Medicion 1 (Linea Base)'),
        ('2', 'Medicion 2 (Salida)'),
        ('3', 'Medicion 3 (Seguimiento)')
    )

    INSTITUCION_SALUD_CHOICES = (
        ('1', 'ESE Ladera de Cali'),
        ('2', 'Hospital Rubén Cruz de Tuluá'),
        ('3', 'IPS Renaseres - Piloto Hombres'),
        ('4', 'Hospital Divino Niño Buga'),
        ('5', 'Fundacion FAMI SQ - Piloto Hombres'),
        ('6', 'ESE Centro Cali'),
        ('7', 'Hospital Departamental Tomas Uribe Uribe'),
        ('8', 'Hospital Piloto Jamundí'),
    )

    CIUDAD_CHOICES = (
        ('1', 'Cali'),
        ('2', 'Tuluá'),
        ('3', 'Buga'),
        ('4', 'Santander de Quilichao')
    )

    ESTADO_CIVIL_CHOICES = (
        ('1', 'Soltera'),
        ('2', 'Casada'),
        ('3', 'Divorciada'),
        ('4', 'Separada'),
        ('5', 'Viuda'),
        ('6', 'Unión Libre')
    )

    SITUACION_SENTIMENTAL_CHOICES = (
        ('1', 'Con pareja'),
        ('2', 'Sin pareja')
    )

    ESCOLARIDAD_CHOICES = (
        ('1', 'Sin escolaridad'),
        ('2', 'Primaria'),
        ('3', 'Secundaria'),
        ('4', 'Técnico'),
        ('5', 'Universidad')
    )

    hora_inicio = models.TimeField(default=datetime.now())
    hora_final = models.TimeField(default=datetime.now())
    fecha_encuesta = models.DateField(default=date.today)
    id_paciente = models.CharField(max_length=100)
    id_encuestador = models.CharField(max_length=100)
    medicion = models.CharField(max_length=100, choices=MEDICION_CHOICES)
    institucion_salud = models.CharField(max_length=100, choices=INSTITUCION_SALUD_CHOICES)
    servicio_remitente = models.CharField(max_length=100)
    a1_ciudad = models.CharField(max_length=100, choices=CIUDAD_CHOICES)
    a2_barrio = models.CharField(max_length=100)
    a3_direccion = models.CharField(max_length=100)
    a4_edad = models.IntegerField(null=True)
    a5_estado_civil = models.CharField(max_length=100, choices=ESTADO_CIVIL_CHOICES)
    a6_situacion_sentimental = models.CharField(max_length=100, choices=SITUACION_SENTIMENTAL_CHOICES)
    a7_escolaridad = models.CharField(max_length=100, choices=ESCOLARIDAD_CHOICES)


