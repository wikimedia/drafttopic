Model Information:
	 - type: GradientBoosting
	 - version: 0.1
	 - params: {'max_leaf_nodes': None, 'population_rates': None, 'min_samples_leaf': 1, 'random_state': None, 'label_weights': {}, 'max_depth': 5, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'criterion': 'friedman_mse', 'scale': False, 'n_estimators': 150, 'learning_rate': 0.1, 'subsample': 1.0, 'verbose': 0, 'min_impurity_decrease': 0.0, 'presort': 'auto', 'min_impurity_split': None, 'max_features': 'log2', 'init': None, 'center': False, 'multilabel': True, 'min_samples_split': 2, 'labels': ['Geography.Oceania', 'STEM.Mathematics', 'STEM.Science', 'STEM.Meteorology', 'Culture.Sports', 'Culture.Performing arts', 'Culture.Entertainment', 'Assistance.Article improvement and grading', 'Culture.Language and literature', 'Culture.Visual arts', 'STEM.Biology', 'History_And_Society.Business and economics', 'Assistance.Files', 'History_And_Society.History and society', 'STEM.Medicine', 'Culture.Crafts and hobbies', 'STEM.Geosciences', 'Culture.Food and drink', 'History_And_Society.Transportation', 'Geography.Cities', 'Geography.Landforms', 'Assistance.Maintenance', 'STEM.Information science', 'STEM.Time', 'Geography.Europe', 'STEM.Engineering', 'Culture.Media', 'STEM.Technology', 'STEM.Space', 'History_And_Society.Education', 'Geography.Countries', 'History_And_Society.Military and warfare', 'Culture.Plastic arts', 'STEM.Physics', 'History_And_Society.Politics and government', 'STEM.Chemistry', 'Culture.Broadcasting', 'Geography.Maps', 'Culture.Arts', 'Culture.Internet culture', 'Geography.Bodies of water', 'Assistance.Contents systems', 'Culture.Philosophy and religion']}
	Environment:
	 - revscoring_version: '2.3.0'
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
	counts (n=83530):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Geography.Oceania'                             3978  -->   2427  1551   196  79356
			'STEM.Mathematics'                              1440  -->    925   515   105  81985
			'STEM.Science'                                  2118  -->    533  1585   154  81258
			'STEM.Meteorology'                              1728  -->   1335   393    70  81732
			'Culture.Sports'                                4809  -->   3972   837   370  78351
			'Culture.Performing arts'                       4154  -->   3262   892   389  78987
			'Culture.Entertainment'                         5464  -->   3569  1895   573  77493
			'Assistance.Article improvement and grading'      66  -->     25    41   117  83347
			'Culture.Language and literature'              19460  -->  14182  5278  2406  61664
			'Culture.Visual arts'                           4529  -->   2543  1986   540  78461
			'STEM.Biology'                                  3094  -->   1757  1337   277  80159
			'History_And_Society.Business and economics'    5999  -->   2989  3010   792  76739
			'Assistance.Files'                               350  -->     24   326   129  83051
			'History_And_Society.History and society'       6937  -->   1350  5587   509  76084
			'STEM.Medicine'                                 1942  -->   1103   839   258  81330
			'Culture.Crafts and hobbies'                    1950  -->   1102   848    63  81517
			'STEM.Geosciences'                              1970  -->   1178   792   127  81433
			'Culture.Food and drink'                        2243  -->   1545   698   153  81134
			'History_And_Society.Transportation'            3630  -->   2471  1159   336  79564
			'Geography.Cities'                               786  -->    486   300   140  82604
			'Geography.Landforms'                           2133  -->   1708   425   128  81269
			'Assistance.Maintenance'                        4982  -->   1078  3904   241  78307
			'STEM.Information science'                      2024  -->   1178   846   109  81397
			'STEM.Time'                                     2208  -->   1522   686   109  81213
			'Geography.Europe'                             15169  -->   8859  6310  2564  65797
			'STEM.Engineering'                              2115  -->    729  1386   260  81155
			'Culture.Media'                                 2021  -->    593  1428   240  81269
			'STEM.Technology'                               3777  -->   1315  2462   589  79164
			'STEM.Space'                                    2105  -->   1732   373    95  81330
			'History_And_Society.Education'                 2605  -->   1610   995   237  80688
			'Geography.Countries'                          23775  -->  14212  9563  4093  55662
			'History_And_Society.Military and warfare'      3874  -->   2424  1450   393  79263
			'Culture.Plastic arts'                          3676  -->   2101  1575   394  79460
			'STEM.Physics'                                  2365  -->   1274  1091   359  80806
			'History_And_Society.Politics and government'   3869  -->   1450  2419   483  79178
			'STEM.Chemistry'                                2074  -->   1275   799   287  81169
			'Culture.Broadcasting'                          2757  -->   1566  1191   380  80393
			'Geography.Maps'                                2405  -->   1374  1031    81  81044
			'Culture.Arts'                                  1984  -->   1466   518    94  81452
			'Culture.Internet culture'                      1811  -->    926   885   229  81490
			'Geography.Bodies of water'                     2225  -->   1716   509   154  81151
			'Assistance.Contents systems'                   1932  -->    666  1266   163  81435
			'Culture.Philosophy and religion'               3793  -->   1687  2106   456  79281
	rates:
		          'Geography.Oceania'    'STEM.Mathematics'    'STEM.Science'    'STEM.Meteorology'    'Culture.Sports'    'Culture.Performing arts'    'Culture.Entertainment'    'Assistance.Article improvement and grading'    'Culture.Language and literature'    'Culture.Visual arts'    'STEM.Biology'    'History_And_Society.Business and economics'    'Assistance.Files'    'History_And_Society.History and society'    'STEM.Medicine'    'Culture.Crafts and hobbies'    'STEM.Geosciences'    'Culture.Food and drink'    'History_And_Society.Transportation'    'Geography.Cities'    'Geography.Landforms'    'Assistance.Maintenance'    'STEM.Information science'    'STEM.Time'    'Geography.Europe'    'STEM.Engineering'    'Culture.Media'    'STEM.Technology'    'STEM.Space'    'History_And_Society.Education'    'Geography.Countries'    'History_And_Society.Military and warfare'    'Culture.Plastic arts'    'STEM.Physics'    'History_And_Society.Politics and government'    'STEM.Chemistry'    'Culture.Broadcasting'    'Geography.Maps'    'Culture.Arts'    'Culture.Internet culture'    'Geography.Bodies of water'    'Assistance.Contents systems'    'Culture.Philosophy and religion'
		------  ---------------------  --------------------  ----------------  --------------------  ------------------  ---------------------------  -------------------------  ----------------------------------------------  -----------------------------------  -----------------------  ----------------  ----------------------------------------------  --------------------  -------------------------------------------  -----------------  ------------------------------  --------------------  --------------------------  --------------------------------------  --------------------  -----------------------  --------------------------  ----------------------------  -------------  --------------------  --------------------  -----------------  -------------------  --------------  ---------------------------------  -----------------------  --------------------------------------------  ------------------------  ----------------  -----------------------------------------------  ------------------  ------------------------  ------------------  ----------------  ----------------------------  -----------------------------  -------------------------------  -----------------------------------
		sample                  0.048                 0.017             0.025                 0.021               0.058                         0.05                      0.065                                           0.001                                0.233                    0.054             0.037                                           0.072                 0.004                                        0.083              0.023                           0.023                 0.024                       0.027                                   0.043                 0.009                    0.026                        0.06                         0.024          0.026                 0.182                 0.025              0.024                0.045           0.025                              0.031                    0.285                                         0.046                     0.044             0.028                                            0.046               0.025                     0.033               0.029             0.024                         0.022                          0.027                            0.023                                0.045
	match_rate (micro=0.082, macro=0.033):
		-------------------------------------------  -----
		Culture.Sports                               0.052
		Culture.Visual arts                          0.037
		Culture.Food and drink                       0.02
		Geography.Oceania                            0.031
		Culture.Media                                0.01
		STEM.Space                                   0.022
		Geography.Landforms                          0.022
		Culture.Entertainment                        0.05
		Assistance.Files                             0.002
		Culture.Arts                                 0.019
		Culture.Philosophy and religion              0.026
		Geography.Bodies of water                    0.022
		STEM.Chemistry                               0.019
		Culture.Broadcasting                         0.023
		STEM.Time                                    0.02
		STEM.Information science                     0.015
		History_And_Society.Education                0.022
		STEM.Engineering                             0.012
		History_And_Society.Politics and government  0.023
		STEM.Geosciences                             0.016
		Geography.Maps                               0.017
		Geography.Cities                             0.007
		Culture.Crafts and hobbies                   0.014
		History_And_Society.Business and economics   0.045
		STEM.Technology                              0.023
		STEM.Meteorology                             0.017
		STEM.Physics                                 0.02
		Culture.Internet culture                     0.014
		Assistance.Maintenance                       0.016
		History_And_Society.Transportation           0.034
		Geography.Europe                             0.137
		Assistance.Article improvement and grading   0.002
		History_And_Society.Military and warfare     0.034
		Culture.Performing arts                      0.044
		STEM.Science                                 0.008
		Geography.Countries                          0.219
		STEM.Medicine                                0.016
		Assistance.Contents systems                  0.01
		STEM.Biology                                 0.024
		Culture.Plastic arts                         0.03
		STEM.Mathematics                             0.012
		Culture.Language and literature              0.199
		History_And_Society.History and society      0.022
		-------------------------------------------  -----
	filter_rate (micro=0.918, macro=0.967):
		-------------------------------------------  -----
		Culture.Sports                               0.948
		Culture.Visual arts                          0.963
		Culture.Food and drink                       0.98
		Geography.Oceania                            0.969
		Culture.Media                                0.99
		STEM.Space                                   0.978
		Geography.Landforms                          0.978
		Culture.Entertainment                        0.95
		Assistance.Files                             0.998
		Culture.Arts                                 0.981
		Culture.Philosophy and religion              0.974
		Geography.Bodies of water                    0.978
		STEM.Chemistry                               0.981
		Culture.Broadcasting                         0.977
		STEM.Time                                    0.98
		STEM.Information science                     0.985
		History_And_Society.Education                0.978
		STEM.Engineering                             0.988
		History_And_Society.Politics and government  0.977
		STEM.Geosciences                             0.984
		Geography.Maps                               0.983
		Geography.Cities                             0.993
		Culture.Crafts and hobbies                   0.986
		History_And_Society.Business and economics   0.955
		STEM.Technology                              0.977
		STEM.Meteorology                             0.983
		STEM.Physics                                 0.98
		Culture.Internet culture                     0.986
		Assistance.Maintenance                       0.984
		History_And_Society.Transportation           0.966
		Geography.Europe                             0.863
		Assistance.Article improvement and grading   0.998
		History_And_Society.Military and warfare     0.966
		Culture.Performing arts                      0.956
		STEM.Science                                 0.992
		Geography.Countries                          0.781
		STEM.Medicine                                0.984
		Assistance.Contents systems                  0.99
		STEM.Biology                                 0.976
		Culture.Plastic arts                         0.97
		STEM.Mathematics                             0.988
		Culture.Language and literature              0.801
		History_And_Society.History and society      0.978
		-------------------------------------------  -----
	recall (micro=0.576, macro=0.554):
		-------------------------------------------  -----
		Culture.Sports                               0.826
		Culture.Visual arts                          0.561
		Culture.Food and drink                       0.689
		Geography.Oceania                            0.61
		Culture.Media                                0.293
		STEM.Space                                   0.823
		Geography.Landforms                          0.801
		Culture.Entertainment                        0.653
		Assistance.Files                             0.069
		Culture.Arts                                 0.739
		Culture.Philosophy and religion              0.445
		Geography.Bodies of water                    0.771
		STEM.Chemistry                               0.615
		Culture.Broadcasting                         0.568
		STEM.Time                                    0.689
		STEM.Information science                     0.582
		History_And_Society.Education                0.618
		STEM.Engineering                             0.345
		History_And_Society.Politics and government  0.375
		STEM.Geosciences                             0.598
		Geography.Maps                               0.571
		Geography.Cities                             0.618
		Culture.Crafts and hobbies                   0.565
		History_And_Society.Business and economics   0.498
		STEM.Technology                              0.348
		STEM.Meteorology                             0.773
		STEM.Physics                                 0.539
		Culture.Internet culture                     0.511
		Assistance.Maintenance                       0.216
		History_And_Society.Transportation           0.681
		Geography.Europe                             0.584
		Assistance.Article improvement and grading   0.379
		History_And_Society.Military and warfare     0.626
		Culture.Performing arts                      0.785
		STEM.Science                                 0.252
		Geography.Countries                          0.598
		STEM.Medicine                                0.568
		Assistance.Contents systems                  0.345
		STEM.Biology                                 0.568
		Culture.Plastic arts                         0.572
		STEM.Mathematics                             0.642
		Culture.Language and literature              0.729
		History_And_Society.History and society      0.195
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.994):
		-------------------------------------------  -----
		Culture.Sports                               0.995
		Culture.Visual arts                          0.993
		Culture.Food and drink                       0.998
		Geography.Oceania                            0.998
		Culture.Media                                0.997
		STEM.Space                                   0.999
		Geography.Landforms                          0.998
		Culture.Entertainment                        0.993
		Assistance.Files                             0.998
		Culture.Arts                                 0.999
		Culture.Philosophy and religion              0.994
		Geography.Bodies of water                    0.998
		STEM.Chemistry                               0.996
		Culture.Broadcasting                         0.995
		STEM.Time                                    0.999
		STEM.Information science                     0.999
		History_And_Society.Education                0.997
		STEM.Engineering                             0.997
		History_And_Society.Politics and government  0.994
		STEM.Geosciences                             0.998
		Geography.Maps                               0.999
		Geography.Cities                             0.998
		Culture.Crafts and hobbies                   0.999
		History_And_Society.Business and economics   0.99
		STEM.Technology                              0.993
		STEM.Meteorology                             0.999
		STEM.Physics                                 0.996
		Culture.Internet culture                     0.997
		Assistance.Maintenance                       0.997
		History_And_Society.Transportation           0.996
		Geography.Europe                             0.962
		Assistance.Article improvement and grading   0.999
		History_And_Society.Military and warfare     0.995
		Culture.Performing arts                      0.995
		STEM.Science                                 0.998
		Geography.Countries                          0.932
		STEM.Medicine                                0.997
		Assistance.Contents systems                  0.998
		STEM.Biology                                 0.997
		Culture.Plastic arts                         0.995
		STEM.Mathematics                             0.999
		Culture.Language and literature              0.962
		History_And_Society.History and society      0.993
		-------------------------------------------  -----
	precision (micro=0.826, macro=0.814):
		-------------------------------------------  -----
		Culture.Sports                               0.915
		Culture.Visual arts                          0.825
		Culture.Food and drink                       0.91
		Geography.Oceania                            0.925
		Culture.Media                                0.712
		STEM.Space                                   0.948
		Geography.Landforms                          0.93
		Culture.Entertainment                        0.862
		Assistance.Files                             0.157
		Culture.Arts                                 0.94
		Culture.Philosophy and religion              0.787
		Geography.Bodies of water                    0.918
		STEM.Chemistry                               0.816
		Culture.Broadcasting                         0.805
		STEM.Time                                    0.933
		STEM.Information science                     0.915
		History_And_Society.Education                0.872
		STEM.Engineering                             0.737
		History_And_Society.Politics and government  0.75
		STEM.Geosciences                             0.903
		Geography.Maps                               0.944
		Geography.Cities                             0.776
		Culture.Crafts and hobbies                   0.946
		History_And_Society.Business and economics   0.791
		STEM.Technology                              0.691
		STEM.Meteorology                             0.95
		STEM.Physics                                 0.78
		Culture.Internet culture                     0.802
		Assistance.Maintenance                       0.817
		History_And_Society.Transportation           0.88
		Geography.Europe                             0.776
		Assistance.Article improvement and grading   0.176
		History_And_Society.Military and warfare     0.86
		Culture.Performing arts                      0.893
		STEM.Science                                 0.776
		Geography.Countries                          0.776
		STEM.Medicine                                0.81
		Assistance.Contents systems                  0.803
		STEM.Biology                                 0.864
		Culture.Plastic arts                         0.842
		STEM.Mathematics                             0.898
		Culture.Language and literature              0.855
		History_And_Society.History and society      0.726
		-------------------------------------------  -----
	!precision (micro=0.949, macro=0.978):
		-------------------------------------------  -----
		Culture.Sports                               0.989
		Culture.Visual arts                          0.975
		Culture.Food and drink                       0.991
		Geography.Oceania                            0.981
		Culture.Media                                0.983
		STEM.Space                                   0.995
		Geography.Landforms                          0.995
		Culture.Entertainment                        0.976
		Assistance.Files                             0.996
		Culture.Arts                                 0.994
		Culture.Philosophy and religion              0.974
		Geography.Bodies of water                    0.994
		STEM.Chemistry                               0.99
		Culture.Broadcasting                         0.985
		STEM.Time                                    0.992
		STEM.Information science                     0.99
		History_And_Society.Education                0.988
		STEM.Engineering                             0.983
		History_And_Society.Politics and government  0.97
		STEM.Geosciences                             0.99
		Geography.Maps                               0.987
		Geography.Cities                             0.996
		Culture.Crafts and hobbies                   0.99
		History_And_Society.Business and economics   0.962
		STEM.Technology                              0.97
		STEM.Meteorology                             0.995
		STEM.Physics                                 0.987
		Culture.Internet culture                     0.989
		Assistance.Maintenance                       0.953
		History_And_Society.Transportation           0.986
		Geography.Europe                             0.912
		Assistance.Article improvement and grading   1
		History_And_Society.Military and warfare     0.982
		Culture.Performing arts                      0.989
		STEM.Science                                 0.981
		Geography.Countries                          0.853
		STEM.Medicine                                0.99
		Assistance.Contents systems                  0.985
		STEM.Biology                                 0.984
		Culture.Plastic arts                         0.981
		STEM.Mathematics                             0.994
		Culture.Language and literature              0.921
		History_And_Society.History and society      0.932
		-------------------------------------------  -----
	f1 (micro=0.668, macro=0.648):
		-------------------------------------------  -----
		Culture.Sports                               0.868
		Culture.Visual arts                          0.668
		Culture.Food and drink                       0.784
		Geography.Oceania                            0.735
		Culture.Media                                0.416
		STEM.Space                                   0.881
		Geography.Landforms                          0.861
		Culture.Entertainment                        0.743
		Assistance.Files                             0.095
		Culture.Arts                                 0.827
		Culture.Philosophy and religion              0.568
		Geography.Bodies of water                    0.838
		STEM.Chemistry                               0.701
		Culture.Broadcasting                         0.666
		STEM.Time                                    0.793
		STEM.Information science                     0.712
		History_And_Society.Education                0.723
		STEM.Engineering                             0.47
		History_And_Society.Politics and government  0.5
		STEM.Geosciences                             0.719
		Geography.Maps                               0.712
		Geography.Cities                             0.688
		Culture.Crafts and hobbies                   0.708
		History_And_Society.Business and economics   0.611
		STEM.Technology                              0.463
		STEM.Meteorology                             0.852
		STEM.Physics                                 0.637
		Culture.Internet culture                     0.624
		Assistance.Maintenance                       0.342
		History_And_Society.Transportation           0.768
		Geography.Europe                             0.666
		Assistance.Article improvement and grading   0.24
		History_And_Society.Military and warfare     0.725
		Culture.Performing arts                      0.836
		STEM.Science                                 0.38
		Geography.Countries                          0.675
		STEM.Medicine                                0.668
		Assistance.Contents systems                  0.482
		STEM.Biology                                 0.685
		Culture.Plastic arts                         0.681
		STEM.Mathematics                             0.749
		Culture.Language and literature              0.787
		History_And_Society.History and society      0.307
		-------------------------------------------  -----
	!f1 (micro=0.964, macro=0.986):
		-------------------------------------------  -----
		Culture.Sports                               0.992
		Culture.Visual arts                          0.984
		Culture.Food and drink                       0.995
		Geography.Oceania                            0.989
		Culture.Media                                0.99
		STEM.Space                                   0.997
		Geography.Landforms                          0.997
		Culture.Entertainment                        0.984
		Assistance.Files                             0.997
		Culture.Arts                                 0.996
		Culture.Philosophy and religion              0.984
		Geography.Bodies of water                    0.996
		STEM.Chemistry                               0.993
		Culture.Broadcasting                         0.99
		STEM.Time                                    0.995
		STEM.Information science                     0.994
		History_And_Society.Education                0.992
		STEM.Engineering                             0.99
		History_And_Society.Politics and government  0.982
		STEM.Geosciences                             0.994
		Geography.Maps                               0.993
		Geography.Cities                             0.997
		Culture.Crafts and hobbies                   0.994
		History_And_Society.Business and economics   0.976
		STEM.Technology                              0.981
		STEM.Meteorology                             0.997
		STEM.Physics                                 0.991
		Culture.Internet culture                     0.993
		Assistance.Maintenance                       0.974
		History_And_Society.Transportation           0.991
		Geography.Europe                             0.937
		Assistance.Article improvement and grading   0.999
		History_And_Society.Military and warfare     0.989
		Culture.Performing arts                      0.992
		STEM.Science                                 0.989
		Geography.Countries                          0.891
		STEM.Medicine                                0.993
		Assistance.Contents systems                  0.991
		STEM.Biology                                 0.99
		Culture.Plastic arts                         0.988
		STEM.Mathematics                             0.996
		Culture.Language and literature              0.941
		History_And_Society.History and society      0.961
		-------------------------------------------  -----
	accuracy (micro=0.941, macro=0.974):
		-------------------------------------------  -----
		Culture.Sports                               0.986
		Culture.Visual arts                          0.97
		Culture.Food and drink                       0.99
		Geography.Oceania                            0.979
		Culture.Media                                0.98
		STEM.Space                                   0.994
		Geography.Landforms                          0.993
		Culture.Entertainment                        0.97
		Assistance.Files                             0.995
		Culture.Arts                                 0.993
		Culture.Philosophy and religion              0.969
		Geography.Bodies of water                    0.992
		STEM.Chemistry                               0.987
		Culture.Broadcasting                         0.981
		STEM.Time                                    0.99
		STEM.Information science                     0.989
		History_And_Society.Education                0.985
		STEM.Engineering                             0.98
		History_And_Society.Politics and government  0.965
		STEM.Geosciences                             0.989
		Geography.Maps                               0.987
		Geography.Cities                             0.995
		Culture.Crafts and hobbies                   0.989
		History_And_Society.Business and economics   0.954
		STEM.Technology                              0.963
		STEM.Meteorology                             0.994
		STEM.Physics                                 0.983
		Culture.Internet culture                     0.987
		Assistance.Maintenance                       0.95
		History_And_Society.Transportation           0.982
		Geography.Europe                             0.894
		Assistance.Article improvement and grading   0.998
		History_And_Society.Military and warfare     0.978
		Culture.Performing arts                      0.985
		STEM.Science                                 0.979
		Geography.Countries                          0.837
		STEM.Medicine                                0.987
		Assistance.Contents systems                  0.983
		STEM.Biology                                 0.981
		Culture.Plastic arts                         0.976
		STEM.Mathematics                             0.993
		Culture.Language and literature              0.908
		History_And_Society.History and society      0.927
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.006):
		-------------------------------------------  -----
		Culture.Sports                               0.005
		Culture.Visual arts                          0.007
		Culture.Food and drink                       0.002
		Geography.Oceania                            0.002
		Culture.Media                                0.003
		STEM.Space                                   0.001
		Geography.Landforms                          0.002
		Culture.Entertainment                        0.007
		Assistance.Files                             0.002
		Culture.Arts                                 0.001
		Culture.Philosophy and religion              0.006
		Geography.Bodies of water                    0.002
		STEM.Chemistry                               0.004
		Culture.Broadcasting                         0.005
		STEM.Time                                    0.001
		STEM.Information science                     0.001
		History_And_Society.Education                0.003
		STEM.Engineering                             0.003
		History_And_Society.Politics and government  0.006
		STEM.Geosciences                             0.002
		Geography.Maps                               0.001
		Geography.Cities                             0.002
		Culture.Crafts and hobbies                   0.001
		History_And_Society.Business and economics   0.01
		STEM.Technology                              0.007
		STEM.Meteorology                             0.001
		STEM.Physics                                 0.004
		Culture.Internet culture                     0.003
		Assistance.Maintenance                       0.003
		History_And_Society.Transportation           0.004
		Geography.Europe                             0.038
		Assistance.Article improvement and grading   0.001
		History_And_Society.Military and warfare     0.005
		Culture.Performing arts                      0.005
		STEM.Science                                 0.002
		Geography.Countries                          0.068
		STEM.Medicine                                0.003
		Assistance.Contents systems                  0.002
		STEM.Biology                                 0.003
		Culture.Plastic arts                         0.005
		STEM.Mathematics                             0.001
		Culture.Language and literature              0.038
		History_And_Society.History and society      0.007
		-------------------------------------------  -----
	roc_auc (micro=0.942, macro=0.949):
		-------------------------------------------  -----
		Culture.Sports                               0.976
		Culture.Visual arts                          0.969
		Culture.Food and drink                       0.975
		Geography.Oceania                            0.967
		Culture.Media                                0.949
		STEM.Space                                   0.987
		Geography.Landforms                          0.988
		Culture.Entertainment                        0.971
		Assistance.Files                             0.765
		Culture.Arts                                 0.985
		Culture.Philosophy and religion              0.935
		Geography.Bodies of water                    0.986
		STEM.Chemistry                               0.98
		Culture.Broadcasting                         0.971
		STEM.Time                                    0.971
		STEM.Information science                     0.97
		History_And_Society.Education                0.968
		STEM.Engineering                             0.954
		History_And_Society.Politics and government  0.941
		STEM.Geosciences                             0.971
		Geography.Maps                               0.969
		Geography.Cities                             0.968
		Culture.Crafts and hobbies                   0.963
		History_And_Society.Business and economics   0.948
		STEM.Technology                              0.942
		STEM.Meteorology                             0.986
		STEM.Physics                                 0.976
		Culture.Internet culture                     0.97
		Assistance.Maintenance                       0.835
		History_And_Society.Transportation           0.975
		Geography.Europe                             0.929
		Assistance.Article improvement and grading   0.754
		History_And_Society.Military and warfare     0.967
		Culture.Performing arts                      0.983
		STEM.Science                                 0.934
		Geography.Countries                          0.892
		STEM.Medicine                                0.974
		Assistance.Contents systems                  0.948
		STEM.Biology                                 0.958
		Culture.Plastic arts                         0.966
		STEM.Mathematics                             0.98
		Culture.Language and literature              0.95
		History_And_Society.History and society      0.87
		-------------------------------------------  -----
	pr_auc (micro=0.761, macro=0.726):
		-------------------------------------------  -----
		Culture.Sports                               0.902
		Culture.Visual arts                          0.773
		Culture.Food and drink                       0.853
		Geography.Oceania                            0.841
		Culture.Media                                0.504
		STEM.Space                                   0.938
		Geography.Landforms                          0.926
		Culture.Entertainment                        0.843
		Assistance.Files                             0.036
		Culture.Arts                                 0.908
		Culture.Philosophy and religion              0.621
		Geography.Bodies of water                    0.915
		STEM.Chemistry                               0.791
		Culture.Broadcasting                         0.729
		STEM.Time                                    0.855
		STEM.Information science                     0.797
		History_And_Society.Education                0.782
		STEM.Engineering                             0.585
		History_And_Society.Politics and government  0.607
		STEM.Geosciences                             0.797
		Geography.Maps                               0.832
		Geography.Cities                             0.728
		Culture.Crafts and hobbies                   0.809
		History_And_Society.Business and economics   0.708
		STEM.Technology                              0.548
		STEM.Meteorology                             0.92
		STEM.Physics                                 0.718
		Culture.Internet culture                     0.695
		Assistance.Maintenance                       0.46
		History_And_Society.Transportation           0.86
		Geography.Europe                             0.769
		Assistance.Article improvement and grading   0.095
		History_And_Society.Military and warfare     0.809
		Culture.Performing arts                      0.912
		STEM.Science                                 0.5
		Geography.Countries                          0.776
		STEM.Medicine                                0.755
		Assistance.Contents systems                  0.58
		STEM.Biology                                 0.757
		Culture.Plastic arts                         0.784
		STEM.Mathematics                             0.843
		Culture.Language and literature              0.874
		History_And_Society.History and society      0.484
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Culture.Sports': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Oceania': {'type': 'number'}, 'Culture.Media': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Landforms': {'type': 'number'}, 'STEM.Time': {'type': 'number'}, 'Culture.Arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Bodies of water': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Broadcasting': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Information science': {'type': 'number'}, 'History_And_Society.Education': {'type': 'number'}, 'Culture.Entertainment': {'type': 'number'}, 'History_And_Society.Politics and government': {'type': 'number'}, 'Assistance.Files': {'type': 'number'}, 'STEM.Geosciences': {'type': 'number'}, 'Geography.Maps': {'type': 'number'}, 'Geography.Cities': {'type': 'number'}, 'Culture.Crafts and hobbies': {'type': 'number'}, 'History_And_Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Plastic arts': {'type': 'number'}, 'Assistance.Maintenance': {'type': 'number'}, 'History_And_Society.Transportation': {'type': 'number'}, 'Geography.Europe': {'type': 'number'}, 'Assistance.Article improvement and grading': {'type': 'number'}, 'History_And_Society.Military and warfare': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Science': {'type': 'number'}, 'Geography.Countries': {'type': 'number'}, 'STEM.Medicine': {'type': 'number'}, 'Assistance.Contents systems': {'type': 'number'}, 'STEM.Meteorology': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Language and literature': {'type': 'number'}, 'History_And_Society.History and society': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

