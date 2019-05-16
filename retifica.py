import sys
print("--- Bem-vindo ao programa de Retífica ---")
print("--- Primeiramente, informe as medidas do munhão e do moente")
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
elif (resultado > terceira_medida and resultado < quarta_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado, quarta_medida))
else:
    print("Substituir o virabrequim")

moente = float(input("Medida do moente STD: "))
moenteMedido = float(input("Medida encontrada no moente: "))

resultado2 = moente - moenteMedido

if (resultado2 <= primeira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,primeira_medida))
elif (resultado2 > primeira_medida and resultado < segunda_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,segunda_medida))
elif (resultado2 > segunda_medida and resultado2 < terceira_medida):
    print("A folga é de {:.3f}, retificar para {:.3f}".format(resultado2,terceira_medida))
elif (resultado2 > terceira_medida and resultado2 < quarta_medida):
    print("A folga é de {:.3f}, retificar para {:.3f} \n".format(resultado2, quarta_medida))
else:
    print("Substitua o virabrequim")

print("--- Agora, serão avaliados os cilindros. ---")
cilindro = float(input("Medida do cilindro STD: "))

cilindroMedido = float(input("Informe a medida do cilindro mais gasto: "))

resultado3 = cilindroMedido - cilindro

if (resultado3 <= primeira_medida):
    print("O desgaste foi de {:.3f}, retificar para {:.3f}".format(resultado3,primeira_medida))
elif (resultado3 > primeira_medida and resultado3 < segunda_medida):
    print("O desgaste foi de {:.3f}, retificar para {:.3f}".format(resultado3,segunda_medida))
elif (resultado3 > segunda_medida and resultado3 < terceira_medida):
    print("O desgaste foi de {:.3f}, retificar para {:.3f}".format(resultado3,terceira_medida))
elif (resultado3 > terceira_medida and resultado3 < quarta_medida):
    print("O desgaste foi de {:.3f}, retificar para {:.3f} \n".format(resultado3,quarta_medida))
else:
    print("Substitua o bloco do motor")

print("--- OBRIGADO POR USAR VALHALLA SOFTWARE ---")
#sys.exit()
