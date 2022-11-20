import logging

import azure.functions as func
import math

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

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    b = req.params.get('b')
    a = req.params.get('a')
    


    if a and b:
        integral = integration(float(b), float(a))
        return func.HttpResponse(f"Hello, The integral is.{integral}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

