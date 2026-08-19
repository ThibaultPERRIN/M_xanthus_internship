## ===< DATASETS >===

--------

20260727_FB_homogenisation_conditions_count


- Description:
  - Test the impact, through different experimental parameters (Amplitude, Pulse, Time) of the myxospores solution's homogenisation (2nd sonication -  c.f. myxospores isolation protocol).
  - Two replicates in the dataset: *20/07/2026* & *27/07/2026*
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
  - *Cluster_size* (str): Size of the clusters. Arbitrary chosen: $None = No cluster$ ; $Small \geq 3 objects$ ; $Medium \geq 20 objects$ ; $Large \geq 50 objects$


--------
