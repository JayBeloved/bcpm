from django import forms

# Create input form
class predictor_form(forms.Form):
    radius_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Radius Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    texture_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Texture Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    smoothness_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Smoothness Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    compactness_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Compactness Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    symmetry_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Symmetry Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    fractal_dimension_mean = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Fractal Dimension Mean ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    radius_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Radiues SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    texture_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Texture SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    smoothness_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Smoothness SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))
    
    compactness_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Compactness SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    symmetry_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Symmetry SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))

    fractal_dimension_se = forms.FloatField(
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': " Fractal Dimension SE ",
            'style': "border-radius: 10rem;padding: 0.5rem 0.5rem;",
        }
    ))



    