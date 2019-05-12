print("--- Bem-vindo ao programa de Retífica ---")
print("Informe as medidas STD, e as medidas encontradas no munhão e moente")

primeira_medida = 0.250
segunda_medida = 0.500
terceira_medida = 0.750
quarta_medida = 1.000

munhao = float(input("Medida do munhão STD: "))
munhaoMedido = float(input("Medida encontrada no munhão: "))

resultado = munhao - munhaoMedido
if (resultado <= primeira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado,primeira_medida))
elif (resultado > primeira_medida and resultado < segunda_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado,segunda_medida))
elif (resultado > segunda_medida and resultado < terceira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado,terceira_medida))
else:
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado,quarta_medida))

moente = float(input("Medida do moente STD: "))
moenteMedido = float(input("Medida encontrada no moente: "))

resultado2 = moente - moenteMedido

if (resultado2 <= primeira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,primeira_medida))
elif (resultado2 > primeira_medida and resultado < segunda_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,segunda_medida))
elif (resultado2 > segunda_medida and resultado2 < terceira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,terceira_medida))
else:
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,quarta_medida))

print("--- OBRIGADO POR USAR VALHALLA SOFTWARE ---")