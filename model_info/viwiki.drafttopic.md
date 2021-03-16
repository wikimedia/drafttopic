Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.8'
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
	counts (n=59996):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14008  -->  12213  1795   905  45083
			'Culture.Biography.Women'                       5105  -->   3982  1123   800  54091
			'Culture.Food and drink'                        1372  -->    899   473   127  58497
			'Culture.Internet culture'                      3477  -->   2749   728   256  56263
			'Culture.Linguistics'                           1472  -->   1109   363    78  58446
			'Culture.Literature'                            5540  -->   4098  1442   504  53952
			'Culture.Media.Books'                           1416  -->    979   437   138  58442
			'Culture.Media.Entertainment'                   1937  -->    873  1064   170  57889
			'Culture.Media.Films'                           2566  -->   1957   609   203  57227
			'Culture.Media.Media*'                         13028  -->  11118  1910  1323  45645
			'Culture.Media.Music'                           2872  -->   2374   498   181  56943
			'Culture.Media.Radio'                            274  -->    158   116    44  59678
			'Culture.Media.Software'                        2246  -->   1767   479   300  57450
			'Culture.Media.Television'                      1943  -->   1278   665   166  57887
			'Culture.Media.Video games'                     2118  -->   1896   222    72  57806
			'Culture.Performing arts'                       1354  -->    876   478   128  58514
			'Culture.Philosophy and religion'               2966  -->   1513  1453   266  56764
			'Culture.Sports'                                3832  -->   3298   534   106  56058
			'Culture.Visual arts.Architecture'              1814  -->   1261   553   170  58012
			'Culture.Visual arts.Comics and Anime'          2201  -->   1912   289    87  57708
			'Culture.Visual arts.Fashion'                   1483  -->   1163   320   109  58404
			'Culture.Visual arts.Visual arts*'              6013  -->   4343  1670   418  53565
			'Geography.Geographical'                        3953  -->   2508  1445   529  55514
			'Geography.Regions.Africa.Africa*'              5715  -->   4198  1517   505  53776
			'Geography.Regions.Africa.Central Africa'       1211  -->    722   489   131  58654
			'Geography.Regions.Africa.Eastern Africa'        450  -->    214   236    40  59506
			'Geography.Regions.Africa.Northern Africa'      1467  -->    986   481   112  58417
			'Geography.Regions.Africa.Southern Africa'      1168  -->    780   388    83  58745
			'Geography.Regions.Africa.Western Africa'        670  -->    506   164    49  59277
			'Geography.Regions.Americas.Central America'    1578  -->    874   704   125  58293
			'Geography.Regions.Americas.North America'      5362  -->   3375  1987   591  54043
			'Geography.Regions.Americas.South America'      2198  -->   1579   619   167  57631
			'Geography.Regions.Asia.Asia*'                 13666  -->  10996  2670  1204  45126
			'Geography.Regions.Asia.Central Asia'           1196  -->    881   315    81  58719
			'Geography.Regions.Asia.East Asia'              5485  -->   4173  1312   496  54015
			'Geography.Regions.Asia.North Asia'             1651  -->   1157   494   216  58129
			'Geography.Regions.Asia.South Asia'             2015  -->   1522   493   112  57869
			'Geography.Regions.Asia.Southeast Asia'         2582  -->   1681   901   198  57216
			'Geography.Regions.Asia.West Asia'              2161  -->   1648   513   121  57714
			'Geography.Regions.Europe.Eastern Europe'       3540  -->   2687   853   297  56159
			'Geography.Regions.Europe.Europe*'             12516  -->   9682  2834  1202  46278
			'Geography.Regions.Europe.Northern Europe'      2860  -->   1656  1204   247  56889
			'Geography.Regions.Europe.Southern Europe'      2800  -->   2029   771   201  56995
			'Geography.Regions.Europe.Western Europe'       4004  -->   2994  1010   237  55755
			'Geography.Regions.Oceania'                     2232  -->   1570   662   166  57598
			'History and Society.Business and economics'    3348  -->   1844  1504   348  56300
			'History and Society.Education'                 1568  -->    852   716   129  58299
			'History and Society.History'                   4494  -->   2242  2252   552  54950
			'History and Society.Military and warfare'      4968  -->   3722  1246   472  54556
			'History and Society.Politics and government'   4525  -->   2266  2259   505  54966
			'History and Society.Society'                   6042  -->   2616  3426   508  53446
			'History and Society.Transportation'            3547  -->   3183   364    91  56358
			'STEM.Biology'                                  7090  -->   6457   633   173  52733
			'STEM.Chemistry'                                1476  -->   1105   371   177  58343
			'STEM.Computing'                                2392  -->   1882   510   320  57284
			'STEM.Earth and environment'                    1628  -->   1016   612   154  58214
			'STEM.Engineering'                              2989  -->   2438   551   135  56872
			'STEM.Libraries & Information'                   479  -->    338   141    41  59476
			'STEM.Mathematics'                               932  -->    736   196    56  59008
			'STEM.Medicine & Health'                        1745  -->   1163   582   125  58126
			'STEM.Physics'                                  1338  -->    910   428   144  58514
			'STEM.STEM*'                                   20343  -->  18410  1933  1026  38627
			'STEM.Space'                                    1615  -->   1413   202    44  58337
			'STEM.Technology'                               4144  -->   2882  1262   543  55309
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.217         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.049         0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.095         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.037         0.006
		Geography.Regions.Asia.Asia*                    0.228         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.091         0.011
		Geography.Regions.Asia.North Asia               0.028         0.001
		Geography.Regions.Asia.South Asia               0.034         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.059         0.013
		Geography.Regions.Europe.Europe*                0.209         0.076
		Geography.Regions.Europe.Northern Europe        0.048         0.031
		Geography.Regions.Europe.Southern Europe        0.047         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.026         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.083         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.118         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.339         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.051, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.063
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.082
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.015
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.023
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.087
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.918
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.977
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.913
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.762, macro=0.71):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.78
		Culture.Food and drink                       0.655
		Culture.Internet culture                     0.791
		Culture.Linguistics                          0.753
		Culture.Literature                           0.74
		Culture.Media.Books                          0.691
		Culture.Media.Entertainment                  0.451
		Culture.Media.Films                          0.763
		Culture.Media.Media*                         0.853
		Culture.Media.Music                          0.827
		Culture.Media.Radio                          0.577
		Culture.Media.Software                       0.787
		Culture.Media.Television                     0.658
		Culture.Media.Video games                    0.895
		Culture.Performing arts                      0.647
		Culture.Philosophy and religion              0.51
		Culture.Sports                               0.861
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.869
		Culture.Visual arts.Fashion                  0.784
		Culture.Visual arts.Visual arts*             0.722
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.735
		Geography.Regions.Africa.Central Africa      0.596
		Geography.Regions.Africa.Eastern Africa      0.476
		Geography.Regions.Africa.Northern Africa     0.672
		Geography.Regions.Africa.Southern Africa     0.668
		Geography.Regions.Africa.Western Africa      0.755
		Geography.Regions.Americas.Central America   0.554
		Geography.Regions.Americas.North America     0.629
		Geography.Regions.Americas.South America     0.718
		Geography.Regions.Asia.Asia*                 0.805
		Geography.Regions.Asia.Central Asia          0.737
		Geography.Regions.Asia.East Asia             0.761
		Geography.Regions.Asia.North Asia            0.701
		Geography.Regions.Asia.South Asia            0.755
		Geography.Regions.Asia.Southeast Asia        0.651
		Geography.Regions.Asia.West Asia             0.763
		Geography.Regions.Europe.Eastern Europe      0.759
		Geography.Regions.Europe.Europe*             0.774
		Geography.Regions.Europe.Northern Europe     0.579
		Geography.Regions.Europe.Southern Europe     0.725
		Geography.Regions.Europe.Western Europe      0.748
		Geography.Regions.Oceania                    0.703
		History and Society.Business and economics   0.551
		History and Society.Education                0.543
		History and Society.History                  0.499
		History and Society.Military and warfare     0.749
		History and Society.Politics and government  0.501
		History and Society.Society                  0.433
		History and Society.Transportation           0.897
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.749
		STEM.Computing                               0.787
		STEM.Earth and environment                   0.624
		STEM.Engineering                             0.816
		STEM.Libraries & Information                 0.706
		STEM.Mathematics                             0.79
		STEM.Medicine & Health                       0.666
		STEM.Physics                                 0.68
		STEM.STEM*                                   0.905
		STEM.Space                                   0.875
		STEM.Technology                              0.695
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.718, macro=0.551):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.862
		Culture.Biography.Women                      0.442
		Culture.Food and drink                       0.428
		Culture.Internet culture                     0.38
		Culture.Linguistics                          0.807
		Culture.Literature                           0.557
		Culture.Media.Books                          0.543
		Culture.Media.Entertainment                  0.356
		Culture.Media.Films                          0.696
		Culture.Media.Media*                         0.653
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.628
		Culture.Media.Software                       0.168
		Culture.Media.Television                     0.672
		Culture.Media.Video games                    0.653
		Culture.Performing arts                      0.462
		Culture.Philosophy and religion              0.541
		Culture.Sports                               0.972
		Culture.Visual arts.Architecture             0.718
		Culture.Visual arts.Comics and Anime         0.559
		Culture.Visual arts.Fashion                  0.254
		Culture.Visual arts.Visual arts*             0.635
		Geography.Geographical                       0.619
		Geography.Regions.Africa.Africa*             0.383
		Geography.Regions.Africa.Central Africa      0.145
		Geography.Regions.Africa.Eastern Africa      0.244
		Geography.Regions.Africa.Northern Africa     0.301
		Geography.Regions.Africa.Southern Africa     0.358
		Geography.Regions.Africa.Western Africa      0.385
		Geography.Regions.Americas.Central America   0.461
		Geography.Regions.Americas.North America     0.8
		Geography.Regions.Americas.South America     0.612
		Geography.Regions.Asia.Asia*                 0.596
		Geography.Regions.Asia.Central Asia          0.317
		Geography.Regions.Asia.East Asia             0.491
		Geography.Regions.Asia.North Asia            0.149
		Geography.Regions.Asia.South Asia            0.858
		Geography.Regions.Asia.Southeast Asia        0.533
		Geography.Regions.Asia.West Asia             0.801
		Geography.Regions.Europe.Eastern Europe      0.652
		Geography.Regions.Europe.Europe*             0.716
		Geography.Regions.Europe.Northern Europe     0.809
		Geography.Regions.Europe.Southern Europe     0.731
		Geography.Regions.Europe.Western Europe      0.775
		Geography.Regions.Oceania                    0.79
		History and Society.Business and economics   0.477
		History and Society.Education                0.646
		History and Society.History                  0.355
		History and Society.Military and warfare     0.555
		History and Society.Politics and government  0.615
		History and Society.Society                  0.37
		History and Society.Transportation           0.895
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.279
		STEM.Computing                               0.276
		STEM.Earth and environment                   0.519
		STEM.Engineering                             0.644
		STEM.Libraries & Information                 0.389
		STEM.Mathematics                             0.258
		STEM.Medicine & Health                       0.667
		STEM.Physics                                 0.191
		STEM.STEM*                                   0.722
		STEM.Space                                   0.875
		STEM.Technology                              0.269
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.731, macro=0.598):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.564
		Culture.Food and drink                       0.517
		Culture.Internet culture                     0.513
		Culture.Linguistics                          0.779
		Culture.Literature                           0.636
		Culture.Media.Books                          0.608
		Culture.Media.Entertainment                  0.398
		Culture.Media.Films                          0.728
		Culture.Media.Media*                         0.74
		Culture.Media.Music                          0.845
		Culture.Media.Radio                          0.601
		Culture.Media.Software                       0.276
		Culture.Media.Television                     0.665
		Culture.Media.Video games                    0.755
		Culture.Performing arts                      0.539
		Culture.Philosophy and religion              0.525
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.681
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.676
		Geography.Geographical                       0.627
		Geography.Regions.Africa.Africa*             0.503
		Geography.Regions.Africa.Central Africa      0.233
		Geography.Regions.Africa.Eastern Africa      0.322
		Geography.Regions.Africa.Northern Africa     0.416
		Geography.Regions.Africa.Southern Africa     0.466
		Geography.Regions.Africa.Western Africa      0.51
		Geography.Regions.Americas.Central America   0.503
		Geography.Regions.Americas.North America     0.704
		Geography.Regions.Americas.South America     0.661
		Geography.Regions.Asia.Asia*                 0.685
		Geography.Regions.Asia.Central Asia          0.443
		Geography.Regions.Asia.East Asia             0.597
		Geography.Regions.Asia.North Asia            0.246
		Geography.Regions.Asia.South Asia            0.803
		Geography.Regions.Asia.Southeast Asia        0.586
		Geography.Regions.Asia.West Asia             0.781
		Geography.Regions.Europe.Eastern Europe      0.702
		Geography.Regions.Europe.Europe*             0.744
		Geography.Regions.Europe.Northern Europe     0.675
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.761
		Geography.Regions.Oceania                    0.744
		History and Society.Business and economics   0.511
		History and Society.Education                0.59
		History and Society.History                  0.415
		History and Society.Military and warfare     0.638
		History and Society.Politics and government  0.552
		History and Society.Society                  0.399
		History and Society.Transportation           0.896
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.406
		STEM.Computing                               0.409
		STEM.Earth and environment                   0.567
		STEM.Engineering                             0.72
		STEM.Libraries & Information                 0.502
		STEM.Mathematics                             0.389
		STEM.Medicine & Health                       0.667
		STEM.Physics                                 0.298
		STEM.STEM*                                   0.803
		STEM.Space                                   0.875
		STEM.Technology                              0.388
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.977
		History and Society.Society                  0.984
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.998
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.02
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.026
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.009
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.025
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.978
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.972
		Culture.Literature                           0.975
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.938
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.95
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.985
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.974
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.957
		Geography.Regions.Africa.Northern Africa     0.976
		Geography.Regions.Africa.Southern Africa     0.971
		Geography.Regions.Africa.Western Africa      0.98
		Geography.Regions.Americas.Central America   0.972
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.982
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.973
		Geography.Regions.Asia.West Asia             0.975
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.973
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.962
		History and Society.Education                0.968
		History and Society.History                  0.949
		History and Society.Military and warfare     0.975
		History and Society.Politics and government  0.944
		History and Society.Society                  0.925
		History and Society.Transportation           0.985
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.986
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.957
		STEM.Mathematics                             0.983
		STEM.Medicine & Health                       0.97
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.979
		STEM.Space                                   0.99
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.781, macro=0.608):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.927
		Culture.Biography.Women                      0.555
		Culture.Food and drink                       0.544
		Culture.Internet culture                     0.607
		Culture.Linguistics                          0.815
		Culture.Literature                           0.687
		Culture.Media.Books                          0.591
		Culture.Media.Entertainment                  0.332
		Culture.Media.Films                          0.773
		Culture.Media.Media*                         0.827
		Culture.Media.Music                          0.886
		Culture.Media.Radio                          0.407
		Culture.Media.Software                       0.331
		Culture.Media.Television                     0.643
		Culture.Media.Video games                    0.872
		Culture.Performing arts                      0.462
		Culture.Philosophy and religion              0.493
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.728
		Culture.Visual arts.Comics and Anime         0.772
		Culture.Visual arts.Fashion                  0.319
		Culture.Visual arts.Visual arts*             0.719
		Geography.Geographical                       0.654
		Geography.Regions.Africa.Africa*             0.547
		Geography.Regions.Africa.Central Africa      0.24
		Geography.Regions.Africa.Eastern Africa      0.157
		Geography.Regions.Africa.Northern Africa     0.336
		Geography.Regions.Africa.Southern Africa     0.357
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.473
		Geography.Regions.Americas.North America     0.791
		Geography.Regions.Americas.South America     0.645
		Geography.Regions.Asia.Asia*                 0.759
		Geography.Regions.Asia.Central Asia          0.35
		Geography.Regions.Asia.East Asia             0.618
		Geography.Regions.Asia.North Asia            0.232
		Geography.Regions.Asia.South Asia            0.826
		Geography.Regions.Asia.Southeast Asia        0.583
		Geography.Regions.Asia.West Asia             0.844
		Geography.Regions.Europe.Eastern Europe      0.781
		Geography.Regions.Europe.Europe*             0.823
		Geography.Regions.Europe.Northern Europe     0.747
		Geography.Regions.Europe.Southern Europe     0.76
		Geography.Regions.Europe.Western Europe      0.794
		Geography.Regions.Oceania                    0.769
		History and Society.Business and economics   0.475
		History and Society.Education                0.554
		History and Society.History                  0.369
		History and Society.Military and warfare     0.717
		History and Society.Politics and government  0.593
		History and Society.Society                  0.396
		History and Society.Transportation           0.927
		STEM.Biology                                 0.954
		STEM.Chemistry                               0.419
		STEM.Computing                               0.385
		STEM.Earth and environment                   0.524
		STEM.Engineering                             0.777
		STEM.Libraries & Information                 0.322
		STEM.Mathematics                             0.505
		STEM.Medicine & Health                       0.675
		STEM.Physics                                 0.252
		STEM.STEM*                                   0.913
		STEM.Space                                   0.912
		STEM.Technology                              0.431
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

