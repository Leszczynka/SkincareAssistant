from django import forms
from skincare_app.models import Product


CATEGORIES = (
    ('', '---------'),
    ('Face Wash & Cleansers', 'Face Wash & Cleansers'),
    ('Makeup Removers', 'Makeup Removers'),
    ('Toners', 'Toners'),
    ('Moisturizers', 'Moisturizers'),
    ('Night Creams', 'Night Creams'),
    ('Face Serums', 'Face Serums',),
    ('Facial Peels', 'Facial Peels'),
    ('Face Oils', 'Face Oils'),
    ('Face Masks', 'Face Masks'),
    ('Face Sunscreen', 'Face Sunscreen'),
)


class SearchProductForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=False)
    brand = forms.ChoiceField(choices=[], required=False)
    category = forms.ChoiceField(choices=CATEGORIES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].choices = Product.objects.values_list('brand', 'brand').distinct().order_by('brand')
        self.fields['brand'].choices.insert(0, ('', '---------'))

    class Meta:
        model = Product
        fields = ['name', 'brand', 'category']





