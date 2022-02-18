from flask import Flask, render_template, request, redirect, make_response, Response, send_from_directory, send_file
import time


app = Flask(__name__)


@app.route("/")
def main():
    return Response("{'Data':'Hello World!'}", status=200, mimetype='application/json')

@app.route("/delay")
def delay():

    delay = int(request.args.get("delay"))
    time.sleep(delay)
    return Response("{'Delay':{'" + str(delay) +"'}", status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, use_reloader=False)
