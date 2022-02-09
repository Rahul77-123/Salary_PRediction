from flask import Flask, request
import pickle

# load the model from pickle file
file = open('./salary_model.pkl', 'rb')
model = pickle.load(file)
file.close()


# Route Table
# -----------------------------------------------
#   method  |   path        |       function
# -----------------------------------------------
#   GET     |   /           |   root()
#   GET     |   /predict    |   predict_salary()
# -----------------------------------------------


# create a server
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <h1>Salary Prediction</h1>
        <form method="POST" action="/predict">
            Experience <input name="experience" type="text" >
            <button>Predict Salary</button>
        </form>
    """


@app.route("/predict", methods=["POST"])
def predict_salary():
    # value is in str so convert it into float
    experience = float(request.form.get("experience"))
    print(f"experience = {experience}, type = {type(experience)}")

    salaries = model.predict([[experience]])
    print(salaries)

    return f"<h1>Your experience  {experience} yrs, Salary = {salaries[0]}</h1>"


# run the server
app.run(port=5002)
