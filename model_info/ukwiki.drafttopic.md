Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'max_depth': 5, 'scale': False, 'n_estimators': 150, 'random_state': None, 'subsample': 1.0, 'warm_start': False, 'tol': 0.0001, 'presort': 'auto', 'validation_fraction': 0.1, 'init': None, 'min_impurity_decrease': 0.0, 'center': False, 'population_rates': None, 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'min_impurity_split': None, 'max_leaf_nodes': None, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_split': 2, 'learning_rate': 0.1, 'max_features': 'log2', 'label_weights': {}, 'loss': 'deviance', 'n_iter_no_change': None, 'verbose': 0}
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
	counts (n=59889):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14132  -->   7131  7001  2121  43636
			'Culture.Biography.Women'                       5057  -->   1313  3744   486  54346
			'Culture.Food and drink'                        1339  -->     92  1247    56  58494
			'Culture.Internet culture'                      3498  -->   2308  1190   282  56109
			'Culture.Linguistics'                           1439  -->    534   905   106  58344
			'Culture.Literature'                            5557  -->   1876  3681   380  53952
			'Culture.Media.Books'                           1395  -->    249  1146    70  58424
			'Culture.Media.Entertainment'                   1896  -->    522  1374   105  57888
			'Culture.Media.Films'                           2587  -->   1366  1221   231  57071
			'Culture.Media.Media*'                         13025  -->   8289  4736  1563  45301
			'Culture.Media.Music'                           2797  -->   1590  1207   314  56778
			'Culture.Media.Radio'                            267  -->    120   147    56  59566
			'Culture.Media.Software'                        2225  -->   1456   769   297  57367
			'Culture.Media.Television'                      1931  -->    673  1258   117  57841
			'Culture.Media.Video games'                     2167  -->   1761   406   117  57605
			'Culture.Performing arts'                       1336  -->    411   925    75  58478
			'Culture.Philosophy and religion'               2954  -->    256  2698    89  56846
			'Culture.Sports'                                3975  -->   2399  1576   178  55736
			'Culture.Visual arts.Architecture'              1829  -->    343  1486   138  57922
			'Culture.Visual arts.Comics and Anime'          2222  -->   1527   695   129  57538
			'Culture.Visual arts.Fashion'                   1535  -->    365  1170    74  58280
			'Culture.Visual arts.Visual arts*'              6069  -->   1907  4162   365  53455
			'Geography.Geographical'                        3869  -->   1047  2822   284  55736
			'Geography.Regions.Africa.Africa*'              5668  -->   2065  3603   584  53637
			'Geography.Regions.Africa.Central Africa'       1220  -->    174  1046    67  58602
			'Geography.Regions.Africa.Eastern Africa'        432  -->    185   247    65  59392
			'Geography.Regions.Africa.Northern Africa'      1457  -->    595   862   148  58284
			'Geography.Regions.Africa.Southern Africa'      1142  -->    361   781   106  58641
			'Geography.Regions.Africa.Western Africa'        666  -->    203   463    55  59168
			'Geography.Regions.Americas.Central America'    1553  -->    175  1378    65  58271
			'Geography.Regions.Americas.North America'      5081  -->   1931  3150   454  54354
			'Geography.Regions.Americas.South America'      2132  -->    751  1381   168  57589
			'Geography.Regions.Asia.Asia*'                 13593  -->   6383  7210  1461  44835
			'Geography.Regions.Asia.Central Asia'           1106  -->    178   928    55  58728
			'Geography.Regions.Asia.East Asia'              5491  -->   2050  3441   534  53864
			'Geography.Regions.Asia.North Asia'             1585  -->    507  1078   134  58170
			'Geography.Regions.Asia.South Asia'             1917  -->   1025   892    79  57893
			'Geography.Regions.Asia.Southeast Asia'         2615  -->    456  2159   153  57121
			'Geography.Regions.Asia.West Asia'              2106  -->   1234   872   111  57672
			'Geography.Regions.Europe.Eastern Europe'       3513  -->   1645  1868   197  56179
			'Geography.Regions.Europe.Europe*'             12470  -->   6486  5984  1435  45984
			'Geography.Regions.Europe.Northern Europe'      2803  -->    694  2109   206  56880
			'Geography.Regions.Europe.Southern Europe'      2768  -->   1272  1496   170  56951
			'Geography.Regions.Europe.Western Europe'       3888  -->   2096  1792   342  55659
			'Geography.Regions.Oceania'                     2258  -->   1083  1175   228  57403
			'History and Society.Business and economics'    3190  -->    391  2799   137  56562
			'History and Society.Education'                 1581  -->    213  1368    74  58234
			'History and Society.History'                   4149  -->    674  3475   251  55489
			'History and Society.Military and warfare'      4808  -->   1967  2841   339  54742
			'History and Society.Politics and government'   4384  -->    966  3418   250  55255
			'History and Society.Society'                   5825  -->    708  5117   175  53889
			'History and Society.Transportation'            3542  -->   2532  1010   166  56181
			'STEM.Biology'                                  7087  -->   5742  1345   136  52666
			'STEM.Chemistry'                                1422  -->    470   952   180  58287
			'STEM.Computing'                                2350  -->   1218  1132   276  57263
			'STEM.Earth and environment'                    1591  -->    276  1315    47  58251
			'STEM.Engineering'                              2941  -->   1863  1078   116  56832
			'STEM.Libraries & Information'                   479  -->    213   266    61  59349
			'STEM.Mathematics'                               909  -->    447   462    81  58899
			'STEM.Medicine & Health'                        1731  -->    530  1201   161  57997
			'STEM.Physics'                                  1367  -->    197  1170    89  58433
			'STEM.STEM*'                                   20228  -->  14462  5766  1846  37815
			'STEM.Space'                                    1563  -->    838   725    99  58227
			'STEM.Technology'                               4173  -->   1697  2476   425  55291
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.236         0.122
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.022         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.217         0.055
		Culture.Media.Music                             0.047         0.021
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.049         0.01
		Culture.Sports                                  0.066         0.061
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.026         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.095         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.085         0.064
		Geography.Regions.Americas.South America        0.036         0.007
		Geography.Regions.Asia.Asia*                    0.227         0.049
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.092         0.012
		Geography.Regions.Asia.North Asia               0.026         0.001
		Geography.Regions.Asia.South Asia               0.032         0.017
		Geography.Regions.Asia.Southeast Asia           0.044         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.014
		Geography.Regions.Europe.Europe*                0.208         0.077
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.046         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.038         0.017
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.026         0.008
		History and Society.History                     0.069         0.011
		History and Society.Military and warfare        0.08          0.015
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.097         0.013
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.118         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.007
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.338         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.04, macro=0.013):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.102
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.005
		Culture.Literature                           0.012
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.067
		Culture.Media.Music                          0.017
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.005
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.002
		Culture.Sports                               0.04
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.012
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.032
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.01
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.068
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.017
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.004
		History and Society.Education                0.002
		History and Society.History                  0.006
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.011
		History and Society.Society                  0.005
		History and Society.Transportation           0.015
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.09
		STEM.Space                                   0.004
		STEM.Technology                              0.01
		-------------------------------------------  -----
	filter_rate (micro=0.96, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.995
		Culture.Literature                           0.988
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.933
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.998
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.994
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.989
		History and Society.Society                  0.995
		History and Society.Transportation           0.985
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.91
		STEM.Space                                   0.996
		STEM.Technology                              0.99
		-------------------------------------------  -----
	recall (micro=0.468, macro=0.389):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.505
		Culture.Biography.Women                      0.26
		Culture.Food and drink                       0.069
		Culture.Internet culture                     0.66
		Culture.Linguistics                          0.371
		Culture.Literature                           0.338
		Culture.Media.Books                          0.178
		Culture.Media.Entertainment                  0.275
		Culture.Media.Films                          0.528
		Culture.Media.Media*                         0.636
		Culture.Media.Music                          0.568
		Culture.Media.Radio                          0.449
		Culture.Media.Software                       0.654
		Culture.Media.Television                     0.349
		Culture.Media.Video games                    0.813
		Culture.Performing arts                      0.308
		Culture.Philosophy and religion              0.087
		Culture.Sports                               0.604
		Culture.Visual arts.Architecture             0.188
		Culture.Visual arts.Comics and Anime         0.687
		Culture.Visual arts.Fashion                  0.238
		Culture.Visual arts.Visual arts*             0.314
		Geography.Geographical                       0.271
		Geography.Regions.Africa.Africa*             0.364
		Geography.Regions.Africa.Central Africa      0.143
		Geography.Regions.Africa.Eastern Africa      0.428
		Geography.Regions.Africa.Northern Africa     0.408
		Geography.Regions.Africa.Southern Africa     0.316
		Geography.Regions.Africa.Western Africa      0.305
		Geography.Regions.Americas.Central America   0.113
		Geography.Regions.Americas.North America     0.38
		Geography.Regions.Americas.South America     0.352
		Geography.Regions.Asia.Asia*                 0.47
		Geography.Regions.Asia.Central Asia          0.161
		Geography.Regions.Asia.East Asia             0.373
		Geography.Regions.Asia.North Asia            0.32
		Geography.Regions.Asia.South Asia            0.535
		Geography.Regions.Asia.Southeast Asia        0.174
		Geography.Regions.Asia.West Asia             0.586
		Geography.Regions.Europe.Eastern Europe      0.468
		Geography.Regions.Europe.Europe*             0.52
		Geography.Regions.Europe.Northern Europe     0.248
		Geography.Regions.Europe.Southern Europe     0.46
		Geography.Regions.Europe.Western Europe      0.539
		Geography.Regions.Oceania                    0.48
		History and Society.Business and economics   0.123
		History and Society.Education                0.135
		History and Society.History                  0.162
		History and Society.Military and warfare     0.409
		History and Society.Politics and government  0.22
		History and Society.Society                  0.122
		History and Society.Transportation           0.715
		STEM.Biology                                 0.81
		STEM.Chemistry                               0.331
		STEM.Computing                               0.518
		STEM.Earth and environment                   0.173
		STEM.Engineering                             0.633
		STEM.Libraries & Information                 0.445
		STEM.Mathematics                             0.492
		STEM.Medicine & Health                       0.306
		STEM.Physics                                 0.144
		STEM.STEM*                                   0.715
		STEM.Space                                   0.536
		STEM.Technology                              0.407
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.954
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.998
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.992
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.998
		History and Society.Education                0.999
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.995
		History and Society.Society                  0.997
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.953
		STEM.Space                                   0.998
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.588, macro=0.438):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.601
		Culture.Biography.Women                      0.31
		Culture.Food and drink                       0.157
		Culture.Internet culture                     0.333
		Culture.Linguistics                          0.626
		Culture.Literature                           0.424
		Culture.Media.Books                          0.395
		Culture.Media.Entertainment                  0.379
		Culture.Media.Films                          0.607
		Culture.Media.Media*                         0.528
		Culture.Media.Music                          0.691
		Culture.Media.Radio                          0.53
		Culture.Media.Software                       0.144
		Culture.Media.Television                     0.61
		Culture.Media.Video games                    0.542
		Culture.Performing arts                      0.426
		Culture.Philosophy and religion              0.37
		Culture.Sports                               0.925
		Culture.Visual arts.Architecture             0.465
		Culture.Visual arts.Comics and Anime         0.427
		Culture.Visual arts.Fashion                  0.145
		Culture.Visual arts.Visual arts*             0.463
		Geography.Geographical                       0.538
		Geography.Regions.Africa.Africa*             0.226
		Geography.Regions.Africa.Central Africa      0.082
		Geography.Regions.Africa.Eastern Africa      0.166
		Geography.Regions.Africa.Northern Africa     0.181
		Geography.Regions.Africa.Southern Africa     0.188
		Geography.Regions.Africa.Western Africa      0.198
		Geography.Regions.Americas.Central America   0.262
		Geography.Regions.Americas.North America     0.757
		Geography.Regions.Americas.South America     0.458
		Geography.Regions.Asia.Asia*                 0.432
		Geography.Regions.Asia.Central Asia          0.122
		Geography.Regions.Asia.East Asia             0.321
		Geography.Regions.Asia.North Asia            0.126
		Geography.Regions.Asia.South Asia            0.869
		Geography.Regions.Asia.Southeast Asia        0.293
		Geography.Regions.Asia.West Asia             0.785
		Geography.Regions.Europe.Eastern Europe      0.655
		Geography.Regions.Europe.Europe*             0.59
		Geography.Regions.Europe.Northern Europe     0.674
		Geography.Regions.Europe.Southern Europe     0.686
		Geography.Regions.Europe.Western Europe      0.651
		Geography.Regions.Oceania                    0.672
		History and Society.Business and economics   0.335
		History and Society.Education                0.462
		History and Society.History                  0.287
		History and Society.Military and warfare     0.511
		History and Society.Politics and government  0.588
		History and Society.Society                  0.338
		History and Society.Transportation           0.802
		STEM.Biology                                 0.919
		STEM.Chemistry                               0.155
		STEM.Computing                               0.236
		STEM.Earth and environment                   0.508
		STEM.Engineering                             0.645
		STEM.Libraries & Information                 0.231
		STEM.Mathematics                             0.143
		STEM.Medicine & Health                       0.42
		STEM.Physics                                 0.082
		STEM.STEM*                                   0.519
		STEM.Space                                   0.577
		STEM.Technology                              0.218
		-------------------------------------------  -----
	!precision (micro=0.976, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.933
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.995
		Culture.Literature                           0.99
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.959
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.991
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.991
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.978
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.979
		STEM.Space                                   0.998
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.505, macro=0.384):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.549
		Culture.Biography.Women                      0.283
		Culture.Food and drink                       0.096
		Culture.Internet culture                     0.443
		Culture.Linguistics                          0.466
		Culture.Literature                           0.376
		Culture.Media.Books                          0.246
		Culture.Media.Entertainment                  0.319
		Culture.Media.Films                          0.565
		Culture.Media.Media*                         0.577
		Culture.Media.Music                          0.624
		Culture.Media.Radio                          0.486
		Culture.Media.Software                       0.236
		Culture.Media.Television                     0.444
		Culture.Media.Video games                    0.65
		Culture.Performing arts                      0.357
		Culture.Philosophy and religion              0.14
		Culture.Sports                               0.73
		Culture.Visual arts.Architecture             0.267
		Culture.Visual arts.Comics and Anime         0.527
		Culture.Visual arts.Fashion                  0.18
		Culture.Visual arts.Visual arts*             0.374
		Geography.Geographical                       0.36
		Geography.Regions.Africa.Africa*             0.279
		Geography.Regions.Africa.Central Africa      0.104
		Geography.Regions.Africa.Eastern Africa      0.239
		Geography.Regions.Africa.Northern Africa     0.25
		Geography.Regions.Africa.Southern Africa     0.236
		Geography.Regions.Africa.Western Africa      0.24
		Geography.Regions.Americas.Central America   0.158
		Geography.Regions.Americas.North America     0.506
		Geography.Regions.Americas.South America     0.398
		Geography.Regions.Asia.Asia*                 0.45
		Geography.Regions.Asia.Central Asia          0.139
		Geography.Regions.Asia.East Asia             0.345
		Geography.Regions.Asia.North Asia            0.181
		Geography.Regions.Asia.South Asia            0.662
		Geography.Regions.Asia.Southeast Asia        0.219
		Geography.Regions.Asia.West Asia             0.671
		Geography.Regions.Europe.Eastern Europe      0.546
		Geography.Regions.Europe.Europe*             0.553
		Geography.Regions.Europe.Northern Europe     0.362
		Geography.Regions.Europe.Southern Europe     0.55
		Geography.Regions.Europe.Western Europe      0.59
		Geography.Regions.Oceania                    0.56
		History and Society.Business and economics   0.179
		History and Society.Education                0.209
		History and Society.History                  0.207
		History and Society.Military and warfare     0.454
		History and Society.Politics and government  0.321
		History and Society.Society                  0.179
		History and Society.Transportation           0.756
		STEM.Biology                                 0.861
		STEM.Chemistry                               0.211
		STEM.Computing                               0.324
		STEM.Earth and environment                   0.259
		STEM.Engineering                             0.639
		STEM.Libraries & Information                 0.304
		STEM.Mathematics                             0.222
		STEM.Medicine & Health                       0.354
		STEM.Physics                                 0.105
		STEM.STEM*                                   0.602
		STEM.Space                                   0.556
		STEM.Technology                              0.284
		-------------------------------------------  -----
	!f1 (micro=0.979, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.943
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.962, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.983
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.991
		Culture.Media.Media*                         0.948
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.973
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.997
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.944
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.974
		History and Society.Society                  0.985
		History and Society.Transportation           0.992
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.938
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.046
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.007
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.002
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.008
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.032
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.01
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.03
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.002
		History and Society.Education                0.001
		History and Society.History                  0.005
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.005
		History and Society.Society                  0.003
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.047
		STEM.Space                                   0.002
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.905, macro=0.908):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.884
		Culture.Biography.Women                      0.899
		Culture.Food and drink                       0.871
		Culture.Internet culture                     0.963
		Culture.Linguistics                          0.893
		Culture.Literature                           0.908
		Culture.Media.Books                          0.91
		Culture.Media.Entertainment                  0.916
		Culture.Media.Films                          0.946
		Culture.Media.Media*                         0.93
		Culture.Media.Music                          0.95
		Culture.Media.Radio                          0.867
		Culture.Media.Software                       0.969
		Culture.Media.Television                     0.927
		Culture.Media.Video games                    0.977
		Culture.Performing arts                      0.914
		Culture.Philosophy and religion              0.862
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.898
		Culture.Visual arts.Comics and Anime         0.968
		Culture.Visual arts.Fashion                  0.906
		Culture.Visual arts.Visual arts*             0.887
		Geography.Geographical                       0.893
		Geography.Regions.Africa.Africa*             0.892
		Geography.Regions.Africa.Central Africa      0.902
		Geography.Regions.Africa.Eastern Africa      0.907
		Geography.Regions.Africa.Northern Africa     0.914
		Geography.Regions.Africa.Southern Africa     0.897
		Geography.Regions.Africa.Western Africa      0.937
		Geography.Regions.Americas.Central America   0.873
		Geography.Regions.Americas.North America     0.902
		Geography.Regions.Americas.South America     0.907
		Geography.Regions.Asia.Asia*                 0.875
		Geography.Regions.Asia.Central Asia          0.888
		Geography.Regions.Asia.East Asia             0.903
		Geography.Regions.Asia.North Asia            0.926
		Geography.Regions.Asia.South Asia            0.917
		Geography.Regions.Asia.Southeast Asia        0.86
		Geography.Regions.Asia.West Asia             0.928
		Geography.Regions.Europe.Eastern Europe      0.924
		Geography.Regions.Europe.Europe*             0.892
		Geography.Regions.Europe.Northern Europe     0.885
		Geography.Regions.Europe.Southern Europe     0.918
		Geography.Regions.Europe.Western Europe      0.931
		Geography.Regions.Oceania                    0.938
		History and Society.Business and economics   0.857
		History and Society.Education                0.878
		History and Society.History                  0.874
		History and Society.Military and warfare     0.907
		History and Society.Politics and government  0.843
		History and Society.Society                  0.809
		History and Society.Transportation           0.953
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.925
		STEM.Computing                               0.951
		STEM.Earth and environment                   0.87
		STEM.Engineering                             0.935
		STEM.Libraries & Information                 0.885
		STEM.Mathematics                             0.932
		STEM.Medicine & Health                       0.906
		STEM.Physics                                 0.898
		STEM.STEM*                                   0.926
		STEM.Space                                   0.934
		STEM.Technology                              0.915
		-------------------------------------------  -----
	pr_auc (micro=0.522, macro=0.335):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.604
		Culture.Biography.Women                      0.225
		Culture.Food and drink                       0.053
		Culture.Internet culture                     0.465
		Culture.Linguistics                          0.362
		Culture.Literature                           0.364
		Culture.Media.Books                          0.154
		Culture.Media.Entertainment                  0.236
		Culture.Media.Films                          0.524
		Culture.Media.Media*                         0.615
		Culture.Media.Music                          0.628
		Culture.Media.Radio                          0.266
		Culture.Media.Software                       0.16
		Culture.Media.Television                     0.402
		Culture.Media.Video games                    0.652
		Culture.Performing arts                      0.25
		Culture.Philosophy and religion              0.119
		Culture.Sports                               0.795
		Culture.Visual arts.Architecture             0.245
		Culture.Visual arts.Comics and Anime         0.474
		Culture.Visual arts.Fashion                  0.064
		Culture.Visual arts.Visual arts*             0.345
		Geography.Geographical                       0.37
		Geography.Regions.Africa.Africa*             0.231
		Geography.Regions.Africa.Central Africa      0.032
		Geography.Regions.Africa.Eastern Africa      0.082
		Geography.Regions.Africa.Northern Africa     0.104
		Geography.Regions.Africa.Southern Africa     0.099
		Geography.Regions.Africa.Western Africa      0.091
		Geography.Regions.Americas.Central America   0.092
		Geography.Regions.Americas.North America     0.608
		Geography.Regions.Americas.South America     0.33
		Geography.Regions.Asia.Asia*                 0.459
		Geography.Regions.Asia.Central Asia          0.041
		Geography.Regions.Asia.East Asia             0.251
		Geography.Regions.Asia.North Asia            0.071
		Geography.Regions.Asia.South Asia            0.654
		Geography.Regions.Asia.Southeast Asia        0.125
		Geography.Regions.Asia.West Asia             0.647
		Geography.Regions.Europe.Eastern Europe      0.534
		Geography.Regions.Europe.Europe*             0.604
		Geography.Regions.Europe.Northern Europe     0.419
		Geography.Regions.Europe.Southern Europe     0.525
		Geography.Regions.Europe.Western Europe      0.608
		Geography.Regions.Oceania                    0.517
		History and Society.Business and economics   0.13
		History and Society.Education                0.189
		History and Society.History                  0.152
		History and Society.Military and warfare     0.42
		History and Society.Politics and government  0.325
		History and Society.Society                  0.15
		History and Society.Transportation           0.758
		STEM.Biology                                 0.836
		STEM.Chemistry                               0.099
		STEM.Computing                               0.196
		STEM.Earth and environment                   0.208
		STEM.Engineering                             0.615
		STEM.Libraries & Information                 0.129
		STEM.Mathematics                             0.078
		STEM.Medicine & Health                       0.277
		STEM.Physics                                 0.03
		STEM.STEM*                                   0.721
		STEM.Space                                   0.452
		STEM.Technology                              0.21
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

