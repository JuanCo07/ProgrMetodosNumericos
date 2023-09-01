from sympy import diff
from math import sin, cos

class Trapezoidal:
    @staticmethod
    def simple(function, lower_limit, upper_limit):
        h = upper_limit - lower_limit
        result = (h / 2) * (eval(function, {"x": lower_limit}) + eval(function, {"x": upper_limit}))
        error = Trapezoidal.calculate_error(function, lower_limit, upper_limit, 1)
        return result, error

    @staticmethod
    def composite(function, lower_limit, upper_limit, intervals):
        h = (upper_limit - lower_limit) / intervals
        x_values = [lower_limit + i * h for i in range(intervals + 1)]
        y_values = [eval(function, {"x": x}) for x in x_values]
        result = (h / 2) * (y_values[0] + 2 * sum(y_values[1:-1]) + y_values[-1])
        error = Trapezoidal.calculate_error(function, lower_limit, upper_limit, intervals)
        return result, error

    @staticmethod
    def calculate_error(function, lower_limit, upper_limit, intervals):
        second_derivative = eval(f"abs({diff(diff(function)).simplify()})")
        max_second_derivative = max([eval(str(second_derivative), {"x": x}) for x in [lower_limit, upper_limit]])
        error = (max_second_derivative * ((upper_limit - lower_limit) * 3)) / (12 * (intervals * 2))
        return error

try:
  function = input("Ingrese la función a integrar: ")
  lower_limit = float(input("Ingrese el límite inferior: "))
  upper_limit = float(input("Ingrese el límite superior: "))
  intervals = int(input("Ingrese el número de intervalos: "))
  if intervals == 1:
      result, error = Trapezoidal.simple(function, lower_limit, upper_limit)
  elif intervals >1:
      result, error = Trapezoidal.composite(function, lower_limit, upper_limit, intervals)
  else :
      handle_input_error()
  Plotter.plot_trapezoidal(function, lower_limit, upper_limit, intervals)
  print(f"El resultado aproximado es: {result}")
  print(f"El porcentaje de error es: {error}%")
except ValueError:
  handle_input_error()

# result, error = Trapezoidal.simple("x**2", 0, 1)
# print(f"Resultado: {result}")
# print(f"Error: {error}")