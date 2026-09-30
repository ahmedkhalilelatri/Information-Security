from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")

    print("IP address          :", request.remote_addr)
    print("HTTP method         :", request.method)

    print("User-Agent          :", request.headers.get("User-Agent"))
    print("Accept-Language     :", request.headers.get("Accept-Language"))

    print("Accept              :", request.headers.get("Accept"))
    print("Accept-Encoding     :", request.headers.get("Accept-Encoding"))
    print("Sec-CH-UA           :", request.headers.get("Sec-CH-UA"))
    print("Sec-CH-UA-Platform  :", request.headers.get("Sec-CH-UA-Platform"))
    print("Sec-CH-UA-Mobile    :", request.headers.get("Sec-CH-UA-Mobile"))
    print("DNT                 :", request.headers.get("DNT"))
    print("Sec-Fetch-Site      :", request.headers.get("Sec-Fetch-Site"))
    print("Sec-Fetch-Mode      :", request.headers.get("Sec-Fetch-Mode"))

    print("================================\n")

    return render_template("index.html")


@app.route("/collect", methods=["POST"])
def collect():
    data = request.get_json()

    print("\n====== ACTIVE FEATURES ======")
    print("Language             :", data.get("language"))
    print("CPU logical cores    :", data.get("hardwareConcurrency"))
    print("Screen resolution    :", data.get("screenResolution"))
    print("Window size          :", data.get("windowSize"))
    print("Time zone            :", data.get("timeZone"))
    print("=============================\n")

    return {"status": "ok"}

@app.route("/typing", methods=["POST"])
def typing():
    data = request.get_json()

    print("\n====== TYPING BEHAVIOUR ======")
    print("Typing time       :", data.get("typingTime"))
    print("Typing speed      :", data.get("typingSpeed"))
    print("Corrections       :", data.get("corrections"))
    print("==============================\n")

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)