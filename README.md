-> Descripción del módulo (Courses and Resources):

Nuestro módulo consta de dos grandes bloques: la sección de cursos y el detalle de los mismos y la sección del formador. 
En la primera sección, se van a listar los cursos junto a un filtro para facilitar la búsqueda deseada por parte del usuario y se podrá acceder al detalle de cada uno de los cursos. Además, hemos reforzado esta sección con un sistema de recomendaciones elaborado con inteligencia artificial mediante el uso de un modelo de KNN dónde el usuario recibe recomendaciones basadas en perfiles similares al suyo dentro de la misma página. 
Por otro lado, tenemos la sección dónde los profesores tienen un CRUD para la gestión de los cursos. En el dashboard del profesor pueden crear, editar o eliminar los sus cursos y también tienen un pequeño apartado de estadísticas en relación a los mismos.

-> Funciones y características:

1. Listar cursos y ver el detalle de cada uno de ellos.
2. Filtrar por los campos del mismo modelo.
3. Apuntarse a un curso y redigir al dashboard del alumno.
4. Posibilidad de dar me gusta a un curso o recurso que a su vez servirá como parámetro para la recomendación.
5. Sistema de recomendaciones con KNN para cada usuario.
6. Apartado para crear, editar y borrar los cursos de un perfil de profesor.
7. Dashboard personalizada para los profesores.
8. Chatbot para resolver FAQS por parte de los usuarios.
9. Listado de recursos que tengan relación o no con las lecciones.
10. Apartado para elaboración de reviews por parte del usuario a los cursos, con la posibilidad de dar un rating del 1 al 5 y un comentario.

-> Dependencias necesarias.

Instalación del requirements.txt   (y añadir)
faker (populate_cursos para elaborar una fake data)
scikit-learn
pandas
nltk
tensorflow


-> Interacción del módulo con el resto:

Con la sección de Profile_CV:

Estos módulos están en estrecho contacto dado que la información que se obtiene desdel perfil del usuario es la que se va a emplear para mostrar los datos en el dashboard del alumno y, por ejemplo, la foto del usuario que deja un comentario en un curso. Las certificaciones que se obtienen de los cursos pasarán posteriormente a la creación de CV's dinámicos. 

Con la sección de Test_management:

La sección de test se encarga de validar que los conocimientos adquiridos en los cursos que el usuario haya llevado a cabo son satisfactorios. Sería como la parte de "examinación" o "autoevaluación" para el usuario. Además, también potenciarán las softskills que de la mano de sus capacidades técnicas crearán un perfil más completo del usuario.

Con la sección de HeadHunters:

En la sección de búsqueda de ofertas laborales las hardskills requeridas por las empresas o cazatalentos serán las que el apartado de cursos deba satisfacer para que se produzca un encuentro de perfiles adecuados a cada oferta.
Por otra parte, los headhunters tendrán la posibilidad de poder ver el progreso del usuario que puede interesarles comprobando los certificados que ha obtenido de los cursos que ha terminado.

-> Rama de la sección de cursos:

G3B