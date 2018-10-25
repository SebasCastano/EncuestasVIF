from .models import DatosMujeres
from django_select2.forms import Select2Widget
from django import forms


class AgregarEncuestaMujerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AgregarEncuestaMujerForm, self).__init__(*args, **kwargs)

        self.fields['a4_edad'].widget.attrs['placeholder'] = "Edad en años cumplidos"
        self.fields['b2_otro_especificado'].widget.attrs['placeholder'] = "Espeficique si marcó 'otro'"
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


    class Meta:
        model = DatosMujeres
        fields = ('hora_inicio', 'hora_final','fecha_encuesta', 'id_paciente', 'id_encuestador', 'medicion', 'institucion_salud',
                  'servicio_remitente', 'a1_ciudad', 'a2_barrio', 'a3_direccion', 'a4_edad', 'a5_estado_civil', 'a6_situacion_sentimental', 'a7_escolaridad',
                  'a8_discapacidad', 'a8a_tipo_discapacidad', 'a9_situacion_laboral', 'a10_consume_cigarrillo', 'a11_consume_alcohol', 'a12_consume_tipo_sustancia',
                  'a12a_tipo_sustancia', 'a12b_otro_tipo_sustancia', 'b1_num_personas_hogar', 'b2_esposo', 'b2_companero', 'b2_hijos', 'b2_sobrinos', 'b2_primos',
                  'b2_suegros', 'b2_ex_esposo', 'b2_ex_companero', 'b2_tios', 'b2_hermanos', 'b2_abuelos', 'b2_conocidos', 'b2_otro', 'b2_otro_especificado',
                  'b3_num_personas_aportan_hogar', 'b4_num_personas_dependen_dentro', 'b4_num_personas_dependen_fuera', 'b5_tipo_de_vivienda', 'b6_regimen_salud',
                  'b6_otro_especificado', 'c1_relacion_agresor', 'c1_otro_especificado', 'd1_sentir_susto', 'd2_sentir_miedo', 'd3_sentir_desmayo', 'd4_sentir_nervios',
                  'd5_sentir_corazon', 'd6_sentir_tembladera', 'd7_sentir_tension', 'd8_dolor_cabeza', 'd9_sentir_terror', 'd10_sentir_agitada',)
