Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'population_rates': None, 'learning_rate': 0.1, 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'loss': 'deviance', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'max_leaf_nodes': None, 'presort': 'auto', 'n_estimators': 150, 'init': None, 'subsample': 1.0, 'scale': False, 'tol': 0.0001, 'multilabel': True, 'warm_start': False, 'center': False, 'min_impurity_decrease': 0.0, 'max_features': 'log2', 'min_impurity_split': None, 'n_iter_no_change': None, 'label_weights': {}, 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'verbose': 0, 'criterion': 'friedman_mse', 'min_samples_split': 2}
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
	counts (n=60630):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14517  -->  13036  1481   644  45469
			'Culture.Biography.Women'                       5074  -->   4116   958   799  54757
			'Culture.Food and drink'                        1379  -->    968   411   133  59118
			'Culture.Internet culture'                      3594  -->   2916   678   254  56782
			'Culture.Linguistics'                           1508  -->   1137   371    77  59045
			'Culture.Literature'                            5505  -->   4262  1243   509  54616
			'Culture.Media.Books'                           1440  -->   1013   427   149  59041
			'Culture.Media.Entertainment'                   1946  -->    969   977   178  58506
			'Culture.Media.Films'                           2565  -->   2017   548   154  57911
			'Culture.Media.Media*'                         13258  -->  11424  1834  1441  45931
			'Culture.Media.Music'                           2857  -->   2432   425   218  57555
			'Culture.Media.Radio'                            293  -->    207    86    39  60298
			'Culture.Media.Software'                        2267  -->   1742   525   356  58007
			'Culture.Media.Television'                      2015  -->   1381   634   149  58466
			'Culture.Media.Video games'                     2214  -->   2027   187    58  58358
			'Culture.Performing arts'                       1403  -->    934   469   144  59083
			'Culture.Philosophy and religion'               3001  -->   1581  1420   277  57352
			'Culture.Sports'                                4102  -->   3587   515   149  56379
			'Culture.Visual arts.Architecture'              1813  -->   1324   489   179  58638
			'Culture.Visual arts.Comics and Anime'          2236  -->   1926   310   107  58287
			'Culture.Visual arts.Fashion'                   1521  -->   1268   253    94  59015
			'Culture.Visual arts.Visual arts*'              6095  -->   4634  1461   488  54047
			'Geography.Geographical'                        3932  -->   2461  1471   579  56119
			'Geography.Regions.Africa.Africa*'              5722  -->   2561  3161   662  54246
			'Geography.Regions.Africa.Central Africa'       1184  -->    326   858   125  59321
			'Geography.Regions.Africa.Eastern Africa'        436  -->    131   305    64  60130
			'Geography.Regions.Africa.Northern Africa'      1459  -->    586   873   118  59053
			'Geography.Regions.Africa.Southern Africa'      1196  -->    461   735    84  59350
			'Geography.Regions.Africa.Western Africa'        679  -->    302   377    87  59864
			'Geography.Regions.Americas.Central America'    1646  -->    226  1420    91  58893
			'Geography.Regions.Americas.North America'      5360  -->   2143  3217   290  54980
			'Geography.Regions.Americas.South America'      2213  -->    766  1447   135  58282
			'Geography.Regions.Asia.Asia*'                 14732  -->   8570  6162  1755  44143
			'Geography.Regions.Asia.Central Asia'           1070  -->    338   732   130  59430
			'Geography.Regions.Asia.East Asia'              5746  -->   2917  2829   442  54442
			'Geography.Regions.Asia.North Asia'             2600  -->   1004  1596   133  57897
			'Geography.Regions.Asia.South Asia'             1954  -->    897  1057    70  58606
			'Geography.Regions.Asia.Southeast Asia'         2623  -->    485  2138    76  57931
			'Geography.Regions.Asia.West Asia'              2103  -->   1033  1070   103  58424
			'Geography.Regions.Europe.Eastern Europe'       4273  -->   1950  2323   175  56182
			'Geography.Regions.Europe.Europe*'             13278  -->   7664  5614  1411  45941
			'Geography.Regions.Europe.Northern Europe'      2831  -->    569  2262   154  57645
			'Geography.Regions.Europe.Southern Europe'      2751  -->   1256  1495   121  57758
			'Geography.Regions.Europe.Western Europe'       3991  -->   1830  2161   107  56532
			'Geography.Regions.Oceania'                     1750  -->    474  1276   184  58696
			'History and Society.Business and economics'    3358  -->   2049  1309   448  56824
			'History and Society.Education'                 1594  -->    916   678   122  58914
			'History and Society.History'                   4277  -->   2032  2245   685  55668
			'History and Society.Military and warfare'      4357  -->   3132  1225   426  55847
			'History and Society.Politics and government'   3203  -->   1623  1580   515  56912
			'History and Society.Society'                   4458  -->   1401  3057   306  55866
			'History and Society.Transportation'            3527  -->   3249   278    97  57006
			'STEM.Biology'                                  6725  -->   6160   565   183  53722
			'STEM.Chemistry'                                1438  -->   1105   333   174  59018
			'STEM.Computing'                                2397  -->   1903   494   349  57884
			'STEM.Earth and environment'                    1693  -->   1157   536   175  58762
			'STEM.Engineering'                              2956  -->   2443   513   138  57536
			'STEM.Libraries & Information'                   485  -->    379   106    48  60097
			'STEM.Mathematics'                               912  -->    724   188    51  59667
			'STEM.Medicine & Health'                        1787  -->   1287   500   136  58707
			'STEM.Physics'                                  1391  -->   1011   380   181  59058
			'STEM.STEM*'                                   20086  -->  18386  1700   977  39567
			'STEM.Space'                                    1569  -->   1443   126    48  59013
			'STEM.Technology'                               4179  -->   2972  1207   628  55823
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.239         0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.042         0.012
		Culture.Media.Media*                            0.219         0.055
		Culture.Media.Music                             0.047         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.049         0.01
		Culture.Sports                                  0.068         0.061
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.088         0.064
		Geography.Regions.Americas.South America        0.037         0.007
		Geography.Regions.Asia.Asia*                    0.243         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.095         0.012
		Geography.Regions.Asia.North Asia               0.043         0.006
		Geography.Regions.Asia.South Asia               0.032         0.017
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.07          0.018
		Geography.Regions.Europe.Europe*                0.219         0.082
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.045         0.014
		Geography.Regions.Europe.Western Europe         0.066         0.021
		Geography.Regions.Oceania                       0.029         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.026         0.008
		History and Society.History                     0.071         0.011
		History and Society.Military and warfare        0.072         0.015
		History and Society.Politics and government     0.053         0.016
		History and Society.Society                     0.074         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.111         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.331         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.046, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.121
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.016
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.03
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.067
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.009
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.074
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.008
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.008
		History and Society.Business and economics   0.014
		History and Society.Education                0.007
		History and Society.History                  0.017
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.017
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.083
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.954, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.933
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.926
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.983
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.917
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.675, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.811
		Culture.Food and drink                       0.702
		Culture.Internet culture                     0.811
		Culture.Linguistics                          0.754
		Culture.Literature                           0.774
		Culture.Media.Books                          0.703
		Culture.Media.Entertainment                  0.498
		Culture.Media.Films                          0.786
		Culture.Media.Media*                         0.862
		Culture.Media.Music                          0.851
		Culture.Media.Radio                          0.706
		Culture.Media.Software                       0.768
		Culture.Media.Television                     0.685
		Culture.Media.Video games                    0.916
		Culture.Performing arts                      0.666
		Culture.Philosophy and religion              0.527
		Culture.Sports                               0.874
		Culture.Visual arts.Architecture             0.73
		Culture.Visual arts.Comics and Anime         0.861
		Culture.Visual arts.Fashion                  0.834
		Culture.Visual arts.Visual arts*             0.76
		Geography.Geographical                       0.626
		Geography.Regions.Africa.Africa*             0.448
		Geography.Regions.Africa.Central Africa      0.275
		Geography.Regions.Africa.Eastern Africa      0.3
		Geography.Regions.Africa.Northern Africa     0.402
		Geography.Regions.Africa.Southern Africa     0.385
		Geography.Regions.Africa.Western Africa      0.445
		Geography.Regions.Americas.Central America   0.137
		Geography.Regions.Americas.North America     0.4
		Geography.Regions.Americas.South America     0.346
		Geography.Regions.Asia.Asia*                 0.582
		Geography.Regions.Asia.Central Asia          0.316
		Geography.Regions.Asia.East Asia             0.508
		Geography.Regions.Asia.North Asia            0.386
		Geography.Regions.Asia.South Asia            0.459
		Geography.Regions.Asia.Southeast Asia        0.185
		Geography.Regions.Asia.West Asia             0.491
		Geography.Regions.Europe.Eastern Europe      0.456
		Geography.Regions.Europe.Europe*             0.577
		Geography.Regions.Europe.Northern Europe     0.201
		Geography.Regions.Europe.Southern Europe     0.457
		Geography.Regions.Europe.Western Europe      0.459
		Geography.Regions.Oceania                    0.271
		History and Society.Business and economics   0.61
		History and Society.Education                0.575
		History and Society.History                  0.475
		History and Society.Military and warfare     0.719
		History and Society.Politics and government  0.507
		History and Society.Society                  0.314
		History and Society.Transportation           0.921
		STEM.Biology                                 0.916
		STEM.Chemistry                               0.768
		STEM.Computing                               0.794
		STEM.Earth and environment                   0.683
		STEM.Engineering                             0.826
		STEM.Libraries & Information                 0.781
		STEM.Mathematics                             0.794
		STEM.Medicine & Health                       0.72
		STEM.Physics                                 0.727
		STEM.STEM*                                   0.915
		STEM.Space                                   0.92
		STEM.Technology                              0.711
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.995
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.962
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.695, macro=0.534):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.464
		Culture.Food and drink                       0.447
		Culture.Internet culture                     0.408
		Culture.Linguistics                          0.826
		Culture.Literature                           0.561
		Culture.Media.Books                          0.55
		Culture.Media.Entertainment                  0.396
		Culture.Media.Films                          0.778
		Culture.Media.Media*                         0.624
		Culture.Media.Music                          0.83
		Culture.Media.Radio                          0.72
		Culture.Media.Software                       0.143
		Culture.Media.Television                     0.709
		Culture.Media.Video games                    0.731
		Culture.Performing arts                      0.458
		Culture.Philosophy and religion              0.537
		Culture.Sports                               0.956
		Culture.Visual arts.Architecture             0.726
		Culture.Visual arts.Comics and Anime         0.532
		Culture.Visual arts.Fashion                  0.322
		Culture.Visual arts.Visual arts*             0.612
		Geography.Geographical                       0.572
		Geography.Regions.Africa.Africa*             0.243
		Geography.Regions.Africa.Central Africa      0.085
		Geography.Regions.Africa.Eastern Africa      0.125
		Geography.Regions.Africa.Northern Africa     0.216
		Geography.Regions.Africa.Southern Africa     0.265
		Geography.Regions.Africa.Western Africa      0.188
		Geography.Regions.Americas.Central America   0.237
		Geography.Regions.Americas.North America     0.838
		Geography.Regions.Americas.South America     0.511
		Geography.Regions.Asia.Asia*                 0.46
		Geography.Regions.Asia.Central Asia          0.104
		Geography.Regions.Asia.East Asia             0.439
		Geography.Regions.Asia.North Asia            0.49
		Geography.Regions.Asia.South Asia            0.867
		Geography.Regions.Asia.Southeast Asia        0.472
		Geography.Regions.Asia.West Asia             0.769
		Geography.Regions.Europe.Eastern Europe      0.734
		Geography.Regions.Europe.Europe*             0.633
		Geography.Regions.Europe.Northern Europe     0.695
		Geography.Regions.Europe.Southern Europe     0.755
		Geography.Regions.Europe.Western Europe      0.837
		Geography.Regions.Oceania                    0.594
		History and Society.Business and economics   0.436
		History and Society.Education                0.692
		History and Society.History                  0.303
		History and Society.Military and warfare     0.598
		History and Society.Politics and government  0.486
		History and Society.Society                  0.327
		History and Society.Transportation           0.901
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.309
		STEM.Computing                               0.275
		STEM.Earth and environment                   0.525
		STEM.Engineering                             0.668
		STEM.Libraries & Information                 0.404
		STEM.Mathematics                             0.303
		STEM.Medicine & Health                       0.671
		STEM.Physics                                 0.184
		STEM.STEM*                                   0.727
		STEM.Space                                   0.83
		STEM.Technology                              0.25
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.664, macro=0.541):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.59
		Culture.Food and drink                       0.546
		Culture.Internet culture                     0.543
		Culture.Linguistics                          0.788
		Culture.Literature                           0.65
		Culture.Media.Books                          0.618
		Culture.Media.Entertainment                  0.441
		Culture.Media.Films                          0.782
		Culture.Media.Media*                         0.724
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.713
		Culture.Media.Software                       0.241
		Culture.Media.Television                     0.697
		Culture.Media.Video games                    0.813
		Culture.Performing arts                      0.543
		Culture.Philosophy and religion              0.532
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.728
		Culture.Visual arts.Comics and Anime         0.658
		Culture.Visual arts.Fashion                  0.465
		Culture.Visual arts.Visual arts*             0.678
		Geography.Geographical                       0.598
		Geography.Regions.Africa.Africa*             0.315
		Geography.Regions.Africa.Central Africa      0.13
		Geography.Regions.Africa.Eastern Africa      0.177
		Geography.Regions.Africa.Northern Africa     0.281
		Geography.Regions.Africa.Southern Africa     0.314
		Geography.Regions.Africa.Western Africa      0.264
		Geography.Regions.Americas.Central America   0.174
		Geography.Regions.Americas.North America     0.541
		Geography.Regions.Americas.South America     0.413
		Geography.Regions.Asia.Asia*                 0.514
		Geography.Regions.Asia.Central Asia          0.157
		Geography.Regions.Asia.East Asia             0.471
		Geography.Regions.Asia.North Asia            0.432
		Geography.Regions.Asia.South Asia            0.6
		Geography.Regions.Asia.Southeast Asia        0.266
		Geography.Regions.Asia.West Asia             0.6
		Geography.Regions.Europe.Eastern Europe      0.563
		Geography.Regions.Europe.Europe*             0.604
		Geography.Regions.Europe.Northern Europe     0.312
		Geography.Regions.Europe.Southern Europe     0.569
		Geography.Regions.Europe.Western Europe      0.592
		Geography.Regions.Oceania                    0.372
		History and Society.Business and economics   0.509
		History and Society.Education                0.628
		History and Society.History                  0.37
		History and Society.Military and warfare     0.653
		History and Society.Politics and government  0.496
		History and Society.Society                  0.32
		History and Society.Transportation           0.911
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.441
		STEM.Computing                               0.408
		STEM.Earth and environment                   0.594
		STEM.Engineering                             0.739
		STEM.Libraries & Information                 0.532
		STEM.Mathematics                             0.438
		STEM.Medicine & Health                       0.695
		STEM.Physics                                 0.293
		STEM.STEM*                                   0.811
		STEM.Space                                   0.873
		STEM.Technology                              0.37
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.942
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.983
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.014
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.005
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.038
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.03
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.957, macro=0.961):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.972
		Culture.Literature                           0.98
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.97
		Culture.Media.Films                          0.981
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.955
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.977
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.954
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.99
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.933
		Geography.Regions.Africa.Central Africa      0.956
		Geography.Regions.Africa.Eastern Africa      0.903
		Geography.Regions.Africa.Northern Africa     0.939
		Geography.Regions.Africa.Southern Africa     0.953
		Geography.Regions.Africa.Western Africa      0.963
		Geography.Regions.Americas.Central America   0.915
		Geography.Regions.Americas.North America     0.924
		Geography.Regions.Americas.South America     0.933
		Geography.Regions.Asia.Asia*                 0.912
		Geography.Regions.Asia.Central Asia          0.949
		Geography.Regions.Asia.East Asia             0.947
		Geography.Regions.Asia.North Asia            0.937
		Geography.Regions.Asia.South Asia            0.93
		Geography.Regions.Asia.Southeast Asia        0.914
		Geography.Regions.Asia.West Asia             0.944
		Geography.Regions.Europe.Eastern Europe      0.932
		Geography.Regions.Europe.Europe*             0.92
		Geography.Regions.Europe.Northern Europe     0.915
		Geography.Regions.Europe.Southern Europe     0.934
		Geography.Regions.Europe.Western Europe      0.938
		Geography.Regions.Oceania                    0.911
		History and Society.Business and economics   0.968
		History and Society.Education                0.972
		History and Society.History                  0.949
		History and Society.Military and warfare     0.973
		History and Society.Politics and government  0.957
		History and Society.Society                  0.907
		History and Society.Transportation           0.988
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.988
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.983
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.981
		STEM.Space                                   0.991
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.7, macro=0.534):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.937
		Culture.Biography.Women                      0.589
		Culture.Food and drink                       0.63
		Culture.Internet culture                     0.717
		Culture.Linguistics                          0.756
		Culture.Literature                           0.739
		Culture.Media.Books                          0.628
		Culture.Media.Entertainment                  0.392
		Culture.Media.Films                          0.807
		Culture.Media.Media*                         0.811
		Culture.Media.Music                          0.875
		Culture.Media.Radio                          0.523
		Culture.Media.Software                       0.22
		Culture.Media.Television                     0.691
		Culture.Media.Video games                    0.84
		Culture.Performing arts                      0.513
		Culture.Philosophy and religion              0.462
		Culture.Sports                               0.939
		Culture.Visual arts.Architecture             0.715
		Culture.Visual arts.Comics and Anime         0.8
		Culture.Visual arts.Fashion                  0.409
		Culture.Visual arts.Visual arts*             0.716
		Geography.Geographical                       0.605
		Geography.Regions.Africa.Africa*             0.29
		Geography.Regions.Africa.Central Africa      0.048
		Geography.Regions.Africa.Eastern Africa      0.04
		Geography.Regions.Africa.Northern Africa     0.127
		Geography.Regions.Africa.Southern Africa     0.18
		Geography.Regions.Africa.Western Africa      0.111
		Geography.Regions.Americas.Central America   0.091
		Geography.Regions.Americas.North America     0.651
		Geography.Regions.Americas.South America     0.356
		Geography.Regions.Asia.Asia*                 0.569
		Geography.Regions.Asia.Central Asia          0.055
		Geography.Regions.Asia.East Asia             0.422
		Geography.Regions.Asia.North Asia            0.334
		Geography.Regions.Asia.South Asia            0.601
		Geography.Regions.Asia.Southeast Asia        0.204
		Geography.Regions.Asia.West Asia             0.534
		Geography.Regions.Europe.Eastern Europe      0.562
		Geography.Regions.Europe.Europe*             0.681
		Geography.Regions.Europe.Northern Europe     0.404
		Geography.Regions.Europe.Southern Europe     0.557
		Geography.Regions.Europe.Western Europe      0.621
		Geography.Regions.Oceania                    0.351
		History and Society.Business and economics   0.499
		History and Society.Education                0.61
		History and Society.History                  0.319
		History and Society.Military and warfare     0.702
		History and Society.Politics and government  0.453
		History and Society.Society                  0.239
		History and Society.Transportation           0.92
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.538
		STEM.Computing                               0.38
		STEM.Earth and environment                   0.576
		STEM.Engineering                             0.781
		STEM.Libraries & Information                 0.446
		STEM.Mathematics                             0.509
		STEM.Medicine & Health                       0.691
		STEM.Physics                                 0.264
		STEM.STEM*                                   0.922
		STEM.Space                                   0.927
		STEM.Technology                              0.367
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

