document.addEventListener('DOMContentLoaded', function () {
    // Limpiar formulario
    const limpiarBtn = document.getElementById('limpiar');
    if (limpiarBtn) {
        limpiarBtn.addEventListener('click', function () {
            document.querySelector('.cifrado-form').reset();
        });
    }

    // Generador de clave automática (existente)
    document.getElementById('generar-clave').addEventListener('click', function () {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
        let clave = '';
        for (let i = 0; i < 32; i++) {
            clave += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        document.getElementById('clave').value = clave;
    });

    // Copiar resultado
    const copiarResultado = document.getElementById('copiar-resultado');
    if (copiarResultado) {
        copiarResultado.addEventListener('click', function () {
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

    // Descargar resultado
    const descargarResultado = document.getElementById('descargar-resultado');
    if (descargarResultado) {
        descargarResultado.addEventListener('click', function () {
            const resultado = document.querySelector('.hex-result');
            if (resultado) {
                const blob = new Blob([resultado.textContent], { type: 'text/plain' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'texto_cifrado.txt';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }
        });
    }

    // Validación del formulario
    document.querySelector('.cifrado-form').addEventListener('submit', function (e) {
        const clave = document.getElementById('clave').value;
        if (document.querySelector('input[name="modo"]:checked').value === 'cifrar' && clave.length !== 32) {
            e.preventDefault();
            alert('Para AES-256, la clave debe tener exactamente 32 caracteres');
            return false;
        }
        return true;
    });

    const keyInput = document.getElementById('clave');
    const charCount = document.querySelector('.key-char-count');

    // Actualizar contador de caracteres
    keyInput.addEventListener('input', function() {
        const currentLength = this.value.length;
        charCount.textContent = `${currentLength}/32`;
        
        // Cambiar color si alcanza el límite
        if (currentLength === 32) {
            charCount.style.color = 'var(--success-color)';
        } else {
            charCount.style.color = 'var(--text-light)';
        }
    });

});

