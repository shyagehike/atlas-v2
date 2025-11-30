# ATLAS v2 - Global Landslide Prediction with a Random Fourier Features + Log-Gaussian Cox Process Model
An open-source early-warning framework for near-real-time landslide risk prediction to prevent landslide fatalities around the world 

## The Problem(s)
Every year, landslides kill over 4,500 people globally, with developing nations bearing a large fraction of casualties despite having the fewest resources for prediction, prevention, and relief.
This project develops an RFF LGCP model that can predict landslides at an hourly cadence using limited data, specifically designed for deployment in resource-constrained regions of the world (namely, sub-Saharan Africa)

Current landslide prediction systems often fail or have limited utility in real-world deployment because they:
- require massive amounts of high-quality data, which doesn't exist in vulnerable regions
- ignore temporal effects that can accumulate over weeks
- can't handle uncertain or missing location data
- need heavy computational resources to run
- generate too many false alarms, causing warning fatigue

## Key Innovations
1. Continuous Spatial Probability Fields (dropped a grid based approach in favor of modeling landslide risk as a continuous probabilistic distribution through log-gaussian cox processes parametrized via RFFs, saving parameters and allowing us to query risk at any location)
3. Uncertainty-Aware Training (the model explicitly accounts for coordinate, labeling, & temporal uncertainties by weighting certain samples rather than discarding them, expanding usable training data and improving redundancy to real-world noise)
4. Multi-Resolution Fusion (allows the elegant combination of data at different spatial resolutions without information loss (resolution invariance))
5. Computational Efficiency & Transparency (training completes in under 8 hours on standard hardware; localized inference runs in under a minute + all data sources are open and freely accessible via primarily Google Earth Engine)

## Citations
1. Cooperative Open Online Landslide Repository (COOLR):
Kirschbaum, D.B., Stanley, T., & Zhou, Y. (2015). Spatial and temporal analysis of a global landslide catalog. Geomorphology, 249, 4-15. doi:10.1016/j.geomorph.2015.03.016
Kirschbaum, D.B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52, 561-575. doi:10.1007/s11069-009-9401-4

2. Global Fatal Landslide Dataset (GFLD, courtesy of Prof. Dave Petley):
Froude, M. J. and Petley, D. N.: Global fatal landslide occurrence from 2004 to 2016, Nat. Hazards Earth Syst. Sci., 18, 2161–2181, https://doi.org/10.5194/nhess-18-2161-2018, 2018.

3. NASADEM (courtesy of NASA / USGS / JPL-Caltech via GEE):
NASA JPL (2020). NASADEM Merged DEM Global 1 arc second V001 [Data set]. NASA EOSDIS Land Processes DAAC. Accessed 2025-10-26 from doi:10.5067/MEaSUREs/NASADEM/NASADEM_HGT.001

4. OpenLandMap Sand & Clay Content (courtesy of EnvirometriX Ltd via GEE)
Tomislav Hengl. (2018). Sand content in % (kg / kg) at 6 standard depths (0, 10, 30, 60, 100 and 200 cm) at 250 m resolution (Version v02) [Data set]. 10.5281/zenodo.1476851
https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_CLAY-WFRACTION_USDA-3A1A1A_M_v02

5. ESA WorldCover v200 (courtesy of ESA WorldCover Consortium via GEE)
Zanaga, D., Van De Kerchove, R., Daems, D., De Keersmaecker, W., Brockmann, C., Kirches, G., Wevers, J., Cartus, O., Santoro, M., Fritz, S., Lesiv, M., Herold, M., Tsendbazar, N.E., Xu, P., Ramoino, F., Arino, O., 2022. ESA WorldCover 10 m 2021 v200. (doi:10.5281/zenodo.7254221)

6. Global Precipitation Measurement (GPM, courtesy of NASA GES DISC at NASA Goddard Space Flight Center via GEE)
Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2019), GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V06, Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: 2025-10-26, doi:10.5067/GPM/IMERG/3B-HH/07

7. ERA5-Land Hourly - ECMWF Climate Reanalysis (courtesy of Copernicus Climate Data Store via GEE)
Muñoz Sabater, J., (2019): ERA5-Land monthly averaged data from 1981 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). (2025-10-26), doi:10.24381/cds.68d2bb30

8. MOD13Q1.061 Terra Vegetation Indices 16-Day Global (courtesy of NASA LP DAAC at the USGS EROS Center via GEE)
Didan, K. (2021). MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V061 [Data set]. NASA Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD13Q1.061 Date Accessed: 2025-10-26

9. MERIT Hydro: Global Hydrography Datasets (for upstream catchment area) (courtesy of Dai Yamazaki (University of Tokyo) via GEE)
Yamazaki D., D. Ikeshima, J. Sosa, P.D. Bates, G.H. Allen, T.M. Pavelsky. MERIT Hydro: A high-resolution global hydrography map based on latest topography datasets Water Resources Research, vol.55, pp.5053-5073, 2019, doi:10.1029/2019WR024873

10. SoilGrids 250m 2.0 - Volumetric Water Content (courtesy of ISRIC via GEE)
Global mapping of volumetric water retention at 100, 330 and 15000 cm suction using the WoSIS database Turek M.E., Poggio L., Batjes N.H., Armindo R.A., de Jong van Lier Q., de Sousa L., Heuvelink G.B.M. (2023) International Soil and Water Conservation Research, 11 (2), pp. 225-239.

11. JRC Global Surface Water Mapping Layers (for masking) (courtesy of EE JRC / Google via GEE)
Jean-Francois Pekel, Andrew Cottam, Noel Gorelick, Alan S. Belward, High-resolution mapping of global surface water and its long-term changes. Nature 540, 418-422 (2016). (doi:10.1038/nature20584)

## Extra Notes

In 2023, I witnessed the aftermath of heavy rains in East Africa that triggered flooding and landslides in Northwestern Rwanda, among other places, destroying nearly 6 thousand homes (damaging 2.5 thousand extra), 26 bridges, over a dozen roads, a dozen power stations, eight water treatment plants, five health centers, and a hospital. 130 people died as well as thousands of livestock. These historically unusual rainfall patterns can largely be attributed to climate change, according to Rwanda's local weather authority. See:
- https://www.usnews.com/news/world/articles/2023-05-04/rwanda-floods-kill-130-destroy-over-5-000-houses
- https://www.thestatesman.com/world/135-killed-over-20k-displaced-in-recent-flooding-landslides-in-rwanda-1503181246.html
- https://www.bbc.com/news/world-africa-65469374


For technical details on the model and methodology, see the "Model Architecture & Training" section of the model.ipynb notebook (https://github.com/shyagehike/atlas-v2/blob/main/model.ipynb).
output.csv, main.csv, pca.csv, & models/ downloads: https://drive.google.com/drive/folders/1jUbqnbn_2SpEdACm7KCuOAGVMVHU96oE?usp=drive_link (all belong in database/outputs)

Copyright (c) 2025 shyagehike
