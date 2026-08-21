from predict import predict_message
from risk_engine import analyze_risk
from category_predict import predict_category
from recommendations import get_recommendation


while True:

    message = input("\nEnter Message (type 'exit' to quit): ")

    if message.lower() == "exit":
        break

    # Binary Prediction
    prediction = predict_message(message)

    # Risk Analysis
    risk = analyze_risk(message)

    print("\n==============================")
    print("FRAUDSHIELD ANALYSIS")
    print("==============================")

    print("Prediction :", prediction["prediction"])
    print("AI Confidence :", prediction["confidence"], "%")

    # Run category model only for scams
    if prediction["prediction"].lower() == "scam":

        category, category_confidence = predict_category(message)

        print("\nFraud Category :", category)

        # Optional: Don't show percentage if you don't want to
        # print("Category Confidence :", category_confidence, "%")

        print("\nRecommendation:")
        print(get_recommendation(category))

    else:

        print("\nFraud Category : Not Applicable")

        print("\nRecommendation:")
        print(get_recommendation("Safe"))

    

    print("\nReasons:")

    if len(risk["reasons"]) == 0:
        print("✓ No major red flags detected.")
    else:
        for reason in risk["reasons"]:
            print("✓", reason)