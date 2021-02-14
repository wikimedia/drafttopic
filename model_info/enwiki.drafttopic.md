Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'min_impurity_split': None, 'learning_rate': 0.1, 'subsample': 1.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'scale': False, 'n_estimators': 150, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'validation_fraction': 0.1, 'min_samples_leaf': 1, 'population_rates': None, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'max_features': 'log2', 'random_state': None, 'ccp_alpha': 0.0, 'center': False, 'criterion': 'friedman_mse', 'init': None, 'label_weights': {}, 'verbose': 0, 'n_iter_no_change': None, 'multilabel': True, 'max_depth': 5, 'min_samples_split': 2, 'presort': 'deprecated', 'loss': 'deviance'}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=60716):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16451  -->  13638  2813  1434  42831
			'Culture.Biography.Women'                       3989  -->   2739  1250   788  55939
			'Culture.Food and drink'                        1234  -->    722   512    88  59394
			'Culture.Internet culture'                      2694  -->   1898   796   209  57813
			'Culture.Linguistics'                           1224  -->    823   401    96  59396
			'Culture.Literature'                            4994  -->   3397  1597   507  55215
			'Culture.Media.Books'                           1788  -->   1122   666   237  58691
			'Culture.Media.Entertainment'                   1659  -->    671   988   201  58856
			'Culture.Media.Films'                           2171  -->   1624   547   199  58346
			'Culture.Media.Media*'                         13339  -->  10654  2685  1574  45803
			'Culture.Media.Music'                           2499  -->   1793   706   293  57924
			'Culture.Media.Radio'                           1118  -->    841   277    45  59553
			'Culture.Media.Software'                        1617  -->    791   826   328  58771
			'Culture.Media.Television'                      2015  -->   1292   723   220  58481
			'Culture.Media.Video games'                     1953  -->   1588   365    78  58685
			'Culture.Performing arts'                       1313  -->    777   536   119  59284
			'Culture.Philosophy and religion'               2619  -->   1309  1310   310  57787
			'Culture.Sports'                                5942  -->   5181   761   310  54464
			'Culture.Visual arts.Architecture'              2485  -->   1633   852   287  57944
			'Culture.Visual arts.Comics and Anime'          1428  -->   1051   377   121  59167
			'Culture.Visual arts.Fashion'                   1121  -->    693   428    75  59520
			'Culture.Visual arts.Visual arts*'              5698  -->   3826  1872   574  54444
			'Geography.Geographical'                        3310  -->   2027  1283   301  57105
			'Geography.Regions.Africa.Africa*'              6264  -->   5200  1064   381  54071
			'Geography.Regions.Africa.Central Africa'       1097  -->    804   293    44  59575
			'Geography.Regions.Africa.Eastern Africa'       1047  -->    820   227    28  59641
			'Geography.Regions.Africa.Northern Africa'      1234  -->    875   359    96  59386
			'Geography.Regions.Africa.Southern Africa'      1232  -->    879   353    58  59426
			'Geography.Regions.Africa.Western Africa'       1112  -->    857   255    66  59538
			'Geography.Regions.Americas.Central America'    1267  -->    833   434    74  59375
			'Geography.Regions.Americas.North America'      7444  -->   4744  2700  1187  52085
			'Geography.Regions.Americas.South America'      1512  -->   1054   458   125  59079
			'Geography.Regions.Asia.Asia*'                 11217  -->   9195  2022   881  48618
			'Geography.Regions.Asia.Central Asia'           1056  -->    751   305    56  59604
			'Geography.Regions.Asia.East Asia'              2595  -->   1835   760   267  57854
			'Geography.Regions.Asia.North Asia'             1967  -->   1345   622   199  58550
			'Geography.Regions.Asia.South Asia'             2342  -->   1883   459   143  58231
			'Geography.Regions.Asia.Southeast Asia'         1641  -->   1193   448    90  58985
			'Geography.Regions.Asia.West Asia'              2063  -->   1572   491   143  58510
			'Geography.Regions.Europe.Eastern Europe'       3378  -->   2539   839   296  57042
			'Geography.Regions.Europe.Europe*'             12461  -->   9191  3270  1812  46443
			'Geography.Regions.Europe.Northern Europe'      3966  -->   2506  1460   623  56127
			'Geography.Regions.Europe.Southern Europe'      2435  -->   1648   787   332  57949
			'Geography.Regions.Europe.Western Europe'       2996  -->   1942  1054   470  57250
			'Geography.Regions.Oceania'                     2093  -->   1559   534   147  58476
			'History and Society.Business and economics'    3310  -->   1342  1968   471  56935
			'History and Society.Education'                 2151  -->    829  1322   233  58332
			'History and Society.History'                   3065  -->   1021  2044   405  57246
			'History and Society.Military and warfare'      3127  -->   1902  1225   347  57242
			'History and Society.Politics and government'   2929  -->   1245  1684   383  57404
			'History and Society.Society'                   2850  -->    576  2274   206  57660
			'History and Society.Transportation'            3438  -->   2793   645   254  57024
			'STEM.Biology'                                  2762  -->   2151   611   138  57816
			'STEM.Chemistry'                                1185  -->    687   498   162  59369
			'STEM.Computing'                                1851  -->   1056   795   375  58490
			'STEM.Earth and environment'                    1529  -->    978   551   121  59066
			'STEM.Engineering'                              2202  -->   1501   701   194  58320
			'STEM.Libraries & Information'                  1107  -->    586   521    85  59524
			'STEM.Mathematics'                              1025  -->    570   455    86  59605
			'STEM.Medicine & Health'                        1561  -->    867   694   157  58998
			'STEM.Physics'                                  1138  -->    569   569   142  59436
			'STEM.STEM*'                                   15479  -->  12909  2570  1192  44045
			'STEM.Space'                                    1301  -->   1071   230    73  59342
			'STEM.Technology'                               3361  -->   1785  1576   539  56816
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.271         0.121
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.02          0.003
		Culture.Internet culture                        0.044         0.004
		Culture.Linguistics                             0.02          0.008
		Culture.Literature                              0.082         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.027         0.004
		Culture.Media.Films                             0.036         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.041         0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.043         0.01
		Culture.Sports                                  0.098         0.061
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.055         0.021
		Geography.Regions.Africa.Africa*                0.103         0.009
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0.001
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.123         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.185         0.053
		Geography.Regions.Asia.Central Asia             0.017         0.001
		Geography.Regions.Asia.East Asia                0.043         0.012
		Geography.Regions.Asia.North Asia               0.032         0.006
		Geography.Regions.Asia.South Asia               0.039         0.017
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.034         0.012
		Geography.Regions.Europe.Eastern Europe         0.056         0.018
		Geography.Regions.Europe.Europe*                0.205         0.082
		Geography.Regions.Europe.Northern Europe        0.065         0.029
		Geography.Regions.Europe.Southern Europe        0.04          0.014
		Geography.Regions.Europe.Western Europe         0.049         0.021
		Geography.Regions.Oceania                       0.034         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.035         0.008
		History and Society.History                     0.05          0.011
		History and Society.Military and warfare        0.052         0.015
		History and Society.Politics and government     0.048         0.016
		History and Society.Society                     0.047         0.008
		History and Society.Transportation              0.057         0.016
		STEM.Biology                                    0.045         0.035
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.03          0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.036         0.006
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.026         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.255         0.066
		STEM.Space                                      0.021         0.004
		STEM.Technology                                 0.055         0.005
	match_rate (micro=0.051, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.058
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.016
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.019
		Geography.Regions.Europe.Europe*             0.095
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.011
		History and Society.Military and warfare     0.015
		History and Society.Politics and government  0.014
		History and Society.Society                  0.005
		History and Society.Transportation           0.018
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.079
		STEM.Space                                   0.005
		STEM.Technology                              0.012
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.905
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.986
		History and Society.Society                  0.995
		History and Society.Transportation           0.982
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.921
		STEM.Space                                   0.995
		STEM.Technology                              0.988
		-------------------------------------------  -----
	recall (micro=0.723, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.829
		Culture.Biography.Women                      0.687
		Culture.Food and drink                       0.585
		Culture.Internet culture                     0.705
		Culture.Linguistics                          0.672
		Culture.Literature                           0.68
		Culture.Media.Books                          0.628
		Culture.Media.Entertainment                  0.404
		Culture.Media.Films                          0.748
		Culture.Media.Media*                         0.799
		Culture.Media.Music                          0.717
		Culture.Media.Radio                          0.752
		Culture.Media.Software                       0.489
		Culture.Media.Television                     0.641
		Culture.Media.Video games                    0.813
		Culture.Performing arts                      0.592
		Culture.Philosophy and religion              0.5
		Culture.Sports                               0.872
		Culture.Visual arts.Architecture             0.657
		Culture.Visual arts.Comics and Anime         0.736
		Culture.Visual arts.Fashion                  0.618
		Culture.Visual arts.Visual arts*             0.671
		Geography.Geographical                       0.612
		Geography.Regions.Africa.Africa*             0.83
		Geography.Regions.Africa.Central Africa      0.733
		Geography.Regions.Africa.Eastern Africa      0.783
		Geography.Regions.Africa.Northern Africa     0.709
		Geography.Regions.Africa.Southern Africa     0.713
		Geography.Regions.Africa.Western Africa      0.771
		Geography.Regions.Americas.Central America   0.657
		Geography.Regions.Americas.North America     0.637
		Geography.Regions.Americas.South America     0.697
		Geography.Regions.Asia.Asia*                 0.82
		Geography.Regions.Asia.Central Asia          0.711
		Geography.Regions.Asia.East Asia             0.707
		Geography.Regions.Asia.North Asia            0.684
		Geography.Regions.Asia.South Asia            0.804
		Geography.Regions.Asia.Southeast Asia        0.727
		Geography.Regions.Asia.West Asia             0.762
		Geography.Regions.Europe.Eastern Europe      0.752
		Geography.Regions.Europe.Europe*             0.738
		Geography.Regions.Europe.Northern Europe     0.632
		Geography.Regions.Europe.Southern Europe     0.677
		Geography.Regions.Europe.Western Europe      0.648
		Geography.Regions.Oceania                    0.745
		History and Society.Business and economics   0.405
		History and Society.Education                0.385
		History and Society.History                  0.333
		History and Society.Military and warfare     0.608
		History and Society.Politics and government  0.425
		History and Society.Society                  0.202
		History and Society.Transportation           0.812
		STEM.Biology                                 0.779
		STEM.Chemistry                               0.58
		STEM.Computing                               0.571
		STEM.Earth and environment                   0.64
		STEM.Engineering                             0.682
		STEM.Libraries & Information                 0.529
		STEM.Mathematics                             0.556
		STEM.Medicine & Health                       0.555
		STEM.Physics                                 0.5
		STEM.STEM*                                   0.834
		STEM.Space                                   0.823
		STEM.Technology                              0.531
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.993
		History and Society.Society                  0.996
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.672, macro=0.544):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.78
		Culture.Biography.Women                      0.431
		Culture.Food and drink                       0.505
		Culture.Internet culture                     0.425
		Culture.Linguistics                          0.773
		Culture.Literature                           0.532
		Culture.Media.Books                          0.406
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.722
		Culture.Media.Media*                         0.585
		Culture.Media.Music                          0.755
		Culture.Media.Radio                          0.701
		Culture.Media.Software                       0.104
		Culture.Media.Television                     0.608
		Culture.Media.Video games                    0.643
		Culture.Performing arts                      0.477
		Culture.Philosophy and religion              0.498
		Culture.Sports                               0.909
		Culture.Visual arts.Architecture             0.595
		Culture.Visual arts.Comics and Anime         0.466
		Culture.Visual arts.Fashion                  0.308
		Culture.Visual arts.Visual arts*             0.545
		Geography.Geographical                       0.718
		Geography.Regions.Africa.Africa*             0.506
		Geography.Regions.Africa.Central Africa      0.414
		Geography.Regions.Africa.Eastern Africa      0.459
		Geography.Regions.Africa.Northern Africa     0.375
		Geography.Regions.Africa.Southern Africa     0.492
		Geography.Regions.Africa.Western Africa      0.344
		Geography.Regions.Americas.Central America   0.649
		Geography.Regions.Americas.North America     0.66
		Geography.Regions.Americas.South America     0.697
		Geography.Regions.Asia.Asia*                 0.721
		Geography.Regions.Asia.Central Asia          0.379
		Geography.Regions.Asia.East Asia             0.657
		Geography.Regions.Asia.North Asia            0.535
		Geography.Regions.Asia.South Asia            0.848
		Geography.Regions.Asia.Southeast Asia        0.751
		Geography.Regions.Asia.West Asia             0.789
		Geography.Regions.Europe.Eastern Europe      0.733
		Geography.Regions.Europe.Europe*             0.636
		Geography.Regions.Europe.Northern Europe     0.634
		Geography.Regions.Europe.Southern Europe     0.628
		Geography.Regions.Europe.Western Europe      0.627
		Geography.Regions.Oceania                    0.834
		History and Society.Business and economics   0.329
		History and Society.Education                0.439
		History and Society.History                  0.344
		History and Society.Military and warfare     0.613
		History and Society.Politics and government  0.518
		History and Society.Society                  0.323
		History and Society.Transportation           0.754
		STEM.Biology                                 0.922
		STEM.Chemistry                               0.267
		STEM.Computing                               0.204
		STEM.Earth and environment                   0.6
		STEM.Engineering                             0.545
		STEM.Libraries & Information                 0.204
		STEM.Mathematics                             0.153
		STEM.Medicine & Health                       0.578
		STEM.Physics                                 0.166
		STEM.STEM*                                   0.69
		STEM.Space                                   0.743
		STEM.Technology                              0.228
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.988
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
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
	f1 (micro=0.692, macro=0.581):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.804
		Culture.Biography.Women                      0.53
		Culture.Food and drink                       0.542
		Culture.Internet culture                     0.53
		Culture.Linguistics                          0.719
		Culture.Literature                           0.597
		Culture.Media.Books                          0.493
		Culture.Media.Entertainment                  0.359
		Culture.Media.Films                          0.735
		Culture.Media.Media*                         0.675
		Culture.Media.Music                          0.736
		Culture.Media.Radio                          0.726
		Culture.Media.Software                       0.172
		Culture.Media.Television                     0.624
		Culture.Media.Video games                    0.718
		Culture.Performing arts                      0.528
		Culture.Philosophy and religion              0.499
		Culture.Sports                               0.89
		Culture.Visual arts.Architecture             0.625
		Culture.Visual arts.Comics and Anime         0.571
		Culture.Visual arts.Fashion                  0.411
		Culture.Visual arts.Visual arts*             0.601
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.629
		Geography.Regions.Africa.Central Africa      0.529
		Geography.Regions.Africa.Eastern Africa      0.579
		Geography.Regions.Africa.Northern Africa     0.49
		Geography.Regions.Africa.Southern Africa     0.582
		Geography.Regions.Africa.Western Africa      0.476
		Geography.Regions.Americas.Central America   0.653
		Geography.Regions.Americas.North America     0.649
		Geography.Regions.Americas.South America     0.697
		Geography.Regions.Asia.Asia*                 0.767
		Geography.Regions.Asia.Central Asia          0.494
		Geography.Regions.Asia.East Asia             0.681
		Geography.Regions.Asia.North Asia            0.6
		Geography.Regions.Asia.South Asia            0.825
		Geography.Regions.Asia.Southeast Asia        0.739
		Geography.Regions.Asia.West Asia             0.775
		Geography.Regions.Europe.Eastern Europe      0.742
		Geography.Regions.Europe.Europe*             0.683
		Geography.Regions.Europe.Northern Europe     0.633
		Geography.Regions.Europe.Southern Europe     0.651
		Geography.Regions.Europe.Western Europe      0.637
		Geography.Regions.Oceania                    0.787
		History and Society.Business and economics   0.363
		History and Society.Education                0.41
		History and Society.History                  0.339
		History and Society.Military and warfare     0.611
		History and Society.Politics and government  0.467
		History and Society.Society                  0.249
		History and Society.Transportation           0.782
		STEM.Biology                                 0.844
		STEM.Chemistry                               0.366
		STEM.Computing                               0.3
		STEM.Earth and environment                   0.619
		STEM.Engineering                             0.606
		STEM.Libraries & Information                 0.295
		STEM.Mathematics                             0.239
		STEM.Medicine & Health                       0.566
		STEM.Physics                                 0.249
		STEM.STEM*                                   0.755
		STEM.Space                                   0.781
		STEM.Technology                              0.319
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.951
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.986
		History and Society.Education                0.991
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.984
		History and Society.Society                  0.99
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.964
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.032
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.007
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.007
		History and Society.Society                  0.004
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.965
		Culture.Food and drink                       0.97
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.965
		Culture.Literature                           0.966
		Culture.Media.Books                          0.975
		Culture.Media.Entertainment                  0.954
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.976
		Culture.Media.Software                       0.973
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.944
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.958
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.975
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.979
		Geography.Regions.Africa.Northern Africa     0.969
		Geography.Regions.Africa.Southern Africa     0.97
		Geography.Regions.Africa.Western Africa      0.98
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.952
		Geography.Regions.Americas.South America     0.972
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.978
		Geography.Regions.Asia.East Asia             0.973
		Geography.Regions.Asia.North Asia            0.971
		Geography.Regions.Asia.South Asia            0.979
		Geography.Regions.Asia.Southeast Asia        0.971
		Geography.Regions.Asia.West Asia             0.972
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.958
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.94
		History and Society.Education                0.942
		History and Society.History                  0.92
		History and Society.Military and warfare     0.964
		History and Society.Politics and government  0.936
		History and Society.Society                  0.869
		History and Society.Transportation           0.979
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.974
		STEM.Computing                               0.975
		STEM.Earth and environment                   0.969
		STEM.Engineering                             0.968
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.97
		STEM.Medicine & Health                       0.958
		STEM.Physics                                 0.97
		STEM.STEM*                                   0.968
		STEM.Space                                   0.982
		STEM.Technology                              0.959
		-------------------------------------------  -----
	pr_auc (micro=0.725, macro=0.576):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.488
		Culture.Food and drink                       0.461
		Culture.Internet culture                     0.641
		Culture.Linguistics                          0.7
		Culture.Literature                           0.639
		Culture.Media.Books                          0.455
		Culture.Media.Entertainment                  0.26
		Culture.Media.Films                          0.744
		Culture.Media.Media*                         0.765
		Culture.Media.Music                          0.781
		Culture.Media.Radio                          0.759
		Culture.Media.Software                       0.111
		Culture.Media.Television                     0.612
		Culture.Media.Video games                    0.806
		Culture.Performing arts                      0.479
		Culture.Philosophy and religion              0.424
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.639
		Culture.Visual arts.Comics and Anime         0.625
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.655
		Geography.Geographical                       0.712
		Geography.Regions.Africa.Africa*             0.656
		Geography.Regions.Africa.Central Africa      0.509
		Geography.Regions.Africa.Eastern Africa      0.513
		Geography.Regions.Africa.Northern Africa     0.465
		Geography.Regions.Africa.Southern Africa     0.45
		Geography.Regions.Africa.Western Africa      0.427
		Geography.Regions.Americas.Central America   0.611
		Geography.Regions.Americas.North America     0.714
		Geography.Regions.Americas.South America     0.661
		Geography.Regions.Asia.Asia*                 0.814
		Geography.Regions.Asia.Central Asia          0.522
		Geography.Regions.Asia.East Asia             0.679
		Geography.Regions.Asia.North Asia            0.644
		Geography.Regions.Asia.South Asia            0.855
		Geography.Regions.Asia.Southeast Asia        0.699
		Geography.Regions.Asia.West Asia             0.798
		Geography.Regions.Europe.Eastern Europe      0.783
		Geography.Regions.Europe.Europe*             0.73
		Geography.Regions.Europe.Northern Europe     0.649
		Geography.Regions.Europe.Southern Europe     0.654
		Geography.Regions.Europe.Western Europe      0.628
		Geography.Regions.Oceania                    0.809
		History and Society.Business and economics   0.284
		History and Society.Education                0.356
		History and Society.History                  0.243
		History and Society.Military and warfare     0.634
		History and Society.Politics and government  0.446
		History and Society.Society                  0.207
		History and Society.Transportation           0.788
		STEM.Biology                                 0.888
		STEM.Chemistry                               0.281
		STEM.Computing                               0.23
		STEM.Earth and environment                   0.64
		STEM.Engineering                             0.574
		STEM.Libraries & Information                 0.22
		STEM.Mathematics                             0.179
		STEM.Medicine & Health                       0.509
		STEM.Physics                                 0.183
		STEM.STEM*                                   0.842
		STEM.Space                                   0.837
		STEM.Technology                              0.307
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}, 'type': 'object'}

