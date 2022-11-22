#Verificar quem é que esta com os sintomas do vecna.
#vericar fichas dos alunos que visitaram a psicóloga E fora atacados
#Sintomas: Dor de cabeça, insônia, pesadelos, suor, frio e visões
#Criar lista com sintomas
#Receber inputs dos alunos e seus sintomas separados por vírgulas e espaço.
    #criar listas com esses inputs
    #descobrir para de receber input
    #Criar lista com pessoas com sintomas
    #Criar lista com pessoas sem sintomas
    #Max fica numa lista separada
    #Provavelmente laço com while

symptoms = ['dor de cabeca', 'insonia', 'pesadelos', 'suor frio', 'visoes']
maxine = []
names = []
safe = []

assess = False

while assess == False:
    assess_list = input().split(", ")
    assess_name = assess_list[0]
    assess_list.pop(0)
    if assess_name == 'descobrir':
        assess = True
    elif assess_name == 'Max':
         maxine.append(assess_name)
    else:
        names.append(assess_name)
    for a in assess_list:
        testing = symptoms.count(a)
        if testing == 0:
            continue
        else:
            with_symptoms.append(assess_name)
            break