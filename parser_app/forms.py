from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOISES = (

        ('FILMS.KG'), ('FILMS.KG'),

    )

    media_type = forms.CharField(choices=MEDIA_CHOISES)

    class Meta:
        field = [

        'media_type',

        ]

    def parser_data(self):
        if self.data['media_type'] == 'FILMS.KG':
            film_parser = parser.parser()
            for i in film_parser:
                models.TvParser.objects.create(**i)