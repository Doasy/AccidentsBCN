#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import chardet
import os


if not os.path.exists('../clean_data'):
    os.mkdir('../clean_data')
for year in range(2010,2019):
    if not os.path.exists('../clean_data/'+str(year)):
        os.mkdir('../clean_data/'+str(year))


accidents = []
causes = []
tipus = []
persones = []
vehicles = []
domicilis_sexe = []
padro_ocupacio = []
districtes_i_barris = None


accidents2010 = pd.read_csv('../data/accidents/2010.csv')
accidents2010.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2010 = accidents2010.loc[accidents2010['Codi districte'] != -1]
accidents.append(accidents2010)


causes2010 = pd.read_csv('../data/causes/2010.csv')[['N£mero d\'expedient', 'Descripci¢ causa mediata']]
causes2010.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes2010['Descripció causa mediata'] = causes2010['Descripció causa mediata'].str.replace('‚', 'é')
causes2010['Descripció causa mediata'] = causes2010['Descripció causa mediata'].str.replace('Š', 'è')
causes2010['Descripció causa mediata'] = causes2010['Descripció causa mediata'].str.replace('‡', 'ç')
causes2010['Descripció causa mediata'] = causes2010['Descripció causa mediata'].str.replace('¢', 'ó')
causes2010['Descripció causa mediata'] = causes2010['Descripció causa mediata'].str.replace('£', 'ú')
causes.append(causes2010)



tipus2010 = pd.read_csv('../data/tipus/2010.csv')[['N£mero d\'expedient', 'Descripci¢ tipus accident']]
tipus2010.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('‚', 'é')
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('Š', 'è')
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('‡', 'ç')
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('¢', 'ó')
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('…', 'à')
tipus2010['Descripció tipus accident'] = tipus2010['Descripció tipus accident'].str.replace('£', 'ú')
tipus.append(tipus2010)


persones2010 = pd.read_csv('../data/persones/2010.csv')[['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']]
persones.append(persones2010)



vehicles2010 = pd.read_csv('../data/vehicles/2010.csv')[['Codi d\'expedient', 'Descripci¢ tipus de vehicle', 'Descripci¢ model', 'Descripci¢ marca', 'Descripci¢ color', 'Descripci¢ carnet', 'Antiguitat carnet']]
vehicles2010.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('…', 'à'), axis=1)
vehicles2010 = vehicles2010.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
vehicles.append(vehicles2010)

accidents2011 = pd.read_csv('../data/accidents/2011.csv')
accidents2011.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']

accidents2011 = accidents2011.loc[accidents2011['Codi districte'] != -1]
accidents.append(accidents2011)


causes2011 = pd.read_csv('../data/causes/2011.csv')[['N£mero d\'expedient', 'Descripci¢ causa mediata']]
causes2011.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes2011['Descripció causa mediata'] = causes2011['Descripció causa mediata'].str.replace('‚', 'é')
causes2011['Descripció causa mediata'] = causes2011['Descripció causa mediata'].str.replace('Š', 'è')
causes2011['Descripció causa mediata'] = causes2011['Descripció causa mediata'].str.replace('‡', 'ç')
causes2011['Descripció causa mediata'] = causes2011['Descripció causa mediata'].str.replace('¢', 'ó')
causes2011['Descripció causa mediata'] = causes2011['Descripció causa mediata'].str.replace('£', 'ú')
causes.append(causes2011)


tipus2011 = pd.read_csv('../data/tipus/2011.csv')[['N£mero d\'expedient', 'Descripci¢ tipus accident']]
tipus2011.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('‚', 'é')
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('Š', 'è')
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('‡', 'ç')
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('¢', 'ó')
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('…', 'à')
tipus2011['Descripció tipus accident'] = tipus2011['Descripció tipus accident'].str.replace('£', 'ú')
tipus.append(tipus2011)

persones2011 = pd.read_csv('../data/persones/2011.csv')[['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']]
persones.append(persones2011)



