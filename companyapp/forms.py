from django.forms import ModelForm
from django import forms

from .models import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address"]


class PicUploadform(forms.ModelForm):
    class Meta:
        model = Picupload
        fields = ["picupload", "picupload_owner"]


# # class AddressForm(forms.Form):
# #     class Meta:
# #         model = Address
# #         fields = ["address"]
#
# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['address']

# class CompanyForm(forms.ModelForm):
#     address=forms.ModelChoiceField(queryset=Address.objects.all())
#     class Meta:
#         model=Company
#         fields=["address"]
#
#     def __init__(self,*args,**kwargs):
#         if kwargs.get("instance"):
#             initial=kwargs.setdefault('initial',{})
#             if kwargs['instance'].group.all():
#                 initial['address']=kwargs['instance'].group.all()[0]
#             else:
#                 initial['role']=None
#         forms.ModelForm.__init__(self,*args,**kwargs)
#
#     def save(self):
#         address=self.cleaned_data.pop('address')
#         u=super().save()
#         u.address.set([address])
#         u.save()
#         return u
