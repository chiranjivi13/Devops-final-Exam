document.addEventListener('DOMContentLoaded', () => {
    const actionBtn = document.getElementById('action-btn');
    const statusMsg = document.getElementById('status-msg');

    actionBtn.addEventListener('click', () => {
        // Remove hidden class to show the success message
        statusMsg.classList.remove('hidden');
        
        // Optional: Change button text
        actionBtn.textContent = 'Clicked!';
        actionBtn.style.backgroundColor = 'var(--success)';
        
        // The selenium test will look for the visibility of #status-msg
    });
});
