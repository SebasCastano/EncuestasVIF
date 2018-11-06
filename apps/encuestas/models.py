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
        ('0', 'No'),
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

    ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES = (
        ('5', 'Muy de acuerdo'),
        ('4', 'De acuerdo'),
        ('3', 'Ni de acuerdo, ni en desacuerdo'),
        ('2', 'En desacuerdo'),
        ('1', 'Muy en desacuerdo')
    )

    ESCALA_NINGUNA_A_EXTREMA_CHOICES = (
        ('1', 'Ninguna'),
        ('2', 'Leve'),
        ('3', 'Moderada'),
        ('4', 'Severa'),
        ('5', 'Extrema/No puede hacerlo')
    )

    ESCALA_DEPENDENCIA_EMOCIAL_CHOICES = (
        ('1', 'Completamente falso'),
        ('2', 'Mayor parte falso'),
        ('3', 'Ligeramente mas verdadero'),
        ('4', 'Moderadamente verdadero'),
        ('5', 'Mayor parte verdadero'),
        ('6', 'Me describe perfectamente')
    )

    ESCALA_VIOLENCIA_CHOICES = (
        ('1', 'Nunca'),
        ('2', 'Una vez'),
        ('3', 'Algunas veces'),
        ('4', 'Muchas veces')
    )

    ESCALA_NUNCA_A_SIEMPRE_CHOICES = (
        ('1', 'Nunca'),
        ('2', 'Pocas veces'),
        ('3', 'Algunas veces'),
        ('4', 'Muchas veces'),
        ('5', 'Siempre')
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
    i1_sentirse_desamparada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i2_ser_abandonada_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i3_deslumbrar_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i4_centro_atencion_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i5_necesitar_afecto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i6_angustia_enojo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    i7_aungustia_ausencia_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i8_preocupacion_discucion_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i9_hacerse_dano_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i10_persona_debil_necesitada = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i11_necesidad_expresividad_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i12_ser_persona_especial = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i13_vacia_tras_discusion = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i14_sentirse_mal_sin_afecto = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i15_temor_por_abandono = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i16_dejar_todo_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i17_intranquila_paradero_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i18_vacia_sola = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i19_intolerancia_soledad = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i20_cosas_temerarias_por_amor = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i21_cambiar_planes_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i22_alejar_amigos_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i23_diversion_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    j1_golpear_patear = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j2_tirar_romper = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j3_conducir_peligroso = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j4_tirar_objeto = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j5_senalar_dedo = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j6_intimidar_caras = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j7_amenazarla_puno = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j8_actuar_maton = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j9_destruirle_algo = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j10_amenazar_danar = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j11_amenazar_destruir_propiedad = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j12_amenazar_alguien_cercano = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j13_amenazar_hacerle_dano = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j14_amenazar_suicidarse = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j15_amenazar_matarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j16_amenazar_arma = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j17_amenazar_palos = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j18_actuar_querer_matarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j19_amenazar_cuchillo = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j20_agarrar_fuerte = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j21_aventarla_empujarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j22_agarrarla_repentina = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j23_estrujarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j24_aranarla_cortarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j25_harlarle_cabello = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j26_torcerle_brazo = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j27_azotarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j28_morderla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j29_darle_cachetada_palma = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j30_darle_cachetada_dorso = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j31_abofetearla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j32_golpearla_objeto = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j33_pegarle_puno = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j34_pegarle_patada = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j35_pisarla_fuerte = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j36_ahorcarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j37_quemarla = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j38_golpearla_garrote = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j39_lastimarla_arma = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j40_exigir_relaciones = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j41_obligarla_relaciones = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j42_relaciones_fuerta_bruta = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    j43_usar_objeto_sexual = models.CharField(max_length=100, choices=ESCALA_VIOLENCIA_CHOICES)
    k1_dolor_cabeza = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k2_mal_apetito = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k3_mal_dormir = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k4_facil_susto = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k5_temblor_manos = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k6_nervios_sin_causa = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k7_tensa_sin_causa = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k8_aburrida = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k9_mala_digestion = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k10_no_pensar_claro = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k11_triste = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k12_no_disfrutar_diario = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k13_no_disfrutar_trabajo = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k14_dicultad_decisiones = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k15_acabar_vida = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k16_cansada_sin_razon = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k17_sensacion_estomago = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k18_dificultad_diario = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k19_tratado_herirla = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k20_controlar_pensamientos = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k21_escuchar_voces = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k22_tener_convulsiones = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    k23_llora_frecuentemente = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    k24_util_vida = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    k25_perdidad_interes = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    k26_persona_inutil = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    k27_persona_importante = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    opinion_dificultad_proceso = models.CharField(max_length=400)
    opinion_atencion_terapia = models.CharField(max_length=400)

class DatosHombres(models.Model):

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
        ('0', 'No'),
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

    ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES = (
        ('5', 'Muy de acuerdo'),
        ('4', 'De acuerdo'),
        ('3', 'Ni de acuerdo, ni en desacuerdo'),
        ('2', 'En desacuerdo'),
        ('1', 'Muy en desacuerdo')
    )

    ESCALA_NINGUNA_A_EXTREMA_CHOICES = (
        ('1', 'Ninguna'),
        ('2', 'Leve'),
        ('3', 'Moderada'),
        ('4', 'Severa'),
        ('5', 'Extrema/No puede hacerlo')
    )

    ESCALA_DEPENDENCIA_EMOCIAL_CHOICES = (
        ('1', 'Completamente falso'),
        ('2', 'Mayor parte falso'),
        ('3', 'Ligeramente mas verdadero'),
        ('4', 'Moderadamente verdadero'),
        ('5', 'Mayor parte verdadero'),
        ('6', 'Me describe perfectamente')
    )

    ESCALA_VIOLENCIA_CHOICES = (
        ('1', 'Nunca'),
        ('2', 'Una vez'),
        ('3', 'Algunas veces'),
        ('4', 'Muchas veces')
    )

    ESCALA_NUNCA_A_SIEMPRE_CHOICES = (
        ('1', 'Nunca'),
        ('2', 'Pocas veces'),
        ('3', 'Algunas veces'),
        ('4', 'Muchas veces'),
        ('5', 'Siempre')
    )

    ESCALA_NINGUNA_A_CASI_SIEMPRE = (
        ('0', 'Nunca'),
        ('1', 'A veces'),
        ('2', 'A menudo'),
        ('3', 'Casi siempre')
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
    c1_sentir_susto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c2_sentir_miedo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c3_sentir_desmayo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c4_sentir_nervios = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c5_sentir_corazon = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c6_sentir_tembladera = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c7_sentir_tension = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c8_dolor_cabeza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c9_sentir_terror = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    c10_sentir_agitada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    d1_digna_aprecio = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    d2_cualidades_buenas = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    d3_capaz_hacer_cosas = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    d4_actitud_positiva = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    d5_satisfecha = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CHOICES)
    d6_no_estar_orgullosa = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    d7_inclino_fracasada = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    d8_sentir_respesto_propio = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    d9_pensar_ser_inutil = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    d10_no_buena_persona = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_INVERTIDA_CHOICES)
    e1_sentirse_sin_energia = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e2_culparse_por_algo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e3_llorar_facilmente = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e4_perdida_sexual = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e5_poco_apetito = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e6_dificultad_dormir = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e7_sentir_sin_esperanza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e8_sentirse_triste = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e9_sentirse_sola = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e10_pensar_acabar_vida = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e11_sentirse_atrapada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e12_preocuparse_demasiado = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e13_no_sentir_interes = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e14_sentir_todo_cuesta = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    e15_sentir_no_valer = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f_evento1 = models.CharField(max_length=200)
    f_evento2 = models.CharField(max_length=200)
    f_evento3 = models.CharField(max_length=200)
    f_evento4 = models.CharField(max_length=200)
    f_evento5 = models.CharField(max_length=200)
    f1_recuerdos_dolorosos = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f2_ocurrir_de_nuevo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f3_suenos_desagradables = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f4_sentirse_distante = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f5_sentir_incapaz_amar = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f6_saltar_susto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f7_dificultad_concentrarse = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f8_dificultad_dormir = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f9_sentirse_alerta = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f10_sentirse_irritable = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f11_evadir_situaciones = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f12_problemas_recordando = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f13_perder_interes = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f14_sentirse_sin_futuro = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f15_intentar_no_pensar = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f16_reacciones_fisicas = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f17_sentir_culpa = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    f_numero_evento = models.IntegerField()
    g1_beber_menos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g2_criticar_beber = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g3_culpable_beber = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g4_beber_manana = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g5_reducir_juego = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g6_ocultar_juego = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g7_problemas_juego = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g8_impulsado_juego = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g9_menos_drogas = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g10_niega_drogas = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g11_problema_psicologico_drogas = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g12_impulsado_drogas = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g13_vomito_evitar_engordar = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g14_perder_control_comida = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g15_creer_gordo = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g16_obsesionado_comida = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g17_tiempo_internet = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g18_quejas_internet = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g19_alejar_internet = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g20_controlar_internet = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g21_tiempo_videojuegos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g22_quejar_videojuegos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g23_dias_sin_videojuegos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g24_reducir_tiempo_videojuegos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g25_impulso_comprar = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g26_problemas_gastos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g27_problemas_credito = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g28_reducir_gastos = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g29_sexo_impedir_obligaciones = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g30_quejas_actividad_sexual = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g31_excesiva_actividad_sexual = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    g32_moderar_actividad_sexual = models.CharField(max_length=100, choices=SI_NO_CHOICES)
    h1_sentirse_desamparada = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h2_ser_abandonada_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h3_deslumbrar_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h4_centro_atencion_pareja = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h5_necesitar_afecto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h6_angustia_enojo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_MUCHAS_VECES_CHOICES)
    h7_aungustia_ausencia_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h8_preocupacion_discucion_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h9_hacerse_dano_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h10_persona_debil_necesitada = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h11_necesidad_expresividad_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h12_ser_persona_especial = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h13_vacia_tras_discusion = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h14_sentirse_mal_sin_afecto = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h15_temor_por_abandono = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h16_dejar_todo_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h17_intranquila_paradero_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h18_vacia_sola = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h19_intolerancia_soledad = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h20_cosas_temerarias_por_amor = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h21_cambiar_planes_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h22_alejar_amigos_por_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    h23_diversion_pareja = models.CharField(max_length=100, choices=ESCALA_DEPENDENCIA_EMOCIAL_CHOICES)
    i1_dificil_esperar_cola = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i2_cosas_impulsivas = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i3_dinero_impulsivo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i4_planear_anticipacion = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i5_perder_paciencia = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i6_facil_concentrarse = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i7_impulsos_sexuales = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i8_decir_primero_cabeza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i9_comer_sin_hambre = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i10_impulsivo = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i11_terminar_cosas_empieza = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i12_dificil_control_emociones = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i13_distraerse_facilmente = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i14_dificil_quieto = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    i15_cauteloso = models.CharField(max_length=100, choices=ESCALA_NINGUNA_A_CASI_SIEMPRE)
    j1_dolor_cabeza = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j2_mal_apetito = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j3_mal_dormir = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j4_facil_susto = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j5_temblor_manos = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j6_nervios_sin_causa = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j7_tensa_sin_causa = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j8_aburrida = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j9_mala_digestion = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j10_no_pensar_claro = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j11_triste = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j12_no_disfrutar_diario = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j13_no_disfrutar_trabajo = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j14_dicultad_decisiones = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j15_acabar_vida = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j16_cansada_sin_razon = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j17_sensacion_estomago = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j18_dificultad_diario = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j19_tratado_herirla = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j20_controlar_pensamientos = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j21_escuchar_voces = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j22_tener_convulsiones = models.CharField(max_length=100, choices=ESCALA_NUNCA_A_SIEMPRE_CHOICES)
    j23_llora_frecuentemente = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    j24_util_vida = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    j25_perdidad_interes = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    j26_persona_inutil = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    j27_persona_importante = models.CharField(max_length=100, choices=ESCALA_MUY_DEACUERDO_MUY_DESACUERDO_CINCO_CHOICES)
    opinion_dificultad_proceso = models.CharField(max_length=400)
    opinion_atencion_terapia = models.CharField(max_length=400)