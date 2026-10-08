from django import forms

from .models import UserName


class UserNameForm(forms.ModelForm):

    class Meta:

        model = UserName

        fields = ["name"]


    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if not name:

            raise forms.ValidationError(
                "Введите имя."
            )

        return name
