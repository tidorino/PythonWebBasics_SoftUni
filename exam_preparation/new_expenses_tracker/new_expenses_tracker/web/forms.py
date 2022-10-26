import os

from django import forms

from new_expenses_tracker.web.models import Profile, Expense


class NoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price',)
        labels = {
            'title': 'Title',
            'description': 'Description',
            'expense_image': 'Link to Image',
            'price': 'Price',
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price',)
        labels = {
            'title': 'Title',
            'description': 'Description',
            'expense_image': 'Link to Image',
            'price': 'Price',
        }


class DeleteExpenseForm(forms.ModelForm):
    def __int__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disable'] = 'disable'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price',)
        labels = {
            'title': 'Title',
            'description': 'Description',
            'expense_image': 'Link to Image',
            'price': 'Price',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        if commit:
            self.instance.delete()
            Expense.objects.all().delete()
            os.remove(image_path)

        return self.instance
