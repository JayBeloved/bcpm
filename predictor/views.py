import joblib, os
import pandas as pd
from django.shortcuts import render, HttpResponseRedirect
from .forms import predictor_form

# Create your views here.
def landing(request):
    return HttpResponseRedirect('model/landing')

def index(request):

    # The names of the features used by the model for prediction.
    feature_names = [ 
        'Id',
        'Radius Mean',
        'Texture Mean',
        'Smoothness Mean',
        'Compactness Mean',
        'Symmetry Mean',
        'Fractal Dimension Mean',
        'Radius SE',
        'Texture SE',
        'Smoothness SE',
        'compactness_se',
        'Symmetry SE',
        'Fractal Dimension SE'
    ]

    # Get form
    form = predictor_form(request.POST or None)
    
    # Check if request is post
    if request.method == 'POST':
        # Get user input
        if form.is_valid():
            id = 1
            radius_mean = form.cleaned_data.get("radius_mean")
            texture_mean = form.cleaned_data.get("texture_mean")
            smoothness_mean = form.cleaned_data.get("smoothness_mean")
            compactness_mean = form.cleaned_data.get("compactness_mean")
            symmetry_mean = form.cleaned_data.get("symmetry_mean")
            fractal_dimension_mean = form.cleaned_data.get("fractal_dimension_mean")
            radius_se = form.cleaned_data.get("radius_se")
            texture_se = form.cleaned_data.get("texture_se")
            smoothness_se = form.cleaned_data.get("smoothness_se")
            compactness_se = form.cleaned_data.get("compactness_se")
            symmetry_se = form.cleaned_data.get("symmetry_se")
            fractal_dimension_se = form.cleaned_data.get("fractal_dimension_se")

            # Prepare the input data in the format expected by the model
            input_data = [[id, radius_mean, texture_mean, smoothness_mean, compactness_mean,
                        symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
                        smoothness_se, compactness_se, symmetry_se, fractal_dimension_se]]
            
            # Get the absolute file path to the knn.joblib file
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models\knn.joblib")
            model = joblib.load(file_path)

            # Run Prediction
            prediction = model.predict(input_data)

            # Create a dictionary for features
            features = pd.DataFrame({'name': feature_names, 'value': list(input_data[0]) })
            # Convert Dataframe to html table
            # Convert the DataFrame to an HTML table
            html_table = features.to_html(classes="table table-outline table-hover", index=False, header=False)

            # Return Results
            return render(request, 'predictor/result.html', {'prediction': prediction[0], 'table': html_table})

    # View Context
    context = {
        'features': feature_names,
        'form': form,
    }

    return render(request, 'predictor/landing.html', context)