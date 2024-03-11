// Mock data item
const item = {
    question: "What is the capital of France?",
    answer: "" // Initially empty
};

// Updated JavaScript code with Fetch API integration

document.addEventListener('DOMContentLoaded', function() {
    fetchQuestion();
});

// Fetch a random question from the FastAPI backend
async function fetchQuestion() {
    const response = await fetch('http://localhost:8001/random-item');
    if (response.ok) {
        const item = await response.json();
        displayQuestion(item);
    } else {
        console.error('Failed to fetch question');
    }
}

// Function to display the fetched question
function displayQuestion(item) {
    const questionElement = document.getElementById('question');
    questionElement.textContent = item.question;

    const answerElement = document.getElementById('answer');
    answerElement.value = item.answer || ""; // Use fetched answer or default to empty string
}

// Function to save the edited answer
async function saveAnswer() {
    const answerElement = document.getElementById('answer');
    const updatedAnswer = answerElement.value; // Get the updated answer from the textarea

    console.log("Answer saved:", updatedAnswer);
    // Here, you would send the updated answer back to your server
    // Example (you need to implement the API endpoint for saving the answer):
    /*
    const response = await fetch('http://localhost:8001/save-answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: document.getElementById('question').textContent, answer: updatedAnswer }),
    });
    
    if (response.ok) {
        console.log('Answer saved successfully');
    } else {
        console.error('Failed to save answer');
    }
    */
}
