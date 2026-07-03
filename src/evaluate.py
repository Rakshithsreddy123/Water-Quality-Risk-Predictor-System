from src.rules import RULES

def evaluate_rules(data):
    triggered_rules = []
    overall_risk = "Low Risk"

    for param, rule in RULES.items():
        value = data.get(param)

        if value is not None and rule["condition"](value):
            
            triggered_rules.append({
                "parameter": param,
                "value": value,
                "severity": rule["severity"],
                "reason": rule["reason"],
                "suggestions": rule["suggestions"]
            })

            # Update overall risk
            if rule["severity"] == "High Risk":
                overall_risk = "High Risk"
            elif rule["severity"] == "Moderate Risk" and overall_risk != "High Risk":
                overall_risk = "Moderate Risk"

    return overall_risk, triggered_rules