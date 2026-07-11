window.onload = function () {
    // Attach event listeners
    const switches = ["light", "ac", "fan", "geyser", "tv"];
    switches.forEach(id => {
        const toggle = document.getElementById(`${id}-toggle`);
        if (toggle) toggle.addEventListener("change", getPrediction);
    });

    // Optional: load prediction initially
    getPrediction();
};

function getPrediction() {
    const deviceStates = {
        light: getState("light-toggle"),
        ac: getState("ac-toggle"),
        fan: getState("fan-toggle"),
        geyser: getState("geyser-toggle"),
        tv: getState("tv-toggle")
    };

    // Optional UI feedback
    const usageElem = document.getElementById("usage-value");
    const costElem = document.getElementById("cost-value");
    if (usageElem) usageElem.innerText = "Calculating...";
    if (costElem) costElem.innerText = "₹...";

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(deviceStates)
    })
    .then(response => response.json())
    .then(data => {
        if (usageElem) usageElem.innerText = `${data.predicted_kwh} kWh`;
        if (costElem) costElem.innerText = `₹${data.predicted_cost}`;
    })
    .catch(error => {
        console.error("Prediction error:", error);
        if (usageElem) usageElem.innerText = "Error";
        if (costElem) costElem.innerText = "₹--";
    });
}

function getState(id) {
    const el = document.getElementById(id);
    return el && el.checked ? 1 : 0;
}

