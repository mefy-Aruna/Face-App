# -*- coding: utf-8 -*-
"""

"""
from flask import Flask, render_template, redirect, url_for, session, request
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, UserMixin, current_user, login_user, \
                        login_required, logout_user
# from flask_session import Session

import faceLoginApp 

# __author__ = 'Aruna Ramasmay'

# app = Flask(__name__)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# app = Flask(__name__, static_url_path='', static_folder='static')
# app.config['SECRET_KEY'] = 'secret!'
# app.config['SESSION_TYPE'] = 'filesystem'
# login = LoginManager(app)
# class User(UserMixin, object):
#     def __init__(self, id=None, name=''):
#         self.id = id
#         self.name = name

# @login.user_loader
# def load_user(id):
#     try:
#       name = session['user_' + id]
#       return User(id, name)
#     except:
#       return None

# @app.route('/')
# def index():
#     return render_template('index.html', user_name = current_user)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     if request.method == 'GET':
#       return render_template('login.html')

#     print(request.form)
#     if request.form['auth_key'] == '1234567890':
#       login_user(User(1, 'Garv'))
#       session['user_1'] = 'Garv'
#     return redirect(url_for('login'))

# @app.route('/logout')
# @login_required
# def logout():
#     print('Logging out')
#     logout_user()
#     return redirect(url_for('index'))

# # @app.route("/")
# # def index():
    
# #     return render_template("index.html")


# # @app.route("/upload")

# # def upload():
# #     print("here")
# #     UserLogin.captureAndCompare()
# #     print("Done")

# # def upload():
# #     target = os.path.join(APP_ROOT, 'images/')
# #     print(target)
# #     if not os.path.isdir(target):
# #             os.mkdir(target)
# #     else:
# #         print("Couldn't create upload directory: {}".format(target))
# #     print(request.files.getlist("file"))
# #     for upload in request.files.getlist("file"):
# #         print(upload)
# #         print("{} is the file name".format(upload.filename))
# #         filename = upload.filename
# #         destination = "/".join([target, filename])
# #         print("Accept incoming file:", filename)
# #         print("Save it to:", destination)
# #         upload.save(destination)
# #     execution_path = target
# #     print(execution_path)
# #     image = Predict(os.path.join(execution_path, filename))
# #     print(image.shape)
# #     print('predicted')
# #     out_image = cv2.imwrite(os.path.join(execution_path,  "flask"+filename), image)
# #     print('wrote out the image')
# #     print('flask'+filename)
# #     return render_template("Flask_FacialRecognition_WebService.html", image_name="flask"+filename)


# # @app.route('/upload/<filename>')
# # def send_image(filename):
# #     return send_from_directory("images", filename)


# if __name__ == "__main__":
#     app.run()





# ///////////////////////

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_TYPE'] = 'filesystem'
login = LoginManager(app)
# Session(app)
socketio = SocketIO(app)
recognizer = faceLoginApp.UserLogin

class User(UserMixin, object):
    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name

@login.user_loader
def load_user(id):
    try:
      name = session['user_' + id]
      return User(id, name)
    except:
      return None

@app.route('/')
def index():
    return render_template('index.html', user_name = current_user)

# @app.route('/'
# def index():
#     if form.validate_on_submit():
#         if 'Register' in request.form:
#             pass # do something
#         elif 'Already registered? Face Login' in request.form:
#             pass # do something else

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'GET':
        
        recognizer.captureAndCompare('Aruna')

        return render_template('login.html')

    print(request.form)
    if request.form['auth_key'] == '1234567890':
      login_user(User(1, 'Aruna'))
      session['user_1'] = 'Aruna'
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    print('Logging out')
    logout_user()
    return redirect(url_for('index'))

@socketio.on('stream')
def send_image(img):
    print("here")
    
       

# real time streaming
@socketio.on('stream-end')
def send_image_end(img):
  emit('stream-end', {'endded': True}, broadcast=True)

@socketio.on('verify-user')
def verifyt_user(img):
  id, name, accouracy = recognizer.Recognize()
  auth_key = ''
  if id is not None:
      auth_key = '1234567890'
  emit('verify-user', {'id': id, 'name': name, 'auth_key': auth_key,'accouracy': accouracy}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
