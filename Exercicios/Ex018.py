import math
ângulo = float(input('Digite um ângulo'))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem: \n o SENO de {:.2f} \n o cosseno de {:.2f}\n a tangente de {:.2f}'.format(ângulo,seno,cosseno,tangente))

