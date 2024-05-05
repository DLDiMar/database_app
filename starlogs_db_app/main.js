const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const url = require('url');

// Create the main window
let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    // Load the index.html file
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));

    // Open DevTools (remove this in production)
    // mainWindow.webContents.openDevTools();

    // Handle window closed
    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

// Create the main window when Electron has finished initializing
app.on('ready', createWindow);

// Quit when all windows are closed
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

// Create a new window when the app is activated and there are no windows open (macOS)
app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});

// Handle form submission and interact with the backend
ipcMain.on('add-entry', (event, data) => {
    // Here you would add the entry to the database
    // For demonstration purposes, let's just send back a success message
    // Replace this with your actual database logic

    // Simulate database operation (replace this with your actual database logic)
    // For demonstration purposes, we'll just wait for 1 second before sending the response
    setTimeout(() => {
        // Send a success message back to the renderer process
        mainWindow.webContents.send('entry-added', 'Entry added successfully');
    }, 1000);
});
