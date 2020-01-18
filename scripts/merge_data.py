import pandas as pd
import numpy as np
import os
from functools import reduce


def create_folders():
    if not os.path.exists('../data/merged'):
        os.mkdir('../data/merged')


def merge_data(list_of_files):
    for i in range(9):
        list_of_files[i]['Any'] = 2010 + i
    return reduce(lambda left, right: pd.concat([left, right], join="inner"), list_of_files)


def get_data():
    accidents = [pd.read_csv('../data/processed/' + str(2010 + i) + '/accidents.csv') for i in range(9)]
    causes = [pd.read_csv('../data/processed/' + str(2010 + i) + '/causes.csv') for i in range(9)]
    domicilis_sexe = [pd.read_csv('../data/processed/' + str(2010 + i) + '/domicilis_sexe.csv') for i in range(9)]
    padro_ocupacio = [pd.read_csv('../data/processed/' + str(2010 + i) + '/padro_ocupacio.csv') for i in range(9)]
    persones = [pd.read_csv('../data/processed/' + str(2010 + i) + '/persones.csv') for i in range(9)]
    tipus = [pd.read_csv('../data/processed/' + str(2010 + i) + '/tipus.csv') for i in range(9)]
    vehicles = [pd.read_csv('../data/processed/' + str(2010 + i) + '/vehicles.csv') for i in range(9)]

    return accidents, causes, domicilis_sexe, padro_ocupacio, persones, tipus, vehicles


if __name__ == "__main__":
    create_folders()
    accidents, causes, domicilis_sexe, padro_ocupacio, persones, tipus, vehicles = get_data()
    merge_data(accidents).to_csv('../data/merged/accidents.csv', index=False)
    merge_data(causes).to_csv('../data/merged/causes.csv', index=False)
    merge_data(domicilis_sexe).to_csv('../data/merged/domicilis_sexe.csv', index=False)
    merge_data(padro_ocupacio).to_csv('../data/merged/padro_ocupacio.csv', index=False)
    merge_data(persones).to_csv('../data/merged/persones.csv', index=False)
    merge_data(tipus).to_csv('../data/merged/tipus.csv', index=False)
    merge_data(vehicles).to_csv('../data/merged/vehicles.csv', index=False)
    pd.read_csv('../data/processed/districtes_i_barris.csv').to_csv('../data/merged/districtes_i_barris.csv',
                                                                    index=False)
