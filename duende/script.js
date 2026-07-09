const modal = document.getElementById("modalContacto");

const abrirFormulario = document.getElementById("abrirFormulario");
const abrirFormularioHero = document.getElementById("abrirFormularioHero");

const cerrarFormulario = document.getElementById("cerrarFormulario");

const formulario = document.getElementById("formularioWhatsapp");

const origen = document.getElementById("origen");
const campoRecomendacion = document.getElementById("campoRecomendacion");

const botonesVer = document.querySelectorAll(".btn-ver");

const numeroWhatsapp = "51969527971";

function mostrarModal(producto = "") {
    modal.classList.add("activo");

    if (producto !== "") {
        document.getElementById("producto").value = producto;
    }
}

abrirFormulario.addEventListener("click", function () {
    mostrarModal();
});

abrirFormularioHero.addEventListener("click", function () {
    mostrarModal();
});

cerrarFormulario.addEventListener("click", function () {
    modal.classList.remove("activo");
});

botonesVer.forEach(function (boton) {
    boton.addEventListener("click", function () {
        mostrarModal(boton.dataset.producto);
    });
});

origen.addEventListener("change", function () {
    if (origen.value === "Recomendación") {
        campoRecomendacion.style.display = "block";
    } else {
        campoRecomendacion.style.display = "none";
        document.getElementById("recomendadoPor").value = "";
    }
});

formulario.addEventListener("submit", function (e) {
    e.preventDefault();

    const producto = document.getElementById("producto").value;
    const comoConocio = document.getElementById("origen").value;
    const recomendadoPor = document.getElementById("recomendadoPor").value;

    let mensaje = `Hola, quiero cotizar un(a): ${producto}.%0A`;
    mensaje += `Conocí el catálogo por: ${comoConocio}.%0A`;

    if (comoConocio === "Recomendación" && recomendadoPor !== "") {
        mensaje += `Me recomendó: ${recomendadoPor}.`;
    }

    window.open(
        `https://wa.me/${numeroWhatsapp}?text=${mensaje}`,
        "_blank"
    );
});