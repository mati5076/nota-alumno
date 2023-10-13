class Profesor:
    def __init__(self, nombre_profesor , nota_alumno , usuario , contraseña):
        self.nombre_profesor = nombre_profesor
        self.nota_alumno = nota_alumno
        self.usuario = usuario
        self.contraseña = contraseña

    def login_profesor(self):
        if self.nombre_profesor == "matias" and self.contraseña.isalnum() <= 8:
            print("iniciaste sesion...")
        else :
            print("error")

    def promedio_notas(self):
        promedio = 0
        for i in range(3):
            promedio += self.nota_estudiante
        promedio/=3
        print(f"el promedio es de {promedio}")
