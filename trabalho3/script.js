const GrafoEstados = {
    "AC": ["AM", "RO"], 
    "AL": ["BA", "PE", "SE"], 
    "AP": ["PA"], 
    "AM": ["AC", "MT", "PA", "RO", "RR"], 
    "BA": ["AL", "ES", "GO", "MG", "PE", "PI", "SE", "TO"], 
    "CE": ["PB", "PE", "PI", "RN"], 
    "DF": ["GO", "MG"], 
    "ES": ["BA", "MG", "RJ"], 
    "GO": ["BA", "DF", "MT", "MS", "MG", "TO"], 
    "MA": ["PA", "PI", "TO"], 
    "MT": ["AM", "GO", "MS", "PA", "RO", "TO"], 
    "MS": ["GO", "MT", "MG", "PR", "SP"], 
    "MG": ["BA", "DF", "ES", "GO", "MS", "RJ", "SP"], 
    "PA": ["AP", "AM", "MA", "MT", "RR", "TO"], 
    "PB": ["CE", "PE", "RN"], 
    "PR": ["MS", "SC", "SP"], 
    "PE": ["AL", "BA", "CE", "PB", "PI"], 
    "PI": ["BA", "CE", "MA", "PE", "TO"], 
    "RJ": ["ES", "MG", "SP"], 
    "RN": ["CE", "PB"], 
    "RS": ["SC"], 
    "RO": ["AC", "AM", "MT"], 
    "RR": ["AM", "PA"], 
    "SC": ["PR", "RS"], 
    "SP": ["MS", "MG", "PR", "RJ"], 
    "SE": ["AL", "BA"], 
    "TO": ["BA", "GO", "MA", "MT", "PA", "PI"]
};

const colors = [
    "yellow",
    "red",
    "green",
    "blue",
    "orange",
    "purple"
];

const paths = document.getElementsByTagName("path");

function getElementsByIds(ids) {
    return ids.map(id => document.getElementById(id));
}

function paintState(stateElement, color) {
    stateElement.style = `fill:${color};stroke:#ffffff;stroke-opacity:1;stroke-width:282.23677982;stroke-miterlimit:4;stroke-dasharray:none`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


(async () => {
    for (const path of paths) {
        let inkscapeLabel = path.getAttribute("inkscape:label");
        if (inkscapeLabel) {

            let currentStateElement = path;
            let currentStateName = currentStateElement.id;
            let currentStateNeighbours = getElementsByIds(GrafoEstados[currentStateName]);
            let currentStateNeighboursColors = currentStateNeighbours.map(neighbour => neighbour.style.fill);
            let colorIndex = 0;
            let color = colors[colorIndex];

            // console.log(currentStateName, currentStateNeighbours)

            while (currentStateNeighboursColors.includes(color)) {
                colorIndex++;
                color = colors[colorIndex];
                await sleep(200);
                paintState(currentStateElement, color);
            }
            await sleep(200);
            paintState(currentStateElement, color);
        }
    }

    console.log("done!")
})();
