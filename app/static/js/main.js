// Generate fake data for the histogram
function generateFakeData() {
    var data = [];
    for (var i = 0; i < 24; i++) {
        var value = Math.floor(Math.random() * 1000);
        data.push(value);
    }
    return data;
}

// instantiating socket object
var socket= io.connect('http://127.0.0.1:5000/');
var people = 0;

var test = 10;

$(document).ready(function() {
    socket.on('after connect', function(msg) {
        console.log('After connect', msg.data);
    })
    function getUpdate() {
        console.log("It's been 20 seconds, we need an update!")
        socket.emit('Update histogram', {
            bool: true
        });
    }
    setInterval(getUpdate, 10000);
    socket.on('update count of people', function(num_people) {
        console.log('Updated the histogram!');
        // console.log(num_people.count);
        people = num_people.count;
        updateHistogramChart(people);
    })
})


async function updateHistogramChart(num_people) {
    // const num_people = await getPrediction();
    const now = new Date();
    const minute = now.getMinutes();
    histogramChart.data.labels.shift();
    histogramChart.data.labels.push(minute);
    // histogramChart.data.datasets[0].data.shift();
    histogramChart.data.datasets[0].data.push(num_people);
    histogramChart.update();
}




// Create the histogram chart
var ctx = document.getElementById('histogramChart').getContext('2d');
var histogramChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Array.from({ length: 5 }, (_, i) => i + 1),
        datasets: [{
            label: 'Number of People',
            data: [2, 4],
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
                text: 'Time of Day (minutes)'
            }
        }
        }
    }
});