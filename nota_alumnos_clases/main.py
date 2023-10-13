from colegio.profesor import Profesor
from colegio.estudiante import Estudiante

usuario = input("ingresa el usuario para entrar: ")

contraseña = input("ingresa la contraseña : ")

profe_matias = Profesor("matias",3.5,usuario,contraseña)

profe_matias.login_profesor()

alumno_matias = Estudiante("matias" , "montecinos",3.5)
alumno_nico = Estudiante("nicolas" , "ojeda",6.6)
alumno_kevin = Estudiante("kevin" , "ibarra",6.1)
alumno_lucas = Estudiante("lucas" , "montecinos",5.0)
alumno_benja = Estudiante("benjamin" , "Sotomayor",2.0)

alumno_matias.login_estudiante()
alumno_matias.carrera()
alumno_matias.promedio_notas()

alumno_nico.login_estudiante()
alumno_nico.carrera()
alumno_nico.promedio_notas()


alumno_kevin.login_estudiante()
alumno_kevin.carrera()
alumno_kevin.promedio_notas()

alumno_lucas.login_estudiante()
alumno_lucas.carrera()
alumno_lucas.promedio_notas()

alumno_benja.login_estudiante()
alumno_benja.carrera()
alumno_benja.promedio_notas()
