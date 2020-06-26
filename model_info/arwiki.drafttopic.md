Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'center': False, 'min_impurity_split': None, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'scale': False, 'subsample': 1.0, 'random_state': None, 'max_features': 'log2', 'presort': 'auto', 'population_rates': None, 'max_depth': 5, 'n_iter_no_change': None, 'multilabel': True, 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'learning_rate': 0.1, 'verbose': 0, 'label_weights': {}, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_leaf_nodes': None, 'n_estimators': 150, 'criterion': 'friedman_mse', 'loss': 'deviance', 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'init': None, 'warm_start': False}
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
	counts (n=62859):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 27310  -->  25935  1375  1005  34544
			'Culture.Biography.Women'                       6094  -->   4554  1540   932  55833
			'Culture.Food and drink'                        1371  -->    709   662   127  61361
			'Culture.Internet culture'                      3343  -->   2481   862   219  59297
			'Culture.Linguistics'                           1394  -->    755   639   105  61360
			'Culture.Literature'                            5652  -->   3783  1869   611  56596
			'Culture.Media.Books'                           1547  -->   1053   494   175  61137
			'Culture.Media.Entertainment'                   2102  -->    816  1286   209  60548
			'Culture.Media.Films'                           2057  -->   1525   532   114  60688
			'Culture.Media.Media*'                         13804  -->  10830  2974  1701  47354
			'Culture.Media.Music'                           2671  -->   1816   855   331  59857
			'Culture.Media.Radio'                           1132  -->    424   708   102  61625
			'Culture.Media.Software'                        1936  -->   1237   699   367  60556
			'Culture.Media.Television'                      2331  -->   1218  1113   223  60305
			'Culture.Media.Video games'                     2229  -->   1871   358    77  60553
			'Culture.Performing arts'                       1533  -->    602   931   136  61190
			'Culture.Philosophy and religion'               3343  -->   1334  2009   345  59171
			'Culture.Sports'                                8817  -->   7911   906   450  53592
			'Culture.Visual arts.Architecture'              1803  -->   1035   768   193  60863
			'Culture.Visual arts.Comics and Anime'          1865  -->   1307   558   136  60858
			'Culture.Visual arts.Fashion'                   1337  -->    841   496   103  61419
			'Culture.Visual arts.Visual arts*'              5826  -->   3782  2044   542  56491
			'Geography.Geographical'                        3643  -->   2523  1120   435  58781
			'Geography.Regions.Africa.Africa*'              6429  -->   4685  1744   518  55912
			'Geography.Regions.Africa.Central Africa'       1111  -->    703   408    69  61679
			'Geography.Regions.Africa.Eastern Africa'        947  -->    541   406    68  61844
			'Geography.Regions.Africa.Northern Africa'      2013  -->   1282   731   226  60620
			'Geography.Regions.Africa.Southern Africa'      1170  -->    799   371    73  61616
			'Geography.Regions.Africa.Western Africa'        718  -->    473   245    57  62084
			'Geography.Regions.Americas.Central America'    1375  -->    731   644    94  61390
			'Geography.Regions.Americas.North America'      8631  -->   5398  3233  2219  52009
			'Geography.Regions.Americas.South America'      1645  -->   1108   537   125  61089
			'Geography.Regions.Asia.Asia*'                 12423  -->   9536  2887  1030  49406
			'Geography.Regions.Asia.Central Asia'           1154  -->    709   445    76  61629
			'Geography.Regions.Asia.East Asia'              2771  -->   1865   906   271  59817
			'Geography.Regions.Asia.North Asia'             2404  -->   1514   890   215  60240
			'Geography.Regions.Asia.South Asia'             1876  -->   1305   571    85  60898
			'Geography.Regions.Asia.Southeast Asia'         1553  -->    962   591    75  61231
			'Geography.Regions.Asia.West Asia'              3773  -->   2743  1030   301  58785
			'Geography.Regions.Europe.Eastern Europe'       3496  -->   2269  1227   255  59108
			'Geography.Regions.Europe.Europe*'             13614  -->   9939  3675  2082  47163
			'Geography.Regions.Europe.Northern Europe'      4053  -->   2351  1702   607  58199
			'Geography.Regions.Europe.Southern Europe'      2746  -->   1741  1005   295  59818
			'Geography.Regions.Europe.Western Europe'       3950  -->   2642  1308   545  58364
			'Geography.Regions.Oceania'                     1984  -->   1440   544    95  60780
			'History and Society.Business and economics'    3575  -->   1707  1868   425  58859
			'History and Society.Education'                 2004  -->    684  1320   151  60704
			'History and Society.History'                   4313  -->   1469  2844   619  57927
			'History and Society.Military and warfare'      4075  -->   2369  1706   456  58328
			'History and Society.Politics and government'   4058  -->   1914  2144   621  58180
			'History and Society.Society'                   4346  -->    892  3454   294  58219
			'History and Society.Transportation'            3256  -->   2636   620   185  59418
			'STEM.Biology'                                  2926  -->   2039   887   234  59699
			'STEM.Chemistry'                                1397  -->    853   544   158  61304
			'STEM.Computing'                                2282  -->   1480   802   372  60205
			'STEM.Earth and environment'                    1682  -->    853   829   176  61001
			'STEM.Engineering'                              2830  -->   1855   975   244  59785
			'STEM.Libraries & Information'                  1191  -->    728   463   103  61565
			'STEM.Mathematics'                              1160  -->    683   477    70  61629
			'STEM.Medicine & Health'                        2243  -->   1341   902   281  60335
			'STEM.Physics'                                  1478  -->    861   617   190  61191
			'STEM.STEM*'                                   17637  -->  14815  2822  1396  43826
			'STEM.Space'                                    1703  -->   1425   278    68  61088
			'STEM.Technology'                               4232  -->   2550  1682   672  57955
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.434         0.121
		Culture.Biography.Women                         0.097         0.015
		Culture.Food and drink                          0.022         0.003
		Culture.Internet culture                        0.053         0.004
		Culture.Linguistics                             0.022         0.008
		Culture.Literature                              0.09          0.015
		Culture.Media.Books                             0.025         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.033         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.042         0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.031         0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.053         0.01
		Culture.Sports                                  0.14          0.061
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.03          0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.058         0.021
		Geography.Regions.Africa.Africa*                0.102         0.009
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0.001
		Geography.Regions.Africa.Northern Africa        0.032         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.137         0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.198         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.044         0.012
		Geography.Regions.Asia.North Asia               0.038         0.006
		Geography.Regions.Asia.South Asia               0.03          0.017
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.06          0.012
		Geography.Regions.Europe.Eastern Europe         0.056         0.018
		Geography.Regions.Europe.Europe*                0.217         0.082
		Geography.Regions.Europe.Northern Europe        0.064         0.029
		Geography.Regions.Europe.Southern Europe        0.044         0.014
		Geography.Regions.Europe.Western Europe         0.063         0.021
		Geography.Regions.Oceania                       0.032         0.017
		History and Society.Business and economics      0.057         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.069         0.011
		History and Society.Military and warfare        0.065         0.015
		History and Society.Politics and government     0.065         0.016
		History and Society.Society                     0.069         0.008
		History and Society.Transportation              0.052         0.016
		STEM.Biology                                    0.047         0.035
		STEM.Chemistry                                  0.022         0.002
		STEM.Computing                                  0.036         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.045         0.006
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.281         0.066
		STEM.Space                                      0.027         0.004
		STEM.Technology                                 0.067         0.005
	match_rate (micro=0.055, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.14
		Culture.Biography.Women                      0.027
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.062
		Culture.Visual arts.Architecture             0.009
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.078
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.098
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.005
		History and Society.History                  0.014
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.018
		History and Society.Society                  0.007
		History and Society.Transportation           0.016
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.945, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.86
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.938
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.922
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.902
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.986
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.982
		History and Society.Society                  0.993
		History and Society.Transportation           0.984
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.72, macro=0.628):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.95
		Culture.Biography.Women                      0.747
		Culture.Food and drink                       0.517
		Culture.Internet culture                     0.742
		Culture.Linguistics                          0.542
		Culture.Literature                           0.669
		Culture.Media.Books                          0.681
		Culture.Media.Entertainment                  0.388
		Culture.Media.Films                          0.741
		Culture.Media.Media*                         0.785
		Culture.Media.Music                          0.68
		Culture.Media.Radio                          0.375
		Culture.Media.Software                       0.639
		Culture.Media.Television                     0.523
		Culture.Media.Video games                    0.839
		Culture.Performing arts                      0.393
		Culture.Philosophy and religion              0.399
		Culture.Sports                               0.897
		Culture.Visual arts.Architecture             0.574
		Culture.Visual arts.Comics and Anime         0.701
		Culture.Visual arts.Fashion                  0.629
		Culture.Visual arts.Visual arts*             0.649
		Geography.Geographical                       0.693
		Geography.Regions.Africa.Africa*             0.729
		Geography.Regions.Africa.Central Africa      0.633
		Geography.Regions.Africa.Eastern Africa      0.571
		Geography.Regions.Africa.Northern Africa     0.637
		Geography.Regions.Africa.Southern Africa     0.683
		Geography.Regions.Africa.Western Africa      0.659
		Geography.Regions.Americas.Central America   0.532
		Geography.Regions.Americas.North America     0.625
		Geography.Regions.Americas.South America     0.674
		Geography.Regions.Asia.Asia*                 0.768
		Geography.Regions.Asia.Central Asia          0.614
		Geography.Regions.Asia.East Asia             0.673
		Geography.Regions.Asia.North Asia            0.63
		Geography.Regions.Asia.South Asia            0.696
		Geography.Regions.Asia.Southeast Asia        0.619
		Geography.Regions.Asia.West Asia             0.727
		Geography.Regions.Europe.Eastern Europe      0.649
		Geography.Regions.Europe.Europe*             0.73
		Geography.Regions.Europe.Northern Europe     0.58
		Geography.Regions.Europe.Southern Europe     0.634
		Geography.Regions.Europe.Western Europe      0.669
		Geography.Regions.Oceania                    0.726
		History and Society.Business and economics   0.477
		History and Society.Education                0.341
		History and Society.History                  0.341
		History and Society.Military and warfare     0.581
		History and Society.Politics and government  0.472
		History and Society.Society                  0.205
		History and Society.Transportation           0.81
		STEM.Biology                                 0.697
		STEM.Chemistry                               0.611
		STEM.Computing                               0.649
		STEM.Earth and environment                   0.507
		STEM.Engineering                             0.655
		STEM.Libraries & Information                 0.611
		STEM.Mathematics                             0.589
		STEM.Medicine & Health                       0.598
		STEM.Physics                                 0.583
		STEM.STEM*                                   0.84
		STEM.Space                                   0.837
		STEM.Technology                              0.603
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.959
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.647, macro=0.508):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.823
		Culture.Biography.Women                      0.411
		Culture.Food and drink                       0.393
		Culture.Internet culture                     0.433
		Culture.Linguistics                          0.722
		Culture.Literature                           0.488
		Culture.Media.Books                          0.511
		Culture.Media.Entertainment                  0.311
		Culture.Media.Films                          0.823
		Culture.Media.Media*                         0.57
		Culture.Media.Music                          0.728
		Culture.Media.Radio                          0.348
		Culture.Media.Software                       0.123
		Culture.Media.Television                     0.562
		Culture.Media.Video games                    0.66
		Culture.Performing arts                      0.354
		Culture.Philosophy and religion              0.421
		Culture.Sports                               0.875
		Culture.Visual arts.Architecture             0.667
		Culture.Visual arts.Comics and Anime         0.432
		Culture.Visual arts.Fashion                  0.254
		Culture.Visual arts.Visual arts*             0.559
		Geography.Geographical                       0.673
		Geography.Regions.Africa.Africa*             0.407
		Geography.Regions.Africa.Central Africa      0.287
		Geography.Regions.Africa.Eastern Africa      0.209
		Geography.Regions.Africa.Northern Africa     0.19
		Geography.Regions.Africa.Southern Africa     0.433
		Geography.Regions.Africa.Western Africa      0.351
		Geography.Regions.Americas.Central America   0.549
		Geography.Regions.Americas.North America     0.509
		Geography.Regions.Americas.South America     0.697
		Geography.Regions.Asia.Asia*                 0.678
		Geography.Regions.Asia.Central Asia          0.287
		Geography.Regions.Asia.East Asia             0.65
		Geography.Regions.Asia.North Asia            0.502
		Geography.Regions.Asia.South Asia            0.894
		Geography.Regions.Asia.Southeast Asia        0.762
		Geography.Regions.Asia.West Asia             0.63
		Geography.Regions.Europe.Eastern Europe      0.74
		Geography.Regions.Europe.Europe*             0.605
		Geography.Regions.Europe.Northern Europe     0.629
		Geography.Regions.Europe.Southern Europe     0.646
		Geography.Regions.Europe.Western Europe      0.604
		Geography.Regions.Oceania                    0.887
		History and Society.Business and economics   0.398
		History and Society.Education                0.526
		History and Society.History                  0.264
		History and Society.Military and warfare     0.54
		History and Society.Politics and government  0.428
		History and Society.Society                  0.256
		History and Society.Transportation           0.813
		STEM.Biology                                 0.866
		STEM.Chemistry                               0.289
		STEM.Computing                               0.232
		STEM.Earth and environment                   0.458
		STEM.Engineering                             0.485
		STEM.Libraries & Information                 0.202
		STEM.Mathematics                             0.195
		STEM.Medicine & Health                       0.458
		STEM.Physics                                 0.151
		STEM.STEM*                                   0.657
		STEM.Space                                   0.765
		STEM.Technology                              0.215
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.993
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.996
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.987
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
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
		STEM.STEM*                                   0.989
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.675, macro=0.542):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.882
		Culture.Biography.Women                      0.53
		Culture.Food and drink                       0.446
		Culture.Internet culture                     0.547
		Culture.Linguistics                          0.619
		Culture.Literature                           0.565
		Culture.Media.Books                          0.584
		Culture.Media.Entertainment                  0.345
		Culture.Media.Films                          0.78
		Culture.Media.Media*                         0.66
		Culture.Media.Music                          0.703
		Culture.Media.Radio                          0.361
		Culture.Media.Software                       0.206
		Culture.Media.Television                     0.542
		Culture.Media.Video games                    0.739
		Culture.Performing arts                      0.372
		Culture.Philosophy and religion              0.41
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.617
		Culture.Visual arts.Comics and Anime         0.535
		Culture.Visual arts.Fashion                  0.362
		Culture.Visual arts.Visual arts*             0.601
		Geography.Geographical                       0.682
		Geography.Regions.Africa.Africa*             0.522
		Geography.Regions.Africa.Central Africa      0.395
		Geography.Regions.Africa.Eastern Africa      0.306
		Geography.Regions.Africa.Northern Africa     0.292
		Geography.Regions.Africa.Southern Africa     0.53
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.54
		Geography.Regions.Americas.North America     0.561
		Geography.Regions.Americas.South America     0.685
		Geography.Regions.Asia.Asia*                 0.72
		Geography.Regions.Asia.Central Asia          0.391
		Geography.Regions.Asia.East Asia             0.661
		Geography.Regions.Asia.North Asia            0.559
		Geography.Regions.Asia.South Asia            0.783
		Geography.Regions.Asia.Southeast Asia        0.684
		Geography.Regions.Asia.West Asia             0.675
		Geography.Regions.Europe.Eastern Europe      0.691
		Geography.Regions.Europe.Europe*             0.662
		Geography.Regions.Europe.Northern Europe     0.603
		Geography.Regions.Europe.Southern Europe     0.64
		Geography.Regions.Europe.Western Europe      0.635
		Geography.Regions.Oceania                    0.798
		History and Society.Business and economics   0.434
		History and Society.Education                0.414
		History and Society.History                  0.297
		History and Society.Military and warfare     0.56
		History and Society.Politics and government  0.449
		History and Society.Society                  0.228
		History and Society.Transportation           0.811
		STEM.Biology                                 0.772
		STEM.Chemistry                               0.392
		STEM.Computing                               0.342
		STEM.Earth and environment                   0.481
		STEM.Engineering                             0.557
		STEM.Libraries & Information                 0.304
		STEM.Mathematics                             0.293
		STEM.Medicine & Health                       0.518
		STEM.Physics                                 0.24
		STEM.STEM*                                   0.737
		STEM.Space                                   0.799
		STEM.Technology                              0.317
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.955
		Culture.Media.Music                          0.988
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.981
		History and Society.Society                  0.988
		History and Society.Transportation           0.994
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.028
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.008
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.007
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.041
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.042
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.011
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.011
		History and Society.Society                  0.005
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.962, macro=0.962):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.96
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.955
		Culture.Literature                           0.964
		Culture.Media.Books                          0.97
		Culture.Media.Entertainment                  0.946
		Culture.Media.Films                          0.975
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.971
		Culture.Media.Radio                          0.957
		Culture.Media.Software                       0.976
		Culture.Media.Television                     0.967
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.954
		Culture.Philosophy and religion              0.919
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.965
		Culture.Visual arts.Comics and Anime         0.978
		Culture.Visual arts.Fashion                  0.974
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.966
		Geography.Regions.Africa.Central Africa      0.977
		Geography.Regions.Africa.Eastern Africa      0.962
		Geography.Regions.Africa.Northern Africa     0.97
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.967
		Geography.Regions.Americas.Central America   0.953
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.968
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.965
		Geography.Regions.Asia.East Asia             0.967
		Geography.Regions.Asia.North Asia            0.962
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.96
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.962
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.956
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.965
		Geography.Regions.Oceania                    0.966
		History and Society.Business and economics   0.942
		History and Society.Education                0.932
		History and Society.History                  0.92
		History and Society.Military and warfare     0.954
		History and Society.Politics and government  0.932
		History and Society.Society                  0.864
		History and Society.Transportation           0.979
		STEM.Biology                                 0.967
		STEM.Chemistry                               0.979
		STEM.Computing                               0.979
		STEM.Earth and environment                   0.957
		STEM.Engineering                             0.966
		STEM.Libraries & Information                 0.964
		STEM.Mathematics                             0.971
		STEM.Medicine & Health                       0.965
		STEM.Physics                                 0.977
		STEM.STEM*                                   0.966
		STEM.Space                                   0.985
		STEM.Technology                              0.96
		-------------------------------------------  -----
	pr_auc (micro=0.704, macro=0.523):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.942
		Culture.Biography.Women                      0.492
		Culture.Food and drink                       0.382
		Culture.Internet culture                     0.566
		Culture.Linguistics                          0.591
		Culture.Literature                           0.604
		Culture.Media.Books                          0.555
		Culture.Media.Entertainment                  0.259
		Culture.Media.Films                          0.808
		Culture.Media.Media*                         0.75
		Culture.Media.Music                          0.711
		Culture.Media.Radio                          0.226
		Culture.Media.Software                       0.162
		Culture.Media.Television                     0.537
		Culture.Media.Video games                    0.798
		Culture.Performing arts                      0.304
		Culture.Philosophy and religion              0.33
		Culture.Sports                               0.907
		Culture.Visual arts.Architecture             0.586
		Culture.Visual arts.Comics and Anime         0.471
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.619
		Geography.Geographical                       0.738
		Geography.Regions.Africa.Africa*             0.501
		Geography.Regions.Africa.Central Africa      0.259
		Geography.Regions.Africa.Eastern Africa      0.21
		Geography.Regions.Africa.Northern Africa     0.211
		Geography.Regions.Africa.Southern Africa     0.394
		Geography.Regions.Africa.Western Africa      0.321
		Geography.Regions.Americas.Central America   0.431
		Geography.Regions.Americas.North America     0.582
		Geography.Regions.Americas.South America     0.643
		Geography.Regions.Asia.Asia*                 0.779
		Geography.Regions.Asia.Central Asia          0.297
		Geography.Regions.Asia.East Asia             0.648
		Geography.Regions.Asia.North Asia            0.576
		Geography.Regions.Asia.South Asia            0.817
		Geography.Regions.Asia.Southeast Asia        0.68
		Geography.Regions.Asia.West Asia             0.712
		Geography.Regions.Europe.Eastern Europe      0.709
		Geography.Regions.Europe.Europe*             0.723
		Geography.Regions.Europe.Northern Europe     0.627
		Geography.Regions.Europe.Southern Europe     0.659
		Geography.Regions.Europe.Western Europe      0.632
		Geography.Regions.Oceania                    0.809
		History and Society.Business and economics   0.373
		History and Society.Education                0.349
		History and Society.History                  0.225
		History and Society.Military and warfare     0.596
		History and Society.Politics and government  0.401
		History and Society.Society                  0.159
		History and Society.Transportation           0.85
		STEM.Biology                                 0.808
		STEM.Chemistry                               0.342
		STEM.Computing                               0.301
		STEM.Earth and environment                   0.432
		STEM.Engineering                             0.553
		STEM.Libraries & Information                 0.206
		STEM.Mathematics                             0.233
		STEM.Medicine & Health                       0.544
		STEM.Physics                                 0.175
		STEM.STEM*                                   0.847
		STEM.Space                                   0.835
		STEM.Technology                              0.328
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Media.Films': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}}}}}

