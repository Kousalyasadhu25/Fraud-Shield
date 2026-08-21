const analyzeBtn = document.getElementById("analyzeBtn");
const textInput = document.getElementById("textInput");
const fileInput = document.getElementById("fileInput");
const selectedFile = document.getElementById("selectedFile");
const resultBox = document.getElementById("resultBox");

let uploadedFile = null;

// =========================
// File Selection
// =========================

fileInput.addEventListener("change", () => {
  if (fileInput.files.length > 0) {
    uploadedFile = fileInput.files[0];
    selectedFile.innerText = uploadedFile.name;
    console.log("FILE STORED:", uploadedFile);
  } else {
    uploadedFile = null;
    selectedFile.innerText = "No File Selected";
  }
});

// =========================
// UI Loading Helper
// =========================

function setLoading(isLoading) {
  analyzeBtn.disabled = isLoading;
  analyzeBtn.innerHTML = isLoading
    ? `<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...`
    : `<i class="fa-solid fa-magnifying-glass"></i> Analyze with FraudShield AI`;
}

// =========================
// Display Result
// =========================

function showResult(result) {
  console.log("SHOW RESULT:", result);

  if (!result) return;

  // Handle Backend Error Responses
  if (result.error) {
    resultBox.innerHTML = `
      <div class="result error-result">
        <h2><i class="fa-solid fa-triangle-exclamation"></i> Error</h2>
        <p>${result.error}</p>
      </div>
    `;
    resultBox.style.display = "block";
    return;
  }

  // Format Reasons List
  let reasonsHTML = "<li>No scam indicators detected</li>";
  if (result.reasons && result.reasons.length > 0) {
    reasonsHTML = result.reasons
      .map((r) => `<li>${r}</li>`)
      .join("");
  }

  // Determine Class based on Prediction
  const isScam = result.prediction && result.prediction.toLowerCase() === "scam";
  const resultClass = isScam ? "scam-result" : "safe-result";

  resultBox.innerHTML = `
    <div class="result ${resultClass}">
      <h2>🛡 FRAUDSHIELD ANALYSIS</h2>

      <div class="prediction">
        ${result.prediction || "Unknown"}
      </div>

      <div class="result-item">
        <strong>📂 Fraud Category:</strong>
        ${result.fraud_category || "Not Available"}
      </div>

      <div class="result-item">
        <strong>⚠️ Risk Level:</strong>
        ${result.risk_level || "Not Available"}
      </div>

      <div class="result-item">
        <strong>🤖 AI Confidence:</strong>
        ${result.confidence || 0}%
      </div>

      <div class="result-item">
        <strong>🚩 Reasons:</strong>
        <ul>
          ${reasonsHTML}
        </ul>
      </div>

      <div class="recommendation">
        <strong>💡 Recommendation:</strong>
        <br><br>
        ${result.recommendation || "No specific recommendation provided."}
      </div>
    </div>
  `;

  resultBox.style.display = "block";
}

// =========================
// Analyze Button Event
// =========================

analyzeBtn.addEventListener("click", async (event) => {
  event.preventDefault();

  const text = textInput ? textInput.value.trim() : "";

  // Mutual Exclusion Validation
  if (text !== "" && uploadedFile) {
    alert("Please enter text OR select a file to analyze (not both).");
    return;
  }

  if (text === "" && !uploadedFile) {
    alert("Please enter text or select a file to analyze.");
    return;
  }

  setLoading(true);

  try {
    let response;

    // 1. TEXT ANALYSIS PIPELINE
    if (text !== "") {
      response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: text }),
      });
    }

    // 2. FILE / IMAGE ANALYSIS PIPELINE
    else if (uploadedFile) {
      const formData = new FormData();
      formData.append("file", uploadedFile);

      const filename = uploadedFile.name.toLowerCase();
      const isImage = [".png", ".jpg", ".jpeg", ".webp"].some((ext) =>
        filename.endsWith(ext)
      );

      // Route image files to /analyze-image and docs/PDFs to /analyze
      const endpoint = isImage
        ? "http://127.0.0.1:5000/analyze-image"
        : "http://127.0.0.1:5000/analyze";

      response = await fetch(endpoint, {
        method: "POST",
        body: formData,
      });
    }

    const data = await response.json();
    console.log("RESPONSE FROM SERVER:", data);

    if (!response.ok) {
      showResult({ error: data.error || `Server Error (${response.status})` });
      return;
    }

    // Unwraps { extracted_text: ..., result: {...} } or direct prediction objects
    showResult(data.result ? data.result : data);

  } catch (error) {
    console.error("ANALYSIS ERROR:", error);
    showResult({
      error: "Failed to connect to backend server. Make sure Python app.py is running on port 5000."
    });
  } finally {
    setLoading(false);
  }
});