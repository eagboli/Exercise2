from flask import Flask, render_template, request
import urllib.request
import json

app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/edu')
def edu():
  return render_template("edu.html")

@app.route('/exp')
def exp():
  return render_template("exp.html")

@app.route('/skills')
def skills():
  return render_template("skills.html")

@app.route('/vol')
def vol():
  return render_template("vol.html")

@app.route('/ref')
def ref():
  return render_template("ref.html")

@app.route('/weather')
def weather():
  city='sudbury'
  key='bc448800d4c0db057fde7aafc4a36d6d'
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
  request = urllib.request.urlopen(url)
  result=json.loads(request.read())
  temp_c=result["main"]["temp"]
  return render_template("weather.html",temp_c=temp_c)


@app.route('/bmi', methods = ['POST', 'GET'])
def bmi():
  
  height=0
  weight = 0
  bmi = 0
  if request.method == 'POST' and 'userweight' and 'userheight' in request.form:
    #user interaction to get an input
    height = request.form.get('userheight')
    weight = request.form.get('userweight')
    #BMI calculation
    bmi = int(weight) / (int(height)/100) ** 2

  def log_bmi():
    data = {'height': height, 'weight': weight, 'bmi': bmi}
    try:
      with open('bmi.txt', "a") as file:
        file.write(str(data))
    except FileNotFoundError:
      with open('bmi.txt', "w") as file:
        file.write(str(data))
      
  log_bmi()
  
  return render_template("bmi.html", height = height, weight=weight, bmi=round(bmi,2))


@app.route('/iss')
def iss():
  return render_template("iss.html")



 
app.run(host='0.0.0.0', port=8080)