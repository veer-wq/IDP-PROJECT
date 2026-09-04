console.log("Composite Materials Engineering Platform loaded.");


// Update footer year automatically
const yearElement = document.getElementById("currentYear");

if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
}
// Load materials from FastAPI backend
const materialsContainer = document.getElementById("materialsContainer");

if (materialsContainer) {
    fetch("https://idp-project-5gdy.onrender.com/api/materials")
        .then(response => response.json())
        .then(materials => {

            materials.forEach(material => {

                const card = document.createElement("div");
                card.className = "col-md-4";

                card.innerHTML = `
                    <div class="custom-card">
                        <div class="card-icon">◼</div>

                        <h3>${material.name}</h3>

                        <p>
                            Material density:
                            <strong>${material.density} kg/m³</strong>
                        </p>

                        <button class="btn btn-primary">
                            View Details
                        </button>
                    </div>
                `;

                materialsContainer.appendChild(card);
            });

        })
        .catch(error => {
            console.error("Error loading materials:", error);

            materialsContainer.innerHTML = `
                <div class="alert alert-danger">
                    Unable to load materials from backend.
                </div>
            `;
        });
}
// Load manufacturing processes from FastAPI backend
const processesContainer = document.getElementById("processesContainer");

if (processesContainer) {
    fetch("https://idp-project-5gdy.onrender.com/api/processes")
        .then(response => response.json())
        .then(processes => {

            processes.forEach(process => {

                const card = document.createElement("div");
                card.className = "col-md-4";

                card.innerHTML = `
                    <div class="custom-card">

                        <div class="card-icon">⚙️</div>

                        <h3>${process.name}</h3>

                        <p>
                            ${process.description}
                        </p>

                        <button class="btn btn-primary">
                            Learn More
                        </button>

                    </div>
                `;

                processesContainer.appendChild(card);
            });

        })
        .catch(error => {
            console.error("Error loading processes:", error);

            processesContainer.innerHTML = `
                <div class="alert alert-danger">
                    Unable to load manufacturing processes from backend.
                </div>
            `;
        });
}
// Composite weight calculator
const calculateButton = document.getElementById("calculateButton");

if (calculateButton) {

    calculateButton.addEventListener("click", function () {

        const length = Number(document.getElementById("length").value);
        const width = Number(document.getElementById("width").value);
        const thickness = Number(document.getElementById("thickness").value);
        const density = Number(document.getElementById("density").value);

        fetch("https://idp-project-5gdy.onrender.com/api/calculate", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                length: length,
                width: width,
                thickness: thickness,
                density: density
            })
        })

        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            return response.json();
        })

        .then(result => {

            console.log("Calculation result:", result);

            document.getElementById("calculationResult").innerHTML = `
                <div class="alert alert-success">
                    <strong>Volume:</strong> ${result.volume} m³
                    <br>
                    <strong>Mass:</strong> ${result.mass} kg
                </div>
            `;

        })

        .catch(error => {

            console.error("Calculation error:", error);

            document.getElementById("calculationResult").innerHTML = `
                <div class="alert alert-danger">
                    Unable to calculate. Please check the backend.
                </div>
            `;

        });

    });
}
// ML Prediction
const predictButton = document.getElementById("predictButton");

if (predictButton) {

    predictButton.addEventListener("click", function () {

        const fiberType = document.getElementById("fiberType").value;
        const resinType = document.getElementById("resinType").value;
        const fiberVolumeFraction =
            Number(document.getElementById("fiberVolumeFraction").value);
        const manufacturingProcess =
            document.getElementById("manufacturingProcess").value;

        fetch("https://idp-project-5gdy.onrender.com/api/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                fiber_type: fiberType,
                resin_type: resinType,
                fiber_volume_fraction: fiberVolumeFraction,
                manufacturing_process: manufacturingProcess
            })

        })

        .then(response => response.json())

        .then(result => {

            document.querySelector(".placeholder-area").innerHTML = `
                <div class="card-icon">🤖</div>

                <h4>Prediction Result</h4>

                <h2>
                    ${result.prediction} ${result.unit}
                </h2>

                <p class="text-muted">
                    ${result.message}
                </p>
            `;

        })

        .catch(error => {

            console.error("Prediction error:", error);

            document.querySelector(".placeholder-area").innerHTML = `
                <div class="alert alert-danger">
                    Unable to get prediction from backend.
                </div>
            `;

        });

    });
}