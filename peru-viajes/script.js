// =====================
// 1. NAVBAR AL HACER SCROLL
// =====================
const navbar = document.getElementById('navbar')

window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled')
    } else {
        navbar.classList.remove('scrolled')
    }
})


// =====================
// 2. MENÚ HAMBURGUESA
// =====================
const hamburguesa = document.getElementById('hamburguesa')
const navLinks = document.getElementById('nav-links')

hamburguesa.addEventListener('click', function() {
    navLinks.classList.toggle('activo')
})


// =====================
// 3. MODAL DE RESERVA
// =====================

// Seleccionamos el modal y el botón de cerrar
const modal = document.getElementById('modal')
const cerrarModal = document.getElementById('cerrar-modal')
const modalPaquete = document.getElementById('modal-paquete')

// Función que se llama cuando hacen clic en "Reservar"
// "boton" es el botón que se clickeó
function mostrarModal(boton) {

    // Subimos al elemento padre para obtener el nombre del paquete
    const paquete = boton.closest('.paquete')
    const nombre = paquete.querySelector('h3').textContent

    // Escribimos el nombre del paquete en el modal
    modalPaquete.textContent = '📦 ' + nombre

    // Mostramos el modal agregando la clase "activo"
    modal.classList.add('activo')

    // Bloqueamos el scroll de la página mientras el modal está abierto
    document.body.style.overflow = 'hidden'
}

// Cerrar modal al hacer clic en la X
cerrarModal.addEventListener('click', function() {
    modal.classList.remove('activo')
    document.body.style.overflow = ''   // Devuelve el scroll
})

// Cerrar modal al hacer clic fuera de él
modal.addEventListener('click', function(e) {
    // e.target es el elemento que se clickeó
    // Si se clickeó el fondo oscuro (no el contenido) cierra el modal
    if (e.target === modal) {
        modal.classList.remove('activo')
        document.body.style.overflow = ''
    }
})


// =====================
// 4. BOTÓN CONFIRMAR
// =====================
const botonConfirmar = document.querySelector('.boton-confirmar')

botonConfirmar.addEventListener('click', function() {
    // Cambia el texto del botón
    botonConfirmar.textContent = '✅ ¡Reserva Enviada!'
    botonConfirmar.style.backgroundColor = '#005c3a'

    // Después de 2 segundos cierra el modal
    setTimeout(function() {
        modal.classList.remove('activo')
        document.body.style.overflow = ''
        botonConfirmar.textContent = 'Confirmar Reserva'
        botonConfirmar.style.backgroundColor = '#00a86b'
    }, 2000)  // 2000 milisegundos = 2 segundos
})