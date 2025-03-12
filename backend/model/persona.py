class Persona:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}\\nApellido: {self.apellido}\\nCorreo: {self.correo}"