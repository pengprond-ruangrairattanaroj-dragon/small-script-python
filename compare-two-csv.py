import pandas as pd
import os

path1 = os.getcwd()+"/WKFS_EOM_TEST_FOLDER/wkfs_eom"
path2 = os.getcwd()+"/WKFS_EOM_TEST_FOLDER/wkfs_eom_test"
path3 = os.getcwd()+"/WKFS_EOM_TEST_FOLDER/wkfs_compare"
files1 = [os.path.join(path1, x) for x in os.listdir(path1) if '.csv' in str(x)]
files2 = [os.path.join(path2, x) for x in os.listdir(path2) if '.csv' in str(x)]

for file_location_1 in files1:
    file_name_1 = (file_location_1.split("/"))[-1]
    file_location_2 = path2+"/"+file_name_1
    
    print(f"Here is the file : {file_name_1}")
    if file_location_2 in files2 :
        df1 = pd.read_csv(file_location_1, sep=";", index_col=False)
        df2 = pd.read_csv(file_location_2, sep=";", index_col=False)
        df_diff = pd.concat([df1,df2]).drop_duplicates(keep=False)

        df_diff.to_csv(path3+"/"+file_name_1, sep=";", index=False)
