"""
flask App development

"""
from flask import Flask,render_template,request
import sklearn
app = Flask(__name__)
import pickle
model = pickle.load(open("liver_prediction.pkl","rb"))

@app.route("/")
def index():
    return render_template("page.html")
@app.route('/index', methods = ['POST','GET'])
def index1():
    if request.method =='POST':
        AGE =float(request.form['AGE'])
        Gender =float(request.form['Gender'])
        Place = float( request.form["Place(location where the patient lives)"])
        Duration_of_alcohol_consumption = float(request.form["Duration of alcohol consumption(years)"])
        Quantity_of_alcohol_consumption  = float( request.form["Quantity of alcohol consumption (quarters/day)"])
        
        Type_of_alcohol_consumed = float(request.form["Type of alcohol consumed"])
        Blood_pressure = float(request.form["Blood pressure (mmhg)"])
        Obesity = float(request.form["Obesity"])
        Family_history_of_cirrhosis_hereditary =float( request.form["Family history of cirrhosis/ hereditary"])
        
        Hemoglobin = float(request.form["Hemoglobin  (g/dl)"])
        PCV = float(request.form["PCV  (%)"])
        RBC = float(request.form["RBC  (million cells/microliter)"])
        MCV = float(request.form["MCV   (femtoliters/cell)"])
        MCH = float(request.form["MCH  (picograms/cell)"])
        MCHC = float(request.form["MCHC  (grams/deciliter)"])
        Total_Count = float(request.form["Total Count"])
        Polymorphs = float(request.form["Polymorphs  (%)"])
        Lymphocytes = float(request.form["Lymphocytes  (%)"])
        Monocytes = float(request.form["Monocytes   (%)"])
        Eosinophils = float(request.form["Eosinophils   (%)"])
        Basophils  = float(request.form["Basophils  (%)"])
        Platelet_Count  = float(request.form["Platelet Count  (lakhs/mm)"])
        Direct  = float(request.form["Direct    (mg/dl)"])
        Indirect = float(request.form["Indirect     (mg/dl)"])
        Total_Protein  = float(request.form["Total Protein     (g/dl)"])
        Albumin = float(request.form["Albumin   (g/dl)"])
        Globulin = float(request.form["Globulin  (g/dl)"])
        
        AL_Phosphatase = float(request.form["AL.Phosphatase      (U/L)"])
        SGOT_AST = float(request.form["SGOT/AST      (U/L)"])
        USG_Abdomen = float(request.form["USG Abdomen (diffuse liver or  not)"])
        Outcome = float(request.form["Outcome"])
        data = [[AGE,Gender,Place,Duration_of_alcohol_consumption,Quantity_of_alcohol_consumption,Type_of_alcohol_consumed,Blood_pressure,Obesity,Family_history_of_cirrhosis_hereditary,Hemoglobin,PCV,RBC,MCV,MCH,MCHC,Total_Count,Polymorphs,Lymphocytes,Monocytes,Eosinophils,Basophils,Platelet_Count,Direct,Indirect,Total_Protein,Albumin,Globulin,AL_Phosphatase,SGOT_AST,USG_Abdomen,Outcome]]
        prediction = model.predict(data)
        prediction = int(prediction[0])
        if prediction==0:
            return render_template("index.html",prediction="'Non-Diabetes'     Your liver is healthy enough and No need to worry Consume healthy food with balanced diet and take care")
        
        else:
            return render_template("index.html",prediction="'Diabetes'        You are consult the docter and follow the instructions strictly Taking vitamins, Exercising, losing weight and medicines prescribed by your health care provider avoid consumption of food that affects the liver (like alcohol, Added sugar, fried foods,salt..)Avoid risky behavior and Get vaccinated")
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run(debug = True)