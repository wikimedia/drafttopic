Model Information:
	 - type: GradientBoosting
	 - version: 0.2
	 - params: {'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'n_estimators': 150, 'max_depth': 5, 'population_rates': None, 'min_samples_leaf': 1, 'criterion': 'friedman_mse', 'multilabel': True, 'min_impurity_split': None, 'subsample': 1.0, 'learning_rate': 0.1, 'loss': 'deviance', 'random_state': None, 'init': None, 'scale': False, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'presort': 'auto', 'validation_fraction': 0.1, 'label_weights': {}, 'warm_start': False, 'center': False, 'labels': ['Geography.Oceania', 'STEM.Mathematics', 'STEM.Science', 'STEM.Meteorology', 'Culture.Sports', 'Culture.Performing arts', 'Culture.Entertainment', 'Assistance.Article improvement and grading', 'Culture.Language and literature', 'Culture.Visual arts', 'STEM.Biology', 'History_And_Society.Business and economics', 'Assistance.Files', 'History_And_Society.History and society', 'STEM.Medicine', 'Culture.Crafts and hobbies', 'STEM.Geosciences', 'Culture.Food and drink', 'History_And_Society.Transportation', 'Geography.Cities', 'Geography.Landforms', 'Assistance.Maintenance', 'STEM.Information science', 'STEM.Time', 'Geography.Europe', 'STEM.Engineering', 'Culture.Media', 'STEM.Technology', 'STEM.Space', 'History_And_Society.Education', 'Geography.Countries', 'History_And_Society.Military and warfare', 'Culture.Plastic arts', 'STEM.Physics', 'History_And_Society.Politics and government', 'STEM.Chemistry', 'Culture.Broadcasting', 'Geography.Maps', 'Culture.Arts', 'Culture.Internet culture', 'Geography.Bodies of water', 'Assistance.Contents systems', 'Culture.Philosophy and religion'], 'min_samples_split': 2, 'max_features': 'log2', 'max_leaf_nodes': None}
	Environment:
	 - revscoring_version: '2.5.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.168-1+deb9u2 (2019-05-13)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-9-amd64'
	
	Statistics:
	counts (n=83530):
			label                                              n          TP    FP     FN     TN
			---------------------------------------------  -----  ---  -----  ----  -----  -----
			'Geography.Oceania'                             3978  -->   2445  1533    211  79341
			'STEM.Mathematics'                              1440  -->    945   495     93  81997
			'STEM.Science'                                  2118  -->    530  1588    146  81266
			'STEM.Meteorology'                              1728  -->   1329   399     65  81737
			'Culture.Sports'                                4809  -->   3977   832    360  78361
			'Culture.Performing arts'                       4154  -->   3288   866    394  78982
			'Culture.Entertainment'                         5464  -->   3567  1897    556  77510
			'Assistance.Article improvement and grading'      66  -->     26    40  16654  66810
			'Culture.Language and literature'              19460  -->  14167  5293   2387  61683
			'Culture.Visual arts'                           4529  -->   2564  1965    554  78447
			'STEM.Biology'                                  3094  -->   1749  1345    258  80178
			'History_And_Society.Business and economics'    5999  -->   2964  3035    819  76712
			'Assistance.Files'                               350  -->     29   321    159  83021
			'History_And_Society.History and society'       6937  -->   1368  5569    511  76082
			'STEM.Medicine'                                 1942  -->   1106   836    254  81334
			'Culture.Crafts and hobbies'                    1950  -->   1127   823     53  81527
			'STEM.Geosciences'                              1970  -->   1156   814    129  81431
			'Culture.Food and drink'                        2243  -->   1544   699    143  81144
			'History_And_Society.Transportation'            3630  -->   2487  1143    333  79567
			'Geography.Cities'                               786  -->    492   294    132  82612
			'Geography.Landforms'                           2133  -->   1707   426    122  81275
			'Assistance.Maintenance'                        4982  -->   1076  3906    254  78294
			'STEM.Information science'                      2024  -->   1149   875     99  81407
			'STEM.Time'                                     2208  -->   1530   678    101  81221
			'Geography.Europe'                             15169  -->   8910  6259   2563  65798
			'STEM.Engineering'                              2115  -->    747  1368    260  81155
			'Culture.Media'                                 2021  -->    558  1463    230  81279
			'STEM.Technology'                               3777  -->   1308  2469    587  79166
			'STEM.Space'                                    2105  -->   1712   393     87  81338
			'History_And_Society.Education'                 2605  -->   1581  1024    233  80692
			'Geography.Countries'                          23775  -->  14187  9588   4179  55576
			'History_And_Society.Military and warfare'      3874  -->   2422  1452    385  79271
			'Culture.Plastic arts'                          3676  -->   2099  1577    380  79474
			'STEM.Physics'                                  2365  -->   1235  1130    375  80790
			'History_And_Society.Politics and government'   3869  -->   1445  2424    501  79160
			'STEM.Chemistry'                                2074  -->   1290   784    272  81184
			'Culture.Broadcasting'                          2757  -->   1560  1197    367  80406
			'Geography.Maps'                                2405  -->   1407   998     92  81033
			'Culture.Arts'                                  1984  -->   1462   522    108  81438
			'Culture.Internet culture'                      1811  -->    905   906    216  81503
			'Geography.Bodies of water'                     2225  -->   1718   507    150  81155
			'Assistance.Contents systems'                   1932  -->    659  1273    142  81456
			'Culture.Philosophy and religion'               3793  -->   1686  2107    454  79283
	rates:
		          'Geography.Oceania'    'STEM.Mathematics'    'STEM.Science'    'STEM.Meteorology'    'Culture.Sports'    'Culture.Performing arts'    'Culture.Entertainment'    'Assistance.Article improvement and grading'    'Culture.Language and literature'    'Culture.Visual arts'    'STEM.Biology'    'History_And_Society.Business and economics'    'Assistance.Files'    'History_And_Society.History and society'    'STEM.Medicine'    'Culture.Crafts and hobbies'    'STEM.Geosciences'    'Culture.Food and drink'    'History_And_Society.Transportation'    'Geography.Cities'    'Geography.Landforms'    'Assistance.Maintenance'    'STEM.Information science'    'STEM.Time'    'Geography.Europe'    'STEM.Engineering'    'Culture.Media'    'STEM.Technology'    'STEM.Space'    'History_And_Society.Education'    'Geography.Countries'    'History_And_Society.Military and warfare'    'Culture.Plastic arts'    'STEM.Physics'    'History_And_Society.Politics and government'    'STEM.Chemistry'    'Culture.Broadcasting'    'Geography.Maps'    'Culture.Arts'    'Culture.Internet culture'    'Geography.Bodies of water'    'Assistance.Contents systems'    'Culture.Philosophy and religion'
		------  ---------------------  --------------------  ----------------  --------------------  ------------------  ---------------------------  -------------------------  ----------------------------------------------  -----------------------------------  -----------------------  ----------------  ----------------------------------------------  --------------------  -------------------------------------------  -----------------  ------------------------------  --------------------  --------------------------  --------------------------------------  --------------------  -----------------------  --------------------------  ----------------------------  -------------  --------------------  --------------------  -----------------  -------------------  --------------  ---------------------------------  -----------------------  --------------------------------------------  ------------------------  ----------------  -----------------------------------------------  ------------------  ------------------------  ------------------  ----------------  ----------------------------  -----------------------------  -------------------------------  -----------------------------------
		sample                  0.048                 0.017             0.025                 0.021               0.058                         0.05                      0.065                                           0.001                                0.233                    0.054             0.037                                           0.072                 0.004                                        0.083              0.023                           0.023                 0.024                       0.027                                   0.043                 0.009                    0.026                        0.06                         0.024          0.026                 0.182                 0.025              0.024                0.045           0.025                              0.031                    0.285                                         0.046                     0.044             0.028                                            0.046               0.025                     0.033               0.029             0.024                         0.022                          0.027                            0.023                                0.045
	match_rate (micro=0.082, macro=0.038):
		-------------------------------------------  -----
		History_And_Society.Education                0.022
		STEM.Geosciences                             0.015
		Culture.Language and literature              0.198
		Assistance.Maintenance                       0.016
		STEM.Technology                              0.023
		Geography.Cities                             0.007
		Culture.Sports                               0.052
		STEM.Chemistry                               0.019
		STEM.Physics                                 0.019
		Culture.Broadcasting                         0.023
		Assistance.Contents systems                  0.01
		Geography.Oceania                            0.032
		Assistance.Files                             0.002
		Geography.Maps                               0.018
		Assistance.Article improvement and grading   0.2
		Geography.Landforms                          0.022
		Culture.Visual arts                          0.037
		STEM.Medicine                                0.016
		Culture.Plastic arts                         0.03
		Culture.Arts                                 0.019
		Culture.Food and drink                       0.02
		STEM.Information science                     0.015
		STEM.Engineering                             0.012
		Culture.Philosophy and religion              0.026
		STEM.Science                                 0.008
		Culture.Crafts and hobbies                   0.014
		History_And_Society.Business and economics   0.045
		Geography.Countries                          0.22
		STEM.Time                                    0.02
		STEM.Biology                                 0.024
		History_And_Society.Transportation           0.034
		STEM.Meteorology                             0.017
		History_And_Society.Politics and government  0.023
		Culture.Internet culture                     0.013
		History_And_Society.Military and warfare     0.034
		Culture.Media                                0.009
		STEM.Mathematics                             0.012
		STEM.Space                                   0.022
		Culture.Performing arts                      0.044
		Geography.Bodies of water                    0.022
		Geography.Europe                             0.137
		History_And_Society.History and society      0.022
		Culture.Entertainment                        0.049
		-------------------------------------------  -----
	filter_rate (micro=0.918, macro=0.962):
		-------------------------------------------  -----
		History_And_Society.Education                0.978
		STEM.Geosciences                             0.985
		Culture.Language and literature              0.802
		Assistance.Maintenance                       0.984
		STEM.Technology                              0.977
		Geography.Cities                             0.993
		Culture.Sports                               0.948
		STEM.Chemistry                               0.981
		STEM.Physics                                 0.981
		Culture.Broadcasting                         0.977
		Assistance.Contents systems                  0.99
		Geography.Oceania                            0.968
		Assistance.Files                             0.998
		Geography.Maps                               0.982
		Assistance.Article improvement and grading   0.8
		Geography.Landforms                          0.978
		Culture.Visual arts                          0.963
		STEM.Medicine                                0.984
		Culture.Plastic arts                         0.97
		Culture.Arts                                 0.981
		Culture.Food and drink                       0.98
		STEM.Information science                     0.985
		STEM.Engineering                             0.988
		Culture.Philosophy and religion              0.974
		STEM.Science                                 0.992
		Culture.Crafts and hobbies                   0.986
		History_And_Society.Business and economics   0.955
		Geography.Countries                          0.78
		STEM.Time                                    0.98
		STEM.Biology                                 0.976
		History_And_Society.Transportation           0.966
		STEM.Meteorology                             0.983
		History_And_Society.Politics and government  0.977
		Culture.Internet culture                     0.987
		History_And_Society.Military and warfare     0.966
		Culture.Media                                0.991
		STEM.Mathematics                             0.988
		STEM.Space                                   0.978
		Culture.Performing arts                      0.956
		Geography.Bodies of water                    0.978
		Geography.Europe                             0.863
		History_And_Society.History and society      0.978
		Culture.Entertainment                        0.951
		-------------------------------------------  -----
	recall (micro=0.576, macro=0.554):
		-------------------------------------------  -----
		History_And_Society.Education                0.607
		STEM.Geosciences                             0.587
		Culture.Language and literature              0.728
		Assistance.Maintenance                       0.216
		STEM.Technology                              0.346
		Geography.Cities                             0.626
		Culture.Sports                               0.827
		STEM.Chemistry                               0.622
		STEM.Physics                                 0.522
		Culture.Broadcasting                         0.566
		Assistance.Contents systems                  0.341
		Geography.Oceania                            0.615
		Assistance.Files                             0.083
		Geography.Maps                               0.585
		Assistance.Article improvement and grading   0.394
		Geography.Landforms                          0.8
		Culture.Visual arts                          0.566
		STEM.Medicine                                0.57
		Culture.Plastic arts                         0.571
		Culture.Arts                                 0.737
		Culture.Food and drink                       0.688
		STEM.Information science                     0.568
		STEM.Engineering                             0.353
		Culture.Philosophy and religion              0.445
		STEM.Science                                 0.25
		Culture.Crafts and hobbies                   0.578
		History_And_Society.Business and economics   0.494
		Geography.Countries                          0.597
		STEM.Time                                    0.693
		STEM.Biology                                 0.565
		History_And_Society.Transportation           0.685
		STEM.Meteorology                             0.769
		History_And_Society.Politics and government  0.373
		Culture.Internet culture                     0.5
		History_And_Society.Military and warfare     0.625
		Culture.Media                                0.276
		STEM.Mathematics                             0.656
		STEM.Space                                   0.813
		Culture.Performing arts                      0.792
		Geography.Bodies of water                    0.772
		Geography.Europe                             0.587
		History_And_Society.History and society      0.197
		Culture.Entertainment                        0.653
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.989):
		-------------------------------------------  -----
		History_And_Society.Education                0.997
		STEM.Geosciences                             0.998
		Culture.Language and literature              0.963
		Assistance.Maintenance                       0.997
		STEM.Technology                              0.993
		Geography.Cities                             0.998
		Culture.Sports                               0.995
		STEM.Chemistry                               0.997
		STEM.Physics                                 0.995
		Culture.Broadcasting                         0.995
		Assistance.Contents systems                  0.998
		Geography.Oceania                            0.997
		Assistance.Files                             0.998
		Geography.Maps                               0.999
		Assistance.Article improvement and grading   0.8
		Geography.Landforms                          0.999
		Culture.Visual arts                          0.993
		STEM.Medicine                                0.997
		Culture.Plastic arts                         0.995
		Culture.Arts                                 0.999
		Culture.Food and drink                       0.998
		STEM.Information science                     0.999
		STEM.Engineering                             0.997
		Culture.Philosophy and religion              0.994
		STEM.Science                                 0.998
		Culture.Crafts and hobbies                   0.999
		History_And_Society.Business and economics   0.989
		Geography.Countries                          0.93
		STEM.Time                                    0.999
		STEM.Biology                                 0.997
		History_And_Society.Transportation           0.996
		STEM.Meteorology                             0.999
		History_And_Society.Politics and government  0.994
		Culture.Internet culture                     0.997
		History_And_Society.Military and warfare     0.995
		Culture.Media                                0.997
		STEM.Mathematics                             0.999
		STEM.Space                                   0.999
		Culture.Performing arts                      0.995
		Geography.Bodies of water                    0.998
		Geography.Europe                             0.963
		History_And_Society.History and society      0.993
		Culture.Entertainment                        0.993
		-------------------------------------------  -----
	precision (micro=0.826, macro=0.811):
		-------------------------------------------  -----
		History_And_Society.Education                0.872
		STEM.Geosciences                             0.9
		Culture.Language and literature              0.856
		Assistance.Maintenance                       0.809
		STEM.Technology                              0.69
		Geography.Cities                             0.788
		Culture.Sports                               0.917
		STEM.Chemistry                               0.826
		STEM.Physics                                 0.767
		Culture.Broadcasting                         0.81
		Assistance.Contents systems                  0.823
		Geography.Oceania                            0.921
		Assistance.Files                             0.154
		Geography.Maps                               0.939
		Assistance.Article improvement and grading   0.002
		Geography.Landforms                          0.933
		Culture.Visual arts                          0.822
		STEM.Medicine                                0.813
		Culture.Plastic arts                         0.847
		Culture.Arts                                 0.931
		Culture.Food and drink                       0.915
		STEM.Information science                     0.921
		STEM.Engineering                             0.742
		Culture.Philosophy and religion              0.788
		STEM.Science                                 0.784
		Culture.Crafts and hobbies                   0.955
		History_And_Society.Business and economics   0.784
		Geography.Countries                          0.772
		STEM.Time                                    0.938
		STEM.Biology                                 0.871
		History_And_Society.Transportation           0.882
		STEM.Meteorology                             0.953
		History_And_Society.Politics and government  0.743
		Culture.Internet culture                     0.807
		History_And_Society.Military and warfare     0.863
		Culture.Media                                0.708
		STEM.Mathematics                             0.91
		STEM.Space                                   0.952
		Culture.Performing arts                      0.893
		Geography.Bodies of water                    0.92
		Geography.Europe                             0.777
		History_And_Society.History and society      0.728
		Culture.Entertainment                        0.865
		-------------------------------------------  -----
	!precision (micro=0.949, macro=0.978):
		-------------------------------------------  -----
		History_And_Society.Education                0.987
		STEM.Geosciences                             0.99
		Culture.Language and literature              0.921
		Assistance.Maintenance                       0.952
		STEM.Technology                              0.97
		Geography.Cities                             0.996
		Culture.Sports                               0.989
		STEM.Chemistry                               0.99
		STEM.Physics                                 0.986
		Culture.Broadcasting                         0.985
		Assistance.Contents systems                  0.985
		Geography.Oceania                            0.981
		Assistance.Files                             0.996
		Geography.Maps                               0.988
		Assistance.Article improvement and grading   0.999
		Geography.Landforms                          0.995
		Culture.Visual arts                          0.976
		STEM.Medicine                                0.99
		Culture.Plastic arts                         0.981
		Culture.Arts                                 0.994
		Culture.Food and drink                       0.991
		STEM.Information science                     0.989
		STEM.Engineering                             0.983
		Culture.Philosophy and religion              0.974
		STEM.Science                                 0.981
		Culture.Crafts and hobbies                   0.99
		History_And_Society.Business and economics   0.962
		Geography.Countries                          0.853
		STEM.Time                                    0.992
		STEM.Biology                                 0.984
		History_And_Society.Transportation           0.986
		STEM.Meteorology                             0.995
		History_And_Society.Politics and government  0.97
		Culture.Internet culture                     0.989
		History_And_Society.Military and warfare     0.982
		Culture.Media                                0.982
		STEM.Mathematics                             0.994
		STEM.Space                                   0.995
		Culture.Performing arts                      0.989
		Geography.Bodies of water                    0.994
		Geography.Europe                             0.913
		History_And_Society.History and society      0.932
		Culture.Entertainment                        0.976
		-------------------------------------------  -----
	f1 (micro=0.668, macro=0.643):
		-------------------------------------------  -----
		History_And_Society.Education                0.716
		STEM.Geosciences                             0.71
		Culture.Language and literature              0.787
		Assistance.Maintenance                       0.341
		STEM.Technology                              0.461
		Geography.Cities                             0.698
		Culture.Sports                               0.87
		STEM.Chemistry                               0.71
		STEM.Physics                                 0.621
		Culture.Broadcasting                         0.666
		Assistance.Contents systems                  0.482
		Geography.Oceania                            0.737
		Assistance.Files                             0.108
		Geography.Maps                               0.721
		Assistance.Article improvement and grading   0.003
		Geography.Landforms                          0.862
		Culture.Visual arts                          0.671
		STEM.Medicine                                0.67
		Culture.Plastic arts                         0.682
		Culture.Arts                                 0.823
		Culture.Food and drink                       0.786
		STEM.Information science                     0.702
		STEM.Engineering                             0.479
		Culture.Philosophy and religion              0.568
		STEM.Science                                 0.379
		Culture.Crafts and hobbies                   0.72
		History_And_Society.Business and economics   0.606
		Geography.Countries                          0.673
		STEM.Time                                    0.797
		STEM.Biology                                 0.686
		History_And_Society.Transportation           0.771
		STEM.Meteorology                             0.851
		History_And_Society.Politics and government  0.497
		Culture.Internet culture                     0.617
		History_And_Society.Military and warfare     0.725
		Culture.Media                                0.397
		STEM.Mathematics                             0.763
		STEM.Space                                   0.877
		Culture.Performing arts                      0.839
		Geography.Bodies of water                    0.839
		Geography.Europe                             0.669
		History_And_Society.History and society      0.31
		Culture.Entertainment                        0.744
		-------------------------------------------  -----
	!f1 (micro=0.964, macro=0.983):
		-------------------------------------------  -----
		History_And_Society.Education                0.992
		STEM.Geosciences                             0.994
		Culture.Language and literature              0.941
		Assistance.Maintenance                       0.974
		STEM.Technology                              0.981
		Geography.Cities                             0.997
		Culture.Sports                               0.992
		STEM.Chemistry                               0.994
		STEM.Physics                                 0.991
		Culture.Broadcasting                         0.99
		Assistance.Contents systems                  0.991
		Geography.Oceania                            0.989
		Assistance.Files                             0.997
		Geography.Maps                               0.993
		Assistance.Article improvement and grading   0.889
		Geography.Landforms                          0.997
		Culture.Visual arts                          0.984
		STEM.Medicine                                0.993
		Culture.Plastic arts                         0.988
		Culture.Arts                                 0.996
		Culture.Food and drink                       0.995
		STEM.Information science                     0.994
		STEM.Engineering                             0.99
		Culture.Philosophy and religion              0.984
		STEM.Science                                 0.989
		Culture.Crafts and hobbies                   0.995
		History_And_Society.Business and economics   0.975
		Geography.Countries                          0.89
		STEM.Time                                    0.995
		STEM.Biology                                 0.99
		History_And_Society.Transportation           0.991
		STEM.Meteorology                             0.997
		History_And_Society.Politics and government  0.982
		Culture.Internet culture                     0.993
		History_And_Society.Military and warfare     0.989
		Culture.Media                                0.99
		STEM.Mathematics                             0.996
		STEM.Space                                   0.997
		Culture.Performing arts                      0.992
		Geography.Bodies of water                    0.996
		Geography.Europe                             0.937
		History_And_Society.History and society      0.962
		Culture.Entertainment                        0.984
		-------------------------------------------  -----
	accuracy (micro=0.941, macro=0.97):
		-------------------------------------------  -----
		History_And_Society.Education                0.985
		STEM.Geosciences                             0.989
		Culture.Language and literature              0.908
		Assistance.Maintenance                       0.95
		STEM.Technology                              0.963
		Geography.Cities                             0.995
		Culture.Sports                               0.986
		STEM.Chemistry                               0.987
		STEM.Physics                                 0.982
		Culture.Broadcasting                         0.981
		Assistance.Contents systems                  0.983
		Geography.Oceania                            0.979
		Assistance.Files                             0.994
		Geography.Maps                               0.987
		Assistance.Article improvement and grading   0.8
		Geography.Landforms                          0.993
		Culture.Visual arts                          0.97
		STEM.Medicine                                0.987
		Culture.Plastic arts                         0.977
		Culture.Arts                                 0.992
		Culture.Food and drink                       0.99
		STEM.Information science                     0.988
		STEM.Engineering                             0.981
		Culture.Philosophy and religion              0.969
		STEM.Science                                 0.979
		Culture.Crafts and hobbies                   0.99
		History_And_Society.Business and economics   0.954
		Geography.Countries                          0.835
		STEM.Time                                    0.991
		STEM.Biology                                 0.981
		History_And_Society.Transportation           0.982
		STEM.Meteorology                             0.994
		History_And_Society.Politics and government  0.965
		Culture.Internet culture                     0.987
		History_And_Society.Military and warfare     0.978
		Culture.Media                                0.98
		STEM.Mathematics                             0.993
		STEM.Space                                   0.994
		Culture.Performing arts                      0.985
		Geography.Bodies of water                    0.992
		Geography.Europe                             0.894
		History_And_Society.History and society      0.927
		Culture.Entertainment                        0.971
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.011):
		-------------------------------------------  -----
		History_And_Society.Education                0.003
		STEM.Geosciences                             0.002
		Culture.Language and literature              0.037
		Assistance.Maintenance                       0.003
		STEM.Technology                              0.007
		Geography.Cities                             0.002
		Culture.Sports                               0.005
		STEM.Chemistry                               0.003
		STEM.Physics                                 0.005
		Culture.Broadcasting                         0.005
		Assistance.Contents systems                  0.002
		Geography.Oceania                            0.003
		Assistance.Files                             0.002
		Geography.Maps                               0.001
		Assistance.Article improvement and grading   0.2
		Geography.Landforms                          0.001
		Culture.Visual arts                          0.007
		STEM.Medicine                                0.003
		Culture.Plastic arts                         0.005
		Culture.Arts                                 0.001
		Culture.Food and drink                       0.002
		STEM.Information science                     0.001
		STEM.Engineering                             0.003
		Culture.Philosophy and religion              0.006
		STEM.Science                                 0.002
		Culture.Crafts and hobbies                   0.001
		History_And_Society.Business and economics   0.011
		Geography.Countries                          0.07
		STEM.Time                                    0.001
		STEM.Biology                                 0.003
		History_And_Society.Transportation           0.004
		STEM.Meteorology                             0.001
		History_And_Society.Politics and government  0.006
		Culture.Internet culture                     0.003
		History_And_Society.Military and warfare     0.005
		Culture.Media                                0.003
		STEM.Mathematics                             0.001
		STEM.Space                                   0.001
		Culture.Performing arts                      0.005
		Geography.Bodies of water                    0.002
		Geography.Europe                             0.037
		History_And_Society.History and society      0.007
		Culture.Entertainment                        0.007
		-------------------------------------------  -----
	roc_auc (micro=0.943, macro=0.948):
		-------------------------------------------  -----
		History_And_Society.Education                0.966
		STEM.Geosciences                             0.972
		Culture.Language and literature              0.95
		Assistance.Maintenance                       0.837
		STEM.Technology                              0.941
		Geography.Cities                             0.968
		Culture.Sports                               0.977
		STEM.Chemistry                               0.981
		STEM.Physics                                 0.975
		Culture.Broadcasting                         0.972
		Assistance.Contents systems                  0.948
		Geography.Oceania                            0.966
		Assistance.Files                             0.768
		Geography.Maps                               0.968
		Assistance.Article improvement and grading   0.688
		Geography.Landforms                          0.988
		Culture.Visual arts                          0.968
		STEM.Medicine                                0.974
		Culture.Plastic arts                         0.967
		Culture.Arts                                 0.984
		Culture.Food and drink                       0.975
		STEM.Information science                     0.97
		STEM.Engineering                             0.954
		Culture.Philosophy and religion              0.936
		STEM.Science                                 0.934
		Culture.Crafts and hobbies                   0.963
		History_And_Society.Business and economics   0.947
		Geography.Countries                          0.894
		STEM.Time                                    0.97
		STEM.Biology                                 0.958
		History_And_Society.Transportation           0.976
		STEM.Meteorology                             0.987
		History_And_Society.Politics and government  0.94
		Culture.Internet culture                     0.97
		History_And_Society.Military and warfare     0.968
		Culture.Media                                0.951
		STEM.Mathematics                             0.98
		STEM.Space                                   0.987
		Culture.Performing arts                      0.983
		Geography.Bodies of water                    0.986
		Geography.Europe                             0.929
		History_And_Society.History and society      0.87
		Culture.Entertainment                        0.971
		-------------------------------------------  -----
	pr_auc (micro=0.76, macro=0.723):
		-------------------------------------------  -----
		History_And_Society.Education                0.771
		STEM.Geosciences                             0.798
		Culture.Language and literature              0.872
		Assistance.Maintenance                       0.447
		STEM.Technology                              0.554
		Geography.Cities                             0.728
		Culture.Sports                               0.915
		STEM.Chemistry                               0.79
		STEM.Physics                                 0.706
		Culture.Broadcasting                         0.727
		Assistance.Contents systems                  0.603
		Geography.Oceania                            0.837
		Assistance.Files                             0.039
		Geography.Maps                               0.834
		Assistance.Article improvement and grading   0.001
		Geography.Landforms                          0.929
		Culture.Visual arts                          0.768
		STEM.Medicine                                0.754
		Culture.Plastic arts                         0.783
		Culture.Arts                                 0.902
		Culture.Food and drink                       0.853
		STEM.Information science                     0.8
		STEM.Engineering                             0.581
		Culture.Philosophy and religion              0.618
		STEM.Science                                 0.507
		Culture.Crafts and hobbies                   0.814
		History_And_Society.Business and economics   0.704
		Geography.Countries                          0.777
		STEM.Time                                    0.866
		STEM.Biology                                 0.749
		History_And_Society.Transportation           0.863
		STEM.Meteorology                             0.926
		History_And_Society.Politics and government  0.594
		Culture.Internet culture                     0.691
		History_And_Society.Military and warfare     0.807
		Culture.Media                                0.505
		STEM.Mathematics                             0.843
		STEM.Space                                   0.935
		Culture.Performing arts                      0.918
		Geography.Bodies of water                    0.909
		Geography.Europe                             0.768
		History_And_Society.History and society      0.476
		Culture.Entertainment                        0.842
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'History_And_Society.Education': {'type': 'number'}, 'STEM.Geosciences': {'type': 'number'}, 'Culture.Language and literature': {'type': 'number'}, 'Assistance.Maintenance': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Cities': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Broadcasting': {'type': 'number'}, 'Assistance.Contents systems': {'type': 'number'}, 'History_And_Society.Business and economics': {'type': 'number'}, 'Geography.Oceania': {'type': 'number'}, 'Assistance.Files': {'type': 'number'}, 'Geography.Maps': {'type': 'number'}, 'Assistance.Article improvement and grading': {'type': 'number'}, 'Geography.Landforms': {'type': 'number'}, 'Culture.Visual arts': {'type': 'number'}, 'STEM.Medicine': {'type': 'number'}, 'Culture.Plastic arts': {'type': 'number'}, 'Culture.Arts': {'type': 'number'}, 'History_And_Society.Military and warfare': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Science': {'type': 'number'}, 'Culture.Crafts and hobbies': {'type': 'number'}, 'STEM.Information science': {'type': 'number'}, 'Geography.Countries': {'type': 'number'}, 'STEM.Time': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'History_And_Society.Transportation': {'type': 'number'}, 'STEM.Meteorology': {'type': 'number'}, 'History_And_Society.Politics and government': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Bodies of water': {'type': 'number'}, 'Geography.Europe': {'type': 'number'}, 'History_And_Society.History and society': {'type': 'number'}, 'Culture.Entertainment': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'type': 'object'}

