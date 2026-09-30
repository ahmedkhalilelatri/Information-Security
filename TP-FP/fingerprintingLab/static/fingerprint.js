const features = {
    language: navigator.language,
    hardwareConcurrency: navigator.hardwareConcurrency,
    screenResolution: screen.width + "x" + screen.height,
    windowSize: window.innerWidth + "x" + window.innerHeight,
    timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone
};

// Display in browser console
console.log("Collected features:", features);

// Display on webpage
const outputElement = document.getElementById("feature-output");

outputElement.innerHTML = `
    <strong>Language:</strong> ${features.language}<br>
    <strong>CPU logical cores:</strong> ${features.hardwareConcurrency}<br>
    <strong>Screen resolution:</strong> ${features.screenResolution}<br>
    <strong>Window size:</strong> ${features.windowSize}<br>
    <strong>Time zone:</strong> ${features.timeZone}
`;

// Send features to Flask
fetch("/collect", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(features)
});