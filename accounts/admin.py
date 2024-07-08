from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import CustomUser, Site


class UserCreationForm(forms.ModelForm):
    """
    新規ユーザー作成用フォーム
    """
    user_id = forms.IntegerField(
        label='ID',
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = CustomUser
        fields = ('user_id', 'username', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Password don't match."
            )
        return password2

    def save(self, commit=True):
        """
        パスワードをハッシュ化して保存する
        :param commit:
        :return:
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    ユーザー更新用フォーム
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('user_id', 'username', 'is_staff', 'is_active', 'is_superuser', )

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'username', 'is_active', 'is_staff', 'is_superuser', )
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {'fields': ('user_id', 'username', 'password', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('user_id', 'username', 'password1', 'password2', )}),
    )
    search_fields = ('user_id', 'username', )
    ordering = ('user_id', )
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Site)
