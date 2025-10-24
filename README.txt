AUTHORS:
Bowen Cameroon
Bowen Chu
Sari Parvillers

SOURCE:
https://github.com/Sari-Parvillers/Vulnerable-Earth-TW1-2025.git
The repository is public.

CONTACT:
sariparvillers@gmail.com
bowen.chu@student.uva.nl

REQUIREMENTS:
All the required python modules to run the scripts in this folder are in
the "requirement.txt" file.

DATA:

--- lichen_moss_coverage_data.csv ---

Angle: vertical angle of the sampled rock surface. 0 = perfectly vertical, negative values = angled towards the ground
Aspect: absolute aspect of sampled rock surface.
total_cover: combined coverage surface of mosses AND lichens. 0 = no coverage, 1 = full coverage
moss_fraction: of the total_cover, fraction which consists of moss.
* If total_cover is 0.25, and moss_fraction is 0.2, then 0.25 * 0.2 = 0.05 total moss coverage.
* The reason it's noted down this way is because of the methodology we used to estimate coverage.
crustose: true if the sample contained crustose form lichen
foliose: true if the sample contained foliose form lichen
fruticose: true if the sample contained fruticose form lichen
species: form and colour of lichen species we identified on the sample plot
* First character signifies colour. G=Green, Y=Yellow, O=Orange, W=White, BL=Black, GR=Grey
* Second character signifies lichen form. Crustose=c, Foliose=f, and Fruticose=fr
* Example: W_f = white foliose lichen was present
deviation_north: The amount that the aspect deviated from north-facing 
* Example 1: an aspect value of 355 deviates by 5 degrees from north.
* Example 2: An aspect value of 60 deviates by 60 degrees from north.
solar_radiation: amount of average yearly solar radiation in W/m2
elevation: elevation from sea level in metres
no3,no2,nh4,total_nitrogen,po4: nutrient contents in µmol/l as part of a K2SO4 extraction,
obtained from crushed sample rocks of each sample plot.

--- coverage_data_processed.csv ---

All values with identical names as lichen_moss_coverage_data.csv have identical
meaning for this file.

moss_cover: coverage surface of only moss. 0 = no coverage, 1 = full coverage
lichen_cover: coverage surface of only lichen. 0 = no coverage, 1 = full coverage
has_[X]: whether the sample contained a type of lichen species or form (see "species" data entries)


INFO:
This folder contains data, processed data and data analysis from a field
trip in Tenerife conducted by Master's students of the University of Amsterdam,
as part of the Vulnerable Earth course, a first year Earth Science course.

The result is a research proposal titled "Pioneering on lavaflows: how bryophites
 and/or lichen take hold on basaltic a’a lavaflows on Tenerife West."

Each data entry consists of a sample plot. We visually estimated moss and lichen
coverage on a rock surface on lava flows in Tenerife West, took a rock sample,
and noted the angle and aspect, as well as coordinates. 

Our primary data (lichen_moss_coverage_data.csv) contains data gathered from
fieldwork, laboratory analysis of rock samples gathered from each sample plot,
and GIS data. 

Secondary data is very similar but contains markers for presence of specific
kinds of species, and actual moss coverage data.

For information about the research proposal of any of the data, please don't
hesitate to contact us: 
sariparvillers@gmail.com
bowen.chu@student.uva.nl