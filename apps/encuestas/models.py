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
        ('4', 'Otro')
    )

    TIPO_VIVIENDA_CHOICES = (
        ('1', 'Propia'),
        ('2', 'Rentada/Alquilada'),
        ('3', 'Prestada'),
        ('4', 'Invadida')
    )

    TIPO_REGIMEN_SALUD_CHOICES  = (
        ('1', 'Contributivo'),
        ('2', 'Subsidiado'),
        ('3', 'Vinculado'),
        ('4', 'Otro')
    )

    TIPO_RELACION_AGRESOR_CHOICES = (
        ('1', 'Pareja actual EN convivencia'),
        ('2', 'Pareja actual SIN convivencia'),
        ('3', 'Pareja anterior EN convivencia'),
        ('4', 'Pareja anterior SIN convivencia'),
        ('5', 'Otro')
    )

    ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES = (
        ('0', 'Ninguna'),
        ('1', 'Pocas veces'),
        ('2', 'Varias veces'),
        ('3', 'Muchas veces')
    )

    ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES = (
        ('4', 'Muy de acuerdo'),
        ('3', 'De acuerdo'),
        ('2', 'En desacuerdo'),
        ('1', 'Muy en desacuerdo')
    )

    ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES = (
        ('1', 'Muy de acuerdo'),
        ('2', 'De acuerdo'),
        ('3', 'En desacuerdo'),
        ('4', 'Muy en desacuerdo')
    )

    ESCALA_NINGUNA_A_EXTREMA_CHOICES = (
        ('1', 'Ninguna'),
        ('2', 'Leve'),
        ('3', 'Moderada'),
        ('4', 'Severa'),
        ('5', 'Extrema/No puede hacerlo')
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
    b2_esposo = models.BooleanField()
    b2_companero = models.BooleanField()
    b2_hijos = models.BooleanField()
    b2_sobrinos = models.BooleanField()
    b2_primos = models.BooleanField()
    b2_suegros = models.BooleanField()
    b2_ex_esposo = models.BooleanField()
    b2_ex_companero = models.BooleanField()
    b2_tios = models.BooleanField()
    b2_hermanos = models.BooleanField()
    b2_abuelos = models.BooleanField()
    b2_conocidos = models.BooleanField()
    b2_otro = models.BooleanField()
    b2_otro_especificado = models.CharField(max_length=100)
    b3_num_personas_aportan_hogar = models.IntegerField()
    b4_num_personas_dependen_dentro = models.IntegerField()
    b4_num_personas_dependen_fuera = models.IntegerField()
    b5_tipo_de_vivienda = models.CharField(max_length=100, choices=TIPO_VIVIENDA_CHOICES)
    b6_regimen_salud = models.CharField(max_length=100, choices=TIPO_REGIMEN_SALUD_CHOICES)
    b6_otro_especificado = models.CharField(max_length=100)
    c1_relacion_agresor = models.CharField(max_length=100, choices=TIPO_RELACION_AGRESOR_CHOICES)
    c1_otro_especificado = models.CharField(max_length=100)
    d1_sentir_susto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d2_sentir_miedo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d3_sentir_desmayo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d4_sentir_nervios = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d5_sentir_corazon = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d6_sentir_tembladera = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d7_sentir_tension = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d8_dolor_cabeza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d9_sentir_terror = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d10_sentir_agitada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e1_digna_aprecio = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    e2_cualidades_buenas = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    e3_capaz_hacer_cosas = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    e4_actitud_positiva = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    e5_satisfecha = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    e6_no_estar_orgullosa = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    e7_inclino_fracasada = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    e8_sentir_respesto_propio = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    e9_pensar_ser_inutil = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    e10_no_buena_persona = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    f1_sentirse_sin_energia = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f2_culparse_por_algo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f3_llorar_facilmente = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f4_perdida_sexual = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f5_poco_apetito = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f6_dificultad_dormir = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f7_sentir_sin_esperanza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f8_sentirse_triste = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f9_sentirse_sola = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f10_pensar_acabar_vida = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f11_sentirse_atrapada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f12_preocuparse_demasiado = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f13_no_sentir_interes = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f14_sentir_todo_cuesta = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f15_sentir_no_valer = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    g1_pie_largo_periodo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g2_cumplir_quehaceres = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g3_aprender_nueva_tarea = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g4_mismo_nivel_otros = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g5_afectacion_emocional = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g6_concentrarse_algo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g7_caminar_distancias = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g8_lavarse_cuerpo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g9_vestirse = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g10_relacionarse_persona = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g11_mantener_amistad = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    g12_trabajo_diario = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_EXTREMA_CHOICES)
    h_evento1 = models.CharField(max_length=200)
    h_evento2 = models.CharField(max_length=200)
    h_evento3 = models.CharField(max_length=200)
    h_evento4 = models.CharField(max_length=200)
    h_evento5 = models.CharField(max_length=200)
    h1_recuerdos_dolorosos = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h2_ocurrir_de_nuevo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h3_suenos_desagradables = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h4_sentirse_distante = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h5_sentir_incapaz_amar = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h6_saltar_susto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h7_dificultad_concentrarse = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h8_dificultad_dormir = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h9_sentirse_alerta = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h10_sentirse_irritable = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h11_evadir_situaciones = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h12_problemas_recordando = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h13_perder_interes = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h14_sentirse_sin_futuro = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h15_intentar_no_pensar = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h16_reacciones_fisicas = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h17_sentir_culpa = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h_numero_evento = models.IntegerField()



