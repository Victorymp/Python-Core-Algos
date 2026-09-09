countries = [
    {"code": "GB", "risk": 72},
    {"code": "FR", "risk": 65},
    {"code": "DE", "risk": 80},
]

above_seventy = [ x.get("code") for x in countries if x.get("risk") > 70 ]

print(above_seventy)