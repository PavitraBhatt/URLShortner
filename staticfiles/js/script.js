// AJAX Functions for Different Features
document.addEventListener("DOMContentLoaded", () => {
    // Generic URL Shortener
    const genericForm = document.getElementById("generic-form");
    if (genericForm) {
        genericForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const link = document.getElementById("link").value;

            fetch(genericForm.action, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": genericForm.querySelector("input[name='csrfmiddlewaretoken']").value,
                },
                body: `link=${encodeURIComponent(link)}`,
            })
                .then((response) => response.json())
                .then((data) => {
                    const output = document.getElementById("generic-output");
                    output.innerHTML = `<p>Shortened URL: <a href="/${data.uuid}" target="_blank">/${data.uuid}</a></p>`;
                });
        });
    }

    // Add similar event listeners for other forms (expiry, qr, password) if needed
});
