// =====================
// 1. NAVBAR AL HACER SCROLL
// =====================

// Seleccionamos el navbar por su id
const navbar = document.getElementById('navbar')

// Escuchamos cuando el usuario hace scroll
window.addEventListener('scroll', function() {
    
    // Si el usuario bajó más de 50px
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled')    // Agrega la clase "scrolled"
    } else {
        navbar.classList.remove('scrolled') // La quita si sube arriba
    }
})


// =====================
// 2. MENÚ HAMBURGUESA
// =====================

// Seleccionamos el botón y el menú
const hamburguesa = document.getElementById('hamburguesa')
const navLinks = document.getElementById('nav-links')

// Cuando hacen clic en la hamburguesa
hamburguesa.addEventListener('click', function() {
    navLinks.classList.toggle('activo') // toggle = si no tiene la clase la agrega, si la tiene la quita
})


// =====================
// 3. CONTADORES ANIMADOS
// =====================

// Seleccionamos todos los elementos con clase "contador"
const contadores = document.querySelectorAll('.contador')

// Función que anima un contador
function animarContador(elemento) {
    const objetivo = parseInt(elemento.getAttribute('data-target')) // Lee el data-target
    const duracion = 2000  // 2 segundos de animación
    const pasos = 60       // Cantidad de pasos
    const incremento = objetivo / pasos // Cuánto sube en cada paso

    let actual = 0

    // setInterval repite una función cada X milisegundos
    const intervalo = setInterval(function() {
        actual += incremento

        if (actual >= objetivo) {
            elemento.textContent = objetivo + '+'  // Muestra el número final con +
            clearInterval(intervalo)               // Para el intervalo
        } else {
            elemento.textContent = Math.floor(actual) // Muestra el número redondeado
        }
    }, duracion / pasos)
}

// IntersectionObserver detecta cuando un elemento aparece en pantalla
const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
        if (entry.isIntersecting) {           // Si el elemento es visible
            animarContador(entry.target)       // Anima ese contador
            observer.unobserve(entry.target)   // No lo anima de nuevo
        }
    })
}, { threshold: 0.5 }) // Se activa cuando el 50% del elemento es visible

// Aplicamos el observer a cada contador
contadores.forEach(function(contador) {
    observer.observe(contador)
})