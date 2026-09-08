***

### 📜 File 2: `script.js`
Create a new file named exactly **`script.js`** in the **same exact folder** as your `index.html` file, and paste this inside:

```javascript
// Wait for the HTML elements to load before executing event listeners
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const transferForm = document.getElementById('transfer-form');

    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }
    if (transferForm) {
        transferForm.addEventListener('submit', handleTransferSubmit);
    }
});

function handleLogin(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    document.getElementById('welcome-message').innerText = `Hello, ${username}!`;
    document.getElementById('profile-name').innerText = username;
    document.getElementById('login-page').classList.add('hidden');
    document.getElementById('dashboard-page').classList.remove('hidden');
}

function handleLogout() {
    document.getElementById('dashboard-page').classList.add('hidden');
    document.getElementById('login-page').classList.remove('hidden');
}

function toggleProfile() { 
    document.getElementById('profile-panel').classList.toggle('hidden'); 
}

function toggleTransferPanel() { 
    document.getElementById('transfer-panel').classList.toggle('hidden'); 
    document.getElementById('transfer-error').classList.add('hidden'); 
}

function handleTransferSubmit(event) { 
    event.preventDefault(); 
    document.getElementById('transfer-error').classList.remove('hidden'); 
}
```

<FollowUp>
Are both files saved inside the **same directory** on your device, and are the login and log out actions working smoothly now?
</FollowUp>
