from flask import Flask,render_template,request,redirect,url_for,send_file


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if  request.form.get('action1') == 'Web Application':
            return render_template("item/website.html") # do something

        elif  request.form.get('action1') == 'Big Data Analysis':
            return send_file("static/project-file/Python.pdf", as_attachment=True)    
        elif  request.form.get('action1') == 'Vision System':
            return send_file("static/project-file/Vision.pdf", as_attachment=True)
        elif request.form.get('action1') == 'Quality Indicator':
            return send_file("static/project-file/Quality.pdf", as_attachment=True)

        elif  request.form.get('action2') == 'Homepage':
            return render_template("index.html") # do something
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")    