Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'init': None, 'n_estimators': 150, 'criterion': 'friedman_mse', 'presort': 'deprecated', 'min_impurity_split': None, 'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 1, 'subsample': 1.0, 'max_leaf_nodes': None, 'max_features': 'log2', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'learning_rate': 0.1, 'center': False, 'multilabel': True, 'min_impurity_decrease': 0.0, 'population_rates': None, 'tol': 0.0001, 'n_iter_no_change': None, 'label_weights': {}, 'verbose': 0, 'loss': 'deviance', 'ccp_alpha': 0.0, 'random_state': None, 'validation_fraction': 0.1, 'scale': False, 'max_depth': 5, 'warm_start': False, 'min_samples_split': 2}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=59389):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 17601  -->  15138  2463  1493  40295
			'Culture.Biography.Women'                       3879  -->   2215  1664   528  54982
			'Culture.Food and drink'                        1483  -->   1012   471   125  57781
			'Culture.Internet culture'                      3043  -->   2088   955   278  56068
			'Culture.Linguistics'                           1586  -->    938   648   149  57654
			'Culture.Literature'                            5594  -->   3616  1978   746  53049
			'Culture.Media.Books'                           1544  -->    826   718   247  57598
			'Culture.Media.Entertainment'                   2182  -->    955  1227   182  57025
			'Culture.Media.Films'                           2629  -->   1807   822   263  56497
			'Culture.Media.Media*'                         14040  -->  11077  2963  1995  43354
			'Culture.Media.Music'                           3171  -->   2353   818   357  55861
			'Culture.Media.Radio'                            787  -->    384   403    76  58526
			'Culture.Media.Software'                        1888  -->   1087   801   414  57087
			'Culture.Media.Television'                      2061  -->   1193   868   213  57115
			'Culture.Media.Video games'                     2181  -->   1718   463   128  57080
			'Culture.Performing arts'                       1414  -->    730   684   143  57832
			'Culture.Philosophy and religion'               3192  -->   1442  1750   344  55853
			'Culture.Sports'                                6570  -->   5597   973   297  52522
			'Culture.Visual arts.Architecture'              1987  -->   1018   969   271  57131
			'Culture.Visual arts.Comics and Anime'          2405  -->   1694   711   264  56720
			'Culture.Visual arts.Fashion'                   1194  -->    730   464   105  58090
			'Culture.Visual arts.Visual arts*'              6154  -->   3694  2460   744  52491
			'Geography.Geographical'                        3395  -->   1838  1557   577  55417
			'Geography.Regions.Africa.Africa*'              4858  -->   3337  1521   396  54135
			'Geography.Regions.Africa.Central Africa'       1162  -->    718   444    69  58158
			'Geography.Regions.Africa.Eastern Africa'        583  -->    296   287    57  58749
			'Geography.Regions.Africa.Northern Africa'      1377  -->    833   544   115  57897
			'Geography.Regions.Africa.Southern Africa'      1002  -->    586   416    70  58317
			'Geography.Regions.Africa.Western Africa'        339  -->    132   207    47  59003
			'Geography.Regions.Americas.Central America'    1301  -->    708   593    96  57992
			'Geography.Regions.Americas.North America'      5960  -->   3084  2876   989  52440
			'Geography.Regions.Americas.South America'      1491  -->    864   627    98  57800
			'Geography.Regions.Asia.Asia*'                 15101  -->  11169  3932  1862  42426
			'Geography.Regions.Asia.Central Asia'           1181  -->    713   468    73  58135
			'Geography.Regions.Asia.East Asia'              7203  -->   4837  2366  1051  51135
			'Geography.Regions.Asia.North Asia'             2820  -->   1670  1150   282  56287
			'Geography.Regions.Asia.South Asia'             1640  -->   1100   540   124  57625
			'Geography.Regions.Asia.Southeast Asia'         1670  -->   1013   657   118  57601
			'Geography.Regions.Asia.West Asia'              1924  -->   1139   785   183  57282
			'Geography.Regions.Europe.Eastern Europe'       3865  -->   2390  1475   370  55154
			'Geography.Regions.Europe.Europe*'             13524  -->   9360  4164  1982  43883
			'Geography.Regions.Europe.Northern Europe'      3345  -->   1725  1620   444  55600
			'Geography.Regions.Europe.Southern Europe'      2992  -->   1855  1137   343  56054
			'Geography.Regions.Europe.Western Europe'       4149  -->   2440  1709   580  54660
			'Geography.Regions.Oceania'                     1575  -->    948   627    90  57724
			'History and Society.Business and economics'    3752  -->   1820  1932   557  55080
			'History and Society.Education'                 1907  -->    821  1086   170  57312
			'History and Society.History'                   4604  -->   1973  2631   655  54130
			'History and Society.Military and warfare'      4643  -->   2895  1748   524  54222
			'History and Society.Politics and government'   3373  -->   1418  1955   482  55534
			'History and Society.Society'                   3974  -->    902  3072   259  55156
			'History and Society.Transportation'            4763  -->   4016   747   325  54301
			'STEM.Biology'                                  2779  -->   1937   842   250  56360
			'STEM.Chemistry'                                1414  -->    956   458   203  57772
			'STEM.Computing'                                2448  -->   1698   750   447  56494
			'STEM.Earth and environment'                    1773  -->   1032   741   180  57436
			'STEM.Engineering'                              2886  -->   2036   850   237  56266
			'STEM.Libraries & Information'                   957  -->    501   456    78  58354
			'STEM.Mathematics'                              1092  -->    752   340    69  58228
			'STEM.Medicine & Health'                        1855  -->   1046   809   203  57331
			'STEM.Physics'                                  1300  -->    739   561   168  57921
			'STEM.STEM*'                                   17046  -->  14285  2761  1341  41002
			'STEM.Space'                                    1825  -->   1578   247    65  57499
			'STEM.Technology'                               4199  -->   2480  1719   737  54453
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.296         0.121
		Culture.Biography.Women                         0.065         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.051         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.044         0.012
		Culture.Media.Media*                            0.236         0.055
		Culture.Media.Music                             0.053         0.021
		Culture.Media.Radio                             0.013         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.01
		Culture.Sports                                  0.111         0.061
		Culture.Visual arts.Architecture                0.033         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.02          0.001
		Culture.Visual arts.Visual arts*                0.104         0.018
		Geography.Geographical                          0.057         0.021
		Geography.Regions.Africa.Africa*                0.082         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.01          0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.017         0.001
		Geography.Regions.Africa.Western Africa         0.006         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.254         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.121         0.012
		Geography.Regions.Asia.North Asia               0.047         0.006
		Geography.Regions.Asia.South Asia               0.028         0.017
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.065         0.018
		Geography.Regions.Europe.Europe*                0.228         0.082
		Geography.Regions.Europe.Northern Europe        0.056         0.029
		Geography.Regions.Europe.Southern Europe        0.05          0.014
		Geography.Regions.Europe.Western Europe         0.07          0.021
		Geography.Regions.Oceania                       0.027         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.078         0.011
		History and Society.Military and warfare        0.078         0.015
		History and Society.Politics and government     0.057         0.016
		History and Society.Society                     0.067         0.008
		History and Society.Transportation              0.08          0.016
		STEM.Biology                                    0.047         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.016         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.031         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.287         0.066
		STEM.Space                                      0.031         0.004
		STEM.Technology                                 0.071         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.136
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.023
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.013
		Culture.Media.Media*                         0.085
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.005
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.057
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.006
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.025
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.05
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.079
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.028
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.096
		Geography.Regions.Europe.Northern Europe     0.023
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.015
		History and Society.Education                0.006
		History and Society.History                  0.017
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.015
		History and Society.Society                  0.007
		History and Society.Transportation           0.02
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.005
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.005
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.864
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.977
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.915
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.994
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.975
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.921
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.904
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.985
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.985
		History and Society.Society                  0.993
		History and Society.Transportation           0.98
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.995
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.995
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.682, macro=0.61):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.86
		Culture.Biography.Women                      0.571
		Culture.Food and drink                       0.682
		Culture.Internet culture                     0.686
		Culture.Linguistics                          0.591
		Culture.Literature                           0.646
		Culture.Media.Books                          0.535
		Culture.Media.Entertainment                  0.438
		Culture.Media.Films                          0.687
		Culture.Media.Media*                         0.789
		Culture.Media.Music                          0.742
		Culture.Media.Radio                          0.488
		Culture.Media.Software                       0.576
		Culture.Media.Television                     0.579
		Culture.Media.Video games                    0.788
		Culture.Performing arts                      0.516
		Culture.Philosophy and religion              0.452
		Culture.Sports                               0.852
		Culture.Visual arts.Architecture             0.512
		Culture.Visual arts.Comics and Anime         0.704
		Culture.Visual arts.Fashion                  0.611
		Culture.Visual arts.Visual arts*             0.6
		Geography.Geographical                       0.541
		Geography.Regions.Africa.Africa*             0.687
		Geography.Regions.Africa.Central Africa      0.618
		Geography.Regions.Africa.Eastern Africa      0.508
		Geography.Regions.Africa.Northern Africa     0.605
		Geography.Regions.Africa.Southern Africa     0.585
		Geography.Regions.Africa.Western Africa      0.389
		Geography.Regions.Americas.Central America   0.544
		Geography.Regions.Americas.North America     0.517
		Geography.Regions.Americas.South America     0.579
		Geography.Regions.Asia.Asia*                 0.74
		Geography.Regions.Asia.Central Asia          0.604
		Geography.Regions.Asia.East Asia             0.672
		Geography.Regions.Asia.North Asia            0.592
		Geography.Regions.Asia.South Asia            0.671
		Geography.Regions.Asia.Southeast Asia        0.607
		Geography.Regions.Asia.West Asia             0.592
		Geography.Regions.Europe.Eastern Europe      0.618
		Geography.Regions.Europe.Europe*             0.692
		Geography.Regions.Europe.Northern Europe     0.516
		Geography.Regions.Europe.Southern Europe     0.62
		Geography.Regions.Europe.Western Europe      0.588
		Geography.Regions.Oceania                    0.602
		History and Society.Business and economics   0.485
		History and Society.Education                0.431
		History and Society.History                  0.429
		History and Society.Military and warfare     0.624
		History and Society.Politics and government  0.42
		History and Society.Society                  0.227
		History and Society.Transportation           0.843
		STEM.Biology                                 0.697
		STEM.Chemistry                               0.676
		STEM.Computing                               0.694
		STEM.Earth and environment                   0.582
		STEM.Engineering                             0.705
		STEM.Libraries & Information                 0.524
		STEM.Mathematics                             0.689
		STEM.Medicine & Health                       0.564
		STEM.Physics                                 0.568
		STEM.STEM*                                   0.838
		STEM.Space                                   0.865
		STEM.Technology                              0.591
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.956
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.958
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.957
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.99
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.994
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
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
	precision (micro=0.615, macro=0.476):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.769
		Culture.Biography.Women                      0.479
		Culture.Food and drink                       0.449
		Culture.Internet culture                     0.345
		Culture.Linguistics                          0.652
		Culture.Literature                           0.415
		Culture.Media.Books                          0.354
		Culture.Media.Entertainment                  0.355
		Culture.Media.Films                          0.636
		Culture.Media.Media*                         0.513
		Culture.Media.Music                          0.717
		Culture.Media.Radio                          0.469
		Culture.Media.Software                       0.096
		Culture.Media.Television                     0.585
		Culture.Media.Video games                    0.509
		Culture.Performing arts                      0.393
		Culture.Philosophy and religion              0.438
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.545
		Culture.Visual arts.Comics and Anime         0.269
		Culture.Visual arts.Fashion                  0.235
		Culture.Visual arts.Visual arts*             0.444
		Geography.Geographical                       0.534
		Geography.Regions.Africa.Africa*             0.45
		Geography.Regions.Africa.Central Africa      0.27
		Geography.Regions.Africa.Eastern Africa      0.21
		Geography.Regions.Africa.Northern Africa     0.294
		Geography.Regions.Africa.Southern Africa     0.392
		Geography.Regions.Africa.Western Africa      0.269
		Geography.Regions.Americas.Central America   0.535
		Geography.Regions.Americas.North America     0.655
		Geography.Regions.Americas.South America     0.704
		Geography.Regions.Asia.Asia*                 0.496
		Geography.Regions.Asia.Central Asia          0.279
		Geography.Regions.Asia.East Asia             0.293
		Geography.Regions.Asia.North Asia            0.403
		Geography.Regions.Asia.South Asia            0.841
		Geography.Regions.Asia.Southeast Asia        0.653
		Geography.Regions.Asia.West Asia             0.69
		Geography.Regions.Europe.Eastern Europe      0.636
		Geography.Regions.Europe.Europe*             0.588
		Geography.Regions.Europe.Northern Europe     0.662
		Geography.Regions.Europe.Southern Europe     0.591
		Geography.Regions.Europe.Western Europe      0.542
		Geography.Regions.Oceania                    0.867
		History and Society.Business and economics   0.325
		History and Society.Education                0.54
		History and Society.History                  0.284
		History and Society.Military and warfare     0.505
		History and Society.Politics and government  0.45
		History and Society.Society                  0.29
		History and Society.Transportation           0.703
		STEM.Biology                                 0.851
		STEM.Chemistry                               0.248
		STEM.Computing                               0.202
		STEM.Earth and environment                   0.472
		STEM.Engineering                             0.495
		STEM.Libraries & Information                 0.213
		STEM.Mathematics                             0.214
		STEM.Medicine & Health                       0.511
		STEM.Physics                                 0.157
		STEM.STEM*                                   0.65
		STEM.Space                                   0.768
		STEM.Technology                              0.188
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.987
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.637, macro=0.515):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.812
		Culture.Biography.Women                      0.521
		Culture.Food and drink                       0.542
		Culture.Internet culture                     0.459
		Culture.Linguistics                          0.62
		Culture.Literature                           0.506
		Culture.Media.Books                          0.426
		Culture.Media.Entertainment                  0.392
		Culture.Media.Films                          0.661
		Culture.Media.Media*                         0.621
		Culture.Media.Music                          0.729
		Culture.Media.Radio                          0.479
		Culture.Media.Software                       0.164
		Culture.Media.Television                     0.582
		Culture.Media.Video games                    0.618
		Culture.Performing arts                      0.446
		Culture.Philosophy and religion              0.445
		Culture.Sports                               0.879
		Culture.Visual arts.Architecture             0.528
		Culture.Visual arts.Comics and Anime         0.389
		Culture.Visual arts.Fashion                  0.339
		Culture.Visual arts.Visual arts*             0.51
		Geography.Geographical                       0.538
		Geography.Regions.Africa.Africa*             0.544
		Geography.Regions.Africa.Central Africa      0.376
		Geography.Regions.Africa.Eastern Africa      0.297
		Geography.Regions.Africa.Northern Africa     0.396
		Geography.Regions.Africa.Southern Africa     0.469
		Geography.Regions.Africa.Western Africa      0.318
		Geography.Regions.Americas.Central America   0.54
		Geography.Regions.Americas.North America     0.578
		Geography.Regions.Americas.South America     0.636
		Geography.Regions.Asia.Asia*                 0.594
		Geography.Regions.Asia.Central Asia          0.382
		Geography.Regions.Asia.East Asia             0.408
		Geography.Regions.Asia.North Asia            0.48
		Geography.Regions.Asia.South Asia            0.746
		Geography.Regions.Asia.Southeast Asia        0.629
		Geography.Regions.Asia.West Asia             0.637
		Geography.Regions.Europe.Eastern Europe      0.627
		Geography.Regions.Europe.Europe*             0.636
		Geography.Regions.Europe.Northern Europe     0.58
		Geography.Regions.Europe.Southern Europe     0.605
		Geography.Regions.Europe.Western Europe      0.564
		Geography.Regions.Oceania                    0.711
		History and Society.Business and economics   0.389
		History and Society.Education                0.479
		History and Society.History                  0.342
		History and Society.Military and warfare     0.558
		History and Society.Politics and government  0.435
		History and Society.Society                  0.255
		History and Society.Transportation           0.767
		STEM.Biology                                 0.766
		STEM.Chemistry                               0.363
		STEM.Computing                               0.312
		STEM.Earth and environment                   0.521
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.303
		STEM.Mathematics                             0.326
		STEM.Medicine & Health                       0.536
		STEM.Physics                                 0.246
		STEM.STEM*                                   0.732
		STEM.Space                                   0.813
		STEM.Technology                              0.285
		-------------------------------------------  -----
	!f1 (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.97, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.952
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.992
		Culture.Media.Media*                         0.947
		Culture.Media.Music                          0.988
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.952
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.985
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.982
		History and Society.Society                  0.989
		History and Society.Transportation           0.992
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.96
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.008):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.036
		Culture.Biography.Women                      0.01
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.003
		Culture.Literature                           0.014
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.005
		Culture.Media.Media*                         0.044
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.014
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.019
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.042
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.02
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.043
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.01
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.006
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
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
	roc_auc (micro=0.957, macro=0.96):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.96
		Culture.Food and drink                       0.974
		Culture.Internet culture                     0.973
		Culture.Linguistics                          0.96
		Culture.Literature                           0.961
		Culture.Media.Books                          0.968
		Culture.Media.Entertainment                  0.948
		Culture.Media.Films                          0.972
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.955
		Culture.Media.Software                       0.976
		Culture.Media.Television                     0.966
		Culture.Media.Video games                    0.981
		Culture.Performing arts                      0.962
		Culture.Philosophy and religion              0.932
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.963
		Culture.Visual arts.Comics and Anime         0.975
		Culture.Visual arts.Fashion                  0.966
		Culture.Visual arts.Visual arts*             0.942
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.965
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.96
		Geography.Regions.Africa.Northern Africa     0.963
		Geography.Regions.Africa.Southern Africa     0.96
		Geography.Regions.Africa.Western Africa      0.942
		Geography.Regions.Americas.Central America   0.961
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.963
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.971
		Geography.Regions.Asia.East Asia             0.956
		Geography.Regions.Asia.North Asia            0.959
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.957
		Geography.Regions.Asia.West Asia             0.958
		Geography.Regions.Europe.Eastern Europe      0.954
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.947
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.958
		Geography.Regions.Oceania                    0.963
		History and Society.Business and economics   0.943
		History and Society.Education                0.95
		History and Society.History                  0.929
		History and Society.Military and warfare     0.959
		History and Society.Politics and government  0.935
		History and Society.Society                  0.871
		History and Society.Transportation           0.982
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.98
		STEM.Computing                               0.979
		STEM.Earth and environment                   0.964
		STEM.Engineering                             0.969
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.976
		STEM.Medicine & Health                       0.962
		STEM.Physics                                 0.978
		STEM.STEM*                                   0.966
		STEM.Space                                   0.985
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.665, macro=0.5):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.892
		Culture.Biography.Women                      0.48
		Culture.Food and drink                       0.537
		Culture.Internet culture                     0.543
		Culture.Linguistics                          0.586
		Culture.Literature                           0.507
		Culture.Media.Books                          0.353
		Culture.Media.Entertainment                  0.372
		Culture.Media.Films                          0.674
		Culture.Media.Media*                         0.702
		Culture.Media.Music                          0.724
		Culture.Media.Radio                          0.359
		Culture.Media.Software                       0.131
		Culture.Media.Television                     0.606
		Culture.Media.Video games                    0.669
		Culture.Performing arts                      0.384
		Culture.Philosophy and religion              0.384
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.509
		Culture.Visual arts.Comics and Anime         0.392
		Culture.Visual arts.Fashion                  0.284
		Culture.Visual arts.Visual arts*             0.518
		Geography.Geographical                       0.529
		Geography.Regions.Africa.Africa*             0.542
		Geography.Regions.Africa.Central Africa      0.39
		Geography.Regions.Africa.Eastern Africa      0.126
		Geography.Regions.Africa.Northern Africa     0.336
		Geography.Regions.Africa.Southern Africa     0.395
		Geography.Regions.Africa.Western Africa      0.148
		Geography.Regions.Americas.Central America   0.421
		Geography.Regions.Americas.North America     0.632
		Geography.Regions.Americas.South America     0.626
		Geography.Regions.Asia.Asia*                 0.62
		Geography.Regions.Asia.Central Asia          0.276
		Geography.Regions.Asia.East Asia             0.389
		Geography.Regions.Asia.North Asia            0.432
		Geography.Regions.Asia.South Asia            0.77
		Geography.Regions.Asia.Southeast Asia        0.603
		Geography.Regions.Asia.West Asia             0.627
		Geography.Regions.Europe.Eastern Europe      0.622
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.601
		Geography.Regions.Europe.Southern Europe     0.637
		Geography.Regions.Europe.Western Europe      0.548
		Geography.Regions.Oceania                    0.758
		History and Society.Business and economics   0.296
		History and Society.Education                0.436
		History and Society.History                  0.274
		History and Society.Military and warfare     0.592
		History and Society.Politics and government  0.379
		History and Society.Society                  0.184
		History and Society.Transportation           0.836
		STEM.Biology                                 0.797
		STEM.Chemistry                               0.286
		STEM.Computing                               0.262
		STEM.Earth and environment                   0.488
		STEM.Engineering                             0.627
		STEM.Libraries & Information                 0.237
		STEM.Mathematics                             0.397
		STEM.Medicine & Health                       0.545
		STEM.Physics                                 0.189
		STEM.STEM*                                   0.831
		STEM.Space                                   0.875
		STEM.Technology                              0.275
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

