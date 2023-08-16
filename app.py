from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if(request.form.get("field1")):
            field1=1
        else: 
            field1=0
        if(request.form.get("field2")):
            field2=1
        else: 
            field2=0
        if(request.form.get("field3")):
            field3=1
        else: 
            field3=0
        if(request.form.get("field4")):
            field4=1
        else: 
            field4=0
        if(request.form.get("field5")):
            field5=1
        else: 
            field5=0
        if(request.form.get("field6")):
            field6=1
        else: 
            field6=0
        if(request.form.get("field7")):
            field7=1
        else: 
            field7=0
        if(request.form.get("field8")):
            field8=1
        else: 
            field8=0
        if(request.form.get("field9")):
            field9=1
        else: 
            field9=0
        if(request.form.get("field10")):
            field10=1
        else: 
            field10=0
        if(request.form.get("field11")):
            field11=1
        else: 
            field11=0
        if(request.form.get("field12")):
            field12=1
        else: 
            field12=0
        if(request.form.get("field13")):
            field13=1
        else: 
            field13=0
        if(request.form.get("field14")):
            field14=1
        else: 
            field14=0
        if(request.form.get("field15")):
            field15=1
        else: 
            field15=0
        if(request.form.get("field16")):
            field16=1
        else: 
            field16=0
        if(request.form.get("field17")):
            field17=1
        else: 
            field17=0
        if(request.form.get("field18")):
            field18=1
        else: 
            field18=0
        pickled_model = pickle.load(open('model', 'rb'))
        x_test = [[field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18]]

        result=pickled_model.predict(x_test)
        return render_template('index.html', result=result)
    return render_template('index.html')




app.run(debug=True)