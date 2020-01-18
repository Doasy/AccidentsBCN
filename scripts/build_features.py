import pandas as pd
import os


def expertise_definer(row):
    if row < 2:
        return 0
    elif row < 5:
        return 1
    elif row < 10:
        return 2
    else:
        return 3


def extract_vehicles_info(df, vehicles):
    df = df.merge(vehicles, how='inner', on="Número d'expedient")
    df.rename({'Any_x': 'any', "Descripció tipus de vehicle": 'tipus_vehicle', 'Descripció model': 'model',
               'Descripció marca': 'marca', "Descripció color": 'color_vehicle', 'Descripció carnet': 'tipus_carnet',
               'Antiguitat carnet': 'antiguitat_carnet'}, axis=1, inplace=True)
    df.drop(df.loc[df.antiguitat_carnet == 'Desconegut'].index, axis=0, inplace=True)
    df.antiguitat_carnet = df.antiguitat_carnet.astype('int')
    df['expertesa_carnet'] = df.antiguitat_carnet.apply(expertise_definer)
    df.drop(['Any_y', 'antiguitat_carnet'], axis=1, inplace=True)
    return df


# rangs de edats dels conductors
# genere del conductor
def driver_info(df, driver):
    driver.drop(driver.loc[driver['Descripció tipus persona'] != 'Conductor'].index, axis=0, inplace=True)
    driver = driver[['Descripció sexe', 'Edat']]
    df = df.merge(driver, how='inner', on="Número d'expedient")
    df.rename({'Any_x': 'any', 'Descripció sexe': 'genere', 'Edat': 'edat'}, axis=1, inplace=True)
    df.drop(df.loc[df.edat == 'Desconegut'].index, axis=0, inplace=True)
    df.edat = df.edat.astype('int')
    df['rang_edat'] = df.edat.apply(lambda x: 0 if x < 30 else 1)
    df['rang_edat'] = df.edat.apply(lambda x: 1 if x < 65 else 2)
    df.drop('edat', axis=1, inplace=True)
    return df


# nombre d'accidents donat un perfil
def accidents_number(df):
    print(df.groupby(['any', 'tipus_vehicle', 'model', 'marca', 'color_vehicle',
       'tipus_carnet', 'expertesa_carnet', 'genere', 'rang_edat']).size())
    # no contar accidents, sino fer un factor de risc. Aplicar factor de risc a differents agrupacions
    return df


if __name__ == '__main__':
    if not os.path.exists('../data/final'):
        os.mkdir('../data/final')
    accidents = pd.read_csv('../data/merged/accidents.csv', index_col="Número d'expedient")
    vehicles = pd.read_csv('../data/merged/vehicles.csv', index_col="Número d'expedient")
    persones = pd.read_csv('../data/merged/persones.csv', index_col="Número d'expedient")
    df = pd.DataFrame(accidents["Any"])
    (df.pipe(extract_vehicles_info, vehicles)
     .pipe(driver_info, persones)
     .pipe(accidents_number)
     .to_csv('../data/final/featured.csv'))
