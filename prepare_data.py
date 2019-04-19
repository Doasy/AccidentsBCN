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

def download_accidents():
    accidents2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/40838699-52ea-4e87-9e68-d9244ad10d9c/download/2010_ACCIDENTS_GU_BCN_.csv', encoding='ANSI')
    accidents2010.to_csv('data/accidents/2010.csv', index=False)
    accidents2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/bd601249-a019-4798-aa3a-f112d4b6845b/download', encoding='ANSI')
    accidents2011.to_csv('data/accidents/2011.csv', index=False)
    accidents2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/c47bf51c-afd8-47e3-ab1b-51835465cd57/download', encoding='ANSI')
    accidents2012.to_csv('data/accidents/2012.csv', index=False)
    accidents2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/f6e0b9b2-fd47-408f-8b36-ee09f7f4a336/download', encoding='ANSI')
    accidents2013.to_csv('data/accidents/2013.csv', index=False)
    accidents2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/9d8fb285-65d1-4380-8d98-137ca6c52f3e/download', encoding='ANSI')
    accidents2014.to_csv('data/accidents/2014.csv', index=False)
    accidents2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/962dcec4-f2a0-41e1-b6c2-c47c260f24b6/download/2015_accidents_gu_bcn.csv', encoding='ANSI', delimiter=';')
    accidents2015.to_csv('data/accidents/2015.csv', index=False)
    accidents2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/be253540-d3ec-418f-9b72-386492fa5269/download/2016_accidents_gu_bcn.csv')
    accidents2016.to_csv('data/accidents/2016.csv', index=False)
    accidents2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/acc9db4c-17b2-4862-8bcc-ed216f8e5839/download/2017_accidents_gu_bcn.csv')
    accidents2017.to_csv('data/accidents/2017.csv', index=False)
    accidents2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/e769eb9d-d778-4cd7-9e3a-5858bba49b20/resource/f94d9ac3-e46e-47cd-a3d0-a9b5b9639d86/download/2018_accidents_gu_bcn.csv')
    accidents2018.to_csv('data/accidents/2018.csv', index=False)


def download_causes():
    causes2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/bbeeb0bb-5ed6-4015-92ce-33c2a8f378d1/download', encoding='ANSI')
    causes2010.to_csv('data/causes/2010.csv', index=False)
    causes2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/6d85f2aa-25b1-4ea3-8f4e-30ddbdb12632/download', encoding='ANSI')
    causes2011.to_csv('data/causes/2011.csv', index=False)
    causes2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/83334c28-4019-420b-80a0-58d95515eaa9/download', encoding='ANSI')
    causes2012.to_csv('data/causes/2012.csv', index=False)
    causes2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/82907ba9-f754-4601-8a49-2eada471894b/download', encoding='ANSI')
    causes2013.to_csv('data/causes/2013.csv', index=False)
    causes2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/24150ee2-cc9a-406e-b4e5-44011d43e4d3/download', encoding='ANSI')
    causes2014.to_csv('data/causes/2014.csv', index=False)
    causes2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/976d35c3-37e2-40ba-be1d-b7b5b791f68e/download', encoding='ANSI')
    causes2015.to_csv('data/causes/2015.csv', index=False)
    causes2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/1c647e80-fbdf-4f87-af48-3085fcc9a4a5/download/2016_accidents_causes_gu_bcn_.csv')
    causes2016.to_csv('data/causes/2016.csv', index=False)
    causes2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/adc0c6e9-4af6-41c0-9020-5af7a28f5461/download/2017_accidents_causes_gu_bcn_.csv')
    causes2017.to_csv('data/causes/2017.csv', index=False)
    causes2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/200fa1e2-7188-4a01-9b3d-e4ac0016528e/download/2018_accidents_causes_gu_bcn_.csv')
    causes2018.to_csv('data/causes/2018.csv', index=False)


def download_persones():
    persones2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/d0733ef7-9466-4bf8-b164-f6d0e487d7a6/download', encoding='ANSI')
    persones2010.to_csv('data/persones/2010.csv', index=False)
    persones2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/8caccf80-ac31-448e-9d7e-da59ee198c83/download', encoding='ANSI')
    persones2011.to_csv('data/persones/2011.csv', index=False)
    persones2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/9414851a-deeb-49f2-9975-05b8193afe49/download', encoding='ANSI')
    persones2012.to_csv('data/persones/2012.csv', index=False)
    persones2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/4e63c37a-304a-4310-b3eb-d10e64885ca0/download', encoding='ANSI')
    persones2013.to_csv('data/persones/2013.csv', index=False)
    persones2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/34090ede-942c-4e05-bc1f-f575c339affc/download', encoding='ANSI')
    persones2014.to_csv('data/persones/2014.csv', index=False)
    persones2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/3e3760b8-ed7d-4ada-a5fe-6ed3988a05ca/download', encoding='ANSI')
    persones2015.to_csv('data/persones/2015.csv', index=False)
    persones2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/08afa8b9-c2fd-4a11-a416-e8650b7fb838/download/2016_accidents_persones_gu_bcn.csv')
    persones2016.to_csv('data/persones/2016.csv', index=False)
    persones2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/435d38f9-0b15-4bd0-b32e-e187965de8db/download/2017_accidents_persones_gu_bcn_.csv')
    persones2017.to_csv('data/persones/2017.csv', index=False)
    persones2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/c6b05180-8084-4d89-a80c-f56de1f8e4de/download/2018_accidents_persones_gu_bcn_.csv')
    persones2018.to_csv('data/persones/2018.csv', index=False)


