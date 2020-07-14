Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'label_weights': {}, 'init': None, 'loss': 'deviance', 'max_depth': 5, 'learning_rate': 0.1, 'center': False, 'verbose': 0, 'n_iter_no_change': None, 'random_state': None, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_impurity_split': None, 'n_estimators': 150, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'presort': 'auto', 'scale': False, 'population_rates': None, 'multilabel': True, 'tol': 0.0001, 'validation_fraction': 0.1, 'max_leaf_nodes': None, 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'min_samples_split': 2, 'criterion': 'friedman_mse'}
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
	counts (n=59911):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14169  -->  12438  1731   914  44828
			'Culture.Biography.Women'                       5028  -->   3823  1205   830  54053
			'Culture.Food and drink'                        1364  -->    883   481   138  58409
			'Culture.Internet culture'                      3550  -->   2805   745   269  56092
			'Culture.Linguistics'                           1471  -->   1076   395    82  58358
			'Culture.Literature'                            5443  -->   3995  1448   517  53951
			'Culture.Media.Books'                           1391  -->    919   472   139  58381
			'Culture.Media.Entertainment'                   1875  -->    832  1043   174  57862
			'Culture.Media.Films'                           2568  -->   1950   618   190  57153
			'Culture.Media.Media*'                         12947  -->  10977  1970  1408  45556
			'Culture.Media.Music'                           2768  -->   2248   520   199  56944
			'Culture.Media.Radio'                            280  -->    179   101    26  59605
			'Culture.Media.Software'                        2169  -->   1670   499   301  57441
			'Culture.Media.Television'                      1980  -->   1294   686   173  57758
			'Culture.Media.Video games'                     2219  -->   1990   229    70  57622
			'Culture.Performing arts'                       1336  -->    837   499   132  58443
			'Culture.Philosophy and religion'               2938  -->   1457  1481   263  56710
			'Culture.Sports'                                4031  -->   3473   558   132  55748
			'Culture.Visual arts.Architecture'              1810  -->   1232   578   170  57931
			'Culture.Visual arts.Comics and Anime'          2270  -->   1968   302   122  57519
			'Culture.Visual arts.Fashion'                   1491  -->   1203   288    90  58330
			'Culture.Visual arts.Visual arts*'              6066  -->   4434  1632   450  53395
			'Geography.Geographical'                        3889  -->   2479  1410   518  55504
			'Geography.Regions.Africa.Africa*'              5660  -->   4166  1494   515  53736
			'Geography.Regions.Africa.Central Africa'       1203  -->    744   459   144  58564
			'Geography.Regions.Africa.Eastern Africa'        431  -->    213   218    52  59428
			'Geography.Regions.Africa.Northern Africa'      1448  -->    970   478    90  58373
			'Geography.Regions.Africa.Southern Africa'      1167  -->    790   377    74  58670
			'Geography.Regions.Africa.Western Africa'        673  -->    519   154    55  59183
			'Geography.Regions.Americas.Central America'    1616  -->    926   690   142  58153
			'Geography.Regions.Americas.North America'      5197  -->   3362  1835   590  54124
			'Geography.Regions.Americas.South America'      2173  -->   1542   631   183  57555
			'Geography.Regions.Asia.Asia*'                 14352  -->  11640  2712  1155  44404
			'Geography.Regions.Asia.Central Asia'           1066  -->    735   331    79  58766
			'Geography.Regions.Asia.East Asia'              5591  -->   4350  1241   483  53837
			'Geography.Regions.Asia.North Asia'             2490  -->   1756   734   210  57211
			'Geography.Regions.Asia.South Asia'             1886  -->   1447   439    95  57930
			'Geography.Regions.Asia.Southeast Asia'         2550  -->   1696   854   205  57156
			'Geography.Regions.Asia.West Asia'              2082  -->   1621   461   102  57727
			'Geography.Regions.Europe.Eastern Europe'       4108  -->   3087  1021   239  55564
			'Geography.Regions.Europe.Europe*'             12999  -->  10238  2761  1198  45714
			'Geography.Regions.Europe.Northern Europe'      2749  -->   1623  1126   262  56900
			'Geography.Regions.Europe.Southern Europe'      2724  -->   2015   709   177  57010
			'Geography.Regions.Europe.Western Europe'       3919  -->   2932   987   259  55733
			'Geography.Regions.Oceania'                     2339  -->   1636   703   148  57424
			'History and Society.Business and economics'    3172  -->   1692  1480   343  56396
			'History and Society.Education'                 1607  -->    850   757   124  58180
			'History and Society.History'                   4158  -->   1976  2182   496  55257
			'History and Society.Military and warfare'      4111  -->   2935  1176   399  55401
			'History and Society.Politics and government'   4239  -->   2121  2118   445  55227
			'History and Society.Society'                   4245  -->   1472  2773   296  55370
			'History and Society.Transportation'            3486  -->   3134   352   103  56322
			'STEM.Biology'                                  7223  -->   6595   628   180  52508
			'STEM.Chemistry'                                1400  -->   1008   392   179  58332
			'STEM.Computing'                                2332  -->   1775   557   345  57234
			'STEM.Earth and environment'                    1598  -->    984   614   140  58173
			'STEM.Engineering'                              2928  -->   2378   550   140  56843
			'STEM.Libraries & Information'                   484  -->    360   124    47  59380
			'STEM.Mathematics'                               888  -->    677   211    68  58955
			'STEM.Medicine & Health'                        1749  -->   1161   588   136  58026
			'STEM.Physics'                                  1376  -->    922   454   171  58364
			'STEM.STEM*'                                   20248  -->  18282  1966  1039  38624
			'STEM.Space'                                    1570  -->   1386   184    56  58285
			'STEM.Technology'                               4084  -->   2832  1252   587  55240
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.237         0.12
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.031         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.216         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.049         0.01
		Culture.Sports                                  0.067         0.06
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.038         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.094         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.087         0.063
		Geography.Regions.Americas.South America        0.036         0.007
		Geography.Regions.Asia.Asia*                    0.24          0.052
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.093         0.012
		Geography.Regions.Asia.North Asia               0.042         0.006
		Geography.Regions.Asia.South Asia               0.031         0.016
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.069         0.018
		Geography.Regions.Europe.Europe*                0.217         0.081
		Geography.Regions.Europe.Northern Europe        0.046         0.029
		Geography.Regions.Europe.Southern Europe        0.045         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.02
		Geography.Regions.Oceania                       0.039         0.016
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.069         0.011
		History and Society.Military and warfare        0.069         0.015
		History and Society.Politics and government     0.071         0.028
		History and Society.Society                     0.071         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.121         0.034
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.338         0.065
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.068         0.005
	match_rate (micro=0.049, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.123
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.054
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.016
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.067
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.087
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.014
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.022
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.083
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.951, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.933
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.913
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.986
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.978
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.917
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.763, macro=0.707):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.76
		Culture.Food and drink                       0.647
		Culture.Internet culture                     0.79
		Culture.Linguistics                          0.731
		Culture.Literature                           0.734
		Culture.Media.Books                          0.661
		Culture.Media.Entertainment                  0.444
		Culture.Media.Films                          0.759
		Culture.Media.Media*                         0.848
		Culture.Media.Music                          0.812
		Culture.Media.Radio                          0.639
		Culture.Media.Software                       0.77
		Culture.Media.Television                     0.654
		Culture.Media.Video games                    0.897
		Culture.Performing arts                      0.626
		Culture.Philosophy and religion              0.496
		Culture.Sports                               0.862
		Culture.Visual arts.Architecture             0.681
		Culture.Visual arts.Comics and Anime         0.867
		Culture.Visual arts.Fashion                  0.807
		Culture.Visual arts.Visual arts*             0.731
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.736
		Geography.Regions.Africa.Central Africa      0.618
		Geography.Regions.Africa.Eastern Africa      0.494
		Geography.Regions.Africa.Northern Africa     0.67
		Geography.Regions.Africa.Southern Africa     0.677
		Geography.Regions.Africa.Western Africa      0.771
		Geography.Regions.Americas.Central America   0.573
		Geography.Regions.Americas.North America     0.647
		Geography.Regions.Americas.South America     0.71
		Geography.Regions.Asia.Asia*                 0.811
		Geography.Regions.Asia.Central Asia          0.689
		Geography.Regions.Asia.East Asia             0.778
		Geography.Regions.Asia.North Asia            0.705
		Geography.Regions.Asia.South Asia            0.767
		Geography.Regions.Asia.Southeast Asia        0.665
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.751
		Geography.Regions.Europe.Europe*             0.788
		Geography.Regions.Europe.Northern Europe     0.59
		Geography.Regions.Europe.Southern Europe     0.74
		Geography.Regions.Europe.Western Europe      0.748
		Geography.Regions.Oceania                    0.699
		History and Society.Business and economics   0.533
		History and Society.Education                0.529
		History and Society.History                  0.475
		History and Society.Military and warfare     0.714
		History and Society.Politics and government  0.5
		History and Society.Society                  0.347
		History and Society.Transportation           0.899
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.72
		STEM.Computing                               0.761
		STEM.Earth and environment                   0.616
		STEM.Engineering                             0.812
		STEM.Libraries & Information                 0.744
		STEM.Mathematics                             0.762
		STEM.Medicine & Health                       0.664
		STEM.Physics                                 0.67
		STEM.STEM*                                   0.903
		STEM.Space                                   0.883
		STEM.Technology                              0.693
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.717, macro=0.563):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.857
		Culture.Biography.Women                      0.433
		Culture.Food and drink                       0.412
		Culture.Internet culture                     0.382
		Culture.Linguistics                          0.808
		Culture.Literature                           0.538
		Culture.Media.Books                          0.546
		Culture.Media.Entertainment                  0.369
		Culture.Media.Films                          0.728
		Culture.Media.Media*                         0.62
		Culture.Media.Music                          0.833
		Culture.Media.Radio                          0.773
		Culture.Media.Software                       0.151
		Culture.Media.Television                     0.662
		Culture.Media.Video games                    0.683
		Culture.Performing arts                      0.459
		Culture.Philosophy and religion              0.529
		Culture.Sports                               0.959
		Culture.Visual arts.Architecture             0.717
		Culture.Visual arts.Comics and Anime         0.495
		Culture.Visual arts.Fashion                  0.319
		Culture.Visual arts.Visual arts*             0.616
		Geography.Geographical                       0.598
		Geography.Regions.Africa.Africa*             0.398
		Geography.Regions.Africa.Central Africa      0.15
		Geography.Regions.Africa.Eastern Africa      0.221
		Geography.Regions.Africa.Northern Africa     0.37
		Geography.Regions.Africa.Southern Africa     0.413
		Geography.Regions.Africa.Western Africa      0.382
		Geography.Regions.Americas.Central America   0.449
		Geography.Regions.Americas.North America     0.801
		Geography.Regions.Americas.South America     0.606
		Geography.Regions.Asia.Asia*                 0.639
		Geography.Regions.Asia.Central Asia          0.29
		Geography.Regions.Asia.East Asia             0.518
		Geography.Regions.Asia.North Asia            0.52
		Geography.Regions.Asia.South Asia            0.887
		Geography.Regions.Asia.Southeast Asia        0.538
		Geography.Regions.Asia.West Asia             0.839
		Geography.Regions.Europe.Eastern Europe      0.765
		Geography.Regions.Europe.Europe*             0.73
		Geography.Regions.Europe.Northern Europe     0.793
		Geography.Regions.Europe.Southern Europe     0.77
		Geography.Regions.Europe.Western Europe      0.772
		Geography.Regions.Oceania                    0.819
		History and Society.Business and economics   0.464
		History and Society.Education                0.665
		History and Society.History                  0.37
		History and Society.Military and warfare     0.608
		History and Society.Politics and government  0.643
		History and Society.Society                  0.352
		History and Society.Transportation           0.89
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.285
		STEM.Computing                               0.27
		STEM.Earth and environment                   0.549
		STEM.Engineering                             0.656
		STEM.Libraries & Information                 0.391
		STEM.Mathematics                             0.234
		STEM.Medicine & Health                       0.647
		STEM.Physics                                 0.177
		STEM.STEM*                                   0.705
		STEM.Space                                   0.797
		STEM.Technology                              0.25
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
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
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.986
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
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
	f1 (micro=0.731, macro=0.606):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.551
		Culture.Food and drink                       0.504
		Culture.Internet culture                     0.515
		Culture.Linguistics                          0.768
		Culture.Literature                           0.621
		Culture.Media.Books                          0.598
		Culture.Media.Entertainment                  0.403
		Culture.Media.Films                          0.743
		Culture.Media.Media*                         0.717
		Culture.Media.Music                          0.822
		Culture.Media.Radio                          0.7
		Culture.Media.Software                       0.252
		Culture.Media.Television                     0.658
		Culture.Media.Video games                    0.775
		Culture.Performing arts                      0.53
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.63
		Culture.Visual arts.Fashion                  0.457
		Culture.Visual arts.Visual arts*             0.669
		Geography.Geographical                       0.617
		Geography.Regions.Africa.Africa*             0.517
		Geography.Regions.Africa.Central Africa      0.242
		Geography.Regions.Africa.Eastern Africa      0.305
		Geography.Regions.Africa.Northern Africa     0.477
		Geography.Regions.Africa.Southern Africa     0.513
		Geography.Regions.Africa.Western Africa      0.511
		Geography.Regions.Americas.Central America   0.503
		Geography.Regions.Americas.North America     0.716
		Geography.Regions.Americas.South America     0.654
		Geography.Regions.Asia.Asia*                 0.715
		Geography.Regions.Asia.Central Asia          0.408
		Geography.Regions.Asia.East Asia             0.622
		Geography.Regions.Asia.North Asia            0.599
		Geography.Regions.Asia.South Asia            0.823
		Geography.Regions.Asia.Southeast Asia        0.595
		Geography.Regions.Asia.West Asia             0.808
		Geography.Regions.Europe.Eastern Europe      0.758
		Geography.Regions.Europe.Europe*             0.758
		Geography.Regions.Europe.Northern Europe     0.677
		Geography.Regions.Europe.Southern Europe     0.754
		Geography.Regions.Europe.Western Europe      0.76
		Geography.Regions.Oceania                    0.755
		History and Society.Business and economics   0.496
		History and Society.Education                0.589
		History and Society.History                  0.416
		History and Society.Military and warfare     0.657
		History and Society.Politics and government  0.563
		History and Society.Society                  0.349
		History and Society.Transportation           0.895
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.408
		STEM.Computing                               0.398
		STEM.Earth and environment                   0.58
		STEM.Engineering                             0.726
		STEM.Libraries & Information                 0.513
		STEM.Mathematics                             0.358
		STEM.Medicine & Health                       0.655
		STEM.Physics                                 0.28
		STEM.STEM*                                   0.792
		STEM.Space                                   0.838
		STEM.Technology                              0.368
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.98
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
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.98, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.978
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.02
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.025
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.009
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.026
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.005
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.009
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.974
		Culture.Literature                           0.975
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.962
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.953
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.949
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.975
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.963
		Geography.Regions.Africa.Africa*             0.973
		Geography.Regions.Africa.Central Africa      0.98
		Geography.Regions.Africa.Eastern Africa      0.957
		Geography.Regions.Africa.Northern Africa     0.976
		Geography.Regions.Africa.Southern Africa     0.969
		Geography.Regions.Africa.Western Africa      0.985
		Geography.Regions.Americas.Central America   0.969
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.979
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.978
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.97
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.974
		Geography.Regions.Asia.West Asia             0.978
		Geography.Regions.Europe.Eastern Europe      0.972
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.974
		History and Society.Business and economics   0.961
		History and Society.Education                0.969
		History and Society.History                  0.946
		History and Society.Military and warfare     0.974
		History and Society.Politics and government  0.944
		History and Society.Society                  0.918
		History and Society.Transportation           0.986
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.985
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.969
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.98
		STEM.Space                                   0.988
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.777, macro=0.607):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.927
		Culture.Biography.Women                      0.533
		Culture.Food and drink                       0.519
		Culture.Internet culture                     0.621
		Culture.Linguistics                          0.774
		Culture.Literature                           0.686
		Culture.Media.Books                          0.543
		Culture.Media.Entertainment                  0.344
		Culture.Media.Films                          0.778
		Culture.Media.Media*                         0.809
		Culture.Media.Music                          0.845
		Culture.Media.Radio                          0.555
		Culture.Media.Software                       0.233
		Culture.Media.Television                     0.637
		Culture.Media.Video games                    0.866
		Culture.Performing arts                      0.497
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.643
		Culture.Visual arts.Fashion                  0.366
		Culture.Visual arts.Visual arts*             0.719
		Geography.Geographical                       0.62
		Geography.Regions.Africa.Africa*             0.548
		Geography.Regions.Africa.Central Africa      0.194
		Geography.Regions.Africa.Eastern Africa      0.133
		Geography.Regions.Africa.Northern Africa     0.379
		Geography.Regions.Africa.Southern Africa     0.399
		Geography.Regions.Africa.Western Africa      0.35
		Geography.Regions.Americas.Central America   0.481
		Geography.Regions.Americas.North America     0.792
		Geography.Regions.Americas.South America     0.602
		Geography.Regions.Asia.Asia*                 0.791
		Geography.Regions.Asia.Central Asia          0.355
		Geography.Regions.Asia.East Asia             0.606
		Geography.Regions.Asia.North Asia            0.6
		Geography.Regions.Asia.South Asia            0.855
		Geography.Regions.Asia.Southeast Asia        0.602
		Geography.Regions.Asia.West Asia             0.844
		Geography.Regions.Europe.Eastern Europe      0.799
		Geography.Regions.Europe.Europe*             0.836
		Geography.Regions.Europe.Northern Europe     0.735
		Geography.Regions.Europe.Southern Europe     0.809
		Geography.Regions.Europe.Western Europe      0.817
		Geography.Regions.Oceania                    0.783
		History and Society.Business and economics   0.473
		History and Society.Education                0.582
		History and Society.History                  0.366
		History and Society.Military and warfare     0.722
		History and Society.Politics and government  0.603
		History and Society.Society                  0.314
		History and Society.Transportation           0.922
		STEM.Biology                                 0.954
		STEM.Chemistry                               0.393
		STEM.Computing                               0.374
		STEM.Earth and environment                   0.546
		STEM.Engineering                             0.774
		STEM.Libraries & Information                 0.406
		STEM.Mathematics                             0.427
		STEM.Medicine & Health                       0.673
		STEM.Physics                                 0.221
		STEM.STEM*                                   0.911
		STEM.Space                                   0.9
		STEM.Technology                              0.385
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Culture.Performing arts': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