vehicles2011 = pd.read_csv('../data/vehicles/2011.csv')[['Codi d\'expedient', 'Descripci¢ tipus de vehicle', 'Descripci¢ model', 'Descripci¢ marca', 'Descripci¢ color', 'Descripci¢ carnet', 'Antiguitat carnet']]
vehicles2011.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('…', 'à'), axis=1)
vehicles2011 = vehicles2011.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
vehicles.append(vehicles2011)



accidents2012 = pd.read_csv('../data/accidents/2012.csv')
accidents2012.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2012 = accidents2012.loc[accidents2012['Codi districte'] != -1]
accidents.append(accidents2012)



causes2012 = pd.read_csv('../data/causes/2012.csv')[['N£mero d\'expedient', 'Descripci¢ causa mediata']]
causes2012.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes2012['Descripció causa mediata'] = causes2012['Descripció causa mediata'].str.replace('‚', 'é')
causes2012['Descripció causa mediata'] = causes2012['Descripció causa mediata'].str.replace('Š', 'è')
causes2012['Descripció causa mediata'] = causes2012['Descripció causa mediata'].str.replace('‡', 'ç')
causes2012['Descripció causa mediata'] = causes2012['Descripció causa mediata'].str.replace('¢', 'ó')
causes2012['Descripció causa mediata'] = causes2012['Descripció causa mediata'].str.replace('£', 'ú')
causes.append(causes2012)



tipus2012 = pd.read_csv('../data/tipus/2012.csv')[['N£mero d\'expedient', 'Descripci¢ tipus accident']]
tipus2012.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('‚', 'é')
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('Š', 'è')
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('‡', 'ç')
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('¢', 'ó')
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('…', 'à')
tipus2012['Descripció tipus accident'] = tipus2012['Descripció tipus accident'].str.replace('£', 'ú')
tipus.append(tipus2012)



persones2012 = pd.read_csv('../data/persones/2012.csv')[['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']]
persones.append(persones2012)



vehicles2012 = pd.read_csv('../data/vehicles/2012.csv')[['Codi d\'expedient', 'Descripci¢ tipus de vehicle', 'Descripci¢ model', 'Descripci¢ marca', 'Descripci¢ color', 'Descripci¢ carnet', 'Antiguitat carnet']]
vehicles2012.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('…', 'à'), axis=1)
vehicles2012 = vehicles2012.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
vehicles.append(vehicles2012)



accidents2013 = pd.read_csv('../data/accidents/2013.csv')
accidents2013.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2013 = accidents2013.loc[accidents2013['Codi districte'] != -1]
accidents.append(accidents2013)



causes2013 = pd.read_csv('../data/causes/2013.csv')[['N£mero d\'expedient', 'Descripci¢ causa mediata']]
causes2013.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes2013['Descripció causa mediata'] = causes2013['Descripció causa mediata'].str.replace('‚', 'é')
causes2013['Descripció causa mediata'] = causes2013['Descripció causa mediata'].str.replace('Š', 'è')
causes2013['Descripció causa mediata'] = causes2013['Descripció causa mediata'].str.replace('‡', 'ç')
causes2013['Descripció causa mediata'] = causes2013['Descripció causa mediata'].str.replace('¢', 'ó')
causes2013['Descripció causa mediata'] = causes2013['Descripció causa mediata'].str.replace('£', 'ú')
causes.append(causes2013)



tipus2013 = pd.read_csv('../data/tipus/2013.csv')[['N£mero d\'expedient', 'Descripci¢ tipus accident']]
tipus2013.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('‚', 'é')
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('Š', 'è')
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('‡', 'ç')
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('¢', 'ó')
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('…', 'à')
tipus2013['Descripció tipus accident'] = tipus2013['Descripció tipus accident'].str.replace('£', 'ú')
tipus.append(tipus2013)



persones2013 = pd.read_csv('../data/persones/2013.csv')[['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']]
persones.append(persones2013)



