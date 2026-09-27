from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)

@app.route("/")
def home():
    #check whether the user already has an identfier 
    aid = request.cookies.get("aid")
    is_new = aid is None

    #Generate a new identifier for a new browser
    if is_new:
        aid = secrets.token_hex(8)

    #create the normal HTTP response with the index.html template
    response = make_response(render_template("index.html"))

    #ask the browser to store the identifier
    if is_new:
        response.set_cookie(
            key="aid",
            value=aid,
            samesite="None")
    
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)