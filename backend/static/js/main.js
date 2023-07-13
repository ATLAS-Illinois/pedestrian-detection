// Generate fake data for the histogram
function generateFakeData() {
    var data = [];
    for (var i = 0; i < 24; i++) {
        var value = Math.floor(Math.random() * 1000);
        data.push(value);
    }
    return data;
}

// Create the histogram chart
var ctx = document.getElementById('histogramChart').getContext('2d');
var histogramChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Array.from({ length: 24 }, (_, i) => i),
        datasets: [{
        label: 'Number of People',
        data: generateFakeData(),
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
        }]
    },
    options: {
        scales: {
        y: {
            beginAtZero: true,
            title: {
            display: true,
            text: 'Number of People'
            }
        },
        x: {
            title: {
            display: true,
            text: 'Time of Day (hours)'
            }
        }
        }
    }
});