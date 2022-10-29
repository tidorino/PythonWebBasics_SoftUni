from django import forms

from my_music_app.web.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age',)
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'User name',
                       'type': 'text',
                       }
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email', }
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
        }
        labels = {
            'username': 'User name',
            'email': 'Email',
            'age': 'Age',
        }


class AddAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name',
                       'type': 'text',
                       }
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist', }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', }
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Image URL', }
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price', }
            ),
        }
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class EditAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __int__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.required = False

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class ProfileDeleteForm(forms.ModelForm):
    def __int__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    class Meta:
        model = Profile
        fields = ()
