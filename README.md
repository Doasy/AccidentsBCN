# Accidents BCN

This project takes data published by Barcelona's council, about accidents in the city.
Currently, the Project only makes the data gathering and cleaning.

# Data

First, the user should manually download all data from [the Barcelona opendata webpage](https://opendata-ajuntament.barcelona.cat/data/en/dataset?q=accidents&sort=fecha_publicacion+desc) with CSV format and put it all in a folder.

## Create folders structure

After downloading the data and keep it in a folder, run the script "prepare_data.py" with one argument: the path of the folder where the data is.

    python prepare_data.py downloaded_data_folder_path

# Data Gathering

The data gathering is made by the notebook accidents_bcn.ipynb.
