import json  
num = str(input("Введите номер квалификации для поиска: "))
skills = False

with open('dump.json', 'r', encoding='utf-8') as file: 
    data = json.load(file) 
    #Квалификация
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == num: 
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                skill_specialty =  skill["fields"].get("specialty")
                skills = True
                #Специальность
                for profes in data:
                    if profes.get("model") == "data.specialty":
                        profes_code = profes.get("fields").get("code")
                        profes_pk = profes["pk"]
                        if profes_code in num and  skill_specialty == profes_pk :  
                            profes_title = profes["fields"].get("title")
                            profes_type = profes["fields"].get("c_type")
                            break    
                break  


#Вывод
if not skills:
    print("=============== Не Найдено ===============") 
else:
    print("=============== Найдено ===============") 
    print(f"{skill_code} >> Квалификация {skill_title}")
    print(f"{profes_code} >> Специальность {profes_title} , {profes_type}")
    
