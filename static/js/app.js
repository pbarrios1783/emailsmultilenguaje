document.getElementById("email-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    // Mostrar el spinner
    document.getElementById("loading").style.display = "flex";

    const email = document.getElementById("email").value;
    const cultura = document.getElementById("cultura").value;
    const formalidad = document.getElementById("formalidad").value;
    const idioma = document.getElementById("idioma").value;

    try {
        const response = await fetch('/adapt', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, cultura, formalidad, idioma })
        });

        const data = await response.json();

        // Ocultar el spinner
        document.getElementById("loading").style.display = "none";

        if (data.adapted_email) {
            document.getElementById("adapted-email").value = data.adapted_email;
        } else {
            document.getElementById("adapted-email").value = "Error: " + data.error;
        }
    } catch (error) {
        document.getElementById("loading").style.display = "none";
        document.getElementById("adapted-email").value = "Error al generar el email.";
    }
});
