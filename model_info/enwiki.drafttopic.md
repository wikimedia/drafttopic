Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'n_estimators': 150, 'init': None, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'max_depth': 5, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'population_rates': None, 'validation_fraction': 0.1, 'random_state': None, 'warm_start': False, 'min_weight_fraction_leaf': 0.0, 'max_leaf_nodes': None, 'presort': 'auto', 'n_iter_no_change': None, 'scale': False, 'multilabel': True, 'subsample': 1.0, 'label_weights': {}, 'tol': 0.0001, 'verbose': 0, 'min_impurity_decrease': 0.0, 'learning_rate': 0.1, 'min_impurity_split': None, 'loss': 'deviance', 'min_samples_split': 2, 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.6.3'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.11'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.189-3+deb9u1 (2019-09-20)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-11-amd64'
	
	Statistics:
	counts (n=60052):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16350  -->  12379  3971  2039  41663
			'Culture.Biography.Women'                       4056  -->   1093  2963   501  55495
			'Culture.Food and drink'                        1245  -->    802   443    97  58710
			'Culture.Internet culture'                      2681  -->   1735   946   214  57157
			'Culture.Linguistics'                           1210  -->    666   544   105  58737
			'Culture.Literature'                            4977  -->   2944  2033   658  54417
			'Culture.Media.Books'                           1810  -->    929   881   222  58020
			'Culture.Media.Entertainment'                   1737  -->    328  1409   107  58208
			'Culture.Media.Films'                           2225  -->   1523   702   201  57626
			'Culture.Media.Media*'                         13453  -->  10311  3142  2038  44561
			'Culture.Media.Music'                           2532  -->   1844   688   276  57244
			'Culture.Media.Radio'                           1116  -->    830   286    51  58885
			'Culture.Media.Software'                        1667  -->    783   884   353  58032
			'Culture.Media.Television'                      2008  -->   1051   957   260  57784
			'Culture.Media.Video games'                     1881  -->   1454   427    77  58094
			'Culture.Performing arts'                       1273  -->    638   635   120  58659
			'Culture.Philosophy and religion'               2505  -->   1119  1386   347  57200
			'Culture.Sports'                                5720  -->   4960   760   357  53975
			'Culture.Visual arts.Architecture'              2468  -->   1529   939   260  57324
			'Culture.Visual arts.Comics and Anime'          1384  -->    761   623   127  58541
			'Culture.Visual arts.Fashion'                   1118  -->    672   446    95  58839
			'Culture.Visual arts.Visual arts*'              5691  -->   3140  2551   534  53827
			'Geography.Geographical'                        3224  -->   1827  1397   295  56533
			'Geography.Regions.Africa.Africa*'              5529  -->   3835  1694   277  54246
			'Geography.Regions.Africa.Central Africa'         27  -->      0    27    64  59961
			'Geography.Regions.Africa.Eastern Africa'       1079  -->    613   466    57  58916
			'Geography.Regions.Africa.Northern Africa'      1228  -->    624   604   114  58710
			'Geography.Regions.Africa.Southern Africa'      1244  -->    738   506    63  58745
			'Geography.Regions.Africa.Western Africa'       1131  -->    758   373    55  58866
			'Geography.Regions.Americas.Central America'    1282  -->    421   861   100  58670
			'Geography.Regions.Americas.North America'      7247  -->   3838  3409   897  51908
			'Geography.Regions.Americas.South America'      1480  -->    699   781   183  58389
			'Geography.Regions.Asia.Asia*'                 10642  -->   7332  3310   985  48425
			'Geography.Regions.Asia.Central Asia'           1125  -->    561   564    47  58880
			'Geography.Regions.Asia.East Asia'              2594  -->   1414  1180   289  57169
			'Geography.Regions.Asia.North Asia'             1317  -->    672   645   191  58544
			'Geography.Regions.Asia.South Asia'             2361  -->   1664   697   131  57560
			'Geography.Regions.Asia.Southeast Asia'         1623  -->    734   889   101  58328
			'Geography.Regions.Asia.West Asia'              2154  -->   1269   885   123  57775
			'Geography.Regions.Europe.Eastern Europe'       2996  -->   1676  1320   334  56722
			'Geography.Regions.Europe.Europe*'             11970  -->   7205  4765  1720  46362
			'Geography.Regions.Europe.Northern Europe'      4083  -->   1669  2414   456  55513
			'Geography.Regions.Europe.Southern Europe'      2233  -->    861  1372   238  57581
			'Geography.Regions.Europe.Western Europe'       3035  -->   1468  1567   407  56610
			'Geography.Regions.Oceania'                     2466  -->   1387  1079    92  57494
			'History and Society.Business and economics'    3248  -->   1148  2100   488  56316
			'History and Society.Education'                 2097  -->    893  1204   268  57687
			'History and Society.History'                   3062  -->    600  2462   296  56694
			'History and Society.Military and warfare'      3819  -->   2311  1508   411  55822
			'History and Society.Politics and government'   4473  -->   1793  2680   458  55121
			'History and Society.Society'                   3850  -->    757  3093   263  55939
			'History and Society.Transportation'            3424  -->   2568   856   274  56354
			'STEM.Biology'                                  2735  -->   1967   768   150  57167
			'STEM.Chemistry'                                1251  -->    682   569   193  58608
			'STEM.Computing'                                1902  -->   1013   889   390  57760
			'STEM.Earth and environment'                    1590  -->    799   791   118  58344
			'STEM.Engineering'                              2145  -->   1241   904   166  57741
			'STEM.Libraries & Information'                  1110  -->    509   601    68  58874
			'STEM.Mathematics'                              1026  -->    464   562   118  58908
			'STEM.Medicine & Health'                        1613  -->    873   740   200  58239
			'STEM.Physics'                                  1135  -->    532   603   147  58770
			'STEM.STEM*'                                   15592  -->  12309  3283  1419  43041
			'STEM.Space'                                    1330  -->   1044   286    55  58667
			'STEM.Technology'                               3436  -->   1544  1892   605  56011
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.272         0.123
		Culture.Biography.Women                         0.068         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.02          0.007
		Culture.Literature                              0.083         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.224         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.054         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.019         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.121         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.177         0.046
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.199         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.057         0.005
	match_rate (micro=0.051, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.134
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.05
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.05
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.079
		Geography.Regions.Europe.Northern Europe     0.02
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.016
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.012
		History and Society.Education                0.008
		History and Society.History                  0.007
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.019
		History and Society.Society                  0.007
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.004
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.95
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.921
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.993
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.981
		History and Society.Society                  0.993
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.628, macro=0.542):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.757
		Culture.Biography.Women                      0.269
		Culture.Food and drink                       0.644
		Culture.Internet culture                     0.647
		Culture.Linguistics                          0.55
		Culture.Literature                           0.592
		Culture.Media.Books                          0.513
		Culture.Media.Entertainment                  0.189
		Culture.Media.Films                          0.684
		Culture.Media.Media*                         0.766
		Culture.Media.Music                          0.728
		Culture.Media.Radio                          0.744
		Culture.Media.Software                       0.47
		Culture.Media.Television                     0.523
		Culture.Media.Video games                    0.773
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.447
		Culture.Sports                               0.867
		Culture.Visual arts.Architecture             0.62
		Culture.Visual arts.Comics and Anime         0.55
		Culture.Visual arts.Fashion                  0.601
		Culture.Visual arts.Visual arts*             0.552
		Geography.Geographical                       0.567
		Geography.Regions.Africa.Africa*             0.694
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.568
		Geography.Regions.Africa.Northern Africa     0.508
		Geography.Regions.Africa.Southern Africa     0.593
		Geography.Regions.Africa.Western Africa      0.67
		Geography.Regions.Americas.Central America   0.328
		Geography.Regions.Americas.North America     0.53
		Geography.Regions.Americas.South America     0.472
		Geography.Regions.Asia.Asia*                 0.689
		Geography.Regions.Asia.Central Asia          0.499
		Geography.Regions.Asia.East Asia             0.545
		Geography.Regions.Asia.North Asia            0.51
		Geography.Regions.Asia.South Asia            0.705
		Geography.Regions.Asia.Southeast Asia        0.452
		Geography.Regions.Asia.West Asia             0.589
		Geography.Regions.Europe.Eastern Europe      0.559
		Geography.Regions.Europe.Europe*             0.602
		Geography.Regions.Europe.Northern Europe     0.409
		Geography.Regions.Europe.Southern Europe     0.386
		Geography.Regions.Europe.Western Europe      0.484
		Geography.Regions.Oceania                    0.562
		History and Society.Business and economics   0.353
		History and Society.Education                0.426
		History and Society.History                  0.196
		History and Society.Military and warfare     0.605
		History and Society.Politics and government  0.401
		History and Society.Society                  0.197
		History and Society.Transportation           0.75
		STEM.Biology                                 0.719
		STEM.Chemistry                               0.545
		STEM.Computing                               0.533
		STEM.Earth and environment                   0.503
		STEM.Engineering                             0.579
		STEM.Libraries & Information                 0.459
		STEM.Mathematics                             0.452
		STEM.Medicine & Health                       0.541
		STEM.Physics                                 0.469
		STEM.STEM*                                   0.789
		STEM.Space                                   0.785
		STEM.Technology                              0.449
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.953
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.988
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.956
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.995
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.995
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.628, macro=0.478):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.695
		Culture.Biography.Women                      0.308
		Culture.Food and drink                       0.491
		Culture.Internet culture                     0.379
		Culture.Linguistics                          0.695
		Culture.Literature                           0.438
		Culture.Media.Books                          0.353
		Culture.Media.Entertainment                  0.27
		Culture.Media.Films                          0.677
		Culture.Media.Media*                         0.521
		Culture.Media.Music                          0.788
		Culture.Media.Radio                          0.65
		Culture.Media.Software                       0.094
		Culture.Media.Television                     0.51
		Culture.Media.Video games                    0.605
		Culture.Performing arts                      0.416
		Culture.Philosophy and religion              0.444
		Culture.Sports                               0.91
		Culture.Visual arts.Architecture             0.594
		Culture.Visual arts.Comics and Anime         0.359
		Culture.Visual arts.Fashion                  0.232
		Culture.Visual arts.Visual arts*             0.512
		Geography.Geographical                       0.725
		Geography.Regions.Africa.Africa*             0.518
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.211
		Geography.Regions.Africa.Northern Africa     0.244
		Geography.Regions.Africa.Southern Africa     0.395
		Geography.Regions.Africa.Western Africa      0.329
		Geography.Regions.Americas.Central America   0.39
		Geography.Regions.Americas.North America     0.682
		Geography.Regions.Americas.South America     0.49
		Geography.Regions.Asia.Asia*                 0.622
		Geography.Regions.Asia.Central Asia          0.352
		Geography.Regions.Asia.East Asia             0.556
		Geography.Regions.Asia.North Asia            0.127
		Geography.Regions.Asia.South Asia            0.827
		Geography.Regions.Asia.Southeast Asia        0.613
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.554
		Geography.Regions.Europe.Europe*             0.581
		Geography.Regions.Europe.Northern Europe     0.613
		Geography.Regions.Europe.Southern Europe     0.553
		Geography.Regions.Europe.Western Europe      0.57
		Geography.Regions.Oceania                    0.844
		History and Society.Business and economics   0.296
		History and Society.Education                0.406
		History and Society.History                  0.293
		History and Society.Military and warfare     0.542
		History and Society.Politics and government  0.585
		History and Society.Society                  0.349
		History and Society.Transportation           0.704
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.206
		STEM.Computing                               0.176
		STEM.Earth and environment                   0.532
		STEM.Engineering                             0.515
		STEM.Libraries & Information                 0.198
		STEM.Mathematics                             0.086
		STEM.Medicine & Health                       0.505
		STEM.Physics                                 0.138
		STEM.STEM*                                   0.648
		STEM.Space                                   0.835
		STEM.Technology                              0.178
		-------------------------------------------  -----
	!precision (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.985
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.983
		History and Society.Society                  0.99
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.725
		Culture.Biography.Women                      0.287
		Culture.Food and drink                       0.557
		Culture.Internet culture                     0.478
		Culture.Linguistics                          0.614
		Culture.Literature                           0.503
		Culture.Media.Books                          0.418
		Culture.Media.Entertainment                  0.222
		Culture.Media.Films                          0.681
		Culture.Media.Media*                         0.621
		Culture.Media.Music                          0.757
		Culture.Media.Radio                          0.694
		Culture.Media.Software                       0.156
		Culture.Media.Television                     0.516
		Culture.Media.Video games                    0.679
		Culture.Performing arts                      0.454
		Culture.Philosophy and religion              0.445
		Culture.Sports                               0.888
		Culture.Visual arts.Architecture             0.607
		Culture.Visual arts.Comics and Anime         0.434
		Culture.Visual arts.Fashion                  0.335
		Culture.Visual arts.Visual arts*             0.531
		Geography.Geographical                       0.636
		Geography.Regions.Africa.Africa*             0.593
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.308
		Geography.Regions.Africa.Northern Africa     0.329
		Geography.Regions.Africa.Southern Africa     0.474
		Geography.Regions.Africa.Western Africa      0.442
		Geography.Regions.Americas.Central America   0.357
		Geography.Regions.Americas.North America     0.596
		Geography.Regions.Americas.South America     0.481
		Geography.Regions.Asia.Asia*                 0.654
		Geography.Regions.Asia.Central Asia          0.412
		Geography.Regions.Asia.East Asia             0.55
		Geography.Regions.Asia.North Asia            0.203
		Geography.Regions.Asia.South Asia            0.761
		Geography.Regions.Asia.Southeast Asia        0.52
		Geography.Regions.Asia.West Asia             0.661
		Geography.Regions.Europe.Eastern Europe      0.557
		Geography.Regions.Europe.Europe*             0.591
		Geography.Regions.Europe.Northern Europe     0.49
		Geography.Regions.Europe.Southern Europe     0.454
		Geography.Regions.Europe.Western Europe      0.523
		Geography.Regions.Oceania                    0.675
		History and Society.Business and economics   0.322
		History and Society.Education                0.416
		History and Society.History                  0.235
		History and Society.Military and warfare     0.572
		History and Society.Politics and government  0.476
		History and Society.Society                  0.252
		History and Society.Transportation           0.726
		STEM.Biology                                 0.802
		STEM.Chemistry                               0.299
		STEM.Computing                               0.265
		STEM.Earth and environment                   0.517
		STEM.Engineering                             0.545
		STEM.Libraries & Information                 0.277
		STEM.Mathematics                             0.145
		STEM.Medicine & Health                       0.522
		STEM.Physics                                 0.213
		STEM.STEM*                                   0.712
		STEM.Space                                   0.809
		STEM.Technology                              0.255
		-------------------------------------------  -----
	!f1 (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.959
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.968, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.945
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.937
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.985
		History and Society.Education                0.991
		History and Society.History                  0.986
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.975
		History and Society.Society                  0.985
		History and Society.Transportation           0.991
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.956
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.047
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.012
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.044
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.036
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.005
		History and Society.History                  0.005
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.005
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.955, macro=0.956):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.933
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.962
		Culture.Literature                           0.961
		Culture.Media.Books                          0.969
		Culture.Media.Entertainment                  0.938
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.984
		Culture.Media.Software                       0.975
		Culture.Media.Television                     0.968
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.979
		Culture.Visual arts.Fashion                  0.976
		Culture.Visual arts.Visual arts*             0.951
		Geography.Geographical                       0.959
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.589
		Geography.Regions.Africa.Eastern Africa      0.969
		Geography.Regions.Africa.Northern Africa     0.966
		Geography.Regions.Africa.Southern Africa     0.975
		Geography.Regions.Africa.Western Africa      0.982
		Geography.Regions.Americas.Central America   0.953
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.961
		Geography.Regions.Asia.Asia*                 0.958
		Geography.Regions.Asia.Central Asia          0.973
		Geography.Regions.Asia.East Asia             0.965
		Geography.Regions.Asia.North Asia            0.974
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.962
		Geography.Regions.Asia.West Asia             0.969
		Geography.Regions.Europe.Eastern Europe      0.967
		Geography.Regions.Europe.Europe*             0.934
		Geography.Regions.Europe.Northern Europe     0.94
		Geography.Regions.Europe.Southern Europe     0.953
		Geography.Regions.Europe.Western Europe      0.956
		Geography.Regions.Oceania                    0.965
		History and Society.Business and economics   0.936
		History and Society.Education                0.953
		History and Society.History                  0.902
		History and Society.Military and warfare     0.965
		History and Society.Politics and government  0.931
		History and Society.Society                  0.867
		History and Society.Transportation           0.98
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.982
		STEM.Computing                               0.978
		STEM.Earth and environment                   0.962
		STEM.Engineering                             0.964
		STEM.Libraries & Information                 0.959
		STEM.Mathematics                             0.972
		STEM.Medicine & Health                       0.966
		STEM.Physics                                 0.976
		STEM.STEM*                                   0.958
		STEM.Space                                   0.984
		STEM.Technology                              0.953
		-------------------------------------------  -----
	pr_auc (micro=0.653, macro=0.484):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.795
		Culture.Biography.Women                      0.241
		Culture.Food and drink                       0.56
		Culture.Internet culture                     0.564
		Culture.Linguistics                          0.622
		Culture.Literature                           0.527
		Culture.Media.Books                          0.375
		Culture.Media.Entertainment                  0.17
		Culture.Media.Films                          0.71
		Culture.Media.Media*                         0.686
		Culture.Media.Music                          0.781
		Culture.Media.Radio                          0.756
		Culture.Media.Software                       0.089
		Culture.Media.Television                     0.491
		Culture.Media.Video games                    0.761
		Culture.Performing arts                      0.396
		Culture.Philosophy and religion              0.358
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.651
		Culture.Visual arts.Comics and Anime         0.42
		Culture.Visual arts.Fashion                  0.279
		Culture.Visual arts.Visual arts*             0.546
		Geography.Geographical                       0.692
		Geography.Regions.Africa.Africa*             0.597
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.206
		Geography.Regions.Africa.Northern Africa     0.292
		Geography.Regions.Africa.Southern Africa     0.428
		Geography.Regions.Africa.Western Africa      0.359
		Geography.Regions.Americas.Central America   0.282
		Geography.Regions.Americas.North America     0.655
		Geography.Regions.Americas.South America     0.426
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.358
		Geography.Regions.Asia.East Asia             0.527
		Geography.Regions.Asia.North Asia            0.196
		Geography.Regions.Asia.South Asia            0.798
		Geography.Regions.Asia.Southeast Asia        0.504
		Geography.Regions.Asia.West Asia             0.692
		Geography.Regions.Europe.Eastern Europe      0.585
		Geography.Regions.Europe.Europe*             0.618
		Geography.Regions.Europe.Northern Europe     0.512
		Geography.Regions.Europe.Southern Europe     0.469
		Geography.Regions.Europe.Western Europe      0.531
		Geography.Regions.Oceania                    0.729
		History and Society.Business and economics   0.238
		History and Society.Education                0.343
		History and Society.History                  0.164
		History and Society.Military and warfare     0.589
		History and Society.Politics and government  0.506
		History and Society.Society                  0.214
		History and Society.Transportation           0.766
		STEM.Biology                                 0.861
		STEM.Chemistry                               0.239
		STEM.Computing                               0.197
		STEM.Earth and environment                   0.522
		STEM.Engineering                             0.543
		STEM.Libraries & Information                 0.263
		STEM.Mathematics                             0.158
		STEM.Medicine & Health                       0.468
		STEM.Physics                                 0.175
		STEM.STEM*                                   0.796
		STEM.Space                                   0.856
		STEM.Technology                              0.213
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'properties': {'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

