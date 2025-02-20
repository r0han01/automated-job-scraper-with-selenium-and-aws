function fillJobTitle(title) {
    document.getElementById('jobTitle').value = title;
}

function fillLocation(location) {
    document.getElementById('location').value = location;
}

function searchJobs() {
    const jobTitle = document.getElementById('jobTitle').value;
    const location = document.getElementById('location').value;

    if (!jobTitle || !location) {
        alert("Please enter both Job Title and Location.");
        return;
    }

    // Show overlay and countdown pop-up
    const overlay = document.getElementById('overlay');
    overlay.style.display = "block";
    setTimeout(() => {
        overlay.classList.add("active");
    }, 10);

    document.getElementById('countdownPopup').style.display = "block";

    let countdownValue = 8;
    const countdownElement = document.getElementById('countdown');

    const countdownInterval = setInterval(() => {
        countdownValue--;
        countdownElement.textContent = countdownValue;
        if (countdownValue === 0) {
            clearInterval(countdownInterval);
            overlay.classList.remove("active");
            setTimeout(() => {
                overlay.style.display = "none";
            }, 800);
            document.getElementById('countdownPopup').style.display = "none";

            // ✅ Send AJAX Request to Flask
            fetch('/search_jobs', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ job_title: jobTitle, location: location })
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);

                    // ✅ Close the browser immediately after Selenium starts
                    window.open('', '_self', '');
                    window.close();
                })
                .catch(error => {
                    console.error("Error starting job search:", error);
                    alert("Error! Could not start automation.");
                });
        }
    }, 1000);
}