Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'scale': False, 'min_weight_fraction_leaf': 0.0, 'min_samples_split': 2, 'center': False, 'population_rates': None, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'n_estimators': 150, 'learning_rate': 0.1, 'multilabel': True, 'max_depth': 5, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'verbose': 0, 'tol': 0.0001, 'random_state': None, 'loss': 'deviance', 'min_samples_leaf': 1, 'init': None, 'max_features': 'log2', 'warm_start': False, 'criterion': 'friedman_mse', 'max_leaf_nodes': None, 'subsample': 1.0, 'presort': 'auto', 'n_iter_no_change': None, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.6.2-no_zero_vectors'
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
	counts (n=63017):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16717  -->  14282  2435  1291  45009
			'Culture.Biography.Women'                       4173  -->   1269  2904   635  58209
			'Culture.Food and drink'                        1323  -->    914   409   116  61578
			'Culture.Internet culture'                      2946  -->   2084   862   230  59841
			'Culture.Linguistics'                           1384  -->    996   388   104  61529
			'Culture.Literature'                            5277  -->   3662  1615   638  57102
			'Culture.Media.Books'                           1919  -->   1287   632   209  60889
			'Culture.Media.Entertainment'                   1876  -->    619  1257   129  61012
			'Culture.Media.Films'                           2307  -->   1812   495   146  60564
			'Culture.Media.Media*'                         14363  -->  11814  2549  1972  46682
			'Culture.Media.Music'                           2677  -->   2149   528   318  60022
			'Culture.Media.Radio'                           1174  -->    914   260    55  61788
			'Culture.Media.Software'                        1798  -->    912   886   446  60773
			'Culture.Media.Television'                      2200  -->   1368   832   243  60574
			'Culture.Media.Video games'                     2078  -->   1738   340    56  60883
			'Culture.Performing arts'                       1334  -->    744   590   135  61548
			'Culture.Philosophy and religion'               2638  -->   1196  1442   344  60035
			'Culture.Sports'                                5843  -->   5179   664   404  56770
			'Culture.Visual arts.Architecture'              2565  -->   1762   803   362  60090
			'Culture.Visual arts.Comics and Anime'          1488  -->    884   604   137  61392
			'Culture.Visual arts.Fashion'                   1188  -->    745   443    97  61732
			'Culture.Visual arts.Visual arts*'              5987  -->   3824  2163   684  56346
			'Geography.Geographical'                        3344  -->   1943  1401   351  59322
			'Geography.Regions.Africa.Africa*'              5693  -->    836  4857   281  57043
			'Geography.Regions.Africa.Central Africa'         28  -->      2    26    48  62941
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    151   963    64  61839
			'Geography.Regions.Africa.Northern Africa'      1266  -->     98  1168    91  61660
			'Geography.Regions.Africa.Southern Africa'      1288  -->    201  1087    79  61650
			'Geography.Regions.Africa.Western Africa'       1152  -->    125  1027    88  61777
			'Geography.Regions.Americas.Central America'    1326  -->     48  1278    84  61607
			'Geography.Regions.Americas.North America'      7565  -->   2572  4993   490  54962
			'Geography.Regions.Americas.South America'      1523  -->    202  1321   159  61335
			'Geography.Regions.Asia.Asia*'                 11060  -->   3437  7623   796  51161
			'Geography.Regions.Asia.Central Asia'           1163  -->    155  1008   108  61746
			'Geography.Regions.Asia.East Asia'              2721  -->    453  2268   126  60170
			'Geography.Regions.Asia.North Asia'             1361  -->    162  1199    84  61572
			'Geography.Regions.Asia.South Asia'             2438  -->    607  1831    98  60481
			'Geography.Regions.Asia.Southeast Asia'         1688  -->     61  1627    61  61268
			'Geography.Regions.Asia.West Asia'              2264  -->    896  1368    78  60675
			'Geography.Regions.Europe.Eastern Europe'       3083  -->    633  2450   112  59822
			'Geography.Regions.Europe.Europe*'             12415  -->   3819  8596  1285  49317
			'Geography.Regions.Europe.Northern Europe'      4244  -->    546  3698   165  58608
			'Geography.Regions.Europe.Southern Europe'      2320  -->    316  2004   148  60549
			'Geography.Regions.Europe.Western Europe'       3160  -->    682  2478   246  59611
			'Geography.Regions.Oceania'                     2537  -->    275  2262    81  60399
			'History and Society.Business and economics'    3430  -->   1594  1836   623  58964
			'History and Society.Education'                 2178  -->   1026  1152   253  60586
			'History and Society.History'                   3217  -->    742  2475   349  59451
			'History and Society.Military and warfare'      3977  -->   2124  1853   353  58687
			'History and Society.Politics and government'   4647  -->   1297  3350   459  57911
			'History and Society.Society'                   4057  -->    513  3544   201  58759
			'History and Society.Transportation'            3604  -->   2935   669   266  59147
			'STEM.Biology'                                  2834  -->   2226   608   177  60006
			'STEM.Chemistry'                                1344  -->    914   430   216  61457
			'STEM.Computing'                                2011  -->   1233   778   451  60555
			'STEM.Earth and environment'                    1683  -->   1003   680   159  61175
			'STEM.Engineering'                              2272  -->   1402   870   195  60550
			'STEM.Libraries & Information'                  1159  -->    555   604    95  61763
			'STEM.Mathematics'                              1121  -->    659   462   129  61767
			'STEM.Medicine & Health'                        1737  -->   1071   666   199  61081
			'STEM.Physics'                                  1206  -->    735   471   176  61635
			'STEM.STEM*'                                   16499  -->  13602  2897  1318  45200
			'STEM.Space'                                    1398  -->   1131   267    49  61570
			'STEM.Technology'                               3712  -->   1913  1799   768  58537
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.265         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.047         0.004
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.228         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.029         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.093         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.053         0.024
		Geography.Regions.Africa.Africa*                0.09          0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.12          0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.176         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.197         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.05          0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.262         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.059         0.005
	match_rate (micro=0.044, macro=0.014):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.022
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.03
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.029
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.005
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.006
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.047
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.015
		History and Society.Education                0.008
		History and Society.History                  0.008
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.016
		History and Society.Society                  0.005
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.005
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.956, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.978
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.992
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.984
		History and Society.Society                  0.995
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.995
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.555, macro=0.461):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.304
		Culture.Food and drink                       0.691
		Culture.Internet culture                     0.707
		Culture.Linguistics                          0.72
		Culture.Literature                           0.694
		Culture.Media.Books                          0.671
		Culture.Media.Entertainment                  0.33
		Culture.Media.Films                          0.785
		Culture.Media.Media*                         0.823
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.779
		Culture.Media.Software                       0.507
		Culture.Media.Television                     0.622
		Culture.Media.Video games                    0.836
		Culture.Performing arts                      0.558
		Culture.Philosophy and religion              0.453
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.687
		Culture.Visual arts.Comics and Anime         0.594
		Culture.Visual arts.Fashion                  0.627
		Culture.Visual arts.Visual arts*             0.639
		Geography.Geographical                       0.581
		Geography.Regions.Africa.Africa*             0.147
		Geography.Regions.Africa.Central Africa      0.071
		Geography.Regions.Africa.Eastern Africa      0.136
		Geography.Regions.Africa.Northern Africa     0.077
		Geography.Regions.Africa.Southern Africa     0.156
		Geography.Regions.Africa.Western Africa      0.109
		Geography.Regions.Americas.Central America   0.036
		Geography.Regions.Americas.North America     0.34
		Geography.Regions.Americas.South America     0.133
		Geography.Regions.Asia.Asia*                 0.311
		Geography.Regions.Asia.Central Asia          0.133
		Geography.Regions.Asia.East Asia             0.166
		Geography.Regions.Asia.North Asia            0.119
		Geography.Regions.Asia.South Asia            0.249
		Geography.Regions.Asia.Southeast Asia        0.036
		Geography.Regions.Asia.West Asia             0.396
		Geography.Regions.Europe.Eastern Europe      0.205
		Geography.Regions.Europe.Europe*             0.308
		Geography.Regions.Europe.Northern Europe     0.129
		Geography.Regions.Europe.Southern Europe     0.136
		Geography.Regions.Europe.Western Europe      0.216
		Geography.Regions.Oceania                    0.108
		History and Society.Business and economics   0.465
		History and Society.Education                0.471
		History and Society.History                  0.231
		History and Society.Military and warfare     0.534
		History and Society.Politics and government  0.279
		History and Society.Society                  0.126
		History and Society.Transportation           0.814
		STEM.Biology                                 0.785
		STEM.Chemistry                               0.68
		STEM.Computing                               0.613
		STEM.Earth and environment                   0.596
		STEM.Engineering                             0.617
		STEM.Libraries & Information                 0.479
		STEM.Mathematics                             0.588
		STEM.Medicine & Health                       0.617
		STEM.Physics                                 0.609
		STEM.STEM*                                   0.824
		STEM.Space                                   0.809
		STEM.Technology                              0.515
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.991
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.99
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.997
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.621, macro=0.438):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.811
		Culture.Biography.Women                      0.294
		Culture.Food and drink                       0.476
		Culture.Internet culture                     0.394
		Culture.Linguistics                          0.759
		Culture.Literature                           0.497
		Culture.Media.Books                          0.442
		Culture.Media.Entertainment                  0.36
		Culture.Media.Films                          0.776
		Culture.Media.Media*                         0.558
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.654
		Culture.Media.Software                       0.085
		Culture.Media.Television                     0.581
		Culture.Media.Video games                    0.705
		Culture.Performing arts                      0.425
		Culture.Philosophy and religion              0.462
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.551
		Culture.Visual arts.Comics and Anime         0.37
		Culture.Visual arts.Fashion                  0.245
		Culture.Visual arts.Visual arts*             0.498
		Geography.Geographical                       0.705
		Geography.Regions.Africa.Africa*             0.191
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.056
		Geography.Regions.Africa.Northern Africa     0.061
		Geography.Regions.Africa.Southern Africa     0.126
		Geography.Regions.Africa.Western Africa      0.05
		Geography.Regions.Americas.Central America   0.081
		Geography.Regions.Americas.North America     0.726
		Geography.Regions.Americas.South America     0.246
		Geography.Regions.Asia.Asia*                 0.492
		Geography.Regions.Asia.Central Asia          0.062
		Geography.Regions.Asia.East Asia             0.479
		Geography.Regions.Asia.North Asia            0.075
		Geography.Regions.Asia.South Asia            0.704
		Geography.Regions.Asia.Southeast Asia        0.18
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.588
		Geography.Regions.Europe.Europe*             0.5
		Geography.Regions.Europe.Northern Europe     0.591
		Geography.Regions.Europe.Southern Europe     0.425
		Geography.Regions.Europe.Western Europe      0.507
		Geography.Regions.Oceania                    0.554
		History and Society.Business and economics   0.312
		History and Society.Education                0.456
		History and Society.History                  0.302
		History and Society.Military and warfare     0.56
		History and Society.Politics and government  0.507
		History and Society.Society                  0.322
		History and Society.Transportation           0.736
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.233
		STEM.Computing                               0.183
		STEM.Earth and environment                   0.512
		STEM.Engineering                             0.503
		STEM.Libraries & Information                 0.162
		STEM.Mathematics                             0.105
		STEM.Medicine & Health                       0.55
		STEM.Physics                                 0.154
		STEM.STEM*                                   0.684
		STEM.Space                                   0.86
		STEM.Technology                              0.17
		-------------------------------------------  -----
	!precision (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.945
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.979
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.56, macro=0.414):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.832
		Culture.Biography.Women                      0.299
		Culture.Food and drink                       0.564
		Culture.Internet culture                     0.506
		Culture.Linguistics                          0.739
		Culture.Literature                           0.579
		Culture.Media.Books                          0.533
		Culture.Media.Entertainment                  0.344
		Culture.Media.Films                          0.781
		Culture.Media.Media*                         0.665
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.711
		Culture.Media.Software                       0.145
		Culture.Media.Television                     0.601
		Culture.Media.Video games                    0.765
		Culture.Performing arts                      0.482
		Culture.Philosophy and religion              0.457
		Culture.Sports                               0.896
		Culture.Visual arts.Architecture             0.611
		Culture.Visual arts.Comics and Anime         0.456
		Culture.Visual arts.Fashion                  0.352
		Culture.Visual arts.Visual arts*             0.56
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.166
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.08
		Geography.Regions.Africa.Northern Africa     0.068
		Geography.Regions.Africa.Southern Africa     0.139
		Geography.Regions.Africa.Western Africa      0.068
		Geography.Regions.Americas.Central America   0.05
		Geography.Regions.Americas.North America     0.463
		Geography.Regions.Americas.South America     0.172
		Geography.Regions.Asia.Asia*                 0.381
		Geography.Regions.Asia.Central Asia          0.085
		Geography.Regions.Asia.East Asia             0.247
		Geography.Regions.Asia.North Asia            0.092
		Geography.Regions.Asia.South Asia            0.368
		Geography.Regions.Asia.Southeast Asia        0.06
		Geography.Regions.Asia.West Asia             0.523
		Geography.Regions.Europe.Eastern Europe      0.304
		Geography.Regions.Europe.Europe*             0.381
		Geography.Regions.Europe.Northern Europe     0.211
		Geography.Regions.Europe.Southern Europe     0.206
		Geography.Regions.Europe.Western Europe      0.303
		Geography.Regions.Oceania                    0.181
		History and Society.Business and economics   0.373
		History and Society.Education                0.464
		History and Society.History                  0.262
		History and Society.Military and warfare     0.547
		History and Society.Politics and government  0.36
		History and Society.Society                  0.182
		History and Society.Transportation           0.773
		STEM.Biology                                 0.84
		STEM.Chemistry                               0.347
		STEM.Computing                               0.282
		STEM.Earth and environment                   0.551
		STEM.Engineering                             0.554
		STEM.Libraries & Information                 0.243
		STEM.Mathematics                             0.179
		STEM.Medicine & Health                       0.582
		STEM.Physics                                 0.246
		STEM.STEM*                                   0.748
		STEM.Space                                   0.834
		STEM.Technology                              0.256
		-------------------------------------------  -----
	!f1 (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.971, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.984
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.951
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.954
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.924
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.984
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.972
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.028
		Culture.Biography.Women                      0.011
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.041
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.006
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.012
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.009
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.015
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.002
		Geography.Regions.Europe.Europe*             0.025
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.01
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.008
		History and Society.Society                  0.003
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.93, macro=0.929):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.937
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.968
		Culture.Literature                           0.971
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.953
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.986
		Culture.Media.Software                       0.976
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.947
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.98
		Culture.Visual arts.Fashion                  0.979
		Culture.Visual arts.Visual arts*             0.961
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.861
		Geography.Regions.Africa.Central Africa      0.552
		Geography.Regions.Africa.Eastern Africa      0.894
		Geography.Regions.Africa.Northern Africa     0.867
		Geography.Regions.Africa.Southern Africa     0.862
		Geography.Regions.Africa.Western Africa      0.898
		Geography.Regions.Americas.Central America   0.846
		Geography.Regions.Americas.North America     0.888
		Geography.Regions.Americas.South America     0.893
		Geography.Regions.Asia.Asia*                 0.86
		Geography.Regions.Asia.Central Asia          0.897
		Geography.Regions.Asia.East Asia             0.869
		Geography.Regions.Asia.North Asia            0.921
		Geography.Regions.Asia.South Asia            0.896
		Geography.Regions.Asia.Southeast Asia        0.817
		Geography.Regions.Asia.West Asia             0.892
		Geography.Regions.Europe.Eastern Europe      0.896
		Geography.Regions.Europe.Europe*             0.847
		Geography.Regions.Europe.Northern Europe     0.841
		Geography.Regions.Europe.Southern Europe     0.867
		Geography.Regions.Europe.Western Europe      0.89
		Geography.Regions.Oceania                    0.858
		History and Society.Business and economics   0.953
		History and Society.Education                0.956
		History and Society.History                  0.911
		History and Society.Military and warfare     0.949
		History and Society.Politics and government  0.884
		History and Society.Society                  0.833
		History and Society.Transportation           0.984
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.984
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.971
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.967
		STEM.Space                                   0.991
		STEM.Technology                              0.959
		-------------------------------------------  -----
	pr_auc (micro=0.588, macro=0.407):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.225
		Culture.Food and drink                       0.557
		Culture.Internet culture                     0.678
		Culture.Linguistics                          0.735
		Culture.Literature                           0.632
		Culture.Media.Books                          0.477
		Culture.Media.Entertainment                  0.261
		Culture.Media.Films                          0.776
		Culture.Media.Media*                         0.773
		Culture.Media.Music                          0.828
		Culture.Media.Radio                          0.784
		Culture.Media.Software                       0.088
		Culture.Media.Television                     0.586
		Culture.Media.Video games                    0.858
		Culture.Performing arts                      0.437
		Culture.Philosophy and religion              0.383
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.662
		Culture.Visual arts.Comics and Anime         0.456
		Culture.Visual arts.Fashion                  0.263
		Culture.Visual arts.Visual arts*             0.55
		Geography.Geographical                       0.666
		Geography.Regions.Africa.Africa*             0.103
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.029
		Geography.Regions.Africa.Northern Africa     0.021
		Geography.Regions.Africa.Southern Africa     0.043
		Geography.Regions.Africa.Western Africa      0.018
		Geography.Regions.Americas.Central America   0.03
		Geography.Regions.Americas.North America     0.539
		Geography.Regions.Americas.South America     0.12
		Geography.Regions.Asia.Asia*                 0.399
		Geography.Regions.Asia.Central Asia          0.03
		Geography.Regions.Asia.East Asia             0.227
		Geography.Regions.Asia.North Asia            0.027
		Geography.Regions.Asia.South Asia            0.36
		Geography.Regions.Asia.Southeast Asia        0.046
		Geography.Regions.Asia.West Asia             0.459
		Geography.Regions.Europe.Eastern Europe      0.307
		Geography.Regions.Europe.Europe*             0.416
		Geography.Regions.Europe.Northern Europe     0.272
		Geography.Regions.Europe.Southern Europe     0.187
		Geography.Regions.Europe.Western Europe      0.301
		Geography.Regions.Oceania                    0.205
		History and Society.Business and economics   0.286
		History and Society.Education                0.402
		History and Society.History                  0.18
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.343
		History and Society.Society                  0.148
		History and Society.Transportation           0.808
		STEM.Biology                                 0.877
		STEM.Chemistry                               0.383
		STEM.Computing                               0.237
		STEM.Earth and environment                   0.536
		STEM.Engineering                             0.536
		STEM.Libraries & Information                 0.238
		STEM.Mathematics                             0.173
		STEM.Medicine & Health                       0.551
		STEM.Physics                                 0.274
		STEM.STEM*                                   0.83
		STEM.Space                                   0.887
		STEM.Technology                              0.211
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}}}}}

