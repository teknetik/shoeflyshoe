from flask import Flask, url_for, render_template, request, redirect, make_response, Response, send_from_directory, send_file, session
import time
import jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'kongstrong'

oauth = OAuth(app)
stepon = oauth.register(
    name='stepon',
    client_id='NAzqk2VNCF5hJ2NpzmatyUuiOluVqer4',
    client_secret='9AyBIuG62OvN3aQvxBK9yoi4uZNTyZ0D',
    access_token_url='https://reprocloud.app:944/stepon/stepcounts/oauth2/token',
    access_token_params={'method': 'POST'},
    authorize_url='https://reprocloud.app:9444/stepon/stepcounts/oauth2/authorize',
    authorize_params={'method': 'POST'},
    api_base_url='https://reprocloud.app:9444/stepon/stepcounts/',
    client_kwargs={'scopes': 'step_counts', 'method': 'POST'},
    redirect_uri='https://shoeflyshoe.store',
)


# @app.route('/login')
# def login():
#     print("Login")
#     stepon = oauth.create_client('stepon')
#     redirect_uri = url_for('authorize', _external=True)
#     return stepon.authorize_redirect(redirect_uri)

# @app.route('/authorize')
# def authorize():
#     print("Authorize")
#     stepon = oauth.create_client('stepon')
#     token = oauth.stepon.authorize_access_token()
#     resp = stepon.get('userinfo')
#     user_info = resp.json
#     return redirect('http://shoeflyshoe.store/')

@app.route('/login')
def login():
    print("Login")
    redirect_uri = url_for('authorize', _external=True)
    print("Return")
    return stepon.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    print("Authorization")
    token = oauth.stepon.authorize_access_token()
    print(token)
    resp = oauth.stepon.get('user')
    profile = resp.json()
    print(profile)
    # do something with the token and profile
    return redirect('/')    

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/delay")
def delay():

    delay = int(request.args.get("delay"))
    time.sleep(delay)
    return Response("{'Delay':{'" + str(delay) +"'}", status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, use_reloader=False, ssl_context=('fullchain.pem', 'privkey.pem'))




