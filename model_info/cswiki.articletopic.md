Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'population_rates': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_features': 'log2', 'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'tol': 0.0001, 'validation_fraction': 0.1, 'multilabel': True, 'min_impurity_split': None, 'n_iter_no_change': None, 'init': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'subsample': 1.0, 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'max_depth': 5, 'n_estimators': 150, 'center': False, 'warm_start': False, 'scale': False, 'random_state': None, 'min_samples_leaf': 1, 'presort': 'auto', 'max_leaf_nodes': None}
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
	counts (n=60138):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16585  -->  15237  1348   845  42708
			'Culture.Biography.Women'                       4180  -->   3476   704   282  55676
			'Culture.Food and drink'                        1583  -->   1110   473   129  58426
			'Culture.Internet culture'                      3169  -->   2599   570   228  56741
			'Culture.Linguistics'                           1605  -->   1129   476    95  58438
			'Culture.Literature'                            4987  -->   3582  1405   460  54691
			'Culture.Media.Books'                           1675  -->   1310   365   133  58330
			'Culture.Media.Entertainment'                   2249  -->    983  1266   298  57591
			'Culture.Media.Films'                           2597  -->   2165   432   116  57425
			'Culture.Media.Media*'                         14346  -->  12472  1874  1317  44475
			'Culture.Media.Music'                           3323  -->   2807   516   278  56537
			'Culture.Media.Radio'                            393  -->    155   238    35  59710
			'Culture.Media.Software'                        2285  -->   1717   568   382  57471
			'Culture.Media.Television'                      2531  -->   2089   442   107  57500
			'Culture.Media.Video games'                     1963  -->   1796   167    44  58131
			'Culture.Performing arts'                       1477  -->    904   573   123  58538
			'Culture.Philosophy and religion'               4372  -->   2465  1907   464  55302
			'Culture.Sports'                                5971  -->   5283   688   185  53982
			'Culture.Visual arts.Architecture'              2301  -->   1622   679   242  57595
			'Culture.Visual arts.Comics and Anime'          1633  -->   1370   263    59  58446
			'Culture.Visual arts.Fashion'                   1054  -->    664   390    84  59000
			'Culture.Visual arts.Visual arts*'              5844  -->   4271  1573   445  53849
			'Geography.Geographical'                        4550  -->   3234  1316   739  54849
			'Geography.Regions.Africa.Africa*'              4073  -->   2560  1513   339  55726
			'Geography.Regions.Africa.Central Africa'        747  -->    345   402    67  59324
			'Geography.Regions.Africa.Eastern Africa'        453  -->    218   235    51  59634
			'Geography.Regions.Africa.Northern Africa'      1515  -->    879   636   126  58497
			'Geography.Regions.Africa.Southern Africa'       691  -->    315   376    52  59395
			'Geography.Regions.Africa.Western Africa'        184  -->     85    99    41  59913
			'Geography.Regions.Americas.Central America'    1344  -->    643   701    72  58722
			'Geography.Regions.Americas.North America'      5968  -->   3577  2391   958  53212
			'Geography.Regions.Americas.South America'      1525  -->   1004   521    95  58518
			'Geography.Regions.Asia.Asia*'                 11835  -->   9253  2582   866  47437
			'Geography.Regions.Asia.Central Asia'           1263  -->    692   571   117  58758
			'Geography.Regions.Asia.East Asia'              2918  -->   2168   750   203  57017
			'Geography.Regions.Asia.North Asia'             3352  -->   2335  1017   330  56456
			'Geography.Regions.Asia.South Asia'             1727  -->   1179   548    97  58314
			'Geography.Regions.Asia.Southeast Asia'         1529  -->    831   698    95  58514
			'Geography.Regions.Asia.West Asia'              2706  -->   1996   710   178  57254
			'Geography.Regions.Europe.Eastern Europe'       6461  -->   4699  1762   713  52964
			'Geography.Regions.Europe.Europe*'             18092  -->  14426  3666  2644  39402
			'Geography.Regions.Europe.Northern Europe'      4012  -->   2504  1508   439  55687
			'Geography.Regions.Europe.Southern Europe'      3497  -->   2282  1215   361  56280
			'Geography.Regions.Europe.Western Europe'       5163  -->   3610  1553   649  54326
			'Geography.Regions.Oceania'                     1637  -->   1049   588    91  58410
			'History and Society.Business and economics'    3569  -->   2085  1484   374  56195
			'History and Society.Education'                 1798  -->    877   921   183  58157
			'History and Society.History'                   5463  -->   3150  2313   696  53979
			'History and Society.Military and warfare'      4979  -->   3415  1564   537  54622
			'History and Society.Politics and government'   3651  -->   1786  1865   467  56020
			'History and Society.Society'                   4394  -->   1121  3273   331  55413
			'History and Society.Transportation'            4424  -->   3985   439   178  55536
			'STEM.Biology'                                  3774  -->   3036   738   173  56191
			'STEM.Chemistry'                                1524  -->   1199   325   156  58458
			'STEM.Computing'                                2779  -->   2223   556   390  56969
			'STEM.Earth and environment'                    2187  -->   1472   715   161  57790
			'STEM.Engineering'                              2936  -->   2191   745   213  56989
			'STEM.Libraries & Information'                   716  -->    463   253    50  59372
			'STEM.Mathematics'                              1176  -->    845   331    67  58895
			'STEM.Medicine & Health'                        2023  -->   1327   696   205  57910
			'STEM.Physics'                                  1452  -->    976   476   152  58534
			'STEM.STEM*'                                   18875  -->  16662  2213  1096  40167
			'STEM.Space'                                    2096  -->   1914   182    57  57985
			'STEM.Technology'                               5198  -->   3788  1410   750  54190
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.276         0.121
		Culture.Biography.Women                         0.07          0.015
		Culture.Food and drink                          0.026         0.003
		Culture.Internet culture                        0.053         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.239         0.055
		Culture.Media.Music                             0.055         0.021
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.01
		Culture.Sports                                  0.099         0.061
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.097         0.018
		Geography.Geographical                          0.076         0.021
		Geography.Regions.Africa.Africa*                0.068         0.009
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.099         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.197         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.049         0.012
		Geography.Regions.Asia.North Asia               0.056         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.045         0.012
		Geography.Regions.Europe.Eastern Europe         0.107         0.018
		Geography.Regions.Europe.Europe*                0.301         0.082
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
		STEM.Biology                                    0.063         0.035
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.036         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.314         0.066
		STEM.Space                                      0.035         0.004
		STEM.Technology                                 0.086         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.057
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.028
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.055
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.058
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.01
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.026
		Geography.Regions.Europe.Europe*             0.123
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.026
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.016
		History and Society.Society                  0.008
		History and Society.Transportation           0.018
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.942
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.99
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.877
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.982
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.762, macro=0.683):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.919
		Culture.Biography.Women                      0.832
		Culture.Food and drink                       0.701
		Culture.Internet culture                     0.82
		Culture.Linguistics                          0.703
		Culture.Literature                           0.718
		Culture.Media.Books                          0.782
		Culture.Media.Entertainment                  0.437
		Culture.Media.Films                          0.834
		Culture.Media.Media*                         0.869
		Culture.Media.Music                          0.845
		Culture.Media.Radio                          0.394
		Culture.Media.Software                       0.751
		Culture.Media.Television                     0.825
		Culture.Media.Video games                    0.915
		Culture.Performing arts                      0.612
		Culture.Philosophy and religion              0.564
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.705
		Culture.Visual arts.Comics and Anime         0.839
		Culture.Visual arts.Fashion                  0.63
		Culture.Visual arts.Visual arts*             0.731
		Geography.Geographical                       0.711
		Geography.Regions.Africa.Africa*             0.629
		Geography.Regions.Africa.Central Africa      0.462
		Geography.Regions.Africa.Eastern Africa      0.481
		Geography.Regions.Africa.Northern Africa     0.58
		Geography.Regions.Africa.Southern Africa     0.456
		Geography.Regions.Africa.Western Africa      0.462
		Geography.Regions.Americas.Central America   0.478
		Geography.Regions.Americas.North America     0.599
		Geography.Regions.Americas.South America     0.658
		Geography.Regions.Asia.Asia*                 0.782
		Geography.Regions.Asia.Central Asia          0.548
		Geography.Regions.Asia.East Asia             0.743
		Geography.Regions.Asia.North Asia            0.697
		Geography.Regions.Asia.South Asia            0.683
		Geography.Regions.Asia.Southeast Asia        0.543
		Geography.Regions.Asia.West Asia             0.738
		Geography.Regions.Europe.Eastern Europe      0.727
		Geography.Regions.Europe.Europe*             0.797
		Geography.Regions.Europe.Northern Europe     0.624
		Geography.Regions.Europe.Southern Europe     0.653
		Geography.Regions.Europe.Western Europe      0.699
		Geography.Regions.Oceania                    0.641
		History and Society.Business and economics   0.584
		History and Society.Education                0.488
		History and Society.History                  0.577
		History and Society.Military and warfare     0.686
		History and Society.Politics and government  0.489
		History and Society.Society                  0.255
		History and Society.Transportation           0.901
		STEM.Biology                                 0.804
		STEM.Chemistry                               0.787
		STEM.Computing                               0.8
		STEM.Earth and environment                   0.673
		STEM.Engineering                             0.746
		STEM.Libraries & Information                 0.647
		STEM.Mathematics                             0.719
		STEM.Medicine & Health                       0.656
		STEM.Physics                                 0.672
		STEM.STEM*                                   0.883
		STEM.Space                                   0.913
		STEM.Technology                              0.729
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.937
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	precision (micro=0.684, macro=0.546):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.717
		Culture.Food and drink                       0.451
		Culture.Internet culture                     0.437
		Culture.Linguistics                          0.78
		Culture.Literature                           0.567
		Culture.Media.Books                          0.601
		Culture.Media.Entertainment                  0.254
		Culture.Media.Films                          0.83
		Culture.Media.Media*                         0.639
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.613
		Culture.Media.Software                       0.131
		Culture.Media.Television                     0.801
		Culture.Media.Video games                    0.781
		Culture.Performing arts                      0.474
		Culture.Philosophy and religion              0.418
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.65
		Culture.Visual arts.Comics and Anime         0.668
		Culture.Visual arts.Fashion                  0.286
		Culture.Visual arts.Visual arts*             0.624
		Geography.Geographical                       0.538
		Geography.Regions.Africa.Africa*             0.473
		Geography.Regions.Africa.Central Africa      0.225
		Geography.Regions.Africa.Eastern Africa      0.222
		Geography.Regions.Africa.Northern Africa     0.269
		Geography.Regions.Africa.Southern Africa     0.408
		Geography.Regions.Africa.Western Africa      0.337
		Geography.Regions.Americas.Central America   0.578
		Geography.Regions.Americas.North America     0.697
		Geography.Regions.Americas.South America     0.739
		Geography.Regions.Asia.Asia*                 0.71
		Geography.Regions.Asia.Central Asia          0.182
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.406
		Geography.Regions.Asia.South Asia            0.874
		Geography.Regions.Asia.Southeast Asia        0.68
		Geography.Regions.Asia.West Asia             0.74
		Geography.Regions.Europe.Eastern Europe      0.507
		Geography.Regions.Europe.Europe*             0.53
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.591
		Geography.Regions.Europe.Western Europe      0.556
		Geography.Regions.Oceania                    0.874
		History and Society.Business and economics   0.467
		History and Society.Education                0.556
		History and Society.History                  0.335
		History and Society.Military and warfare     0.525
		History and Society.Politics and government  0.498
		History and Society.Society                  0.266
		History and Society.Transportation           0.825
		STEM.Biology                                 0.904
		STEM.Chemistry                               0.336
		STEM.Computing                               0.252
		STEM.Earth and environment                   0.537
		STEM.Engineering                             0.539
		STEM.Libraries & Information                 0.347
		STEM.Mathematics                             0.228
		STEM.Medicine & Health                       0.549
		STEM.Physics                                 0.197
		STEM.STEM*                                   0.7
		STEM.Space                                   0.801
		STEM.Technology                              0.218
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.713, macro=0.588):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.892
		Culture.Biography.Women                      0.77
		Culture.Food and drink                       0.549
		Culture.Internet culture                     0.57
		Culture.Linguistics                          0.74
		Culture.Literature                           0.634
		Culture.Media.Books                          0.68
		Culture.Media.Entertainment                  0.321
		Culture.Media.Films                          0.832
		Culture.Media.Media*                         0.737
		Culture.Media.Music                          0.816
		Culture.Media.Radio                          0.48
		Culture.Media.Software                       0.223
		Culture.Media.Television                     0.813
		Culture.Media.Video games                    0.843
		Culture.Performing arts                      0.534
		Culture.Philosophy and religion              0.48
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.676
		Culture.Visual arts.Comics and Anime         0.744
		Culture.Visual arts.Fashion                  0.394
		Culture.Visual arts.Visual arts*             0.673
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.54
		Geography.Regions.Africa.Central Africa      0.303
		Geography.Regions.Africa.Eastern Africa      0.304
		Geography.Regions.Africa.Northern Africa     0.368
		Geography.Regions.Africa.Southern Africa     0.431
		Geography.Regions.Africa.Western Africa      0.39
		Geography.Regions.Americas.Central America   0.523
		Geography.Regions.Americas.North America     0.645
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.744
		Geography.Regions.Asia.Central Asia          0.273
		Geography.Regions.Asia.East Asia             0.733
		Geography.Regions.Asia.North Asia            0.513
		Geography.Regions.Asia.South Asia            0.767
		Geography.Regions.Asia.Southeast Asia        0.604
		Geography.Regions.Asia.West Asia             0.739
		Geography.Regions.Europe.Eastern Europe      0.598
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.663
		Geography.Regions.Europe.Southern Europe     0.62
		Geography.Regions.Europe.Western Europe      0.619
		Geography.Regions.Oceania                    0.739
		History and Society.Business and economics   0.519
		History and Society.Education                0.52
		History and Society.History                  0.424
		History and Society.Military and warfare     0.595
		History and Society.Politics and government  0.493
		History and Society.Society                  0.26
		History and Society.Transportation           0.861
		STEM.Biology                                 0.851
		STEM.Chemistry                               0.471
		STEM.Computing                               0.383
		STEM.Earth and environment                   0.598
		STEM.Engineering                             0.626
		STEM.Libraries & Information                 0.452
		STEM.Mathematics                             0.346
		STEM.Medicine & Health                       0.598
		STEM.Physics                                 0.305
		STEM.STEM*                                   0.781
		STEM.Space                                   0.853
		STEM.Technology                              0.336
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.926
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.063
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.008
		History and Society.Society                  0.006
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.014
		-------------------------------------------  -----
	roc_auc (micro=0.97, macro=0.97):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.978
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.975
		Culture.Literature                           0.974
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.962
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.948
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.972
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.975
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.965
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.956
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.959
		Geography.Regions.Africa.Western Africa      0.883
		Geography.Regions.Americas.Central America   0.966
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.973
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.97
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.97
		Geography.Regions.Asia.South Asia            0.971
		Geography.Regions.Asia.Southeast Asia        0.968
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.966
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.97
		Geography.Regions.Europe.Western Europe      0.969
		Geography.Regions.Oceania                    0.973
		History and Society.Business and economics   0.963
		History and Society.Education                0.962
		History and Society.History                  0.953
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.949
		History and Society.Society                  0.895
		History and Society.Transportation           0.986
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.985
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.983
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.975
		STEM.Space                                   0.992
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.76, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.954
		Culture.Biography.Women                      0.787
		Culture.Food and drink                       0.569
		Culture.Internet culture                     0.761
		Culture.Linguistics                          0.73
		Culture.Literature                           0.691
		Culture.Media.Books                          0.712
		Culture.Media.Entertainment                  0.243
		Culture.Media.Films                          0.87
		Culture.Media.Media*                         0.859
		Culture.Media.Music                          0.85
		Culture.Media.Radio                          0.318
		Culture.Media.Software                       0.226
		Culture.Media.Television                     0.865
		Culture.Media.Video games                    0.913
		Culture.Performing arts                      0.517
		Culture.Philosophy and religion              0.45
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.707
		Culture.Visual arts.Comics and Anime         0.789
		Culture.Visual arts.Fashion                  0.317
		Culture.Visual arts.Visual arts*             0.722
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.515
		Geography.Regions.Africa.Central Africa      0.223
		Geography.Regions.Africa.Eastern Africa      0.11
		Geography.Regions.Africa.Northern Africa     0.295
		Geography.Regions.Africa.Southern Africa     0.248
		Geography.Regions.Africa.Western Africa      0.162
		Geography.Regions.Americas.Central America   0.513
		Geography.Regions.Americas.North America     0.697
		Geography.Regions.Americas.South America     0.722
		Geography.Regions.Asia.Asia*                 0.8
		Geography.Regions.Asia.Central Asia          0.168
		Geography.Regions.Asia.East Asia             0.769
		Geography.Regions.Asia.North Asia            0.518
		Geography.Regions.Asia.South Asia            0.808
		Geography.Regions.Asia.Southeast Asia        0.592
		Geography.Regions.Asia.West Asia             0.769
		Geography.Regions.Europe.Eastern Europe      0.622
		Geography.Regions.Europe.Europe*             0.698
		Geography.Regions.Europe.Northern Europe     0.704
		Geography.Regions.Europe.Southern Europe     0.64
		Geography.Regions.Europe.Western Europe      0.64
		Geography.Regions.Oceania                    0.789
		History and Society.Business and economics   0.496
		History and Society.Education                0.512
		History and Society.History                  0.442
		History and Society.Military and warfare     0.659
		History and Society.Politics and government  0.478
		History and Society.Society                  0.185
		History and Society.Transportation           0.917
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.467
		STEM.Computing                               0.412
		STEM.Earth and environment                   0.561
		STEM.Engineering                             0.693
		STEM.Libraries & Information                 0.326
		STEM.Mathematics                             0.429
		STEM.Medicine & Health                       0.623
		STEM.Physics                                 0.266
		STEM.STEM*                                   0.888
		STEM.Space                                   0.914
		STEM.Technology                              0.473
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}}}}}

