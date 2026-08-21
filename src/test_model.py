import joblib

model = joblib.load("models/scam_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


messages = [

"Your SBI account has been suspended. Complete KYC immediately http://sbi-update.com",

"Congratulations you won lottery prize claim now",

"Hey, are you coming to class tomorrow",

"Your OTP is 458921. Do not share"

]


for msg in messages:

    vector = vectorizer.transform([msg])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector).max()*100


    print("\nMessage:")
    print(msg)

    print("Prediction:",prediction)

    print("Confidence:",probability)

