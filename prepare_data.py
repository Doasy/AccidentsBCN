import sys
from shutil import copyfile
import os

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

def copyfiles(src_path):
    if os.path.exists(src_path):
        for year in range(2010,2019):
            if os.path.exists(src_path+'/'+str(year)+'_ACCIDENTS_GU_BCN_'+str(year)+'.csv'):
                origin_accidents = src_path+'/'+str(year)+'_ACCIDENTS_GU_BCN_'+str(year)+'.csv'
            else:
                origin_accidents =  src_path+'/'+str(year)+'_accidents_gu_bcn'+'.csv'       
        
            if os.path.exists(src_path+'/'+str(year)+'_ACCIDENTS_CAUSES_GU_BCN_'+str(year)+'.csv'):
                origin_causes = src_path+'/'+str(year)+'_ACCIDENTS_CAUSES_GU_BCN_'+str(year)+'.csv'
            else:
                origin_causes =  src_path+'/'+str(year)+'_accidents_causes_gu_bcn_'+'.csv'

            if os.path.exists(src_path+'/'+str(year)+'_ACCIDENTS_PERSONES_GU_BCN_'+str(year)+'.csv'):
                origin_persones = src_path+'/'+str(year)+'_ACCIDENTS_PERSONES_GU_BCN_'+str(year)+'.csv'
            elif os.path.exists(src_path+'/'+str(year)+'_accidents_persones_gu_bcn_'+'.csv'):
                origin_persones =  src_path+'/'+str(year)+'_accidents_persones_gu_bcn_'+'.csv'
            else:
                origin_persones =  src_path+'/'+str(year)+'_accidents_persones_gu_bcn'+'.csv'
            if os.path.exists(src_path+'/'+str(year)+'_ACCIDENTS_TIPUS_GU_BCN_'+str(year)+'.csv'):
                origin_tipus = src_path+'/'+str(year)+'_ACCIDENTS_TIPUS_GU_BCN_'+str(year)+'.csv' 
            else:
                origin_tipus =  src_path+'/'+str(year)+'_accidents_tipus_gu_bcn_'+'.csv'

            if os.path.exists(src_path+'/'+str(year)+'_accidents_vehicles_gu_bcn_'+str(year)+'.csv'):
                origin_vehicles = src_path+'/'+str(year)+'_accidents_vehicles_gu_bcn_'+str(year)+'.csv'
            else:
                origin_vehicles =  src_path+'/'+str(year)+'_accidents_vehicles_gu_bcn_'+'.csv'


            destination_accidents = 'data/accidents/'+str(year)+'.csv'
            destination_causes = 'data/causes/'+str(year)+'.csv'
            destination_persones = 'data/persones/'+str(year)+'.csv'
            destination_tipus = 'data/tipus/'+str(year)+'.csv'
            destination_vehicles = 'data/vehicles/'+str(year)+'.csv'

            copyfile(origin_accidents, destination_accidents)
            copyfile(origin_causes, destination_causes)
            copyfile(origin_persones, destination_persones)
            copyfile(origin_tipus, destination_tipus)
            copyfile(origin_vehicles, destination_vehicles)
    else:
        print("This path doesn't exist.") 
        exit(1)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("It's necessary only one argument: the path where the download data is.") 
        exit(1)
    folder_path = sys.argv[1]
    create_folders()
    copyfiles(folder_path)
    