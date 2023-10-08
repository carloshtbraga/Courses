document.addEventListener('DOMContentLoaded', function() {
    const is_instructor = document.getElementById('is_instructor');
    const biographyField = document.getElementById('biography-field');
    const fotoField = document.getElementById('foto-field');
    const imagemInput = document.getElementById('imagem');

    is_instructor.addEventListener('change', () => {
        if (is_instructor.value === '1') {
            biographyField.style.display = 'block';
            fotoField.style.display = 'block';
            imagemInput.required = true;
        } else {
            biographyField.style.display = 'none';
            fotoField.style.display = 'none';
            imagemInput.required = false;
        }
    });
});
