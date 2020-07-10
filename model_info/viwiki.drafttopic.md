Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'presort': 'auto', 'n_iter_no_change': None, 'center': False, 'random_state': None, 'population_rates': None, 'loss': 'deviance', 'max_depth': 5, 'max_leaf_nodes': None, 'learning_rate': 0.1, 'validation_fraction': 0.1, 'scale': False, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_estimators': 150, 'init': None, 'warm_start': False, 'tol': 0.0001, 'max_features': 'log2', 'subsample': 1.0, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'min_samples_split': 2, 'multilabel': True, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'verbose': 0}
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
	counts (n=60032):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14030  -->  12212  1818   776  45226
			'Culture.Biography.Women'                       5061  -->   3886  1175   834  54137
			'Culture.Food and drink'                        1396  -->    871   525   131  58505
			'Culture.Internet culture'                      3474  -->   2669   805   262  56296
			'Culture.Linguistics'                           1428  -->   1033   395    70  58534
			'Culture.Literature'                            5510  -->   3994  1516   546  53976
			'Culture.Media.Books'                           1408  -->    904   504   143  58481
			'Culture.Media.Entertainment'                   1975  -->    805  1170   197  57860
			'Culture.Media.Films'                           2577  -->   1883   694   186  57269
			'Culture.Media.Media*'                         13141  -->  11005  2136  1473  45418
			'Culture.Media.Music'                           2948  -->   2413   535   230  56854
			'Culture.Media.Radio'                            288  -->    182   106    28  59716
			'Culture.Media.Software'                        2272  -->   1739   533   304  57456
			'Culture.Media.Television'                      1922  -->   1217   705   163  57947
			'Culture.Media.Video games'                     2124  -->   1863   261    71  57837
			'Culture.Performing arts'                       1350  -->    890   460   128  58554
			'Culture.Philosophy and religion'               2960  -->   1362  1598   277  56795
			'Culture.Sports'                                3891  -->   3332   559   136  56005
			'Culture.Visual arts.Architecture'              1793  -->   1237   556   190  58049
			'Culture.Visual arts.Comics and Anime'          2149  -->   1729   420   108  57775
			'Culture.Visual arts.Fashion'                   1486  -->   1177   309   112  58434
			'Culture.Visual arts.Visual arts*'              5943  -->   4200  1743   489  53600
			'Geography.Geographical'                        3951  -->   2485  1466   591  55490
			'Geography.Regions.Africa.Africa*'              5652  -->   2463  3189   669  53711
			'Geography.Regions.Africa.Central Africa'       1203  -->    240   963    69  58760
			'Geography.Regions.Africa.Eastern Africa'        446  -->    137   309    50  59536
			'Geography.Regions.Africa.Northern Africa'      1491  -->    592   899    91  58450
			'Geography.Regions.Africa.Southern Africa'      1182  -->    481   701    77  58773
			'Geography.Regions.Africa.Western Africa'        671  -->    282   389    84  59277
			'Geography.Regions.Americas.Central America'    1582  -->    209  1373    54  58396
			'Geography.Regions.Americas.North America'      5377  -->   1802  3575   263  54392
			'Geography.Regions.Americas.South America'      2201  -->    755  1446   150  57681
			'Geography.Regions.Asia.Asia*'                 13641  -->   7257  6384  1738  44653
			'Geography.Regions.Asia.Central Asia'           1213  -->    418   795    86  58733
			'Geography.Regions.Asia.East Asia'              5488  -->   2398  3090   419  54125
			'Geography.Regions.Asia.North Asia'             1645  -->    651   994   139  58248
			'Geography.Regions.Asia.South Asia'             2040  -->    890  1150    67  57925
			'Geography.Regions.Asia.Southeast Asia'         2515  -->    392  2123    83  57434
			'Geography.Regions.Asia.West Asia'              2191  -->   1098  1093    85  57756
			'Geography.Regions.Europe.Eastern Europe'       3517  -->   1645  1872   169  56346
			'Geography.Regions.Europe.Europe*'             12453  -->   6800  5653  1393  46186
			'Geography.Regions.Europe.Northern Europe'      2853  -->    500  2353   140  57039
			'Geography.Regions.Europe.Southern Europe'      2753  -->   1160  1593    87  57192
			'Geography.Regions.Europe.Western Europe'       3991  -->   1795  2196   106  55935
			'Geography.Regions.Oceania'                     2299  -->    870  1429   241  57492
			'History and Society.Business and economics'    3330  -->   1926  1404   378  56324
			'History and Society.Education'                 1629  -->    860   769   119  58284
			'History and Society.History'                   4354  -->   2017  2337   675  55003
			'History and Society.Military and warfare'      4924  -->   3348  1576   491  54617
			'History and Society.Politics and government'   4579  -->   1679  2900   568  54885
			'History and Society.Society'                   5969  -->   1521  4448   325  53738
			'History and Society.Transportation'            3564  -->   3221   343   100  56368
			'STEM.Biology'                                  7039  -->   6401   638   177  52816
			'STEM.Chemistry'                                1414  -->   1053   361   192  58426
			'STEM.Computing'                                2410  -->   1848   562   327  57295
			'STEM.Earth and environment'                    1600  -->   1004   596   121  58311
			'STEM.Engineering'                              2990  -->   2431   559   155  56887
			'STEM.Libraries & Information'                   492  -->    383   109    57  59483
			'STEM.Mathematics'                               908  -->    675   233    62  59062
			'STEM.Medicine & Health'                        1748  -->   1158   590   149  58135
			'STEM.Physics'                                  1353  -->    907   446   189  58490
			'STEM.STEM*'                                   20307  -->  18271  2036  1047  38678
			'STEM.Space'                                    1586  -->   1407   179    62  58384
			'STEM.Technology'                               4140  -->   2830  1310   615  55277
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.234         0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.219         0.055
		Culture.Media.Music                             0.049         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.049         0.01
		Culture.Sports                                  0.065         0.061
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.066         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.09          0.064
		Geography.Regions.Americas.South America        0.037         0.007
		Geography.Regions.Asia.Asia*                    0.227         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.091         0.012
		Geography.Regions.Asia.North Asia               0.027         0.006
		Geography.Regions.Asia.South Asia               0.034         0.017
		Geography.Regions.Asia.Southeast Asia           0.042         0.006
		Geography.Regions.Asia.West Asia                0.036         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.018
		Geography.Regions.Europe.Europe*                0.207         0.082
		Geography.Regions.Europe.Northern Europe        0.048         0.029
		Geography.Regions.Europe.Southern Europe        0.046         0.014
		Geography.Regions.Europe.Western Europe         0.066         0.021
		Geography.Regions.Oceania                       0.038         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.073         0.011
		History and Society.Military and warfare        0.082         0.015
		History and Society.Politics and government     0.076         0.016
		History and Society.Society                     0.099         0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.117         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.338         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.045, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.121
		Culture.Biography.Women                      0.027
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.054
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.016
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.026
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.064
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.008
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.071
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.017
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.016
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.005
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.955, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.936
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.929
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.995
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.645, macro=0.588):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.768
		Culture.Food and drink                       0.624
		Culture.Internet culture                     0.768
		Culture.Linguistics                          0.723
		Culture.Literature                           0.725
		Culture.Media.Books                          0.642
		Culture.Media.Entertainment                  0.408
		Culture.Media.Films                          0.731
		Culture.Media.Media*                         0.837
		Culture.Media.Music                          0.819
		Culture.Media.Radio                          0.632
		Culture.Media.Software                       0.765
		Culture.Media.Television                     0.633
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.659
		Culture.Philosophy and religion              0.46
		Culture.Sports                               0.856
		Culture.Visual arts.Architecture             0.69
		Culture.Visual arts.Comics and Anime         0.805
		Culture.Visual arts.Fashion                  0.792
		Culture.Visual arts.Visual arts*             0.707
		Geography.Geographical                       0.629
		Geography.Regions.Africa.Africa*             0.436
		Geography.Regions.Africa.Central Africa      0.2
		Geography.Regions.Africa.Eastern Africa      0.307
		Geography.Regions.Africa.Northern Africa     0.397
		Geography.Regions.Africa.Southern Africa     0.407
		Geography.Regions.Africa.Western Africa      0.42
		Geography.Regions.Americas.Central America   0.132
		Geography.Regions.Americas.North America     0.335
		Geography.Regions.Americas.South America     0.343
		Geography.Regions.Asia.Asia*                 0.532
		Geography.Regions.Asia.Central Asia          0.345
		Geography.Regions.Asia.East Asia             0.437
		Geography.Regions.Asia.North Asia            0.396
		Geography.Regions.Asia.South Asia            0.436
		Geography.Regions.Asia.Southeast Asia        0.156
		Geography.Regions.Asia.West Asia             0.501
		Geography.Regions.Europe.Eastern Europe      0.468
		Geography.Regions.Europe.Europe*             0.546
		Geography.Regions.Europe.Northern Europe     0.175
		Geography.Regions.Europe.Southern Europe     0.421
		Geography.Regions.Europe.Western Europe      0.45
		Geography.Regions.Oceania                    0.378
		History and Society.Business and economics   0.578
		History and Society.Education                0.528
		History and Society.History                  0.463
		History and Society.Military and warfare     0.68
		History and Society.Politics and government  0.367
		History and Society.Society                  0.255
		History and Society.Transportation           0.904
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.745
		STEM.Computing                               0.767
		STEM.Earth and environment                   0.628
		STEM.Engineering                             0.813
		STEM.Libraries & Information                 0.778
		STEM.Mathematics                             0.743
		STEM.Medicine & Health                       0.662
		STEM.Physics                                 0.67
		STEM.STEM*                                   0.9
		STEM.Space                                   0.887
		STEM.Technology                              0.684
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.995
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.681, macro=0.522):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.437
		Culture.Food and drink                       0.419
		Culture.Internet culture                     0.385
		Culture.Linguistics                          0.832
		Culture.Literature                           0.524
		Culture.Media.Books                          0.535
		Culture.Media.Entertainment                  0.325
		Culture.Media.Films                          0.727
		Culture.Media.Media*                         0.61
		Culture.Media.Music                          0.815
		Culture.Media.Radio                          0.76
		Culture.Media.Software                       0.161
		Culture.Media.Television                     0.671
		Culture.Media.Video games                    0.678
		Culture.Performing arts                      0.483
		Culture.Philosophy and religion              0.501
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.7
		Culture.Visual arts.Comics and Anime         0.511
		Culture.Visual arts.Fashion                  0.273
		Culture.Visual arts.Visual arts*             0.592
		Geography.Geographical                       0.565
		Geography.Regions.Africa.Africa*             0.234
		Geography.Regions.Africa.Central Africa      0.108
		Geography.Regions.Africa.Eastern Africa      0.157
		Geography.Regions.Africa.Northern Africa     0.258
		Geography.Regions.Africa.Southern Africa     0.291
		Geography.Regions.Africa.Western Africa      0.183
		Geography.Regions.Americas.Central America   0.333
		Geography.Regions.Americas.North America     0.826
		Geography.Regions.Americas.South America     0.479
		Geography.Regions.Asia.Asia*                 0.443
		Geography.Regions.Asia.Central Asia          0.159
		Geography.Regions.Asia.East Asia             0.414
		Geography.Regions.Asia.North Asia            0.486
		Geography.Regions.Asia.South Asia            0.865
		Geography.Regions.Asia.Southeast Asia        0.406
		Geography.Regions.Asia.West Asia             0.803
		Geography.Regions.Europe.Eastern Europe      0.746
		Geography.Regions.Europe.Europe*             0.624
		Geography.Regions.Europe.Northern Europe     0.683
		Geography.Regions.Europe.Southern Europe     0.797
		Geography.Regions.Europe.Western Europe      0.834
		Geography.Regions.Oceania                    0.604
		History and Society.Business and economics   0.463
		History and Society.Education                0.676
		History and Society.History                  0.298
		History and Society.Military and warfare     0.545
		History and Society.Politics and government  0.375
		History and Society.Society                  0.263
		History and Society.Transportation           0.895
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.28
		STEM.Computing                               0.279
		STEM.Earth and environment                   0.592
		STEM.Engineering                             0.636
		STEM.Libraries & Information                 0.36
		STEM.Mathematics                             0.249
		STEM.Medicine & Health                       0.629
		STEM.Physics                                 0.165
		STEM.STEM*                                   0.706
		STEM.Space                                   0.783
		STEM.Technology                              0.245
		-------------------------------------------  -----
	!precision (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.989
		History and Society.Society                  0.994
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
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.64, macro=0.521):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.557
		Culture.Food and drink                       0.501
		Culture.Internet culture                     0.513
		Culture.Linguistics                          0.774
		Culture.Literature                           0.608
		Culture.Media.Books                          0.584
		Culture.Media.Entertainment                  0.361
		Culture.Media.Films                          0.729
		Culture.Media.Media*                         0.706
		Culture.Media.Music                          0.817
		Culture.Media.Radio                          0.69
		Culture.Media.Software                       0.267
		Culture.Media.Television                     0.652
		Culture.Media.Video games                    0.765
		Culture.Performing arts                      0.558
		Culture.Philosophy and religion              0.48
		Culture.Sports                               0.904
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.625
		Culture.Visual arts.Fashion                  0.406
		Culture.Visual arts.Visual arts*             0.645
		Geography.Geographical                       0.596
		Geography.Regions.Africa.Africa*             0.305
		Geography.Regions.Africa.Central Africa      0.14
		Geography.Regions.Africa.Eastern Africa      0.208
		Geography.Regions.Africa.Northern Africa     0.313
		Geography.Regions.Africa.Southern Africa     0.34
		Geography.Regions.Africa.Western Africa      0.255
		Geography.Regions.Americas.Central America   0.189
		Geography.Regions.Americas.North America     0.477
		Geography.Regions.Americas.South America     0.4
		Geography.Regions.Asia.Asia*                 0.483
		Geography.Regions.Asia.Central Asia          0.218
		Geography.Regions.Asia.East Asia             0.425
		Geography.Regions.Asia.North Asia            0.436
		Geography.Regions.Asia.South Asia            0.58
		Geography.Regions.Asia.Southeast Asia        0.225
		Geography.Regions.Asia.West Asia             0.617
		Geography.Regions.Europe.Eastern Europe      0.575
		Geography.Regions.Europe.Europe*             0.582
		Geography.Regions.Europe.Northern Europe     0.279
		Geography.Regions.Europe.Southern Europe     0.551
		Geography.Regions.Europe.Western Europe      0.584
		Geography.Regions.Oceania                    0.465
		History and Society.Business and economics   0.514
		History and Society.Education                0.593
		History and Society.History                  0.363
		History and Society.Military and warfare     0.605
		History and Society.Politics and government  0.371
		History and Society.Society                  0.259
		History and Society.Transportation           0.899
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.407
		STEM.Computing                               0.409
		STEM.Earth and environment                   0.609
		STEM.Engineering                             0.714
		STEM.Libraries & Information                 0.492
		STEM.Mathematics                             0.373
		STEM.Medicine & Health                       0.645
		STEM.Physics                                 0.264
		STEM.STEM*                                   0.791
		STEM.Space                                   0.832
		STEM.Technology                              0.361
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
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
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.988
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.969
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.005
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.037
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.029
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.01
		History and Society.Society                  0.006
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.95, macro=0.955):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.982
		Culture.Linguistics                          0.965
		Culture.Literature                           0.972
		Culture.Media.Books                          0.976
		Culture.Media.Entertainment                  0.961
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.941
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.974
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.965
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.927
		Geography.Regions.Africa.Central Africa      0.942
		Geography.Regions.Africa.Eastern Africa      0.909
		Geography.Regions.Africa.Northern Africa     0.932
		Geography.Regions.Africa.Southern Africa     0.95
		Geography.Regions.Africa.Western Africa      0.96
		Geography.Regions.Americas.Central America   0.902
		Geography.Regions.Americas.North America     0.904
		Geography.Regions.Americas.South America     0.93
		Geography.Regions.Asia.Asia*                 0.897
		Geography.Regions.Asia.Central Asia          0.949
		Geography.Regions.Asia.East Asia             0.93
		Geography.Regions.Asia.North Asia            0.961
		Geography.Regions.Asia.South Asia            0.922
		Geography.Regions.Asia.Southeast Asia        0.885
		Geography.Regions.Asia.West Asia             0.942
		Geography.Regions.Europe.Eastern Europe      0.943
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.907
		Geography.Regions.Europe.Southern Europe     0.927
		Geography.Regions.Europe.Western Europe      0.929
		Geography.Regions.Oceania                    0.922
		History and Society.Business and economics   0.961
		History and Society.Education                0.962
		History and Society.History                  0.94
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.911
		History and Society.Society                  0.885
		History and Society.Transportation           0.985
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.985
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.968
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.963
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.97
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.977
		STEM.Space                                   0.987
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.676, macro=0.511):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.535
		Culture.Food and drink                       0.525
		Culture.Internet culture                     0.667
		Culture.Linguistics                          0.77
		Culture.Literature                           0.638
		Culture.Media.Books                          0.553
		Culture.Media.Entertainment                  0.317
		Culture.Media.Films                          0.745
		Culture.Media.Media*                         0.802
		Culture.Media.Music                          0.843
		Culture.Media.Radio                          0.543
		Culture.Media.Software                       0.281
		Culture.Media.Television                     0.598
		Culture.Media.Video games                    0.805
		Culture.Performing arts                      0.5
		Culture.Philosophy and religion              0.437
		Culture.Sports                               0.918
		Culture.Visual arts.Architecture             0.679
		Culture.Visual arts.Comics and Anime         0.723
		Culture.Visual arts.Fashion                  0.392
		Culture.Visual arts.Visual arts*             0.67
		Geography.Geographical                       0.606
		Geography.Regions.Africa.Africa*             0.304
		Geography.Regions.Africa.Central Africa      0.045
		Geography.Regions.Africa.Eastern Africa      0.051
		Geography.Regions.Africa.Northern Africa     0.136
		Geography.Regions.Africa.Southern Africa     0.174
		Geography.Regions.Africa.Western Africa      0.13
		Geography.Regions.Americas.Central America   0.101
		Geography.Regions.Americas.North America     0.605
		Geography.Regions.Americas.South America     0.328
		Geography.Regions.Asia.Asia*                 0.517
		Geography.Regions.Asia.Central Asia          0.093
		Geography.Regions.Asia.East Asia             0.367
		Geography.Regions.Asia.North Asia            0.37
		Geography.Regions.Asia.South Asia            0.572
		Geography.Regions.Asia.Southeast Asia        0.158
		Geography.Regions.Asia.West Asia             0.566
		Geography.Regions.Europe.Eastern Europe      0.595
		Geography.Regions.Europe.Europe*             0.657
		Geography.Regions.Europe.Northern Europe     0.407
		Geography.Regions.Europe.Southern Europe     0.558
		Geography.Regions.Europe.Western Europe      0.607
		Geography.Regions.Oceania                    0.424
		History and Society.Business and economics   0.492
		History and Society.Education                0.567
		History and Society.History                  0.284
		History and Society.Military and warfare     0.68
		History and Society.Politics and government  0.3
		History and Society.Society                  0.192
		History and Society.Transportation           0.942
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.438
		STEM.Computing                               0.434
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.701
		STEM.Libraries & Information                 0.442
		STEM.Mathematics                             0.509
		STEM.Medicine & Health                       0.665
		STEM.Physics                                 0.192
		STEM.STEM*                                   0.905
		STEM.Space                                   0.891
		STEM.Technology                              0.332
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

