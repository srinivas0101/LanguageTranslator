const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const translateBtn = document.getElementById('translateBtn'); // Get the Translate button
const resultBox = document.getElementById('resultBox');
const languageSelect = document.getElementById('languageSelect');

let recognition = null;
let selectedLanguage = languageSelect.value;

function startRecording() {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = selectedLanguage;
    recognition.start();

    startBtn.style.display = 'none';
    stopBtn.style.display = 'inline-block';
    translateBtn.style.display = 'none'; // Hide Translate button when recording starts

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        resultBox.textContent = transcript;
        translateBtn.style.display = 'inline-block'; // Show Translate button when result is available
    };

    recognition.onerror = function(event) {
        resultBox.textContent = 'Error occurred: ' + event.error;
    };
}

function stopRecording() {
    if (recognition) {
        recognition.stop();
        recognition = null;

        startBtn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}

function translateText() {
    const textToTranslate = resultBox.textContent;
    const languageCode = languageSelect.value;
}

startBtn.addEventListener('click', startRecording);
stopBtn.addEventListener('click', stopRecording);
translateBtn.addEventListener('click', translateText); // Call translateText function when Translate button is clicked

languageSelect.addEventListener('change', function() {
    selectedLanguage = languageSelect.value;
    if (recognition) {
        recognition.lang = selectedLanguage;
    }
});



var translateBtn1 = document.getElementById('translateBtn');


var resultForm = document.getElementById('resultForm');
var resultInput = document.getElementById('resultInput');
var resultBox1 = document.getElementById('resultBox');


function submitResult() {
    resultInput.value = resultBox.innerText;
    resultForm.submit(); 
}

// Attach an event listener to the translate button
translateBtn1.addEventListener('click', submitResult);



