from flask import render_template
from systeminfo.main import main
from app import app


@app.route('/')
def index():
	returnDict = {}
	returnDict['user'] = 'Sophie Heseltine'
	returnDict['title'] = 'Home'
	returnDict['info'] = main()
	return render_template("index.html", **returnDict)

