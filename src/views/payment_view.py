from src import app


@app.route("/payments", methods=["POST"])
def process_payment():
    # TODO -> add payment processing logic in this view
    return {
        "message": "Dummy payment result"
    }
