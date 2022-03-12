from flask import Flask, render_template, request
from numpy import float64, int64
import pandas as pd
import pickle


app = Flask(__name__)


model = pickle.load(open('model_save/model.pkl', 'rb'))

# input = pd.read_csv('user_input.csv')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    sqft_living = request.form.get('sqft_living')
    sqft_lot = request.form.get('sqft_lot')
    floors = request.form.get('floors')
    waterfront = 0
    view = request.form.get('view')
    condition = request.form.get('condition')
    grade = request.form.get('grade')
    sqft_above = request.form.get('sqft_above')
    sqft_basement = request.form.get('sqft_basement')
    yr_built = request.form.get('yr_built')
    yr_renovated = 0
    zipcode = request.form.get('zipcode')
    lat = 0
    long = 0
    sqft_living15 = 0
    sqft_lot15 = 0

    try:
        input1 = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront , view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15]], columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15'], dtype=float64)

        pred = model.predict(input1)[0].round(2)

        return str(pred)

    except:
        return "Please enter valid data"



if __name__ == '__main__':
    app.run(debug=False, port=5000)