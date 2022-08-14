from django import forms

class CreatePollItem(forms.Form):
    title = forms.CharField(
        max_length=200,
        initial="",
        widget=forms.TextInput(attrs={
            'class': "form-control create-form",
            'placeholder': 'Enter a title'
        }),
        label = '',
    )

