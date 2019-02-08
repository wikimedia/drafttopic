Model Information:
	 - type: GradientBoosting
	 - version: 0.2
	 - params: {'min_samples_leaf': 1, 'init': None, 'criterion': 'friedman_mse', 'n_estimators': 150, 'verbose': 0, 'min_impurity_split': None, 'subsample': 1.0, 'presort': 'auto', 'population_rates': None, 'multilabel': True, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'learning_rate': 0.1, 'loss': 'deviance', 'warm_start': False, 'max_depth': 5, 'max_features': 'log2', 'random_state': None, 'center': False, 'labels': ['STEM.Technology', 'History_And_Society.History and society', 'Geography.Countries', 'Culture.Food and drink', 'STEM.Time', 'Assistance.Maintenance', 'STEM.Mathematics', 'Assistance.Files', 'Geography.Landforms', 'Culture.Media', 'Culture.Entertainment', 'Geography.Europe', 'STEM.Engineering', 'History_And_Society.Politics and government', 'History_And_Society.Transportation', 'Assistance.Article improvement and grading', 'Culture.Arts', 'Culture.Internet culture', 'STEM.Science', 'STEM.Chemistry', 'STEM.Geosciences', 'History_And_Society.Education', 'Culture.Philosophy and religion', 'Culture.Crafts and hobbies', 'STEM.Information science', 'Geography.Maps', 'Culture.Language and literature', 'Geography.Bodies of water', 'Culture.Plastic arts', 'STEM.Medicine', 'Geography.Cities', 'Assistance.Contents systems', 'Culture.Visual arts', 'History_And_Society.Business and economics', 'History_And_Society.Military and warfare', 'STEM.Physics', 'STEM.Space', 'STEM.Biology', 'Culture.Sports', 'Culture.Broadcasting', 'Culture.Performing arts', 'STEM.Meteorology', 'Geography.Oceania'], 'min_impurity_decrease': 0.0, 'label_weights': {}, 'max_leaf_nodes': None, 'scale': False}
	Environment:
	 - revscoring_version: '2.3.3'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=83357):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'STEM.Technology'                               3768  -->   1301  2467   598  78991
			'History_And_Society.History and society'       6920  -->   1391  5529   502  75935
			'Geography.Countries'                          23713  -->  14111  9602  4093  55551
			'Culture.Food and drink'                        2239  -->   1563   676   165  80953
			'STEM.Time'                                     2208  -->   1531   677   106  81043
			'Assistance.Maintenance'                        4974  -->   1117  3857   233  78150
			'STEM.Mathematics'                              1440  -->    932   508    90  81827
			'Assistance.Files'                               349  -->     24   325   135  82873
			'Geography.Landforms'                           2131  -->   1695   436   135  81091
			'Culture.Media'                                 2014  -->    577  1437   244  81099
			'Culture.Entertainment'                         5450  -->   3540  1910   553  77354
			'Geography.Europe'                             15146  -->   8892  6254  2493  65718
			'STEM.Engineering'                              2115  -->    767  1348   244  80998
			'History_And_Society.Politics and government'   3857  -->   1449  2408   520  78980
			'History_And_Society.Transportation'            3617  -->   2446  1171   335  79405
			'Assistance.Article improvement and grading'      66  -->     20    46   918  82373
			'Culture.Arts'                                  1983  -->   1447   536   110  81264
			'Culture.Internet culture'                      1805  -->    902   903   216  81336
			'STEM.Science'                                  2115  -->    538  1577   148  81094
			'STEM.Chemistry'                                2072  -->   1306   766   278  81007
			'STEM.Geosciences'                              1967  -->   1172   795   138  81252
			'History_And_Society.Education'                 2595  -->   1572  1023   248  80514
			'Culture.Philosophy and religion'               3786  -->   1637  2149   436  79135
			'Culture.Crafts and hobbies'                    1947  -->   1106   841    71  81339
			'STEM.Information science'                      2020  -->   1157   863   124  81213
			'Geography.Maps'                                2399  -->   1378  1021    78  80880
			'Culture.Language and literature'              19434  -->  14113  5321  2329  61594
			'Geography.Bodies of water'                     2223  -->   1727   496   131  81003
			'Culture.Plastic arts'                          3673  -->   2100  1573   411  79273
			'STEM.Medicine'                                 1942  -->   1081   861   250  81165
			'Geography.Cities'                               786  -->    487   299   139  82432
			'Assistance.Contents systems'                   1928  -->    672  1256   151  81278
			'Culture.Visual arts'                           4518  -->   2506  2012   530  78309
			'History_And_Society.Business and economics'    5978  -->   2950  3028   776  76603
			'History_And_Society.Military and warfare'      3864  -->   2410  1454   379  79114
			'STEM.Physics'                                  2363  -->   1240  1123   367  80627
			'STEM.Space'                                    2103  -->   1724   379    90  81164
			'STEM.Biology'                                  3089  -->   1741  1348   261  80007
			'Culture.Sports'                                4801  -->   3956   845   373  78183
			'Culture.Broadcasting'                          2732  -->   1507  1225   382  80243
			'Culture.Performing arts'                       4151  -->   3301   850   391  78815
			'STEM.Meteorology'                              1726  -->   1310   416    56  81575
			'Geography.Oceania'                             3975  -->   2432  1543   198  79184
	rates:
		          'STEM.Technology'    'History_And_Society.History and society'    'Geography.Countries'    'Culture.Food and drink'    'STEM.Time'    'Assistance.Maintenance'    'STEM.Mathematics'    'Assistance.Files'    'Geography.Landforms'    'Culture.Media'    'Culture.Entertainment'    'Geography.Europe'    'STEM.Engineering'    'History_And_Society.Politics and government'    'History_And_Society.Transportation'    'Assistance.Article improvement and grading'    'Culture.Arts'    'Culture.Internet culture'    'STEM.Science'    'STEM.Chemistry'    'STEM.Geosciences'    'History_And_Society.Education'    'Culture.Philosophy and religion'    'Culture.Crafts and hobbies'    'STEM.Information science'    'Geography.Maps'    'Culture.Language and literature'    'Geography.Bodies of water'    'Culture.Plastic arts'    'STEM.Medicine'    'Geography.Cities'    'Assistance.Contents systems'    'Culture.Visual arts'    'History_And_Society.Business and economics'    'History_And_Society.Military and warfare'    'STEM.Physics'    'STEM.Space'    'STEM.Biology'    'Culture.Sports'    'Culture.Broadcasting'    'Culture.Performing arts'    'STEM.Meteorology'    'Geography.Oceania'
		------  -------------------  -------------------------------------------  -----------------------  --------------------------  -------------  --------------------------  --------------------  --------------------  -----------------------  -----------------  -------------------------  --------------------  --------------------  -----------------------------------------------  --------------------------------------  ----------------------------------------------  ----------------  ----------------------------  ----------------  ------------------  --------------------  ---------------------------------  -----------------------------------  ------------------------------  ----------------------------  ------------------  -----------------------------------  -----------------------------  ------------------------  -----------------  --------------------  -------------------------------  -----------------------  ----------------------------------------------  --------------------------------------------  ----------------  --------------  ----------------  ------------------  ------------------------  ---------------------------  --------------------  ---------------------
		sample                0.045                                        0.083                    0.284                       0.027          0.026                        0.06                 0.017                 0.004                    0.026              0.024                      0.065                 0.182                 0.025                                            0.046                                   0.043                                           0.001             0.024                         0.022             0.025               0.025                 0.024                              0.031                                0.045                           0.023                         0.024               0.029                                0.233                          0.027                     0.044              0.023                 0.009                            0.023                    0.054                                           0.072                                         0.046             0.028           0.025             0.037               0.058                     0.033                         0.05                 0.021                  0.048
	match_rate (micro=0.082, macro=0.033):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.016
		Geography.Oceania                            0.032
		History_And_Society.Transportation           0.033
		STEM.Space                                   0.022
		Culture.Broadcasting                         0.023
		STEM.Technology                              0.023
		STEM.Physics                                 0.019
		Culture.Entertainment                        0.049
		History_And_Society.Military and warfare     0.033
		Assistance.Article improvement and grading   0.011
		STEM.Meteorology                             0.016
		STEM.Biology                                 0.024
		Culture.Performing arts                      0.044
		STEM.Information science                     0.015
		History_And_Society.Politics and government  0.024
		Culture.Arts                                 0.019
		Geography.Landforms                          0.022
		History_And_Society.Education                0.022
		Geography.Bodies of water                    0.022
		Culture.Food and drink                       0.021
		Culture.Crafts and hobbies                   0.014
		Culture.Language and literature              0.197
		History_And_Society.History and society      0.023
		Geography.Countries                          0.218
		Geography.Maps                               0.017
		Culture.Internet culture                     0.013
		STEM.Geosciences                             0.016
		Culture.Sports                               0.052
		STEM.Engineering                             0.012
		STEM.Mathematics                             0.012
		STEM.Science                                 0.008
		Culture.Media                                0.01
		Assistance.Files                             0.002
		Assistance.Contents systems                  0.01
		History_And_Society.Business and economics   0.045
		STEM.Medicine                                0.016
		Culture.Plastic arts                         0.03
		STEM.Time                                    0.02
		Geography.Europe                             0.137
		STEM.Chemistry                               0.019
		Geography.Cities                             0.008
		Culture.Philosophy and religion              0.025
		Culture.Visual arts                          0.036
		-------------------------------------------  -----
	filter_rate (micro=0.918, macro=0.967):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.984
		Geography.Oceania                            0.968
		History_And_Society.Transportation           0.967
		STEM.Space                                   0.978
		Culture.Broadcasting                         0.977
		STEM.Technology                              0.977
		STEM.Physics                                 0.981
		Culture.Entertainment                        0.951
		History_And_Society.Military and warfare     0.967
		Assistance.Article improvement and grading   0.989
		STEM.Meteorology                             0.984
		STEM.Biology                                 0.976
		Culture.Performing arts                      0.956
		STEM.Information science                     0.985
		History_And_Society.Politics and government  0.976
		Culture.Arts                                 0.981
		Geography.Landforms                          0.978
		History_And_Society.Education                0.978
		Geography.Bodies of water                    0.978
		Culture.Food and drink                       0.979
		Culture.Crafts and hobbies                   0.986
		Culture.Language and literature              0.803
		History_And_Society.History and society      0.977
		Geography.Countries                          0.782
		Geography.Maps                               0.983
		Culture.Internet culture                     0.987
		STEM.Geosciences                             0.984
		Culture.Sports                               0.948
		STEM.Engineering                             0.988
		STEM.Mathematics                             0.988
		STEM.Science                                 0.992
		Culture.Media                                0.99
		Assistance.Files                             0.998
		Assistance.Contents systems                  0.99
		History_And_Society.Business and economics   0.955
		STEM.Medicine                                0.984
		Culture.Plastic arts                         0.97
		STEM.Time                                    0.98
		Geography.Europe                             0.863
		STEM.Chemistry                               0.981
		Geography.Cities                             0.992
		Culture.Philosophy and religion              0.975
		Culture.Visual arts                          0.964
		-------------------------------------------  -----
	recall (micro=0.575, macro=0.551):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.225
		Geography.Oceania                            0.612
		History_And_Society.Transportation           0.676
		STEM.Space                                   0.82
		Culture.Broadcasting                         0.552
		STEM.Technology                              0.345
		STEM.Physics                                 0.525
		Culture.Entertainment                        0.65
		History_And_Society.Military and warfare     0.624
		Assistance.Article improvement and grading   0.303
		STEM.Meteorology                             0.759
		STEM.Biology                                 0.564
		Culture.Performing arts                      0.795
		STEM.Information science                     0.573
		History_And_Society.Politics and government  0.376
		Culture.Arts                                 0.73
		Geography.Landforms                          0.795
		History_And_Society.Education                0.606
		Geography.Bodies of water                    0.777
		Culture.Food and drink                       0.698
		Culture.Crafts and hobbies                   0.568
		Culture.Language and literature              0.726
		History_And_Society.History and society      0.201
		Geography.Countries                          0.595
		Geography.Maps                               0.574
		Culture.Internet culture                     0.5
		STEM.Geosciences                             0.596
		Culture.Sports                               0.824
		STEM.Engineering                             0.363
		STEM.Mathematics                             0.647
		STEM.Science                                 0.254
		Culture.Media                                0.286
		Assistance.Files                             0.069
		Assistance.Contents systems                  0.349
		History_And_Society.Business and economics   0.493
		STEM.Medicine                                0.557
		Culture.Plastic arts                         0.572
		STEM.Time                                    0.693
		Geography.Europe                             0.587
		STEM.Chemistry                               0.63
		Geography.Cities                             0.62
		Culture.Philosophy and religion              0.432
		Culture.Visual arts                          0.555
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.993):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.997
		Geography.Oceania                            0.998
		History_And_Society.Transportation           0.996
		STEM.Space                                   0.999
		Culture.Broadcasting                         0.995
		STEM.Technology                              0.992
		STEM.Physics                                 0.995
		Culture.Entertainment                        0.993
		History_And_Society.Military and warfare     0.995
		Assistance.Article improvement and grading   0.989
		STEM.Meteorology                             0.999
		STEM.Biology                                 0.997
		Culture.Performing arts                      0.995
		STEM.Information science                     0.998
		History_And_Society.Politics and government  0.993
		Culture.Arts                                 0.999
		Geography.Landforms                          0.998
		History_And_Society.Education                0.997
		Geography.Bodies of water                    0.998
		Culture.Food and drink                       0.998
		Culture.Crafts and hobbies                   0.999
		Culture.Language and literature              0.964
		History_And_Society.History and society      0.993
		Geography.Countries                          0.931
		Geography.Maps                               0.999
		Culture.Internet culture                     0.997
		STEM.Geosciences                             0.998
		Culture.Sports                               0.995
		STEM.Engineering                             0.997
		STEM.Mathematics                             0.999
		STEM.Science                                 0.998
		Culture.Media                                0.997
		Assistance.Files                             0.998
		Assistance.Contents systems                  0.998
		History_And_Society.Business and economics   0.99
		STEM.Medicine                                0.997
		Culture.Plastic arts                         0.995
		STEM.Time                                    0.999
		Geography.Europe                             0.963
		STEM.Chemistry                               0.997
		Geography.Cities                             0.998
		Culture.Philosophy and religion              0.995
		Culture.Visual arts                          0.993
		-------------------------------------------  -----
	precision (micro=0.827, macro=0.811):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.827
		Geography.Oceania                            0.925
		History_And_Society.Transportation           0.88
		STEM.Space                                   0.95
		Culture.Broadcasting                         0.798
		STEM.Technology                              0.685
		STEM.Physics                                 0.772
		Culture.Entertainment                        0.865
		History_And_Society.Military and warfare     0.864
		Assistance.Article improvement and grading   0.021
		STEM.Meteorology                             0.959
		STEM.Biology                                 0.87
		Culture.Performing arts                      0.894
		STEM.Information science                     0.903
		History_And_Society.Politics and government  0.736
		Culture.Arts                                 0.929
		Geography.Landforms                          0.926
		History_And_Society.Education                0.864
		Geography.Bodies of water                    0.929
		Culture.Food and drink                       0.905
		Culture.Crafts and hobbies                   0.94
		Culture.Language and literature              0.858
		History_And_Society.History and society      0.735
		Geography.Countries                          0.775
		Geography.Maps                               0.946
		Culture.Internet culture                     0.807
		STEM.Geosciences                             0.895
		Culture.Sports                               0.914
		STEM.Engineering                             0.759
		STEM.Mathematics                             0.912
		STEM.Science                                 0.784
		Culture.Media                                0.703
		Assistance.Files                             0.151
		Assistance.Contents systems                  0.817
		History_And_Society.Business and economics   0.792
		STEM.Medicine                                0.812
		Culture.Plastic arts                         0.836
		STEM.Time                                    0.935
		Geography.Europe                             0.781
		STEM.Chemistry                               0.824
		Geography.Cities                             0.778
		Culture.Philosophy and religion              0.79
		Culture.Visual arts                          0.825
		-------------------------------------------  -----
	!precision (micro=0.949, macro=0.978):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.953
		Geography.Oceania                            0.981
		History_And_Society.Transportation           0.985
		STEM.Space                                   0.995
		Culture.Broadcasting                         0.985
		STEM.Technology                              0.97
		STEM.Physics                                 0.986
		Culture.Entertainment                        0.976
		History_And_Society.Military and warfare     0.982
		Assistance.Article improvement and grading   0.999
		STEM.Meteorology                             0.995
		STEM.Biology                                 0.983
		Culture.Performing arts                      0.989
		STEM.Information science                     0.989
		History_And_Society.Politics and government  0.97
		Culture.Arts                                 0.993
		Geography.Landforms                          0.995
		History_And_Society.Education                0.987
		Geography.Bodies of water                    0.994
		Culture.Food and drink                       0.992
		Culture.Crafts and hobbies                   0.99
		Culture.Language and literature              0.92
		History_And_Society.History and society      0.932
		Geography.Countries                          0.853
		Geography.Maps                               0.988
		Culture.Internet culture                     0.989
		STEM.Geosciences                             0.99
		Culture.Sports                               0.989
		STEM.Engineering                             0.984
		STEM.Mathematics                             0.994
		STEM.Science                                 0.981
		Culture.Media                                0.983
		Assistance.Files                             0.996
		Assistance.Contents systems                  0.985
		History_And_Society.Business and economics   0.962
		STEM.Medicine                                0.99
		Culture.Plastic arts                         0.981
		STEM.Time                                    0.992
		Geography.Europe                             0.913
		STEM.Chemistry                               0.991
		Geography.Cities                             0.996
		Culture.Philosophy and religion              0.974
		Culture.Visual arts                          0.975
		-------------------------------------------  -----
	f1 (micro=0.668, macro=0.643):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.353
		Geography.Oceania                            0.736
		History_And_Society.Transportation           0.765
		STEM.Space                                   0.88
		Culture.Broadcasting                         0.652
		STEM.Technology                              0.459
		STEM.Physics                                 0.625
		Culture.Entertainment                        0.742
		History_And_Society.Military and warfare     0.724
		Assistance.Article improvement and grading   0.04
		STEM.Meteorology                             0.847
		STEM.Biology                                 0.684
		Culture.Performing arts                      0.842
		STEM.Information science                     0.701
		History_And_Society.Politics and government  0.497
		Culture.Arts                                 0.818
		Geography.Landforms                          0.856
		History_And_Society.Education                0.712
		Geography.Bodies of water                    0.846
		Culture.Food and drink                       0.788
		Culture.Crafts and hobbies                   0.708
		Culture.Language and literature              0.787
		History_And_Society.History and society      0.316
		Geography.Countries                          0.673
		Geography.Maps                               0.715
		Culture.Internet culture                     0.617
		STEM.Geosciences                             0.715
		Culture.Sports                               0.867
		STEM.Engineering                             0.491
		STEM.Mathematics                             0.757
		STEM.Science                                 0.384
		Culture.Media                                0.407
		Assistance.Files                             0.094
		Assistance.Contents systems                  0.489
		History_And_Society.Business and economics   0.608
		STEM.Medicine                                0.661
		Culture.Plastic arts                         0.679
		STEM.Time                                    0.796
		Geography.Europe                             0.67
		STEM.Chemistry                               0.714
		Geography.Cities                             0.69
		Culture.Philosophy and religion              0.559
		Culture.Visual arts                          0.663
		-------------------------------------------  -----
	!f1 (micro=0.964, macro=0.985):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.974
		Geography.Oceania                            0.989
		History_And_Society.Transportation           0.991
		STEM.Space                                   0.997
		Culture.Broadcasting                         0.99
		STEM.Technology                              0.981
		STEM.Physics                                 0.991
		Culture.Entertainment                        0.984
		History_And_Society.Military and warfare     0.989
		Assistance.Article improvement and grading   0.994
		STEM.Meteorology                             0.997
		STEM.Biology                                 0.99
		Culture.Performing arts                      0.992
		STEM.Information science                     0.994
		History_And_Society.Politics and government  0.982
		Culture.Arts                                 0.996
		Geography.Landforms                          0.996
		History_And_Society.Education                0.992
		Geography.Bodies of water                    0.996
		Culture.Food and drink                       0.995
		Culture.Crafts and hobbies                   0.994
		Culture.Language and literature              0.942
		History_And_Society.History and society      0.962
		Geography.Countries                          0.89
		Geography.Maps                               0.993
		Culture.Internet culture                     0.993
		STEM.Geosciences                             0.994
		Culture.Sports                               0.992
		STEM.Engineering                             0.99
		STEM.Mathematics                             0.996
		STEM.Science                                 0.989
		Culture.Media                                0.99
		Assistance.Files                             0.997
		Assistance.Contents systems                  0.991
		History_And_Society.Business and economics   0.976
		STEM.Medicine                                0.993
		Culture.Plastic arts                         0.988
		STEM.Time                                    0.995
		Geography.Europe                             0.938
		STEM.Chemistry                               0.994
		Geography.Cities                             0.997
		Culture.Philosophy and religion              0.984
		Culture.Visual arts                          0.984
		-------------------------------------------  -----
	accuracy (micro=0.941, macro=0.974):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.951
		Geography.Oceania                            0.979
		History_And_Society.Transportation           0.982
		STEM.Space                                   0.994
		Culture.Broadcasting                         0.981
		STEM.Technology                              0.963
		STEM.Physics                                 0.982
		Culture.Entertainment                        0.97
		History_And_Society.Military and warfare     0.978
		Assistance.Article improvement and grading   0.988
		STEM.Meteorology                             0.994
		STEM.Biology                                 0.981
		Culture.Performing arts                      0.985
		STEM.Information science                     0.988
		History_And_Society.Politics and government  0.965
		Culture.Arts                                 0.992
		Geography.Landforms                          0.993
		History_And_Society.Education                0.985
		Geography.Bodies of water                    0.992
		Culture.Food and drink                       0.99
		Culture.Crafts and hobbies                   0.989
		Culture.Language and literature              0.908
		History_And_Society.History and society      0.928
		Geography.Countries                          0.836
		Geography.Maps                               0.987
		Culture.Internet culture                     0.987
		STEM.Geosciences                             0.989
		Culture.Sports                               0.985
		STEM.Engineering                             0.981
		STEM.Mathematics                             0.993
		STEM.Science                                 0.979
		Culture.Media                                0.98
		Assistance.Files                             0.994
		Assistance.Contents systems                  0.983
		History_And_Society.Business and economics   0.954
		STEM.Medicine                                0.987
		Culture.Plastic arts                         0.976
		STEM.Time                                    0.991
		Geography.Europe                             0.895
		STEM.Chemistry                               0.987
		Geography.Cities                             0.995
		Culture.Philosophy and religion              0.969
		Culture.Visual arts                          0.97
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.007):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.003
		Geography.Oceania                            0.002
		History_And_Society.Transportation           0.004
		STEM.Space                                   0.001
		Culture.Broadcasting                         0.005
		STEM.Technology                              0.008
		STEM.Physics                                 0.005
		Culture.Entertainment                        0.007
		History_And_Society.Military and warfare     0.005
		Assistance.Article improvement and grading   0.011
		STEM.Meteorology                             0.001
		STEM.Biology                                 0.003
		Culture.Performing arts                      0.005
		STEM.Information science                     0.002
		History_And_Society.Politics and government  0.007
		Culture.Arts                                 0.001
		Geography.Landforms                          0.002
		History_And_Society.Education                0.003
		Geography.Bodies of water                    0.002
		Culture.Food and drink                       0.002
		Culture.Crafts and hobbies                   0.001
		Culture.Language and literature              0.036
		History_And_Society.History and society      0.007
		Geography.Countries                          0.069
		Geography.Maps                               0.001
		Culture.Internet culture                     0.003
		STEM.Geosciences                             0.002
		Culture.Sports                               0.005
		STEM.Engineering                             0.003
		STEM.Mathematics                             0.001
		STEM.Science                                 0.002
		Culture.Media                                0.003
		Assistance.Files                             0.002
		Assistance.Contents systems                  0.002
		History_And_Society.Business and economics   0.01
		STEM.Medicine                                0.003
		Culture.Plastic arts                         0.005
		STEM.Time                                    0.001
		Geography.Europe                             0.037
		STEM.Chemistry                               0.003
		Geography.Cities                             0.002
		Culture.Philosophy and religion              0.005
		Culture.Visual arts                          0.007
		-------------------------------------------  -----
	roc_auc (micro=0.943, macro=0.947):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.836
		Geography.Oceania                            0.965
		History_And_Society.Transportation           0.976
		STEM.Space                                   0.988
		Culture.Broadcasting                         0.972
		STEM.Technology                              0.941
		STEM.Physics                                 0.977
		Culture.Entertainment                        0.972
		History_And_Society.Military and warfare     0.967
		Assistance.Article improvement and grading   0.676
		STEM.Meteorology                             0.987
		STEM.Biology                                 0.959
		Culture.Performing arts                      0.986
		STEM.Information science                     0.969
		History_And_Society.Politics and government  0.941
		Culture.Arts                                 0.984
		Geography.Landforms                          0.988
		History_And_Society.Education                0.968
		Geography.Bodies of water                    0.987
		Culture.Food and drink                       0.975
		Culture.Crafts and hobbies                   0.964
		Culture.Language and literature              0.951
		History_And_Society.History and society      0.87
		Geography.Countries                          0.893
		Geography.Maps                               0.969
		Culture.Internet culture                     0.969
		STEM.Geosciences                             0.971
		Culture.Sports                               0.976
		STEM.Engineering                             0.953
		STEM.Mathematics                             0.979
		STEM.Science                                 0.934
		Culture.Media                                0.946
		Assistance.Files                             0.761
		Assistance.Contents systems                  0.951
		History_And_Society.Business and economics   0.948
		STEM.Medicine                                0.972
		Culture.Plastic arts                         0.966
		STEM.Time                                    0.974
		Geography.Europe                             0.929
		STEM.Chemistry                               0.98
		Geography.Cities                             0.972
		Culture.Philosophy and religion              0.936
		Culture.Visual arts                          0.968
		-------------------------------------------  -----
	pr_auc (micro=0.76, macro=0.723):
		-------------------------------------------  -----
		Assistance.Maintenance                       0.45
		Geography.Oceania                            0.841
		History_And_Society.Transportation           0.859
		STEM.Space                                   0.939
		Culture.Broadcasting                         0.733
		STEM.Technology                              0.547
		STEM.Physics                                 0.714
		Culture.Entertainment                        0.846
		History_And_Society.Military and warfare     0.811
		Assistance.Article improvement and grading   0.014
		STEM.Meteorology                             0.915
		STEM.Biology                                 0.75
		Culture.Performing arts                      0.92
		STEM.Information science                     0.792
		History_And_Society.Politics and government  0.595
		Culture.Arts                                 0.907
		Geography.Landforms                          0.928
		History_And_Society.Education                0.772
		Geography.Bodies of water                    0.92
		Culture.Food and drink                       0.855
		Culture.Crafts and hobbies                   0.807
		Culture.Language and literature              0.875
		History_And_Society.History and society      0.48
		Geography.Countries                          0.777
		Geography.Maps                               0.828
		Culture.Internet culture                     0.685
		STEM.Geosciences                             0.796
		Culture.Sports                               0.906
		STEM.Engineering                             0.588
		STEM.Mathematics                             0.846
		STEM.Science                                 0.498
		Culture.Media                                0.497
		Assistance.Files                             0.033
		Assistance.Contents systems                  0.597
		History_And_Society.Business and economics   0.708
		STEM.Medicine                                0.746
		Culture.Plastic arts                         0.781
		STEM.Time                                    0.86
		Geography.Europe                             0.759
		STEM.Chemistry                               0.797
		Geography.Cities                             0.734
		Culture.Philosophy and religion              0.628
		Culture.Visual arts                          0.773
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'History_And_Society.Military and warfare': {'type': 'number'}, 'Assistance.Maintenance': {'type': 'number'}, 'Geography.Oceania': {'type': 'number'}, 'History_And_Society.Transportation': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Broadcasting': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Entertainment': {'type': 'number'}, 'STEM.Medicine': {'type': 'number'}, 'Culture.Plastic arts': {'type': 'number'}, 'STEM.Meteorology': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Information science': {'type': 'number'}, 'History_And_Society.Politics and government': {'type': 'number'}, 'Culture.Arts': {'type': 'number'}, 'Geography.Landforms': {'type': 'number'}, 'History_And_Society.Education': {'type': 'number'}, 'Geography.Bodies of water': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Crafts and hobbies': {'type': 'number'}, 'Culture.Language and literature': {'type': 'number'}, 'History_And_Society.History and society': {'type': 'number'}, 'Geography.Countries': {'type': 'number'}, 'Geography.Maps': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Geosciences': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Science': {'type': 'number'}, 'Culture.Media': {'type': 'number'}, 'Assistance.Files': {'type': 'number'}, 'Assistance.Contents systems': {'type': 'number'}, 'History_And_Society.Business and economics': {'type': 'number'}, 'Assistance.Article improvement and grading': {'type': 'number'}, 'STEM.Time': {'type': 'number'}, 'Geography.Europe': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Cities': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Visual arts': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object'}

