import pyrebase

config = {
    'apiKey': "AIzaSyB9Zwl7foIgnTQkjPfL-luYMZDbvFZuS5I",
    'authDomain': "symbiota-376423.firebaseapp.com",
    'projectId': "symbiota-376423",
    'storageBucket': "symbiota-376423.appspot.com",
    'messagingSenderId': "971555328530",
    'appId': "1:971555328530:web:74e043b974b85e59d23ecb",
    'measurementId': "G-4N86NQLRWY",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def process_login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None
        

def process_create(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None