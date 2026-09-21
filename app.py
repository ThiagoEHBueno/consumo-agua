tipoImovel = input("Qual o tipo do imóvel? As opções são: comercial, casa ou apartamento. ")
consumoAgua = float(input("Qual o consumo mensal de água em metros cúbicos(m³)? "))

if tipoImovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipoImovel == "apartamento" and consumoAgua < 10:
   print("Consumo econômico – excelente controle de água!")
elif (tipoImovel == "apartamento" or "casa") and consumoAgua <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")