from django import forms

class CSVUploadForm(forms.Form):
    source_file = forms.FileField(label='Source CSV')
    target_file = forms.FileField(label='Target CSV')
