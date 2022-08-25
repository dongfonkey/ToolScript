import os
import argparse
import csv
import numpy as np
import pandas as pd
import xarray as xr
from xarray_extras.csv import to_csv
from xarray_extras.backport.pandas import to_csv


def write_to_csv(dict_item, head, path):
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writerow(dict_item)
    f.close()


def get_files_name(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] == '.nc':
                files_list.append(file)
    return files_list

def extract_nc(input_path, output_path):
    header = ["time", "depth(m)", "latitude", "longitude", "chl(mg m-3)", "no3(mmol m-3)", "nppv(mg m-3 day-1)", "o2(mmol m-3)", "po4(mmol m-3)", "si(mmol m-3)"]
    with open(output_path, "w", encoding="utf8") as f_clean:
        f_clean.write(",".join(header) + "\n")
    f_clean.close()

    nc_obj = xr.open_dataset(input_path)
    time_shape = nc_obj["time"].shape[0]
    longitude_shape = nc_obj['longitude'].shape[0]
    latitude_shape = nc_obj['latitude'].shape[0]
    depth_shape = nc_obj['depth'].shape[0]

    nc_ndarray = nc_obj.as_numpy()

    #time遍历
    for time_index in range(0, time_shape):
        time_value = nc_obj['time'][time_index].values
        #depth遍历
        for depth_index in range(0, depth_shape):
            depth_value = nc_obj['depth'][depth_index].values
            #遍历latitude
            for latitude_index in range(0, latitude_shape):
                latitude_value = nc_obj['latitude'][latitude_index].values

                print(nc_obj['chl'][time_index][depth_index][latitude_index].values)

                '''
                #遍历longitude
                for longitude_index in range(0, longitude_shape):
                    longitude_value = nc_obj['longitude'][longitude_index].values
                    
                    #抽取信息
                    chl_value = nc_obj.variables['chl'][time_index][depth_index][latitude_index][longitude_index].values
                    no3_value = nc_obj['no3'][time_index][depth_index][latitude_index][longitude_index].values
                    nppv_value = nc_obj['nppv'][time_index][depth_index][latitude_index][longitude_index].values
                    o2_value = nc_obj['o2'][time_index][depth_index][latitude_index][longitude_index].values
                    po4_value = nc_obj['po4'][time_index][depth_index][latitude_index][longitude_index].values
                    si_value = nc_obj['si'][time_index][depth_index][latitude_index][longitude_index].values
                    record_dict = {
                        "time": time_value,
                        "depth(m)": depth_value,
                        "latitude": latitude_value,
                        "longitude": longitude_value,
                        "chl(mg m-3)": chl_value,
                        "no3(mmol m-3)": no3_value,
                        "nppv(mg m-3 day-1)": nppv_value,
                        "o2(mmol m-3)": o2_value,
                        "po4(mmol m-3)": po4_value,
                        "si(mmol m-3)": si_value
                    }
                    write_to_csv(record_dict, header, output_path)
                '''



def main():
    
    '''
    parser = argparse.ArgumentParser(description="将某个目录下的nc文件抽取为csv文件")
    parser.add_argument("-d", "--directory", help="nc文件所在目录", dest="files_dir", type=str, default=None)
    parser.add_argument("-o", "--output", help="输出文件的目标目录", dest="output_dir", type=str, default=None)
    args = parser.parse_args()



    #Define
    if args.files_dir is None:
        root_dir = os.getcwd()
    else:
        root_dir = args.files_dir
    if args.output_dir is None:
        output_dir = os.getcwd()
    else:
        output_dir = args.output_dir
    
    print(root_dir + "\n" + output_dir)
    

    

    root_files_list = get_files_name(root_dir)
    for file in root_files_list:
        input = os.path.join(root_dir, file)
        output = os.path.join(output_dir, file.replace(".nc", ".csv"))
        extract_nc(input, output)
        print(file + "\thas done!!!")

    '''
    

    input = "mercatorfreebiorys2v4_global_mean_20190101.nc"
    output = "chl.csv"
    extract_nc(input, output)







if __name__ == '__main__':
    main()