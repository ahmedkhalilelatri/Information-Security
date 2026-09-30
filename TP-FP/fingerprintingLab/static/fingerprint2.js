const targetElement = document.getElementById("target-sentence");
const typingInput = document.getElementById("typing-input");
const restartButton = document.getElementById("restart-button");
const resultArea = document.getElementById("typing-results");

const targetSentence = targetElement.textContent.trim();

let startTime = null;
let correctionCount = 0;
let finished = false;


// Detect first key and Backspace
typingInput.addEventListener("keydown", function (event) {

    // Start timer on the first actual typing action
    if (startTime === null && event.key.length === 1) {
        startTime = performance.now();
    }

    // Count Backspace corrections
    if (event.key === "Backspace") {
        correctionCount++;
    }
});


// Detect when sentence is completed
typingInput.addEventListener("input", function () {

    if (
        !finished &&
        startTime !== null &&
        typingInput.value === targetSentence
    ) {

        finished = true;

        const endTime = performance.now();

        const elapsedMilliseconds = endTime - startTime;
        const elapsedSeconds = elapsedMilliseconds / 1000;

        const typingSpeed =
            targetSentence.length / elapsedSeconds;

        resultArea.innerHTML = `
            <p><strong>Total time:</strong>
            ${elapsedSeconds.toFixed(2)} seconds</p>

            <p><strong>Typing speed:</strong>
            ${typingSpeed.toFixed(2)} characters/second</p>

            <p><strong>Corrections:</strong>
            ${correctionCount}</p>
        `;

        const typingData = {
            typingTime: elapsedSeconds.toFixed(2),
            typingSpeed: typingSpeed.toFixed(2),
            corrections: correctionCount
        };

        fetch("/typing", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(typingData)
        });
    }
});


// Restart experiment
restartButton.addEventListener("click", function () {

    typingInput.value = "";
    resultArea.innerHTML = "";

    startTime = null;
    correctionCount = 0;
    finished = false;

    typingInput.focus();
});