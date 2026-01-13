function runCheck() {
    document.getElementById("animation").style.display = "block";

    fetch("/run-check")
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.status;
        });
}
