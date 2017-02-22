from flask import Flask
from script import hello
app=Flask(__name__)

@app.route("/")
def showButton():
	return "<a href='/execute'>Execute </a>"
@app.route("/execute")
def execute():
	return hello();
if __name__ == '__main__':
	app.run()
