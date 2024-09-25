from flask import Flask, request, render_template, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

# Create Flask app
app = Flask(__name__)

# Dummy data for training
X = np.array([[3, 2, 1500], [2, 1, 1200], [4, 3, 2500], [3, 2, 1800], [5, 4, 3000]])
y = np.array([400000, 350000, 650000, 450000, 750000])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Home route to display the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and return the predicted price
@app.route('/predict', methods=['POST'])
def predict():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    sqft = int(request.form['sqft'])

    # Make prediction
    prediction = model.predict(np.array([[bedrooms, bathrooms, sqft]]))
    
    # Return the predicted price to the HTML page
    return render_template('index.html', predicted_price=round(prediction[0], 2))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
