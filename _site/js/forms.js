document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            if (validateForm(form)) {
                // If it's a quote or worker request and no backend is set up, fallback to WhatsApp
                const formType = form.getAttribute('data-form-type');
                if (formType === 'quote' || formType === 'worker-request' || formType === 'worker-registration') {
                    sendToWhatsApp(form);
                } else {
                    alert('Form submitted successfully!'); // Fallback
                    form.reset();
                }
            }
        });
    });
});

function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    // Remove old error messages
    form.querySelectorAll('.form-error').forEach(err => err.remove());
    form.querySelectorAll('.error-border').forEach(el => el.classList.remove('error-border'));

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            showError(field, 'This field is required');
        } else if (field.type === 'email' && !validateEmail(field.value)) {
            isValid = false;
            showError(field, 'Please enter a valid email address');
        }
    });

    return isValid;
}

function showError(field, message) {
    field.classList.add('error-border');
    const errorSpan = document.createElement('span');
    errorSpan.className = 'form-error';
    errorSpan.style.color = 'red';
    errorSpan.style.fontSize = '14px';
    errorSpan.style.display = 'block';
    errorSpan.style.marginTop = '4px';
    errorSpan.textContent = message;
    
    field.parentNode.appendChild(errorSpan);
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function sendToWhatsApp(form) {
    const formData = new FormData(form);
    let message = `*New Request from Website*\n\n`;
    
    for (let [key, value] of formData.entries()) {
        if(value) {
            // Capitalize first letter of key and format
            const formattedKey = key.charAt(0).toUpperCase() + key.slice(1).replace(/-/g, ' ');
            message += `*${formattedKey}:* ${value}\n`;
        }
    }

    const waNumber = NEW_NABLIS_CONFIG.contact.whatsapp.replace(/\D/g, '');
    const waUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`;
    
    window.open(waUrl, '_blank');
}