vehicles2013 = pd.read_csv('../data/vehicles/2013.csv')[['Codi d\'expedient', 'Descripci¢ tipus de vehicle', 'Descripci¢ model', 'Descripci¢ marca', 'Descripci¢ color', 'Descripci¢ carnet', 'Antiguitat carnet']]
vehicles2013.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('…', 'à'), axis=1)
vehicles2013 = vehicles2013.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
vehicles.append(vehicles2013)



accidents2014 = pd.read_csv('../data/accidents/2014.csv')
accidents2014.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2014 = accidents2014.loc[accidents2014['Codi districte'] != -1]
accidents.append(accidents2014)



causes2014 = pd.read_csv('../data/causes/2014.csv')[['N£mero d\'expedient', 'Descripci¢ causa mediata']]
causes2014.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes2014['Descripció causa mediata'] = causes2014['Descripció causa mediata'].str.replace('‚', 'é')
causes2014['Descripció causa mediata'] = causes2014['Descripció causa mediata'].str.replace('Š', 'è')
causes2014['Descripció causa mediata'] = causes2014['Descripció causa mediata'].str.replace('‡', 'ç')
causes2014['Descripció causa mediata'] = causes2014['Descripció causa mediata'].str.replace('¢', 'ó')
causes2014['Descripció causa mediata'] = causes2014['Descripció causa mediata'].str.replace('£', 'ú')
causes.append(causes2014)



tipus2014 = pd.read_csv('../data/tipus/2014.csv')[['N£mero d\'expedient', 'Descripci¢ tipus accident']]
tipus2014.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('‚', 'é')
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('Š', 'è')
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('‡', 'ç')
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('¢', 'ó')
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('…', 'à')
tipus2014['Descripció tipus accident'] = tipus2014['Descripció tipus accident'].str.replace('£', 'ú')
tipus.append(tipus2014)



persones2014 = pd.read_csv('../data/persones/2014.csv')[['N£mero d\'expedient','Descripci¢ causa vianant',  'Desc. Tipus vehicle implicat', 'Descripci¢ sexe', 'Descripci¢ tipus persona', 'Edat', 'Descripci¢ victimitzaci¢']]
persones2014.columns = ['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']
persones2014 = persones2014.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
persones2014 = persones2014.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
persones2014 = persones2014.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
persones2014 = persones2014.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
persones2014 = persones2014.apply(lambda x: x.str.replace('…', 'à'), axis=1)
persones2014 = persones2014.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
persones.append(persones2014)



vehicles2014 = pd.read_csv('../data/vehicles/2014.csv')[['Codi d\'expedient', 'Descripci¢ tipus de vehicle', 'Descripci¢ model', 'Descripci¢ marca', 'Descripci¢ color', 'Descripci¢ carnet', 'Antiguitat carnet']]
vehicles2014.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('‚', 'é'), axis=1)
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('Š', 'è'), axis=1)
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('‡', 'ç'), axis=1)
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('¢', 'ó'), axis=1)
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('…', 'à'), axis=1)
vehicles2014 = vehicles2014.apply(lambda x: x.str.replace('£', 'ú'), axis=1)
vehicles.append(vehicles2014)



accidents2015 = pd.read_csv('../data/accidents/2015.csv')
accidents2015.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2015 = accidents2015.loc[accidents2015['Codi districte'] != -1]
accidents.append(accidents2015)



causes2015 = pd.read_csv('../data/causes/2015.csv')[['Número d\'expedient', 'Descripció causa mediata']]
causes.append(causes2015)



tipus2015 = pd.read_csv('../data/tipus/2015.csv')[['Número d\'expedient', 'Descripció tipus accident']]
tipus.append(tipus2015)



persones2015 = pd.read_csv('../data/persones/2015.csv')[['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']]
persones.append(persones2015)



vehicles2015 = pd.read_csv('../data/vehicles/2015.csv')[['Codi d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']]
vehicles2015.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles.append(vehicles2015)



