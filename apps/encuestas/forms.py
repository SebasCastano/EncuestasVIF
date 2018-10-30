from .models import DatosMujeres
from django_select2.forms import Select2Widget
from django import forms


class AgregarEncuestaMujerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AgregarEncuestaMujerForm, self).__init__(*args, **kwargs)

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
                  'j43_usar_objeto_sexual',
                  )
