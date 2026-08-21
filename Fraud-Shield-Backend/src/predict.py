import joblib

from src.preprocess import clean_text
from src.risk_engine import analyze_risk
from src.rules import detect_fraud_category
from src.recommendations import get_recommendation


# ==========================
# Load Saved ML Model
# ==========================

model = joblib.load("models/scam_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


# ==========================
# Prediction Function
# ==========================

def predict_message(message):

    # --------------------------
    # Text Cleaning
    # --------------------------

    cleaned_text = clean_text(message)


    # --------------------------
    # TF-IDF Transformation
    # --------------------------

    vector = vectorizer.transform([cleaned_text])


    # --------------------------
    # ML Prediction
    # --------------------------

    prediction = model.predict(vector)[0]


    # --------------------------
    # ML Confidence
    # --------------------------

    confidence = model.predict_proba(vector).max() * 100


    if prediction == 1:
        ml_result = "Scam"

    else:
        ml_result = "Safe"



    # --------------------------
    # Rule-Based Risk Analysis
    # --------------------------

    risk = analyze_risk(message)



    # --------------------------
    # Fraud Category
    # --------------------------

    fraud_category = detect_fraud_category(message)



    # --------------------------
    # Recommendation
    # --------------------------

    recommendation = get_recommendation(fraud_category)



    # --------------------------
    # Final Decision
    # --------------------------

    if risk["risk_score"] >= 70:

        final_result = "Scam"


    elif ml_result == "Scam":

        final_result = "Scam"


    else:

        final_result = "Safe"



    # ==========================
    # Final Response
    # ==========================


    if final_result == "Safe":

        result = {


            "prediction": "Safe",


            "ml_prediction": ml_result,


            "confidence": float(round(confidence, 2)),


            "fraud_category": "Not Applicable",


            "recommendation":
            "Continue following normal online safety practices.",


            "risk_level": "🟢 Low",


            "reasons": [
                "No scam indicators detected"
            ]

        }



    else:

        result = {


            "prediction": "Scam",


            "ml_prediction": ml_result,


            "confidence": float(round(confidence, 2)),


            "fraud_category": fraud_category,


            "recommendation": recommendation,


            "risk_level": risk["risk_level"],


            "reasons": risk["reasons"]

        }



    return result





# ==========================
# Testing
# ==========================

if __name__ == "__main__":


    print("\n==============================")
    print("     FRAUDSHIELD AI ANALYZER")
    print("==============================")


    while True:


        message = input(
            "\nEnter Message (type 'exit' to quit): "
        )


        if message.lower() == "exit":

            break



        result = predict_message(message)



        print("\n==============================")
        print("       FRAUDSHIELD REPORT")
        print("==============================")


        print(
            "Prediction :",
            result["prediction"]
        )


        print(
            "ML Prediction :",
            result["ml_prediction"]
        )


        print(
            "AI Confidence :",
            result["confidence"],
            "%"
        )


        print(
            "Fraud Category :",
            result["fraud_category"]
        )


        print(
            "Recommendation :",
            result["recommendation"]
        )


        print(
            "Risk Level :",
            result["risk_level"]
        )



        print("\nRed Flags:")



        if result["reasons"]:


            for reason in result["reasons"]:

                print("-", reason)


        else:

            print(
                "- No suspicious patterns detected"
            )


        print("==============================")