accidents2016 = pd.read_csv('../data/accidents/2016.csv')[['Numero_expedient', 'Codi_districte', 'Nom_districte', 'Codi_barri', 'Nom_barri', 'Codi_carrer', 'Nom_carrer', 'Num_postal', 'Descripcio_dia_setmana', 'Dia_setmana', 'Descripcio_tipus_dia', 'Any', 'Mes_any', 'Nom_mes', 'Dia_mes', 'Hora_dia', 'Descripcio_torn', 'Descripcio_causa_vianant', 'Numero_morts', 'Numero_lesionats_lleus', 'Numero_lesionats_greus', 'Numero_victimes', 'Numero_vehicles_implicats', 'Coordenada_UTM_X', 'Coordenada_UTM_Y']]
accidents2016.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2016 = accidents2016.loc[accidents2016['Codi districte'] != -1]
accidents.append(accidents2016)



causes2016 = pd.read_csv('../data/causes/2016.csv')[['Numero_expedient', 'Descripcio_causa_mediata']]
causes2016.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes.append(causes2016)



tipus2016 = pd.read_csv('../data/tipus/2016.csv')[['Numero_expedient', 'Descripcio_tipus_accident']]
tipus2016.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus.append(tipus2016)



persones2016 = pd.read_csv('../data/persones/2016.csv')[['Numero_expedient', 'Descripcio_causa_vianant', 'Desc_Tipus_vehicle_implicat',
       'Descripcio_sexe', 'Descripcio_tipus_persona', 'Edat', 'Descripcio_victimitzacio']]
persones2016.columns= ['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']
persones.append(persones2016)



vehicles2016 = pd.read_csv('../data/vehicles/2016.csv')[['Codi_expedient', 
       'Descripcio_tipus_vehicle', 'Descripcio_model', 'Descripcio_marca',
       'Descripcio_color', 'Descripcio_carnet', 'Antiguitat_carnet']]
vehicles2016.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles.append(vehicles2016)



accidents2017 = pd.read_csv('../data/accidents/2017.csv')[['Numero_expedient', 'Codi_districte', 'Nom_districte', 'Codi_barri', 'Nom_barri', 'Codi_carrer', 'Nom_carrer', 'Num_postal', 'Descripcio_dia_setmana', 'Dia_setmana', 'Descripcio_tipus_dia', 'Any', 'Mes_any', 'Nom_mes', 'Dia_mes', 'Hora_dia', 'Descripcio_torn', 'Descripcio_causa_vianant', 'Numero_morts', 'Numero_lesionats_lleus', 'Numero_lesionats_greus', 'Numero_victimes', 'Numero_vehicles_implicats', 'Coordenada_UTM_X', 'Coordenada_UTM_Y']]
accidents2017.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']

accidents2017 = accidents2017.loc[accidents2017['Codi districte'] != -1]
accidents.append(accidents2017)



causes2017 = pd.read_csv('../data/causes/2017.csv')[['Número_d\'expedient', 'Descripció_causa_mediata']]
causes2017.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes.append(causes2017)



tipus2017 = pd.read_csv('../data/tipus/2017.csv')[['Numero_expedient', 'Descripcio_tipus_accident']]
tipus2017.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus.append(tipus2017)



persones2017 = pd.read_csv('../data/persones/2017.csv')[['Numero_expedient', 'Descripcio_causa_vianant', 'Desc_Tipus_vehicle_implicat',
       'Descripcio_sexe', 'Edat', 'Descripcio_tipus_persona', 'Descripcio_victimitzacio']]
persones2017.columns= ['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']
persones.append(persones2017)



vehicles2017 = pd.read_csv('../data/vehicles/2017.csv')[['Codi_expedient', 
       'Descripcio_tipus_vehicle', 'Descripcio_model', 'Descripcio_marca',
       'Descripcio_color', 'Descripcio_carnet', 'Antiguitat_carnet']]
vehicles2017.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles.append(vehicles2017)



