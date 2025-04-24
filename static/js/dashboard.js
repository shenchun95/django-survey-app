// Initialize age distribution chart
const ctx = document.getElementById('ageChart').getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['0-20', '21-40', '41-60', '60+'],
        datasets: [{
            label: 'Age Distribution',
            data: [0, 0, 0, 0],  // This will be updated with actual data
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});