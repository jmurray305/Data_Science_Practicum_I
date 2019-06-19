import wget
#Retrieve data from the URL using WGet and saving it to a CSV in the Data file
url = 'https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv'
wget.download(url, './crime.csv')
