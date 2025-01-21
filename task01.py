import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Manaus"
response = requests.get(url)


soup = BeautifulSoup(response.text,features="lxml" )

tables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='wikitable sortable')


columns_def=['Neighborhood', 'Zone', 'Area', 'Population', 'Density', 'Homes_count']
df = pd.DataFrame(columns_def)

# Collecting Ddata
list = []
first = True
for row in table.tbody.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')

    if columns != []:
        neighborhood = columns[0].text.strip()
        zone = columns[1].text.strip()

        area = columns[2].span.contents[0].strip('&0.')
        population = columns[3].span.contents[0].strip('&0.')
        density = columns[4].span.contents[0].strip('&0.')
        homes_count = columns[5].span.contents[0].strip('&0.')
        list.append([neighborhood,zone,area,population,density,homes_count])


df_extended = pd.DataFrame(list, columns=columns_def)


print(df_extended)