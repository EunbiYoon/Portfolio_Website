from flask import Flask,render_template,request,redirect,url_for,send_file


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form.get('action1') == 'Big Data Analysis':
            return render_template('item/data.html') # do something
        elif  request.form.get('action2') == 'Vision System':
            return render_template('item/visiion.html') # do something
        elif  request.form.get('action3') == 'Quality Indicator':
            return render_template('item/quality.html') # do something
        elif  request.form.get('action4') == 'Web Application':
            return render_template("item/website.html") # do something
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template("index.html")


@app.route('/download')
def downloadFile ():
    path = "static/QualityDetailedLogic.zip"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")    