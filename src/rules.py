# ==========================
# FraudShield Rule Database
# ==========================

# Urgency
URGENCY = [
    "urgent",
    "immediately",
    "now",
    "within 24 hours",
    "today",
    "last chance",
    "expires today",
    "action required",
    "limited time"
]

# Threat
THREATS = [
    "account suspended",
    "account blocked",
    "legal action",
    "arrest",
    "freeze account",
    "penalty",
    "police",
    "cyber crime",
    "court notice"
]

# Personal information requests
PERSONAL_REQUESTS = [
    "share otp",
    "enter otp",
    "tell otp",
    "verify otp",
    "share pin",
    "share cvv",
    "enter password",
    "provide aadhaar",
    "provide pan",
    "complete kyc"
]

# Money requests
FINANCIAL_REQUESTS = [
    "pay",
    "transfer",
    "upi",
    "scan qr",
    "registration fee",
    "processing fee",
    "deposit",
    "advance payment",
    "refund fee"
]

# Rewards
REWARDS = [
    "you won",
    "lottery",
    "cash prize",
    "gift voucher",
    "reward",
    "congratulations"
]

# Trusted organisations
IMPERSONATION = [
    "sbi",
    "hdfc",
    "icici",
    "axis bank",
    "rbi",
    "income tax",
    "cyber crime",
    "amazon",
    "flipkart",
    "paytm",
    "phonepe",
    "google pay"
]


# ==========================
# Fraud Category Detection
# ==========================

def detect_fraud_category(message):

    text = message.lower()

    # Investment Scam
    if any(word in text for word in [
        "investment",
        "crypto",
        "bitcoin",
        "guaranteed returns",
        "double your money",
        "10x",
        "profit"
    ]):
        return "Investment Scam"

    # Child Game Scam
    elif any(word in text for word in [
        "free fire",
        "pubg",
        "bgmi",
        "diamonds",
        "uc",
        "game"
    ]):
        return "Child Game Scam"

    # Job Scam
    elif any(word in text for word in [
        "job",
        "interview",
        "work from home",
        "earn from home"
    ]):
        return "Job Scam"

    # Loan Scam
    elif any(word in text for word in [
        "loan",
        "instant loan",
        "credit approval"
    ]):
        return "Loan Scam"

    # Lottery Reward Scam
    elif any(word in text for word in REWARDS):
        return "Lottery Reward Scam"

    # Fake Customer Care
    elif any(word in text for word in [
        "refund",
        "customer care",
        "anydesk",
        "teamviewer",
        "remote desktop"
    ]):
        return "Fake Customer Care"

    # Digital Arrest Scam
    elif any(word in text for word in THREATS):
        return "Digital Arrest Scam"

    # UPI Scam
    elif any(word in text for word in FINANCIAL_REQUESTS):
        return "UPI Scam"

    # Phishing Scam
    elif any(word in text for word in PERSONAL_REQUESTS):
        return "Phishing Scam"

    return "Safe"