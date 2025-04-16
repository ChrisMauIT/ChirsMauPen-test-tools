from flask import Flask, render_template
app = Flask(__name__)

@app.route("/payload/<id>")
def payload(id):
    # You could dynamically load payloads here
    return render_template("payload.html", payload=f"Payload ID: {id}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
