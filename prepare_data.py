import sys
from shutil import copyfile
import os
import pandas as pd

def create_folders():
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/accidents'):
        os.mkdir('data/accidents')
    if not os.path.exists('data/causes'):
        os.mkdir('data/causes')
    if not os.path.exists('data/persones'):
        os.mkdir('data/persones')
    if not os.path.exists('data/tipus'):
        os.mkdir('data/tipus')
    if not os.path.exists('data/vehicles'):
        os.mkdir('data/vehicles')
    if not os.path.exists('data/districtes_i_barris'):
        os.mkdir('data/districtes_i_barris')		
    if not os.path.exists('data/domicilis_sexe'):
        os.mkdir('data/domicilis_sexe')				
    if not os.path.exists('data/padro_ocupacio'):
        os.mkdir('data/padro_ocupacio')		
				

def download_accidents():
    accidents2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/40838699-52ea-4e87-9e68-d9244ad10d9c/download/2010_ACCIDENTS_GU_BCN_.csv', encoding='ISO-8859-1')
    accidents2010.to_csv('data/accidents/2010.csv', index=False)
    accidents2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/bd601249-a019-4798-aa3a-f112d4b6845b/download', encoding='ISO-8859-1')
    accidents2011.to_csv('data/accidents/2011.csv', index=False)
    accidents2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/c47bf51c-afd8-47e3-ab1b-51835465cd57/download', encoding='ISO-8859-1')
    accidents2012.to_csv('data/accidents/2012.csv', index=False)
    accidents2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/f6e0b9b2-fd47-408f-8b36-ee09f7f4a336/download', encoding='ISO-8859-1')
    accidents2013.to_csv('data/accidents/2013.csv', index=False)
    accidents2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/9d8fb285-65d1-4380-8d98-137ca6c52f3e/download', encoding='ISO-8859-1')
    accidents2014.to_csv('data/accidents/2014.csv', index=False)
    accidents2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/962dcec4-f2a0-41e1-b6c2-c47c260f24b6/download/2015_accidents_gu_bcn.csv', encoding='ISO-8859-1', delimiter=';')
    accidents2015.to_csv('data/accidents/2015.csv', index=False)
    accidents2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/be253540-d3ec-418f-9b72-386492fa5269/download/2016_accidents_gu_bcn.csv')
    accidents2016.to_csv('data/accidents/2016.csv', index=False)
    accidents2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/acc9db4c-17b2-4862-8bcc-ed216f8e5839/download/2017_accidents_gu_bcn.csv')
    accidents2017.to_csv('data/accidents/2017.csv', index=False)
    accidents2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/f94d9ac3-e46e-47cd-a3d0-a9b5b9639d86/download/2018_accidents_gu_bcn.csv')
    accidents2018.to_csv('data/accidents/2018.csv', index=False)


def download_causes():
    causes2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/bbeeb0bb-5ed6-4015-92ce-33c2a8f378d1/download', encoding='ISO-8859-1')
    causes2010.to_csv('data/causes/2010.csv', index=False)
    causes2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/6d85f2aa-25b1-4ea3-8f4e-30ddbdb12632/download', encoding='ISO-8859-1')
    causes2011.to_csv('data/causes/2011.csv', index=False)
    causes2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/83334c28-4019-420b-80a0-58d95515eaa9/download', encoding='ISO-8859-1')
    causes2012.to_csv('data/causes/2012.csv', index=False)
    causes2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/82907ba9-f754-4601-8a49-2eada471894b/download', encoding='ISO-8859-1')
    causes2013.to_csv('data/causes/2013.csv', index=False)
    causes2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/24150ee2-cc9a-406e-b4e5-44011d43e4d3/download', encoding='ISO-8859-1')
    causes2014.to_csv('data/causes/2014.csv', index=False)
    causes2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/976d35c3-37e2-40ba-be1d-b7b5b791f68e/download', encoding='ISO-8859-1')
    causes2015.to_csv('data/causes/2015.csv', index=False)
    causes2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/1c647e80-fbdf-4f87-af48-3085fcc9a4a5/download/2016_accidents_causes_gu_bcn_.csv')
    causes2016.to_csv('data/causes/2016.csv', index=False)
    causes2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/adc0c6e9-4af6-41c0-9020-5af7a28f5461/download/2017_accidents_causes_gu_bcn_.csv')
    causes2017.to_csv('data/causes/2017.csv', index=False)
    causes2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/200fa1e2-7188-4a01-9b3d-e4ac0016528e/download/2018_accidents_causes_gu_bcn_.csv')
    causes2018.to_csv('data/causes/2018.csv', index=False)


