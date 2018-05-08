Model Information:
	 - type: GradientBoosting
	 - version: 0.1.0
	 - params: {'learning_rate': 0.1, 'min_impurity_split': None, 'max_leaf_nodes': None, 'multilabel': True, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'min_samples_split': 2, 'criterion': 'friedman_mse', 'max_depth': 5, 'init': None, 'max_features': 'log2', 'center': False, 'random_state': None, 'label_weights': {}, 'population_rates': None, 'n_estimators': 150, 'min_impurity_decrease': 0.0, 'warm_start': False, 'min_samples_leaf': 1, 'scale': False, 'subsample': 1.0, 'verbose': 0, 'presort': 'auto', 'labels': ['STEM.Biology', 'STEM.Space', 'STEM.Information science', 'Geography.Maps', 'Culture.Philosophy and religion', 'Culture.Plastic arts', 'History_And_Society.Politics and government', 'STEM.Engineering', 'Culture.Media', 'Culture.Entertainment', 'Geography.Bodies of water', 'STEM.Physics', 'Assistance.Article improvement and grading', 'STEM.Technology', 'Geography.Oceania', 'Culture.Performing arts', 'STEM.Science', 'STEM.Meteorology', 'Geography.Europe', 'Culture.Crafts and hobbies', 'STEM.Medicine', 'History_And_Society.Business and economics', 'Culture.Internet culture', 'Culture.Arts', 'Assistance.Maintenance', 'STEM.Geosciences', 'Geography.Landforms', 'Culture.Food and drink', 'STEM.Chemistry', 'Culture.Language and literature', 'STEM.Time', 'Geography.Cities', 'History_And_Society.Education', 'Assistance.Contents systems', 'History_And_Society.Transportation', 'Assistance.Files', 'Culture.Visual arts', 'History_And_Society.History and society', 'Geography.Countries', 'History_And_Society.Military and warfare', 'Culture.Sports', 'Culture.Broadcasting', 'STEM.Mathematics']}
	Environment:
	 - revscoring_version: '2.2.3'
	 - platform: 'Linux-4.9.0-5-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.65-3+deb9u2 (2018-01-04)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-5-amd64'
	
	Statistics:
	counts (n=84481):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'STEM.Biology'                                  3134  -->   1784  1350   276  81071
			'STEM.Space'                                    2117  -->   1735   382    93  82271
			'STEM.Information science'                      2037  -->   1174   863   110  82334
			'Geography.Maps'                                2421  -->   1401  1020    63  81997
			'Culture.Philosophy and religion'               3840  -->   1689  2151   481  80160
			'Culture.Plastic arts'                          3717  -->   2121  1596   401  80363
			'History_And_Society.Politics and government'   4047  -->   1557  2490   530  79904
			'STEM.Engineering'                              2133  -->    792  1341   236  82112
			'Culture.Media'                                 2040  -->    599  1441   261  82180
			'Culture.Entertainment'                         5529  -->   3636  1893   562  78390
			'Geography.Bodies of water'                     2232  -->   1725   507   154  82095
			'STEM.Physics'                                  2376  -->   1266  1110   340  81765
			'Assistance.Article improvement and grading'      67  -->     22    45   107  84307
			'STEM.Technology'                               3826  -->   1333  2493   580  80075
			'Geography.Oceania'                             4025  -->   2458  1567   206  80250
			'Culture.Performing arts'                       4180  -->   3310   870   399  79902
			'STEM.Science'                                  2133  -->    537  1596   151  82197
			'STEM.Meteorology'                              1753  -->   1345   408    68  82660
			'Geography.Europe'                             15349  -->   8931  6418  2556  66576
			'Culture.Crafts and hobbies'                    1988  -->   1139   849    62  82431
			'STEM.Medicine'                                 1951  -->   1112   839   255  82275
			'History_And_Society.Business and economics'    6075  -->   3018  3057   796  77610
			'Culture.Internet culture'                      1839  -->    929   910   212  82430
			'Culture.Arts'                                  1999  -->   1451   548    92  82390
			'Assistance.Maintenance'                        5028  -->   1089  3939   254  79199
			'STEM.Geosciences'                              1987  -->   1172   815   122  82372
			'Geography.Landforms'                           2148  -->   1717   431   121  82212
			'Culture.Food and drink'                        2264  -->   1563   701   160  82057
			'STEM.Chemistry'                                2083  -->   1307   776   240  82158
			'Culture.Language and literature'              19588  -->  14221  5367  2454  62439
			'STEM.Time'                                     2216  -->   1513   703    95  82170
			'Geography.Cities'                               791  -->    496   295   107  83583
			'History_And_Society.Education'                 2633  -->   1598  1035   249  81599
			'Assistance.Contents systems'                   1953  -->    683  1270   154  82374
			'History_And_Society.Transportation'            3680  -->   2512  1168   328  80473
			'Assistance.Files'                               350  -->     21   329   137  83994
			'Culture.Visual arts'                           4563  -->   2557  2006   541  79377
			'History_And_Society.History and society'       7010  -->   1373  5637   548  76923
			'Geography.Countries'                          24068  -->  14420  9648  4238  56175
			'History_And_Society.Military and warfare'      3921  -->   2472  1449   391  80169
			'Culture.Sports'                                4844  -->   3965   879   385  79252
			'Culture.Broadcasting'                          2807  -->   1596  1211   424  81250
			'STEM.Mathematics'                              1454  -->    944   510    86  82941
	rates:
		          'STEM.Biology'    'STEM.Space'    'STEM.Information science'    'Geography.Maps'    'Culture.Philosophy and religion'    'Culture.Plastic arts'    'History_And_Society.Politics and government'    'STEM.Engineering'    'Culture.Media'    'Culture.Entertainment'    'Geography.Bodies of water'    'STEM.Physics'    'Assistance.Article improvement and grading'    'STEM.Technology'    'Geography.Oceania'    'Culture.Performing arts'    'STEM.Science'    'STEM.Meteorology'    'Geography.Europe'    'Culture.Crafts and hobbies'    'STEM.Medicine'    'History_And_Society.Business and economics'    'Culture.Internet culture'    'Culture.Arts'    'Assistance.Maintenance'    'STEM.Geosciences'    'Geography.Landforms'    'Culture.Food and drink'    'STEM.Chemistry'    'Culture.Language and literature'    'STEM.Time'    'Geography.Cities'    'History_And_Society.Education'    'Assistance.Contents systems'    'History_And_Society.Transportation'    'Assistance.Files'    'Culture.Visual arts'    'History_And_Society.History and society'    'Geography.Countries'    'History_And_Society.Military and warfare'    'Culture.Sports'    'Culture.Broadcasting'    'STEM.Mathematics'
		------  ----------------  --------------  ----------------------------  ------------------  -----------------------------------  ------------------------  -----------------------------------------------  --------------------  -----------------  -------------------------  -----------------------------  ----------------  ----------------------------------------------  -------------------  ---------------------  ---------------------------  ----------------  --------------------  --------------------  ------------------------------  -----------------  ----------------------------------------------  ----------------------------  ----------------  --------------------------  --------------------  -----------------------  --------------------------  ------------------  -----------------------------------  -------------  --------------------  ---------------------------------  -------------------------------  --------------------------------------  --------------------  -----------------------  -------------------------------------------  -----------------------  --------------------------------------------  ------------------  ------------------------  --------------------
		sample             0.037           0.025                         0.024               0.029                                0.045                     0.044                                            0.048                 0.025              0.024                      0.065                          0.026             0.028                                           0.001                0.045                  0.048                        0.049             0.025                 0.021                 0.182                           0.024              0.023                                           0.072                         0.022             0.024                        0.06                 0.024                    0.025                       0.027               0.025                                0.232          0.026                 0.009                              0.031                            0.023                                   0.044                 0.004                    0.054                                        0.083                    0.285                                         0.046               0.057                     0.033                 0.017
	match_rate (micro=0.082, macro=0.033):
		-------------------------------------------  -----
		Geography.Cities                             0.007
		History_And_Society.Military and warfare     0.034
		Culture.Language and literature              0.197
		Assistance.Maintenance                       0.016
		Culture.Media                                0.01
		STEM.Chemistry                               0.018
		Geography.Maps                               0.017
		STEM.Meteorology                             0.017
		History_And_Society.Politics and government  0.025
		STEM.Time                                    0.019
		History_And_Society.Transportation           0.034
		STEM.Engineering                             0.012
		Geography.Countries                          0.221
		Culture.Visual arts                          0.037
		STEM.Information science                     0.015
		Geography.Landforms                          0.022
		History_And_Society.Education                0.022
		Culture.Entertainment                        0.05
		Geography.Oceania                            0.032
		Culture.Broadcasting                         0.024
		Culture.Arts                                 0.018
		STEM.Mathematics                             0.012
		Culture.Philosophy and religion              0.026
		Culture.Performing arts                      0.044
		STEM.Science                                 0.008
		Geography.Bodies of water                    0.022
		STEM.Space                                   0.022
		STEM.Physics                                 0.019
		History_And_Society.History and society      0.023
		Assistance.Contents systems                  0.01
		History_And_Society.Business and economics   0.045
		STEM.Biology                                 0.024
		Culture.Food and drink                       0.02
		STEM.Geosciences                             0.015
		STEM.Medicine                                0.016
		Assistance.Files                             0.002
		Culture.Internet culture                     0.014
		STEM.Technology                              0.023
		Assistance.Article improvement and grading   0.002
		Culture.Sports                               0.051
		Culture.Plastic arts                         0.03
		Geography.Europe                             0.136
		Culture.Crafts and hobbies                   0.014
		-------------------------------------------  -----
	filter_rate (micro=0.918, macro=0.967):
		-------------------------------------------  -----
		Geography.Cities                             0.993
		History_And_Society.Military and warfare     0.966
		Culture.Language and literature              0.803
		Assistance.Maintenance                       0.984
		Culture.Media                                0.99
		STEM.Chemistry                               0.982
		Geography.Maps                               0.983
		STEM.Meteorology                             0.983
		History_And_Society.Politics and government  0.975
		STEM.Time                                    0.981
		History_And_Society.Transportation           0.966
		STEM.Engineering                             0.988
		Geography.Countries                          0.779
		Culture.Visual arts                          0.963
		STEM.Information science                     0.985
		Geography.Landforms                          0.978
		History_And_Society.Education                0.978
		Culture.Entertainment                        0.95
		Geography.Oceania                            0.968
		Culture.Broadcasting                         0.976
		Culture.Arts                                 0.982
		STEM.Mathematics                             0.988
		Culture.Philosophy and religion              0.974
		Culture.Performing arts                      0.956
		STEM.Science                                 0.992
		Geography.Bodies of water                    0.978
		STEM.Space                                   0.978
		STEM.Physics                                 0.981
		History_And_Society.History and society      0.977
		Assistance.Contents systems                  0.99
		History_And_Society.Business and economics   0.955
		STEM.Biology                                 0.976
		Culture.Food and drink                       0.98
		STEM.Geosciences                             0.985
		STEM.Medicine                                0.984
		Assistance.Files                             0.998
		Culture.Internet culture                     0.986
		STEM.Technology                              0.977
		Assistance.Article improvement and grading   0.998
		Culture.Sports                               0.949
		Culture.Plastic arts                         0.97
		Geography.Europe                             0.864
		Culture.Crafts and hobbies                   0.986
		-------------------------------------------  -----
	recall (micro=0.576, macro=0.553):
		-------------------------------------------  -----
		Geography.Cities                             0.627
		History_And_Society.Military and warfare     0.63
		Culture.Language and literature              0.726
		Assistance.Maintenance                       0.217
		Culture.Media                                0.294
		STEM.Chemistry                               0.627
		Geography.Maps                               0.579
		STEM.Meteorology                             0.767
		History_And_Society.Politics and government  0.385
		STEM.Time                                    0.683
		History_And_Society.Transportation           0.683
		STEM.Engineering                             0.371
		Geography.Countries                          0.599
		Culture.Visual arts                          0.56
		STEM.Information science                     0.576
		Geography.Landforms                          0.799
		History_And_Society.Education                0.607
		Culture.Entertainment                        0.658
		Geography.Oceania                            0.611
		Culture.Broadcasting                         0.569
		Culture.Arts                                 0.726
		STEM.Mathematics                             0.649
		Culture.Philosophy and religion              0.44
		Culture.Performing arts                      0.792
		STEM.Science                                 0.252
		Geography.Bodies of water                    0.773
		STEM.Space                                   0.82
		STEM.Physics                                 0.533
		History_And_Society.History and society      0.196
		Assistance.Contents systems                  0.35
		History_And_Society.Business and economics   0.497
		STEM.Biology                                 0.569
		Culture.Food and drink                       0.69
		STEM.Geosciences                             0.59
		STEM.Medicine                                0.57
		Assistance.Files                             0.06
		Culture.Internet culture                     0.505
		STEM.Technology                              0.348
		Assistance.Article improvement and grading   0.328
		Culture.Sports                               0.819
		Culture.Plastic arts                         0.571
		Geography.Europe                             0.582
		Culture.Crafts and hobbies                   0.573
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.994):
		-------------------------------------------  -----
		Geography.Cities                             0.999
		History_And_Society.Military and warfare     0.995
		Culture.Language and literature              0.962
		Assistance.Maintenance                       0.997
		Culture.Media                                0.997
		STEM.Chemistry                               0.997
		Geography.Maps                               0.999
		STEM.Meteorology                             0.999
		History_And_Society.Politics and government  0.993
		STEM.Time                                    0.999
		History_And_Society.Transportation           0.996
		STEM.Engineering                             0.997
		Geography.Countries                          0.93
		Culture.Visual arts                          0.993
		STEM.Information science                     0.999
		Geography.Landforms                          0.999
		History_And_Society.Education                0.997
		Culture.Entertainment                        0.993
		Geography.Oceania                            0.997
		Culture.Broadcasting                         0.995
		Culture.Arts                                 0.999
		STEM.Mathematics                             0.999
		Culture.Philosophy and religion              0.994
		Culture.Performing arts                      0.995
		STEM.Science                                 0.998
		Geography.Bodies of water                    0.998
		STEM.Space                                   0.999
		STEM.Physics                                 0.996
		History_And_Society.History and society      0.993
		Assistance.Contents systems                  0.998
		History_And_Society.Business and economics   0.99
		STEM.Biology                                 0.997
		Culture.Food and drink                       0.998
		STEM.Geosciences                             0.999
		STEM.Medicine                                0.997
		Assistance.Files                             0.998
		Culture.Internet culture                     0.997
		STEM.Technology                              0.993
		Assistance.Article improvement and grading   0.999
		Culture.Sports                               0.995
		Culture.Plastic arts                         0.995
		Geography.Europe                             0.963
		Culture.Crafts and hobbies                   0.999
		-------------------------------------------  -----
	precision (micro=0.826, macro=0.816):
		-------------------------------------------  -----
		Geography.Cities                             0.823
		History_And_Society.Military and warfare     0.863
		Culture.Language and literature              0.853
		Assistance.Maintenance                       0.811
		Culture.Media                                0.697
		STEM.Chemistry                               0.845
		Geography.Maps                               0.957
		STEM.Meteorology                             0.952
		History_And_Society.Politics and government  0.746
		STEM.Time                                    0.941
		History_And_Society.Transportation           0.885
		STEM.Engineering                             0.77
		Geography.Countries                          0.773
		Culture.Visual arts                          0.825
		STEM.Information science                     0.914
		Geography.Landforms                          0.934
		History_And_Society.Education                0.865
		Culture.Entertainment                        0.866
		Geography.Oceania                            0.923
		Culture.Broadcasting                         0.79
		Culture.Arts                                 0.94
		STEM.Mathematics                             0.917
		Culture.Philosophy and religion              0.778
		Culture.Performing arts                      0.892
		STEM.Science                                 0.781
		Geography.Bodies of water                    0.918
		STEM.Space                                   0.949
		STEM.Physics                                 0.788
		History_And_Society.History and society      0.715
		Assistance.Contents systems                  0.816
		History_And_Society.Business and economics   0.791
		STEM.Biology                                 0.866
		Culture.Food and drink                       0.907
		STEM.Geosciences                             0.906
		STEM.Medicine                                0.813
		Assistance.Files                             0.133
		Culture.Internet culture                     0.814
		STEM.Technology                              0.697
		Assistance.Article improvement and grading   0.171
		Culture.Sports                               0.911
		Culture.Plastic arts                         0.841
		Geography.Europe                             0.777
		Culture.Crafts and hobbies                   0.948
		-------------------------------------------  -----
	!precision (micro=0.949, macro=0.978):
		-------------------------------------------  -----
		Geography.Cities                             0.996
		History_And_Society.Military and warfare     0.982
		Culture.Language and literature              0.921
		Assistance.Maintenance                       0.953
		Culture.Media                                0.983
		STEM.Chemistry                               0.991
		Geography.Maps                               0.988
		STEM.Meteorology                             0.995
		History_And_Society.Politics and government  0.97
		STEM.Time                                    0.992
		History_And_Society.Transportation           0.986
		STEM.Engineering                             0.984
		Geography.Countries                          0.853
		Culture.Visual arts                          0.975
		STEM.Information science                     0.99
		Geography.Landforms                          0.995
		History_And_Society.Education                0.987
		Culture.Entertainment                        0.976
		Geography.Oceania                            0.981
		Culture.Broadcasting                         0.985
		Culture.Arts                                 0.993
		STEM.Mathematics                             0.994
		Culture.Philosophy and religion              0.974
		Culture.Performing arts                      0.989
		STEM.Science                                 0.981
		Geography.Bodies of water                    0.994
		STEM.Space                                   0.995
		STEM.Physics                                 0.987
		History_And_Society.History and society      0.932
		Assistance.Contents systems                  0.985
		History_And_Society.Business and economics   0.962
		STEM.Biology                                 0.984
		Culture.Food and drink                       0.992
		STEM.Geosciences                             0.99
		STEM.Medicine                                0.99
		Assistance.Files                             0.996
		Culture.Internet culture                     0.989
		STEM.Technology                              0.97
		Assistance.Article improvement and grading   0.999
		Culture.Sports                               0.989
		Culture.Plastic arts                         0.981
		Geography.Europe                             0.912
		Culture.Crafts and hobbies                   0.99
		-------------------------------------------  -----
	f1 (micro=0.669, macro=0.649):
		-------------------------------------------  -----
		Geography.Cities                             0.712
		History_And_Society.Military and warfare     0.729
		Culture.Language and literature              0.784
		Assistance.Maintenance                       0.342
		Culture.Media                                0.413
		STEM.Chemistry                               0.72
		Geography.Maps                               0.721
		STEM.Meteorology                             0.85
		History_And_Society.Politics and government  0.508
		STEM.Time                                    0.791
		History_And_Society.Transportation           0.771
		STEM.Engineering                             0.501
		Geography.Countries                          0.675
		Culture.Visual arts                          0.668
		STEM.Information science                     0.707
		Geography.Landforms                          0.862
		History_And_Society.Education                0.713
		Culture.Entertainment                        0.748
		Geography.Oceania                            0.735
		Culture.Broadcasting                         0.661
		Culture.Arts                                 0.819
		STEM.Mathematics                             0.76
		Culture.Philosophy and religion              0.562
		Culture.Performing arts                      0.839
		STEM.Science                                 0.381
		Geography.Bodies of water                    0.839
		STEM.Space                                   0.88
		STEM.Physics                                 0.636
		History_And_Society.History and society      0.307
		Assistance.Contents systems                  0.49
		History_And_Society.Business and economics   0.61
		STEM.Biology                                 0.687
		Culture.Food and drink                       0.784
		STEM.Geosciences                             0.714
		STEM.Medicine                                0.67
		Assistance.Files                             0.083
		Culture.Internet culture                     0.623
		STEM.Technology                              0.465
		Assistance.Article improvement and grading   0.224
		Culture.Sports                               0.863
		Culture.Plastic arts                         0.68
		Geography.Europe                             0.666
		Culture.Crafts and hobbies                   0.714
		-------------------------------------------  -----
	!f1 (micro=0.964, macro=0.986):
		-------------------------------------------  -----
		Geography.Cities                             0.998
		History_And_Society.Military and warfare     0.989
		Culture.Language and literature              0.941
		Assistance.Maintenance                       0.974
		Culture.Media                                0.99
		STEM.Chemistry                               0.994
		Geography.Maps                               0.993
		STEM.Meteorology                             0.997
		History_And_Society.Politics and government  0.981
		STEM.Time                                    0.995
		History_And_Society.Transportation           0.991
		STEM.Engineering                             0.99
		Geography.Countries                          0.89
		Culture.Visual arts                          0.984
		STEM.Information science                     0.994
		Geography.Landforms                          0.997
		History_And_Society.Education                0.992
		Culture.Entertainment                        0.985
		Geography.Oceania                            0.989
		Culture.Broadcasting                         0.99
		Culture.Arts                                 0.996
		STEM.Mathematics                             0.996
		Culture.Philosophy and religion              0.984
		Culture.Performing arts                      0.992
		STEM.Science                                 0.989
		Geography.Bodies of water                    0.996
		STEM.Space                                   0.997
		STEM.Physics                                 0.991
		History_And_Society.History and society      0.961
		Assistance.Contents systems                  0.991
		History_And_Society.Business and economics   0.976
		STEM.Biology                                 0.99
		Culture.Food and drink                       0.995
		STEM.Geosciences                             0.994
		STEM.Medicine                                0.993
		Assistance.Files                             0.997
		Culture.Internet culture                     0.993
		STEM.Technology                              0.981
		Assistance.Article improvement and grading   0.999
		Culture.Sports                               0.992
		Culture.Plastic arts                         0.988
		Geography.Europe                             0.937
		Culture.Crafts and hobbies                   0.995
		-------------------------------------------  -----
	accuracy (micro=0.941, macro=0.974):
		-------------------------------------------  -----
		Geography.Cities                             0.995
		History_And_Society.Military and warfare     0.978
		Culture.Language and literature              0.907
		Assistance.Maintenance                       0.95
		Culture.Media                                0.98
		STEM.Chemistry                               0.988
		Geography.Maps                               0.987
		STEM.Meteorology                             0.994
		History_And_Society.Politics and government  0.964
		STEM.Time                                    0.991
		History_And_Society.Transportation           0.982
		STEM.Engineering                             0.981
		Geography.Countries                          0.836
		Culture.Visual arts                          0.97
		STEM.Information science                     0.988
		Geography.Landforms                          0.993
		History_And_Society.Education                0.985
		Culture.Entertainment                        0.971
		Geography.Oceania                            0.979
		Culture.Broadcasting                         0.981
		Culture.Arts                                 0.992
		STEM.Mathematics                             0.993
		Culture.Philosophy and religion              0.969
		Culture.Performing arts                      0.985
		STEM.Science                                 0.979
		Geography.Bodies of water                    0.992
		STEM.Space                                   0.994
		STEM.Physics                                 0.983
		History_And_Society.History and society      0.927
		Assistance.Contents systems                  0.983
		History_And_Society.Business and economics   0.954
		STEM.Biology                                 0.981
		Culture.Food and drink                       0.99
		STEM.Geosciences                             0.989
		STEM.Medicine                                0.987
		Assistance.Files                             0.994
		Culture.Internet culture                     0.987
		STEM.Technology                              0.964
		Assistance.Article improvement and grading   0.998
		Culture.Sports                               0.985
		Culture.Plastic arts                         0.976
		Geography.Europe                             0.894
		Culture.Crafts and hobbies                   0.989
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.006):
		-------------------------------------------  -----
		Geography.Cities                             0.001
		History_And_Society.Military and warfare     0.005
		Culture.Language and literature              0.038
		Assistance.Maintenance                       0.003
		Culture.Media                                0.003
		STEM.Chemistry                               0.003
		Geography.Maps                               0.001
		STEM.Meteorology                             0.001
		History_And_Society.Politics and government  0.007
		STEM.Time                                    0.001
		History_And_Society.Transportation           0.004
		STEM.Engineering                             0.003
		Geography.Countries                          0.07
		Culture.Visual arts                          0.007
		STEM.Information science                     0.001
		Geography.Landforms                          0.001
		History_And_Society.Education                0.003
		Culture.Entertainment                        0.007
		Geography.Oceania                            0.003
		Culture.Broadcasting                         0.005
		Culture.Arts                                 0.001
		STEM.Mathematics                             0.001
		Culture.Philosophy and religion              0.006
		Culture.Performing arts                      0.005
		STEM.Science                                 0.002
		Geography.Bodies of water                    0.002
		STEM.Space                                   0.001
		STEM.Physics                                 0.004
		History_And_Society.History and society      0.007
		Assistance.Contents systems                  0.002
		History_And_Society.Business and economics   0.01
		STEM.Biology                                 0.003
		Culture.Food and drink                       0.002
		STEM.Geosciences                             0.001
		STEM.Medicine                                0.003
		Assistance.Files                             0.002
		Culture.Internet culture                     0.003
		STEM.Technology                              0.007
		Assistance.Article improvement and grading   0.001
		Culture.Sports                               0.005
		Culture.Plastic arts                         0.005
		Geography.Europe                             0.037
		Culture.Crafts and hobbies                   0.001
		-------------------------------------------  -----
	roc_auc (micro=0.942, macro=0.949):
		-------------------------------------------  -----
		Geography.Cities                             0.973
		History_And_Society.Military and warfare     0.968
		Culture.Language and literature              0.95
		Assistance.Maintenance                       0.835
		Culture.Media                                0.949
		STEM.Chemistry                               0.98
		Geography.Maps                               0.969
		STEM.Meteorology                             0.987
		History_And_Society.Politics and government  0.941
		STEM.Time                                    0.971
		History_And_Society.Transportation           0.976
		STEM.Engineering                             0.956
		Geography.Countries                          0.893
		Culture.Visual arts                          0.968
		STEM.Information science                     0.969
		Geography.Landforms                          0.987
		History_And_Society.Education                0.968
		Culture.Entertainment                        0.971
		Geography.Oceania                            0.964
		Culture.Broadcasting                         0.971
		Culture.Arts                                 0.985
		STEM.Mathematics                             0.981
		Culture.Philosophy and religion              0.936
		Culture.Performing arts                      0.983
		STEM.Science                                 0.934
		Geography.Bodies of water                    0.986
		STEM.Space                                   0.987
		STEM.Physics                                 0.975
		History_And_Society.History and society      0.868
		Assistance.Contents systems                  0.949
		History_And_Society.Business and economics   0.949
		STEM.Biology                                 0.958
		Culture.Food and drink                       0.976
		STEM.Geosciences                             0.972
		STEM.Medicine                                0.972
		Assistance.Files                             0.768
		Culture.Internet culture                     0.97
		STEM.Technology                              0.941
		Assistance.Article improvement and grading   0.735
		Culture.Sports                               0.976
		Culture.Plastic arts                         0.966
		Geography.Europe                             0.929
		Culture.Crafts and hobbies                   0.961
		-------------------------------------------  -----
	pr_auc (micro=0.761, macro=0.727):
		-------------------------------------------  -----
		Geography.Cities                             0.746
		History_And_Society.Military and warfare     0.813
		Culture.Language and literature              0.87
		Assistance.Maintenance                       0.444
		Culture.Media                                0.492
		STEM.Chemistry                               0.796
		Geography.Maps                               0.834
		STEM.Meteorology                             0.922
		History_And_Society.Politics and government  0.61
		STEM.Time                                    0.867
		History_And_Society.Transportation           0.863
		STEM.Engineering                             0.589
		Geography.Countries                          0.775
		Culture.Visual arts                          0.772
		STEM.Information science                     0.794
		Geography.Landforms                          0.928
		History_And_Society.Education                0.774
		Culture.Entertainment                        0.845
		Geography.Oceania                            0.838
		Culture.Broadcasting                         0.743
		Culture.Arts                                 0.906
		STEM.Mathematics                             0.851
		Culture.Philosophy and religion              0.623
		Culture.Performing arts                      0.921
		STEM.Science                                 0.507
		Geography.Bodies of water                    0.914
		STEM.Space                                   0.936
		STEM.Physics                                 0.717
		History_And_Society.History and society      0.482
		Assistance.Contents systems                  0.598
		History_And_Society.Business and economics   0.712
		STEM.Biology                                 0.742
		Culture.Food and drink                       0.854
		STEM.Geosciences                             0.801
		STEM.Medicine                                0.742
		Assistance.Files                             0.035
		Culture.Internet culture                     0.689
		STEM.Technology                              0.547
		Assistance.Article improvement and grading   0.097
		Culture.Sports                               0.914
		Culture.Plastic arts                         0.785
		Geography.Europe                             0.768
		Culture.Crafts and hobbies                   0.807
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'Culture.Performing arts': 'number', 'Geography.Cities': 'number', 'History_And_Society.Military and warfare': 'number', 'Culture.Language and literature': 'number', 'Assistance.Maintenance': 'number', 'Culture.Media': 'number', 'STEM.Chemistry': 'number', 'Geography.Maps': 'number', 'STEM.Meteorology': 'number', 'History_And_Society.Politics and government': 'number', 'STEM.Time': 'number', 'History_And_Society.Transportation': 'number', 'STEM.Engineering': 'number', 'STEM.Geosciences': 'number', 'Culture.Visual arts': 'number', 'STEM.Information science': 'number', 'Geography.Landforms': 'number', 'History_And_Society.Education': 'number', 'Culture.Entertainment': 'number', 'Geography.Oceania': 'number', 'Culture.Broadcasting': 'number', 'Culture.Arts': 'number', 'STEM.Mathematics': 'number', 'Culture.Philosophy and religion': 'number', 'Geography.Countries': 'number', 'STEM.Science': 'number', 'Geography.Bodies of water': 'number', 'STEM.Space': 'number', 'STEM.Physics': 'number', 'Assistance.Contents systems': 'number', 'History_And_Society.Business and economics': 'number', 'STEM.Biology': 'number', 'Culture.Food and drink': 'number', 'History_And_Society.History and society': 'number', 'STEM.Medicine': 'number', 'Assistance.Files': 'number', 'Culture.Internet culture': 'number', 'STEM.Technology': 'number', 'Assistance.Article improvement and grading': 'number', 'Culture.Sports': 'number', 'Culture.Plastic arts': 'number', 'Geography.Europe': 'number', 'Culture.Crafts and hobbies': 'number'}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability'}

