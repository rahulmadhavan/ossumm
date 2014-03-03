from flask import Flask, send_from_directory
from image_generator import ImageGenerator
from flask import render_template, redirect
import sys

# -i ip , -p port, -b base_folder, -h hostname

pargs = {
    '-i' : '127.0.0.1',
    '-p' : 5000,
    '-b' : '/home/ubuntu',
    '-h' : 'localhost'
}


if len(sys.argv) % 2 == 0 :
    raise RuntimeError('arguments are not specified correctly -i ip , -p port, -b base_folder, -h hostname')

option = None
command = None

for arg in sys.argv:
    if command is None:
        command = arg
    else:
        if option is None:
            if arg not in ['-i','-p','-h','-b']:
                raise RuntimeError('options are not specified correctly '+ arg)
            else:
                option = arg
        else:
            if arg in ['-i','-p','-h','-b']:
                raise RuntimeError('options are not specified correctly '+ arg)
            pargs[option] = arg
            option = None



IP = pargs['-i']
PORT = int(pargs['-p'])
BASE_FOLDER = pargs['-b']
HOST_NAME = pargs['-h']
if PORT == 80:
    BASE_URL = "http://"+HOST_NAME+"/"
else:
    BASE_URL = "http://"+HOST_NAME+":"+str(PORT)+"/"



app = Flask(import_name = "ossumm",template_folder = BASE_FOLDER+"/ossumm/app/models/public")
app.debug = True


@app.route("/css/<path:filename>")
def css(filename):
   return send_from_directory(BASE_FOLDER+"/ossumm/app/models/public/css",filename)

@app.route("/images/<path:filename>")
def images(filename):
   return send_from_directory(BASE_FOLDER+"/ossumm/app/models/public/images",filename)

@app.route("/js/<path:filename>")
def js(filename):
   return send_from_directory(BASE_FOLDER+"/ossumm/app/models/public/js",filename)


@app.route("/<search>", methods=['GET', 'POST'] )
def gen(search):
    images = ImageGenerator().generate(search)
    simages=[]
    for image in images:
        simages.append(unicode(image.get_html(),"utf8"))
    return render_template('search-result-template.html',images = simages, base_url = BASE_URL)

@app.route("/gens/<search>", methods=['GET', 'POST'])
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
    return redirect(BASE_URL+'dog',302)

@app.route("/healthcheck")
def healthcheck():
    return "Hello World! yay!!!"


if __name__ == "__main__":
    app.run(IP,PORT)