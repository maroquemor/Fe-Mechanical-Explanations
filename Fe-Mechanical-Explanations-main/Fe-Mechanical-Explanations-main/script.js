// Script para la página de inicio
document.addEventListener('DOMContentLoaded', function() {
    generateQuestions();        // Generar las 120 preguntas
    setupPagination();          // Configurar paginación
    setupContactForm();         // Configurar formulario de contacto
    setupSmoothScrolling();     // Configurar navegación suave
});

function generateQuestions() {
    const questionsContainer = document.getElementById('questions-container');
    const totalQuestions = 120;  // <-- Cambiado a 120

    const topics = [
        "Matemáticas", "Estática", "Dinámica", "Mecánica de Materiales",
        "Termodinámica", "Transferencia de Calor", "Diseño Mecánico",
        "Dinámica de Fluidos", "Manufactura", "Control de Calidad"
    ];

    for (let i = 1; i <= totalQuestions; i++) {
        const topic = topics[(i - 1) % topics.length];
        const questionCard = document.createElement('div');
        questionCard.className = 'question-card';

        // Enlace directo al archivo en la raíz
        const pageLink = `Question_${i}.html`;

        questionCard.innerHTML = `
            <div class="question-number">Pregunta ${i}</div>
            <div class="question-content">
                <h3>${topic} - Pregunta ${i} del FE Mechanical</h3>
                <p>Explicación detallada de la pregunta ${i} del examen FE Mechanical, con solución paso a paso y conceptos clave.</p>
                <a href="${pageLink}" class="view-btn">Ver Explicación</a>
            </div>
        `;
        questionsContainer.appendChild(questionCard);
    }
}

function setupPagination() {
    const questionsPerPage = 12;
    const totalQuestions = 120;
    const totalPages = Math.ceil(totalQuestions / questionsPerPage);
    let currentPage = 1;

    const prevBtn = document.getElementById('prev-page');
    const nextBtn = document.getElementById('next-page');
    const pageNumbersContainer = document.getElementById('page-numbers');

    function generatePageNumbers() {
        pageNumbersContainer.innerHTML = '';
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, startPage + 4);
        if (endPage - startPage < 4) startPage = Math.max(1, endPage - 4);

        for (let i = startPage; i <= endPage; i++) {
            const pageNumber = document.createElement('div');
            pageNumber.className = `page-number ${i === currentPage ? 'active' : ''}`;
            pageNumber.textContent = i;
            pageNumber.addEventListener('click', () => goToPage(i));
            pageNumbersContainer.appendChild(pageNumber);
        }

        prevBtn.disabled = currentPage === 1;
        nextBtn.disabled = currentPage === totalPages;

        showQuestionsForPage(currentPage);
    }

    function showQuestionsForPage(page) {
        const questionCards = document.querySelectorAll('.question-card');
        const startIndex = (page - 1) * questionsPerPage;
        const endIndex = Math.min(startIndex + questionsPerPage, totalQuestions);
        questionCards.forEach((card, index) => {
            card.style.display = (index >= startIndex && index < endIndex) ? 'block' : 'none';
        });
    }

    function goToPage(page) {
        currentPage = page;
        generatePageNumbers();
        document.getElementById('preguntas').scrollIntoView({ behavior: 'smooth' });
    }

    prevBtn.addEventListener('click', () => {
        if (currentPage > 1) goToPage(currentPage - 1);
    });

    nextBtn.addEventListener('click', () => {
        if (currentPage < totalPages) goToPage(currentPage + 1);
    });

    generatePageNumbers();
}

function setupContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('¡Gracias por tu mensaje! Te responderé en breve.');
            contactForm.reset();
        });
    }
}

function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if (this.getAttribute('href') === '#') return;
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({ top: targetElement.offsetTop - 80, behavior: 'smooth' });
                history.pushState(null, null, targetId);
            }
        });
    });
}