accidents2018 = pd.read_csv('../data/accidents/2018.csv')[['Numero_expedient', 'Codi_districte', 'Nom_districte', 'Codi_barri', 'Nom_barri', 'Codi_carrer', 'Nom_carrer', 'Num_postal ', 'Descripcio_dia_setmana', 'Dia_setmana', 'Descripcio_tipus_dia', 'Any', 'Mes_any', 'Nom_mes', 'Dia_mes', 'Hora_dia', 'Descripcio_torn', 'Descripcio_causa_vianant', 'Numero_morts', 'Numero_lesionats_lleus', 'Numero_lesionats_greus', 'Numero_victimes', 'Numero_vehicles_implicats', 'Coordenada_UTM_X', 'Coordenada_UTM_Y']]
accidents2018.columns = ['Número d\'expedient', 'Codi districte', 'Nom districte', 'Codi barri',
       'Nom barri', 'Codi carrer', 'Nom carrer', 'Num postal caption',
       'Descripció dia setmana', 'Dia setmana', 'Descripció tipus dia',
       'NK Any', 'Mes de any', 'Nom mes', 'Dia de mes', 'Hora de dia',
       'Descripció torn', 'Descripció causa vianant', 'Número de morts',
       'Número de lesionats lleus', 'Número de lesionats greus',
       'Número de víctimes', 'Número de vehicles implicats',
       'Coordenada UTM (Y)', 'Coordenada UTM (X)']
accidents2018 = accidents2018.loc[accidents2018['Codi districte'] != -1]
accidents.append(accidents2018)



causes2018 = pd.read_csv('../data/causes/2018.csv')[['Numero_expedient', 'Descripcio_causa_mediata']]
causes2018.columns = ['Número d\'expedient', 'Descripció causa mediata']
causes.append(causes2018)



tipus2018 = pd.read_csv('../data/tipus/2018.csv')[['Codi_expedient', 'Tipus_accident']]
tipus2018.columns = ['Número d\'expedient', 'Descripció tipus accident']
tipus.append(tipus2018)



persones2018 = pd.read_csv('../data/persones/2018.csv')[['Numero_expedient', 'Descripcio_causa_vianant', 'Desc_Tipus_vehicle_implicat',
       'Descripcio_sexe', 'Edat', 'Descripcio_tipus_persona', 'Descripcio_victimitzacio']]
persones2018.columns= ['Número d\'expedient','Descripció causa vianant',  'Desc. Tipus vehicle implicat', 'Descripció sexe', 'Descripció tipus persona', 'Edat', 'Descripció victimització']
persones.append(persones2018)



vehicles2018 = pd.read_csv('../data/vehicles/2018.csv')[['Codi_expedient', 
       'Descripcio_tipus_vehicle', 'Descripcio_model', 'Descripcio_marca',
       'Descripcio_color', 'Descripcio_carnet', 'Antiguitat_carnet']]
vehicles2018.columns = ['Número d\'expedient', 'Descripció tipus de vehicle', 'Descripció model', 'Descripció marca', 'Descripció color', 'Descripció carnet', 'Antiguitat carnet']
vehicles.append(vehicles2018)



for i in range(9):
    accidents[i] = pd.merge(accidents[i], tipus[i], on='Número d\'expedient', how='inner')



domicilis_sexe_files = ['2010.csv', '2011.csv', '2012.csv', '2013.csv','2014.csv',
                        '2015.csv', '2016.csv', '2017.csv', '2018.csv']
camps_to_replace = ['Nom_Barri', 'Nom_Districte', 'Sexe']

for date in domicilis_sexe_files:
    d_file = pd.read_csv('../data/domicilis_sexe/'+date)[['Any', 'Codi_Districte',  'Nom_Districte', 'Codi_Barri', 'Nom_Barri', 'Sexe', 'Nombre']]
    for field in camps_to_replace:       
        d_file[field] = d_file[field].str.replace('‚', 'é')
        d_file[field] = d_file[field].str.replace('Š', 'è')
        d_file[field] = d_file[field].str.replace('‡', 'ç')
        d_file[field] = d_file[field].str.replace('¢', 'ó')
        d_file[field] = d_file[field].str.replace('£', 'ú')
        d_file[field] = d_file[field].str.replace('Ã²', 'ò')
        d_file[field] = d_file[field].str.replace('iÃ', 'ó')
        d_file[field] = d_file[field].str.replace('Ã³', 'ó')
        d_file[field] = d_file[field].str.replace('Ã©', 'é')
        d_file[field] = d_file[field].str.replace('Ã', 'í')
        d_file[field] = d_file[field].str.replace('í¯', 'ï')
        d_file[field] = d_file[field].str.replace('§', 'ç')
    domicilis_sexe.append(d_file)



