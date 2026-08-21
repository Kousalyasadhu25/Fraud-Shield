import re


# ==========================
# Risk Engine
# ==========================

def analyze_risk(message):

    text = message.lower()

    risk_score = 0
    reasons = []

    # --------------------------
    # Suspicious URL
    # --------------------------
    if re.search(r"(https?://|www\.|bit\.ly|tinyurl|t\.co)", text):
        risk_score += 35
        reasons.append("Contains suspicious link")

    # --------------------------
    # Urgency
    # --------------------------
    urgency_words = [
        "urgent",
        "immediately",
        "now",
        "today",
        "within",
        "limited time",
        "expires",
        "expired",
        "last chance",
        "act now",
        "action required",
        "suspended",
        "blocked",
        "2 hours",
        "24 hours"
    ]

    if any(word in text for word in urgency_words):
        risk_score += 15
        reasons.append("Creates urgency")

    # --------------------------
    # Financial Request
    # --------------------------
    money_phrases = [
        "pay now",
        "send money",
        "transfer money",
        "transfer immediately",
        "upi payment",
        "scan qr",
        "processing fee",
        "security deposit",
        "claim refund",
        "refund pending",
        "refund approved",
        "refund amount",
        "refund process",
        "process your refund",
        "pay ₹",
        "pay rs",
        "bank transfer"
    ]

    if any(phrase in text for phrase in money_phrases):
        risk_score += 20
        reasons.append("Requests money or banking action")

    

    # --------------------------
    # Sensitive Information
    # --------------------------
    personal_phrases = [
        "share otp",
        "enter otp",
        "provide otp",
        "tell otp",
        "share pin",
        "share cvv",
        "share password",
        "verify your account",
        "verify kyc",
        "update kyc",
        "confirm aadhaar",
        "confirm pan",
        "login credentials"
    ]

    if any(phrase in text for phrase in personal_phrases):
        risk_score += 20
        reasons.append("Requests sensitive information")
    # --------------------------
    # Account Verification
    # --------------------------
    verification_phrases = [
        "verify your account",
        "verify your bank account",
        "update your account",
        "confirm your identity",
        "re-verify",
        "account verification"
    ]

    if any(phrase in text for phrase in verification_phrases):
        risk_score += 25
        reasons.append("Requests account verification")

    # --------------------------
    # Threat / Fear
    # --------------------------
    threat_words = [
        "arrest",
        "warrant",
        "police",
        "court",
        "legal action",
        "freeze account",
        "penalty",
        "blocked",
        "suspended",
        "blacklisted",
        "criminal",
        "cyber crime"
    ]

    if any(word in text for word in threat_words):
        risk_score += 20
        reasons.append("Uses fear or threat")

    # --------------------------
    # Rewards / Lottery
    # --------------------------
    reward_words = [
        "lottery",
        "winner",
        "won",
        "reward",
        "gift",
        "jackpot",
        "congratulations",
        "claim prize",
        "free cash"
    ]

    if any(word in text for word in reward_words):
        risk_score += 20
        reasons.append("Promises rewards or prizes")

    # --------------------------
    # Investment Scam
    # --------------------------
    investment_words = [
        "guaranteed returns",
        "10x",
        "double your money",
        "earn daily",
        "earn ₹",
        "investment opportunity",
        "profit guaranteed",
        "high returns"
    ]

    if any(word in text for word in investment_words):
        risk_score += 30
        reasons.append("Promises unrealistic investment returns")

    # --------------------------
    # Remote Access Apps
    # --------------------------

    remote_apps = [
        "anydesk",
        "teamviewer",
        "quicksupport",
        "supremo",
        "ultraviewer",
        "remote desktop"
    ]

    if any(app in text for app in remote_apps):
        risk_score += 30
        reasons.append("Requests installation of remote access software")
    # --------------------------
    # Trusted Organization
    # --------------------------
    impersonation = [
        "sbi",
        "hdfc",
        "icici",
        "axis",
        "rbi",
        "income tax",
        "cyber crime",
        "police",
        "amazon",
        "flipkart",
        "paytm",
        "phonepe",
        "google pay",
        "aadhaar",
        "uidai"
    ]

    if any(word in text for word in impersonation):
        risk_score += 15
        reasons.append("Pretends to be a trusted organization")

    # --------------------------
    # Suspicious Actions
    # --------------------------
    action_phrases = [
        "click here",
        "click the link",
        "login now",
        "download app",
        "install app",
        "open the link"
    ]

    if any(phrase in text for phrase in action_phrases):
        risk_score += 20
        reasons.append("Requests suspicious action")

    # --------------------------
    # Safe Indicators
    # --------------------------
    safe_phrases = [
        "has been credited",
        "transaction successful",
        "order delivered",
        "appointment reminder",
        "scheduled",
        "do not share this otp",
        "thank you for shopping",
        "package delivered",
        "payment received",
        "salary credited"
    ]

    if any(phrase in text for phrase in safe_phrases):
        risk_score = max(0, risk_score - 20)

    # --------------------------
    # Final Score
    # --------------------------
    risk_score = max(0, min(risk_score, 100))

    # --------------------------
    # Risk Level
    # --------------------------
    if risk_score >= 70:
        level = "🔴 Critical"
    elif risk_score >= 40:
        level = "🟠 High"
    elif risk_score >= 20:
        level = "🟡 Medium"
    else:
        level = "🟢 Low"

    if not reasons:
        reasons.append("No major red flags detected.")

    return {
        "risk_score": risk_score,
        "risk_level": level,
        "reasons": reasons
    }


if __name__ == "__main__":

    while True:

        message = input("\nEnter Message (type 'exit' to quit): ")

        if message.lower() in ["exit", "quit"]:
            break

        result = analyze_risk(message)

        print("\nThreat Score :", result["risk_score"], "/100")
        print("Risk Level   :", result["risk_level"])

        print("\nReasons:")
        for reason in result["reasons"]:
            print("✓", reason)