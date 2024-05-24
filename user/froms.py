from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .models import User


PERSIAN_MESSAGES = {
    'required': 'این فیلد ضروری است',
    'max_length': 'تعداد کارکترها بیش از حد مجاز است',
    'min_length': 'تعداد کارکترها کمتر از حد مجاز است',

}

class UserLoginForm(AuthenticationForm):
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره همراه'})
    # )

    username = forms.CharField(
        label='شماره همراه',
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'شماره همراه'})
    )
    password = forms.CharField(
        label='رمز',
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'رمز عبور'})
    )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'lastname', 'firstname']
        labels = {
            'phone_number':'شماره همراه',
            'lastname':'نام خانوادگی',
            'firstname':'نام'
        }

        error_messages = {
            'lastname':PERSIAN_MESSAGES,
            'firstname':PERSIAN_MESSAGES,
            'phone_number':PERSIAN_MESSAGES

        }
    
    #custom extra validation for phone_number field. methos name should be clean__{fiedname}
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try :
            int(phone_number)
        except:
            raise ValidationError(_("شماره موبایل معتبر نیست"))
        return phone_number
    






class CustomPasswordChangeForm(PasswordChangeForm):



    def __init__(self, user: User, *args: Any, **kwargs: Any) -> None:
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].label = 'رمز عبور فعلی'
        self.fields['new_password1'].label = 'رمز عبور جدید'
        self.fields['new_password2'].label = 'تکرار رمز عبور جدید'


    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')


        if not old_password or not new_password1 or not new_password2:
            raise forms.ValidationError(_('وارد کردن همه فیلدها ضروری است'))
        
        return cleaned_data


        # if old_password and not self.user.check_password(old_password):
        #     raise forms.ValidationError(_('رمز عبور فعلی نادرست است'))
        
        # if new_password1 and new_password2 and new_password1!=new_password2:
        #     raise forms.ValidationError(_('پسورد جدید با تکرار آن مطابقت ندارد'))
        
        
        # return cleaned_data



# # class CustomPasswordChangeForm(PasswordChangeForm):

#     old_password = forms.CharField(
#         label='رمز عبور فعلی',
#         widget=forms.PasswordInput(attrs={'class': 'input100'})
#     )

#     new_password1 = forms.CharField(
#         label='رمز عبور جدید',
#         widget=forms.PasswordInput(attrs={'class': 'input100'})
#     )

#     new_password2 = forms.CharField(
#         label='تکرار رمز عبور جدید',
#         widget=forms.PasswordInput(attrs={'class': 'input100'})
#     )
