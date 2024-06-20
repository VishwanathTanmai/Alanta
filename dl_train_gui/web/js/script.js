document.getElementById('startTrial').addEventListener('click', function() {
    alert('Thank you for choosing Alanta Predictive Maintenance Software. Your trial has started.');
    // Set trial end timer (e.g., 30 days)
    var trialEnd = new Date();
    trialEnd.setDate(trialEnd.getDate() + 30); // 30 days from now
    var timer = setInterval(function() {
        var now = new Date().getTime();
        var distance = trialEnd - now;
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById('trialTimer').innerHTML = 'Trial ends in: ' + days + 'd ' + hours + 'h ' + minutes + 'm ' + seconds + 's';
        if (distance < 0) {
            clearInterval(timer);
            document.getElementById('trialTimer').innerHTML = 'Trial ended';
        }
    }, 1000);
});
