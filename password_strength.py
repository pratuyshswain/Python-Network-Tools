import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria 1: Length (Must be at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (needs 8+ chars)")

    # Criteria 2: Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")

    # Criteria 3: Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")

    # Criteria 4: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Missing a number")

    # Criteria 5: Special Characters (!@#$ etc)
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing special char (!@#$)")

    return score, feedback

# --- Main Program ---
print("--- Password Strength Analyzer ---")
user_pass = input("Enter a password to test: ")
score, comments = check_password_strength(user_pass)

print(f"\nScore: {score}/5")
if score == 5:
    print("Rating: STRONG ✅")
elif score >= 3:
    print("Rating: MODERATE ⚠️")
else:
    print("Rating: WEAK ❌")

if comments:
    print("Suggestions:")
    for comment in comments:
        print(f"- {comment}")