def download_persones():
    persones2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/d0733ef7-9466-4bf8-b164-f6d0e487d7a6/download', encoding='ISO-8859-1')
    persones2010.to_csv('data/persones/2010.csv', index=False)
    persones2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/8caccf80-ac31-448e-9d7e-da59ee198c83/download', encoding='ISO-8859-1')
    persones2011.to_csv('data/persones/2011.csv', index=False)
    persones2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/9414851a-deeb-49f2-9975-05b8193afe49/download', encoding='ISO-8859-1')
    persones2012.to_csv('data/persones/2012.csv', index=False)
    persones2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/4e63c37a-304a-4310-b3eb-d10e64885ca0/download', encoding='ISO-8859-1')
    persones2013.to_csv('data/persones/2013.csv', index=False)
    persones2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/34090ede-942c-4e05-bc1f-f575c339affc/download', encoding='ISO-8859-1')
    persones2014.to_csv('data/persones/2014.csv', index=False)
    persones2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/3e3760b8-ed7d-4ada-a5fe-6ed3988a05ca/download', encoding='ISO-8859-1')
    persones2015.to_csv('data/persones/2015.csv', index=False)
    persones2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/08afa8b9-c2fd-4a11-a416-e8650b7fb838/download/2016_accidents_persones_gu_bcn.csv')
    persones2016.to_csv('data/persones/2016.csv', index=False)
    persones2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/435d38f9-0b15-4bd0-b32e-e187965de8db/download/2017_accidents_persones_gu_bcn_.csv')
    persones2017.to_csv('data/persones/2017.csv', index=False)
    persones2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/c6b05180-8084-4d89-a80c-f56de1f8e4de/download/2018_accidents_persones_gu_bcn_.csv')
    persones2018.to_csv('data/persones/2018.csv', index=False)


def download_tipus():
    tipus2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/3bdea112-6c16-457d-b96f-02fccd2ec714/download', encoding='ISO-8859-1')
    tipus2010.to_csv('data/tipus/2010.csv', index=False)
    tipus2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/95c2bb38-767c-4bd0-9d1b-0494837ab9e8/download', encoding='ISO-8859-1')
    tipus2011.to_csv('data/tipus/2011.csv', index=False)
    tipus2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/2c1665fc-f788-4da3-bb62-49647e93441f/download', encoding='ISO-8859-1')
    tipus2012.to_csv('data/tipus/2012.csv', index=False)
    tipus2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/a3a17b36-258a-4894-8693-a535c3856005/download', encoding='ISO-8859-1')
    tipus2013.to_csv('data/tipus/2013.csv', index=False)
    tipus2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/4366441b-a6e4-4f77-aad5-68fd3aa2bd85/download', encoding='ISO-8859-1')
    tipus2014.to_csv('data/tipus/2014.csv', index=False)
    tipus2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/c76f6aad-7dfb-4eb3-9905-3630453df07e/download', encoding='ISO-8859-1')
    tipus2015.to_csv('data/tipus/2015.csv', index=False)
    tipus2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/e7e97824-24a8-4771-b320-edf8ba3ea3e3/download/2016_accidents_tipus_gu_bcn_.csv')
    tipus2016.to_csv('data/tipus/2016.csv', index=False)
    tipus2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/bc2cb941-695c-4fe3-87ba-2ce931df57ff/download/2017_accidents_tipus_gu_bcn_.csv')
    tipus2017.to_csv('data/tipus/2017.csv', index=False)
    tipus2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/1f43e605-4ace-4134-a18b-5a329bf9000c/download/2018_accidents_tipus_gu_bcn_.csv')
    tipus2018.to_csv('data/tipus/2018.csv', index=False)


def download_vehicles():
    vehicles2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/3cbbe058-f407-40d5-bbb6-4ff1084a746b/download/2010_accidents_vehicles_gu_bcn_2010.csv', encoding='ISO-8859-1')
    vehicles2010.to_csv('data/vehicles/2010.csv', index=False)
    vehicles2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6f1155ff-a9b6-4f2d-9ad3-5f0da7bc3b0a/download/2011_accidents_vehicles_gu_bcn_2011.csv', encoding='ISO-8859-1')
    vehicles2011.to_csv('data/vehicles/2011.csv', index=False)
    vehicles2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/9d6e219a-4115-4042-85eb-1018073da9cd/download/2012_accidents_vehicles_gu_bcn_2012.csv', encoding='ISO-8859-1')
    vehicles2012.to_csv('data/vehicles/2012.csv', index=False)
    vehicles2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/4dc5f1de-97de-4e4f-b9a8-b4993e562c7a/download/2013_accidents_vehicles_gu_bcn_2013.csv', encoding='ISO-8859-1')
    vehicles2013.to_csv('data/vehicles/2013.csv', index=False)
    vehicles2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/3e7dfd62-c736-4133-9c9e-a98df3bf9f51/download/2014_accidents_vehicles_gu_bcn_2014.csv', encoding='ISO-8859-1')
    vehicles2014.to_csv('data/vehicles/2014.csv', index=False)
    vehicles2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6d56366a-3a44-4f44-9325-8bcdddde91ee/download/2015_accidents_vehicles_gu_bcn_2015.csv', encoding='ISO-8859-1')
    vehicles2015.to_csv('data/vehicles/2015.csv', index=False)
    vehicles2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/b49e7402-65ed-49c8-8d03-a6cade73bad6/download/2016_accidents_vehicles_gu_bcn_.csv')
    vehicles2016.to_csv('data/vehicles/2016.csv', index=False)
    vehicles2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/51ae5fea-dfc4-4da3-9421-8ed21a9cfdeb/download/2017_accidents_vehicles_gu_bcn_.csv')
    vehicles2017.to_csv('data/vehicles/2017.csv', index=False)
    vehicles2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6e2daeb5-e359-43ad-b0b5-7fdf438c8d6f/download/2018_accidents_vehicles_gu_bcn_.csv')
    vehicles2018.to_csv('data/vehicles/2018.csv', index=False)

