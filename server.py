from flask import Flask, url_for, request, redirect, render_template
import flames
app = Flask(__name__)

result = 'tempResult'
boyName = 'tempBoyName'
girlName = 'tempGirlName'

@app.route('/')
def upload_file():
	return render_template("index.html", action="Add")

@app.route('/flamesEngine', methods = ['POST'])
def flamesEngine():
    global boyName, girlName, result
    boyName = request.form['bn']
    girlName = request.form['gn']
    nameStriker = flames.NameStriker()
    result = nameStriker.flamesCalculate(boyName, girlName)

    if result == 'FRIENDS':
        flamesResult = '%s and %s are FRIENDS' % (boyName, girlName)
    elif result == 'LOVE':
        flamesResult = '%s LOVES %s' % (boyName, girlName)
    elif result == 'AFFECTIONATE':
        flamesResult = '%s and %s are AFFECTIONATE' % (boyName, girlName)
    elif result == 'MARRIAGE':
        flamesResult = '%s will MARRY %s' % (boyName, girlName)
    elif result == 'ENEMIES':
        flamesResult = '%s and %s are ENEMIES' % (boyName, girlName)
    elif result == 'SIBLINGS':
        flamesResult = '%s is %s\'s SISTER' % (boyName, girlName)
    else:
        flamesResult = 'ERROR! CONTACT MAINTENANCE'
    return render_template("index.html", action="Add", result=flamesResult)

if __name__ == '__main__':
	app.run(debug = True, threaded = True, host = '0.0.0.0')
