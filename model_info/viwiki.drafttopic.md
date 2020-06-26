Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'multilabel': True, 'population_rates': None, 'min_impurity_decrease': 0.0, 'n_estimators': 150, 'min_samples_split': 2, 'learning_rate': 0.1, 'presort': 'deprecated', 'subsample': 1.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'loss': 'deviance', 'criterion': 'friedman_mse', 'max_features': 'log2', 'validation_fraction': 0.1, 'ccp_alpha': 0.0, 'init': None, 'min_impurity_split': None, 'max_leaf_nodes': None, 'random_state': None, 'tol': 0.0001, 'verbose': 0, 'center': False, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'label_weights': {}, 'scale': False, 'max_depth': 5}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=59996):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14008  -->  12139  1869   795  45193
			'Culture.Biography.Women'                       5105  -->   3921  1184   830  54061
			'Culture.Food and drink'                        1372  -->    861   511   138  58486
			'Culture.Internet culture'                      3477  -->   2624   853   275  56244
			'Culture.Linguistics'                           1472  -->   1105   367    77  58447
			'Culture.Literature'                            5540  -->   4009  1531   534  53922
			'Culture.Media.Books'                           1416  -->    887   529   150  58430
			'Culture.Media.Entertainment'                   1937  -->    785  1152   164  57895
			'Culture.Media.Films'                           2566  -->   1859   707   156  57274
			'Culture.Media.Media*'                         13028  -->  10921  2107  1471  45497
			'Culture.Media.Music'                           2872  -->   2350   522   218  56906
			'Culture.Media.Radio'                            274  -->    159   115    42  59680
			'Culture.Media.Software'                        2246  -->   1658   588   323  57427
			'Culture.Media.Television'                      1943  -->   1240   703   167  57886
			'Culture.Media.Video games'                     2118  -->   1871   247    80  57798
			'Culture.Performing arts'                       1354  -->    878   476   121  58521
			'Culture.Philosophy and religion'               2966  -->   1405  1561   273  56757
			'Culture.Sports'                                3832  -->   3307   525   134  56030
			'Culture.Visual arts.Architecture'              1814  -->   1235   579   174  58008
			'Culture.Visual arts.Comics and Anime'          2201  -->   1792   409   138  57657
			'Culture.Visual arts.Fashion'                   1483  -->   1140   343   129  58384
			'Culture.Visual arts.Visual arts*'              6013  -->   4243  1770   508  53475
			'Geography.Geographical'                        3953  -->   2532  1421   572  55471
			'Geography.Regions.Africa.Africa*'              5715  -->   2500  3215   712  53569
			'Geography.Regions.Africa.Central Africa'       1211  -->    248   963    57  58728
			'Geography.Regions.Africa.Eastern Africa'        450  -->    131   319    47  59499
			'Geography.Regions.Africa.Northern Africa'      1467  -->    591   876    91  58438
			'Geography.Regions.Africa.Southern Africa'      1168  -->    476   692    89  58739
			'Geography.Regions.Africa.Western Africa'        670  -->    289   381    73  59253
			'Geography.Regions.Americas.Central America'    1578  -->    224  1354    61  58357
			'Geography.Regions.Americas.North America'      5362  -->   1714  3648   194  54440
			'Geography.Regions.Americas.South America'      2198  -->    794  1404   139  57659
			'Geography.Regions.Asia.Asia*'                 13666  -->   7154  6512  1680  44650
			'Geography.Regions.Asia.Central Asia'           1196  -->    385   811    94  58706
			'Geography.Regions.Asia.East Asia'              5485  -->   2272  3213   399  54112
			'Geography.Regions.Asia.North Asia'             1651  -->    613  1038   132  58213
			'Geography.Regions.Asia.South Asia'             2015  -->    894  1121    77  57904
			'Geography.Regions.Asia.Southeast Asia'         2582  -->    431  2151    90  57324
			'Geography.Regions.Asia.West Asia'              2161  -->   1093  1068    95  57740
			'Geography.Regions.Europe.Eastern Europe'       3540  -->   1617  1923   189  56267
			'Geography.Regions.Europe.Europe*'             12516  -->   6584  5932  1415  46065
			'Geography.Regions.Europe.Northern Europe'      2860  -->    427  2433   106  57030
			'Geography.Regions.Europe.Southern Europe'      2800  -->   1140  1660    92  57104
			'Geography.Regions.Europe.Western Europe'       4004  -->   1765  2239   103  55889
			'Geography.Regions.Oceania'                     2232  -->    858  1374   237  57527
			'History and Society.Business and economics'    3348  -->   1926  1422   408  56240
			'History and Society.Education'                 1568  -->    836   732   155  58273
			'History and Society.History'                   4494  -->   2144  2350   647  54855
			'History and Society.Military and warfare'      4968  -->   3357  1611   483  54545
			'History and Society.Politics and government'   4525  -->   1707  2818   553  54918
			'History and Society.Society'                   6042  -->   1532  4510   367  53587
			'History and Society.Transportation'            3547  -->   3199   348   122  56327
			'STEM.Biology'                                  7090  -->   6443   647   175  52731
			'STEM.Chemistry'                                1476  -->   1097   379   188  58332
			'STEM.Computing'                                2392  -->   1821   571   344  57260
			'STEM.Earth and environment'                    1628  -->   1021   607   143  58225
			'STEM.Engineering'                              2989  -->   2433   556   129  56878
			'STEM.Libraries & Information'                   479  -->    346   133    64  59453
			'STEM.Mathematics'                               932  -->    717   215    63  59001
			'STEM.Medicine & Health'                        1745  -->   1163   582   149  58102
			'STEM.Physics'                                  1338  -->    903   435   179  58479
			'STEM.STEM*'                                   20343  -->  18256  2087  1087  38566
			'STEM.Space'                                    1615  -->   1418   197    52  58329
			'STEM.Technology'                               4144  -->   2818  1326   622  55230
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
	match_rate (micro=0.047, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.016
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.024
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.058
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.008
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.009
		Geography.Regions.Europe.Europe*             0.068
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.017
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.02
		History and Society.Society                  0.01
		History and Society.Transportation           0.016
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.088
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.953, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.942
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.98
		History and Society.Society                  0.99
		History and Society.Transportation           0.984
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.912
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.645, macro=0.584):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.768
		Culture.Food and drink                       0.628
		Culture.Internet culture                     0.755
		Culture.Linguistics                          0.751
		Culture.Literature                           0.724
		Culture.Media.Books                          0.626
		Culture.Media.Entertainment                  0.405
		Culture.Media.Films                          0.724
		Culture.Media.Media*                         0.838
		Culture.Media.Music                          0.818
		Culture.Media.Radio                          0.58
		Culture.Media.Software                       0.738
		Culture.Media.Television                     0.638
		Culture.Media.Video games                    0.883
		Culture.Performing arts                      0.648
		Culture.Philosophy and religion              0.474
		Culture.Sports                               0.863
		Culture.Visual arts.Architecture             0.681
		Culture.Visual arts.Comics and Anime         0.814
		Culture.Visual arts.Fashion                  0.769
		Culture.Visual arts.Visual arts*             0.706
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.437
		Geography.Regions.Africa.Central Africa      0.205
		Geography.Regions.Africa.Eastern Africa      0.291
		Geography.Regions.Africa.Northern Africa     0.403
		Geography.Regions.Africa.Southern Africa     0.408
		Geography.Regions.Africa.Western Africa      0.431
		Geography.Regions.Americas.Central America   0.142
		Geography.Regions.Americas.North America     0.32
		Geography.Regions.Americas.South America     0.361
		Geography.Regions.Asia.Asia*                 0.523
		Geography.Regions.Asia.Central Asia          0.322
		Geography.Regions.Asia.East Asia             0.414
		Geography.Regions.Asia.North Asia            0.371
		Geography.Regions.Asia.South Asia            0.444
		Geography.Regions.Asia.Southeast Asia        0.167
		Geography.Regions.Asia.West Asia             0.506
		Geography.Regions.Europe.Eastern Europe      0.457
		Geography.Regions.Europe.Europe*             0.526
		Geography.Regions.Europe.Northern Europe     0.149
		Geography.Regions.Europe.Southern Europe     0.407
		Geography.Regions.Europe.Western Europe      0.441
		Geography.Regions.Oceania                    0.384
		History and Society.Business and economics   0.575
		History and Society.Education                0.533
		History and Society.History                  0.477
		History and Society.Military and warfare     0.676
		History and Society.Politics and government  0.377
		History and Society.Society                  0.254
		History and Society.Transportation           0.902
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.743
		STEM.Computing                               0.761
		STEM.Earth and environment                   0.627
		STEM.Engineering                             0.814
		STEM.Libraries & Information                 0.722
		STEM.Mathematics                             0.769
		STEM.Medicine & Health                       0.666
		STEM.Physics                                 0.675
		STEM.STEM*                                   0.897
		STEM.Space                                   0.878
		STEM.Technology                              0.68
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.996
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.964
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.684, macro=0.506):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.429
		Culture.Food and drink                       0.397
		Culture.Internet culture                     0.353
		Culture.Linguistics                          0.808
		Culture.Literature                           0.537
		Culture.Media.Books                          0.497
		Culture.Media.Entertainment                  0.34
		Culture.Media.Films                          0.739
		Culture.Media.Media*                         0.624
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.64
		Culture.Media.Software                       0.149
		Culture.Media.Television                     0.664
		Culture.Media.Video games                    0.626
		Culture.Performing arts                      0.476
		Culture.Philosophy and religion              0.516
		Culture.Sports                               0.965
		Culture.Visual arts.Architecture             0.709
		Culture.Visual arts.Comics and Anime         0.429
		Culture.Visual arts.Fashion                  0.22
		Culture.Visual arts.Visual arts*             0.583
		Geography.Geographical                       0.602
		Geography.Regions.Africa.Africa*             0.208
		Geography.Regions.Africa.Central Africa      0.118
		Geography.Regions.Africa.Eastern Africa      0.144
		Geography.Regions.Africa.Northern Africa     0.241
		Geography.Regions.Africa.Southern Africa     0.241
		Geography.Regions.Africa.Western Africa      0.193
		Geography.Regions.Americas.Central America   0.31
		Geography.Regions.Americas.North America     0.861
		Geography.Regions.Americas.South America     0.488
		Geography.Regions.Asia.Asia*                 0.408
		Geography.Regions.Asia.Central Asia          0.149
		Geography.Regions.Asia.East Asia             0.395
		Geography.Regions.Asia.North Asia            0.132
		Geography.Regions.Asia.South Asia            0.837
		Geography.Regions.Asia.Southeast Asia        0.392
		Geography.Regions.Asia.West Asia             0.772
		Geography.Regions.Europe.Eastern Europe      0.639
		Geography.Regions.Europe.Europe*             0.593
		Geography.Regions.Europe.Northern Europe     0.717
		Geography.Regions.Europe.Southern Europe     0.77
		Geography.Regions.Europe.Western Europe      0.824
		Geography.Regions.Oceania                    0.59
		History and Society.Business and economics   0.449
		History and Society.Education                0.598
		History and Society.History                  0.31
		History and Society.Military and warfare     0.523
		History and Society.Politics and government  0.523
		History and Society.Society                  0.323
		History and Society.Transportation           0.865
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.265
		STEM.Computing                               0.256
		STEM.Earth and environment                   0.538
		STEM.Engineering                             0.654
		STEM.Libraries & Information                 0.295
		STEM.Mathematics                             0.231
		STEM.Medicine & Health                       0.627
		STEM.Physics                                 0.158
		STEM.STEM*                                   0.709
		STEM.Space                                   0.856
		STEM.Technology                              0.239
		-------------------------------------------  -----
	!precision (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.997
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
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.991
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.982
		History and Society.Society                  0.99
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
		STEM.STEM*                                   0.992
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.639, macro=0.508):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.55
		Culture.Food and drink                       0.486
		Culture.Internet culture                     0.481
		Culture.Linguistics                          0.778
		Culture.Literature                           0.617
		Culture.Media.Books                          0.554
		Culture.Media.Entertainment                  0.37
		Culture.Media.Films                          0.732
		Culture.Media.Media*                         0.716
		Culture.Media.Music                          0.829
		Culture.Media.Radio                          0.609
		Culture.Media.Software                       0.248
		Culture.Media.Television                     0.651
		Culture.Media.Video games                    0.733
		Culture.Performing arts                      0.549
		Culture.Philosophy and religion              0.494
		Culture.Sports                               0.911
		Culture.Visual arts.Architecture             0.694
		Culture.Visual arts.Comics and Anime         0.562
		Culture.Visual arts.Fashion                  0.342
		Culture.Visual arts.Visual arts*             0.638
		Geography.Geographical                       0.621
		Geography.Regions.Africa.Africa*             0.282
		Geography.Regions.Africa.Central Africa      0.15
		Geography.Regions.Africa.Eastern Africa      0.192
		Geography.Regions.Africa.Northern Africa     0.302
		Geography.Regions.Africa.Southern Africa     0.303
		Geography.Regions.Africa.Western Africa      0.267
		Geography.Regions.Americas.Central America   0.195
		Geography.Regions.Americas.North America     0.466
		Geography.Regions.Americas.South America     0.415
		Geography.Regions.Asia.Asia*                 0.458
		Geography.Regions.Asia.Central Asia          0.203
		Geography.Regions.Asia.East Asia             0.404
		Geography.Regions.Asia.North Asia            0.194
		Geography.Regions.Asia.South Asia            0.58
		Geography.Regions.Asia.Southeast Asia        0.234
		Geography.Regions.Asia.West Asia             0.611
		Geography.Regions.Europe.Eastern Europe      0.533
		Geography.Regions.Europe.Europe*             0.557
		Geography.Regions.Europe.Northern Europe     0.247
		Geography.Regions.Europe.Southern Europe     0.533
		Geography.Regions.Europe.Western Europe      0.574
		Geography.Regions.Oceania                    0.465
		History and Society.Business and economics   0.504
		History and Society.Education                0.564
		History and Society.History                  0.375
		History and Society.Military and warfare     0.59
		History and Society.Politics and government  0.438
		History and Society.Society                  0.284
		History and Society.Transportation           0.883
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.391
		STEM.Computing                               0.383
		STEM.Earth and environment                   0.579
		STEM.Engineering                             0.725
		STEM.Libraries & Information                 0.418
		STEM.Mathematics                             0.356
		STEM.Medicine & Health                       0.646
		STEM.Physics                                 0.256
		STEM.STEM*                                   0.792
		STEM.Space                                   0.867
		STEM.Technology                              0.354
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
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
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.986
		History and Society.Society                  0.992
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
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.997
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.944
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.973
		History and Society.Society                  0.984
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
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
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.004
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.036
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.007
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.03
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.01
		History and Society.Society                  0.007
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.95, macro=0.954):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.969
		Culture.Literature                           0.972
		Culture.Media.Books                          0.975
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.976
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.935
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.94
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.982
		Culture.Visual arts.Visual arts*             0.967
		Geography.Geographical                       0.962
		Geography.Regions.Africa.Africa*             0.927
		Geography.Regions.Africa.Central Africa      0.946
		Geography.Regions.Africa.Eastern Africa      0.895
		Geography.Regions.Africa.Northern Africa     0.935
		Geography.Regions.Africa.Southern Africa     0.945
		Geography.Regions.Africa.Western Africa      0.963
		Geography.Regions.Americas.Central America   0.914
		Geography.Regions.Americas.North America     0.904
		Geography.Regions.Americas.South America     0.928
		Geography.Regions.Asia.Asia*                 0.897
		Geography.Regions.Asia.Central Asia          0.949
		Geography.Regions.Asia.East Asia             0.929
		Geography.Regions.Asia.North Asia            0.96
		Geography.Regions.Asia.South Asia            0.913
		Geography.Regions.Asia.Southeast Asia        0.889
		Geography.Regions.Asia.West Asia             0.94
		Geography.Regions.Europe.Eastern Europe      0.941
		Geography.Regions.Europe.Europe*             0.911
		Geography.Regions.Europe.Northern Europe     0.894
		Geography.Regions.Europe.Southern Europe     0.925
		Geography.Regions.Europe.Western Europe      0.931
		Geography.Regions.Oceania                    0.925
		History and Society.Business and economics   0.962
		History and Society.Education                0.964
		History and Society.History                  0.94
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.913
		History and Society.Society                  0.885
		History and Society.Transportation           0.985
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.984
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.969
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.954
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.967
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.977
		STEM.Space                                   0.987
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.672, macro=0.485):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.92
		Culture.Biography.Women                      0.531
		Culture.Food and drink                       0.444
		Culture.Internet culture                     0.611
		Culture.Linguistics                          0.776
		Culture.Literature                           0.669
		Culture.Media.Books                          0.502
		Culture.Media.Entertainment                  0.255
		Culture.Media.Films                          0.754
		Culture.Media.Media*                         0.812
		Culture.Media.Music                          0.87
		Culture.Media.Radio                          0.403
		Culture.Media.Software                       0.221
		Culture.Media.Television                     0.608
		Culture.Media.Video games                    0.698
		Culture.Performing arts                      0.487
		Culture.Philosophy and religion              0.445
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.681
		Culture.Visual arts.Comics and Anime         0.606
		Culture.Visual arts.Fashion                  0.262
		Culture.Visual arts.Visual arts*             0.686
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.251
		Geography.Regions.Africa.Central Africa      0.047
		Geography.Regions.Africa.Eastern Africa      0.039
		Geography.Regions.Africa.Northern Africa     0.137
		Geography.Regions.Africa.Southern Africa     0.182
		Geography.Regions.Africa.Western Africa      0.135
		Geography.Regions.Americas.Central America   0.108
		Geography.Regions.Americas.North America     0.604
		Geography.Regions.Americas.South America     0.356
		Geography.Regions.Asia.Asia*                 0.49
		Geography.Regions.Asia.Central Asia          0.086
		Geography.Regions.Asia.East Asia             0.349
		Geography.Regions.Asia.North Asia            0.1
		Geography.Regions.Asia.South Asia            0.556
		Geography.Regions.Asia.Southeast Asia        0.162
		Geography.Regions.Asia.West Asia             0.557
		Geography.Regions.Europe.Eastern Europe      0.496
		Geography.Regions.Europe.Europe*             0.63
		Geography.Regions.Europe.Northern Europe     0.366
		Geography.Regions.Europe.Southern Europe     0.517
		Geography.Regions.Europe.Western Europe      0.576
		Geography.Regions.Oceania                    0.427
		History and Society.Business and economics   0.464
		History and Society.Education                0.516
		History and Society.History                  0.301
		History and Society.Military and warfare     0.666
		History and Society.Politics and government  0.41
		History and Society.Society                  0.234
		History and Society.Transportation           0.903
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.407
		STEM.Computing                               0.37
		STEM.Earth and environment                   0.54
		STEM.Engineering                             0.742
		STEM.Libraries & Information                 0.315
		STEM.Mathematics                             0.352
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.263
		STEM.STEM*                                   0.906
		STEM.Space                                   0.893
		STEM.Technology                              0.343
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Internet culture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}}}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}}

