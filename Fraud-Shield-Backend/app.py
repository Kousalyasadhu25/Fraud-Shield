from flask import Flask, request, jsonify

from flask_cors import CORS

from werkzeug.utils import secure_filename

import os



from src.predict import predict_message

from src.file_processor import extract_text

from src.image_processor import extract_text_from_image



app = Flask(__name__)

CORS(app)



# ==========================

# Upload Folder Setup

# ==========================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# ==========================

# Home Route

# ==========================

@app.route("/")

def home():

    return jsonify({"status": "running", "message": "FraudShield Backend Active"})



# ==================================================

# TEXT + DOCUMENT ANALYSIS ROUTE

# ==================================================

@app.route("/analyze", methods=["POST"])

def analyze():

    # --------------------------

    # 1. Text Analysis (JSON)

    # --------------------------

    if request.is_json:

        data = request.get_json(silent=True) or {}

        message = data.get("message", "").strip()



        if not message:

            return jsonify({"error": "Message content is required"}), 400



        try:

            result = predict_message(message)

            return jsonify(result), 200

        except Exception as e:

            print("PREDICTION ERROR:", str(e))

            return jsonify({"error": f"Error running analysis model: {str(e)}"}), 500



    # --------------------------

    # 2. File Upload Analysis (PDF / DOCX / TXT)

    # --------------------------

    if "file" not in request.files:

        return jsonify({"error": "No file uploaded"}), 400



    file = request.files["file"]



    if file.filename == "":

        return jsonify({"error": "No file selected"}), 400



    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)



    try:

        file.save(filepath)



        extracted_text = extract_text(filepath)



        if not extracted_text or not extracted_text.strip():

            return jsonify({"error": "No readable text found in document"}), 400



        result = predict_message(extracted_text)



        print("========== FILE BACKEND RESPONSE ==========")

        print("Extracted Text:", extracted_text[:100], "...")

        print("Prediction Result:", result)



        return jsonify({

            "extracted_text": extracted_text,

            "result": result

        }), 200



    except Exception as e:

        print("FILE PROCESSING ERROR:", str(e))

        return jsonify({"error": f"Failed to process file: {str(e)}"}), 500



    finally:

        if os.path.exists(filepath):

            os.remove(filepath)



# ==================================================

# IMAGE SCREENSHOT ANALYSIS ROUTE

# ==================================================

@app.route("/analyze-image", methods=["POST"])

def analyze_image():

    if "file" not in request.files:

        return jsonify({"error": "No image uploaded"}), 400



    file = request.files["file"]



    if file.filename == "":

        return jsonify({"error": "No image selected"}), 400



    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)



    try:

        file.save(filepath)

        print("SAVED PATH:", filepath)



        # EasyOCR extraction

        extracted_text = extract_text_from_image(filepath)

        print("OCR TEXT:", extracted_text)



        if not extracted_text or not extracted_text.strip():

            return jsonify({"error": "No text detected in image. Please try a clearer screenshot."}), 400



        print("STARTING PREDICTION")

        result = predict_message(extracted_text)

        print("PREDICTION COMPLETED")



        print("========== IMAGE BACKEND RESPONSE ==========")

        print("Extracted Text:", extracted_text)

        print("Prediction Result:", result)



        return jsonify({

            "extracted_text": extracted_text,

            "result": result

        }), 200



    except Exception as e:

        print("IMAGE PROCESSING ERROR:", str(e))

        return jsonify({"error": f"Failed to analyze image: {str(e)}"}), 500



    finally:

        if os.path.exists(filepath):

            os.remove(filepath)



# ==================================================

# RUN SERVER

# ==================================================

if __name__ == "__main__":

    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port, debug=False) 

