async function checkEmail() {
    const text = document.getElementById("emailText").value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    const resultDiv = document.getElementById("result");
    resultDiv.innerText = data.result;

    // Color change
    if (data.result.includes("Phishing")) {
        resultDiv.style.color = "red";
    } else {
        resultDiv.style.color = "lightgreen";
    }
}