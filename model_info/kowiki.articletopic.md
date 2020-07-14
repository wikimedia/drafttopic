Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'init': None, 'presort': 'deprecated', 'min_impurity_decrease': 0.0, 'warm_start': False, 'label_weights': {}, 'random_state': None, 'min_samples_split': 2, 'learning_rate': 0.1, 'n_estimators': 150, 'population_rates': None, 'center': False, 'criterion': 'friedman_mse', 'max_depth': 5, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'loss': 'deviance', 'verbose': 0, 'max_features': 'log2', 'scale': False, 'subsample': 1.0, 'n_iter_no_change': None, 'ccp_alpha': 0.0, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'tol': 0.0001, 'min_impurity_split': None, 'multilabel': True}
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
	counts (n=60741):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15801  -->  14235  1566   827  44113
			'Culture.Biography.Women'                       4424  -->   3274  1150   430  55887
			'Culture.Food and drink'                        1776  -->   1367   409    88  58877
			'Culture.Internet culture'                      3463  -->   2729   734   221  57057
			'Culture.Linguistics'                           1688  -->   1152   536   100  58953
			'Culture.Literature'                            5858  -->   4323  1535   505  54378
			'Culture.Media.Books'                           1614  -->   1169   445   121  59006
			'Culture.Media.Entertainment'                   2343  -->   1229  1114   239  58159
			'Culture.Media.Films'                           2950  -->   2446   504   109  57682
			'Culture.Media.Media*'                         15181  -->  13011  2170  1546  44014
			'Culture.Media.Music'                           3247  -->   2609   638   275  57219
			'Culture.Media.Radio'                            702  -->    429   273    66  59973
			'Culture.Media.Software'                        2364  -->   1802   562   377  58000
			'Culture.Media.Television'                      2480  -->   1803   677   162  58099
			'Culture.Media.Video games'                     2305  -->   2021   284    85  58351
			'Culture.Performing arts'                       1527  -->    871   656   142  59072
			'Culture.Philosophy and religion'               3856  -->   2050  1806   334  56551
			'Culture.Sports'                                5207  -->   4500   707   171  55363
			'Culture.Visual arts.Architecture'              2141  -->   1419   722   218  58382
			'Culture.Visual arts.Comics and Anime'          2404  -->   2041   363   153  58184
			'Culture.Visual arts.Fashion'                   1355  -->    948   407    76  59310
			'Culture.Visual arts.Visual arts*'              6401  -->   4521  1880   538  53802
			'Geography.Geographical'                        3907  -->   2541  1366   538  56296
			'Geography.Regions.Africa.Africa*'              4310  -->   3234  1076   243  56188
			'Geography.Regions.Africa.Central Africa'        847  -->    614   233    42  59852
			'Geography.Regions.Africa.Eastern Africa'        475  -->    336   139    77  60189
			'Geography.Regions.Africa.Northern Africa'      1517  -->   1089   428   111  59113
			'Geography.Regions.Africa.Southern Africa'       690  -->    496   194    58  59993
			'Geography.Regions.Africa.Western Africa'        280  -->    195    85    34  60427
			'Geography.Regions.Americas.Central America'    1359  -->    860   499    68  59314
			'Geography.Regions.Americas.North America'      6585  -->   4572  2013  1182  52974
			'Geography.Regions.Americas.South America'      1532  -->   1117   415    90  59119
			'Geography.Regions.Asia.Asia*'                 15107  -->  12516  2591  1540  44094
			'Geography.Regions.Asia.Central Asia'           1328  -->    938   390    86  59327
			'Geography.Regions.Asia.East Asia'              7562  -->   6091  1471   823  52356
			'Geography.Regions.Asia.North Asia'             1823  -->   1372   451   197  58721
			'Geography.Regions.Asia.South Asia'             1867  -->   1404   463    83  58791
			'Geography.Regions.Asia.Southeast Asia'         1913  -->   1355   558    91  58737
			'Geography.Regions.Asia.West Asia'              2393  -->   1749   644   182  58166
			'Geography.Regions.Europe.Eastern Europe'       3409  -->   2597   812   316  57016
			'Geography.Regions.Europe.Europe*'             13405  -->  10882  2523  1627  45709
			'Geography.Regions.Europe.Northern Europe'      3936  -->   2782  1154   405  56400
			'Geography.Regions.Europe.Southern Europe'      3303  -->   2386   917   284  57154
			'Geography.Regions.Europe.Western Europe'       4084  -->   3070  1014   427  56230
			'Geography.Regions.Oceania'                     1829  -->   1341   488    62  58850
			'History and Society.Business and economics'    3915  -->   2140  1775   403  56423
			'History and Society.Education'                 1907  -->   1131   776   127  58707
			'History and Society.History'                   5526  -->   3175  2351   660  54555
			'History and Society.Military and warfare'      5276  -->   3611  1665   477  54988
			'History and Society.Politics and government'   5159  -->   2870  2289   534  55048
			'History and Society.Society'                   6675  -->   3126  3549   588  53478
			'History and Society.Transportation'            3768  -->   3259   509   167  56806
			'STEM.Biology'                                  3464  -->   2662   802   192  57085
			'STEM.Chemistry'                                1495  -->   1150   345   135  59111
			'STEM.Computing'                                2753  -->   2123   630   459  57529
			'STEM.Earth and environment'                    1903  -->   1247   656   136  58702
			'STEM.Engineering'                              2710  -->   1879   831   184  57847
			'STEM.Libraries & Information'                   753  -->    508   245    39  59949
			'STEM.Mathematics'                              1179  -->    875   304    97  59465
			'STEM.Medicine & Health'                        1993  -->   1265   728   173  58575
			'STEM.Physics'                                  1467  -->    937   530   183  59091
			'STEM.STEM*'                                   17902  -->  15664  2238  1087  41752
			'STEM.Space'                                    1703  -->   1499   204    44  58994
			'STEM.Technology'                               4764  -->   3350  1414   669  55308
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.26          0.123
		Culture.Biography.Women                         0.073         0.015
		Culture.Food and drink                          0.029         0.002
		Culture.Internet culture                        0.057         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.25          0.058
		Culture.Media.Music                             0.053         0.024
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.063         0.011
		Culture.Sports                                  0.086         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.064         0.024
		Geography.Regions.Africa.Africa*                0.071         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.108         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.249         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.124         0.011
		Geography.Regions.Asia.North Asia               0.03          0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.039         0.011
		Geography.Regions.Europe.Eastern Europe         0.056         0.013
		Geography.Regions.Europe.Europe*                0.221         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.054         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.091         0.011
		History and Society.Military and warfare        0.087         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.11          0.013
		History and Society.Transportation              0.062         0.015
		STEM.Biology                                    0.057         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.295         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.082
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.002
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.065
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.07
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.024
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.025
		History and Society.Society                  0.017
		History and Society.Transportation           0.016
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.918
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.935
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.93
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.975
		History and Society.Society                  0.983
		History and Society.Transportation           0.984
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.774, macro=0.72):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.901
		Culture.Biography.Women                      0.74
		Culture.Food and drink                       0.77
		Culture.Internet culture                     0.788
		Culture.Linguistics                          0.682
		Culture.Literature                           0.738
		Culture.Media.Books                          0.724
		Culture.Media.Entertainment                  0.525
		Culture.Media.Films                          0.829
		Culture.Media.Media*                         0.857
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.611
		Culture.Media.Software                       0.762
		Culture.Media.Television                     0.727
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.57
		Culture.Philosophy and religion              0.532
		Culture.Sports                               0.864
		Culture.Visual arts.Architecture             0.663
		Culture.Visual arts.Comics and Anime         0.849
		Culture.Visual arts.Fashion                  0.7
		Culture.Visual arts.Visual arts*             0.706
		Geography.Geographical                       0.65
		Geography.Regions.Africa.Africa*             0.75
		Geography.Regions.Africa.Central Africa      0.725
		Geography.Regions.Africa.Eastern Africa      0.707
		Geography.Regions.Africa.Northern Africa     0.718
		Geography.Regions.Africa.Southern Africa     0.719
		Geography.Regions.Africa.Western Africa      0.696
		Geography.Regions.Americas.Central America   0.633
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.729
		Geography.Regions.Asia.Asia*                 0.828
		Geography.Regions.Asia.Central Asia          0.706
		Geography.Regions.Asia.East Asia             0.805
		Geography.Regions.Asia.North Asia            0.753
		Geography.Regions.Asia.South Asia            0.752
		Geography.Regions.Asia.Southeast Asia        0.708
		Geography.Regions.Asia.West Asia             0.731
		Geography.Regions.Europe.Eastern Europe      0.762
		Geography.Regions.Europe.Europe*             0.812
		Geography.Regions.Europe.Northern Europe     0.707
		Geography.Regions.Europe.Southern Europe     0.722
		Geography.Regions.Europe.Western Europe      0.752
		Geography.Regions.Oceania                    0.733
		History and Society.Business and economics   0.547
		History and Society.Education                0.593
		History and Society.History                  0.575
		History and Society.Military and warfare     0.684
		History and Society.Politics and government  0.556
		History and Society.Society                  0.468
		History and Society.Transportation           0.865
		STEM.Biology                                 0.768
		STEM.Chemistry                               0.769
		STEM.Computing                               0.771
		STEM.Earth and environment                   0.655
		STEM.Engineering                             0.693
		STEM.Libraries & Information                 0.675
		STEM.Mathematics                             0.742
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.639
		STEM.STEM*                                   0.875
		STEM.Space                                   0.88
		STEM.Technology                              0.703
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.99
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.698, macro=0.551):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.589
		Culture.Food and drink                       0.56
		Culture.Internet culture                     0.418
		Culture.Linguistics                          0.748
		Culture.Literature                           0.558
		Culture.Media.Books                          0.589
		Culture.Media.Entertainment                  0.315
		Culture.Media.Films                          0.824
		Culture.Media.Media*                         0.611
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.546
		Culture.Media.Software                       0.136
		Culture.Media.Television                     0.699
		Culture.Media.Video games                    0.612
		Culture.Performing arts                      0.408
		Culture.Philosophy and religion              0.494
		Culture.Sports                               0.956
		Culture.Visual arts.Architecture             0.655
		Culture.Visual arts.Comics and Anime         0.416
		Culture.Visual arts.Fashion                  0.307
		Culture.Visual arts.Visual arts*             0.571
		Geography.Geographical                       0.624
		Geography.Regions.Africa.Africa*             0.578
		Geography.Regions.Africa.Central Africa      0.395
		Geography.Regions.Africa.Eastern Africa      0.201
		Geography.Regions.Africa.Northern Africa     0.32
		Geography.Regions.Africa.Southern Africa     0.467
		Geography.Regions.Africa.Western Africa      0.459
		Geography.Regions.Americas.Central America   0.647
		Geography.Regions.Americas.North America     0.686
		Geography.Regions.Americas.South America     0.753
		Geography.Regions.Asia.Asia*                 0.539
		Geography.Regions.Asia.Central Asia          0.297
		Geography.Regions.Asia.East Asia             0.375
		Geography.Regions.Asia.North Asia            0.172
		Geography.Regions.Asia.South Asia            0.892
		Geography.Regions.Asia.Southeast Asia        0.735
		Geography.Regions.Asia.West Asia             0.721
		Geography.Regions.Europe.Eastern Europe      0.642
		Geography.Regions.Europe.Europe*             0.661
		Geography.Regions.Europe.Northern Europe     0.758
		Geography.Regions.Europe.Southern Europe     0.659
		Geography.Regions.Europe.Western Europe      0.661
		Geography.Regions.Oceania                    0.914
		History and Society.Business and economics   0.44
		History and Society.Education                0.671
		History and Society.History                  0.345
		History and Society.Military and warfare     0.532
		History and Society.Politics and government  0.627
		History and Society.Society                  0.355
		History and Society.Transportation           0.819
		STEM.Biology                                 0.889
		STEM.Chemistry                               0.345
		STEM.Computing                               0.208
		STEM.Earth and environment                   0.564
		STEM.Engineering                             0.535
		STEM.Libraries & Information                 0.392
		STEM.Mathematics                             0.16
		STEM.Medicine & Health                       0.581
		STEM.Physics                                 0.15
		STEM.STEM*                                   0.719
		STEM.Space                                   0.877
		STEM.Technology                              0.233
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.726, macro=0.603):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.656
		Culture.Food and drink                       0.648
		Culture.Internet culture                     0.546
		Culture.Linguistics                          0.714
		Culture.Literature                           0.635
		Culture.Media.Books                          0.649
		Culture.Media.Entertainment                  0.394
		Culture.Media.Films                          0.826
		Culture.Media.Media*                         0.713
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.576
		Culture.Media.Software                       0.23
		Culture.Media.Television                     0.713
		Culture.Media.Video games                    0.721
		Culture.Performing arts                      0.476
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.659
		Culture.Visual arts.Comics and Anime         0.558
		Culture.Visual arts.Fashion                  0.426
		Culture.Visual arts.Visual arts*             0.631
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.653
		Geography.Regions.Africa.Central Africa      0.511
		Geography.Regions.Africa.Eastern Africa      0.313
		Geography.Regions.Africa.Northern Africa     0.443
		Geography.Regions.Africa.Southern Africa     0.566
		Geography.Regions.Africa.Western Africa      0.553
		Geography.Regions.Americas.Central America   0.64
		Geography.Regions.Americas.North America     0.69
		Geography.Regions.Americas.South America     0.741
		Geography.Regions.Asia.Asia*                 0.653
		Geography.Regions.Asia.Central Asia          0.418
		Geography.Regions.Asia.East Asia             0.512
		Geography.Regions.Asia.North Asia            0.28
		Geography.Regions.Asia.South Asia            0.816
		Geography.Regions.Asia.Southeast Asia        0.721
		Geography.Regions.Asia.West Asia             0.726
		Geography.Regions.Europe.Eastern Europe      0.697
		Geography.Regions.Europe.Europe*             0.728
		Geography.Regions.Europe.Northern Europe     0.731
		Geography.Regions.Europe.Southern Europe     0.689
		Geography.Regions.Europe.Western Europe      0.703
		Geography.Regions.Oceania                    0.814
		History and Society.Business and economics   0.487
		History and Society.Education                0.629
		History and Society.History                  0.431
		History and Society.Military and warfare     0.598
		History and Society.Politics and government  0.589
		History and Society.Society                  0.404
		History and Society.Transportation           0.841
		STEM.Biology                                 0.824
		STEM.Chemistry                               0.476
		STEM.Computing                               0.328
		STEM.Earth and environment                   0.606
		STEM.Engineering                             0.604
		STEM.Libraries & Information                 0.496
		STEM.Mathematics                             0.263
		STEM.Medicine & Health                       0.607
		STEM.Physics                                 0.242
		STEM.STEM*                                   0.789
		STEM.Space                                   0.879
		STEM.Technology                              0.35
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.995
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
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.978
		History and Society.Society                  0.983
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.034
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.015
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.01
		History and Society.Society                  0.011
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.976
		Culture.Literature                           0.975
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.964
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.966
		Culture.Philosophy and religion              0.946
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.976
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.979
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.975
		Geography.Regions.Africa.Central Africa      0.982
		Geography.Regions.Africa.Eastern Africa      0.97
		Geography.Regions.Africa.Northern Africa     0.978
		Geography.Regions.Africa.Southern Africa     0.963
		Geography.Regions.Africa.Western Africa      0.951
		Geography.Regions.Americas.Central America   0.973
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.978
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.98
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.978
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.96
		History and Society.Education                0.972
		History and Society.History                  0.953
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.95
		History and Society.Society                  0.926
		History and Society.Transportation           0.984
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.972
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.98
		STEM.STEM*                                   0.974
		STEM.Space                                   0.988
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.775, macro=0.614):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.949
		Culture.Biography.Women                      0.646
		Culture.Food and drink                       0.668
		Culture.Internet culture                     0.629
		Culture.Linguistics                          0.734
		Culture.Literature                           0.708
		Culture.Media.Books                          0.701
		Culture.Media.Entertainment                  0.37
		Culture.Media.Films                          0.804
		Culture.Media.Media*                         0.832
		Culture.Media.Music                          0.825
		Culture.Media.Radio                          0.424
		Culture.Media.Software                       0.295
		Culture.Media.Television                     0.716
		Culture.Media.Video games                    0.817
		Culture.Performing arts                      0.4
		Culture.Philosophy and religion              0.481
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.608
		Culture.Visual arts.Fashion                  0.372
		Culture.Visual arts.Visual arts*             0.692
		Geography.Geographical                       0.662
		Geography.Regions.Africa.Africa*             0.662
		Geography.Regions.Africa.Central Africa      0.425
		Geography.Regions.Africa.Eastern Africa      0.22
		Geography.Regions.Africa.Northern Africa     0.327
		Geography.Regions.Africa.Southern Africa     0.472
		Geography.Regions.Africa.Western Africa      0.378
		Geography.Regions.Americas.Central America   0.622
		Geography.Regions.Americas.North America     0.733
		Geography.Regions.Americas.South America     0.759
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.336
		Geography.Regions.Asia.East Asia             0.568
		Geography.Regions.Asia.North Asia            0.336
		Geography.Regions.Asia.South Asia            0.867
		Geography.Regions.Asia.Southeast Asia        0.742
		Geography.Regions.Asia.West Asia             0.726
		Geography.Regions.Europe.Eastern Europe      0.738
		Geography.Regions.Europe.Europe*             0.799
		Geography.Regions.Europe.Northern Europe     0.787
		Geography.Regions.Europe.Southern Europe     0.724
		Geography.Regions.Europe.Western Europe      0.737
		Geography.Regions.Oceania                    0.864
		History and Society.Business and economics   0.446
		History and Society.Education                0.635
		History and Society.History                  0.438
		History and Society.Military and warfare     0.665
		History and Society.Politics and government  0.617
		History and Society.Society                  0.372
		History and Society.Transportation           0.876
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.567
		STEM.Computing                               0.349
		STEM.Earth and environment                   0.591
		STEM.Engineering                             0.626
		STEM.Libraries & Information                 0.437
		STEM.Mathematics                             0.301
		STEM.Medicine & Health                       0.569
		STEM.Physics                                 0.222
		STEM.STEM*                                   0.88
		STEM.Space                                   0.906
		STEM.Technology                              0.398
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}}}}}