def download_districtes_i_barris():	
    districtes_i_barris = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/808daafa-d9ce-48c0-925a-fa5afdb1ed41/resource/4cc59b76-a977-40ac-8748-61217c8ff367/download/districtes_i_barris_170705.csv', encoding='ISO-8859-1')
    districtes_i_barris.to_csv('data/districtes_i_barris/general.csv', index=False)
    
def download_domicilis_sexe():
    domicilis_sexe2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/1979024c-496c-4086-864d-0d02b6a20c10/download/2010_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2010.to_csv('data/domicilis_sexe/2010.csv', index=False)
    domicilis_sexe2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/c8c29362-d8d2-4882-ae2f-3f7fd1769148/download/2011_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2011.to_csv('data/domicilis_sexe/2011.csv', index=False)
    domicilis_sexe2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/71052747-9ee7-4db9-bcaf-8bdce33f937c/download/2012_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2012.to_csv('data/domicilis_sexe/2012.csv', index=False)
    domicilis_sexe2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/ef4e24f3-bdbe-40cc-ad30-cdec5bb32273/download/2013_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2013.to_csv('data/domicilis_sexe/2013.csv', index=False)
    domicilis_sexe2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/ef5054aa-e75e-4804-9090-c1dc50c0cd44/download/2014_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2014.to_csv('data/domicilis_sexe/2014.csv', index=False)
    domicilis_sexe2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/ba0453fd-2d7f-43ca-88c7-f9d2dedd2200/download/2015_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2015.to_csv('data/domicilis_sexe/2015.csv', index=False)
    domicilis_sexe2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/64f5c35d-53f6-4602-b39b-0677a78c9772/download/2016_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2016.to_csv('data/domicilis_sexe/2016.csv', index=False)
    domicilis_sexe2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/35c3c8bb-0c02-4caf-ac3d-7ca728bbd978/download/2017_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2017.to_csv('data/domicilis_sexe/2017.csv', index=False)
    domicilis_sexe2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/7263eea4-50e2-4fc4-a4f3-a9ab6cf8d7fd/resource/46bf0abf-3159-4985-bfbf-ee861777f987/download/2018_domicilis_sexe.csv', encoding='ISO-8859-1')
    domicilis_sexe2018.to_csv('data/domicilis_sexe/2018.csv', index=False)
	
	
def download_padro_ocupacio():
    padro_ocupacio2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/00393c1a-787a-4010-8271-9de1e577864f/download/2010_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2010.to_csv('data/padro_ocupacio/2010.csv', index=False)
    padro_ocupacio2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/c6b17c2a-22b9-4fa2-82d9-b3f421c3cda9/download/2011_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2011.to_csv('data/padro_ocupacio/2011.csv', index=False)
    padro_ocupacio2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/05d44dab-d990-4a94-b928-94a2e9029898/download/2012_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2012.to_csv('data/padro_ocupacio/2012.csv', index=False)
    padro_ocupacio2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/a7b513a3-e7d2-4540-8440-c2d5230d0bed/download/2013_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2013.to_csv('data/padro_ocupacio/2013.csv', index=False)
    padro_ocupacio2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/eb70ef29-0c39-4854-8e54-ff3a9c5e8dd1/download/2014_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2014.to_csv('data/padro_ocupacio/2014.csv', index=False)
    padro_ocupacio2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/687d9f5b-9afc-475c-baae-e251f646d891/download/2015_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2015.to_csv('data/padro_ocupacio/2015.csv', index=False)
    padro_ocupacio2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/310f5907-3c49-4cad-b1f6-e4c2c7c01a37/download/2016_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2016.to_csv('data/padro_ocupacio/2016.csv', index=False)
    padro_ocupacio2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/23c7f642-1a46-4cc2-aa42-abe93562c3f7/download/2017_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2017.to_csv('data/padro_ocupacio/2017.csv', index=False)
    padro_ocupacio2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/56568d9d-651a-49ff-bbc8-52d3fcee4421/resource/6588f621-b882-4164-ac88-c5bc54a1a788/download/2018_padro_ocupacio_mitjana.csv', encoding='ISO-8859-1')
    padro_ocupacio2018.to_csv('data/padro_ocupacio/2018.csv', index=False)
    
    


if __name__ == "__main__":
    create_folders()
    download_accidents()
    download_causes()
    download_persones()
    download_tipus()
    download_vehicles()
    download_districtes_i_barris()
    download_domicilis_sexe()
    download_padro_ocupacio()