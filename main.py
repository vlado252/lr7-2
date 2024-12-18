import json  # Импортируем библиотеку json для работы с JSON файлами

# Запрашиваем у пользователя ввод номера квалификации для поиска
num = str(input("Введите номер квалификации для поиска: "))
skills = False  # Инициализируем переменную, которая будет указывать, найдена ли квалификация

# Открываем JSON файл в режиме чтения с кодировкой UTF-8
with open('dump.json', 'r', encoding='utf-8') as file: 
    data = json.load(file)  # Загружаем данные из файла в переменную data

    # Перебираем все элементы в data
    for skill in data:
        # Проверяем, является ли текущий элемент моделью "data.skill"
        if skill.get("model") == "data.skill":
            # Проверяем, соответствует ли код квалификации введенному номеру
            if skill["fields"].get("code") == num: 
                skill_code = skill["fields"].get("code")  # Получаем код квалификации
                skill_title = skill["fields"].get("title")  # Получаем название квалификации
                skill_specialty = skill["fields"].get("specialty")  # Получаем специальность квалификации
                skills = True  # Устанавливаем флаг, что квалификация найдена

                # Перебираем все элементы в data для поиска специальности
                for profes in data:
                    # Проверяем, является ли текущий элемент моделью "data.specialty"
                    if profes.get("model") == "data.specialty":
                        profes_code = profes.get("fields").get("code")  # Получаем код специальности
                        profes_pk = profes["pk"]  # Получаем первичный ключ специальности

                        # Проверяем, соответствует ли код специальности введенному номеру и совпадает ли специальность
                        if profes_code in num and skill_specialty == profes_pk:  
                            profes_title = profes["fields"].get("title")  # Получаем название специальности
                            profes_type = profes["fields"].get("c_type")  # Получаем тип специальности
                            break    
                break  

# Вывод результата
if not skills:  # Если квалификация не найдена
    print("=============== Не Найдено ===============") 
else:  # Если квалификация найдена
    print("=============== Найдено ===============") 
    print(f"{skill_code} >> Квалификация {skill_title}")
    print(f"{profes_code} >> Специальность {profes_title} , {profes_type}")
