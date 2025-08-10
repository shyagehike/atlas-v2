import numpy as np, pandas as pd, h3

def set_regions(dataframe:pd.DataFrame,res_region:int=2,res_fold:int=1,min_events_per_region:int=13,max_neighbor_k:int=3):
    # set regions & folds for CV blocking (not to be fed into the model!!!)
    dF=dataframe.copy()
    fold_regions={}
    mapping={}

    # assign region_id (finer) and fold_id (coarser)
    dF["region_id"]=[h3.latlng_to_cell(float(lat),float(lon),res_region)for lat,lon in zip(dF["latitude_center"],dF["longitude_center"])]
    dF["fold_id"]=[h3.cell_to_parent(c,res_fold) for c in dF["region_id"]]

    # get counts per (fold, region)
    grp=dF.groupby(["fold_id","region_id"]).size().rename("cnt").reset_index()
    counts={(r.fold_id,r.region_id): int(r.cnt) for r in grp.itertuples(index=False)}
    for r in grp.itertuples(index=False):fold_regions.setdefault(r.fold_id,set()).add(r.region_id)

    # find small regions and build replacement mapping
    small=[(r.fold_id,r.region_id) for r in grp.itertuples(index=False) if r.cnt<min_events_per_region]

    for fold,region in small:
        replacement=None
        # search outward in H3 rings & join to meet minimum events per region
        for k in range(1,max_neighbor_k+1):
            for nb in h3.grid_disk(region,k):
                if nb==region or nb not in fold_regions.get(fold,()): continue
                if counts.get((fold,nb),0)>=min_events_per_region:
                    replacement=nb
                    break
            if replacement==None:break
        if replacement==None:replacement=f"{fold}-OTHER"
        mapping[(fold,region)]=replacement

    if mapping:dF["region_id"]=dF.apply(lambda r:mapping.get((r["fold_id"],r["region_id"]),r["region_id"]),axis=1)
    return dF

def add_index(dataframe:pd.DataFrame):
    # self explanatory no?
    dF=dataframe.copy()
    dF.insert(0,'event_id',range(0,len(dF)))
    return dF

def concatenate(*dataframes:pd.DataFrame):
    # also now time to assign regions for blocked CV
    dF=add_index(set_regions(pd.concat(dataframes).reset_index(drop=True)))
    dF=dF[dF['spatial_uncertainty']<np.percentile(dF['spatial_uncertainty'],95)] # remove highest 5% of points there are genuinely some outliers that skew the dataset by an unreasonable amount (see figures somewhere)

    return dF