from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'some_class', 'id':'some_id'}))
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)