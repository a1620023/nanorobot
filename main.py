class NanoRobot:
  def __init__(self, initial_x, initial_y):
      self.x = initial_x
      self.y = initial_y

  def move(self, delta_x, delta_y):
      self.x += delta_x
      self.y += delta_y

  def get_position(self):
      return self.x, self.y

# Crear un nanorobot en la posición (0, 0)
nano_robot = NanoRobot(0, 0)

# Simular un recorrido
nano_robot.move(1, 0)
nano_robot.move(0, 1)
nano_robot.move(1, 1)

# Obtener la posición actual
posicion_actual = nano_robot.get_position()
print("Posición actual: X =", posicion_actual[0], "Y =", posicion_actual[1])
