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
                  'h16_reacciones_fisicas', 'h17_sentir_culpa', 'h_numero_evento')
