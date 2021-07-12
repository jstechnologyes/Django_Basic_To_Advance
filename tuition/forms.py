from django import forms
from .models import Contact,Post


class ContactForm(forms.ModelForm):


    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your phone number'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Say Something','rows':5}),

        }
        labels={
            'name':'Your Name',
            'phone':'Your phone number',
            'content':'Your Content'
        }
        # help_texts={
        #     'name': 'Your Name',
        #     'phone': 'Your phone number',
        #     'content': 'Your Content'
        # }

class ContactFormtwo(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','created_ad','slug']
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
        }

