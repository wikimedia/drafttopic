Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'min_impurity_decrease': 0.0, 'warm_start': False, 'min_samples_leaf': 1, 'random_state': None, 'max_depth': 5, 'min_samples_split': 2, 'n_iter_no_change': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'max_leaf_nodes': None, 'label_weights': {}, 'loss': 'deviance', 'init': None, 'validation_fraction': 0.1, 'scale': False, 'criterion': 'friedman_mse', 'verbose': 0, 'center': False, 'n_estimators': 150, 'min_impurity_split': None, 'presort': 'auto', 'tol': 0.0001, 'subsample': 1.0, 'learning_rate': 0.1, 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.6.9'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=58745):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16270  -->  14314  1956  1146  41329
			'Culture.Biography.Women'                       4005  -->   3119   886   314  54426
			'Culture.Food and drink'                        1533  -->    974   559   127  57085
			'Culture.Internet culture'                      3075  -->   2380   695   264  55406
			'Culture.Linguistics'                           1561  -->   1003   558   106  57078
			'Culture.Literature'                            4879  -->   3221  1658   518  53348
			'Culture.Media.Books'                           1629  -->   1147   482   164  56952
			'Culture.Media.Entertainment'                   2198  -->    869  1329   279  56268
			'Culture.Media.Films'                           2536  -->   1970   566   142  56067
			'Culture.Media.Media*'                         14021  -->  11835  2186  1428  43296
			'Culture.Media.Music'                           3277  -->   2592   685   303  55165
			'Culture.Media.Radio'                            386  -->    147   239    45  58314
			'Culture.Media.Software'                        2220  -->   1589   631   359  56166
			'Culture.Media.Television'                      2485  -->   1920   565   154  56106
			'Culture.Media.Video games'                     1902  -->   1676   226    65  56778
			'Culture.Performing arts'                       1439  -->    788   651   126  57180
			'Culture.Philosophy and religion'               4289  -->   2178  2111   449  54007
			'Culture.Sports'                                5768  -->   4978   790   216  52761
			'Culture.Visual arts.Architecture'              2266  -->   1492   774   253  56226
			'Culture.Visual arts.Comics and Anime'          1612  -->   1283   329    62  57071
			'Culture.Visual arts.Fashion'                   1010  -->    586   424    92  57643
			'Culture.Visual arts.Visual arts*'              5735  -->   3820  1915   473  52537
			'Geography.Geographical'                        4459  -->   2938  1521   689  53597
			'Geography.Regions.Africa.Africa*'              3998  -->   2350  1648   343  54404
			'Geography.Regions.Africa.Central Africa'        733  -->    331   402    56  57956
			'Geography.Regions.Africa.Eastern Africa'        450  -->    217   233    58  58237
			'Geography.Regions.Africa.Northern Africa'      1477  -->    821   656   140  57128
			'Geography.Regions.Africa.Southern Africa'       676  -->    285   391    46  58023
			'Geography.Regions.Africa.Western Africa'        179  -->     72   107    46  58520
			'Geography.Regions.Americas.Central America'    1320  -->    551   769    94  57331
			'Geography.Regions.Americas.North America'      5869  -->   3183  2686   950  51926
			'Geography.Regions.Americas.South America'      1504  -->    937   567   111  57130
			'Geography.Regions.Asia.Asia*'                 11599  -->   8678  2921   929  46217
			'Geography.Regions.Asia.Central Asia'           1235  -->    638   597   100  57410
			'Geography.Regions.Asia.East Asia'              2848  -->   2003   845   214  55683
			'Geography.Regions.Asia.North Asia'             3279  -->   2161  1118   329  55137
			'Geography.Regions.Asia.South Asia'             1690  -->   1045   645   102  56953
			'Geography.Regions.Asia.Southeast Asia'         1497  -->    725   772    83  57165
			'Geography.Regions.Asia.West Asia'              2665  -->   1894   771   161  55919
			'Geography.Regions.Europe.Eastern Europe'       6336  -->   4378  1958   679  51730
			'Geography.Regions.Europe.Europe*'             17720  -->  13569  4151  2797  38228
			'Geography.Regions.Europe.Northern Europe'      3935  -->   2268  1667   442  54368
			'Geography.Regions.Europe.Southern Europe'      3407  -->   2077  1330   356  54982
			'Geography.Regions.Europe.Western Europe'       5050  -->   3256  1794   713  52982
			'Geography.Regions.Oceania'                     1574  -->    911   663    98  57073
			'History and Society.Business and economics'    3485  -->   1794  1691   407  54853
			'History and Society.Education'                 1770  -->    789   981   151  56824
			'History and Society.History'                   5317  -->   2822  2495   730  52698
			'History and Society.Military and warfare'      4875  -->   3173  1702   539  53331
			'History and Society.Politics and government'   3561  -->   1469  2092   409  54775
			'History and Society.Society'                   4274  -->    930  3344   295  54176
			'History and Society.Transportation'            4362  -->   3769   593   212  54171
			'STEM.Biology'                                  3667  -->   2788   879   202  54876
			'STEM.Chemistry'                                1468  -->   1074   394   139  57138
			'STEM.Computing'                                2700  -->   2065   635   390  55655
			'STEM.Earth and environment'                    2131  -->   1300   831   168  56446
			'STEM.Engineering'                              2860  -->   2030   830   213  55672
			'STEM.Libraries & Information'                   705  -->    417   288    49  57991
			'STEM.Mathematics'                              1154  -->    798   356    82  57509
			'STEM.Medicine & Health'                        1954  -->   1132   822   201  56590
			'STEM.Physics'                                  1410  -->    820   590   154  57181
			'STEM.STEM*'                                   18386  -->  15886  2500  1296  39063
			'STEM.Space'                                    2082  -->   1843   239    61  56602
			'STEM.Technology'                               5066  -->   3494  1572   718  52961
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.277         0.121
		Culture.Biography.Women                         0.068         0.015
		Culture.Food and drink                          0.026         0.003
		Culture.Internet culture                        0.052         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.239         0.055
		Culture.Media.Music                             0.056         0.021
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.073         0.01
		Culture.Sports                                  0.098         0.061
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.017         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.076         0.021
		Geography.Regions.Africa.Africa*                0.068         0.009
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.012         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.197         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.048         0.012
		Geography.Regions.Asia.North Asia               0.056         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.045         0.012
		Geography.Regions.Europe.Eastern Europe         0.108         0.018
		Geography.Regions.Europe.Europe*                0.302         0.082
		Geography.Regions.Europe.Northern Europe        0.067         0.029
		Geography.Regions.Europe.Southern Europe        0.058         0.014
		Geography.Regions.Europe.Western Europe         0.086         0.021
		Geography.Regions.Oceania                       0.027         0.017
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.03          0.008
		History and Society.History                     0.091         0.011
		History and Society.Military and warfare        0.083         0.015
		History and Society.Politics and government     0.061         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.074         0.016
		STEM.Biology                                    0.062         0.035
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.036         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.313         0.066
		STEM.Space                                      0.035         0.004
		STEM.Technology                                 0.086         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.058
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.01
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.025
		Geography.Regions.Europe.Europe*             0.125
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.026
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.014
		History and Society.Society                  0.007
		History and Society.Transportation           0.018
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.087
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.942
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.99
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.875
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.982
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.913
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.721, macro=0.637):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.88
		Culture.Biography.Women                      0.779
		Culture.Food and drink                       0.635
		Culture.Internet culture                     0.774
		Culture.Linguistics                          0.643
		Culture.Literature                           0.66
		Culture.Media.Books                          0.704
		Culture.Media.Entertainment                  0.395
		Culture.Media.Films                          0.777
		Culture.Media.Media*                         0.844
		Culture.Media.Music                          0.791
		Culture.Media.Radio                          0.381
		Culture.Media.Software                       0.716
		Culture.Media.Television                     0.773
		Culture.Media.Video games                    0.881
		Culture.Performing arts                      0.548
		Culture.Philosophy and religion              0.508
		Culture.Sports                               0.863
		Culture.Visual arts.Architecture             0.658
		Culture.Visual arts.Comics and Anime         0.796
		Culture.Visual arts.Fashion                  0.58
		Culture.Visual arts.Visual arts*             0.666
		Geography.Geographical                       0.659
		Geography.Regions.Africa.Africa*             0.588
		Geography.Regions.Africa.Central Africa      0.452
		Geography.Regions.Africa.Eastern Africa      0.482
		Geography.Regions.Africa.Northern Africa     0.556
		Geography.Regions.Africa.Southern Africa     0.422
		Geography.Regions.Africa.Western Africa      0.402
		Geography.Regions.Americas.Central America   0.417
		Geography.Regions.Americas.North America     0.542
		Geography.Regions.Americas.South America     0.623
		Geography.Regions.Asia.Asia*                 0.748
		Geography.Regions.Asia.Central Asia          0.517
		Geography.Regions.Asia.East Asia             0.703
		Geography.Regions.Asia.North Asia            0.659
		Geography.Regions.Asia.South Asia            0.618
		Geography.Regions.Asia.Southeast Asia        0.484
		Geography.Regions.Asia.West Asia             0.711
		Geography.Regions.Europe.Eastern Europe      0.691
		Geography.Regions.Europe.Europe*             0.766
		Geography.Regions.Europe.Northern Europe     0.576
		Geography.Regions.Europe.Southern Europe     0.61
		Geography.Regions.Europe.Western Europe      0.645
		Geography.Regions.Oceania                    0.579
		History and Society.Business and economics   0.515
		History and Society.Education                0.446
		History and Society.History                  0.531
		History and Society.Military and warfare     0.651
		History and Society.Politics and government  0.413
		History and Society.Society                  0.218
		History and Society.Transportation           0.864
		STEM.Biology                                 0.76
		STEM.Chemistry                               0.732
		STEM.Computing                               0.765
		STEM.Earth and environment                   0.61
		STEM.Engineering                             0.71
		STEM.Libraries & Information                 0.591
		STEM.Mathematics                             0.692
		STEM.Medicine & Health                       0.579
		STEM.Physics                                 0.582
		STEM.STEM*                                   0.864
		STEM.Space                                   0.885
		STEM.Technology                              0.69
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.986
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.993
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.653, macro=0.517):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.818
		Culture.Biography.Women                      0.676
		Culture.Food and drink                       0.425
		Culture.Internet culture                     0.382
		Culture.Linguistics                          0.739
		Culture.Literature                           0.511
		Culture.Media.Books                          0.518
		Culture.Media.Entertainment                  0.243
		Culture.Media.Films                          0.784
		Culture.Media.Media*                         0.608
		Culture.Media.Music                          0.758
		Culture.Media.Radio                          0.537
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.719
		Culture.Media.Video games                    0.694
		Culture.Performing arts                      0.435
		Culture.Philosophy and religion              0.394
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.618
		Culture.Visual arts.Comics and Anime         0.64
		Culture.Visual arts.Fashion                  0.248
		Culture.Visual arts.Visual arts*             0.581
		Geography.Geographical                       0.531
		Geography.Regions.Africa.Africa*             0.448
		Geography.Regions.Africa.Central Africa      0.249
		Geography.Regions.Africa.Eastern Africa      0.197
		Geography.Regions.Africa.Northern Africa     0.237
		Geography.Regions.Africa.Southern Africa     0.413
		Geography.Regions.Africa.Western Africa      0.278
		Geography.Regions.Americas.Central America   0.472
		Geography.Regions.Americas.North America     0.672
		Geography.Regions.Americas.South America     0.691
		Geography.Regions.Asia.Asia*                 0.68
		Geography.Regions.Asia.Central Asia          0.193
		Geography.Regions.Asia.East Asia             0.695
		Geography.Regions.Asia.North Asia            0.387
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.679
		Geography.Regions.Asia.West Asia             0.747
		Geography.Regions.Europe.Eastern Europe      0.501
		Geography.Regions.Europe.Europe*             0.5
		Geography.Regions.Europe.Northern Europe     0.683
		Geography.Regions.Europe.Southern Europe     0.573
		Geography.Regions.Europe.Western Europe      0.506
		Geography.Regions.Oceania                    0.851
		History and Society.Business and economics   0.409
		History and Society.Education                0.576
		History and Society.History                  0.302
		History and Society.Military and warfare     0.505
		History and Society.Politics and government  0.482
		History and Society.Society                  0.253
		History and Society.Transportation           0.787
		STEM.Biology                                 0.882
		STEM.Chemistry                               0.34
		STEM.Computing                               0.239
		STEM.Earth and environment                   0.496
		STEM.Engineering                             0.521
		STEM.Libraries & Information                 0.326
		STEM.Mathematics                             0.185
		STEM.Medicine & Health                       0.517
		STEM.Physics                                 0.17
		STEM.STEM*                                   0.654
		STEM.Space                                   0.78
		STEM.Technology                              0.212
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.991
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.676, macro=0.551):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.848
		Culture.Biography.Women                      0.724
		Culture.Food and drink                       0.509
		Culture.Internet culture                     0.511
		Culture.Linguistics                          0.687
		Culture.Literature                           0.576
		Culture.Media.Books                          0.597
		Culture.Media.Entertainment                  0.301
		Culture.Media.Films                          0.78
		Culture.Media.Media*                         0.707
		Culture.Media.Music                          0.774
		Culture.Media.Radio                          0.446
		Culture.Media.Software                       0.22
		Culture.Media.Television                     0.745
		Culture.Media.Video games                    0.776
		Culture.Performing arts                      0.485
		Culture.Philosophy and religion              0.444
		Culture.Sports                               0.896
		Culture.Visual arts.Architecture             0.638
		Culture.Visual arts.Comics and Anime         0.709
		Culture.Visual arts.Fashion                  0.348
		Culture.Visual arts.Visual arts*             0.621
		Geography.Geographical                       0.588
		Geography.Regions.Africa.Africa*             0.508
		Geography.Regions.Africa.Central Africa      0.321
		Geography.Regions.Africa.Eastern Africa      0.28
		Geography.Regions.Africa.Northern Africa     0.332
		Geography.Regions.Africa.Southern Africa     0.417
		Geography.Regions.Africa.Western Africa      0.329
		Geography.Regions.Americas.Central America   0.443
		Geography.Regions.Americas.North America     0.6
		Geography.Regions.Americas.South America     0.655
		Geography.Regions.Asia.Asia*                 0.713
		Geography.Regions.Asia.Central Asia          0.281
		Geography.Regions.Asia.East Asia             0.699
		Geography.Regions.Asia.North Asia            0.488
		Geography.Regions.Asia.South Asia            0.717
		Geography.Regions.Asia.Southeast Asia        0.565
		Geography.Regions.Asia.West Asia             0.729
		Geography.Regions.Europe.Eastern Europe      0.581
		Geography.Regions.Europe.Europe*             0.605
		Geography.Regions.Europe.Northern Europe     0.625
		Geography.Regions.Europe.Southern Europe     0.591
		Geography.Regions.Europe.Western Europe      0.567
		Geography.Regions.Oceania                    0.689
		History and Society.Business and economics   0.456
		History and Society.Education                0.502
		History and Society.History                  0.385
		History and Society.Military and warfare     0.569
		History and Society.Politics and government  0.445
		History and Society.Society                  0.234
		History and Society.Transportation           0.824
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.464
		STEM.Computing                               0.364
		STEM.Earth and environment                   0.547
		STEM.Engineering                             0.601
		STEM.Libraries & Information                 0.421
		STEM.Mathematics                             0.292
		STEM.Medicine & Health                       0.546
		STEM.Physics                                 0.263
		STEM.STEM*                                   0.744
		STEM.Space                                   0.829
		STEM.Technology                              0.324
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.918
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.991
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.994
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.027
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.068
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.013
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.014
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.007
		History and Society.Society                  0.005
		History and Society.Transportation           0.004
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.962, macro=0.962):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.973
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.968
		Culture.Literature                           0.965
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.955
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.921
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.97
		Culture.Philosophy and religion              0.938
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.983
		Culture.Visual arts.Fashion                  0.969
		Culture.Visual arts.Visual arts*             0.96
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.956
		Geography.Regions.Africa.Central Africa      0.972
		Geography.Regions.Africa.Eastern Africa      0.948
		Geography.Regions.Africa.Northern Africa     0.963
		Geography.Regions.Africa.Southern Africa     0.948
		Geography.Regions.Africa.Western Africa      0.88
		Geography.Regions.Americas.Central America   0.951
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.961
		Geography.Regions.Asia.East Asia             0.97
		Geography.Regions.Asia.North Asia            0.961
		Geography.Regions.Asia.South Asia            0.958
		Geography.Regions.Asia.Southeast Asia        0.957
		Geography.Regions.Asia.West Asia             0.973
		Geography.Regions.Europe.Eastern Europe      0.957
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.954
		Geography.Regions.Europe.Southern Europe     0.96
		Geography.Regions.Europe.Western Europe      0.96
		Geography.Regions.Oceania                    0.962
		History and Society.Business and economics   0.951
		History and Society.Education                0.951
		History and Society.History                  0.943
		History and Society.Military and warfare     0.963
		History and Society.Politics and government  0.931
		History and Society.Society                  0.877
		History and Society.Transportation           0.984
		STEM.Biology                                 0.974
		STEM.Chemistry                               0.981
		STEM.Computing                               0.983
		STEM.Earth and environment                   0.966
		STEM.Engineering                             0.972
		STEM.Libraries & Information                 0.963
		STEM.Mathematics                             0.978
		STEM.Medicine & Health                       0.966
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.97
		STEM.Space                                   0.988
		STEM.Technology                              0.97
		-------------------------------------------  -----
	pr_auc (micro=0.717, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.916
		Culture.Biography.Women                      0.721
		Culture.Food and drink                       0.481
		Culture.Internet culture                     0.598
		Culture.Linguistics                          0.649
		Culture.Literature                           0.602
		Culture.Media.Books                          0.614
		Culture.Media.Entertainment                  0.223
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.805
		Culture.Media.Music                          0.81
		Culture.Media.Radio                          0.252
		Culture.Media.Software                       0.241
		Culture.Media.Television                     0.805
		Culture.Media.Video games                    0.814
		Culture.Performing arts                      0.44
		Culture.Philosophy and religion              0.375
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.647
		Culture.Visual arts.Comics and Anime         0.77
		Culture.Visual arts.Fashion                  0.258
		Culture.Visual arts.Visual arts*             0.651
		Geography.Geographical                       0.587
		Geography.Regions.Africa.Africa*             0.481
		Geography.Regions.Africa.Central Africa      0.148
		Geography.Regions.Africa.Eastern Africa      0.105
		Geography.Regions.Africa.Northern Africa     0.22
		Geography.Regions.Africa.Southern Africa     0.232
		Geography.Regions.Africa.Western Africa      0.122
		Geography.Regions.Americas.Central America   0.365
		Geography.Regions.Americas.North America     0.655
		Geography.Regions.Americas.South America     0.642
		Geography.Regions.Asia.Asia*                 0.767
		Geography.Regions.Asia.Central Asia          0.179
		Geography.Regions.Asia.East Asia             0.708
		Geography.Regions.Asia.North Asia            0.45
		Geography.Regions.Asia.South Asia            0.763
		Geography.Regions.Asia.Southeast Asia        0.538
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.611
		Geography.Regions.Europe.Europe*             0.666
		Geography.Regions.Europe.Northern Europe     0.658
		Geography.Regions.Europe.Southern Europe     0.593
		Geography.Regions.Europe.Western Europe      0.583
		Geography.Regions.Oceania                    0.739
		History and Society.Business and economics   0.409
		History and Society.Education                0.446
		History and Society.History                  0.358
		History and Society.Military and warfare     0.613
		History and Society.Politics and government  0.409
		History and Society.Society                  0.164
		History and Society.Transportation           0.884
		STEM.Biology                                 0.859
		STEM.Chemistry                               0.46
		STEM.Computing                               0.372
		STEM.Earth and environment                   0.534
		STEM.Engineering                             0.635
		STEM.Libraries & Information                 0.298
		STEM.Mathematics                             0.351
		STEM.Medicine & Health                       0.519
		STEM.Physics                                 0.259
		STEM.STEM*                                   0.862
		STEM.Space                                   0.88
		STEM.Technology                              0.457
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}}}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}}

