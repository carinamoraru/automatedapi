from flask import Flask
application =  Flask(__name__)
app = application

@application.route('/')
def index():
   return 'hello world'

if __name__ == "__main__":
    application.debug = True
    application.run()

