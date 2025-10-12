# global landslide prediction with physics-informed neural network
developing an early warning system to save lives in East Africa and beyond

## mission
every year, landslides kill over 4,500 people globally, with developing nations bearing a large fraction of casualties despite having the fewest resources for prediction, prevention, and relief.
this project develops a physics-informed, temporally-aware AI model that can predict landslides at an hourly cadence using limited data, specifically designed for deployment in resource-constrainted regions of the world (namely, east africa)

## problem
current landslide prediction systems often fail or have limited utility in real-world deployment because they:
- require massive amounts of high-quality data, which doesn't exist in vulnerable regions
- ignore temporal effects that can accumulate over weeks
- can't handle uncertain or missing location data
- need heavy computational resources to run
- generate too many false alarms, causing warning fatigue

## key innovations
1. continuous spatial probability fields (dropped a grid based approach in favor of modeling landslide risk as a continuous probabilistic distribution through log-gaussian cox processes), saving parameters and allowing us to query risk at any location
2. physics informed temporal modeling
3. uncertainty-aware training (first landslide model to handle coordinate uncertainties, enables the use of more training data previously considered "unusable")
4. multi-resolution fusion (allows the elegant combination of data at different spatial resolutions without information loss)

in 2023, i witnessed the aftermath of heavy rains in Rwanda that triggered flooding and landslides in northwestern rwanda, destroying nearly 6 thousand homes (damaging 2.5 thousand extra), 26 bridges, over a dozen roads, a dozen power stations, eight water treatment plants, five health centers, and a hospital.
130 people died as well as thousands of livestock.
these historically unusual rainfall patterns can largely be attributed to climate change, according to rwanda's local weather authority
see:
- https://www.usnews.com/news/world/articles/2023-05-04/rwanda-floods-kill-130-destroy-over-5-000-houses
- https://www.thestatesman.com/world/135-killed-over-20k-displaced-in-recent-flooding-landslides-in-rwanda-1503181246.html
- https://www.bbc.com/news/world-africa-65469374

output.csv/main.csv downloads: https://drive.google.com/drive/folders/1jUbqnbn_2SpEdACm7KCuOAGVMVHU96oE?usp=drive_link

this repository is currently private.
