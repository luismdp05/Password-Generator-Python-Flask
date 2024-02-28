from flask import Flask, render_template, request
import random
import string
import pyperclip

app = Flask(__name__)

def validate_length(length):
  min_length = 8
  max_length = 32
  return min_length <= length <= max_length

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
  length = int(request.form.get('length'))

  if not validate_length(length):
    error_message = f"La longitud debe estar entre 8 y 32 caracteres."
    return render_template('index.html', error=error_message)

  password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
 
  # Copiar la contraseña al portapapeles
  pyperclip.copy(password)

  return render_template('index.html', password=password)

if __name__ == '__main__':
  app.run(debug=True)
