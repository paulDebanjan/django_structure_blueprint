from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
        return user