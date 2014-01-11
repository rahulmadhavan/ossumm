from flask import Flask, send_from_directory
from image_generator import ImageGenerator
from flask import render_template

app = Flask(import_name = "ossumm",template_folder = "/Users/rahulm/Documents/Developer/Projects/ossumm/app/models/public")
app.debug = True


@app.route("/gen/css/<path:filename>")
def css(filename):
   return send_from_directory("/Users/rahulm/Documents/Developer/Projects/ossumm/app/models/public/css",filename)

@app.route("/gen/images/<path:filename>")
def images(filename):
   return send_from_directory("/Users/rahulm/Documents/Developer/Projects/ossumm/app/models/public/images",filename)

@app.route("/gen/js/<path:filename>")
def js(filename):
   return send_from_directory("/Users/rahulm/Documents/Developer/Projects/ossumm/app/models/public/js",filename)


@app.route("/gen/<search>")
def gen(search):
    images = ImageGenerator().generate(search)
    simages=[]
    for image in images:
        simages.append(unicode(image.get_html(),"utf8"))
    return render_template('search-result-template.html',images = simages)

@app.route("/gens/<search>")
def gens(search):
    images = ImageGenerator().generate(search)
    simages=[]
    for image in images:
        simages.append(unicode(image.get_html(),"utf8"))
    return "".join(simages)

@app.route("/temp")
def temp():
    return render_template('search-result.html')

@app.route("/")
def hello():
    return "Hello World! yay!!!"


if __name__ == "__main__":
    app.run()