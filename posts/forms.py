from django import forms


class PostForm(forms.Form):
    
    body = forms.CharField(
        max_length=2000,
        widget=forms.Textarea()
    )
    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        post = cleaned_data.get('body')