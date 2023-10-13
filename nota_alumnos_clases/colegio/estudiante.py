class Estudiante:
    def __init__(self,nombre_estudiante , apellido_estudiante, nota_estudiante):
        self.nombre_estudiante = nombre_estudiante
        self.apellido_estudiante = apellido_estudiante
        self.nota_estudiante = nota_estudiante
    def login_estudiante(self):
        usuario_list = []
        contraseña_list = []
        for i in range(1):
            usuario = input("ingresa usuario")
            usuario_list.append(usuario)
            contraseña = input("ingresa contraseña : ")
            contraseña_list.append(contraseña)
            if "matias" in usuario_list and "1234" in contraseña_list:
                print("iniciaste correctamente")
            elif  "Benjamin" in usuario_list and "1234" in contraseña_list:
                print("iniciaste correctamente")
            elif "Kevin" in usuario_list and "1234" in contraseña_list:
                print("iniciaste correctamente")
            elif"Nico" in usuario_list and "1234" in contraseña_list:
                print("iniciaste correctamente")
            elif "Lucas" in usuario_list and "1234" in contraseña_list:
                print("iniciaste correctamente")
            else:
                print("no estas registrado")
                break
    def carrera(self):
        carrera_list = []
        asignatura_list = []
        for i in range(5):
            carreras = input("ingresa carrera :")
            carrera_list.append(carreras)
            asignatura = input("ingresa asignaturas : ")
            asignatura_list.append(asignatura)
        for j in range(5):
            print(f"la carrera es {carrera_list[j]} y su asignatura es : {asignatura_list[j]}")
    def promedio_notas(self):
        promedio = 0
        for i in range(3):
            promedio += self.nota_estudiante
        promedio/=3
        if promedio <= 3.0:
            print("Reprobado")

        elif promedio >= 3.0 and promedio < 4.9:
            print("Debe rendir examen")

        elif promedio > 4.9:
            print("Aprobado")
