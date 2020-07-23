Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'presort': 'auto', 'max_features': 'log2', 'n_estimators': 150, 'tol': 0.0001, 'n_iter_no_change': None, 'learning_rate': 0.1, 'warm_start': False, 'scale': False, 'validation_fraction': 0.1, 'subsample': 1.0, 'max_leaf_nodes': None, 'label_weights': {}, 'population_rates': None, 'verbose': 0, 'multilabel': True, 'min_samples_split': 2, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_impurity_decrease': 0.0, 'random_state': None, 'init': None, 'min_weight_fraction_leaf': 0.0, 'loss': 'deviance', 'center': False, 'min_impurity_split': None, 'max_depth': 5}
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
	counts (n=60612):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14250  -->   7932  6318  2334  44028
			'Culture.Biography.Women'                       5092  -->   1287  3805   505  55015
			'Culture.Food and drink'                        1369  -->    169  1200    76  59167
			'Culture.Internet culture'                      3542  -->   2511  1031   291  56779
			'Culture.Linguistics'                           1471  -->    544   927    84  59057
			'Culture.Literature'                            5664  -->   2303  3361   460  54488
			'Culture.Media.Books'                           1441  -->    325  1116    70  59101
			'Culture.Media.Entertainment'                   1937  -->    590  1347   114  58561
			'Culture.Media.Films'                           2635  -->   1504  1131   222  57755
			'Culture.Media.Media*'                         13244  -->   9055  4189  1656  45712
			'Culture.Media.Music'                           2833  -->   1777  1056   288  57491
			'Culture.Media.Radio'                            273  -->    151   122    34  60305
			'Culture.Media.Software'                        2262  -->   1563   699   299  58051
			'Culture.Media.Television'                      1968  -->    816  1152   109  58535
			'Culture.Media.Video games'                     2185  -->   1874   311   101  58326
			'Culture.Performing arts'                       1353  -->    464   889    77  59182
			'Culture.Philosophy and religion'               3018  -->    325  2693   136  57458
			'Culture.Sports'                                4019  -->   2592  1427   172  56421
			'Culture.Visual arts.Architecture'              1858  -->    405  1453   142  58612
			'Culture.Visual arts.Comics and Anime'          2262  -->   1808   454   116  58234
			'Culture.Visual arts.Fashion'                   1557  -->    431  1126    74  58981
			'Culture.Visual arts.Visual arts*'              6167  -->   2345  3822   336  54109
			'Geography.Geographical'                        3907  -->   1179  2728   348  56357
			'Geography.Regions.Africa.Africa*'              5703  -->   1964  3739   594  54315
			'Geography.Regions.Africa.Central Africa'       1223  -->    230   993    86  59303
			'Geography.Regions.Africa.Eastern Africa'        433  -->    203   230    71  60108
			'Geography.Regions.Africa.Northern Africa'      1467  -->    557   910   273  58872
			'Geography.Regions.Africa.Southern Africa'      1153  -->    373   780    91  59368
			'Geography.Regions.Africa.Western Africa'        667  -->    214   453    51  59894
			'Geography.Regions.Americas.Central America'    1563  -->    174  1389    59  58990
			'Geography.Regions.Americas.North America'      5144  -->   2151  2993   549  54919
			'Geography.Regions.Americas.South America'      2145  -->    695  1450   159  58308
			'Geography.Regions.Asia.Asia*'                 13777  -->   7412  6365  1649  45186
			'Geography.Regions.Asia.Central Asia'           1124  -->    228   896    59  59429
			'Geography.Regions.Asia.East Asia'              5560  -->   2426  3134   605  54447
			'Geography.Regions.Asia.North Asia'             1624  -->    552  1072   126  58862
			'Geography.Regions.Asia.South Asia'             1941  -->   1078   863    84  58587
			'Geography.Regions.Asia.Southeast Asia'         2658  -->    617  2041   161  57793
			'Geography.Regions.Asia.West Asia'              2117  -->   1350   767   122  58373
			'Geography.Regions.Europe.Eastern Europe'       3564  -->   1594  1970   213  56835
			'Geography.Regions.Europe.Europe*'             12618  -->   6853  5765  1483  46511
			'Geography.Regions.Europe.Northern Europe'      2838  -->    850  1988   224  57550
			'Geography.Regions.Europe.Southern Europe'      2803  -->   1348  1455   190  57619
			'Geography.Regions.Europe.Western Europe'       3921  -->   2200  1721   336  56355
			'Geography.Regions.Oceania'                     2271  -->   1050  1221   233  58108
			'History and Society.Business and economics'    3233  -->    488  2745   131  57248
			'History and Society.Education'                 1598  -->    203  1395    51  58963
			'History and Society.History'                   4233  -->    892  3341   302  56077
			'History and Society.Military and warfare'      4884  -->   2201  2683   365  55363
			'History and Society.Politics and government'   4441  -->    914  3527   201  55970
			'History and Society.Society'                   5941  -->    833  5108   132  54539
			'History and Society.Transportation'            3571  -->   2659   912   144  56897
			'STEM.Biology'                                  7144  -->   5890  1254   156  53312
			'STEM.Chemistry'                                1453  -->    643   810   185  58974
			'STEM.Computing'                                2407  -->   1336  1071   299  57906
			'STEM.Earth and environment'                    1617  -->    252  1365    66  58929
			'STEM.Engineering'                              2985  -->   1943  1042   114  57513
			'STEM.Libraries & Information'                   489  -->    222   267    68  60055
			'STEM.Mathematics'                               918  -->    309   609    76  59618
			'STEM.Medicine & Health'                        1754  -->    604  1150   167  58691
			'STEM.Physics'                                  1392  -->    314  1078   109  59111
			'STEM.STEM*'                                   20503  -->  15360  5143  1678  38431
			'STEM.Space'                                    1584  -->    870   714   125  58903
			'STEM.Technology'                               4268  -->   1890  2378   477  55867
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.235         0.122
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.219         0.055
		Culture.Media.Music                             0.047         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.05          0.01
		Culture.Sports                                  0.066         0.061
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.026         0.001
		Culture.Visual arts.Visual arts*                0.102         0.018
		Geography.Geographical                          0.064         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.085         0.064
		Geography.Regions.Americas.South America        0.035         0.007
		Geography.Regions.Asia.Asia*                    0.227         0.049
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.092         0.012
		Geography.Regions.Asia.North Asia               0.027         0.001
		Geography.Regions.Asia.South Asia               0.032         0.017
		Geography.Regions.Asia.Southeast Asia           0.044         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.014
		Geography.Regions.Europe.Europe*                0.208         0.077
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.046         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.037         0.017
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.026         0.008
		History and Society.History                     0.07          0.011
		History and Society.Military and warfare        0.081         0.015
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.098         0.013
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.118         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.007
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.338         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.042, macro=0.014):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.112
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.004
		Culture.Literature                           0.014
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.071
		Culture.Media.Music                          0.018
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.006
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.003
		Culture.Sports                               0.042
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.013
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.036
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.016
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.011
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.071
		Geography.Regions.Europe.Northern Europe     0.013
		Geography.Regions.Europe.Southern Europe     0.01
		Geography.Regions.Europe.Western Europe      0.017
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.004
		History and Society.Education                0.002
		History and Society.History                  0.008
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.009
		History and Society.Society                  0.004
		History and Society.Transportation           0.015
		STEM.Biology                                 0.032
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.088
		STEM.Space                                   0.004
		STEM.Technology                              0.011
		-------------------------------------------  -----
	filter_rate (micro=0.958, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.888
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.929
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.997
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.929
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.992
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.991
		History and Society.Society                  0.996
		History and Society.Transportation           0.985
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.912
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	recall (micro=0.503, macro=0.419):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.557
		Culture.Biography.Women                      0.253
		Culture.Food and drink                       0.123
		Culture.Internet culture                     0.709
		Culture.Linguistics                          0.37
		Culture.Literature                           0.407
		Culture.Media.Books                          0.226
		Culture.Media.Entertainment                  0.305
		Culture.Media.Films                          0.571
		Culture.Media.Media*                         0.684
		Culture.Media.Music                          0.627
		Culture.Media.Radio                          0.553
		Culture.Media.Software                       0.691
		Culture.Media.Television                     0.415
		Culture.Media.Video games                    0.858
		Culture.Performing arts                      0.343
		Culture.Philosophy and religion              0.108
		Culture.Sports                               0.645
		Culture.Visual arts.Architecture             0.218
		Culture.Visual arts.Comics and Anime         0.799
		Culture.Visual arts.Fashion                  0.277
		Culture.Visual arts.Visual arts*             0.38
		Geography.Geographical                       0.302
		Geography.Regions.Africa.Africa*             0.344
		Geography.Regions.Africa.Central Africa      0.188
		Geography.Regions.Africa.Eastern Africa      0.469
		Geography.Regions.Africa.Northern Africa     0.38
		Geography.Regions.Africa.Southern Africa     0.324
		Geography.Regions.Africa.Western Africa      0.321
		Geography.Regions.Americas.Central America   0.111
		Geography.Regions.Americas.North America     0.418
		Geography.Regions.Americas.South America     0.324
		Geography.Regions.Asia.Asia*                 0.538
		Geography.Regions.Asia.Central Asia          0.203
		Geography.Regions.Asia.East Asia             0.436
		Geography.Regions.Asia.North Asia            0.34
		Geography.Regions.Asia.South Asia            0.555
		Geography.Regions.Asia.Southeast Asia        0.232
		Geography.Regions.Asia.West Asia             0.638
		Geography.Regions.Europe.Eastern Europe      0.447
		Geography.Regions.Europe.Europe*             0.543
		Geography.Regions.Europe.Northern Europe     0.3
		Geography.Regions.Europe.Southern Europe     0.481
		Geography.Regions.Europe.Western Europe      0.561
		Geography.Regions.Oceania                    0.462
		History and Society.Business and economics   0.151
		History and Society.Education                0.127
		History and Society.History                  0.211
		History and Society.Military and warfare     0.451
		History and Society.Politics and government  0.206
		History and Society.Society                  0.14
		History and Society.Transportation           0.745
		STEM.Biology                                 0.824
		STEM.Chemistry                               0.443
		STEM.Computing                               0.555
		STEM.Earth and environment                   0.156
		STEM.Engineering                             0.651
		STEM.Libraries & Information                 0.454
		STEM.Mathematics                             0.337
		STEM.Medicine & Health                       0.344
		STEM.Physics                                 0.226
		STEM.STEM*                                   0.749
		STEM.Space                                   0.549
		STEM.Technology                              0.443
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.95
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.998
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.99
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.998
		History and Society.Education                0.999
		History and Society.History                  0.995
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.996
		History and Society.Society                  0.998
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.958
		STEM.Space                                   0.998
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.601, macro=0.454):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.605
		Culture.Biography.Women                      0.299
		Culture.Food and drink                       0.199
		Culture.Internet culture                     0.345
		Culture.Linguistics                          0.681
		Culture.Literature                           0.425
		Culture.Media.Books                          0.455
		Culture.Media.Entertainment                  0.386
		Culture.Media.Films                          0.638
		Culture.Media.Media*                         0.534
		Culture.Media.Music                          0.732
		Culture.Media.Radio                          0.698
		Culture.Media.Software                       0.152
		Culture.Media.Television                     0.669
		Culture.Media.Video games                    0.594
		Culture.Performing arts                      0.45
		Culture.Philosophy and religion              0.326
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.499
		Culture.Visual arts.Comics and Anime         0.493
		Culture.Visual arts.Fashion                  0.167
		Culture.Visual arts.Visual arts*             0.534
		Geography.Geographical                       0.518
		Geography.Regions.Africa.Africa*             0.216
		Geography.Regions.Africa.Central Africa      0.085
		Geography.Regions.Africa.Eastern Africa      0.168
		Geography.Regions.Africa.Northern Africa     0.101
		Geography.Regions.Africa.Southern Africa     0.219
		Geography.Regions.Africa.Western Africa      0.221
		Geography.Regions.Americas.Central America   0.281
		Geography.Regions.Americas.North America     0.742
		Geography.Regions.Americas.South America     0.454
		Geography.Regions.Asia.Asia*                 0.438
		Geography.Regions.Asia.Central Asia          0.142
		Geography.Regions.Asia.East Asia             0.331
		Geography.Regions.Asia.North Asia            0.142
		Geography.Regions.Asia.South Asia            0.868
		Geography.Regions.Asia.Southeast Asia        0.346
		Geography.Regions.Asia.West Asia             0.785
		Geography.Regions.Europe.Eastern Europe      0.63
		Geography.Regions.Europe.Europe*             0.596
		Geography.Regions.Europe.Northern Europe     0.7
		Geography.Regions.Europe.Southern Europe     0.674
		Geography.Regions.Europe.Western Europe      0.667
		Geography.Regions.Oceania                    0.661
		History and Society.Business and economics   0.396
		History and Society.Education                0.543
		History and Society.History                  0.305
		History and Society.Military and warfare     0.519
		History and Society.Politics and government  0.626
		History and Society.Society                  0.441
		History and Society.Transportation           0.831
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.195
		STEM.Computing                               0.236
		STEM.Earth and environment                   0.401
		STEM.Engineering                             0.658
		STEM.Libraries & Information                 0.217
		STEM.Mathematics                             0.11
		STEM.Medicine & Health                       0.443
		STEM.Physics                                 0.104
		STEM.STEM*                                   0.557
		STEM.Space                                   0.529
		STEM.Technology                              0.215
		-------------------------------------------  -----
	!precision (micro=0.978, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.939
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.995
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.991
		History and Society.Business and economics   0.992
		History and Society.Education                0.993
		History and Society.History                  0.991
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.977
		History and Society.Society                  0.988
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.998
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.53, macro=0.406):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.58
		Culture.Biography.Women                      0.274
		Culture.Food and drink                       0.152
		Culture.Internet culture                     0.464
		Culture.Linguistics                          0.479
		Culture.Literature                           0.416
		Culture.Media.Books                          0.302
		Culture.Media.Entertainment                  0.34
		Culture.Media.Films                          0.602
		Culture.Media.Media*                         0.6
		Culture.Media.Music                          0.675
		Culture.Media.Radio                          0.617
		Culture.Media.Software                       0.249
		Culture.Media.Television                     0.512
		Culture.Media.Video games                    0.702
		Culture.Performing arts                      0.389
		Culture.Philosophy and religion              0.162
		Culture.Sports                               0.762
		Culture.Visual arts.Architecture             0.303
		Culture.Visual arts.Comics and Anime         0.61
		Culture.Visual arts.Fashion                  0.208
		Culture.Visual arts.Visual arts*             0.444
		Geography.Geographical                       0.381
		Geography.Regions.Africa.Africa*             0.265
		Geography.Regions.Africa.Central Africa      0.117
		Geography.Regions.Africa.Eastern Africa      0.247
		Geography.Regions.Africa.Northern Africa     0.16
		Geography.Regions.Africa.Southern Africa     0.261
		Geography.Regions.Africa.Western Africa      0.262
		Geography.Regions.Americas.Central America   0.159
		Geography.Regions.Americas.North America     0.535
		Geography.Regions.Americas.South America     0.378
		Geography.Regions.Asia.Asia*                 0.483
		Geography.Regions.Asia.Central Asia          0.167
		Geography.Regions.Asia.East Asia             0.376
		Geography.Regions.Asia.North Asia            0.2
		Geography.Regions.Asia.South Asia            0.677
		Geography.Regions.Asia.Southeast Asia        0.278
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.523
		Geography.Regions.Europe.Europe*             0.568
		Geography.Regions.Europe.Northern Europe     0.419
		Geography.Regions.Europe.Southern Europe     0.561
		Geography.Regions.Europe.Western Europe      0.609
		Geography.Regions.Oceania                    0.544
		History and Society.Business and economics   0.219
		History and Society.Education                0.206
		History and Society.History                  0.249
		History and Society.Military and warfare     0.483
		History and Society.Politics and government  0.31
		History and Society.Society                  0.213
		History and Society.Transportation           0.786
		STEM.Biology                                 0.865
		STEM.Chemistry                               0.271
		STEM.Computing                               0.331
		STEM.Earth and environment                   0.224
		STEM.Engineering                             0.654
		STEM.Libraries & Information                 0.294
		STEM.Mathematics                             0.166
		STEM.Medicine & Health                       0.387
		STEM.Physics                                 0.142
		STEM.STEM*                                   0.639
		STEM.Space                                   0.539
		STEM.Technology                              0.289
		-------------------------------------------  -----
	!f1 (micro=0.98, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.944
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.963, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.902
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.983
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.991
		Culture.Media.Media*                         0.949
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.944
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.974
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.944
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.05
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.002
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.006
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.01
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.035
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.031
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.002
		History and Society.Education                0.001
		History and Society.History                  0.005
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.004
		History and Society.Society                  0.002
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.042
		STEM.Space                                   0.002
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.918, macro=0.921):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.9
		Culture.Biography.Women                      0.907
		Culture.Food and drink                       0.907
		Culture.Internet culture                     0.973
		Culture.Linguistics                          0.899
		Culture.Literature                           0.925
		Culture.Media.Books                          0.927
		Culture.Media.Entertainment                  0.937
		Culture.Media.Films                          0.964
		Culture.Media.Media*                         0.942
		Culture.Media.Music                          0.963
		Culture.Media.Radio                          0.895
		Culture.Media.Software                       0.974
		Culture.Media.Television                     0.948
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.935
		Culture.Philosophy and religion              0.878
		Culture.Sports                               0.939
		Culture.Visual arts.Architecture             0.915
		Culture.Visual arts.Comics and Anime         0.979
		Culture.Visual arts.Fashion                  0.916
		Culture.Visual arts.Visual arts*             0.907
		Geography.Geographical                       0.904
		Geography.Regions.Africa.Africa*             0.895
		Geography.Regions.Africa.Central Africa      0.911
		Geography.Regions.Africa.Eastern Africa      0.903
		Geography.Regions.Africa.Northern Africa     0.92
		Geography.Regions.Africa.Southern Africa     0.905
		Geography.Regions.Africa.Western Africa      0.934
		Geography.Regions.Americas.Central America   0.872
		Geography.Regions.Americas.North America     0.916
		Geography.Regions.Americas.South America     0.914
		Geography.Regions.Asia.Asia*                 0.889
		Geography.Regions.Asia.Central Asia          0.911
		Geography.Regions.Asia.East Asia             0.913
		Geography.Regions.Asia.North Asia            0.938
		Geography.Regions.Asia.South Asia            0.935
		Geography.Regions.Asia.Southeast Asia        0.881
		Geography.Regions.Asia.West Asia             0.948
		Geography.Regions.Europe.Eastern Europe      0.931
		Geography.Regions.Europe.Europe*             0.899
		Geography.Regions.Europe.Northern Europe     0.9
		Geography.Regions.Europe.Southern Europe     0.926
		Geography.Regions.Europe.Western Europe      0.942
		Geography.Regions.Oceania                    0.942
		History and Society.Business and economics   0.875
		History and Society.Education                0.884
		History and Society.History                  0.888
		History and Society.Military and warfare     0.917
		History and Society.Politics and government  0.858
		History and Society.Society                  0.823
		History and Society.Transportation           0.962
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.947
		STEM.Computing                               0.959
		STEM.Earth and environment                   0.895
		STEM.Engineering                             0.945
		STEM.Libraries & Information                 0.899
		STEM.Mathematics                             0.938
		STEM.Medicine & Health                       0.93
		STEM.Physics                                 0.921
		STEM.STEM*                                   0.938
		STEM.Space                                   0.947
		STEM.Technology                              0.926
		-------------------------------------------  -----
	pr_auc (micro=0.552, macro=0.365):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.633
		Culture.Biography.Women                      0.229
		Culture.Food and drink                       0.082
		Culture.Internet culture                     0.482
		Culture.Linguistics                          0.399
		Culture.Literature                           0.436
		Culture.Media.Books                          0.233
		Culture.Media.Entertainment                  0.289
		Culture.Media.Films                          0.589
		Culture.Media.Media*                         0.66
		Culture.Media.Music                          0.695
		Culture.Media.Radio                          0.405
		Culture.Media.Software                       0.183
		Culture.Media.Television                     0.499
		Culture.Media.Video games                    0.72
		Culture.Performing arts                      0.263
		Culture.Philosophy and religion              0.141
		Culture.Sports                               0.816
		Culture.Visual arts.Architecture             0.282
		Culture.Visual arts.Comics and Anime         0.647
		Culture.Visual arts.Fashion                  0.099
		Culture.Visual arts.Visual arts*             0.43
		Geography.Geographical                       0.373
		Geography.Regions.Africa.Africa*             0.204
		Geography.Regions.Africa.Central Africa      0.035
		Geography.Regions.Africa.Eastern Africa      0.102
		Geography.Regions.Africa.Northern Africa     0.075
		Geography.Regions.Africa.Southern Africa     0.141
		Geography.Regions.Africa.Western Africa      0.103
		Geography.Regions.Americas.Central America   0.087
		Geography.Regions.Americas.North America     0.632
		Geography.Regions.Americas.South America     0.307
		Geography.Regions.Asia.Asia*                 0.495
		Geography.Regions.Asia.Central Asia          0.066
		Geography.Regions.Asia.East Asia             0.3
		Geography.Regions.Asia.North Asia            0.082
		Geography.Regions.Asia.South Asia            0.689
		Geography.Regions.Asia.Southeast Asia        0.187
		Geography.Regions.Asia.West Asia             0.654
		Geography.Regions.Europe.Eastern Europe      0.508
		Geography.Regions.Europe.Europe*             0.617
		Geography.Regions.Europe.Northern Europe     0.457
		Geography.Regions.Europe.Southern Europe     0.526
		Geography.Regions.Europe.Western Europe      0.632
		Geography.Regions.Oceania                    0.541
		History and Society.Business and economics   0.175
		History and Society.Education                0.195
		History and Society.History                  0.178
		History and Society.Military and warfare     0.442
		History and Society.Politics and government  0.327
		History and Society.Society                  0.186
		History and Society.Transportation           0.806
		STEM.Biology                                 0.897
		STEM.Chemistry                               0.143
		STEM.Computing                               0.244
		STEM.Earth and environment                   0.158
		STEM.Engineering                             0.648
		STEM.Libraries & Information                 0.109
		STEM.Mathematics                             0.059
		STEM.Medicine & Health                       0.29
		STEM.Physics                                 0.043
		STEM.STEM*                                   0.758
		STEM.Space                                   0.433
		STEM.Technology                              0.224
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

