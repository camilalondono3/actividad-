class Paciente:
  def __init__(self):
    self.__nombre= ""
    self.__cedula = 0
    self.__gener = ""
    self.__servicio = ""

  def ver_nombre(self):
    return self.__nombre
  def ver_servicio(self):
    return self.__servicio
  def ver_genero(self):
    return self.__genero
  def ver_cedula(self):
    return self.__cedula

  def asignar_nombre(self, n):
    self.__nombre = n
  def asignar_servicio(self, s):
    self.__servicio = s
  def asignar_genero(self, g):
    self.__genero = g
  def asignar_cedula(self, c):
    self.__cedula = c

class Sistema:
  def __init__(self):
    self.__lista_pacientes = []
    self.__numero_pacientes = len(self.__lista_pacientes)
  def ingresarPacientes(self):
    #solicitar datos
    nombre = ("Ingrese el nombre: ")
    cedula = ("Ingrese la cedula: ")
    genero = ("Ingrese el genero: ")
    servicio = ("Ingrese el servicio: ")
    # objeto paciente y asignar datos
    p = Paciente()
    p.asignar_nombre(nombre)
    p.asignar_cedula(cedula)
    p.asignar_genero(genero)
    p.asignar_servicio(servicio)
    # guardar paciente
    self.__lista_pacientes.append(p)
    #actualizo
    self.numero_pacientes = len(self.__lista_pacientes)
  def verNumeroPacientes(self):
    return self.__numero_pacientes
  def VerDatosPacientes(self):
    cedula = int(input("Ingrese la ceula que desea buscar: "))
    for paciente in self.__lista_pacientes:
      if cedula == paciente.ver_cedula():
        print("Nombre: " + paciente.ver_nombre())
        print("Cedula: " + str(paciente.ver_cedula()))
        print("Genero: " + paciente.ver_genero())
        print("Servicio: " + paciente.ver_servicio())
mi_sistema = Sistema()
while True:
  opcion = int(input("1. Nuevo paciente - 2. Numero mde pacientes - 3. Datos paciente - 4 salir"))
  if opcion == 1:
    mi_sistema.ingresar_paciente()
  elif opcion == 2:
    print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
  elif opcion == 3:
    mi_sistema.VerDatosPaciente()
  elif opcion == 4:
    break
  else:
    print("Opcion Invalida ")