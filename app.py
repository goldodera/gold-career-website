from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lagos, Nigeria',
        'salary': 'Naira. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Abuja, Nigeria',
        'salary': 'Naira. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Abia, Nigeria',
        'salary': 'Naira. 150,00,000'
    }
]
@app.route("/")
def hello_gold():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Gold")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
print(__name__)
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)