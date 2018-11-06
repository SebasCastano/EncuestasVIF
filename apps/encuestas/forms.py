from .models import DatosMujeres, DatosHombres
from django_select2.forms import Select2Widget
from django import forms


class AgregarEncuestaMujerForm(forms.ModelForm):
    opinion_dificultad_proceso = forms.CharField(widget=forms.Textarea, label="Por favor, indique brevemente si usted "
    "tuvo algún tipo de dificultad para asistir a las consultas de psicología, trabajo social o apoyo psicosocial "
    "durante su proceso de atención:")

    opinion_atencion_terapia = forms.CharField(widget=forms.Textarea, label="Para finalizar, indique brevemente su "
    "opinión sobre las terapias y apoyos recibidos durante su atención psicosocial.")

    def __init__(self, *args, **kwargs):
        super(AgregarEncuestaMujerForm, self).__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget.attrs['disabled'] = True
        self.fields['hora_final'].widget.attrs['disabled'] = True
        self.fields['id_encuestador'].widget.attrs['disabled'] = True
        self.fields['fecha_encuesta'].widget.attrs['disabled'] = True
        self.fields['c1_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['a12a_tipo_sustancia'].widget.attrs['disabled'] = True
        self.fields['a12b_otro_tipo_sustancia'].widget.attrs['disabled'] = True
        self.fields['b2_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['b6_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['c1_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['a4_edad'].widget.attrs['placeholder'] = "Edad en años cumplidos"
        self.fields['b2_otro_especificado'].widget.attrs['placeholder'] = "Especifique si marcó 'otro'"
        self.fields['b2_otro_especificado'].label = ""
        self.fields['b2_esposo'].label = "Esposo"
        self.fields['b2_companero'].label = "Compañero"
        self.fields['b2_hijos'].label = "Hijos"
        self.fields['b2_sobrinos'].label = "Sobrinos"
        self.fields['b2_primos'].label = "Primos"
        self.fields['b2_suegros'].label = "Suegros"
        self.fields['b2_ex_esposo'].label = "Ex-esposo"
        self.fields['b2_ex_companero'].label = "Ex-compañero"
        self.fields['b2_tios'].label = "Tíos"
        self.fields['b2_hermanos'].label = "Hermanos"
        self.fields['b2_abuelos'].label = "Abuelos"
        self.fields['b2_conocidos'].label = "Conocidos"
        self.fields['b2_otro'].label = "Otro"
        self.fields['b4_num_personas_dependen_dentro'].label = ""
        self.fields['b4_num_personas_dependen_dentro'].widget.attrs['placeholder'] = "Dentro del hogar"
        self.fields['b4_num_personas_dependen_fuera'].label = ""
        self.fields['b4_num_personas_dependen_fuera'].widget.attrs['placeholder'] = "Fuera del hogar"
        self.fields['b3_num_personas_aportan_hogar'].label = "B3 numero de persona que aportan en su hogar"
        self.fields['c1_relacion_agresor'].label = ""
        self.fields['c1_otro_especificado'].label = ""
        self.fields['c1_otro_especificado'].widget.attrs['placeholder'] = "Espeficique si marcó 'otro'"
        self.fields['d1_sentir_susto'].label = "D1 Sentirse asustada sin razón"
        self.fields['d2_sentir_miedo'].label = "D2 Sentirse con miedo"
        self.fields['d3_sentir_desmayo'].label = "D3 Sentirse con desmayos, mareos o debilidad"
        self.fields['d4_sentir_nervios'].label = "D4 Sentirse nerviosa o con temblores"
        self.fields['d5_sentir_corazon'].label = "D5 Sentir el corazón que se le quiere salir"
        self.fields['d6_sentir_tembladera'].label = "D6 Sentir tembladera"
        self.fields['d7_sentir_tension'].label = "D7 Sentirse tensa o rígida"
        self.fields['d8_dolor_cabeza'].label = "D8 Estar con dolor de cabeza"
        self.fields['d9_sentir_terror'].label = "D9 Tener sentimientos de terror o pánico"
        self.fields['d10_sentir_agitada'].label = "D10 Sentirse agitada, como si no se pudiera quedar tranquila"
        self.fields['e1_digna_aprecio'].label = "E1 Siento que soy digna de aprecio, al menos en igual medida que los demás"
        self.fields['e2_cualidades_buenas'].label = "E2 Estoy convencida de que tengo cualidades buenas"
        self.fields['e3_capaz_hacer_cosas'].label = "E3 Soy capaz de hacer las cosas tan bien como la mayoría de la gente"
        self.fields['e4_actitud_positiva'].label = "E4 Tengo una actitud positiva hacia mí misma"
        self.fields['e5_satisfecha'].label = "E5 En general estoy satisfecha de mí misma"
        self.fields['e6_no_estar_orgullosa'].label = "E6 Siento que no tengo mucho de lo que estar orgullosa"
        self.fields['e7_inclino_fracasada'].label = "E7  En general, me inclino a pensar que soy una fracasada"
        self.fields['e8_sentir_respesto_propio'].label = "E8 Me gustaría sentir más respeto por mí misma"
        self.fields['e9_pensar_ser_inutil'].label = "E9 Hay veces que realmente pienso que soy una inútil"
        self.fields['e10_no_buena_persona'].label = "E10 A veces pienso que no soy buena persona"
        self.fields['f1_sentirse_sin_energia'].label = "F1 Sentirse sin energía, como si estuviera lenta"
        self.fields['f2_culparse_por_algo'].label = "F2 Culparse uno mismo por alguna cosa"
        self.fields['f3_llorar_facilmente'].label = "F3 Llorar fácilmente "
        self.fields['f4_perdida_sexual'].label = "F4 Pérdida de interés sexual"
        self.fields['f5_poco_apetito'].label = "F5 Poco apetito"
        self.fields['f6_dificultad_dormir'].label = "F6 Dificultad para quedarse dormida, permanecer dormida"
        self.fields['f7_sentir_sin_esperanza'].label = "F7 Sentirse sin esperanza por el futuro"
        self.fields['f8_sentirse_triste'].label = "F8 Sentirse triste"
        self.fields['f9_sentirse_sola'].label = "F9 Sentirse sola"
        self.fields['f10_pensar_acabar_vida'].label = "F10 Pensamientos de acabar con la vida propia"
        self.fields['f11_sentirse_atrapada'].label = "F11 Sentirse atrapada o encarcelada"
        self.fields['f12_preocuparse_demasiado'].label = "F12 Preocuparse demasiado por cosas"
        self.fields['f13_no_sentir_interes'].label = "F13 No sentir interés por las cosas"
        self.fields['f14_sentir_todo_cuesta'].label = "F14 Sentir que todo cuesta mucho esfuerzo"
        self.fields['f15_sentir_no_valer'].label = "F15 Sentir que uno no vale nada"
        self.fields['g1_pie_largo_periodo'].label = "G1 Estar de pie durante largos periodos de tiempo, como por ejemplo 30 minutos."
        self.fields['g2_cumplir_quehaceres'].label = "G2 Cumplir con sus quehaceres de la casa."
        self.fields['g3_aprender_nueva_tarea'].label = "G3 Aprender una nueva tarea, como por ejemplo llegar a un lugar nuevo."
        self.fields['g4_mismo_nivel_otros'].label = "G4 Cuánta dificultad ha tenido para participar, al mismo nivel que el resto de las personas, en actividades de la comunidad (por ejemplo, fiestas, actividades religiosas u otras actividades)."
        self.fields['g5_afectacion_emocional'].label = "G5 ¿Cuánto le ha afectado emocionalmente su “condición de salud”? (El evento traumático de violencia)"
        self.fields['g6_concentrarse_algo'].label = "G6 Concentrarse en hacer algo durante diez (10) minutos."
        self.fields['g7_caminar_distancias'].label = "G7 Caminar largas distancias, como un kilómetro (más o menos 10 cuadras)."
        self.fields['g8_lavarse_cuerpo'].label = "G8 Lavarse todo el cuerpo (Bañarse)"
        self.fields['g9_vestirse'].label = "G9 Vestirse"
        self.fields['g10_relacionarse_persona'].label = "G10 Relacionarse con personas que no conoce"
        self.fields['g11_mantener_amistad'].label = "G11 Mantener una amistad"
        self.fields['g12_trabajo_diario'].label = "G12 Llevar a cabo su trabajo diario o actividades académicas"
        self.fields['h_evento1'].label = "1."
        self.fields['h_evento2'].label = "2."
        self.fields['h_evento3'].label = "3."
        self.fields['h_evento4'].label = "4."
        self.fields['h_evento5'].label = "5."
        self.fields['h1_recuerdos_dolorosos'].label = "H1 Recuerdos y pensamientos recurrentes sobre un evento doloroso"
        self.fields['h2_ocurrir_de_nuevo'].label = "H2 Tener sentimientos como si algo que me ocurrió me fuera a ocurrir de nuevo"
        self.fields['h3_suenos_desagradables'].label = "H3 Tener sueños desagradables sobre algo que ocurrió"
        self.fields['h4_sentirse_distante'].label = "H4 Sentirse distante o alejada de otras personas"
        self.fields['h5_sentir_incapaz_amar'].label = "H5 Sentir que no es capaz de amar a las personas cercanas a usted"
        self.fields['h6_saltar_susto'].label = "H6 Sentir que fácilmente salta del susto o se siente nerviosa"
        self.fields['h7_dificultad_concentrarse'].label = "H7 Tener dificultad para concentrarse"
        self.fields['h8_dificultad_dormir'].label = "H8 Dificultad para quedarse dormida"
        self.fields['h9_sentirse_alerta'].label = "H9 Sentirse muy alerta o prevenida"
        self.fields['h10_sentirse_irritable'].label = "H10 Sentirse irritable o con arranques de rabia"
        self.fields['h11_evadir_situaciones'].label = "H11 Intentar evadir situaciones o actividades que le recuerdan lo que le pasó"
        self.fields['h12_problemas_recordando'].label = "H12 Tener problemas recordando cosas importantes de algo que ocurrió"
        self.fields['h13_perder_interes'].label = "H13 Perder el interés en cosas que antes le gustaba hacer"
        self.fields['h14_sentirse_sin_futuro'].label = "H14 Sentir como si no tuviera futuro"
        self.fields['h15_intentar_no_pensar'].label = "H15 Intentar no pensar o hablar de algo que le ha ocurrido"
        self.fields['h16_reacciones_fisicas'].label = "H16 Tener reacciones físicas o emocionales (se acelera el corazón, la respiración y sudoración) cuando algo le recuerda de algo que haya ocurrido"
        self.fields['h17_sentir_culpa'].label = "H17 Sentir culpa"
        self.fields['h_numero_evento'].label = "¿Estos pensamientos o sentimientos que me acaba de describir son principalmente de cuál evento? (Leerle a la participante el listado de eventos que ella mencionó)."
        self.fields['h_numero_evento'].widget.attrs['placeholder'] = "Especifique número"
        self.fields['i1_sentirse_desamparada'].label = "I1 Me siento desamparada cuando estoy sola"
        self.fields['i2_ser_abandonada_pareja'].label = "I2 Me preocupa la idea de ser abandonada por mi pareja"
        self.fields['i3_deslumbrar_pareja'].label = "I3 Para atraer a mi pareja busco deslumbrarlo o divertirlo"
        self.fields['i4_centro_atencion_pareja'].label = "I4 Hago todo lo posible por ser el centro de atención en la vida de mi pareja"
        self.fields['i5_necesitar_afecto'].label = "I5 Necesito constantemente expresiones de afecto de mi pareja"
        self.fields['i6_angustia_enojo'].label = "I6 Si mi pareja no llama o no aparece a la hora acordada me angustia pensar que está enojado conmigo"
        self.fields['i7_aungustia_ausencia_pareja'].label = "I7 Cuando mi pareja debe ausentarse por algunos días me siento angustiada"
        self.fields['i8_preocupacion_discucion_pareja'].label = "I8 Cuando discuto con mi pareja me preocupa que deje de quererme"
        self.fields['i9_hacerse_dano_por_pareja'].label = "I9 He amenazado con hacerme daño para que mi pareja no me deje"
        self.fields['i10_persona_debil_necesitada'].label = "I10 Soy una persona necesitada y débil"
        self.fields['i11_necesidad_expresividad_pareja'].label = "I11 Necesito demasiado que mi pareja sea expresiva conmigo"
        self.fields['i12_ser_persona_especial'].label = "I12 Necesito tener a una persona para quien yo sea más especial que los demás"
        self.fields['i13_vacia_tras_discusion'].label = "I13 Cuando tengo una discusión con mi pareja me siento vacía"
        self.fields['i14_sentirse_mal_sin_afecto'].label = "I14 Me siento muy mal si mi pareja no me expresa constantemente el afecto"
        self.fields['i15_temor_por_abandono'].label = "I15 Siento temor a que mi pareja me abandone"
        self.fields['i16_dejar_todo_por_pareja'].label = "I16 Si mi pareja me propone un programa dejo todas las actividades que tenga para estar con él"
        self.fields['i17_intranquila_paradero_pareja'].label = "I17 Si desconozco donde está mi pareja me siento intranquila"
        self.fields['i18_vacia_sola'].label = "I18 Siento una fuerte sensación de vacío cuando estoy sola"
        self.fields['i19_intolerancia_soledad'].label = "I19 No tolero la soledad"
        self.fields['i20_cosas_temerarias_por_amor'].label = "I20 Soy capaz de hacer cosas temerarias, hasta arriesgar mi vida, por conservar el amor del otro"
        self.fields['i21_cambiar_planes_por_pareja'].label = "I21 Si tengo planes y mi pareja aparece los cambio sólo por estar con él"
        self.fields['i22_alejar_amigos_por_pareja'].label = "I22 Me alejo demasiado de mis amigos cuando tengo una relación de pareja"
        self.fields['i23_diversion_pareja'].label = "I23 Me divierto solo cuando estoy con mi pareja"
        self.fields['j1_golpear_patear'].label = "J1 Golpear o patear una pared, puerta o algún mueble"
        self.fields['j2_tirar_romper'].label = "J2 Tirar, aplastar o romper un objeto"
        self.fields['j3_conducir_peligroso'].label = "J3 Conducir de manera peligrosa con usted en la moto o carro"
        self.fields['j4_tirar_objeto'].label = "J4 Tirarle algún objeto"
        self.fields['j5_senalar_dedo'].label = "J5 Señalarla con el dedo autoritariamente"
        self.fields['j6_intimidar_caras'].label = "J6 Intimidarla con gestos o caras amenazantes"
        self.fields['j7_amenazarla_puno'].label = "J7 Amenazarla mostrándole el puño"
        self.fields['j8_actuar_maton'].label = "J8 Actuar como un matón para intimidarla"
        self.fields['j9_destruirle_algo'].label = "J9 Destruir algo que le pertenece a usted"
        self.fields['j10_amenazar_danar'].label = "J10 Amenazarla con dañar  o dañar cosas que son importantes para usted"
        self.fields['j11_amenazar_destruir_propiedad'].label = "J11 Amenazar con destruir su casa/propiedad"
        self.fields['j12_amenazar_alguien_cercano'].label = "J12 Amenazar a alguien cercano a usted"
        self.fields['j13_amenazar_hacerle_dano'].label = "J13 Amenazar con hacerle daño"
        self.fields['j14_amenazar_suicidarse'].label = "J14 Amenazar con suicidarse"
        self.fields['j15_amenazar_matarla'].label = "J15 Amenazar con matarla"
        self.fields['j16_amenazar_arma'].label = "J16 Amenazarla con armas"
        self.fields['j17_amenazar_palos'].label = "J17 Amenazarla con objetos como palos o garrotes"
        self.fields['j18_actuar_querer_matarla'].label = "J18 Actuar como si quisiera matarla"
        self.fields['j19_amenazar_cuchillo'].label = "J19 Amenazarla con un cuchillo o pistola"
        self.fields['j20_agarrar_fuerte'].label = "J20 Agarrarla fuerte para que se quede en un lugar"
        self.fields['j21_aventarla_empujarla'].label = "J21 Aventarla o empujarla a propósito"
        self.fields['j22_agarrarla_repentina'].label = "J22 Agarrarla de manera repentina o con fuerza"
        self.fields['j23_estrujarla'].label = "J23 Estrujarla"
        self.fields['j24_aranarla_cortarla'].label = "J24 Arañarla o cortarla"
        self.fields['j25_harlarle_cabello'].label = "J25 Halarle el cabello"
        self.fields['j26_torcerle_brazo'].label = "J26 Torcerle un brazo"
        self.fields['j27_azotarla'].label = "J27 Azotarla"
        self.fields['j28_morderla'].label = "J28 Morderla"
        self.fields['j29_darle_cachetada_palma'].label = "J29 Darle una cachetada con la palma de la mano"
        self.fields['j30_darle_cachetada_dorso'].label = "J30 Darle una cachetada con el dorso de la mano"
        self.fields['j31_abofetearla'].label = "J31 Abofetearla en la cara y cabeza"
        self.fields['j32_golpearla_objeto'].label = "J32 Golpearla con un objeto"
        self.fields['j33_pegarle_puno'].label = "J33 Pegarle puños"
        self.fields['j34_pegarle_patada'].label = "J34 Pegarle patadas"
        self.fields['j35_pisarla_fuerte'].label = "J35 Pisarla fuerte o brincado sobre usted"
        self.fields['j36_ahorcarla'].label = "J36 Ahorcarla o sofocarla"
        self.fields['j37_quemarla'].label = "J37 Quemarla con algo"
        self.fields['j38_golpearla_garrote'].label = "J38 Golpearla con un palo o un garrote"
        self.fields['j39_lastimarla_arma'].label = "J39 Lastimarla con un cuchillo o una pistola"
        self.fields['j40_exigir_relaciones'].label = "J40 Exigirle que tengan relaciones sexuales sin importarle su opinión"
        self.fields['j41_obligarla_relaciones'].label = "J41 Obligarla a tener relaciones sexuales en contra de su voluntad"
        self.fields['j42_relaciones_fuerta_bruta'].label = "J42 Hacer que tengan relaciones sexuales usando la fuerza bruta"
        self.fields['j43_usar_objeto_sexual'].label = "J43 Usar un objeto de manera sexual contra usted"
        self.fields['k1_dolor_cabeza'].label = "K1 ¿Ha sufrido de dolores de cabeza?"
        self.fields['k2_mal_apetito'].label = "K2 ¿Ha tenido mal apetito? "
        self.fields['k3_mal_dormir'].label = "K3 ¿Ha dormido mal? "
        self.fields['k4_facil_susto'].label = "K4 ¿Se asusta con facilidad o sin causa aparente? "
        self.fields['k5_temblor_manos'].label = "K5 ¿Le tiemblan las manos? "
        self.fields['k6_nervios_sin_causa'].label = "K6 ¿Se ha sentido nerviosa sin causa aparente? "
        self.fields['k7_tensa_sin_causa'].label = "K7 ¿Se ha sentido tensa sin causa aparente? "
        self.fields['k8_aburrida'].label = "K8 ¿Se ha sentido aburrida? "
        self.fields['k9_mala_digestion'].label = "K9 ¿Ha sufrido de mala digestión? (Ej: Acidez, reflujo, estreñimiento, etc.)"
        self.fields['k10_no_pensar_claro'].label = "K10 ¿No puede pensar con claridad? "
        self.fields['k11_triste'].label = "K11 ¿Se ha sentido triste? "
        self.fields['k12_no_disfrutar_diario'].label = "K12 ¿Ha tenido dificultad para disfrutar sus   actividades diarias? "
        self.fields['k13_no_disfrutar_trabajo'].label = "K13 ¿Ha tenido dificultad para hacer su trabajo y/o actividades diarias? "
        self.fields['k14_dicultad_decisiones'].label = "K14  ¿Ha tenido dificultad para tomar decisiones? "
        self.fields['k15_acabar_vida'].label = "K15 ¿Ha tenido la idea de acabar con su vida? "
        self.fields['k16_cansada_sin_razon'].label = "K16 ¿Se siente cansada sin razón aparente? "
        self.fields['k17_sensacion_estomago'].label = "K17 ¿Ha tenido sensaciones desagradables en su estómago?  (Vacío, mariposas, vértigo)"
        self.fields['k18_dificultad_diario'].label = "K18 ¿Se cansa con mucha facilidad al realizar sus actividades diarias? "
        self.fields['k19_tratado_herirla'].label = "K19 ¿Siente que las personas han estado tratando de herirla en alguna forma? "
        self.fields['k20_controlar_pensamientos'].label = "K20 ¿Ha notado que algo intenta controlar o interferir en sus pensamientos?"
        self.fields['k21_escuchar_voces'].label = "K21 ¿Oye voces sin saber de dónde vienen o que otras personas no pueden oír?"
        self.fields['k22_tener_convulsiones'].label = "K22 ¿Ha tenido convulsiones, ataques o caídas al suelo, con movimientos de brazos y piernas; con mordedura de la lengua o pérdida del conocimiento?"
        self.fields['k23_llora_frecuentemente'].label = "K23 Soy alguien que llora con mucha frecuencia "
        self.fields['k24_util_vida'].label = "K24 Soy incapaz de desempeñar un papel útil en la vida"
        self.fields['k25_perdidad_interes'].label = "K25 Últimamente he perdido el interés en las cosas "
        self.fields['k26_persona_inutil'].label = "K26 Siento que soy una persona inútil"
        self.fields['k27_persona_importante'].label = "K27 Soy una persona más importante que todos los demás"
        self.fields['opinion_dificultad_proceso'].widget.attrs['placeholder'] = "Comente.."
        self.fields['opinion_atencion_terapia'].widget.attrs['placeholder'] = "Comente.."
        self.fields['opinion_dificultad_proceso'].widget.attrs['style'] = "resize:none"
        self.fields['opinion_atencion_terapia'].widget.attrs['style'] = "resize:none"

    class Meta:
        model = DatosMujeres
        fields = ('hora_inicio', 'hora_final','fecha_encuesta', 'id_paciente', 'id_encuestador', 'medicion',
                  'institucion_salud','servicio_remitente', 'a1_ciudad', 'a2_barrio', 'a3_direccion', 'a4_edad',
                  'a5_estado_civil', 'a6_situacion_sentimental', 'a7_escolaridad', 'a8_discapacidad',
                  'a8a_tipo_discapacidad', 'a9_situacion_laboral', 'a10_consume_cigarrillo', 'a11_consume_alcohol',
                  'a12_consume_tipo_sustancia', 'a12a_tipo_sustancia', 'a12b_otro_tipo_sustancia', 'b1_num_personas_hogar',
                  'b2_esposo', 'b2_companero', 'b2_hijos', 'b2_sobrinos', 'b2_primos','b2_suegros', 'b2_ex_esposo',
                  'b2_ex_companero', 'b2_tios', 'b2_hermanos', 'b2_abuelos', 'b2_conocidos', 'b2_otro',
                  'b2_otro_especificado', 'b3_num_personas_aportan_hogar', 'b4_num_personas_dependen_dentro',
                  'b4_num_personas_dependen_fuera', 'b5_tipo_de_vivienda', 'b6_regimen_salud', 'b6_otro_especificado',
                  'c1_relacion_agresor', 'c1_otro_especificado', 'd1_sentir_susto', 'd2_sentir_miedo', 'd3_sentir_desmayo',
                  'd4_sentir_nervios', 'd5_sentir_corazon', 'd6_sentir_tembladera', 'd7_sentir_tension', 'd8_dolor_cabeza',
                  'd9_sentir_terror', 'd10_sentir_agitada', 'e1_digna_aprecio', 'e2_cualidades_buenas','e3_capaz_hacer_cosas',
                  'e4_actitud_positiva', 'e5_satisfecha', 'e6_no_estar_orgullosa', 'e7_inclino_fracasada',
                  'e8_sentir_respesto_propio', 'e9_pensar_ser_inutil', 'e10_no_buena_persona', 'f1_sentirse_sin_energia',
                  'f2_culparse_por_algo', 'f3_llorar_facilmente','f4_perdida_sexual', 'f5_poco_apetito',
                  'f6_dificultad_dormir', 'f7_sentir_sin_esperanza', 'f8_sentirse_triste', 'f9_sentirse_sola',
                  'f10_pensar_acabar_vida', 'f11_sentirse_atrapada', 'f12_preocuparse_demasiado', 'f13_no_sentir_interes',
                  'f14_sentir_todo_cuesta', 'f15_sentir_no_valer', 'g1_pie_largo_periodo', 'g2_cumplir_quehaceres',
                  'g3_aprender_nueva_tarea', 'g4_mismo_nivel_otros', 'g5_afectacion_emocional', 'g6_concentrarse_algo',
                  'g7_caminar_distancias', 'g8_lavarse_cuerpo','g9_vestirse','g10_relacionarse_persona',
                  'g11_mantener_amistad', 'g12_trabajo_diario', 'h_evento1', 'h_evento2', 'h_evento3', 'h_evento4',
                  'h_evento5', 'h1_recuerdos_dolorosos', 'h2_ocurrir_de_nuevo', 'h3_suenos_desagradables',
                  'h4_sentirse_distante', 'h5_sentir_incapaz_amar', 'h6_saltar_susto', 'h7_dificultad_concentrarse',
                  'h8_dificultad_dormir', 'h9_sentirse_alerta', 'h10_sentirse_irritable', 'h11_evadir_situaciones',
                  'h12_problemas_recordando', 'h13_perder_interes', 'h14_sentirse_sin_futuro', 'h15_intentar_no_pensar',
                  'h16_reacciones_fisicas', 'h17_sentir_culpa', 'h_numero_evento', 'i1_sentirse_desamparada',
                  'i2_ser_abandonada_pareja', 'i3_deslumbrar_pareja', 'i4_centro_atencion_pareja', 'i5_necesitar_afecto',
                  'i6_angustia_enojo', 'i7_aungustia_ausencia_pareja', 'i8_preocupacion_discucion_pareja',
                  'i9_hacerse_dano_por_pareja', 'i10_persona_debil_necesitada', 'i11_necesidad_expresividad_pareja',
                  'i12_ser_persona_especial', 'i13_vacia_tras_discusion', 'i14_sentirse_mal_sin_afecto',
                  'i15_temor_por_abandono', 'i16_dejar_todo_por_pareja', 'i17_intranquila_paradero_pareja',
                  'i18_vacia_sola', 'i19_intolerancia_soledad', 'i20_cosas_temerarias_por_amor',
                  'i21_cambiar_planes_por_pareja', 'i22_alejar_amigos_por_pareja', 'i23_diversion_pareja',
                  'j1_golpear_patear', 'j2_tirar_romper', 'j3_conducir_peligroso', 'j4_tirar_objeto', 'j5_senalar_dedo',
                  'j6_intimidar_caras', 'j7_amenazarla_puno', 'j8_actuar_maton', 'j9_destruirle_algo',
                  'j10_amenazar_danar', 'j11_amenazar_destruir_propiedad', 'j12_amenazar_alguien_cercano',
                  'j13_amenazar_hacerle_dano', 'j14_amenazar_suicidarse', 'j15_amenazar_matarla', 'j16_amenazar_arma',
                  'j17_amenazar_palos', 'j18_actuar_querer_matarla', 'j19_amenazar_cuchillo', 'j20_agarrar_fuerte',
                  'j21_aventarla_empujarla', 'j22_agarrarla_repentina', 'j23_estrujarla', 'j24_aranarla_cortarla',
                  'j25_harlarle_cabello', 'j26_torcerle_brazo', 'j27_azotarla', 'j28_morderla', 'j29_darle_cachetada_palma',
                  'j30_darle_cachetada_dorso', 'j31_abofetearla', 'j32_golpearla_objeto', 'j33_pegarle_puno',
                  'j34_pegarle_patada', 'j35_pisarla_fuerte', 'j36_ahorcarla', 'j37_quemarla', 'j38_golpearla_garrote',
                  'j39_lastimarla_arma', 'j40_exigir_relaciones', 'j41_obligarla_relaciones', 'j42_relaciones_fuerta_bruta',
                  'j43_usar_objeto_sexual', 'k1_dolor_cabeza', 'k2_mal_apetito', 'k3_mal_dormir', 'k4_facil_susto',
                  'k5_temblor_manos', 'k6_nervios_sin_causa', 'k7_tensa_sin_causa', 'k8_aburrida', 'k9_mala_digestion',
                  'k10_no_pensar_claro', 'k11_triste', 'k12_no_disfrutar_diario', 'k13_no_disfrutar_trabajo',
                  'k14_dicultad_decisiones', 'k15_acabar_vida', 'k16_cansada_sin_razon', 'k17_sensacion_estomago',
                  'k18_dificultad_diario', 'k19_tratado_herirla', 'k20_controlar_pensamientos', 'k21_escuchar_voces',
                  'k22_tener_convulsiones', 'k23_llora_frecuentemente', 'k24_util_vida', 'k25_perdidad_interes',
                  'k26_persona_inutil', 'k27_persona_importante', 'opinion_dificultad_proceso',
                  'opinion_atencion_terapia')

    widgets = {
        "opinion_dificultad_proceso": forms.Textarea,
        "opinion_atencion_terapia": forms.Textarea
    }

class AgregarEncuestaHombreForm(forms.ModelForm):
    opinion_dificultad_proceso = forms.CharField(widget=forms.Textarea, label="Por favor, indique brevemente si usted "
    "tuvo algún tipo de dificultad para asistir a las consultas de psicología, trabajo social o apoyo psicosocial "
    "durante su proceso de atención:")

    opinion_atencion_terapia = forms.CharField(widget=forms.Textarea, label="Para finalizar, indique brevemente su "
    "opinión sobre las terapias y apoyos recibidos durante su atención psicosocial.")

    def __init__(self, *args, **kwargs):
        super(AgregarEncuestaHombreForm, self).__init__(*args, **kwargs)
        self.fields['fecha_encuesta'].widget.attrs['disabled'] = True
        self.fields['hora_inicio'].widget.attrs['disabled'] = True
        self.fields['hora_final'].widget.attrs['disabled'] = True
        self.fields['id_encuestador'].widget.attrs['disabled'] = True
        self.fields['a12a_tipo_sustancia'].widget.attrs['disabled'] = True
        self.fields['a12b_otro_tipo_sustancia'].widget.attrs['disabled'] = True
        self.fields['b2_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['b6_otro_especificado'].widget.attrs['disabled'] = True
        self.fields['a4_edad'].widget.attrs['placeholder'] = "Edad en años cumplidos"
        self.fields['b2_otro_especificado'].widget.attrs['placeholder'] = "Especifique si marcó 'otro'"
        self.fields['b2_otro_especificado'].label = ""
        self.fields['b2_esposo'].label = "Esposo"
        self.fields['b2_companero'].label = "Compañero"
        self.fields['b2_hijos'].label = "Hijos"
        self.fields['b2_sobrinos'].label = "Sobrinos"
        self.fields['b2_primos'].label = "Primos"
        self.fields['b2_suegros'].label = "Suegros"
        self.fields['b2_ex_esposo'].label = "Ex-esposo"
        self.fields['b2_ex_companero'].label = "Ex-compañero"
        self.fields['b2_tios'].label = "Tíos"
        self.fields['b2_hermanos'].label = "Hermanos"
        self.fields['b2_abuelos'].label = "Abuelos"
        self.fields['b2_conocidos'].label = "Conocidos"
        self.fields['b2_otro'].label = "Otro"
        self.fields['b4_num_personas_dependen_dentro'].label = ""
        self.fields['b4_num_personas_dependen_dentro'].widget.attrs['placeholder'] = "Dentro del hogar"
        self.fields['b4_num_personas_dependen_fuera'].label = ""
        self.fields['b4_num_personas_dependen_fuera'].widget.attrs['placeholder'] = "Fuera del hogar"
        self.fields['b3_num_personas_aportan_hogar'].label = "B3 numero de persona que aportan en su hogar"
        self.fields['c1_sentir_susto'].label = "C1 Sentirse asustada sin razón"
        self.fields['c2_sentir_miedo'].label = "C2 Sentirse con miedo"
        self.fields['c3_sentir_desmayo'].label = "C3 Sentirse con desmayos, mareos o debilidad"
        self.fields['c4_sentir_nervios'].label = "C4 Sentirse nerviosa o con temblores"
        self.fields['c5_sentir_corazon'].label = "C5 Sentir el corazón que se le quiere salir"
        self.fields['c6_sentir_tembladera'].label = "C6 Sentir tembladera"
        self.fields['c7_sentir_tension'].label = "C7 Sentirse tensa o rígida"
        self.fields['c8_dolor_cabeza'].label = "C8 Estar con dolor de cabeza"
        self.fields['c9_sentir_terror'].label = "C9 Tener sentimientos de terror o pánico"
        self.fields['c10_sentir_agitada'].label = "C10 Sentirse agitada, como si no se pudiera quedar tranquila"
        self.fields['d1_digna_aprecio'].label = "D1 Siento que soy digna de aprecio, al menos en igual medida que los demás"
        self.fields['d2_cualidades_buenas'].label = "D2 Estoy convencida de que tengo cualidades buenas"
        self.fields['d3_capaz_hacer_cosas'].label = "D3 Soy capaz de hacer las cosas tan bien como la mayoría de la gente"
        self.fields['d4_actitud_positiva'].label = "D4 Tengo una actitud positiva hacia mí misma"
        self.fields['d5_satisfecha'].label = "D5 En general estoy satisfecha de mí misma"
        self.fields['d6_no_estar_orgullosa'].label = "D6 Siento que no tengo mucho de lo que estar orgullosa"
        self.fields['d7_inclino_fracasada'].label = "D7  En general, me inclino a pensar que soy una fracasada"
        self.fields['d8_sentir_respesto_propio'].label = "D8 Me gustaría sentir más respeto por mí misma"
        self.fields['d9_pensar_ser_inutil'].label = "D9 Hay veces que realmente pienso que soy una inútil"
        self.fields['d10_no_buena_persona'].label = "D10 A veces pienso que no soy buena persona"
        self.fields['e1_sentirse_sin_energia'].label = "E1 Sentirse sin energía, como si estuviera lenta"
        self.fields['e2_culparse_por_algo'].label = "E2 Culparse uno mismo por alguna cosa"
        self.fields['e3_llorar_facilmente'].label = "E3 Llorar fácilmente "
        self.fields['e4_perdida_sexual'].label = "E4 Pérdida de interés sexual"
        self.fields['e5_poco_apetito'].label = "E5 Poco apetito"
        self.fields['e6_dificultad_dormir'].label = "E6 Dificultad para quedarse dormida, permanecer dormida"
        self.fields['e7_sentir_sin_esperanza'].label = "E7 Sentirse sin esperanza por el futuro"
        self.fields['e8_sentirse_triste'].label = "E8 Sentirse triste"
        self.fields['e9_sentirse_sola'].label = "E9 Sentirse sola"
        self.fields['e10_pensar_acabar_vida'].label = "E10 Pensamientos de acabar con la vida propia"
        self.fields['e11_sentirse_atrapada'].label = "E11 Sentirse atrapada o encarcelada"
        self.fields['e12_preocuparse_demasiado'].label = "E12 Preocuparse demasiado por cosas"
        self.fields['e13_no_sentir_interes'].label = "E13 No sentir interés por las cosas"
        self.fields['e14_sentir_todo_cuesta'].label = "E14 Sentir que todo cuesta mucho esfuerzo"
        self.fields['e15_sentir_no_valer'].label = "E15 Sentir que uno no vale nada"
        self.fields['f_evento1'].label = "1."
        self.fields['f_evento2'].label = "2."
        self.fields['f_evento3'].label = "3."
        self.fields['f_evento4'].label = "4."
        self.fields['f_evento5'].label = "5."
        self.fields['f1_recuerdos_dolorosos'].label = "F1 Recuerdos y pensamientos recurrentes sobre un evento doloroso"
        self.fields['f2_ocurrir_de_nuevo'].label = "F2 Tener sentimientos como si algo que me ocurrió me fuera a ocurrir de nuevo"
        self.fields['f3_suenos_desagradables'].label = "F3 Tener sueños desagradables sobre algo que ocurrió"
        self.fields['f4_sentirse_distante'].label = "F4 Sentirse distante o alejada de otras personas"
        self.fields['f5_sentir_incapaz_amar'].label = "F5 Sentir que no es capaz de amar a las personas cercanas a usted"
        self.fields['f6_saltar_susto'].label = "F6 Sentir que fácilmente salta del susto o se siente nerviosa"
        self.fields['f7_dificultad_concentrarse'].label = "F7 Tener dificultad para concentrarse"
        self.fields['f8_dificultad_dormir'].label = "F8 Dificultad para quedarse dormida"
        self.fields['f9_sentirse_alerta'].label = "F9 Sentirse muy alerta o prevenida"
        self.fields['f10_sentirse_irritable'].label = "F10 Sentirse irritable o con arranques de rabia"
        self.fields['f11_evadir_situaciones'].label = "F11 Intentar evadir situaciones o actividades que le recuerdan lo que le pasó"
        self.fields['f12_problemas_recordando'].label = "F12 Tener problemas recordando cosas importantes de algo que ocurrió"
        self.fields['f13_perder_interes'].label = "F13 Perder el interés en cosas que antes le gustaba hacer"
        self.fields['f14_sentirse_sin_futuro'].label = "F14 Sentir como si no tuviera futuro"
        self.fields['f15_intentar_no_pensar'].label = "F15 Intentar no pensar o hablar de algo que le ha ocurrido"
        self.fields['f16_reacciones_fisicas'].label = "F16 Tener reacciones físicas o emocionales (se acelera el corazón, la respiración y sudoración) cuando algo le recuerda de algo que haya ocurrido"
        self.fields['f17_sentir_culpa'].label = "F17 Sentir culpa"
        self.fields['f_numero_evento'].label = "¿Estos pensamientos o sentimientos que me acaba de describir son principalmente de cuál evento? (Leerle a la participante el listado de eventos que ella mencionó)."
        self.fields['f_numero_evento'].widget.attrs['placeholder'] = "Especifique número"
        self.fields['g1_beber_menos'].label = "G1 ¿Ha pensado alguna vez que debería beber menos?"
        self.fields['g2_criticar_beber'].label = "G2 ¿Se ha sentido molesto cuando alguna persona le ha criticado su manera o forma de beber?"
        self.fields['g3_culpable_beber'].label = "G3¿Se ha sentido culpable alguna vez por su manera o forma de beber?"
        self.fields['g4_beber_manana'].label = "G4 ¿Alguna vez lo primero que ha hecho por la mañana es beber alguna bebida alcohólica  para relajarse o para eliminar el guayabo?"
        self.fields['g5_reducir_juego'].label = "G5 ¿Ha tenido usted la sensación de que debería reducir su conducta de juego? (Apuestas, chances, casinos)"
        self.fields['g6_ocultar_juego'].label = "G6 ¿Niega u oculta su verdadera conducta de juego para que los demás no lo critiquen sobre sus supuestos excesos?"
        self.fields['g7_problemas_juego'].label = "G7 ¿Ha tenido usted problemas psicológicos, familiares, económicos o laborales a causa del juego?"
        self.fields['g8_impulsado_juego'].label = "G8 ¿Se siente con frecuencia impulsado irremediablemente a jugar (Apuestas, chances, casinos) a pesar de sus problemas?"
        self.fields['g9_menos_drogas'].label = "G9 ¿Ha pensado alguna vez que debería usted consumir menos drogas?"
        self.fields['g10_niega_drogas'].label = "G10 ¿Niega usted su consumo de drogas a familiares, amigos o compañeros para evitar que lo critiquen?"
        self.fields['g11_problema_psicologico_drogas'].label = "G11 ¿Ha tenido usted problemas psicológicos, económicos, laborales o familiares a causa de su consumo de drogas?"
        self.fields['g12_impulsado_drogas'].label = "G12 ¿Se siente a veces impulsado a consumir drogas aunque haya decidido no hacerlo?"
        self.fields['g13_vomito_evitar_engordar'].label = "G13 ¿Alguna vez se ha provocado el vómito para evitar engordar?"
        self.fields['g14_perder_control_comida'].label = "G14 ¿Le preocupa que haya perdido el control sobre la cantidad de comida que ingiere?"
        self.fields['g15_creer_gordo'].label = "G15 ¿Cree usted que está gordo aunque los demás le digan que está demasiado delgado/a?"
        self.fields['g16_obsesionado_comida'].label = "G16 ¿Está usted obsesionado con la comida, las dietas y el control de su peso?"
        self.fields['g17_tiempo_internet'].label = "G17 ¿Dedica más tiempo del que cree que debería a estar conectado a Internet/celular con objetivos distintos a los de su trabajo?"
        self.fields['g18_quejas_internet'].label = "G18 ¿Se han quejado sus familiares de las horas que dedica a Internet/celular?"
        self.fields['g19_alejar_internet'].label = "G19 ¿Le resulta duro permanecer alejado de Internet/celular varios días seguidos?"
        self.fields['g20_controlar_internet'].label = "G20 ¿Tiene problemas para controlar el impulso de conectarse a Internet/celular o ha intentado sin éxito reducir el tiempo que dedica a estar conectado?"
        self.fields['g21_tiempo_videojuegos'].label = "G21 ¿Dedica más tiempo del que cree que debería a jugar videojuegos?"
        self.fields['g22_quejar_videojuegos'].label = "G22 ¿Se queja su familia de que pasa demasiado tiempo jugando videojuegos?"
        self.fields['g23_dias_sin_videojuegos'].label = "G23 ¿Le cuesta trabajo estar varios días sin usar videojuegos?"
        self.fields['g24_reducir_tiempo_videojuegos'].label = "G24 ¿Ha intentado sin éxito reducir el tiempo que dedica a jugar videojuegos?"
        self.fields['g25_impulso_comprar'].label = "G25 ¿Tiene usted dificultades para controlar su impulso de comprar, gastando con frecuencia más dinero del que debería?"
        self.fields['g26_problemas_gastos'].label = "G26 ¿Ha tenido problemas con sus familiares debido a sus gastos excesivos y su falta de control sobre el dinero?"
        self.fields['g27_problemas_credito'].label = "G27 ¿Ha tenido problemas con su banco o con familiares por hacer un uso excesivo de las tarjetas de crédito/débito o por haberse quedado sin fondos debido a gastos incontrolados?"
        self.fields['g28_reducir_gastos'].label = "G28 ¿Ha intentado sin éxito controlar su dinero y reducir los gastos innecesarios?"
        self.fields['g29_sexo_impedir_obligaciones'].label = "G29 ¿Su actividad sexual le ha impedido realizar tareas habituales en su vida, como trabajo u obligaciones familiares?"
        self.fields['g30_quejas_actividad_sexual'].label = "G30 ¿Se han quejado sus parejas de su excesiva actividad sexual?"
        self.fields['g31_excesiva_actividad_sexual'].label = "G31 ¿Alguna vez ha considerado que su actividad sexual es excesiva?"
        self.fields['g32_moderar_actividad_sexual'].label = "G32 ¿Ha intentado alguna vez sin éxito moderar su actividad sexual?"
        self.fields['h1_sentirse_desamparada'].label = "H1 Me siento desamparada cuando estoy sola"
        self.fields['h2_ser_abandonada_pareja'].label = "H2 Me preocupa la idea de ser abandonada por mi pareja"
        self.fields['h3_deslumbrar_pareja'].label = "H3 Para atraer a mi pareja busco deslumbrarlo o divertirlo"
        self.fields['h4_centro_atencion_pareja'].label = "H4 Hago todo lo posible por ser el centro de atención en la vida de mi pareja"
        self.fields['h5_necesitar_afecto'].label = "H5 Necesito constantemente expresiones de afecto de mi pareja"
        self.fields['h6_angustia_enojo'].label = "H6 Si mi pareja no llama o no aparece a la hora acordada me angustia pensar que está enojado conmigo"
        self.fields['h7_aungustia_ausencia_pareja'].label = "H7 Cuando mi pareja debe ausentarse por algunos días me siento angustiada"
        self.fields['h8_preocupacion_discucion_pareja'].label = "H8 Cuando discuto con mi pareja me preocupa que deje de quererme"
        self.fields['h9_hacerse_dano_por_pareja'].label = "H9 He amenazado con hacerme daño para que mi pareja no me deje"
        self.fields['h10_persona_debil_necesitada'].label = "H10 Soy una persona necesitada y débil"
        self.fields['h11_necesidad_expresividad_pareja'].label = "H11 Necesito demasiado que mi pareja sea expresiva conmigo"
        self.fields['h12_ser_persona_especial'].label = "H12 Necesito tener a una persona para quien yo sea más especial que los demás"
        self.fields['h13_vacia_tras_discusion'].label = "H13 Cuando tengo una discusión con mi pareja me siento vacía"
        self.fields['h14_sentirse_mal_sin_afecto'].label = "H14 Me siento muy mal si mi pareja no me expresa constantemente el afecto"
        self.fields['h15_temor_por_abandono'].label = "H15 Siento temor a que mi pareja me abandone"
        self.fields['h16_dejar_todo_por_pareja'].label = "H16 Si mi pareja me propone un programa dejo todas las actividades que tenga para estar con él"
        self.fields['h17_intranquila_paradero_pareja'].label = "H17 Si desconozco donde está mi pareja me siento intranquila"
        self.fields['h18_vacia_sola'].label = "H18 Siento una fuerte sensación de vacío cuando estoy sola"
        self.fields['h19_intolerancia_soledad'].label = "H19 No tolero la soledad"
        self.fields['h20_cosas_temerarias_por_amor'].label = "H20 Soy capaz de hacer cosas temerarias, hasta arriesgar mi vida, por conservar el amor del otro"
        self.fields['h21_cambiar_planes_por_pareja'].label = "H21 Si tengo planes y mi pareja aparece los cambio sólo por estar con él"
        self.fields['h22_alejar_amigos_por_pareja'].label = "H22 Me alejo demasiado de mis amigos cuando tengo una relación de pareja"
        self.fields['h23_diversion_pareja'].label = "H23 Me divierto solo cuando estoy con mi pareja"
        self.fields['i1_dificil_esperar_cola'].label = "I1 ¿Le resulta difícil esperar en una cola?"
        self.fields['i2_cosas_impulsivas'].label = "I2 ¿Hace cosas impulsivamente?"
        self.fields['i3_dinero_impulsivo'].label = "I3 ¿Gasta dinero impulsivamente?"
        self.fields['i4_planear_anticipacion'].label = "I4 ¿Planea cosas con anticipación?"
        self.fields['i5_perder_paciencia'].label = "I5 ¿Pierde la paciencia a menudo?"
        self.fields['i6_facil_concentrarse'].label = "I6 ¿Le resulta fácil concentrarse?"
        self.fields['i7_impulsos_sexuales'].label = "I7  ¿Le resulta difícil controlar los impulsos sexuales?"
        self.fields['i8_decir_primero_cabeza'].label = "I8  ¿Dice usted lo primero que le viene a la cabeza?"
        self.fields['i9_comer_sin_hambre'].label = "I9  ¿Acostumbra a comer aun cuando no tenga hambre?"
        self.fields['i10_impulsivo'].label = "I10 ¿Es usted impulsivo?"
        self.fields['i11_terminar_cosas_empieza'].label = "I11 ¿Termina las cosas que empieza?"
        self.fields['i12_dificil_control_emociones'].label = "I12 ¿Le resulta difícil controlar las emociones?"
        self.fields['i13_distraerse_facilmente'].label = "I13 ¿Se distrae fácilmente?"
        self.fields['i14_dificil_quieto'].label = "I14 ¿Le resulta difícil quedarse quieto?"
        self.fields['i15_cauteloso'].label = "I15 ¿Es usted cuidadoso o cauteloso?"
        self.fields['j1_dolor_cabeza'].label = "J1 ¿Ha sufrido de dolores de cabeza?"
        self.fields['j2_mal_apetito'].label = "J2 ¿Ha tenido mal apetito? "
        self.fields['j3_mal_dormir'].label = "J3 ¿Ha dormido mal? "
        self.fields['j4_facil_susto'].label = "J4 ¿Se asusta con facilidad o sin causa aparente? "
        self.fields['j5_temblor_manos'].label = "J5 ¿Le tiemblan las manos? "
        self.fields['j6_nervios_sin_causa'].label = "J6 ¿Se ha sentido nerviosa sin causa aparente? "
        self.fields['j7_tensa_sin_causa'].label = "J7 ¿Se ha sentido tensa sin causa aparente? "
        self.fields['j8_aburrida'].label = "J8 ¿Se ha sentido aburrida? "
        self.fields['j9_mala_digestion'].label = "J9 ¿Ha sufrido de mala digestión? (Ej: Acidez, reflujo, estreñimiento, etc.)"
        self.fields['j10_no_pensar_claro'].label = "J10 ¿No puede pensar con claridad? "
        self.fields['j11_triste'].label = "J11 ¿Se ha sentido triste? "
        self.fields['j12_no_disfrutar_diario'].label = "J12 ¿Ha tenido dificultad para disfrutar sus   actividades diarias? "
        self.fields['j13_no_disfrutar_trabajo'].label = "J13 ¿Ha tenido dificultad para hacer su trabajo y/o actividades diarias? "
        self.fields['j14_dicultad_decisiones'].label = "J14  ¿Ha tenido dificultad para tomar decisiones? "
        self.fields['j15_acabar_vida'].label = "J15 ¿Ha tenido la idea de acabar con su vida? "
        self.fields['j16_cansada_sin_razon'].label = "J16 ¿Se siente cansada sin razón aparente? "
        self.fields['j17_sensacion_estomago'].label = "J17 ¿Ha tenido sensaciones desagradables en su estómago?  (Vacío, mariposas, vértigo)"
        self.fields['j18_dificultad_diario'].label = "J18 ¿Se cansa con mucha facilidad al realizar sus actividades diarias? "
        self.fields['j19_tratado_herirla'].label = "J19 ¿Siente que las personas han estado tratando de herirla en alguna forma? "
        self.fields['j20_controlar_pensamientos'].label = "J20 ¿Ha notado que algo intenta controlar o interferir en sus pensamientos?"
        self.fields['j21_escuchar_voces'].label = "J21 ¿Oye voces sin saber de dónde vienen o que otras personas no pueden oír?"
        self.fields['j22_tener_convulsiones'].label = "J22 ¿Ha tenido convulsiones, ataques o caídas al suelo, con movimientos de brazos y piernas; con mordedura de la lengua o pérdida del conocimiento?"
        self.fields['j23_llora_frecuentemente'].label = "J23 Soy alguien que llora con mucha frecuencia "
        self.fields['j24_util_vida'].label = "J24 Soy incapaz de desempeñar un papel útil en la vida"
        self.fields['j25_perdidad_interes'].label = "J25 Últimamente he perdido el interés en las cosas "
        self.fields['j26_persona_inutil'].label = "J26 Siento que soy una persona inútil"
        self.fields['j27_persona_importante'].label = "J27 Soy una persona más importante que todos los demás"
        self.fields['opinion_dificultad_proceso'].widget.attrs['placeholder'] = "Comente.."
        self.fields['opinion_atencion_terapia'].widget.attrs['placeholder'] = "Comente.."
        self.fields['opinion_dificultad_proceso'].widget.attrs['style'] = "resize:none"
        self.fields['opinion_atencion_terapia'].widget.attrs['style'] = "resize:none"

    class Meta:
        model = DatosHombres
        fields = ('hora_inicio', 'hora_final','fecha_encuesta', 'id_paciente', 'id_encuestador', 'medicion',
                  'institucion_salud','servicio_remitente', 'a1_ciudad', 'a2_barrio', 'a3_direccion', 'a4_edad',
                  'a5_estado_civil', 'a6_situacion_sentimental', 'a7_escolaridad', 'a8_discapacidad',
                  'a8a_tipo_discapacidad', 'a9_situacion_laboral', 'a10_consume_cigarrillo', 'a11_consume_alcohol',
                  'a12_consume_tipo_sustancia', 'a12a_tipo_sustancia', 'a12b_otro_tipo_sustancia', 'b1_num_personas_hogar',
                  'b2_esposo', 'b2_companero', 'b2_hijos', 'b2_sobrinos', 'b2_primos','b2_suegros', 'b2_ex_esposo',
                  'b2_ex_companero', 'b2_tios', 'b2_hermanos', 'b2_abuelos', 'b2_conocidos', 'b2_otro',
                  'b2_otro_especificado', 'b3_num_personas_aportan_hogar', 'b4_num_personas_dependen_dentro',
                  'b4_num_personas_dependen_fuera', 'b5_tipo_de_vivienda', 'b6_regimen_salud', 'b6_otro_especificado',
                  'c1_sentir_susto', 'c2_sentir_miedo', 'c3_sentir_desmayo',
                  'c4_sentir_nervios', 'c5_sentir_corazon', 'c6_sentir_tembladera', 'c7_sentir_tension', 'c8_dolor_cabeza',
                  'c9_sentir_terror', 'c10_sentir_agitada', 'd1_digna_aprecio', 'd2_cualidades_buenas', 'd3_capaz_hacer_cosas',
                  'd4_actitud_positiva', 'd5_satisfecha', 'd6_no_estar_orgullosa', 'd7_inclino_fracasada',
                  'd8_sentir_respesto_propio', 'd9_pensar_ser_inutil', 'd10_no_buena_persona', 'e1_sentirse_sin_energia',
                  'e2_culparse_por_algo', 'e3_llorar_facilmente', 'e4_perdida_sexual', 'e5_poco_apetito',
                  'e6_dificultad_dormir', 'e7_sentir_sin_esperanza', 'e8_sentirse_triste', 'e9_sentirse_sola',
                  'e10_pensar_acabar_vida', 'e11_sentirse_atrapada', 'e12_preocuparse_demasiado', 'e13_no_sentir_interes',
                  'e14_sentir_todo_cuesta', 'e15_sentir_no_valer', 'f_evento1', 'f_evento2', 'f_evento3', 'f_evento4',
                  'f_evento5', 'f1_recuerdos_dolorosos', 'f2_ocurrir_de_nuevo', 'f3_suenos_desagradables',
                  'f4_sentirse_distante', 'f5_sentir_incapaz_amar', 'f6_saltar_susto', 'f7_dificultad_concentrarse',
                  'f8_dificultad_dormir', 'f9_sentirse_alerta', 'f10_sentirse_irritable', 'f11_evadir_situaciones',
                  'f12_problemas_recordando', 'f13_perder_interes', 'f14_sentirse_sin_futuro', 'f15_intentar_no_pensar',
                  'f16_reacciones_fisicas', 'f17_sentir_culpa', 'f_numero_evento',  'h1_sentirse_desamparada',
                  'g1_beber_menos', 'g2_criticar_beber', 'g3_culpable_beber', 'g4_beber_manana', 'g5_reducir_juego',
                  'g6_ocultar_juego', 'g7_problemas_juego', 'g8_impulsado_juego', 'g9_menos_drogas', 'g10_niega_drogas',
                  'g11_problema_psicologico_drogas', 'g12_impulsado_drogas', 'g13_vomito_evitar_engordar',
                  'g14_perder_control_comida', 'g15_creer_gordo', 'g16_obsesionado_comida', 'g17_tiempo_internet',
                  'g18_quejas_internet', 'g19_alejar_internet', 'g20_controlar_internet', 'g21_tiempo_videojuegos',
                  'g22_quejar_videojuegos', 'g23_dias_sin_videojuegos', 'g24_reducir_tiempo_videojuegos',
                  'g25_impulso_comprar', 'g26_problemas_gastos', 'g27_problemas_credito', 'g28_reducir_gastos',
                  'g29_sexo_impedir_obligaciones', 'g30_quejas_actividad_sexual', 'g31_excesiva_actividad_sexual',
                  'g32_moderar_actividad_sexual', 'h2_ser_abandonada_pareja', 'h3_deslumbrar_pareja',
                  'h4_centro_atencion_pareja', 'h5_necesitar_afecto', 'h6_angustia_enojo',
                  'h7_aungustia_ausencia_pareja', 'h8_preocupacion_discucion_pareja',
                  'h9_hacerse_dano_por_pareja', 'h10_persona_debil_necesitada', 'h11_necesidad_expresividad_pareja',
                  'h12_ser_persona_especial', 'h13_vacia_tras_discusion', 'h14_sentirse_mal_sin_afecto',
                  'h15_temor_por_abandono', 'h16_dejar_todo_por_pareja', 'h17_intranquila_paradero_pareja',
                  'h18_vacia_sola', 'h19_intolerancia_soledad', 'h20_cosas_temerarias_por_amor',
                  'h21_cambiar_planes_por_pareja', 'h22_alejar_amigos_por_pareja', 'h23_diversion_pareja',
                  'i1_dificil_esperar_cola', 'i2_cosas_impulsivas', 'i3_dinero_impulsivo', 'i4_planear_anticipacion',
                  'i5_perder_paciencia', 'i6_facil_concentrarse', 'i7_impulsos_sexuales', 'i8_decir_primero_cabeza',
                  'i9_comer_sin_hambre', 'i10_impulsivo', 'i11_terminar_cosas_empieza', 'i12_dificil_control_emociones',
                  'i13_distraerse_facilmente', 'i14_dificil_quieto', 'i15_cauteloso', 'j1_dolor_cabeza',
                  'j2_mal_apetito', 'j3_mal_dormir', 'j4_facil_susto', 'j5_temblor_manos', 'j6_nervios_sin_causa',
                  'j7_tensa_sin_causa', 'j8_aburrida', 'j9_mala_digestion', 'j10_no_pensar_claro', 'j11_triste',
                  'j12_no_disfrutar_diario', 'j13_no_disfrutar_trabajo', 'j14_dicultad_decisiones', 'j15_acabar_vida',
                  'j16_cansada_sin_razon', 'j17_sensacion_estomago', 'j18_dificultad_diario', 'j19_tratado_herirla',
                  'j20_controlar_pensamientos', 'j21_escuchar_voces', 'j22_tener_convulsiones',
                  'j23_llora_frecuentemente', 'j24_util_vida', 'j25_perdidad_interes', 'j26_persona_inutil',
                  'j27_persona_importante', 'opinion_dificultad_proceso', 'opinion_atencion_terapia')

    widgets = {
        "opinion_dificultad_proceso": forms.Textarea,
        "opinion_atencion_terapia": forms.Textarea
    }
