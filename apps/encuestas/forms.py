from .models import DatosMujeres
from django_select2.forms import Select2Widget
from django import forms


class AgregarEncuestaMujerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AgregarEncuestaMujerForm, self).__init__(*args, **kwargs)

        self.fields['a4_edad'].widget.attrs['placeholder'] = "Edad en años cumplidos"
        self.fields['a7_escolaridad'].widget.attrs['label'] = "Escolaridad (Nivel educativo culminado completamente)"

    class Meta:
        model = DatosMujeres
        fields = ('hora_inicio', 'hora_final','fecha_encuesta', 'id_paciente', 'id_encuestador', 'medicion', 'institucion_salud',
                  'servicio_remitente', 'a1_ciudad', 'a2_barrio', 'a3_direccion', 'a4_edad', 'a5_estado_civil', 'a6_situacion_sentimental', 'a7_escolaridad',
                  'a8_discapacidad', 'a8a_tipo_discapacidad', 'a9_situacion_laboral')

    widgets = {
        "medicion": Select2Widget(),
        "institucion_salud": Select2Widget(),
        "a1_ciudad": Select2Widget(),
        "a5_estado_civil": Select2Widget(),
        "a6_situacion_sentimental": Select2Widget(),
        "a7_escolaridad": Select2Widget(),
        "a8_discapacidad": Select2Widget(),
        "a8a_tipo_discapacidad": Select2Widget(),
        "a9_situacion_laboral": Select2Widget()
    }
