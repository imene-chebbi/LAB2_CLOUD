import math
from flask import Flask

app = Flask(__name__)

@app.route('/numericalintegralservice/<b>/<a>')
def integration(b, a):
  result = {}
  L=[10,100,1000,10000,100000]

  for n in L:
    h = (float(a) - float(b))/n
    integral = 0
    for i in range(n):
      x2 = float(b) + h*(i+0.5)
      I = abs(math.sin(x2))*h
      integral += I
    result[n] = integral
  return result
