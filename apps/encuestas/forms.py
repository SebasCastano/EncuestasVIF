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



    class Meta:
        model = DatosMujeres
        fields = ('hora_inicio', 'hora_final','fecha_encuesta', 'id_paciente', 'id_encuestador', 'medicion', 'institucion_salud',
                  'servicio_remitente', 'a1_ciudad', 'a2_barrio', 'a3_direccion', 'a4_edad', 'a5_estado_civil', 'a6_situacion_sentimental', 'a7_escolaridad',
                  'a8_discapacidad', 'a8a_tipo_discapacidad', 'a9_situacion_laboral', 'a10_consume_cigarrillo', 'a11_consume_alcohol', 'a12_consume_tipo_sustancia',
                  'a12a_tipo_sustancia', 'a12b_otro_tipo_sustancia', 'b1_num_personas_hogar', 'b2_esposo', 'b2_companero', 'b2_hijos', 'b2_sobrinos', 'b2_primos',
                  'b2_suegros', 'b2_ex_esposo', 'b2_ex_companero', 'b2_tios', 'b2_hermanos', 'b2_abuelos', 'b2_conocidos', 'b2_otro', 'b2_otro_especificado')

    widgets = {
        "medicion": Select2Widget(),
        "institucion_salud": Select2Widget(),
        "a1_ciudad": Select2Widget(),
        "a5_estado_civil": Select2Widget(),
        "a6_situacion_sentimental": Select2Widget(),
        "a7_escolaridad": Select2Widget(),
        "a8_discapacidad": Select2Widget(),
        "a8a_tipo_discapacidad": Select2Widget(),
        "a9_situacion_laboral": Select2Widget(),
        "a10_consume_cigarrillo": Select2Widget(),
        "a11_consume_alcohol": Select2Widget(),
        "a12_consume_tipo_sustancia": Select2Widget(),
        "a12a_tipo_sustancia": Select2Widget(),
        "a12b_otro_tipo_sustancia": Select2Widget()
    }
