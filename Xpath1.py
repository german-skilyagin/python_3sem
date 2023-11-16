import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
movies = {}
for movie in root.findall('Movie'):
    title = movie.find('Title').text
    runtime = movie.get('runtime', 1)
    movies[title] = runtime
print (movies)