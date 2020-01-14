Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'init': None, 'population_rates': None, 'verbose': 0, 'min_samples_split': 2, 'loss': 'deviance', 'max_depth': 5, 'subsample': 1.0, 'n_iter_no_change': None, 'random_state': None, 'min_impurity_split': None, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'validation_fraction': 0.1, 'min_weight_fraction_leaf': 0.0, 'multilabel': True, 'max_leaf_nodes': None, 'tol': 0.0001, 'scale': False, 'warm_start': False, 'max_features': 'log2', 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'presort': 'auto', 'label_weights': {}, 'learning_rate': 0.1, 'criterion': 'friedman_mse', 'n_estimators': 150}
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
	counts (n=60025):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16106  -->  12947  3159  1625  42294
			'Culture.Biography.Women'                       3942  -->   2466  1476   734  55349
			'Culture.Food and drink'                        1219  -->    793   426   102  58704
			'Culture.Internet culture'                      2718  -->   1801   917   213  57094
			'Culture.Linguistics'                           1170  -->    649   521   137  58718
			'Culture.Literature'                            5018  -->   3003  2015   630  54377
			'Culture.Media.Books'                           1774  -->    914   860   237  58014
			'Culture.Media.Entertainment'                   1686  -->    331  1355   110  58229
			'Culture.Media.Films'                           2153  -->   1471   682   213  57659
			'Culture.Media.Media*'                         13394  -->  10272  3122  2024  44607
			'Culture.Media.Music'                           2568  -->   1882   686   290  57167
			'Culture.Media.Radio'                           1112  -->    850   262    52  58861
			'Culture.Media.Software'                        1594  -->    738   856   341  58090
			'Culture.Media.Television'                      2048  -->   1107   941   246  57731
			'Culture.Media.Video games'                     1917  -->   1508   409    90  58018
			'Culture.Performing arts'                       1279  -->    620   659   125  58621
			'Culture.Philosophy and religion'               2590  -->   1141  1449   346  57089
			'Culture.Sports'                                5636  -->   4841   795   402  53987
			'Culture.Visual arts.Architecture'              2496  -->   1545   951   292  57237
			'Culture.Visual arts.Comics and Anime'          1460  -->    777   683   154  58411
			'Culture.Visual arts.Fashion'                   1136  -->    679   457    71  58818
			'Culture.Visual arts.Visual arts*'              5771  -->   3222  2549   538  53716
			'Geography.Geographical'                        3344  -->   1930  1414   288  56393
			'Geography.Regions.Africa.Africa*'              5501  -->   3791  1710   291  54233
			'Geography.Regions.Africa.Central Africa'         28  -->      3    25    49  59948
			'Geography.Regions.Africa.Eastern Africa'       1060  -->    571   489    46  58919
			'Geography.Regions.Africa.Northern Africa'      1246  -->    594   652   122  58657
			'Geography.Regions.Africa.Southern Africa'      1264  -->    726   538    64  58697
			'Geography.Regions.Africa.Western Africa'       1125  -->    780   345    63  58837
			'Geography.Regions.Americas.Central America'    1230  -->    380   850    82  58713
			'Geography.Regions.Americas.North America'      7240  -->   3804  3436   930  51855
			'Geography.Regions.Americas.South America'      1484  -->    734   750   158  58383
			'Geography.Regions.Asia.Asia*'                 10519  -->   7248  3271   947  48559
			'Geography.Regions.Asia.Central Asia'           1113  -->    596   517    59  58853
			'Geography.Regions.Asia.East Asia'              2537  -->   1347  1190   262  57226
			'Geography.Regions.Asia.North Asia'             1361  -->    715   646   190  58474
			'Geography.Regions.Asia.South Asia'             2271  -->   1595   676   128  57626
			'Geography.Regions.Asia.Southeast Asia'         1580  -->    682   898    83  58362
			'Geography.Regions.Asia.West Asia'              2143  -->   1267   876   147  57735
			'Geography.Regions.Europe.Eastern Europe'       3004  -->   1697  1307   341  56680
			'Geography.Regions.Europe.Europe*'             12011  -->   7315  4696  1753  46261
			'Geography.Regions.Europe.Northern Europe'      3941  -->   1604  2337   426  55658
			'Geography.Regions.Europe.Southern Europe'      2319  -->    898  1421   254  57452
			'Geography.Regions.Europe.Western Europe'       3061  -->   1499  1562   395  56569
			'Geography.Regions.Oceania'                     2500  -->   1424  1076    99  57426
			'History and Society.Business and economics'    3247  -->   1135  2112   447  56331
			'History and Society.Education'                 2070  -->    897  1173   256  57699
			'History and Society.History'                   3121  -->    727  2394   339  56565
			'History and Society.Military and warfare'      3890  -->   2370  1520   395  55740
			'History and Society.Politics and government'   4401  -->   1777  2624   422  55202
			'History and Society.Society'                   3783  -->    692  3091   222  56020
			'History and Society.Transportation'            3395  -->   2545   850   256  56374
			'STEM.Biology'                                  2738  -->   1986   752   158  57129
			'STEM.Chemistry'                                1187  -->    678   509   162  58676
			'STEM.Computing'                                1886  -->   1041   845   358  57781
			'STEM.Earth and environment'                    1590  -->    807   783   136  58299
			'STEM.Engineering'                              2156  -->   1232   924   186  57683
			'STEM.Libraries & Information'                  1118  -->    527   591    73  58834
			'STEM.Mathematics'                              1017  -->    497   520   113  58895
			'STEM.Medicine & Health'                        1627  -->    887   740   162  58236
			'STEM.Physics'                                  1129  -->    520   609   162  58734
			'STEM.STEM*'                                   15492  -->  12331  3161  1349  43184
			'STEM.Space'                                    1328  -->   1007   321    68  58629
			'STEM.Technology'                               3331  -->   1528  1803   629  56065
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.268         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.019         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.223         0.058
		Culture.Media.Music                             0.043         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.034         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.043         0.011
		Culture.Sports                                  0.094         0.071
		Culture.Visual arts.Architecture                0.042         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.096         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.019         0.001
		Geography.Regions.Americas.Central America      0.02          0.003
		Geography.Regions.Americas.North America        0.121         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.175         0.046
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.042         0.011
		Geography.Regions.Asia.North Asia               0.023         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.2           0.076
		Geography.Regions.Europe.Northern Europe        0.066         0.031
		Geography.Regions.Europe.Southern Europe        0.039         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.042         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.065         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.031         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.055         0.005
	match_rate (micro=0.05, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.022
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.002
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
		Geography.Regions.Europe.Europe*             0.08
		Geography.Regions.Europe.Northern Europe     0.02
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.016
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.011
		History and Society.Education                0.008
		History and Society.History                  0.008
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.019
		History and Society.Society                  0.006
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.998
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
		Geography.Regions.Europe.Europe*             0.92
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.992
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.981
		History and Society.Society                  0.994
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.64, macro=0.552):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.804
		Culture.Biography.Women                      0.626
		Culture.Food and drink                       0.651
		Culture.Internet culture                     0.663
		Culture.Linguistics                          0.555
		Culture.Literature                           0.598
		Culture.Media.Books                          0.515
		Culture.Media.Entertainment                  0.196
		Culture.Media.Films                          0.683
		Culture.Media.Media*                         0.767
		Culture.Media.Music                          0.733
		Culture.Media.Radio                          0.764
		Culture.Media.Software                       0.463
		Culture.Media.Television                     0.541
		Culture.Media.Video games                    0.787
		Culture.Performing arts                      0.485
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.859
		Culture.Visual arts.Architecture             0.619
		Culture.Visual arts.Comics and Anime         0.532
		Culture.Visual arts.Fashion                  0.598
		Culture.Visual arts.Visual arts*             0.558
		Geography.Geographical                       0.577
		Geography.Regions.Africa.Africa*             0.689
		Geography.Regions.Africa.Central Africa      0.107
		Geography.Regions.Africa.Eastern Africa      0.539
		Geography.Regions.Africa.Northern Africa     0.477
		Geography.Regions.Africa.Southern Africa     0.574
		Geography.Regions.Africa.Western Africa      0.693
		Geography.Regions.Americas.Central America   0.309
		Geography.Regions.Americas.North America     0.525
		Geography.Regions.Americas.South America     0.495
		Geography.Regions.Asia.Asia*                 0.689
		Geography.Regions.Asia.Central Asia          0.535
		Geography.Regions.Asia.East Asia             0.531
		Geography.Regions.Asia.North Asia            0.525
		Geography.Regions.Asia.South Asia            0.702
		Geography.Regions.Asia.Southeast Asia        0.432
		Geography.Regions.Asia.West Asia             0.591
		Geography.Regions.Europe.Eastern Europe      0.565
		Geography.Regions.Europe.Europe*             0.609
		Geography.Regions.Europe.Northern Europe     0.407
		Geography.Regions.Europe.Southern Europe     0.387
		Geography.Regions.Europe.Western Europe      0.49
		Geography.Regions.Oceania                    0.57
		History and Society.Business and economics   0.35
		History and Society.Education                0.433
		History and Society.History                  0.233
		History and Society.Military and warfare     0.609
		History and Society.Politics and government  0.404
		History and Society.Society                  0.183
		History and Society.Transportation           0.75
		STEM.Biology                                 0.725
		STEM.Chemistry                               0.571
		STEM.Computing                               0.552
		STEM.Earth and environment                   0.508
		STEM.Engineering                             0.571
		STEM.Libraries & Information                 0.471
		STEM.Mathematics                             0.489
		STEM.Medicine & Health                       0.545
		STEM.Physics                                 0.461
		STEM.STEM*                                   0.796
		STEM.Space                                   0.758
		STEM.Technology                              0.459
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.996
		History and Society.Transportation           0.995
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.638, macro=0.481):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.753
		Culture.Biography.Women                      0.414
		Culture.Food and drink                       0.481
		Culture.Internet culture                     0.385
		Culture.Linguistics                          0.638
		Culture.Literature                           0.452
		Culture.Media.Books                          0.339
		Culture.Media.Entertainment                  0.272
		Culture.Media.Films                          0.664
		Culture.Media.Media*                         0.523
		Culture.Media.Music                          0.781
		Culture.Media.Radio                          0.652
		Culture.Media.Software                       0.088
		Culture.Media.Television                     0.531
		Culture.Media.Video games                    0.571
		Culture.Performing arts                      0.398
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.899
		Culture.Visual arts.Architecture             0.566
		Culture.Visual arts.Comics and Anime         0.308
		Culture.Visual arts.Fashion                  0.287
		Culture.Visual arts.Visual arts*             0.512
		Geography.Geographical                       0.733
		Geography.Regions.Africa.Africa*             0.504
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.239
		Geography.Regions.Africa.Northern Africa     0.22
		Geography.Regions.Africa.Southern Africa     0.383
		Geography.Regions.Africa.Western Africa      0.307
		Geography.Regions.Americas.Central America   0.423
		Geography.Regions.Americas.North America     0.672
		Geography.Regions.Americas.South America     0.538
		Geography.Regions.Asia.Asia*                 0.632
		Geography.Regions.Asia.Central Asia          0.317
		Geography.Regions.Asia.East Asia             0.574
		Geography.Regions.Asia.North Asia            0.131
		Geography.Regions.Asia.South Asia            0.83
		Geography.Regions.Asia.Southeast Asia        0.648
		Geography.Regions.Asia.West Asia             0.72
		Geography.Regions.Europe.Eastern Europe      0.551
		Geography.Regions.Europe.Europe*             0.579
		Geography.Regions.Europe.Northern Europe     0.628
		Geography.Regions.Europe.Southern Europe     0.536
		Geography.Regions.Europe.Western Europe      0.58
		Geography.Regions.Oceania                    0.836
		History and Society.Business and economics   0.312
		History and Society.Education                0.421
		History and Society.History                  0.302
		History and Society.Military and warfare     0.553
		History and Society.Politics and government  0.607
		History and Society.Society                  0.372
		History and Society.Transportation           0.718
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.245
		STEM.Computing                               0.202
		STEM.Earth and environment                   0.499
		STEM.Engineering                             0.484
		STEM.Libraries & Information                 0.191
		STEM.Mathematics                             0.096
		STEM.Medicine & Health                       0.559
		STEM.Physics                                 0.125
		STEM.STEM*                                   0.661
		STEM.Space                                   0.799
		STEM.Technology                              0.172
		-------------------------------------------  -----
	!precision (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.994
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
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
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
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.992
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
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.631, macro=0.493):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.778
		Culture.Biography.Women                      0.498
		Culture.Food and drink                       0.553
		Culture.Internet culture                     0.487
		Culture.Linguistics                          0.593
		Culture.Literature                           0.515
		Culture.Media.Books                          0.409
		Culture.Media.Entertainment                  0.228
		Culture.Media.Films                          0.673
		Culture.Media.Media*                         0.622
		Culture.Media.Music                          0.756
		Culture.Media.Radio                          0.704
		Culture.Media.Software                       0.147
		Culture.Media.Television                     0.536
		Culture.Media.Video games                    0.662
		Culture.Performing arts                      0.437
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.879
		Culture.Visual arts.Architecture             0.591
		Culture.Visual arts.Comics and Anime         0.39
		Culture.Visual arts.Fashion                  0.387
		Culture.Visual arts.Visual arts*             0.534
		Geography.Geographical                       0.646
		Geography.Regions.Africa.Africa*             0.582
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.331
		Geography.Regions.Africa.Northern Africa     0.301
		Geography.Regions.Africa.Southern Africa     0.46
		Geography.Regions.Africa.Western Africa      0.426
		Geography.Regions.Americas.Central America   0.357
		Geography.Regions.Americas.North America     0.59
		Geography.Regions.Americas.South America     0.515
		Geography.Regions.Asia.Asia*                 0.659
		Geography.Regions.Asia.Central Asia          0.398
		Geography.Regions.Asia.East Asia             0.552
		Geography.Regions.Asia.North Asia            0.209
		Geography.Regions.Asia.South Asia            0.761
		Geography.Regions.Asia.Southeast Asia        0.518
		Geography.Regions.Asia.West Asia             0.649
		Geography.Regions.Europe.Eastern Europe      0.558
		Geography.Regions.Europe.Europe*             0.594
		Geography.Regions.Europe.Northern Europe     0.494
		Geography.Regions.Europe.Southern Europe     0.45
		Geography.Regions.Europe.Western Europe      0.531
		Geography.Regions.Oceania                    0.677
		History and Society.Business and economics   0.33
		History and Society.Education                0.427
		History and Society.History                  0.263
		History and Society.Military and warfare     0.58
		History and Society.Politics and government  0.485
		History and Society.Society                  0.245
		History and Society.Transportation           0.733
		STEM.Biology                                 0.804
		STEM.Chemistry                               0.343
		STEM.Computing                               0.296
		STEM.Earth and environment                   0.503
		STEM.Engineering                             0.524
		STEM.Libraries & Information                 0.272
		STEM.Mathematics                             0.161
		STEM.Medicine & Health                       0.552
		STEM.Physics                                 0.196
		STEM.STEM*                                   0.722
		STEM.Space                                   0.778
		STEM.Technology                              0.251
		-------------------------------------------  -----
	!f1 (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
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
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.97, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.943
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.994
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.946
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.986
		History and Society.Education                0.991
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.976
		History and Society.Society                  0.986
		History and Society.Transportation           0.992
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.958
		STEM.Space                                   0.997
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.037
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.043
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.004
		History and Society.Transportation           0.005
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.956, macro=0.958):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.967
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.961
		Culture.Literature                           0.964
		Culture.Media.Books                          0.973
		Culture.Media.Entertainment                  0.94
		Culture.Media.Films                          0.976
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.978
		Culture.Media.Software                       0.974
		Culture.Media.Television                     0.972
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.94
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.974
		Culture.Visual arts.Comics and Anime         0.976
		Culture.Visual arts.Fashion                  0.976
		Culture.Visual arts.Visual arts*             0.95
		Geography.Geographical                       0.96
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.639
		Geography.Regions.Africa.Eastern Africa      0.971
		Geography.Regions.Africa.Northern Africa     0.969
		Geography.Regions.Africa.Southern Africa     0.971
		Geography.Regions.Africa.Western Africa      0.984
		Geography.Regions.Americas.Central America   0.95
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.965
		Geography.Regions.Asia.Asia*                 0.956
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.965
		Geography.Regions.Asia.North Asia            0.975
		Geography.Regions.Asia.South Asia            0.975
		Geography.Regions.Asia.Southeast Asia        0.961
		Geography.Regions.Asia.West Asia             0.968
		Geography.Regions.Europe.Eastern Europe      0.968
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.941
		Geography.Regions.Europe.Southern Europe     0.952
		Geography.Regions.Europe.Western Europe      0.956
		Geography.Regions.Oceania                    0.967
		History and Society.Business and economics   0.939
		History and Society.Education                0.947
		History and Society.History                  0.91
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.928
		History and Society.Society                  0.863
		History and Society.Transportation           0.981
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.98
		STEM.Computing                               0.978
		STEM.Earth and environment                   0.966
		STEM.Engineering                             0.967
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.973
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.978
		STEM.STEM*                                   0.959
		STEM.Space                                   0.987
		STEM.Technology                              0.951
		-------------------------------------------  -----
	pr_auc (micro=0.662, macro=0.486):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.85
		Culture.Biography.Women                      0.464
		Culture.Food and drink                       0.56
		Culture.Internet culture                     0.6
		Culture.Linguistics                          0.546
		Culture.Literature                           0.527
		Culture.Media.Books                          0.344
		Culture.Media.Entertainment                  0.145
		Culture.Media.Films                          0.679
		Culture.Media.Media*                         0.695
		Culture.Media.Music                          0.779
		Culture.Media.Radio                          0.778
		Culture.Media.Software                       0.09
		Culture.Media.Television                     0.508
		Culture.Media.Video games                    0.766
		Culture.Performing arts                      0.374
		Culture.Philosophy and religion              0.378
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.63
		Culture.Visual arts.Comics and Anime         0.388
		Culture.Visual arts.Fashion                  0.252
		Culture.Visual arts.Visual arts*             0.542
		Geography.Geographical                       0.694
		Geography.Regions.Africa.Africa*             0.563
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.306
		Geography.Regions.Africa.Northern Africa     0.226
		Geography.Regions.Africa.Southern Africa     0.387
		Geography.Regions.Africa.Western Africa      0.407
		Geography.Regions.Americas.Central America   0.264
		Geography.Regions.Americas.North America     0.648
		Geography.Regions.Americas.South America     0.502
		Geography.Regions.Asia.Asia*                 0.7
		Geography.Regions.Asia.Central Asia          0.383
		Geography.Regions.Asia.East Asia             0.507
		Geography.Regions.Asia.North Asia            0.136
		Geography.Regions.Asia.South Asia            0.794
		Geography.Regions.Asia.Southeast Asia        0.518
		Geography.Regions.Asia.West Asia             0.71
		Geography.Regions.Europe.Eastern Europe      0.558
		Geography.Regions.Europe.Europe*             0.62
		Geography.Regions.Europe.Northern Europe     0.521
		Geography.Regions.Europe.Southern Europe     0.432
		Geography.Regions.Europe.Western Europe      0.526
		Geography.Regions.Oceania                    0.733
		History and Society.Business and economics   0.246
		History and Society.Education                0.379
		History and Society.History                  0.193
		History and Society.Military and warfare     0.614
		History and Society.Politics and government  0.517
		History and Society.Society                  0.202
		History and Society.Transportation           0.779
		STEM.Biology                                 0.865
		STEM.Chemistry                               0.289
		STEM.Computing                               0.21
		STEM.Earth and environment                   0.5
		STEM.Engineering                             0.538
		STEM.Libraries & Information                 0.307
		STEM.Mathematics                             0.082
		STEM.Medicine & Health                       0.497
		STEM.Physics                                 0.153
		STEM.STEM*                                   0.803
		STEM.Space                                   0.839
		STEM.Technology                              0.177
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

