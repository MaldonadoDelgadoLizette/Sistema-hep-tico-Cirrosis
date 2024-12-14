

# Sistema hepático

## Estudiantes
Beltrán Vega Sofía, Díaz Muruaga Carlos Manuel, Maldonado Delgado Lizette 
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: l21212143@tectijuana.edu.mx; l21212741@tectijuana.edu.mx, l21212168@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El hígado juega un papel fundamental en el metabolismo de toxinas y medicamentos.  En las enfermedades hepáticas crónicas, particularmente en la cirrosis, las alteraciones anatómicas del hígado presentan modificaciones en la circulación intrahepática que puede influir también en el metabolismo los fármacos, ya que se reduce la actividad enzimática y disminuye por tanto la depuración intrínseca de éstos.
El circuito RLC se basa en la idea de que el hígado es un filtro metabólico que procesa sustancias (medicamentos, toxinas) que llegan a él a través del sistema sanguíneo. A medida que estas sustancias pasan por el hígado, son metabolizadas y almacenadas temporalmente. Finalmente, las sustancias metabolizadas son liberadas al flujo sanguíneo.
El flujo sanguíneo hacia el hígado es representado por el resistor  R1​, que es baja en un paciente sano y alta en un paciente con cirrosis, simulando la circulación restringida. El resistor R2​ refleja el metabolismo hepático; en el paciente sano, es baja, indicando un metabolismo eficiente, y alta en el paciente con cirrosis, lo que simboliza un metabolismo más lento. El inductor L1​ representa el retardo metabólico: en el paciente sano es bajo, permitiendo un proceso rápido, mientras que en el paciente con cirrosis es alto, indicando un mayor retraso. El capacitor C1 Almacena las toxinas temporalmente; en el paciente sano tiene alta capacidad, mientras que en el enfermo, la capacidad es reducida. Finalmente, el capacitor C2 modela la excreción: en el paciente sano tiene alta capacidad, lo que permite una excreción rápida, y baja en el paciente con cirrosis, reflejando una excreción más lenta.
La señal de entrada representa la concentración de medicamentos administrada a través del tiempo y se representa como Vin (t), la salida representa la concentración de la sustancia metabolizada o residual en la sangre.

## Referencias principales
[1] R. Bravo Coello, C. Monar Goyes, V. Pacheco Moreira, y C. R. Cumanda, Eds., Clinical and therapeutic management in a patients with hepatic cirrhosis, vol. 7, núm. 4. Diciembre Especial 2021, pp. 90–112. Revista científica dominio de las ciencias, 4 de diciembre de 2021.

