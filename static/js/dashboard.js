document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('emissionChart').getContext('2d');
    
    // Check if we have data to display
    if (chartLabels.length === 0) {
        ctx.font = "16px Arial";
        ctx.textAlign = "center";
        ctx.fillText("Complete your first log to see trends", 400, 100);
        return;
    }

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'Carbon Footprint (kg CO2)',
                data: chartData,
                borderColor: '#198754',
                backgroundColor: 'rgba(25, 135, 84, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#198754',
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { display: false }
                },
                x: {
                    grid: { display: false }
                }
            }
        }
    });
});