padro_ocupacio_files = ['2010.csv', '2011.csv', '2012.csv', '2013.csv','2014.csv',
                        '2015.csv', '2016.csv', '2017.csv', '2018.csv']
camps_to_replace = ['Nom_Barri', 'Nom_Districte']
for date in domicilis_sexe_files:
    d_file = pd.read_csv('../data/padro_ocupacio/'+date)[['Any', 'Codi_Districte',  'Nom_Districte', 'Codi_Barri', 'Nom_Barri', 'Poblacio', 'Domicilis', 'Ocupacio_mitjana_(persones_ per_domicili)']]
    d_file.columns = ['Any', 'Codi_Districte',  'Nom_Districte', 'Codi_Barri', 'Nom_Barri', 'Població', 'Domicilis', 'Ocupació mitjana (persones per domicili)']
    for field in camps_to_replace:       
        d_file[field] = d_file[field].str.replace('‚', 'é')
        d_file[field] = d_file[field].str.replace('Š', 'è')
        d_file[field] = d_file[field].str.replace('‡', 'ç')
        d_file[field] = d_file[field].str.replace('¢', 'ó')
        d_file[field] = d_file[field].str.replace('£', 'ú')
        d_file[field] = d_file[field].str.replace('Ã²', 'ò')
        d_file[field] = d_file[field].str.replace('iÃ', 'ó')
        d_file[field] = d_file[field].str.replace('Ã³', 'ó')
        d_file[field] = d_file[field].str.replace('Ã©', 'é')
        d_file[field] = d_file[field].str.replace('Ã', 'í')
        d_file[field] = d_file[field].str.replace('í¯', 'ï')
        d_file[field] = d_file[field].str.replace('§', 'ç')
    padro_ocupacio.append(d_file)



padro_ocupacio_files = ['general.csv']
camps_to_replace = ['NOM_BARRI', 'NOM_DISTRICTE']

d_file = pd.read_csv('../data/districtes_i_barris/'+padro_ocupacio_files[0])
for field in camps_to_replace:       
    d_file[field] = d_file[field].str.replace('‚', 'é')
    d_file[field] = d_file[field].str.replace('Š', 'è')
    d_file[field] = d_file[field].str.replace('‡', 'ç')
    d_file[field] = d_file[field].str.replace('¢', 'ó')
    d_file[field] = d_file[field].str.replace('£', 'ú')
    d_file[field] = d_file[field].str.replace('Ã²', 'ò')
    d_file[field] = d_file[field].str.replace('iÃ', 'ó')
    d_file[field] = d_file[field].str.replace('Ã³', 'ó')
    d_file[field] = d_file[field].str.replace('Ã©', 'é')
    d_file[field] = d_file[field].str.replace('Ã', 'í')
    d_file[field] = d_file[field].str.replace('í¯', 'ï')
    d_file[field] = d_file[field].str.replace('§', 'ç')
districtes_i_barris = d_file



districtes_i_barris.to_csv('../clean_data/districtes_i_barris.csv', index = False)
for i in range(9):
    accidents[i].to_csv('../clean_data/'+str(2010+i)+'/accidents.csv', index = False)
    persones[i].to_csv('../clean_data/'+str(2010+i)+'/persones.csv', index = False)
    vehicles[i].to_csv('../clean_data/'+str(2010+i)+'/vehicles.csv', index = False)
    domicilis_sexe[i].to_csv('../clean_data/'+str(2010+i)+'/domicilis_sexe.csv', index = False)
    padro_ocupacio[i].to_csv('../clean_data/'+str(2010+i)+'/padro_ocupacio.csv', index = False)
    





