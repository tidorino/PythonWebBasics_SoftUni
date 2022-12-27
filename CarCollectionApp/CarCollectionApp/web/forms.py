from django import forms

from CarCollectionApp.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password',)

    labels = {
        'username': 'Username',
        'email': 'Email',
        'age': 'Age',
        'password': 'Password',
    }


class EdiProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeleteCarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['type'].widget.attrs['readonly'] = True
            self.fields['model'].widget.attrs['readonly'] = True
            self.fields['year'].widget.attrs['readonly'] = True
            self.fields['image_url'].widget.attrs['readonly'] = True
            self.fields['price'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }

