from colegio.profesor import Profesor
from colegio.estudiante import Estudiante

opcion = input("eres el profesor o alumno ? ").lower()

if opcion == "profesor":
    usuario = input("ingresa el usuario para entrar: ")
    contraseña = input("ingresa la contraseña : ")
    nota_asignada = float(input("ingresa  la nota"))
    profe_matias = Profesor("matias",nota_asignada,usuario,contraseña)
    profe_matias.login_profesor()
    profe_matias.promedio_notas()
# =====================================
elif opcion == "alumno":
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

else:
    print("no eres ni alumno ni profesor no puedes seguir adelante ")
