from datetime import datetime  # Make sure this is imported at the top if not already

@app.route("/save-lead", methods=["POST"])
def save_lead():
    data = request.get_json()
    email = data.get("email")
    tier = data.get("tierUrl")

    if not email:
        return jsonify({"status": "error", "message": "Missing email"}), 400

    lead_data = {
        "email": email,
        "tier": tier,
        "timestamp": datetime.now().isoformat()
    }

    leads = []
    try:
        with open("leads.json", "r") as f:
            leads = json.load(f)
    except:
        leads = []

    leads.append(lead_data)
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=2)

    return jsonify({"status": "success"})
