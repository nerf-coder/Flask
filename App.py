from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'Papa',
        'contact': '9890443740', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Mummy',
        'contact': '9537137789', 
        'done': False
    }
]


@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" :contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)