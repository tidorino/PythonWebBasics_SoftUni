from django import forms

from car_collection_app.web.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password',)


class CreateCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class EditCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    disabled_fields = ['type', 'model', 'year', 'image_url', 'price',]

    def __init__(self, *args, **kwargs):
        super(DeleteCarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for field in self.disabled_fields:
                self.fields[field].disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ProfileDeleteForm(forms.ModelForm):
    def __int__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    class Meta:
        model = Profile
        fields = ()
