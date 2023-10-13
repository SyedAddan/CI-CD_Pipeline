from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('iris_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def classify_iris():
    result = ''
    
    if request.method == 'POST':
        try:
            # Get user input from the form
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            # Make a prediction using the loaded model
            input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            prediction = model.predict(input_data)[0]

            # Map the numeric prediction to Iris species
            iris_species = ['Setosa', 'Versicolor', 'Virginica']
            result = f'The predicted Iris species is {iris_species[prediction]}'
        except ValueError:
            result = 'Invalid input. Please enter valid numeric values.'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=4000)
