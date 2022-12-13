import geopandas as gpd
import os
import pandas as pd
root_dir=r'/home/cagis/satscan'
base_dir=r'/home/cagis/satscan/out'

df_list=[gpd.read_file(os.path.join(base_dir,f'{i}','out.col.shp')) for i in range(1000)]
rdf = gpd.GeoDataFrame( pd.concat( df_list, ignore_index=True) )
rdf.to_file(os.path.join(root_dir,'out.shp'))
