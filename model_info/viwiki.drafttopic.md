Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'verbose': 0, 'learning_rate': 0.1, 'n_estimators': 150, 'max_leaf_nodes': None, 'min_impurity_split': None, 'tol': 0.0001, 'population_rates': None, 'min_impurity_decrease': 0.0, 'validation_fraction': 0.1, 'presort': 'auto', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_split': 2, 'warm_start': False, 'random_state': None, 'min_samples_leaf': 1, 'criterion': 'friedman_mse', 'max_depth': 5, 'subsample': 1.0, 'multilabel': True, 'label_weights': {}, 'max_features': 'log2', 'loss': 'deviance', 'n_iter_no_change': None, 'init': None, 'scale': False, 'center': False, 'min_weight_fraction_leaf': 0.0}
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
	counts (n=59891):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14390  -->  12589  1801   789  44712
			'Culture.Biography.Women'                       5026  -->   3895  1131   877  53988
			'Culture.Food and drink'                        1353  -->    845   508   143  58395
			'Culture.Internet culture'                      3548  -->   2729   819   287  56056
			'Culture.Linguistics'                           1476  -->   1075   401    99  58316
			'Culture.Literature'                            5383  -->   3881  1502   516  53992
			'Culture.Media.Books'                           1390  -->    851   539   154  58347
			'Culture.Media.Entertainment'                   1913  -->    753  1160   170  57808
			'Culture.Media.Films'                           2516  -->   1835   681   187  57188
			'Culture.Media.Media*'                         13039  -->  10822  2217  1539  45313
			'Culture.Media.Music'                           2821  -->   2288   533   237  56833
			'Culture.Media.Radio'                            285  -->    181   104    42  59564
			'Culture.Media.Software'                        2235  -->   1619   616   348  57308
			'Culture.Media.Television'                      1980  -->   1234   746   172  57739
			'Culture.Media.Video games'                     2189  -->   1932   257    77  57625
			'Culture.Performing arts'                       1387  -->    880   507   148  58356
			'Culture.Philosophy and religion'               2935  -->   1256  1679   269  56687
			'Culture.Sports'                                4070  -->   3500   570   153  55668
			'Culture.Visual arts.Architecture'              1775  -->   1193   582   189  57927
			'Culture.Visual arts.Comics and Anime'          2196  -->   1780   416   108  57587
			'Culture.Visual arts.Fashion'                   1506  -->   1187   319   121  58264
			'Culture.Visual arts.Visual arts*'              5996  -->   4219  1777   530  53365
			'Geography.Geographical'                        3897  -->   2390  1507   575  55419
			'Geography.Regions.Africa.Africa*'              5689  -->   2539  3150   686  53516
			'Geography.Regions.Africa.Central Africa'       1182  -->    220   962    98  58611
			'Geography.Regions.Africa.Eastern Africa'        435  -->    122   313    58  59398
			'Geography.Regions.Africa.Northern Africa'      1451  -->    601   850    92  58348
			'Geography.Regions.Africa.Southern Africa'      1182  -->    457   725    80  58629
			'Geography.Regions.Africa.Western Africa'        677  -->    303   374    79  59135
			'Geography.Regions.Americas.Central America'    1637  -->    222  1415    51  58203
			'Geography.Regions.Americas.North America'      5296  -->   1757  3539   229  54366
			'Geography.Regions.Americas.South America'      2198  -->    778  1420   157  57536
			'Geography.Regions.Asia.Asia*'                 14522  -->   7842  6680  1804  43565
			'Geography.Regions.Asia.Central Asia'           1050  -->    262   788    96  58745
			'Geography.Regions.Asia.East Asia'              5651  -->   2550  3101   442  53798
			'Geography.Regions.Asia.North Asia'             2554  -->    901  1653   123  57214
			'Geography.Regions.Asia.South Asia'             1936  -->    906  1030    88  57867
			'Geography.Regions.Asia.Southeast Asia'         2573  -->    400  2173   102  57216
			'Geography.Regions.Asia.West Asia'              2087  -->   1008  1079   100  57704
			'Geography.Regions.Europe.Eastern Europe'       4219  -->   1807  2412   167  55505
			'Geography.Regions.Europe.Europe*'             13120  -->   7236  5884  1445  45326
			'Geography.Regions.Europe.Northern Europe'      2791  -->    456  2335   138  56962
			'Geography.Regions.Europe.Southern Europe'      2712  -->   1203  1509    89  57090
			'Geography.Regions.Europe.Western Europe'       3957  -->   1744  2213   109  55825
			'Geography.Regions.Oceania'                     1741  -->    497  1244   157  57993
			'History and Society.Business and economics'    3297  -->   1817  1480   403  56191
			'History and Society.Education'                 1576  -->    799   777   142  58173
			'History and Society.History'                   4186  -->   1832  2354   668  55037
			'History and Society.Military and warfare'      4301  -->   2883  1418   404  55186
			'History and Society.Politics and government'   3138  -->   1313  1825   498  56255
			'History and Society.Society'                   4383  -->   1248  3135   255  55253
			'History and Society.Transportation'            3503  -->   3170   333   109  56279
			'STEM.Biology'                                  6673  -->   6024   649   185  53033
			'STEM.Chemistry'                                1415  -->   1041   374   201  58275
			'STEM.Computing'                                2357  -->   1727   630   356  57178
			'STEM.Earth and environment'                    1674  -->   1035   639   159  58058
			'STEM.Engineering'                              2917  -->   2352   565   105  56869
			'STEM.Libraries & Information'                   476  -->    350   126    36  59379
			'STEM.Mathematics'                               904  -->    674   230    57  58930
			'STEM.Medicine & Health'                        1754  -->   1170   584   142  57995
			'STEM.Physics'                                  1364  -->    895   469   186  58341
			'STEM.STEM*'                                   19854  -->  17790  2064  1139  38898
			'STEM.Space'                                    1554  -->   1360   194    67  58270
			'STEM.Technology'                               4103  -->   2716  1387   645  55143
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.24          0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.09          0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.042         0.012
		Culture.Media.Media*                            0.218         0.055
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
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.095         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.088         0.064
		Geography.Regions.Americas.South America        0.037         0.007
		Geography.Regions.Asia.Asia*                    0.242         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.094         0.012
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
		History and Society.History                     0.07          0.011
		History and Society.Military and warfare        0.072         0.015
		History and Society.Politics and government     0.052         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.111         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.332         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.046, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.027
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.008
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.016
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.025
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.066
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.009
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.073
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.008
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.007
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.017
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.016
		History and Society.Society                  0.007
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.005
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.085
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.954, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.992
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.934
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.927
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.984
		History and Society.Society                  0.993
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.995
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.915
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.642, macro=0.579):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.775
		Culture.Food and drink                       0.625
		Culture.Internet culture                     0.769
		Culture.Linguistics                          0.728
		Culture.Literature                           0.721
		Culture.Media.Books                          0.612
		Culture.Media.Entertainment                  0.394
		Culture.Media.Films                          0.729
		Culture.Media.Media*                         0.83
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.635
		Culture.Media.Software                       0.724
		Culture.Media.Television                     0.623
		Culture.Media.Video games                    0.883
		Culture.Performing arts                      0.634
		Culture.Philosophy and religion              0.428
		Culture.Sports                               0.86
		Culture.Visual arts.Architecture             0.672
		Culture.Visual arts.Comics and Anime         0.811
		Culture.Visual arts.Fashion                  0.788
		Culture.Visual arts.Visual arts*             0.704
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.446
		Geography.Regions.Africa.Central Africa      0.186
		Geography.Regions.Africa.Eastern Africa      0.28
		Geography.Regions.Africa.Northern Africa     0.414
		Geography.Regions.Africa.Southern Africa     0.387
		Geography.Regions.Africa.Western Africa      0.448
		Geography.Regions.Americas.Central America   0.136
		Geography.Regions.Americas.North America     0.332
		Geography.Regions.Americas.South America     0.354
		Geography.Regions.Asia.Asia*                 0.54
		Geography.Regions.Asia.Central Asia          0.25
		Geography.Regions.Asia.East Asia             0.451
		Geography.Regions.Asia.North Asia            0.353
		Geography.Regions.Asia.South Asia            0.468
		Geography.Regions.Asia.Southeast Asia        0.155
		Geography.Regions.Asia.West Asia             0.483
		Geography.Regions.Europe.Eastern Europe      0.428
		Geography.Regions.Europe.Europe*             0.552
		Geography.Regions.Europe.Northern Europe     0.163
		Geography.Regions.Europe.Southern Europe     0.444
		Geography.Regions.Europe.Western Europe      0.441
		Geography.Regions.Oceania                    0.285
		History and Society.Business and economics   0.551
		History and Society.Education                0.507
		History and Society.History                  0.438
		History and Society.Military and warfare     0.67
		History and Society.Politics and government  0.418
		History and Society.Society                  0.285
		History and Society.Transportation           0.905
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.736
		STEM.Computing                               0.733
		STEM.Earth and environment                   0.618
		STEM.Engineering                             0.806
		STEM.Libraries & Information                 0.735
		STEM.Mathematics                             0.746
		STEM.Medicine & Health                       0.667
		STEM.Physics                                 0.656
		STEM.STEM*                                   0.896
		STEM.Space                                   0.875
		STEM.Technology                              0.662
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.996
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.993
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
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.677, macro=0.515):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.427
		Culture.Food and drink                       0.398
		Culture.Internet culture                     0.363
		Culture.Linguistics                          0.778
		Culture.Literature                           0.537
		Culture.Media.Books                          0.505
		Culture.Media.Entertainment                  0.349
		Culture.Media.Films                          0.725
		Culture.Media.Media*                         0.597
		Culture.Media.Music                          0.809
		Culture.Media.Radio                          0.679
		Culture.Media.Software                       0.137
		Culture.Media.Television                     0.655
		Culture.Media.Video games                    0.661
		Culture.Performing arts                      0.437
		Culture.Philosophy and religion              0.489
		Culture.Sports                               0.953
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.512
		Culture.Visual arts.Fashion                  0.256
		Culture.Visual arts.Visual arts*             0.571
		Geography.Geographical                       0.566
		Geography.Regions.Africa.Africa*             0.234
		Geography.Regions.Africa.Central Africa      0.073
		Geography.Regions.Africa.Eastern Africa      0.127
		Geography.Regions.Africa.Northern Africa     0.264
		Geography.Regions.Africa.Southern Africa     0.273
		Geography.Regions.Africa.Western Africa      0.202
		Geography.Regions.Americas.Central America   0.351
		Geography.Regions.Americas.North America     0.843
		Geography.Regions.Americas.South America     0.475
		Geography.Regions.Asia.Asia*                 0.432
		Geography.Regions.Asia.Central Asia          0.11
		Geography.Regions.Asia.East Asia             0.408
		Geography.Regions.Asia.North Asia            0.484
		Geography.Regions.Asia.South Asia            0.839
		Geography.Regions.Asia.Southeast Asia        0.356
		Geography.Regions.Asia.West Asia             0.769
		Geography.Regions.Europe.Eastern Europe      0.729
		Geography.Regions.Europe.Europe*             0.613
		Geography.Regions.Europe.Northern Europe     0.671
		Geography.Regions.Europe.Southern Europe     0.801
		Geography.Regions.Europe.Western Europe      0.827
		Geography.Regions.Oceania                    0.641
		History and Society.Business and economics   0.434
		History and Society.Education                0.627
		History and Society.History                  0.289
		History and Society.Military and warfare     0.591
		History and Society.Politics and government  0.444
		History and Society.Society                  0.343
		History and Society.Transportation           0.887
		STEM.Biology                                 0.904
		STEM.Chemistry                               0.268
		STEM.Computing                               0.253
		STEM.Earth and environment                   0.521
		STEM.Engineering                             0.718
		STEM.Libraries & Information                 0.456
		STEM.Mathematics                             0.265
		STEM.Medicine & Health                       0.641
		STEM.Physics                                 0.163
		STEM.STEM*                                   0.689
		STEM.Space                                   0.767
		STEM.Technology                              0.23
		-------------------------------------------  -----
	!precision (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
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
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.635, macro=0.513):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.55
		Culture.Food and drink                       0.486
		Culture.Internet culture                     0.494
		Culture.Linguistics                          0.753
		Culture.Literature                           0.616
		Culture.Media.Books                          0.553
		Culture.Media.Entertainment                  0.37
		Culture.Media.Films                          0.727
		Culture.Media.Media*                         0.694
		Culture.Media.Music                          0.81
		Culture.Media.Radio                          0.657
		Culture.Media.Software                       0.23
		Culture.Media.Television                     0.639
		Culture.Media.Video games                    0.756
		Culture.Performing arts                      0.517
		Culture.Philosophy and religion              0.457
		Culture.Sports                               0.904
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.627
		Culture.Visual arts.Fashion                  0.387
		Culture.Visual arts.Visual arts*             0.63
		Geography.Geographical                       0.588
		Geography.Regions.Africa.Africa*             0.307
		Geography.Regions.Africa.Central Africa      0.105
		Geography.Regions.Africa.Eastern Africa      0.175
		Geography.Regions.Africa.Northern Africa     0.323
		Geography.Regions.Africa.Southern Africa     0.32
		Geography.Regions.Africa.Western Africa      0.278
		Geography.Regions.Americas.Central America   0.196
		Geography.Regions.Americas.North America     0.476
		Geography.Regions.Americas.South America     0.406
		Geography.Regions.Asia.Asia*                 0.48
		Geography.Regions.Asia.Central Asia          0.152
		Geography.Regions.Asia.East Asia             0.428
		Geography.Regions.Asia.North Asia            0.408
		Geography.Regions.Asia.South Asia            0.601
		Geography.Regions.Asia.Southeast Asia        0.216
		Geography.Regions.Asia.West Asia             0.593
		Geography.Regions.Europe.Eastern Europe      0.54
		Geography.Regions.Europe.Europe*             0.581
		Geography.Regions.Europe.Northern Europe     0.263
		Geography.Regions.Europe.Southern Europe     0.571
		Geography.Regions.Europe.Western Europe      0.575
		Geography.Regions.Oceania                    0.395
		History and Society.Business and economics   0.486
		History and Society.Education                0.561
		History and Society.History                  0.348
		History and Society.Military and warfare     0.628
		History and Society.Politics and government  0.431
		History and Society.Society                  0.311
		History and Society.Transportation           0.896
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.393
		STEM.Computing                               0.376
		STEM.Earth and environment                   0.565
		STEM.Engineering                             0.76
		STEM.Libraries & Information                 0.563
		STEM.Mathematics                             0.391
		STEM.Medicine & Health                       0.654
		STEM.Physics                                 0.262
		STEM.STEM*                                   0.779
		STEM.Space                                   0.817
		STEM.Technology                              0.342
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.978
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
		Culture.Visual arts.Visual arts*             0.992
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
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.982
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.967
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.004
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.04
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.031
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.007
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
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.949, macro=0.954):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.963
		Culture.Literature                           0.973
		Culture.Media.Books                          0.976
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.977
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.948
		Culture.Media.Software                       0.982
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.937
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.985
		Culture.Visual arts.Visual arts*             0.964
		Geography.Geographical                       0.958
		Geography.Regions.Africa.Africa*             0.928
		Geography.Regions.Africa.Central Africa      0.944
		Geography.Regions.Africa.Eastern Africa      0.906
		Geography.Regions.Africa.Northern Africa     0.934
		Geography.Regions.Africa.Southern Africa     0.947
		Geography.Regions.Africa.Western Africa      0.958
		Geography.Regions.Americas.Central America   0.91
		Geography.Regions.Americas.North America     0.904
		Geography.Regions.Americas.South America     0.928
		Geography.Regions.Asia.Asia*                 0.898
		Geography.Regions.Asia.Central Asia          0.94
		Geography.Regions.Asia.East Asia             0.931
		Geography.Regions.Asia.North Asia            0.931
		Geography.Regions.Asia.South Asia            0.915
		Geography.Regions.Asia.Southeast Asia        0.892
		Geography.Regions.Asia.West Asia             0.938
		Geography.Regions.Europe.Eastern Europe      0.927
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.896
		Geography.Regions.Europe.Southern Europe     0.929
		Geography.Regions.Europe.Western Europe      0.927
		Geography.Regions.Oceania                    0.908
		History and Society.Business and economics   0.96
		History and Society.Education                0.965
		History and Society.History                  0.937
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.945
		History and Society.Society                  0.89
		History and Society.Transportation           0.986
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.984
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.97
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.977
		STEM.Space                                   0.988
		STEM.Technology                              0.97
		-------------------------------------------  -----
	pr_auc (micro=0.668, macro=0.494):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.533
		Culture.Food and drink                       0.501
		Culture.Internet culture                     0.602
		Culture.Linguistics                          0.717
		Culture.Literature                           0.657
		Culture.Media.Books                          0.501
		Culture.Media.Entertainment                  0.282
		Culture.Media.Films                          0.772
		Culture.Media.Media*                         0.795
		Culture.Media.Music                          0.866
		Culture.Media.Radio                          0.436
		Culture.Media.Software                       0.165
		Culture.Media.Television                     0.615
		Culture.Media.Video games                    0.796
		Culture.Performing arts                      0.448
		Culture.Philosophy and religion              0.399
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.678
		Culture.Visual arts.Comics and Anime         0.717
		Culture.Visual arts.Fashion                  0.315
		Culture.Visual arts.Visual arts*             0.648
		Geography.Geographical                       0.604
		Geography.Regions.Africa.Africa*             0.285
		Geography.Regions.Africa.Central Africa      0.047
		Geography.Regions.Africa.Eastern Africa      0.047
		Geography.Regions.Africa.Northern Africa     0.142
		Geography.Regions.Africa.Southern Africa     0.166
		Geography.Regions.Africa.Western Africa      0.14
		Geography.Regions.Americas.Central America   0.113
		Geography.Regions.Americas.North America     0.595
		Geography.Regions.Americas.South America     0.336
		Geography.Regions.Asia.Asia*                 0.53
		Geography.Regions.Asia.Central Asia          0.052
		Geography.Regions.Asia.East Asia             0.355
		Geography.Regions.Asia.North Asia            0.355
		Geography.Regions.Asia.South Asia            0.555
		Geography.Regions.Asia.Southeast Asia        0.147
		Geography.Regions.Asia.West Asia             0.553
		Geography.Regions.Europe.Eastern Europe      0.537
		Geography.Regions.Europe.Europe*             0.643
		Geography.Regions.Europe.Northern Europe     0.359
		Geography.Regions.Europe.Southern Europe     0.556
		Geography.Regions.Europe.Western Europe      0.598
		Geography.Regions.Oceania                    0.366
		History and Society.Business and economics   0.469
		History and Society.Education                0.547
		History and Society.History                  0.274
		History and Society.Military and warfare     0.675
		History and Society.Politics and government  0.381
		History and Society.Society                  0.22
		History and Society.Transportation           0.921
		STEM.Biology                                 0.859
		STEM.Chemistry                               0.46
		STEM.Computing                               0.346
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.737
		STEM.Libraries & Information                 0.38
		STEM.Mathematics                             0.393
		STEM.Medicine & Health                       0.651
		STEM.Physics                                 0.197
		STEM.STEM*                                   0.899
		STEM.Space                                   0.89
		STEM.Technology                              0.373
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'properties': {'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}}}

