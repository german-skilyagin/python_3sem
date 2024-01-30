import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot() #корневой элемент дерева получаем
movie_dict = {} # задаём словарь
for movie in root.findall('Movie'):#проходимся по каждому элементу
    title = movie.find('Title').text
    runtime = movie.find('Title').get('runtime')
    movie_dict[title] = runtime
print(movie_dict)