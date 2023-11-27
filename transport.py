class NanoRobot:
  def __init__(self, initial_x, initial_y):
      self.x = initial_x
      self.y = initial_y
      self.nutriente = None

  def move(self, delta_x, delta_y):
      self.x += delta_x
      self.y += delta_y

  def tomar_nutriente(self, nutriente):
      self.nutriente = nutriente

  def soltar_nutriente(self):
      nutriente = self.nutriente
      self.nutriente = None
      return nutriente

  def get_position(self):
      return self.x, self.y

# Crear un nanorobot en la posición (0, 0)
nano_robot = NanoRobot(0, 0)

# Simular un recorrido y recoger un nutriente
nano_robot.move(1, 0)
nano_robot.move(0, 1)
nano_robot.tomar_nutriente("Nutriente A")

# Simular otro recorrido y soltar el nutriente
nano_robot.move(1, 1)
nutriente_recogido = nano_robot.soltar_nutriente()

# Obtener la posición actual y el estado del nutriente
posicion_actual = nano_robot.get_position()
print("Posición actual: X =", posicion_actual[0], "Y =", posicion_actual[1])
print("Nutriente recogido:", nutriente_recogido)
