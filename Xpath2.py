import xmltodict
import json

with open("movies.xml", "r") as f:
    # считываем содержимое файла и преобразуем в словарь
    data = xmltodict.parse(f.read())
# преобразуем словарь в формат JSON
json_data = json.dumps(data)
# сохраняем результат в файл
with open("movies.json", "w") as f:
    f.write(json_data)









