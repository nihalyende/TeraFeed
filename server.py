import joblib
# loaded_model = joblib.load('gradient_boosting_model.pkl')
from sklearn.preprocessing import StandardScaler

# Step 1: Scale or normalize your features
# scaler = StandardScaler()
loaded_model = joblib.load('Model_Final_27_03.pkl')

# print(loaded_model.predict([[2.01000000e+03,1020662522, 9.21147059e+00, 1.79620294e+01,
#        7.02976471e+00, 7.98700000e+01, 1.93850000e+02, 3.65500000e+02]]))


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input values from the form
        # year = int(request.form['year'])
        population = float(request.form['population'])
        # unemployment_above_15 = float(request.form['unemployment_above_15'])
        unemployment_between_15_24 = float(request.form['unemployment_between_15_24'])
        unemployment_above_25 = float(request.form['unemployment_above_25'])
        share_of_agricultural_land = float(request.form['share_of_agricultural_land'])
        people_employed_in_agriculture = float(request.form['people_employed_in_agriculture'])
        total_employment_in_africa = float(request.form['total_employment_in_africa'])
        import_us_thousand = float(request.form['import_us_thousand'])
        export_us_thousand = float(request.form['export_us_thousand'])
        net_official_development_assistance_and_aid = float(request.form['net_official_development_assistance_and_aid'])
        credit_received_from_other_countries_in_billions = float(request.form['credit_received_from_other_countries_in_billions'])
        gasoline = float(request.form['gasoline'])
        
        # Make prediction using your model
        print([[ population, unemployment_between_15_24, unemployment_above_25, share_of_agricultural_land, people_employed_in_agriculture, total_employment_in_africa, import_us_thousand, export_us_thousand, net_official_development_assistance_and_aid, credit_received_from_other_countries_in_billions, gasoline]])
        prediction = loaded_model.predict([[ population, unemployment_between_15_24, unemployment_above_25, share_of_agricultural_land, people_employed_in_agriculture, total_employment_in_africa, import_us_thousand, export_us_thousand, net_official_development_assistance_and_aid, credit_received_from_other_countries_in_billions, gasoline]])
        print("hasdf" ,prediction)
        
        # Return the predicted value as JSON
        return jsonify({'prediction': prediction[0]})
    
    # If it's a GET request, render the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
