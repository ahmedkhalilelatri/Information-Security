from flask import Flask, render_template, request, make_response
import secrets
from datetime import datetime

app = Flask(__name__)

# In-memory list containing the visits observed by the tracker
visits = []

@app.route("/track")
def track():
    # Identify which publisher/page loaded the tracker
    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")

    # Check whether this browser already has a tracker identifier
    tracker_id = request.cookies.get("tracker_id")
    is_new = tracker_id is None

    if is_new:
        tracker_id = secrets.token_hex(8)

    # Record the visit
    visit = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tracker_id": tracker_id,
        "publisher": publisher,
        "page": page
    }

    visits.append(visit)

    # Server-side evidence
    print("\n--- TRACKER REQUEST ---")
    print(f"Tracker ID : {tracker_id}")
    print(f"Publisher  : {publisher}")
    print(f"Page       : {page}")

    print("\n--- RECONSTRUCTED PROFILE ---")
    for v in visits:
        if v["tracker_id"] == tracker_id:
            print(
                f'{v["time"]} | '
                f'{v["publisher"]} | '
                f'{v["page"]}'
            )

    response = make_response(
        render_template(
            "tracker.html",
            tracker_id=tracker_id
        )
    )

    # Persistent identifier
    if is_new:
        response.set_cookie(
            key="tracker_id",
            value=tracker_id,
            max_age=3600
        )

    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)