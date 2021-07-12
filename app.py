
from flask import Flask, render_template, url_for,request,redirect
app = Flask(__name__)
import requests
from datetime import datetime

key = 'fe5cb81842cf4c3d9dd40103212303'
def get_json(city):
    url = f'https://api.weatherapi.com/v1/current.json?key=fe5cb81842cf4c3d9dd40103212303&q={city}&aqi=no'
    return requests.get(url).json()
class FormatTime():
    def __init__(self,json):
        self.json = json

    def updated_time(self):
        datetime_str = self.json['current']['last_updated'][2:]
        self.datetime_object = datetime.strptime(datetime_str,'%y-%m-%d %H:%M')
        return self.datetime_object.strftime('%I:%M %p')
    def local_time(self):
        local_datetime_str = self.json['location']['localtime'][2:]
        local_datetime_object = datetime.strptime(local_datetime_str,'%y-%m-%d %H:%M')
        return local_datetime_object
    def current_date(self):
        return self.local_time().strftime('%d %B %Y')
    def current_time(self):
        return self.local_time().strftime('%I:%M %p %A')





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/search", methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
      city = request.form['city']
      print(city)
      return redirect(url_for('result',city = city))
   return render_template('search.html')


@app.route("/result")
def result():
   if request.method == 'POST':
      city = request.form['city']
      return redirect(url_for('result',city = city))  

   json = get_json(request.args.get('city'))
   if json['error']:
       

    url =  'http:'+ json['current']['condition']['icon']
    ft = FormatTime(json)
    updated_time = ft.updated_time()
    local_time = ft.current_time()
    local_date = ft.current_date()

   return render_template('result.html', json = json,icon_url = url,
   updated_time = updated_time,local_time = local_time,local_date = local_date)

@app.route("/error")
def error():
    return render_template('404error.html')



if __name__ == '__main__':
    app.run(debug=True)