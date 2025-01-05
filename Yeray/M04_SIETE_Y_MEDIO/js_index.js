window.addEventListener('load', function() { 
    document.querySelectorAll('.portada h1, .portada p').forEach(function(
        element) { element.style.opacity = 1; 

        }); 
    });
    document.addEventListener('scroll', function() {
         const texto = document.querySelector('.texto-apareciendo'); 
         const posicion = texto.getBoundingClientRect().top; 
         const windowHeight = window.innerHeight; 
         if (posicion < windowHeight) { texto.classList.add('visible'); 

         } else { 
            texto.classList.remove('visible'); 
        }
    });