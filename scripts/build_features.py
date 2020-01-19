import pandas as pd
import os


def extract_vehicles_info(df, vehicles):
    df = df.merge(vehicles, how='inner', on=["Número d'expedient"])
    df.rename({'Any_x': 'any', "Descripció tipus de vehicle": 'tipus_vehicle', 'Descripció model': 'model',
               'Descripció marca': 'marca', "Descripció color": 'color_vehicle', 'Descripció carnet': 'tipus_carnet',
               'Descripció model': 'model', 'Antiguitat carnet': 'expertesa_carnet'}, axis=1, inplace=True)
    df.drop(df.loc[df.expertesa_carnet == 'Desconegut'].index, axis=0, inplace=True)
    df.expertesa_carnet = df.expertesa_carnet.astype('int')
    df.drop(['Any_y'], axis=1, inplace=True)
    return df

def driver_info(df, driver):
    driver.drop(driver.loc[driver['Descripció tipus persona'] != 'Conductor'].index, axis=0, inplace=True)
    driver = driver[['Descripció sexe', 'Edat']]
    df = df.merge(driver, how='inner', on="Número d'expedient")
    df.rename({'Any_x': 'any', 'Descripció sexe': 'genere', 'Edat': 'edat'}, axis=1, inplace=True)
    df.drop(df.loc[df.edat == 'Desconegut'].index, axis=0, inplace=True)
    df.edat = df.edat.astype('int')
    df['expedient'] = df.index
    # We only let one register per expedient. Why? Because there is no foreign key between csvs, meaning that two expedient registers in vehicles cannot be matched with the csv of people data.
    df.drop_duplicates(subset=["expedient"], inplace=True)
    df.drop(['expedient', 'model'], axis=1, inplace=True)
    return df



if __name__ == '__main__':
    if not os.path.exists('../data/final'):
        os.mkdir('../data/final')
    vehicles = pd.read_csv('../data/merged/vehicles.csv', index_col="Número d'expedient")
    persones = pd.read_csv('../data/merged/persones.csv', index_col="Número d'expedient")
    df = pd.DataFrame(persones["Any"])
    (df.pipe(extract_vehicles_info, vehicles)
     .pipe(driver_info, persones)
     .to_csv('../data/final/featured.csv'))
