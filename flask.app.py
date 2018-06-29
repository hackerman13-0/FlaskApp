from flask import Flask
app = Flask("First App")

@app.route('/')
def index():

       return "Its Working"

if __name__=="__main__":
         app.run()
