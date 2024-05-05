// Import required modules
const { ipcRenderer } = require('electron');

// Get a reference to the form element
const entryForm = document.getElementById('entryForm');
const messageDiv = document.getElementById('message');

// Listen for form submission
entryForm.addEventListener('submit', async (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get values from form fields
    const numColumns = parseInt(entryForm.elements['num_columns'].value);
    if (isNaN(numColumns) || numColumns <= 0) {
        messageDiv.textContent = "Please enter a valid number of columns";
        return;
    }

    const columnData = {};
    for (let i = 0; i < numColumns; i++) {
        columnData[`column_${i+1}`] = entryForm.elements[`column_${i+1}`].value;
    }

    try {
        // Create the database by making a POST request to the Flask route
        const createResponse = await fetch('http://localhost:5000/create_database', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ num_columns: numColumns, ...columnData })
        });

        if (!createResponse.ok) {
            throw new Error('Failed to create database');
        }

        // If the database is created successfully, display a success message
        messageDiv.textContent = "Database created successfully";
    } catch (error) {
        // If there's an error, display the error message
        messageDiv.textContent = error.message;
    }
});
