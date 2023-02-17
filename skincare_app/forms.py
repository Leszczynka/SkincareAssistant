from django import forms

SKIN_TYPES = (
    ('', 'all'),
    ('combination', 'combination'),
    ('dry', 'dry'),
    ('normal', 'normal'),
    ('oily', 'oily'),
    ('sensitive', 'sensitive')
)


class SearchProductsForm(forms.Form):
    product_category = forms.CharField(max_length=100)
    skin_type = forms.ChoiceField(choices=SKIN_TYPES, required=False)



