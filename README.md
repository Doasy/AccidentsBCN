# Accidents BCN

This project takes data published by Barcelona's council, about accidents in the city.
Currently, the project download, clean and prepare the data.

## Data Gathering

Data is obtained from [the Barcelona opendata webpage](https://opendata-ajuntament.barcelona.cat/data/en/dataset?q=accidents&sort=fecha_publicacion+desc).

To download and clean the data, run:

1. python scripts/download_data.py
2. python scripts/clean_data.py
3. python scripts/merge_data.py
4. python scripts/build_features.py


**The data needed to execute the final notebook is stored in the data/final/featured.csv**

**The final notebook is in the /notebooks directory**