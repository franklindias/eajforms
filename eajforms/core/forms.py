from django import forms

class MatriculationsUploadFileForm(forms.Form):
    file = forms.FileField(
        label='Arquivo para importação',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'data-multiple-caption': '{count} files selected'
        })
    )


class DocentesUploadFileForm(forms.Form):
    file = forms.FileField(
        label='Arquivo para importação',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'data-multiple-caption': '{count} files selected'
        })
    )