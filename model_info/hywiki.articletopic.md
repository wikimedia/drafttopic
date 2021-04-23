Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2 (2021-01-30)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul 25 2020 13:03:44')
	 - python_compiler: 'GCC 8.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.7.3'
	 - release: '4.19.0-14-amd64'
	
	Statistics:
	counts (n=55551):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15686  -->  14429  1257   647  39218
			'Culture.Biography.Women'                       4518  -->   3350  1168   476  50557
			'Culture.Food and drink'                        1662  -->   1335   327   105  53784
			'Culture.Internet culture'                      2507  -->   2098   409   144  52900
			'Culture.Linguistics'                           1693  -->   1244   449    66  53792
			'Culture.Literature'                            5298  -->   4042  1256   486  49767
			'Culture.Media.Books'                           1758  -->   1483   275   100  53693
			'Culture.Media.Entertainment'                   2153  -->   1049  1104   175  53223
			'Culture.Media.Films'                           3018  -->   2658   360   122  52411
			'Culture.Media.Media*'                         13233  -->  11667  1566  1138  41180
			'Culture.Media.Music'                           3428  -->   2921   507   239  51884
			'Culture.Media.Radio'                            233  -->    170    63    28  55290
			'Culture.Media.Software'                        2201  -->   2065   136   162  53188
			'Culture.Media.Television'                      2078  -->   1685   393   102  53371
			'Culture.Media.Video games'                      766  -->    728    38    16  54769
			'Culture.Performing arts'                       1734  -->   1203   531   121  53696
			'Culture.Philosophy and religion'               3901  -->   2179  1722   366  51284
			'Culture.Sports'                                3288  -->   2775   513    95  52168
			'Culture.Visual arts.Architecture'              2452  -->   1945   507   239  52860
			'Culture.Visual arts.Comics and Anime'          1071  -->    909   162    44  54436
			'Culture.Visual arts.Fashion'                    820  -->    610   210    45  54686
			'Culture.Visual arts.Visual arts*'              5439  -->   4133  1306   482  49630
			'Geography.Geographical'                        4862  -->   3583  1279   608  50081
			'Geography.Regions.Africa.Africa*'              3298  -->   2034  1264   186  52067
			'Geography.Regions.Africa.Central Africa'        401  -->    261   140    32  55118
			'Geography.Regions.Africa.Eastern Africa'        256  -->    188    68    25  55270
			'Geography.Regions.Africa.Northern Africa'      1335  -->    896   439    93  54123
			'Geography.Regions.Africa.Southern Africa'       605  -->    466   139    14  54932
			'Geography.Regions.Africa.Western Africa'        140  -->     99    41    39  55372
			'Geography.Regions.Americas.Central America'    1256  -->    585   671    51  54244
			'Geography.Regions.Americas.North America'      5910  -->   4274  1636   778  48863
			'Geography.Regions.Americas.South America'      1669  -->   1311   358    62  53820
			'Geography.Regions.Asia.Asia*'                 12149  -->   9899  2250  1078  42324
			'Geography.Regions.Asia.Central Asia'           1088  -->    718   370    68  54395
			'Geography.Regions.Asia.East Asia'              2652  -->   2201   451   100  52799
			'Geography.Regions.Asia.North Asia'             2562  -->   1910   652   333  52656
			'Geography.Regions.Asia.South Asia'             1924  -->   1380   544    65  53562
			'Geography.Regions.Asia.Southeast Asia'         1456  -->    774   682    55  54040
			'Geography.Regions.Asia.West Asia'              4499  -->   3564   935   369  50683
			'Geography.Regions.Europe.Eastern Europe'       4478  -->   3397  1081   396  50677
			'Geography.Regions.Europe.Europe*'             16951  -->  13906  3045  1930  36670
			'Geography.Regions.Europe.Northern Europe'      4245  -->   3158  1087   315  50991
			'Geography.Regions.Europe.Southern Europe'      4409  -->   3414   995   289  50853
			'Geography.Regions.Europe.Western Europe'       4936  -->   3955   981   396  50219
			'Geography.Regions.Oceania'                     1674  -->   1025   649    72  53805
			'History and Society.Business and economics'    3475  -->   2362  1113   297  51779
			'History and Society.Education'                 1893  -->   1199   694   125  53533
			'History and Society.History'                   5858  -->   3535  2323   743  48950
			'History and Society.Military and warfare'      5200  -->   3672  1528   626  49725
			'History and Society.Politics and government'   4691  -->   2637  2054   481  50379
			'History and Society.Society'                   7986  -->   4395  3591   744  46821
			'History and Society.Transportation'            2514  -->   2168   346    85  52952
			'STEM.Biology'                                  3086  -->   2423   663   156  52309
			'STEM.Chemistry'                                1651  -->   1400   251   130  53770
			'STEM.Computing'                                2282  -->   1963   319   168  53101
			'STEM.Earth and environment'                    1861  -->   1308   553   120  53570
			'STEM.Engineering'                              2812  -->   2190   622   200  52539
			'STEM.Libraries & Information'                   503  -->    391   112    37  55011
			'STEM.Mathematics'                               592  -->    492   100    30  54929
			'STEM.Medicine & Health'                        2084  -->   1592   492   140  53327
			'STEM.Physics'                                  1667  -->   1315   352   142  53742
			'STEM.STEM*'                                   16786  -->  15011  1775   848  37917
			'STEM.Space'                                    2077  -->   1950   127    39  53435
			'STEM.Technology'                               4483  -->   3448  1035   498  50570
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.282         0.123
		Culture.Biography.Women                         0.081         0.015
		Culture.Food and drink                          0.03          0.002
		Culture.Internet culture                        0.045         0.003
		Culture.Linguistics                             0.03          0.007
		Culture.Literature                              0.095         0.015
		Culture.Media.Books                             0.032         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.054         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.062         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.014         0.003
		Culture.Performing arts                         0.031         0.003
		Culture.Philosophy and religion                 0.07          0.011
		Culture.Sports                                  0.059         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.019         0.002
		Culture.Visual arts.Fashion                     0.015         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.088         0.024
		Geography.Regions.Africa.Africa*                0.059         0.008
		Geography.Regions.Africa.Central Africa         0.007         0.001
		Geography.Regions.Africa.Eastern Africa         0.005         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.03          0.006
		Geography.Regions.Asia.Asia*                    0.219         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.048         0.011
		Geography.Regions.Asia.North Asia               0.046         0.001
		Geography.Regions.Asia.South Asia               0.035         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.081         0.011
		Geography.Regions.Europe.Eastern Europe         0.081         0.013
		Geography.Regions.Europe.Europe*                0.305         0.076
		Geography.Regions.Europe.Northern Europe        0.076         0.031
		Geography.Regions.Europe.Southern Europe        0.079         0.013
		Geography.Regions.Europe.Western Europe         0.089         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.105         0.011
		History and Society.Military and warfare        0.094         0.014
		History and Society.Politics and government     0.084         0.028
		History and Society.Society                     0.144         0.013
		History and Society.Transportation              0.045         0.015
		STEM.Biology                                    0.056         0.034
		STEM.Chemistry                                  0.03          0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.034         0.005
		STEM.Engineering                                0.051         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.011         0
		STEM.Medicine & Health                          0.038         0.006
		STEM.Physics                                    0.03          0.001
		STEM.STEM*                                      0.302         0.069
		STEM.Space                                      0.037         0.006
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.025
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.062
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.016
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.109
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.021
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.025
		History and Society.Society                  0.022
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.938
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.891
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.979
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.975
		History and Society.Society                  0.978
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.795, macro=0.753):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.92
		Culture.Biography.Women                      0.741
		Culture.Food and drink                       0.803
		Culture.Internet culture                     0.837
		Culture.Linguistics                          0.735
		Culture.Literature                           0.763
		Culture.Media.Books                          0.844
		Culture.Media.Entertainment                  0.487
		Culture.Media.Films                          0.881
		Culture.Media.Media*                         0.882
		Culture.Media.Music                          0.852
		Culture.Media.Radio                          0.73
		Culture.Media.Software                       0.938
		Culture.Media.Television                     0.811
		Culture.Media.Video games                    0.95
		Culture.Performing arts                      0.694
		Culture.Philosophy and religion              0.559
		Culture.Sports                               0.844
		Culture.Visual arts.Architecture             0.793
		Culture.Visual arts.Comics and Anime         0.849
		Culture.Visual arts.Fashion                  0.744
		Culture.Visual arts.Visual arts*             0.76
		Geography.Geographical                       0.737
		Geography.Regions.Africa.Africa*             0.617
		Geography.Regions.Africa.Central Africa      0.651
		Geography.Regions.Africa.Eastern Africa      0.734
		Geography.Regions.Africa.Northern Africa     0.671
		Geography.Regions.Africa.Southern Africa     0.77
		Geography.Regions.Africa.Western Africa      0.707
		Geography.Regions.Americas.Central America   0.466
		Geography.Regions.Americas.North America     0.723
		Geography.Regions.Americas.South America     0.786
		Geography.Regions.Asia.Asia*                 0.815
		Geography.Regions.Asia.Central Asia          0.66
		Geography.Regions.Asia.East Asia             0.83
		Geography.Regions.Asia.North Asia            0.746
		Geography.Regions.Asia.South Asia            0.717
		Geography.Regions.Asia.Southeast Asia        0.532
		Geography.Regions.Asia.West Asia             0.792
		Geography.Regions.Europe.Eastern Europe      0.759
		Geography.Regions.Europe.Europe*             0.82
		Geography.Regions.Europe.Northern Europe     0.744
		Geography.Regions.Europe.Southern Europe     0.774
		Geography.Regions.Europe.Western Europe      0.801
		Geography.Regions.Oceania                    0.612
		History and Society.Business and economics   0.68
		History and Society.Education                0.633
		History and Society.History                  0.603
		History and Society.Military and warfare     0.706
		History and Society.Politics and government  0.562
		History and Society.Society                  0.55
		History and Society.Transportation           0.862
		STEM.Biology                                 0.785
		STEM.Chemistry                               0.848
		STEM.Computing                               0.86
		STEM.Earth and environment                   0.703
		STEM.Engineering                             0.779
		STEM.Libraries & Information                 0.777
		STEM.Mathematics                             0.831
		STEM.Medicine & Health                       0.764
		STEM.Physics                                 0.789
		STEM.STEM*                                   0.894
		STEM.Space                                   0.939
		STEM.Technology                              0.769
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.991
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.717, macro=0.597):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.888
		Culture.Biography.Women                      0.54
		Culture.Food and drink                       0.504
		Culture.Internet culture                     0.52
		Culture.Linguistics                          0.816
		Culture.Literature                           0.554
		Culture.Media.Books                          0.647
		Culture.Media.Entertainment                  0.348
		Culture.Media.Films                          0.801
		Culture.Media.Media*                         0.671
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.757
		Culture.Media.Software                       0.291
		Culture.Media.Television                     0.791
		Culture.Media.Video games                    0.895
		Culture.Performing arts                      0.472
		Culture.Philosophy and religion              0.459
		Culture.Sports                               0.973
		Culture.Visual arts.Architecture             0.653
		Culture.Visual arts.Comics and Anime         0.698
		Culture.Visual arts.Fashion                  0.423
		Culture.Visual arts.Visual arts*             0.595
		Geography.Geographical                       0.597
		Geography.Regions.Africa.Africa*             0.577
		Geography.Regions.Africa.Central Africa      0.415
		Geography.Regions.Africa.Eastern Africa      0.425
		Geography.Regions.Africa.Northern Africa     0.325
		Geography.Regions.Africa.Southern Africa     0.781
		Geography.Regions.Africa.Western Africa      0.407
		Geography.Regions.Americas.Central America   0.621
		Geography.Regions.Americas.North America     0.76
		Geography.Regions.Americas.South America     0.812
		Geography.Regions.Asia.Asia*                 0.61
		Geography.Regions.Asia.Central Asia          0.314
		Geography.Regions.Asia.East Asia             0.835
		Geography.Regions.Asia.North Asia            0.099
		Geography.Regions.Asia.South Asia            0.901
		Geography.Regions.Asia.Southeast Asia        0.76
		Geography.Regions.Asia.West Asia             0.547
		Geography.Regions.Europe.Eastern Europe      0.56
		Geography.Regions.Europe.Europe*             0.575
		Geography.Regions.Europe.Northern Europe     0.793
		Geography.Regions.Europe.Southern Europe     0.644
		Geography.Regions.Europe.Western Europe      0.667
		Geography.Regions.Oceania                    0.876
		History and Society.Business and economics   0.548
		History and Society.Education                0.668
		History and Society.History                  0.307
		History and Society.Military and warfare     0.448
		History and Society.Politics and government  0.633
		History and Society.Society                  0.31
		History and Society.Transportation           0.892
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.354
		STEM.Computing                               0.424
		STEM.Earth and environment                   0.589
		STEM.Engineering                             0.519
		STEM.Libraries & Information                 0.418
		STEM.Mathematics                             0.388
		STEM.Medicine & Health                       0.653
		STEM.Physics                                 0.203
		STEM.STEM*                                   0.752
		STEM.Space                                   0.886
		STEM.Technology                              0.289
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       1
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.987
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.746, macro=0.647):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.904
		Culture.Biography.Women                      0.625
		Culture.Food and drink                       0.62
		Culture.Internet culture                     0.641
		Culture.Linguistics                          0.773
		Culture.Literature                           0.642
		Culture.Media.Books                          0.732
		Culture.Media.Entertainment                  0.406
		Culture.Media.Films                          0.839
		Culture.Media.Media*                         0.762
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.743
		Culture.Media.Software                       0.444
		Culture.Media.Television                     0.801
		Culture.Media.Video games                    0.922
		Culture.Performing arts                      0.562
		Culture.Philosophy and religion              0.504
		Culture.Sports                               0.904
		Culture.Visual arts.Architecture             0.716
		Culture.Visual arts.Comics and Anime         0.766
		Culture.Visual arts.Fashion                  0.539
		Culture.Visual arts.Visual arts*             0.668
		Geography.Geographical                       0.66
		Geography.Regions.Africa.Africa*             0.596
		Geography.Regions.Africa.Central Africa      0.507
		Geography.Regions.Africa.Eastern Africa      0.538
		Geography.Regions.Africa.Northern Africa     0.438
		Geography.Regions.Africa.Southern Africa     0.775
		Geography.Regions.Africa.Western Africa      0.517
		Geography.Regions.Americas.Central America   0.532
		Geography.Regions.Americas.North America     0.741
		Geography.Regions.Americas.South America     0.799
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.426
		Geography.Regions.Asia.East Asia             0.833
		Geography.Regions.Asia.North Asia            0.175
		Geography.Regions.Asia.South Asia            0.799
		Geography.Regions.Asia.Southeast Asia        0.625
		Geography.Regions.Asia.West Asia             0.647
		Geography.Regions.Europe.Eastern Europe      0.644
		Geography.Regions.Europe.Europe*             0.676
		Geography.Regions.Europe.Northern Europe     0.767
		Geography.Regions.Europe.Southern Europe     0.703
		Geography.Regions.Europe.Western Europe      0.728
		Geography.Regions.Oceania                    0.721
		History and Society.Business and economics   0.607
		History and Society.Education                0.65
		History and Society.History                  0.407
		History and Society.Military and warfare     0.548
		History and Society.Politics and government  0.595
		History and Society.Society                  0.397
		History and Society.Transportation           0.877
		STEM.Biology                                 0.839
		STEM.Chemistry                               0.5
		STEM.Computing                               0.568
		STEM.Earth and environment                   0.641
		STEM.Engineering                             0.623
		STEM.Libraries & Information                 0.544
		STEM.Mathematics                             0.529
		STEM.Medicine & Health                       0.704
		STEM.Physics                                 0.323
		STEM.STEM*                                   0.817
		STEM.Space                                   0.912
		STEM.Technology                              0.42
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.989
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.981
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.978
		History and Society.Society                  0.979
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.016
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.025
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.008
		Geography.Regions.Europe.Europe*             0.05
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.015
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.009
		History and Society.Society                  0.016
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.975, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.978
		Culture.Literature                           0.976
		Culture.Media.Books                          0.987
		Culture.Media.Entertainment                  0.969
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.916
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.979
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.986
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.982
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.944
		Geography.Regions.Africa.Northern Africa     0.979
		Geography.Regions.Africa.Southern Africa     0.975
		Geography.Regions.Africa.Western Africa      0.882
		Geography.Regions.Americas.Central America   0.956
		Geography.Regions.Americas.North America     0.972
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.976
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.977
		Geography.Regions.Asia.Southeast Asia        0.962
		Geography.Regions.Asia.West Asia             0.982
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.97
		History and Society.Business and economics   0.971
		History and Society.Education                0.973
		History and Society.History                  0.953
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.957
		History and Society.Society                  0.935
		History and Society.Transportation           0.985
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.989
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.964
		STEM.Mathematics                             0.978
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.978
		STEM.Space                                   0.993
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.792, macro=0.644):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.956
		Culture.Biography.Women                      0.627
		Culture.Food and drink                       0.697
		Culture.Internet culture                     0.714
		Culture.Linguistics                          0.781
		Culture.Literature                           0.696
		Culture.Media.Books                          0.762
		Culture.Media.Entertainment                  0.332
		Culture.Media.Films                          0.897
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.894
		Culture.Media.Radio                          0.533
		Culture.Media.Software                       0.496
		Culture.Media.Television                     0.807
		Culture.Media.Video games                    0.945
		Culture.Performing arts                      0.52
		Culture.Philosophy and religion              0.506
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.729
		Culture.Visual arts.Comics and Anime         0.802
		Culture.Visual arts.Fashion                  0.439
		Culture.Visual arts.Visual arts*             0.673
		Geography.Geographical                       0.704
		Geography.Regions.Africa.Africa*             0.552
		Geography.Regions.Africa.Central Africa      0.331
		Geography.Regions.Africa.Eastern Africa      0.311
		Geography.Regions.Africa.Northern Africa     0.359
		Geography.Regions.Africa.Southern Africa     0.618
		Geography.Regions.Africa.Western Africa      0.24
		Geography.Regions.Americas.Central America   0.414
		Geography.Regions.Americas.North America     0.801
		Geography.Regions.Americas.South America     0.841
		Geography.Regions.Asia.Asia*                 0.76
		Geography.Regions.Asia.Central Asia          0.358
		Geography.Regions.Asia.East Asia             0.856
		Geography.Regions.Asia.North Asia            0.18
		Geography.Regions.Asia.South Asia            0.84
		Geography.Regions.Asia.Southeast Asia        0.576
		Geography.Regions.Asia.West Asia             0.676
		Geography.Regions.Europe.Eastern Europe      0.677
		Geography.Regions.Europe.Europe*             0.768
		Geography.Regions.Europe.Northern Europe     0.83
		Geography.Regions.Europe.Southern Europe     0.741
		Geography.Regions.Europe.Western Europe      0.798
		Geography.Regions.Oceania                    0.743
		History and Society.Business and economics   0.624
		History and Society.Education                0.603
		History and Society.History                  0.393
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.63
		History and Society.Society                  0.386
		History and Society.Transportation           0.903
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.571
		STEM.Computing                               0.579
		STEM.Earth and environment                   0.616
		STEM.Engineering                             0.659
		STEM.Libraries & Information                 0.422
		STEM.Mathematics                             0.456
		STEM.Medicine & Health                       0.686
		STEM.Physics                                 0.278
		STEM.STEM*                                   0.901
		STEM.Space                                   0.946
		STEM.Technology                              0.514
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

