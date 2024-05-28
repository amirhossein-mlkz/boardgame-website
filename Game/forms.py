from typing import Any
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from . models import Game

PERSIAN_MESSAGES = {
    'required': 'این فیلد ضروری است',
    'max_length': 'تعداد کارکترها بیش از حد مجاز است',
    'min_length': 'تعداد کارکترها کمتر از حد مجاز است',

}



class creatGameForm(forms.Form):
    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        error_messages=PERSIAN_MESSAGES,
        widget=forms.PasswordInput(),
    )

    password2 = forms.CharField(
        label='تکرار رمز عبور',
        error_messages=PERSIAN_MESSAGES,
        widget=forms.PasswordInput(),
        strip=False,

    )




    def clean_password1(self) -> dict[str, Any]:
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 4:
            raise ValidationError(_('رمز عبور باید حداقل شامل چهار کارکتر باشد'))
        return password1
    
    def clean(self,):
        cleaned_data = super().clean()
        password2 = cleaned_data.get('password2')
        password1 = cleaned_data.get('password1')

        if password1 and password2 and password2 != password1:
            #raise ValidationError(_('رمز عبور با تکرار آن مطابقت ندارد'))
            self.add_error('password2', ValidationError(_('رمز عبور با تکرار آن مطابقت ندارد')))
        
        return cleaned_data
