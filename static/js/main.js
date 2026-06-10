document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Automatically fade out Flask alert notifications after 4 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            // Using Bootstrap's native Alert close utility class safely
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });

    // 2. Prevent accidental negative number inputs on standard metric forms
    const numericInputs = document.querySelectorAll('input[type="number"]');
    numericInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            if (parseFloat(this.value) < 0) {
                this.value = 0;
                alert("Value cannot be negative! Auto-correcting entry to 0.");
            }
        });
    });
});