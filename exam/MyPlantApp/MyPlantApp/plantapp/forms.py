from django import forms

from MyPlantApp.plantapp.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class CreatPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'type': 'Type',
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'price': 'Price',
        }


class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'type': 'Type',
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'price': 'Price',
        }


class DeletePlantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeletePlantForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['type'].widget.attrs['readonly'] = True
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['image_url'].widget.attrs['readonly'] = True
            self.fields['description'].widget.attrs['readonly'] = True
            self.fields['price'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'type': 'Type',
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'price': 'Price',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance


