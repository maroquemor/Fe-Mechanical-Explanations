// Script para la página de inicio
document.addEventListener('DOMContentLoaded', function() {
    // Generar las 100 preguntas
    generateQuestions();
    
    // Configurar paginación
    setupPagination();
    
    // Configurar formulario de contacto
    setupContactForm();
    
    // Configurar navegación suave
    setupSmoothScrolling();
});

// Generar las 100 preguntas
function generateQuestions() {
    const questionsContainer = document.getElementById('questions-container');
    const totalQuestions = 100;
    
    // Temas para las preguntas
    const topics = [
        "Matemáticas", "Estática", "Dinámica", "Mecánica de Materiales",
        "Termodinámica", "Transferencia de Calor", "Diseño Mecánico",
        "Dinámica de Fluidos", "Manufactura", "Control de Calidad"
    ];
    
    // Generar las preguntas
    for (let i = 1; i <= totalQuestions; i++) {
        // Seleccionar un tema basado en el número
        const topic = topics[(i - 1) % topics.length];
        
        // Crear el elemento de la pregunta
        const questionCard = document.createElement('div');
        questionCard.className = 'question-card';
        
        // Determinar la ruta de la pregunta
        let pageLink = '';
        let pageExists = false;
        
        if (i <= 6) {
            // Para las primeras 6 preguntas, usar archivos en raíz
            pageLink = `Question_${i}.html`;
            pageExists = true;
        } else {
            // Para preguntas 7-100, usar archivos en carpeta preguntas/
            pageLink = `preguntas/pregunta-${i}.html`;
            pageExists = true; // Asumir que serán generadas
        }
        
        questionCard.innerHTML = `
            <div class="question-number">Pregunta ${i}</div>
            <div class="question-content">
                <h3>${topic} - Pregunta ${i} del FE Mechanical</h3>
                <p>Explicación detallada de la pregunta ${i} del examen FE Mechanical, con solución paso a paso y conceptos clave.</p>
                ${pageExists ? 
                    `<a href="${pageLink}" class="view-btn">Ver Explicación</a>` : 
                    `<span class="view-btn" style="background-color:#95a5a6; cursor:not-allowed;">Próximamente</span>`
                }
            </div>
        `;
        
        questionsContainer.appendChild(questionCard);
    }
}

// Configurar paginación
function setupPagination() {
    const questionsPerPage = 12;
    const totalQuestions = 100;
    const totalPages = Math.ceil(totalQuestions / questionsPerPage);
    let currentPage = 1;
    
    const prevBtn = document.getElementById('prev-page');
    const nextBtn = document.getElementById('next-page');
    const pageNumbersContainer = document.getElementById('page-numbers');
    
    // Generar números de página
    function generatePageNumbers() {
        pageNumbersContainer.innerHTML = '';
        
        // Mostrar máximo 5 números de página
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, startPage + 4);
        
        // Ajustar si estamos cerca del final
        if (endPage - startPage < 4) {
            startPage = Math.max(1, endPage - 4);
        }
        
        // Generar botones de página
        for (let i = startPage; i <= endPage; i++) {
            const pageNumber = document.createElement('div');
            pageNumber.className = `page-number ${i === currentPage ? 'active' : ''}`;
            pageNumber.textContent = i;
            pageNumber.addEventListener('click', () => goToPage(i));
            pageNumbersContainer.appendChild(pageNumber);
        }
        
        // Actualizar estado de botones
        prevBtn.disabled = currentPage === 1;
        nextBtn.disabled = currentPage === totalPages;
        
        // Mostrar/ocultar preguntas según la página
        showQuestionsForPage(currentPage);
    }
    
    // Mostrar preguntas para una página específica
    function showQuestionsForPage(page) {
        const questionCards = document.querySelectorAll('.question-card');
        const startIndex = (page - 1) * questionsPerPage;
        const endIndex = Math.min(startIndex + questionsPerPage, totalQuestions);
        
        questionCards.forEach((card, index) => {
            if (index >= startIndex && index < endIndex) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    // Ir a una página específica
    function goToPage(page) {
        currentPage = page;
        generatePageNumbers();
        
        // Desplazarse suavemente a la sección de preguntas
        document.getElementById('preguntas').scrollIntoView({ behavior: 'smooth' });
    }
    
    // Configurar botones de paginación
    prevBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            goToPage(currentPage - 1);
        }
    });
    
    nextBtn.addEventListener('click', () => {
        if (currentPage < totalPages) {
            goToPage(currentPage + 1);
        }
    });
    
    // Generar la paginación inicial
    generatePageNumbers();
}

// Configurar formulario de contacto
function setupContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Aquí normalmente enviarías el formulario a un servidor
            // Por ahora, solo mostraremos un mensaje de confirmación
            alert('¡Gracias por tu mensaje! Te responderé en breve.');
            contactForm.reset();
        });
    }
}

// Configurar navegación suave
function setupSmoothScrolling() {
    // Seleccionar todos los enlaces que apuntan a anclas
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            // Excluir enlaces que no sean para navegación interna
            if (this.getAttribute('href') === '#') return;
            
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Desplazamiento suave
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Actualizar URL sin recargar la página
                history.pushState(null, null, targetId);
            }
        });
    });
}