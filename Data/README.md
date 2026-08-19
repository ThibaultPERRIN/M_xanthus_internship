## ===< DATASETS >===

--------

<br>

<ins>**20260727_FB_homogenisation_conditions_count**</ins>


- Use: CAN be used in Python (data)
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

\

--------

\

<ins>**20260804_CFU_assay**</ins>


- Use: CANNOT be used in python (observation)
- Description:
  - CFU assay from individual FB (Fruiting body) spores isolation experiment, using 20 FBs
  - Three replicates in the dataset (one replicate per day): *27/07/2026*, *29/07/2026* & *04/08/2026* 
- Experiment:
  - (1) Myxospores isolation protocol
  - (2) Imaging conditions:
    - 200 µL concentrated solution (without homogenisation)
    - 'Usual' protocol (with homogenisation)
  - (3) CFU assays: Colonies counted after days from inoculation 
- Features
  - *Group* (str): Group corresponding to a replicate
  - *Usual protocol* (int): 'Usual protocol' condition
  - *200 concentrated* (int): 200 µL concentrated condition


--------


20260804_Myxospores_isolation_isolated_FB_protocol_conditions


- Description:
- Experiment:
- Features:
  - Image_ID
  - Condition_protocol
  - N_clumps
  - Manual_count_objects
  - Object_type


--------


- Description:
- Experiment:
- Features




- Description:
- Experiment:
- Features




- Description:
- Experiment:
- Features

