from pathlib import Path
import geopandas as gpd 


BASE_DIR = Path(r'\\TCMHarwell\Harwell\ProjectData\2019\PN19032_EAD_Habitat_Mapping\02_Processed_Data\WV_2014_HabitatMap\Habitat_Orthotile_Intersection')
folders = [x for x in BASE_DIR.iterdir() if not x.name == 'no_habitat_join']
counter = len(folders)
for folder in folders:
    pt = [x for x in folder.iterdir() if x.name.endswith('points.shp')][0]
    print(pt)
    pt_df = gpd.read_file(pt)
    new_names = ['ID', 'Hab_name', 'Hab_num', 'Hab_subname', 'Hab_subnum', 'QC_name', 'QC_num', 'QC_subname', 'QC_subnum', 'QC_by', 'geometry']
    pt_df.columns = new_names
    pt_df['Correction'] = 0
    new_order = ['ID', 'Hab_name', 'Hab_num', 'Hab_subname', 'Hab_subnum', 'QC_name', 'QC_num', 'QC_subname', 'QC_subnum', 'QC_by', 'Correction', 'geometry']
    pt_df = pt_df[new_order]
    pt_df.to_file(pt)
    counter -= 1
    print(counter)
    print(pt.name)
    