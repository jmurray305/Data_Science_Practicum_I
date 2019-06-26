# Data_Science_Practicum_I
Read Me


The problem I tried to solve for my Data Science Practicum I was trying to predict and analyze Crime in Denver Country.  The [Dataset](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime) has 19 fields of criminal offenses from the previous five calendar years pules the current year to date and is updated every weekday. First, I cleaned the data in preparation for visualization, Heat Maps, and time series forecasting using Linear regressions and Long Short Term Memory recurrent neural network. My main goal was to try and predict how many offenses of a crime will happen in the future.


Run - Data/GetData first to create a data file

Modify gmaps.configure(api_key=os.environ["GOOGLE_API_KEY"]) and set your GOOGLE api key or save your api key to an environment variable.
