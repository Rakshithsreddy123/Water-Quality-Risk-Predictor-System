RULES = {

    # 🚨 CRITICAL PARAMETERS

    "pH": {
        "condition": lambda x: x < 6.5 or x > 8.5,
        "severity": "High Risk",
        "reason": "pH is outside safe drinking range (6.5–8.5)",
        "suggestions": [
            "Use pH balancing treatment",
            "Neutralize water before consumption"
        ]
    },

    "Turbidity": {
        "condition": lambda x: x > 5,
        "severity": "High Risk",
        "reason": "High turbidity (cloudy water)",
        "suggestions": [
            "Use advanced filtration system",
            "Sedimentation + filtration recommended"
        ]
    },

    # ⚠️ MODERATE PARAMETERS

    "Solids": {
        "condition": lambda x: x > 500,
        "severity": "Moderate Risk",
        "reason": "High Total Dissolved Solids",
        "suggestions": [
            "Use RO or UV filtration",
            "Improve source water quality"
        ]
    },

    "Hardness": {
        "condition": lambda x: x > 300,
        "severity": "Moderate Risk",
        "reason": "High water hardness",
        "suggestions": [
            "Install water softener",
            "Use ion-exchange treatment"
        ]
    },

    "Sulfates": {
        "condition": lambda x: x > 250,
        "severity": "Moderate Risk",
        "reason": "High sulfate levels (can cause laxative effects)",
        "suggestions": [
            "Use RO treatment",
            "Dilute with low-sulfate water"
        ]
    },

    "Chloramines": {
        "condition": lambda x: x > 4,
        "severity": "Moderate Risk",
        "reason": "High chloramine concentration",
        "suggestions": [
            "Use activated carbon filters",
            "Improve treatment process"
        ]
    },

    "Trihalomethanes": {
        "condition": lambda x: x > 80,
        "severity": "Moderate Risk",
        "reason": "High trihalomethanes (carcinogenic risk)",
        "suggestions": [
            "Use activated carbon filtration",
            "Reduce chlorination byproducts"
        ]
    },

    # ⚠️ ENVIRONMENTAL / INDICATOR PARAMETERS

    "Conductivity": {
        "condition": lambda x: x > 400,
        "severity": "Moderate Risk",
        "reason": "High conductivity (excess ions present)",
        "suggestions": [
            "Use RO treatment",
            "Monitor dissolved salts"
        ]
    },

    "Organic_carbon": {
        "condition": lambda x: x > 2,
        "severity": "Moderate Risk",
        "reason": "High organic carbon content",
        "suggestions": [
            "Use activated carbon filtration",
            "Remove organic contaminants"
        ]
    }
}