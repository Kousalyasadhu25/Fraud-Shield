def get_recommendation(category):

    recommendations = {

        "UPI Scam":
        "Never approve unknown collect requests or scan QR codes to receive money.",

        "Job Scam":
        "Do not pay registration or interview fees. Verify the employer through official channels.",

        "Loan Scam":
        "Check whether the lender is registered and never pay advance processing fees.",

        "Investment Scam":
        "Be cautious of guaranteed returns. Verify investment platforms before investing.",

        "Lottery Reward Scam":
        "Ignore unexpected prize claims. Legitimate lotteries do not ask for processing fees.",

        "Phishing Scam":
        "Do not click suspicious links. Visit the official website directly instead.",

        "Digital Arrest Scam":
        "Government agencies do not demand money or arrests over phone calls.",

        "Child Game Scam":
        "Enable parental controls and never share payment OTPs.",

        "Fake Customer Care":
        "Find customer care numbers only from the company's official website.",

        "Safe":
        "No scam indicators detected. Continue following normal online safety practices."

    }

    return recommendations.get(
        category,
        "Stay cautious and verify information before taking any action."
    )