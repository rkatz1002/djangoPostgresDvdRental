from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from staff.models import *

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=45, label="first name")
    last_name = forms.CharField(max_length=45, label="last name")
    email = forms.CharField(max_length=50, label='email')

    class Meta:
        model = Staff
        fields = ('username', 'password','first_name','email','last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'email')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('first_name',)
    ordering = ('first_name',)
    filter_horizontal = ()
    
admin.site.register(Staff, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)