def download_tipus():
    tipus2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/3bdea112-6c16-457d-b96f-02fccd2ec714/download', encoding='ANSI')
    tipus2010.to_csv('data/tipus/2010.csv', index=False)
    tipus2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/95c2bb38-767c-4bd0-9d1b-0494837ab9e8/download', encoding='ANSI')
    tipus2011.to_csv('data/tipus/2011.csv', index=False)
    tipus2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/2c1665fc-f788-4da3-bb62-49647e93441f/download', encoding='ANSI')
    tipus2012.to_csv('data/tipus/2012.csv', index=False)
    tipus2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/a3a17b36-258a-4894-8693-a535c3856005/download', encoding='ANSI')
    tipus2013.to_csv('data/tipus/2013.csv', index=False)
    tipus2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/4366441b-a6e4-4f77-aad5-68fd3aa2bd85/download', encoding='ANSI')
    tipus2014.to_csv('data/tipus/2014.csv', index=False)
    tipus2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/c76f6aad-7dfb-4eb3-9905-3630453df07e/download', encoding='ANSI')
    tipus2015.to_csv('data/tipus/2015.csv', index=False)
    tipus2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/e7e97824-24a8-4771-b320-edf8ba3ea3e3/download/2016_accidents_tipus_gu_bcn_.csv')
    tipus2016.to_csv('data/tipus/2016.csv', index=False)
    tipus2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/bc2cb941-695c-4fe3-87ba-2ce931df57ff/download/2017_accidents_tipus_gu_bcn_.csv')
    tipus2017.to_csv('data/tipus/2017.csv', index=False)
    tipus2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/834b8920-0685-4e16-8e20-faf13645f4f3/resource/1f43e605-4ace-4134-a18b-5a329bf9000c/download/2018_accidents_tipus_gu_bcn_.csv')
    tipus2018.to_csv('data/tipus/2018.csv', index=False)


def download_vehicles():
    vehicles2010 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/3cbbe058-f407-40d5-bbb6-4ff1084a746b/download/2010_accidents_vehicles_gu_bcn_2010.csv', encoding='ANSI')
    vehicles2010.to_csv('data/vehicles/2010.csv', index=False)
    vehicles2011 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6f1155ff-a9b6-4f2d-9ad3-5f0da7bc3b0a/download/2011_accidents_vehicles_gu_bcn_2011.csv', encoding='ANSI')
    vehicles2011.to_csv('data/vehicles/2011.csv', index=False)
    vehicles2012 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/9d6e219a-4115-4042-85eb-1018073da9cd/download/2012_accidents_vehicles_gu_bcn_2012.csv', encoding='ANSI')
    vehicles2012.to_csv('data/vehicles/2012.csv', index=False)
    vehicles2013 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/4dc5f1de-97de-4e4f-b9a8-b4993e562c7a/download/2013_accidents_vehicles_gu_bcn_2013.csv', encoding='ANSI')
    vehicles2013.to_csv('data/vehicles/2013.csv', index=False)
    vehicles2014 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/3e7dfd62-c736-4133-9c9e-a98df3bf9f51/download/2014_accidents_vehicles_gu_bcn_2014.csv', encoding='ANSI')
    vehicles2014.to_csv('data/vehicles/2014.csv', index=False)
    vehicles2015 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6d56366a-3a44-4f44-9325-8bcdddde91ee/download/2015_accidents_vehicles_gu_bcn_2015.csv', encoding='ANSI')
    vehicles2015.to_csv('data/vehicles/2015.csv', index=False)
    vehicles2016 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/b49e7402-65ed-49c8-8d03-a6cade73bad6/download/2016_accidents_vehicles_gu_bcn_.csv')
    vehicles2016.to_csv('data/vehicles/2016.csv', index=False)
    vehicles2017 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/51ae5fea-dfc4-4da3-9421-8ed21a9cfdeb/download/2017_accidents_vehicles_gu_bcn_.csv')
    vehicles2017.to_csv('data/vehicles/2017.csv', index=False)
    vehicles2018 = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/6e2daeb5-e359-43ad-b0b5-7fdf438c8d6f/download/2018_accidents_vehicles_gu_bcn_.csv')
    vehicles2018.to_csv('data/vehicles/2018.csv', index=False)

if __name__ == "__main__":
    create_folders()
    download_accidents()
    download_causes()
    download_persones()
    download_tipus()
    download_vehicles()