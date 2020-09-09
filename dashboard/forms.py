from django import forms

from .models import Product,  Colours, Supplier



class ProductForm(forms.ModelForm):
    code = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Your Description"}))
    quantity = forms.IntegerField(initial='1')
    minquantity = forms.IntegerField(initial='50')
    colour = forms.SelectMultiple()

    class Meta:
        model = Product
        fields = [
            'code',
            'description',
            'supplier',
            'quantity',
            'minquantity',
            'colour'
        ]

    def clean_title(self, *args, **kwargs):
        code = self.cleaned_data.get("code")
        if not "SAPA" in code:
            raise forms.ValidationError("this is not valid code")
        else:
            return code


class ProductBacklogForm(forms.Form):
    class Meta:
        model = ProductForm
        fields = [
            'products',
            'modified'
        ]


class RawProductForm(forms.Form):
    code = forms.CharField()
    description = forms.CharField()
    quantity = forms.IntegerField()
    minquantity = forms.IntegerField()


class EditProductForm(forms.ModelForm):
    # modifiedby = models.user

    class Meta:
        model = Product
        fields = [
            'quantity'
        ]


class AddColorsForm(forms.ModelForm):
    class Meta:
        model = Colours
        fields = [
            'colour',
            'description',
            'colourcode'
        ]


class ColoursForm(forms.ModelForm):
    colour = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Your Description"}))
    colourcode = forms.CharField()

    class Meta:
        model = Colours
        fields = [
            'colour',
            'description',
            'colourcode'
        ]

    def clean_title(self, *args, **kwargs):
        colourcode = self.cleaned_data.get("colourcode")
        if not "RAL" in colourcode:
            raise forms.ValidationError("this is not valid code")
        else:
            return colourcode


class SupplierForm(forms.ModelForm):
    supplier = forms.CharField()

    class Meta:
        model = Supplier
        fields = [
            'supplier'
        ]
