document.addEventListener('DOMContentLoaded', function() {
    // Limpiar formulario
    const limpiarBtn = document.getElementById('limpiar');
    if (limpiarBtn) {
        limpiarBtn.addEventListener('click', function() {
            document.querySelector('.cifrado-form').reset();
        });
    }

    // Copiar resultado
    const copiarResultado = document.getElementById('copiar-resultado');
    if (copiarResultado) {
        copiarResultado.addEventListener('click', function() {
            const resultado = document.querySelector('.hex-result') || document.querySelector('.text-result');
            if (resultado) {
                navigator.clipboard.writeText(resultado.textContent)
                    .then(() => {
                        const originalText = copiarResultado.innerHTML;
                        copiarResultado.innerHTML = '<i class="icon-check"></i> Copiado';
                        setTimeout(() => {
                            copiarResultado.innerHTML = originalText;
                        }, 2000);
                    })
                    .catch(err => {
                        console.error('Error al copiar: ', err);
                    });
            }
        });
    }

    // Validación del formulario
    const form = document.querySelector('.cifrado-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const texto = document.getElementById('texto').value.trim();
            const clave = document.getElementById('clave').value.trim();
            
            if (!texto || !clave) {
                e.preventDefault();
                alert('Por favor completa todos los campos requeridos');
                return false;
            }
            
            return true;
        });
    }
});