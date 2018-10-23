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

    SI_NO_CHOICES = (
        ('1', 'Si'),
        ('2', 'No'),
    )

    DISCAPACIDAD_CHOICES = (
        ('1', 'Motora'),
        ('2', 'Visual'),
        ('3', 'Mental'),
        ('4', 'Auditiva'),
        ('5', 'Del lenguaje')
    )

    SITUACION_LABORAL_CHOICES = (
        ('1', 'Trabajo de tiempo completo'),
        ('2', 'Trabajo de medio tiempo'),
        ('3', 'Independiente'),
        ('4', 'Estudia y no trabaja'),
        ('5', 'Ni trabaja, ni estudia')
    )

    TIPO_SUSTANCIA_CHOICES = (
        ('1', 'Marihuana'),
        ('2', 'Cocaína'),
        ('3', 'Perico'),
        ('4', 'Otro'),
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
    a4_edad = models.IntegerField()
    a5_estado_civil = models.CharField(max_length=100, choices=ESTADO_CIVIL_CHOICES)
    a6_situacion_sentimental = models.CharField(max_length=100, choices=SITUACION_SENTIMENTAL_CHOICES)
    a7_escolaridad = models.CharField(max_length=100, choices=ESCOLARIDAD_CHOICES)
    a8_discapacidad = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    a8a_tipo_discapacidad = models.CharField(max_length=100, choices=DISCAPACIDAD_CHOICES)
    a9_situacion_laboral = models.CharField(max_length=100, choices=SITUACION_LABORAL_CHOICES)
    a10_consume_cigarrillo = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    a11_consume_alcohol = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    a12_consume_tipo_sustancia = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    a12a_tipo_sustancia = models.CharField(max_length=100, choices=TIPO_SUSTANCIA_CHOICES)
    a12b_otro_tipo_sustancia = models.CharField(max_length=100)
    b1_num_personas_hogar = models.IntegerField()



