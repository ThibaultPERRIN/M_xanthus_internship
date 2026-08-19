## ===< DATASETS >===

--------

Folder: <ins>20260804_measurements_FB_colonies</ins>
 - 20260804_Measurements_FB_size_Group_1-1_concentrated.csv
 - 20260804_Measurements_FB_size_Group_1-1_usual.csv
 - 20260804_Measurements_FB_size_Group_2-1_concentrated.csv
 - 20260804_Measurements_FB_size_Group_2-2_usual.csv
 - 20260804_Measurements_FB_size_Group_3-1_concentrated.csv
 - 20260804_Measurements_FB_size_Group_3-2_usual.csv

<br>

- Description:
  - Measurements of FB area
  - One dataframe per group per experimental condition
- Experiment:
  - (1) Imaging FBs plates
  - (2) Harvest of 20 FBs per experimental condition
  - (3) Myxospores isolation protocol
  - Experimental conditions:
    - *200_concentrated*: 200 µL concentrated solution (without homogenisation)
    - *Homogenised*: 'Usual' protocol (with homogenisation)
- Features:
  - *Area* (float): Area of a FB in pixels
  - Other features are uninteresting
- Use: CAN be used in programming language (data)

--------

<ins>20260727_FB_homogenisation_conditions_count.xlsx</ins>


- Description:
  - Test the impact, through different experimental parameters (Amplitude, Pulse, Time) of the myxospores solution's homogenisation (2nd sonication -  c.f. myxospores isolation protocol).
  - Two replicates in the dataset (one replicate per day): *20/07/2026* & *27/07/2026*
- Experiment:
  - (1) Myxospores isolation protocol
  - (2) Homogenisation - 2nd Sonication:
      | *Amplitude* | *Pulse (ON/OFF)* | *Time* | Optional description                      |
      | :---------- | :--------------- | :----- | ----------------------------------------: |
      | 20          | 5 / 15           | 30     | ×                                         |
      | 20          | 10 / 15          | 30     | ×                                         |
      | 20          | 20 / 15          | 15     | ×                                         |
      | 25          | 5 / 15           | 30     | ×                                         |
      | 25          | 10 / 15          | 30     | ×                                         |
      | 25          | 20 / 15          | 15     | ×                                         |
      | 28          | 5 / 15           | 30     | ×                                         |
      | 28          | 10 / 15          | 30     | Usual condition used from begining        |
      | --           | -------         | --     | 'Control' / 'Unsonicated' = No sonication |
      
- Features:
  - *Image_ID* (str): Image identification 
  - *Replicat_group* (int): Replicate (Group per day)
  - *Amplitude* (int): Amplitude of 2nd sonication
  - *Pulse* (str): Pulse of 2nd sonication
  - *Time* (int): Duration of 2nd sonication
  - *N_objects* (int): Number of objects (vegetative cells  and spores) manually counted
  - *N_cluster* (int): Number of clusters manually counted
  - *Cluster_size* (str): Size of the clusters. Arbitrary chosen:
    - $None = No cluster$ ;
    - $Small \geq 3 objects$ ;
    - $Medium \geq 20 objects$ ;
    - $Large \geq 50 objects$
- Use: CAN be used in programming language (data)

--------

<ins>20260804_CFU_assay.xlsx</ins>


- Description:
  - CFU assay from individual FB (Fruiting body) spores isolation experiment, using 20 FBs
  - Three replicates in the dataset (one replicate per day): *27/07/2026*, *29/07/2026* & *04/08/2026* 
- Experiment:
  - (1) Imaging FBs plates 
  - (2) Myxospores isolation protocol
  - (3) Imaging conditions:
    - 200 µL concentrated solution (without homogenisation)
    - 'Usual' protocol (with homogenisation)
  - (4) CFU assays: Colonies counted after days from inoculation 
- Features
  - *Group* (str): Group corresponding to a replicate
  - *Usual protocol* (int): 'Usual protocol' condition
  - *200 concentrated* (int): 200 µL concentrated condition
- Use: CANNOT be used in programming language (observation)


--------

<ins>20260804_Myxospores_isolation_isolated_FB_protocol_conditions.xlsx</ins>


- Description:
  - Myxospores isolation protocol's application for indidividual FBs
- Experiment:
  - (1) Imaging FBs plates
  - (2) Harvest of 20 FBs per experimental condition
  - (3) Myxospores isolation protocol
  - Experimental conditions:
    - *200_concentrated*: 200 µL concentrated solution (without homogenisation)
    - *Homogenised*: 'Usual' protocol (with homogenisation)
- Features:
  - *Image_ID* (str): Image identification 
  - *Condition_protocol* (str): Experimental conditions
  - *N_clumps* (int): Number of clumps observed (arbitrary measurement, clumps = 3 cells minimum with cell membrane touching)
  - *Manual_count_objects* (int): Objects counted by hand on fiji
  - *Object_type* (int): Differenciation between cell types - spores ("Spore") and vegetative cells ("VC")
- Use: CAN be use in programming language (data)


--------

<ins>20260811_Myxospores_size.xlsx</ins>


- Description:
  - FBs plates observed
  - Spores' size manual measurements on Fiji
  - Three replicates in the dataset (one replicate per day): *27/07/2026*, *29/07/2026* & *04/08/2026* 
- Experiment:
  - (1) Imaging FBs plates
  - (2) Harvest of 20 FBs per experimental condition
  - (3) Myxospores isolation protocol
  - Experimental conditions:
    - *200_concentrated*: 200 µL concentrated solution (without homogenisation)
    - *Homogenised*: 'Usual' protocol (with homogenisation)
- Features:
  - *Image_ID* (str): Image identification 
  - *Condition_protocol* (str): Experimental conditions
  - *Size_µm* (float): Manual measurement in µm
- Use: CAN be used in programming language (data)


--------

<ins>20260812_Results_automated_workflow.csv</ins>


- Description:
  - Myxospores isolation protocol's application for indidividual FBs
  - Output dataset from images processed automatically with a python script (c.f. Automated_workflow)
- Experiment:
  - (1) Imaging FBs plates
  - (2) Harvest of 20 FBs per experimental condition
  - (3) Myxospores isolation protocol
  - Experimental conditions:
    - *200_concentrated*: 200 µL concentrated solution (without homogenisation)
    - *Homogenised*: 'Usual' protocol (with homogenisation)
- Features:
  - *Image_ID* (str): Image identification 
  - *Label* (int): Labelled object (scikit-image `regionprops`)
  - *Cell_type* (str): Differenciation between cell types - spores ("Spore") and vegetative cells ("VC")
  - *Area* (float): 'Area', here the volume in hyperstacked images (scikit-image `regionprops`)
  - *Volume* (float): Volume computed
  - *Surface_area* (float): Surface_area of the cell (scikit-image `regionprops`)
  - *Sphericity* (float): Sphericity computed
  - *Axis_major_length* (float): Axis major length (scikit-image `regionprops`)
  - *Axis_minor_length* (float): Axis minor length (scikit-image `regionprops`)
- Use: CAN be used in programming language (data)



