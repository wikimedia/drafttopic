Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.8'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2 (2021-01-30)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul 25 2020 13:03:44')
	 - python_compiler: 'GCC 8.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.7.3'
	 - release: '4.19.0-14-amd64'
	
	Statistics:
	counts (n=60905):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16147  -->  13460  2687  1471  43287
			'Culture.Biography.Women'                       4041  -->   2720  1321   800  56064
			'Culture.Food and drink'                        1222  -->    716   506    86  59597
			'Culture.Internet culture'                      2732  -->   1895   837   232  57941
			'Culture.Linguistics'                           1169  -->    786   383   122  59614
			'Culture.Literature'                            5001  -->   3325  1676   518  55386
			'Culture.Media.Books'                           1792  -->   1123   669   253  58860
			'Culture.Media.Entertainment'                   1691  -->    677  1014   177  59037
			'Culture.Media.Films'                           2259  -->   1709   550   188  58458
			'Culture.Media.Media*'                         13536  -->  10960  2576  1602  45767
			'Culture.Media.Music'                           2502  -->   1818   684   277  58126
			'Culture.Media.Radio'                           1126  -->    845   281    42  59737
			'Culture.Media.Software'                        1652  -->    784   868   332  58921
			'Culture.Media.Television'                      2029  -->   1322   707   192  58684
			'Culture.Media.Video games'                     1940  -->   1591   349    66  58899
			'Culture.Performing arts'                       1257  -->    713   544   127  59521
			'Culture.Philosophy and religion'               2583  -->   1250  1333   335  57987
			'Culture.Sports'                                5799  -->   5078   721   312  54794
			'Culture.Visual arts.Architecture'              2497  -->   1690   807   280  58128
			'Culture.Visual arts.Comics and Anime'          1399  -->   1014   385    98  59408
			'Culture.Visual arts.Fashion'                   1110  -->    668   442    65  59730
			'Culture.Visual arts.Visual arts*'              5713  -->   3913  1800   561  54631
			'Geography.Geographical'                        3399  -->   2131  1268   261  57245
			'Geography.Regions.Africa.Africa*'              6314  -->   5239  1075   356  54235
			'Geography.Regions.Africa.Central Africa'       1134  -->    821   313    47  59724
			'Geography.Regions.Africa.Eastern Africa'       1074  -->    812   262    40  59791
			'Geography.Regions.Africa.Northern Africa'      1259  -->    896   363   100  59546
			'Geography.Regions.Africa.Southern Africa'      1237  -->    895   342    62  59606
			'Geography.Regions.Africa.Western Africa'       1120  -->    885   235    66  59719
			'Geography.Regions.Americas.Central America'    1269  -->    822   447   101  59535
			'Geography.Regions.Americas.North America'      7174  -->   4516  2658  1136  52595
			'Geography.Regions.Americas.South America'      1531  -->   1086   445   120  59254
			'Geography.Regions.Asia.Asia*'                 10799  -->   8748  2051   864  49242
			'Geography.Regions.Asia.Central Asia'           1097  -->    778   319    51  59757
			'Geography.Regions.Asia.East Asia'              2642  -->   1830   812   291  57972
			'Geography.Regions.Asia.North Asia'             1321  -->    820   501   178  59406
			'Geography.Regions.Asia.South Asia'             2354  -->   1880   474   128  58423
			'Geography.Regions.Asia.Southeast Asia'         1653  -->   1176   477   114  59138
			'Geography.Regions.Asia.West Asia'              2204  -->   1697   507   153  58548
			'Geography.Regions.Europe.Eastern Europe'       3005  -->   2248   757   287  57613
			'Geography.Regions.Europe.Europe*'             11882  -->   8695  3187  1664  47359
			'Geography.Regions.Europe.Northern Europe'      3947  -->   2507  1440   586  56372
			'Geography.Regions.Europe.Southern Europe'      2321  -->   1544   777   296  58288
			'Geography.Regions.Europe.Western Europe'       2971  -->   1875  1096   463  57471
			'Geography.Regions.Oceania'                     2463  -->   1888   575   148  58294
			'History and Society.Business and economics'    3254  -->   1324  1930   505  57146
			'History and Society.Education'                 2112  -->    875  1237   257  58536
			'History and Society.History'                   3155  -->   1056  2099   451  57299
			'History and Society.Military and warfare'      3889  -->   2505  1384   391  56625
			'History and Society.Politics and government'   4429  -->   2468  1961   460  56016
			'History and Society.Society'                   3807  -->   1322  2485   345  56753
			'History and Society.Transportation'            3425  -->   2781   644   238  57242
			'STEM.Biology'                                  2829  -->   2211   618   129  57947
			'STEM.Chemistry'                                1222  -->    737   485   141  59542
			'STEM.Computing'                                1966  -->   1122   844   373  58566
			'STEM.Earth and environment'                    1552  -->   1013   539   129  59224
			'STEM.Engineering'                              2242  -->   1508   734   195  58468
			'STEM.Libraries & Information'                  1120  -->    548   572   102  59683
			'STEM.Mathematics'                              1057  -->    585   472    85  59763
			'STEM.Medicine & Health'                        1640  -->    909   731   199  59066
			'STEM.Physics'                                  1112  -->    571   541   136  59657
			'STEM.STEM*'                                   15719  -->  13088  2631  1200  43986
			'STEM.Space'                                    1343  -->   1119   224    67  59495
			'STEM.Technology'                               3435  -->   1818  1617   591  56879
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.265         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.045         0.003
		Culture.Linguistics                             0.019         0.007
		Culture.Literature                              0.082         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.222         0.058
		Culture.Media.Music                             0.041         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.104         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.118         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.177         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.195         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.049         0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.037         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.018         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.052, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.06
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.087
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.011
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.024
		History and Society.Society                  0.01
		History and Society.Transportation           0.016
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.94
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.913
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.976
		History and Society.Society                  0.99
		History and Society.Transportation           0.984
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.726, macro=0.661):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.834
		Culture.Biography.Women                      0.673
		Culture.Food and drink                       0.586
		Culture.Internet culture                     0.694
		Culture.Linguistics                          0.672
		Culture.Literature                           0.665
		Culture.Media.Books                          0.627
		Culture.Media.Entertainment                  0.4
		Culture.Media.Films                          0.757
		Culture.Media.Media*                         0.81
		Culture.Media.Music                          0.727
		Culture.Media.Radio                          0.75
		Culture.Media.Software                       0.475
		Culture.Media.Television                     0.652
		Culture.Media.Video games                    0.82
		Culture.Performing arts                      0.567
		Culture.Philosophy and religion              0.484
		Culture.Sports                               0.876
		Culture.Visual arts.Architecture             0.677
		Culture.Visual arts.Comics and Anime         0.725
		Culture.Visual arts.Fashion                  0.602
		Culture.Visual arts.Visual arts*             0.685
		Geography.Geographical                       0.627
		Geography.Regions.Africa.Africa*             0.83
		Geography.Regions.Africa.Central Africa      0.724
		Geography.Regions.Africa.Eastern Africa      0.756
		Geography.Regions.Africa.Northern Africa     0.712
		Geography.Regions.Africa.Southern Africa     0.724
		Geography.Regions.Africa.Western Africa      0.79
		Geography.Regions.Americas.Central America   0.648
		Geography.Regions.Americas.North America     0.629
		Geography.Regions.Americas.South America     0.709
		Geography.Regions.Asia.Asia*                 0.81
		Geography.Regions.Asia.Central Asia          0.709
		Geography.Regions.Asia.East Asia             0.693
		Geography.Regions.Asia.North Asia            0.621
		Geography.Regions.Asia.South Asia            0.799
		Geography.Regions.Asia.Southeast Asia        0.711
		Geography.Regions.Asia.West Asia             0.77
		Geography.Regions.Europe.Eastern Europe      0.748
		Geography.Regions.Europe.Europe*             0.732
		Geography.Regions.Europe.Northern Europe     0.635
		Geography.Regions.Europe.Southern Europe     0.665
		Geography.Regions.Europe.Western Europe      0.631
		Geography.Regions.Oceania                    0.767
		History and Society.Business and economics   0.407
		History and Society.Education                0.414
		History and Society.History                  0.335
		History and Society.Military and warfare     0.644
		History and Society.Politics and government  0.557
		History and Society.Society                  0.347
		History and Society.Transportation           0.812
		STEM.Biology                                 0.782
		STEM.Chemistry                               0.603
		STEM.Computing                               0.571
		STEM.Earth and environment                   0.653
		STEM.Engineering                             0.673
		STEM.Libraries & Information                 0.489
		STEM.Mathematics                             0.553
		STEM.Medicine & Health                       0.554
		STEM.Physics                                 0.513
		STEM.STEM*                                   0.833
		STEM.Space                                   0.833
		STEM.Technology                              0.529
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.677, macro=0.53):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.781
		Culture.Biography.Women                      0.414
		Culture.Food and drink                       0.501
		Culture.Internet culture                     0.379
		Culture.Linguistics                          0.708
		Culture.Literature                           0.53
		Culture.Media.Books                          0.372
		Culture.Media.Entertainment                  0.325
		Culture.Media.Films                          0.715
		Culture.Media.Media*                         0.598
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.698
		Culture.Media.Software                       0.101
		Culture.Media.Television                     0.64
		Culture.Media.Video games                    0.657
		Culture.Performing arts                      0.435
		Culture.Philosophy and religion              0.476
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.601
		Culture.Visual arts.Comics and Anime         0.492
		Culture.Visual arts.Fashion                  0.309
		Culture.Visual arts.Visual arts*             0.557
		Geography.Geographical                       0.769
		Geography.Regions.Africa.Africa*             0.5
		Geography.Regions.Africa.Central Africa      0.368
		Geography.Regions.Africa.Eastern Africa      0.34
		Geography.Regions.Africa.Northern Africa     0.343
		Geography.Regions.Africa.Southern Africa     0.45
		Geography.Regions.Africa.Western Africa      0.329
		Geography.Regions.Americas.Central America   0.559
		Geography.Regions.Americas.North America     0.672
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.691
		Geography.Regions.Asia.Central Asia          0.419
		Geography.Regions.Asia.East Asia             0.615
		Geography.Regions.Asia.North Asia            0.161
		Geography.Regions.Asia.South Asia            0.849
		Geography.Regions.Asia.Southeast Asia        0.691
		Geography.Regions.Asia.West Asia             0.765
		Geography.Regions.Europe.Eastern Europe      0.662
		Geography.Regions.Europe.Europe*             0.64
		Geography.Regions.Europe.Northern Europe     0.661
		Geography.Regions.Europe.Southern Europe     0.635
		Geography.Regions.Europe.Western Europe      0.607
		Geography.Regions.Oceania                    0.823
		History and Society.Business and economics   0.321
		History and Society.Education                0.413
		History and Society.History                  0.319
		History and Society.Military and warfare     0.573
		History and Society.Politics and government  0.665
		History and Society.Society                  0.423
		History and Society.Transportation           0.75
		STEM.Biology                                 0.924
		STEM.Chemistry                               0.285
		STEM.Computing                               0.196
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.516
		STEM.Libraries & Information                 0.151
		STEM.Mathematics                             0.14
		STEM.Medicine & Health                       0.515
		STEM.Physics                                 0.161
		STEM.STEM*                                   0.7
		STEM.Space                                   0.818
		STEM.Technology                              0.21
		-------------------------------------------  -----
	!precision (micro=0.988, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.988
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
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
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.695, macro=0.572):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.806
		Culture.Biography.Women                      0.513
		Culture.Food and drink                       0.54
		Culture.Internet culture                     0.49
		Culture.Linguistics                          0.69
		Culture.Literature                           0.59
		Culture.Media.Books                          0.467
		Culture.Media.Entertainment                  0.359
		Culture.Media.Films                          0.735
		Culture.Media.Media*                         0.688
		Culture.Media.Music                          0.757
		Culture.Media.Radio                          0.723
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.646
		Culture.Media.Video games                    0.73
		Culture.Performing arts                      0.493
		Culture.Philosophy and religion              0.48
		Culture.Sports                               0.898
		Culture.Visual arts.Architecture             0.637
		Culture.Visual arts.Comics and Anime         0.586
		Culture.Visual arts.Fashion                  0.409
		Culture.Visual arts.Visual arts*             0.614
		Geography.Geographical                       0.691
		Geography.Regions.Africa.Africa*             0.624
		Geography.Regions.Africa.Central Africa      0.488
		Geography.Regions.Africa.Eastern Africa      0.469
		Geography.Regions.Africa.Northern Africa     0.463
		Geography.Regions.Africa.Southern Africa     0.555
		Geography.Regions.Africa.Western Africa      0.464
		Geography.Regions.Americas.Central America   0.6
		Geography.Regions.Americas.North America     0.65
		Geography.Regions.Americas.South America     0.7
		Geography.Regions.Asia.Asia*                 0.746
		Geography.Regions.Asia.Central Asia          0.527
		Geography.Regions.Asia.East Asia             0.652
		Geography.Regions.Asia.North Asia            0.256
		Geography.Regions.Asia.South Asia            0.823
		Geography.Regions.Asia.Southeast Asia        0.701
		Geography.Regions.Asia.West Asia             0.768
		Geography.Regions.Europe.Eastern Europe      0.703
		Geography.Regions.Europe.Europe*             0.683
		Geography.Regions.Europe.Northern Europe     0.648
		Geography.Regions.Europe.Southern Europe     0.65
		Geography.Regions.Europe.Western Europe      0.619
		Geography.Regions.Oceania                    0.794
		History and Society.Business and economics   0.359
		History and Society.Education                0.413
		History and Society.History                  0.327
		History and Society.Military and warfare     0.606
		History and Society.Politics and government  0.606
		History and Society.Society                  0.382
		History and Society.Transportation           0.78
		STEM.Biology                                 0.847
		STEM.Chemistry                               0.387
		STEM.Computing                               0.291
		STEM.Earth and environment                   0.613
		STEM.Engineering                             0.584
		STEM.Libraries & Information                 0.231
		STEM.Mathematics                             0.223
		STEM.Medicine & Health                       0.534
		STEM.Physics                                 0.245
		STEM.STEM*                                   0.76
		STEM.Space                                   0.825
		STEM.Technology                              0.3
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
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
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
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
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.951
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.985
		History and Society.Education                0.991
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.98
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.964
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.033
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.967):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.967
		Culture.Food and drink                       0.969
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.96
		Culture.Literature                           0.965
		Culture.Media.Books                          0.973
		Culture.Media.Entertainment                  0.953
		Culture.Media.Films                          0.975
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.977
		Culture.Media.Software                       0.972
		Culture.Media.Television                     0.971
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.978
		Culture.Visual arts.Fashion                  0.972
		Culture.Visual arts.Visual arts*             0.961
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.97
		Geography.Regions.Africa.Southern Africa     0.977
		Geography.Regions.Africa.Western Africa      0.981
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.972
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.971
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.977
		Geography.Regions.Asia.Southeast Asia        0.968
		Geography.Regions.Asia.West Asia             0.974
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.96
		Geography.Regions.Europe.Southern Europe     0.969
		Geography.Regions.Europe.Western Europe      0.964
		Geography.Regions.Oceania                    0.974
		History and Society.Business and economics   0.94
		History and Society.Education                0.941
		History and Society.History                  0.925
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.943
		History and Society.Society                  0.897
		History and Society.Transportation           0.981
		STEM.Biology                                 0.974
		STEM.Chemistry                               0.976
		STEM.Computing                               0.974
		STEM.Earth and environment                   0.967
		STEM.Engineering                             0.97
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.968
		STEM.Medicine & Health                       0.968
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.969
		STEM.Space                                   0.982
		STEM.Technology                              0.958
		-------------------------------------------  -----
	pr_auc (micro=0.728, macro=0.566):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.475
		Culture.Food and drink                       0.489
		Culture.Internet culture                     0.595
		Culture.Linguistics                          0.626
		Culture.Literature                           0.625
		Culture.Media.Books                          0.445
		Culture.Media.Entertainment                  0.307
		Culture.Media.Films                          0.743
		Culture.Media.Media*                         0.768
		Culture.Media.Music                          0.793
		Culture.Media.Radio                          0.765
		Culture.Media.Software                       0.104
		Culture.Media.Television                     0.665
		Culture.Media.Video games                    0.8
		Culture.Performing arts                      0.448
		Culture.Philosophy and religion              0.419
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.688
		Culture.Visual arts.Comics and Anime         0.565
		Culture.Visual arts.Fashion                  0.375
		Culture.Visual arts.Visual arts*             0.656
		Geography.Geographical                       0.717
		Geography.Regions.Africa.Africa*             0.669
		Geography.Regions.Africa.Central Africa      0.477
		Geography.Regions.Africa.Eastern Africa      0.396
		Geography.Regions.Africa.Northern Africa     0.343
		Geography.Regions.Africa.Southern Africa     0.523
		Geography.Regions.Africa.Western Africa      0.367
		Geography.Regions.Americas.Central America   0.548
		Geography.Regions.Americas.North America     0.713
		Geography.Regions.Americas.South America     0.727
		Geography.Regions.Asia.Asia*                 0.79
		Geography.Regions.Asia.Central Asia          0.603
		Geography.Regions.Asia.East Asia             0.642
		Geography.Regions.Asia.North Asia            0.202
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.665
		Geography.Regions.Asia.West Asia             0.813
		Geography.Regions.Europe.Eastern Europe      0.705
		Geography.Regions.Europe.Europe*             0.738
		Geography.Regions.Europe.Northern Europe     0.662
		Geography.Regions.Europe.Southern Europe     0.635
		Geography.Regions.Europe.Western Europe      0.614
		Geography.Regions.Oceania                    0.798
		History and Society.Business and economics   0.285
		History and Society.Education                0.337
		History and Society.History                  0.249
		History and Society.Military and warfare     0.644
		History and Society.Politics and government  0.625
		History and Society.Society                  0.329
		History and Society.Transportation           0.825
		STEM.Biology                                 0.888
		STEM.Chemistry                               0.309
		STEM.Computing                               0.217
		STEM.Earth and environment                   0.584
		STEM.Engineering                             0.553
		STEM.Libraries & Information                 0.147
		STEM.Mathematics                             0.202
		STEM.Medicine & Health                       0.508
		STEM.Physics                                 0.239
		STEM.STEM*                                   0.851
		STEM.Space                                   0.859
		STEM.Technology                              0.252
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

