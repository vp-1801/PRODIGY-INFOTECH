import re

def check_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    score = sum(strength_criteria.values())
    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, strength_criteria

if __name__ == "__main__":
    password = input("Enter your password: ").strip()
    strength, criteria = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Criteria Assessment:")
    for criterion, passed in criteria.items():
        print(f" - {criterion.capitalize()}: {'✔' if passed else '✘'}")
