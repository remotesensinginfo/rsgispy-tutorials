# rsgispy Tutorials

A set of Jupyter notebook tutorials for [rsgispy](https://rsgispy.readthedocs.io),
a pure-Python library for remote sensing and GIS data processing built on
rasterio, GeoPandas, NumPy and scikit-learn. The tutorials start with
reading an image and calculating an index, and build up to classification,
regression, change detection, spectral unmixing, hydrology, chained
tile-graph workflows and three case studies.

The tutorials are a port of the
[RSGISLib tutorials](https://github.com/remotesensinginfo/rsgislib-tutorials)
to rsgispy, reorganised so that each section builds on the ones before it.

## Installation

Create the conda environment (it installs rsgispy and everything the
notebooks use), then start JupyterLab:

```bash
conda env create -f environment.yml
conda activate rsgispy-tutorials
jupyter lab
```

The data in `data/` (about 1 GB) is stored with [Git LFS](https://git-lfs.com/).
Install Git LFS before cloning, or run `git lfs pull` after cloning.

Each notebook reads its inputs from `../data` and writes its outputs to the
`outputs/` folder of its own section, so `data/` is never changed. Run the
notebooks in each section in order: some read the outputs of earlier
notebooks in the same section. A few notebooks need a network connection:
the vector maps notebook downloads basemap tiles, and section 12 downloads
data.

## The tutorials

| Section | Notebook | What it covers | Run time |
| --- | --- | --- | --- |
| **1. Getting started** | [01_image_basics_and_ndvi](01_getting_started/01_image_basics_and_ndvi.ipynb) | Image information, band maths, NDVI, statistics and a first map | < 1 min |
| **2. Making maps** | [01_intro_matplotlib](02_making_maps/01_intro_matplotlib.ipynb) | How Matplotlib figures and axes work, and the rsgispy plot style | < 1 min |
| | [02_maps_from_eo_data](02_making_maps/02_maps_from_eo_data.ipynb) | Maps of multi-band satellite images, with scale bars, north arrows and maps side by side | < 1 min |
| | [03_maps_from_vector_data](02_making_maps/03_maps_from_vector_data.ipynb) | Maps of vector layers, with basemaps | < 1 min |
| | [04_combining_data_sources](02_making_maps/04_combining_data_sources.ipynb) | Matching projections and mapping several layers together | < 1 min |
| **3. Vector data and zonal statistics** | [01_zonal_statistics](03_vector_data_and_zonal_stats/01_zonal_statistics.ipynb) | Extracting image values to points and summarising them in polygons | < 1 min |
| | [02_semivariograms](03_vector_data_and_zonal_stats/02_semivariograms.ipynb) | Random sample points and empirical semi-variograms | < 1 min |
| **4. Image classification** | [01_rule_based_classification](04_image_classification/01_rule_based_classification.ipynb) | Spectral indices and rule-based classification | ~1 min |
| | [02_unsupervised_classification](04_image_classification/02_unsupervised_classification.ipynb) | Clustering with K-means, mean shift and other algorithms, and applying a fitted clusterer to another image | ~1 min |
| | [03_supervised_pixel_classification](04_image_classification/03_supervised_pixel_classification.ipynb) | Training samples, a random forest and applying it to an image | ~2 min |
| | [04_object_based_classification](04_image_classification/04_object_based_classification.ipynb) | Segmentation and classifying segments | ~1 min |
| **5. Regression** | [01_intro_and_explore_data](05_regression/01_intro_and_explore_data.ipynb) | A forest inventory regression problem, explored with lidar metrics | ~1 min |
| | [02_feature_selection](05_regression/02_feature_selection.ipynb) | Selecting features with VIF, correlation, CQV and LassoLars | ~1 min |
| | [03_simple_linear_regression](05_regression/03_simple_linear_regression.ipynb) | A simple linear regression, applied to an image | ~1 min |
| | [04_multiple_linear_regression](05_regression/04_multiple_linear_regression.ipynb) | Multiple linear regression with the selected features, and jackknife and k-fold assessment | ~1 min |
| | [05_multivariate_regression](05_regression/05_multivariate_regression.ipynb) | Tuning and applying an Extra Trees regressor for several variables | ~1 min |
| | [06_compare_regressors](05_regression/06_compare_regressors.ipynb) | Comparing six regressors with repeated k-fold cross-validation | ~1 min |
| **6. Change detection** | [01_create_baseline_class](06_change_detection/01_create_baseline_class.ipynb) | A baseline mangrove classification with XGBoost | ~1 min |
| | [02_map_to_map_change](06_change_detection/02_map_to_map_change.ipynb) | Comparing two classifications | ~1 min |
| | [03_image_to_image_change](06_change_detection/03_image_to_image_change.ipynb) | Differences and ratios of spectral indices | ~1 min |
| | [04_map_to_image_change](06_change_detection/04_map_to_image_change.ipynb) | Finding changed pixels of a class in a new image | ~1 min |
| | [05_multivariate_change_detection](06_change_detection/05_multivariate_change_detection.ipynb) | Change vector analysis, slow feature analysis and IR-MAD compared | ~2 min |
| **7. Spectral analysis** | [01_spectral_analysis_intro](07_spectral_analysis/01_spectral_analysis_intro.ipynb) | Spectra, spectral resampling and continuum removal | < 1 min |
| | [02_hyperspectral_image_analysis](07_spectral_analysis/02_hyperspectral_image_analysis.ipynb) | Hyperspectral metadata, smoothing, PCA, MNF and continuum removal of an image | ~1–2 min |
| | [03_spectral_unmixing](07_spectral_analysis/03_spectral_unmixing.ipynb) | Endmembers (including PPI) and linear spectral unmixing | ~3 min |
| **8. Hydrology** | [01_hydrological_analysis](08_hydrology/01_hydrological_analysis.ipynb) | Conditioning a DEM, flow routing, streams, watersheds, HAND flooding and terrain indices | ~2 min |
| **9. Tile-graph workflows** | [01_indices_classification_filtering](09_tile_graph_workflows/01_indices_classification_filtering.ipynb) | Indices, a random forest classification and a majority filter chained in one in-memory tile graph | ~2 min |
| **10. Case study: ICESat-2 bathymetry** | [01_visualise_icesat2](10_case_study_icesat2_bathymetry/01_visualise_icesat2.ipynb) | The ICESat-2 depth points | ~1 min |
| | [02_landsat_composites](10_case_study_icesat2_bathymetry/02_landsat_composites.ipynb) | Composites of a stack of Landsat images: max-NDVI/NDWI, geomedian, median and quality mosaics | ~1.5 min |
| | [03_landsat_composite_bathymetry](10_case_study_icesat2_bathymetry/03_landsat_composite_bathymetry.ipynb) | A bathymetry map from a composite and ICESat-2 depths | ~1 min |
| | [04_landsat_scenes_bathymetry](10_case_study_icesat2_bathymetry/04_landsat_scenes_bathymetry.ipynb) | Bathymetry from individual scenes, combined | ~1 min |
| | [05_cshelph_bathymetry](10_case_study_icesat2_bathymetry/05_cshelph_bathymetry.ipynb) | *Optional:* classifying ICESat-2 photons with C-SHELPh | needs data |
| **11. Case study: species distribution modelling** | [01_prepare_datasets](11_case_study_species_distribution/01_prepare_datasets.ipynb) | Cleaning and thinning species records, and choosing habitat variables from the species' ecology | < 1 min |
| | [02_species_distribution_modelling](11_case_study_species_distribution/02_species_distribution_modelling.ipynb) | A logistic regression SDM: collinearity, spatial cross-validation, AUC/TSS/Boyce, null models, response curves, jackknife, SHAP and Sobol interpretation, uncertainty, extrapolation (MESS/ExDet) and a warming scenario | ~2 min |
| | [03_maxent_species_distribution_modelling](11_case_study_species_distribution/03_maxent_species_distribution_modelling.ipynb) | A MaxEnt SDM: feature classes, regularisation tuning (spatial CV and AICc), clamping | ~2 min |
| | [04_random_forest_species_distribution_modelling](11_case_study_species_distribution/04_random_forest_species_distribution_modelling.ipynb) | A random forest SDM: tuning, over-fitting and spatial CV, tree-based interpretation | ~2 min |
| | [05_compare_sdm_models](11_case_study_species_distribution/05_compare_sdm_models.ipynb) | Comparing the logistic regression, MaxEnt and random forest SDMs: accuracy, maps, consensus, responses, importance and projections | < 1 min |
| **12. Downloading data** | [01_dwnld_usgs_landsat_scenes](12_downloading_data/01_dwnld_usgs_landsat_scenes.ipynb) | Landsat scenes from the USGS (M2M API) | account |
| | [02_nasa_cmr_download_icesat2](12_downloading_data/02_nasa_cmr_download_icesat2.ipynb) | ICESat-2 data from NASA's CMR | account |
| | [03_nasa_cmr_download_gedi](12_downloading_data/03_nasa_cmr_download_gedi.ipynb) | GEDI data from NASA's CMR | account |
| | [04_nasa_cmr_download_modis](12_downloading_data/04_nasa_cmr_download_modis.ipynb) | MODIS data from NASA's CMR | account |
| | [05_copernicus_odata_sen1](12_downloading_data/05_copernicus_odata_sen1.ipynb) | Sentinel-1 from the Copernicus Data Space | account |
| | [06_copernicus_odata_sen2](12_downloading_data/06_copernicus_odata_sen2.ipynb) | Sentinel-2 from the Copernicus Data Space | account |
| | [07_planet_psscene](12_downloading_data/07_planet_psscene.ipynb) | PlanetScope scenes from the Planet API | account |
| | [08_icepyx_download_icesat2](12_downloading_data/08_icepyx_download_icesat2.ipynb) | ICESat-2 ATL03 data with icepyx (used by 10.05) | account |
| **13. Case study: wetland mapping (TropWet)** | [01_composite_and_endmembers](13_case_study_wetland_mapping/01_composite_and_endmembers.ipynb) | A Landsat median composite, the NDVI / MNDWI feature space, automatic TropWet endmember selection and checking it (a bright sand endmember) | < 1 min |
| | [02_unmixing_and_classification](13_case_study_wetland_mapping/02_unmixing_and_classification.ipynb) | Comparing the UCLS / NNLS / FCLS solvers and the endmember sets by their error, a per-pixel model choice (MESMA), the burn correction, the TropWet classes and their sensitivity to the class limits | < 1 min |
| | [03_change_and_accuracy](13_case_study_wetland_mapping/03_change_and_accuracy.ipynb) | Classifying each date, wetland change 1997–2018 (from–to table, gain / loss map) and checking the classes against reference polygons | < 1 min |

Run times are from a recent laptop (Apple M2 Max). The notebooks in
section 12 need a user account with each data provider. They read the login
details from a credentials file you create, as each notebook explains; none
of the other sections need them, because they use the data in `data/`.
Section 13 builds on the rsgispy guide
[Spectral unmixing for wetland mapping (TropWet)](https://rsgispy.readthedocs.io/en/latest/guides/spectral_unmixing.html)
and uses the Landsat images of section 6. The
C-SHELPh notebook needs the optional `cshelph` package and the ICESat-2 data
downloaded by `12_downloading_data/08_icepyx_download_icesat2`.

## For RSGISLib users

rsgispy covers almost all of RSGISLib, but the function names, modules and
some arguments differ, and rsgispy has no raster attribute tables (RATs):
thematic images use colour tables, and object-based workflows keep the
per-segment statistics in a vector layer or table. The notebooks point out
these differences in "**RSGISLib users:**" notes. The
[migration guide](https://rsgispy.readthedocs.io/en/latest/guides/migrating_from_rsgislib.html)
lists the rsgispy equivalent of each RSGISLib function.

The inputs that RSGISLib read as KEA files are GeoTIFFs here, converted
with `tools/convert_kea_data.py`.

## Testing the notebooks

`tools/run_notebooks.py` runs every notebook (or the sections or notebooks
you name) and reports pass / fail and the run time of each. Cells tagged
`skip-execution` (logins and downloads) are not run.

```bash
python tools/run_notebooks.py
python tools/run_notebooks.py 05_regression --save
```

## Licence

MIT; see [LICENSE](LICENSE).
