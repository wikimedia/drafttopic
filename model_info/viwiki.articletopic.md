Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 1, 'n_estimators': 150, 'multilabel': True, 'min_impurity_decrease': 0.0, 'max_depth': 5, 'init': None, 'warm_start': False, 'population_rates': None, 'ccp_alpha': 0.0, 'max_features': 'log2', 'validation_fraction': 0.1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'scale': False, 'tol': 0.0001, 'n_iter_no_change': None, 'presort': 'deprecated', 'learning_rate': 0.1, 'subsample': 1.0, 'max_leaf_nodes': None, 'label_weights': {}, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'verbose': 0, 'loss': 'deviance', 'center': False, 'min_samples_split': 2, 'random_state': None}
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
	counts (n=60764):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14139  -->  12639  1500   646  45979
			'Culture.Biography.Women'                       5153  -->   4171   982   792  54819
			'Culture.Food and drink'                        1399  -->    980   419   127  59238
			'Culture.Internet culture'                      3531  -->   2855   676   254  56979
			'Culture.Linguistics'                           1509  -->   1146   363    78  59177
			'Culture.Literature'                            5659  -->   4401  1258   538  54567
			'Culture.Media.Books'                           1467  -->   1045   422   131  59166
			'Culture.Media.Entertainment'                   1984  -->    978  1006   175  58605
			'Culture.Media.Films'                           2612  -->   2031   581   159  57993
			'Culture.Media.Media*'                         13270  -->  11559  1711  1382  46112
			'Culture.Media.Music'                           2908  -->   2506   402   199  57657
			'Culture.Media.Radio'                            285  -->    181   104    37  60442
			'Culture.Media.Software'                        2291  -->   1804   487   319  58154
			'Culture.Media.Television'                      1983  -->   1385   598   150  58631
			'Culture.Media.Video games'                     2139  -->   1959   180    54  58571
			'Culture.Performing arts'                       1374  -->    956   418   119  59271
			'Culture.Philosophy and religion'               3040  -->   1637  1403   303  57421
			'Culture.Sports'                                3871  -->   3414   457   129  56764
			'Culture.Visual arts.Architecture'              1854  -->   1358   496   176  58734
			'Culture.Visual arts.Comics and Anime'          2239  -->   1959   280   114  58411
			'Culture.Visual arts.Fashion'                   1501  -->   1220   281   125  59138
			'Culture.Visual arts.Visual arts*'              6119  -->   4646  1473   486  54159
			'Geography.Geographical'                        3991  -->   2617  1374   563  56210
			'Geography.Regions.Africa.Africa*'              5744  -->   2524  3220   610  54410
			'Geography.Regions.Africa.Central Africa'       1214  -->    357   857   134  59416
			'Geography.Regions.Africa.Eastern Africa'        451  -->    145   306    48  60265
			'Geography.Regions.Africa.Northern Africa'      1474  -->    618   856   114  59176
			'Geography.Regions.Africa.Southern Africa'      1178  -->    455   723   101  59485
			'Geography.Regions.Africa.Western Africa'        672  -->    300   372    98  59994
			'Geography.Regions.Americas.Central America'    1588  -->    255  1333    88  59088
			'Geography.Regions.Americas.North America'      5438  -->   2082  3356   272  55054
			'Geography.Regions.Americas.South America'      2210  -->    811  1399   165  58389
			'Geography.Regions.Asia.Asia*'                 13867  -->   7972  5895  1644  45253
			'Geography.Regions.Asia.Central Asia'           1211  -->    446   765    83  59470
			'Geography.Regions.Asia.East Asia'              5571  -->   2778  2793   410  54783
			'Geography.Regions.Asia.North Asia'             1693  -->    803   890   135  58936
			'Geography.Regions.Asia.South Asia'             2038  -->    897  1141    83  58643
			'Geography.Regions.Asia.Southeast Asia'         2632  -->    502  2130   101  58031
			'Geography.Regions.Asia.West Asia'              2178  -->   1136  1042   130  58456
			'Geography.Regions.Europe.Eastern Europe'       3590  -->   1776  1814   227  56947
			'Geography.Regions.Europe.Europe*'             12682  -->   7222  5460  1364  46718
			'Geography.Regions.Europe.Northern Europe'      2896  -->    545  2351   127  57741
			'Geography.Regions.Europe.Southern Europe'      2854  -->   1245  1609   109  57801
			'Geography.Regions.Europe.Western Europe'       4043  -->   1853  2190    99  56622
			'Geography.Regions.Oceania'                     2238  -->    822  1416   215  58311
			'History and Society.Business and economics'    3404  -->   2157  1247   410  56950
			'History and Society.Education'                 1589  -->    946   643   118  59057
			'History and Society.History'                   4595  -->   2408  2187   694  55475
			'History and Society.Military and warfare'      5048  -->   3658  1390   462  55254
			'History and Society.Politics and government'   4595  -->   1975  2620   582  55587
			'History and Society.Society'                   6148  -->   1852  4296   418  54198
			'History and Society.Transportation'            3573  -->   3281   292   109  57082
			'STEM.Biology'                                  7137  -->   6580   557   180  53447
			'STEM.Chemistry'                                1506  -->   1179   327   191  59067
			'STEM.Computing'                                2452  -->   2021   431   307  58005
			'STEM.Earth and environment'                    1649  -->   1126   523   145  58970
			'STEM.Engineering'                              3027  -->   2485   542   139  57598
			'STEM.Libraries & Information'                   489  -->    369   120    58  60217
			'STEM.Mathematics'                               942  -->    763   179    68  59754
			'STEM.Medicine & Health'                        1774  -->   1247   527   138  58852
			'STEM.Physics'                                  1374  -->   1007   367   184  59206
			'STEM.STEM*'                                   20595  -->  18858  1737   982  39187
			'STEM.Space'                                    1637  -->   1493   144    41  59086
			'STEM.Technology'                               4233  -->   3070  1163   601  55930
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.218         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.05          0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.095         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.228         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
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
		History and Society.History                     0.076         0.011
		History and Society.Military and warfare        0.083         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.117         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.339         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.047, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.022
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.065
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.029
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.008
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.07
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.008
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.009
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.022
		History and Society.Society                  0.011
		History and Society.Transportation           0.016
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.953, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.978
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.93
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.991
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.978
		History and Society.Society                  0.989
		History and Society.Transportation           0.984
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.68, macro=0.624):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.894
		Culture.Biography.Women                      0.809
		Culture.Food and drink                       0.701
		Culture.Internet culture                     0.809
		Culture.Linguistics                          0.759
		Culture.Literature                           0.778
		Culture.Media.Books                          0.712
		Culture.Media.Entertainment                  0.493
		Culture.Media.Films                          0.778
		Culture.Media.Media*                         0.871
		Culture.Media.Music                          0.862
		Culture.Media.Radio                          0.635
		Culture.Media.Software                       0.787
		Culture.Media.Television                     0.698
		Culture.Media.Video games                    0.916
		Culture.Performing arts                      0.696
		Culture.Philosophy and religion              0.538
		Culture.Sports                               0.882
		Culture.Visual arts.Architecture             0.732
		Culture.Visual arts.Comics and Anime         0.875
		Culture.Visual arts.Fashion                  0.813
		Culture.Visual arts.Visual arts*             0.759
		Geography.Geographical                       0.656
		Geography.Regions.Africa.Africa*             0.439
		Geography.Regions.Africa.Central Africa      0.294
		Geography.Regions.Africa.Eastern Africa      0.322
		Geography.Regions.Africa.Northern Africa     0.419
		Geography.Regions.Africa.Southern Africa     0.386
		Geography.Regions.Africa.Western Africa      0.446
		Geography.Regions.Americas.Central America   0.161
		Geography.Regions.Americas.North America     0.383
		Geography.Regions.Americas.South America     0.367
		Geography.Regions.Asia.Asia*                 0.575
		Geography.Regions.Asia.Central Asia          0.368
		Geography.Regions.Asia.East Asia             0.499
		Geography.Regions.Asia.North Asia            0.474
		Geography.Regions.Asia.South Asia            0.44
		Geography.Regions.Asia.Southeast Asia        0.191
		Geography.Regions.Asia.West Asia             0.522
		Geography.Regions.Europe.Eastern Europe      0.495
		Geography.Regions.Europe.Europe*             0.569
		Geography.Regions.Europe.Northern Europe     0.188
		Geography.Regions.Europe.Southern Europe     0.436
		Geography.Regions.Europe.Western Europe      0.458
		Geography.Regions.Oceania                    0.367
		History and Society.Business and economics   0.634
		History and Society.Education                0.595
		History and Society.History                  0.524
		History and Society.Military and warfare     0.725
		History and Society.Politics and government  0.43
		History and Society.Society                  0.301
		History and Society.Transportation           0.918
		STEM.Biology                                 0.922
		STEM.Chemistry                               0.783
		STEM.Computing                               0.824
		STEM.Earth and environment                   0.683
		STEM.Engineering                             0.821
		STEM.Libraries & Information                 0.755
		STEM.Mathematics                             0.81
		STEM.Medicine & Health                       0.703
		STEM.Physics                                 0.733
		STEM.STEM*                                   0.916
		STEM.Space                                   0.912
		STEM.Technology                              0.725
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.971
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
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.995
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.7, macro=0.522):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.901
		Culture.Biography.Women                      0.456
		Culture.Food and drink                       0.447
		Culture.Internet culture                     0.39
		Culture.Linguistics                          0.81
		Culture.Literature                           0.556
		Culture.Media.Books                          0.566
		Culture.Media.Entertainment                  0.373
		Culture.Media.Films                          0.751
		Culture.Media.Media*                         0.65
		Culture.Media.Music                          0.86
		Culture.Media.Radio                          0.691
		Culture.Media.Software                       0.161
		Culture.Media.Television                     0.709
		Culture.Media.Video games                    0.722
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.525
		Culture.Sports                               0.968
		Culture.Visual arts.Architecture             0.724
		Culture.Visual arts.Comics and Anime         0.497
		Culture.Visual arts.Fashion                  0.238
		Culture.Visual arts.Visual arts*             0.614
		Geography.Geographical                       0.615
		Geography.Regions.Africa.Africa*             0.237
		Geography.Regions.Africa.Central Africa      0.076
		Geography.Regions.Africa.Eastern Africa      0.155
		Geography.Regions.Africa.Northern Africa     0.211
		Geography.Regions.Africa.Southern Africa     0.211
		Geography.Regions.Africa.Western Africa      0.158
		Geography.Regions.Americas.Central America   0.263
		Geography.Regions.Americas.North America     0.842
		Geography.Regions.Americas.South America     0.453
		Geography.Regions.Asia.Asia*                 0.439
		Geography.Regions.Asia.Central Asia          0.186
		Geography.Regions.Asia.East Asia             0.437
		Geography.Regions.Asia.North Asia            0.161
		Geography.Regions.Asia.South Asia            0.828
		Geography.Regions.Asia.Southeast Asia        0.399
		Geography.Regions.Asia.West Asia             0.722
		Geography.Regions.Europe.Eastern Europe      0.618
		Geography.Regions.Europe.Europe*             0.623
		Geography.Regions.Europe.Northern Europe     0.73
		Geography.Regions.Europe.Southern Europe     0.754
		Geography.Regions.Europe.Western Europe      0.837
		Geography.Regions.Oceania                    0.605
		History and Society.Business and economics   0.475
		History and Society.Education                0.689
		History and Society.History                  0.317
		History and Society.Military and warfare     0.555
		History and Society.Politics and government  0.546
		History and Society.Society                  0.335
		History and Society.Transportation           0.881
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.275
		STEM.Computing                               0.297
		STEM.Earth and environment                   0.559
		STEM.Engineering                             0.642
		STEM.Libraries & Information                 0.328
		STEM.Mathematics                             0.229
		STEM.Medicine & Health                       0.659
		STEM.Physics                                 0.167
		STEM.STEM*                                   0.736
		STEM.Space                                   0.888
		STEM.Technology                              0.26
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
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
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.959
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.984
		History and Society.Society                  0.991
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.669, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.897
		Culture.Biography.Women                      0.584
		Culture.Food and drink                       0.546
		Culture.Internet culture                     0.526
		Culture.Linguistics                          0.784
		Culture.Literature                           0.649
		Culture.Media.Books                          0.631
		Culture.Media.Entertainment                  0.425
		Culture.Media.Films                          0.764
		Culture.Media.Media*                         0.745
		Culture.Media.Music                          0.861
		Culture.Media.Radio                          0.662
		Culture.Media.Software                       0.267
		Culture.Media.Television                     0.704
		Culture.Media.Video games                    0.808
		Culture.Performing arts                      0.583
		Culture.Philosophy and religion              0.532
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.728
		Culture.Visual arts.Comics and Anime         0.634
		Culture.Visual arts.Fashion                  0.368
		Culture.Visual arts.Visual arts*             0.679
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.308
		Geography.Regions.Africa.Central Africa      0.121
		Geography.Regions.Africa.Eastern Africa      0.209
		Geography.Regions.Africa.Northern Africa     0.281
		Geography.Regions.Africa.Southern Africa     0.273
		Geography.Regions.Africa.Western Africa      0.233
		Geography.Regions.Americas.Central America   0.2
		Geography.Regions.Americas.North America     0.526
		Geography.Regions.Americas.South America     0.405
		Geography.Regions.Asia.Asia*                 0.498
		Geography.Regions.Asia.Central Asia          0.247
		Geography.Regions.Asia.East Asia             0.466
		Geography.Regions.Asia.North Asia            0.24
		Geography.Regions.Asia.South Asia            0.575
		Geography.Regions.Asia.Southeast Asia        0.258
		Geography.Regions.Asia.West Asia             0.605
		Geography.Regions.Europe.Eastern Europe      0.55
		Geography.Regions.Europe.Europe*             0.595
		Geography.Regions.Europe.Northern Europe     0.299
		Geography.Regions.Europe.Southern Europe     0.553
		Geography.Regions.Europe.Western Europe      0.592
		Geography.Regions.Oceania                    0.457
		History and Society.Business and economics   0.543
		History and Society.Education                0.639
		History and Society.History                  0.395
		History and Society.Military and warfare     0.629
		History and Society.Politics and government  0.481
		History and Society.Society                  0.317
		History and Society.Transportation           0.899
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.407
		STEM.Computing                               0.436
		STEM.Earth and environment                   0.615
		STEM.Engineering                             0.721
		STEM.Libraries & Information                 0.457
		STEM.Mathematics                             0.357
		STEM.Medicine & Health                       0.68
		STEM.Physics                                 0.272
		STEM.STEM*                                   0.816
		STEM.Space                                   0.9
		STEM.Technology                              0.383
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
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
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.987
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
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.995
		History and Society.History                  0.983
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.974
		History and Society.Society                  0.984
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.014
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.029
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
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.005
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.035
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.007
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.028
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.008
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.958, macro=0.961):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.975
		Culture.Literature                           0.979
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.969
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.943
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.979
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.973
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.935
		Geography.Regions.Africa.Central Africa      0.956
		Geography.Regions.Africa.Eastern Africa      0.908
		Geography.Regions.Africa.Northern Africa     0.942
		Geography.Regions.Africa.Southern Africa     0.951
		Geography.Regions.Africa.Western Africa      0.965
		Geography.Regions.Americas.Central America   0.916
		Geography.Regions.Americas.North America     0.925
		Geography.Regions.Americas.South America     0.935
		Geography.Regions.Asia.Asia*                 0.914
		Geography.Regions.Asia.Central Asia          0.953
		Geography.Regions.Asia.East Asia             0.945
		Geography.Regions.Asia.North Asia            0.97
		Geography.Regions.Asia.South Asia            0.922
		Geography.Regions.Asia.Southeast Asia        0.906
		Geography.Regions.Asia.West Asia             0.949
		Geography.Regions.Europe.Eastern Europe      0.95
		Geography.Regions.Europe.Europe*             0.924
		Geography.Regions.Europe.Northern Europe     0.913
		Geography.Regions.Europe.Southern Europe     0.935
		Geography.Regions.Europe.Western Europe      0.942
		Geography.Regions.Oceania                    0.93
		History and Society.Business and economics   0.972
		History and Society.Education                0.972
		History and Society.History                  0.951
		History and Society.Military and warfare     0.974
		History and Society.Politics and government  0.926
		History and Society.Society                  0.902
		History and Society.Transportation           0.987
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.987
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.983
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.985
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.981
		STEM.Space                                   0.989
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.711, macro=0.533):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.561
		Culture.Food and drink                       0.602
		Culture.Internet culture                     0.712
		Culture.Linguistics                          0.774
		Culture.Literature                           0.746
		Culture.Media.Books                          0.63
		Culture.Media.Entertainment                  0.394
		Culture.Media.Films                          0.812
		Culture.Media.Media*                         0.846
		Culture.Media.Music                          0.907
		Culture.Media.Radio                          0.482
		Culture.Media.Software                       0.258
		Culture.Media.Television                     0.682
		Culture.Media.Video games                    0.897
		Culture.Performing arts                      0.565
		Culture.Philosophy and religion              0.508
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.73
		Culture.Visual arts.Comics and Anime         0.76
		Culture.Visual arts.Fashion                  0.36
		Culture.Visual arts.Visual arts*             0.715
		Geography.Geographical                       0.657
		Geography.Regions.Africa.Africa*             0.297
		Geography.Regions.Africa.Central Africa      0.044
		Geography.Regions.Africa.Eastern Africa      0.054
		Geography.Regions.Africa.Northern Africa     0.127
		Geography.Regions.Africa.Southern Africa     0.151
		Geography.Regions.Africa.Western Africa      0.106
		Geography.Regions.Americas.Central America   0.105
		Geography.Regions.Americas.North America     0.659
		Geography.Regions.Americas.South America     0.347
		Geography.Regions.Asia.Asia*                 0.546
		Geography.Regions.Asia.Central Asia          0.12
		Geography.Regions.Asia.East Asia             0.42
		Geography.Regions.Asia.North Asia            0.138
		Geography.Regions.Asia.South Asia            0.555
		Geography.Regions.Asia.Southeast Asia        0.196
		Geography.Regions.Asia.West Asia             0.536
		Geography.Regions.Europe.Eastern Europe      0.563
		Geography.Regions.Europe.Europe*             0.671
		Geography.Regions.Europe.Northern Europe     0.418
		Geography.Regions.Europe.Southern Europe     0.549
		Geography.Regions.Europe.Western Europe      0.628
		Geography.Regions.Oceania                    0.425
		History and Society.Business and economics   0.533
		History and Society.Education                0.605
		History and Society.History                  0.356
		History and Society.Military and warfare     0.682
		History and Society.Politics and government  0.47
		History and Society.Society                  0.285
		History and Society.Transportation           0.925
		STEM.Biology                                 0.878
		STEM.Chemistry                               0.471
		STEM.Computing                               0.48
		STEM.Earth and environment                   0.632
		STEM.Engineering                             0.759
		STEM.Libraries & Information                 0.363
		STEM.Mathematics                             0.386
		STEM.Medicine & Health                       0.677
		STEM.Physics                                 0.246
		STEM.STEM*                                   0.926
		STEM.Space                                   0.935
		STEM.Technology                              0.367
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Internet culture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}}}}}

