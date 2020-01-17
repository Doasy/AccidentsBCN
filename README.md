# Accidents BCN

This project takes data published by Barcelona's council, about accidents in the city.
Currently, the project download, clean and prepare the data.

## Data Gathering

Data is obtained from [the Barcelona opendata webpage](https://opendata-ajuntament.barcelona.cat/data/en/dataset?q=accidents&sort=fecha_publicacion+desc).

To download the data, run:

    python scripts/download_data.py

## Data Cleaning-Transform

The necessary data transformations are made using the scripts in the /scripts directory 
