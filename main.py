from flask import Flask, render_template, request
import scripts
from flask import jsonify
from datetime import datetime
import pytz
import requests

app = Flask('app')
ip_ban_list = ['']


@app.before_request
def block_method():
  ip = get_ip()
  if ip in ip_ban_list:
    return "Fuck You"


@app.route('/form')
def form():
  return render_template('form.html')


@app.route('/admin')
def admin():
  with open("locations_of_users.txt", "r") as file:
    return file.read()
  #return render_template('form.html')


@app.route('/cresh')
def cresh():
  return render_template('cresh.html')


@app.route('/dirt')
def dirt():
  return render_template('dirt.html')


def write(ip, filename):
  with open(filename, "a") as file:
    #today = date.today()
    #current_time = datetime.now()
    file.write(f"\nip: {ip} - - {datetime.now(pytz.timezone('US/Eastern'))}")
    file.close()
def write_dump(ip, filename):
  with open(filename, "a") as file:
    contents = file.read()
    list = contents.split()
    if ip in list:
      pass
    else: 
      file.write(ip)
      file.close()

@app.route('/geo')
def geo():
  ip_address = get_ip()
  response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
  location_data = {
    "ip": ip_address,
    "city": response.get("city"),
    "region": response.get("region"),
    "country": response.get("country_name"),
    "version": response.get("version"),
    "region_code": response.get("region_code"),
    "country_code": response.get("country_code"),
    "country capital": response.get("country_capital"),
    "country tld": response.get("country_tld"),
    "in eu": response.get("in_eu"),
    "postal": response.get("postal"),
    "latitude": response.get("latitude"),
    "longitude": response.get("longitude"),
    "timezone": response.get("timezone"),
    "utc_offset": response.get("utc_offset"),
    "country calling code": response.get("country_callig_code"),
    "currency name": response.get("currency_name"),
    "country area": response.get("country_area"),
    "country population": response.get("country_population"),
  }
  write(location_data, "location.txt")
  return location_data


def beans():
  ip_address = get_ip()
  response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
  location_data = {
    "ip": ip_address,
    "city": response.get("city"),
    "region": response.get("region"),
    "country": response.get("country_name"),
    "version": response.get("version"),
    "region_code": response.get("region_code"),
    "country_code": response.get("country_code"),
    "country capital": response.get("country_capital"),
    "country tld": response.get("country_tld"),
    "in eu": response.get("in_eu"),
    "postal": response.get("postal"),
    "latitude": response.get("latitude"),
    "longitude": response.get("longitude"),
    "timezone": response.get("timezone"),
    "utc_offset": response.get("utc_offset"),
    "country calling code": response.get("country_callig_code"),
    "currency name": response.get("currency_name"),
    "country area": response.get("country_area"),
    "country population": response.get("country_population"),
  }
  write(location_data, "locations_of_users.txt")
  #return location_data


def beans2():
  ip_address = get_ip()
  response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
  location_data = {
    "ip": ip_address,
    "city": response.get("city"),
    "region": response.get("region"),
    "country": response.get("country_name"),
    "version": response.get("version"),
    "region_code": response.get("region_code"),
    "country_code": response.get("country_code"),
    "country capital": response.get("country_capital"),
    "country tld": response.get("country_tld"),
    "in eu": response.get("in_eu"),
    "postal": response.get("postal"),
    "latitude": response.get("latitude"),
    "longitude": response.get("longitude"),
    "timezone": response.get("timezone"),
    "utc_offset": response.get("utc_offset"),
    "country calling code": response.get("country_callig_code"),
    "currency name": response.get("currency_name"),
    "country area": response.get("country_area"),
    "country population": response.get("country_population"),
  }
  return location_data


@app.route("/g", methods=["GET"])
def g():
  #ip = jsonify({'ip': request.remote_addr}), 200
  #write(ip, "output.txt")
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    write(request.environ['REMOTE_ADDR'], "output.txt")
  else:
    write(request.environ['HTTP_X_FORWARDED_FOR'],
          "output.txt")  # if behind a proxy

  return jsonify({'ip': request.remote_addr}), 200


def log():
  #ip = jsonify({'ip': request.remote_addr}), 200
  #write(ip, "output.txt")
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    write(request.environ['REMOTE_ADDR'], "output.txt")
  else:
    write(request.environ['HTTP_X_FORWARDED_FOR'],
          "output.txt")  # if behind a proxy

  #return jsonify({'ip': request.remote_addr}), 200


def get_ip():
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    return request.environ['REMOTE_ADDR']
  else:
    return request.environ['HTTP_X_FORWARDED_FOR']  # if behind a proxy


@app.route('/data', methods=['POST', 'GET'])
def data():
  if request.method == 'GET':
    return "The URL /data is accessed directly. Try going to '/form' to submit form"
  if request.method == 'POST':
    form_data = request.form
    for value in form_data.items():

      return scripts.encode(value)


@app.route('/hashboi', methods=["GET", "POST"])
def hashboi():
  if request.method == "POST":
    # getting input with name = fname in HTML form
    first_name = request.form.get("fname")
    return scripts.returnstring(scripts.encode(first_name)) + " " * 5 + str(
      scripts.encode(first_name))

  return render_template("form.html")

@app.route('/d_hashboi', methods=["GET", "POST"])
def d_hashboi():
  if request.method == "POST":
    # getting input with name = fname in HTML form
    first_name = request.form.get("fname")
    return scripts.returnstring(scripts.decode(first_name)) + " " * 5 + str(
      scripts.encode(first_name))

  return render_template("form_decrypt.html")
  
##############
@app.route('/f', methods=["GET", "POST"])
def f():
  if request.method == "POST":
    # getting input with name = fname in HTML form
    first_name = request.form.get("fname")
    write(beans2(), f"dump/{first_name}.txt")
  #return beans2()
  return render_template("name_form.html")


###############
@app.route("/hello")
def hello_world():
  return 'Hello, World!'


@app.route("/")
def main():
  log()
  beans()
  return render_template("template.html")


@app.route("/ip")
def ip():
  return render_template("ip.html")


@app.route("/home")
def home():
  return render_template("home.html")


@app.route("/js_enc")
def js_enc():
  return render_template("js_enc.html")


@app.route("/js_dec")
def js_dec():
  return render_template("js_dec.html")


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/chat")
def chat():
  return render_template("chat.html")


def print():
  print("hi")


app.run(host='0.0.0.0', port=8080, debug=True)
home()
