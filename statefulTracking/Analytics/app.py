from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

profiles = {}


@app.route("/collect")
def collect():
    analytics_id = request.args.get("id")
    publisher = request.args.get("publisher")
    page = request.args.get("page")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if analytics_id not in profiles:
        profiles[analytics_id] = []

    profiles[analytics_id].append({
        "time": timestamp,
        "publisher": publisher,
        "page": page
    })

    print("\n--- ANALYTICS REQUEST ---")
    print("Analytics ID :", analytics_id)
    print("Publisher    :", publisher)
    print("Page         :", page)

    print("\n--- RECONSTRUCTED PROFILE ---")

    for visit in profiles[analytics_id]:
        print(
            f"{visit['time']} | "
            f"{visit['publisher']} | "
            f"{visit['page']}"
        )

    return "", 204


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=9100,
        debug=True
    )
    