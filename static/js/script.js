const noteField = document.getElementById("note");
const extractBtn = document.getElementById("extract-btn");
const sampleBtn = document.getElementById("sample-btn");
const downloadBtn = document.getElementById("download-btn");
const errorMsg = document.getElementById("error-msg");
const chart = document.getElementById("chart");

const SAMPLE_NOTE =
  "Patient complains of fatigue and joint pain. Diagnosed with rheumatoid arthritis. Prescribed methotrexate. Follow-up in 4 weeks.";

let lastResult = null;

sampleBtn.addEventListener("click", () => {
  noteField.value = SAMPLE_NOTE;
  noteField.focus();
});

extractBtn.addEventListener("click", async () => {
  const note = noteField.value.trim();

  hideError();

  if (!note) {
    showError("Please paste a clinical note.");
    return;
  }

  setLoading(true);

  try {
    const formData = new FormData();
    formData.append("note", note);

    const response = await fetch("/api/extract", {
      method: "POST",
      body: formData,
    });

    const payload = await response.json();

    if (!response.ok) {
      showError(payload.error || "Something went wrong.");
      return;
    }

    renderChart(payload.structured);
  } catch (err) {
    showError("Could not reach the server. Please try again.");
  } finally {
    setLoading(false);
  }
});

downloadBtn.addEventListener("click", () => {
  if (!lastResult) return;

  const blob = new Blob([JSON.stringify(lastResult, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "structured_notes.json";
  a.click();

  URL.revokeObjectURL(url);
});

function renderChart(data) {
  lastResult = data;

  document.getElementById("out-symptoms").textContent = data.symptoms || "N/A";
  document.getElementById("out-diagnosis").textContent = data.diagnosis || "N/A";
  document.getElementById("out-medications").textContent = data.medications || "N/A";
  document.getElementById("out-followup").textContent = data.follow_up || "N/A";

  chart.hidden = false;
  chart.scrollIntoView({ behavior: "smooth", block: "start" });
}

function setLoading(isLoading) {
  extractBtn.disabled = isLoading;
  extractBtn.querySelector(".btn-label").textContent = isLoading
    ? "Analyzing note…"
    : "Structure this note";
}

function showError(message) {
  errorMsg.textContent = message;
  errorMsg.hidden = false;
}

function hideError() {
  errorMsg.hidden = true;
}
