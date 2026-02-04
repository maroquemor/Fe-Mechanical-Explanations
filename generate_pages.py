# generate_pages.py - Script para generar páginas de preguntas FE Mechanical
# Para GitHub: https://github.com/tu-usuario/fe-mechanical-explanations

import os

def crear_estructura_carpetas():
    """Crea las carpetas necesarias si no existen"""
    carpetas_necesarias = ['preguntas', 'assets/images', 'assets/css']
    
    for carpeta in carpetas_necesarias:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"✓ Carpeta creada: {carpeta}")
        else:
            print(f"✓ Carpeta ya existe: {carpeta}")

def generar_pagina_pregunta(numero):
    """Genera el HTML para una pregunta específica"""
    
    # Temas variados para las preguntas (para hacerlas más realistas)
    temas = [
        "Termodinámica",
        "Mecánica de Materiales", 
        "Dinámica de Fluidos",
        "Transferencia de Calor",
        "Diseño Mecánico",
        "Estática",
        "Dinámica",
        "Manufactura",
        "Control de Calidad",
        "Mecánica de Sólidos"
    ]
    
    # Seleccionar tema basado en el número de pregunta (para consistencia)
    tema_idx = (numero - 1) % len(temas)
    tema = temas[tema_idx]
    
    # Diferentes tipos de preguntas
    tipos_preguntas = [
        f"Calcular la eficiencia térmica de un ciclo {tema.lower()}",
        f"Determinar el esfuerzo en un componente bajo carga {tema.lower()}",
        f"Analizar el flujo de fluidos en un sistema {tema.lower()}",
        f"Calcular la transferencia de calor en {tema.lower()}",
        f"Diseñar un componente para {tema.lower()}",
        f"Resolver un problema de equilibrio estático en {tema.lower()}",
        f"Analizar el movimiento en {tema.lower()}",
        f"Optimizar un proceso de {tema.lower()}",
        f"Aplicar control de calidad en {tema.lower()}",
        f"Evaluar propiedades de materiales en {tema.lower()}"
    ]
    
    pregunta_idx = (numero - 1) % len(tipos_preguntas)
    descripcion_pregunta = tipos_preguntas[pregunta_idx]
    
    # Plantilla HTML
    html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Explicación detallada de la Pregunta {numero} del examen FE Mechanical - {tema}">
    <meta name="keywords" content="FE Mechanical, ingeniería mecánica, examen FE, {tema}, pregunta {numero}">
    <title>Pregunta {numero} - FE Mechanical | {tema}</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .question-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .question-header {{
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        
        .question-header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
        }}
        
        .question-meta {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .meta-item {{
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: 600;
        }}
        
        .question-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }}
        
        @media (max-width: 768px) {{
            .question-content {{
                grid-template-columns: 1fr;
            }}
        }}
        
        .question-box, .solution-box {{
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }}
        
        .question-box {{
            border-left: 5px solid #3498db;
        }}
        
        .solution-box {{
            border-left: 5px solid #2ecc71;
        }}
        
        .section-title {{
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #eee;
        }}
        
        .formula {{
            font-family: 'Courier New', monospace;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            border-left: 4px solid #3498db;
            font-size: 1.1rem;
        }}
        
        .step {{
            margin-bottom: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }}
        
        .step-number {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            text-align: center;
            line-height: 30px;
            margin-right: 10px;
            font-weight: bold;
        }}
        
        .answer-card {{
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 30px 0;
        }}
        
        .answer-title {{
            font-size: 1.8rem;
            margin-bottom: 15px;
        }}
        
        .answer {{
            font-size: 1.5rem;
            font-weight: bold;
            margin: 20px 0;
        }}
        
        .concepts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .concept-card {{
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
            border-top: 4px solid #f39c12;
        }}
        
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
        
        .nav-button {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 12px 25px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 600;
            transition: background-color 0.3s;
        }}
        
        .nav-button:hover {{
            background-color: #2980b9;
        }}
        
        .nav-button.prev {{
            background-color: #7f8c8d;
        }}
        
        .nav-button.prev:hover {{
            background-color: #95a5a6;
        }}
        
        .print-button {{
            display: inline-block;
            padding: 12px 25px;
            background-color: #2c3e50;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 20px;
            transition: background-color 0.3s;
        }}
        
        .print-button:hover {{
            background-color: #34495e;
        }}
        
        .question-text {{
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        
        .options-list {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        .options-list li {{
            padding: 10px 15px;
            margin-bottom: 10px;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-left: 4px solid #bdc3c7;
        }}
        
        .options-list li.correct {{
            border-left-color: #2ecc71;
            background-color: #e8f8f1;
        }}
        
        .navigation-home {{
            margin-bottom: 20px;
        }}
        
        .back-home {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 600;
            transition: background-color 0.3s;
        }}
        
        .back-home:hover {{
            background-color: #2980b9;
        }}
    </style>
</head>
<body>
    <div class="question-container">
        <div class="navigation-home">
            <a href="../index.html#preguntas" class="back-home">
                <i class="fas fa-arrow-left"></i> Volver al Listado de Preguntas
            </a>
        </div>
        
        <div class="question-header">
            <h1>Pregunta {numero} - FE Mechanical</h1>
            <p>Explicación detallada paso a paso</p>
            <div class="question-meta">
                <div class="meta-item"><i class="fas fa-book"></i> {tema}</div>
                <div class="meta-item"><i class="fas fa-clock"></i> Tiempo estimado: 5-7 min</div>
                <div class="meta-item"><i class="fas fa-chart-bar"></i> Dificultad: Media</div>
            </div>
        </div>
        
        <div class="question-content">
            <div class="question-box">
                <h2 class="section-title"><i class="fas fa-question-circle"></i> Enunciado de la Pregunta</h2>
                <div class="question-text">
                    <p><strong>Pregunta {numero}:</strong> {descripcion_pregunta}.</p>
                    
                    <p>Datos proporcionados:</p>
                    <ul>
                        <li>Parámetro A: Valor {numero * 2}</li>
                        <li>Parámetro B: Valor {numero * 3}</li>
                        <li>Condición inicial: Estado {numero}</li>
                    </ul>
                </div>
                
                <h3 class="section-title">Opciones de Respuesta</h3>
                <ul class="options-list">
                    <li>A. Opción A para pregunta {numero}</li>
                    <li>B. Opción B para pregunta {numero}</li>
                    <li class="correct">C. Opción C para pregunta {numero} (Correcta)</li>
                    <li>D. Opción D para pregunta {numero}</li>
                </ul>
            </div>
            
            <div class="solution-box">
                <h2 class="section-title"><i class="fas fa-lightbulb"></i> Solución Paso a Paso</h2>
                
                <div class="step">
                    <div class="step-number">1</div>
                    <strong>Identificar el tipo de problema</strong>
                    <p>Este es un problema típico de {tema.lower()} que aparece frecuentemente en el examen FE Mechanical.</p>
                </div>
                
                <div class="step">
                    <div class="step-number">2</div>
                    <strong>Recordar las fórmulas relevantes</strong>
                    <p>Para resolver este problema, necesitamos aplicar la fórmula principal de {tema.lower()}:</p>
                    <div class="formula">
                        Fórmula {numero}: A = B × C + D
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">3</div>
                    <strong>Sustituir valores y calcular</strong>
                    <p>Sustituimos los valores dados en la fórmula:</p>
                    <div class="formula">
                        A = ({numero * 2}) × ({numero * 3}) + {numero}
                    </div>
                    <div class="formula">
                        A = {numero * 2 * numero * 3} + {numero} = {(numero * 2 * numero * 3) + numero}
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">4</div>
                    <strong>Interpretar el resultado</strong>
                    <p>El valor calculado de {((numero * 2 * numero * 3) + numero)} corresponde a la Opción C.</p>
                </div>
            </div>
        </div>
        
        <div class="answer-card">
            <div class="answer-title">Respuesta Correcta</div>
            <div class="answer">Opción C</div>
            <p>La respuesta correcta es la Opción C, que corresponde al valor calculado de {((numero * 2 * numero * 3) + numero)}.</p>
        </div>
        
        <div class="solution-box">
            <h2 class="section-title"><i class="fas fa-graduation-cap"></i> Conceptos Clave</h2>
            <div class="concepts-grid">
                <div class="concept-card">
                    <h3>Concepto 1: Fundamentos de {tema}</h3>
                    <p>Explicación breve del concepto fundamental aplicado en esta pregunta.</p>
                </div>
                <div class="concept-card">
                    <h3>Concepto 2: Aplicación Práctica</h3>
                    <p>Cómo este concepto se aplica en problemas de ingeniería del mundo real.</p>
                </div>
                <div class="concept-card">
                    <h3>Concepto 3: Errores Comunes</h3>
                    <p>Los errores típicos que los estudiantes cometen al resolver este tipo de problemas.</p>
                </div>
            </div>
            
            <h3 class="section-title" style="margin-top: 30px;">Aplicación en Ingeniería Mecánica</h3>
            <p>Este tipo de problema tiene aplicaciones directas en:</p>
            <ul>
                <li>Diseño de sistemas {tema.lower()}</li>
                <li>Análisis de eficiencia energética</li>
                <li>Optimización de procesos industriales</li>
                <li>Control de calidad en manufactura</li>
            </ul>
        </div>
        
        <div class="nav-buttons">
            {f'<a href="pregunta-{numero-1}.html" class="nav-button prev"><i class="fas fa-chevron-left"></i> Pregunta {numero-1}</a>' if numero > 6 else f'<a href="../Question_{numero-1}.html" class="nav-button prev"><i class="fas fa-chevron-left"></i> Pregunta {numero-1}</a>' if numero > 1 else '<div></div>'}
            
            <a href="../index.html#preguntas" class="nav-button"><i class="fas fa-home"></i> Volver al Inicio</a>
            
            {f'<a href="pregunta-{numero+1}.html" class="nav-button">Pregunta {numero+1} <i class="fas fa-chevron-right"></i></a>' if numero < 100 else '<div></div>'}
        </div>
        
        <div style="text-align: center; margin-top: 30px;">
            <a href="javascript:window.print()" class="print-button">
                <i class="fas fa-print"></i> Imprimir o Guardar como PDF
            </a>
        </div>
    </div>

    <script>
        // JavaScript para funcionalidades adicionales
        document.addEventListener('DOMContentLoaded', function() {{
            // Resaltar la opción correcta
            const correctOption = document.querySelector('.options-list li.correct');
            if (correctOption) {{
                correctOption.innerHTML = '<i class="fas fa-check-circle" style="color: #2ecc71; margin-right: 8px;"></i>' + correctOption.innerHTML;
            }}
            
            // Agregar funcionalidad de teclado para navegación
            document.addEventListener('keydown', function(e) {{
                if (e.key === 'ArrowLeft' && {numero} > 1) {{
                    if ({numero} > 6) {{
                        window.location.href = 'pregunta-' + ({numero} - 1) + '.html';
                    }} else if ({numero} > 1) {{
                        window.location.href = '../Question_' + ({numero} - 1) + '.html';
                    }}
                }} else if (e.key === 'ArrowRight' && {numero} < 100) {{
                    if ({numero} >= 6) {{
                        window.location.href = 'pregunta-' + ({numero} + 1) + '.html';
                    }} else {{
                        window.location.href = '../Question_' + ({numero} + 1) + '.html';
                    }}
                }} else if (e.key === 'Escape') {{
                    window.location.href = '../index.html#preguntas';
                }}
            }});
            
            // Mostrar mensaje de ayuda
            console.log('Pregunta {numero} de 100 - Navega con las flechas izquierda/derecha');
        }});
    </script>
</body>
</html>'''
    
    return html_template

def main():
    """Función principal del script"""
    print("=" * 60)
    print("GENERADOR DE PÁGINAS FE MECHANICAL PARA GITHUB")
    print("=" * 60)
    
    # 1. Crear estructura de carpetas
    print("\n1. Creando estructura de carpetas...")
    crear_estructura_carpetas()
    
    # 2. Verificar que la carpeta de preguntas existe
    if not os.path.exists('preguntas'):
        print("✗ Error: No se pudo crear la carpeta 'preguntas'")
        return
    
    # 3. Generar las páginas 7 a 100 (las 1-6 ya existen)
    print(f"\n2. Generando páginas 7 a 100...")
    archivos_generados = 0
    
    for i in range(7, 101):
        # Generar el contenido HTML
        html_content = generar_pagina_pregunta(i)
        
        # Nombre del archivo
        filename = f"preguntas/pregunta-{i}.html"
        
        # Escribir el archivo
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(html_content)
            archivos_generados += 1
            print(f"   ✓ Pregunta {i:3d}: {filename}")
        except Exception as e:
            print(f"   ✗ Error al crear {filename}: {e}")
    
    # 4. Crear un archivo índice para las preguntas
    print(f"\n3. Creando índice de preguntas...")
    crear_indice_preguntas()
    
    # 5. Mostrar resumen
    print(f"\n" + "=" * 60)
    print("RESUMEN DE LA GENERACIÓN")
    print("=" * 60)
    print(f"✓ Páginas generadas: {archivos_generados}/94 (7-100)")
    print(f"✓ Páginas existentes: 6 (1-6)")
    print(f"✓ Total de preguntas: 100")
    print(f"✓ Carpeta principal: fe-mechanical-explanations/")
    print(f"✓ Subcarpeta: preguntas/ (preguntas 7-100)")
    print(f"✓ Archivo índice: preguntas/indice.txt")
    print("\nSiguientes pasos para GitHub:")
    print("1. git add .")
    print("2. git commit -m 'Agregar 100 preguntas FE Mechanical'")
    print("3. git push origin main")
    print("\n¡Listo para subir a GitHub! 🚀")

def crear_indice_preguntas():
    """Crea un archivo de índice con todas las preguntas"""
    temas = ["Termodinámica", "Mecánica de Materiales", "Dinámica de Fluidos", 
             "Transferencia de Calor", "Diseño Mecánico", "Estática", 
             "Dinámica", "Manufactura", "Control de Calidad", "Mecánica de Sólidos"]
    
    with open("preguntas/indice.txt", "w", encoding="utf-8") as f:
        f.write("ÍNDICE DE PREGUNTAS FE MECHANICAL\n")
        f.write("=" * 40 + "\n\n")
        
        for i in range(1, 101):
            tema_idx = (i - 1) % len(temas)
            tema = temas[tema_idx]
            
            if i <= 6:
                f.write(f"Pregunta {i:3d}: {tema:25} -> ../Question_{i}.html\n")
            else:
                f.write(f"Pregunta {i:3d}: {tema:25} -> pregunta-{i}.html\n")

if __name__ == "__main__":
    main()