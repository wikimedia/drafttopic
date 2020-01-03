Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'presort': 'auto', 'learning_rate': 0.1, 'loss': 'deviance', 'warm_start': False, 'verbose': 0, 'max_features': 'log2', 'criterion': 'friedman_mse', 'init': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'label_weights': {}, 'n_estimators': 150, 'scale': False, 'max_depth': 5, 'population_rates': None, 'n_iter_no_change': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'center': False, 'random_state': None, 'max_leaf_nodes': None, 'multilabel': True, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'min_impurity_split': None, 'min_impurity_decrease': 0.0}
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
			'Culture.Biography.Biography*'                 16717  -->  13838  2879  1595  44705
			'Culture.Biography.Women'                       4173  -->    851  3322   534  58310
			'Culture.Food and drink'                        1323  -->    824   499   109  61585
			'Culture.Internet culture'                      2946  -->   1966   980   246  59825
			'Culture.Linguistics'                           1384  -->    907   477   112  61521
			'Culture.Literature'                            5277  -->   3375  1902   740  57000
			'Culture.Media.Books'                           1919  -->   1159   760   262  60836
			'Culture.Media.Entertainment'                   1876  -->    392  1484   119  61022
			'Culture.Media.Films'                           2307  -->   1704   603   195  60515
			'Culture.Media.Media*'                         14363  -->  11373  2990  2193  46461
			'Culture.Media.Music'                           2677  -->   2017   660   335  60005
			'Culture.Media.Radio'                           1174  -->    866   308    77  61766
			'Culture.Media.Software'                        1798  -->    826   972   437  60782
			'Culture.Media.Television'                      2200  -->   1085  1115   252  60565
			'Culture.Media.Video games'                     2078  -->   1690   388    67  60872
			'Culture.Performing arts'                       1334  -->    556   778   148  61535
			'Culture.Philosophy and religion'               2638  -->    877  1761   296  60083
			'Culture.Sports'                                5843  -->   5091   752   467  56707
			'Culture.Visual arts.Architecture'              2565  -->   1627   938   388  60064
			'Culture.Visual arts.Comics and Anime'          1488  -->    760   728   133  61396
			'Culture.Visual arts.Fashion'                   1188  -->    521   667    80  61749
			'Culture.Visual arts.Visual arts*'              5987  -->   2981  3006   662  56368
			'Geography.Geographical'                        3344  -->   1772  1572   335  59338
			'Geography.Regions.Africa.Africa*'              5693  -->    716  4977   303  57021
			'Geography.Regions.Africa.Central Africa'         28  -->      0    28    64  62925
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    126   988    69  61834
			'Geography.Regions.Africa.Northern Africa'      1266  -->    101  1165   112  61639
			'Geography.Regions.Africa.Southern Africa'      1288  -->    173  1115    85  61644
			'Geography.Regions.Africa.Western Africa'       1152  -->    104  1048    79  61786
			'Geography.Regions.Americas.Central America'    1326  -->     45  1281   115  61576
			'Geography.Regions.Americas.North America'      7565  -->   2422  5143   603  54849
			'Geography.Regions.Americas.South America'      1523  -->    234  1289   172  61322
			'Geography.Regions.Asia.Asia*'                 11060  -->   3240  7820   837  51120
			'Geography.Regions.Asia.Central Asia'           1163  -->    137  1026    63  61791
			'Geography.Regions.Asia.East Asia'              2721  -->    474  2247   146  60150
			'Geography.Regions.Asia.North Asia'             1361  -->    163  1198   104  61552
			'Geography.Regions.Asia.South Asia'             2438  -->    294  2144    80  60499
			'Geography.Regions.Asia.Southeast Asia'         1688  -->     36  1652    69  61260
			'Geography.Regions.Asia.West Asia'              2264  -->    904  1360   100  60653
			'Geography.Regions.Europe.Eastern Europe'       3083  -->    597  2486   136  59798
			'Geography.Regions.Europe.Europe*'             12415  -->   3448  8967  1336  49266
			'Geography.Regions.Europe.Northern Europe'      4244  -->    460  3784   153  58620
			'Geography.Regions.Europe.Southern Europe'      2320  -->    269  2051   128  60569
			'Geography.Regions.Europe.Western Europe'       3160  -->    709  2451   293  59564
			'Geography.Regions.Oceania'                     2537  -->    204  2333    74  60406
			'History and Society.Business and economics'    3430  -->   1381  2049   564  59023
			'History and Society.Education'                 2178  -->    914  1264   228  60611
			'History and Society.History'                   3217  -->    555  2662   348  59452
			'History and Society.Military and warfare'      3977  -->   2003  1974   396  58644
			'History and Society.Politics and government'   4647  -->   1138  3509   457  57913
			'History and Society.Society'                   4057  -->    429  3628   116  58844
			'History and Society.Transportation'            3604  -->   2757   847   337  59076
			'STEM.Biology'                                  2834  -->   2133   701   198  59985
			'STEM.Chemistry'                                1344  -->    827   517   228  61445
			'STEM.Computing'                                2011  -->   1112   899   451  60555
			'STEM.Earth and environment'                    1683  -->    827   856   166  61168
			'STEM.Engineering'                              2272  -->   1235  1037   206  60539
			'STEM.Libraries & Information'                  1159  -->    363   796   111  61747
			'STEM.Mathematics'                              1121  -->    567   554   169  61727
			'STEM.Medicine & Health'                        1737  -->    952   785   201  61079
			'STEM.Physics'                                  1206  -->    603   603   213  61598
			'STEM.STEM*'                                   16499  -->  13051  3448  1513  45005
			'STEM.Space'                                    1398  -->    987   411    89  61530
			'STEM.Technology'                               3712  -->   1758  1954   797  58508
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
	match_rate (micro=0.045, macro=0.014):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.012
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.023
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.089
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.031
		Geography.Regions.Americas.South America     0.004
		Geography.Regions.Asia.Asia*                 0.029
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.003
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.006
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.046
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.008
		History and Society.Military and warfare     0.014
		History and Society.Politics and government  0.015
		History and Society.Society                  0.003
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.005
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.003
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.955, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.977
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.911
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.992
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.985
		History and Society.Society                  0.997
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.995
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.997
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.518, macro=0.409):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.828
		Culture.Biography.Women                      0.204
		Culture.Food and drink                       0.623
		Culture.Internet culture                     0.667
		Culture.Linguistics                          0.655
		Culture.Literature                           0.64
		Culture.Media.Books                          0.604
		Culture.Media.Entertainment                  0.209
		Culture.Media.Films                          0.739
		Culture.Media.Media*                         0.792
		Culture.Media.Music                          0.753
		Culture.Media.Radio                          0.738
		Culture.Media.Software                       0.459
		Culture.Media.Television                     0.493
		Culture.Media.Video games                    0.813
		Culture.Performing arts                      0.417
		Culture.Philosophy and religion              0.332
		Culture.Sports                               0.871
		Culture.Visual arts.Architecture             0.634
		Culture.Visual arts.Comics and Anime         0.511
		Culture.Visual arts.Fashion                  0.439
		Culture.Visual arts.Visual arts*             0.498
		Geography.Geographical                       0.53
		Geography.Regions.Africa.Africa*             0.126
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.113
		Geography.Regions.Africa.Northern Africa     0.08
		Geography.Regions.Africa.Southern Africa     0.134
		Geography.Regions.Africa.Western Africa      0.09
		Geography.Regions.Americas.Central America   0.034
		Geography.Regions.Americas.North America     0.32
		Geography.Regions.Americas.South America     0.154
		Geography.Regions.Asia.Asia*                 0.293
		Geography.Regions.Asia.Central Asia          0.118
		Geography.Regions.Asia.East Asia             0.174
		Geography.Regions.Asia.North Asia            0.12
		Geography.Regions.Asia.South Asia            0.121
		Geography.Regions.Asia.Southeast Asia        0.021
		Geography.Regions.Asia.West Asia             0.399
		Geography.Regions.Europe.Eastern Europe      0.194
		Geography.Regions.Europe.Europe*             0.278
		Geography.Regions.Europe.Northern Europe     0.108
		Geography.Regions.Europe.Southern Europe     0.116
		Geography.Regions.Europe.Western Europe      0.224
		Geography.Regions.Oceania                    0.08
		History and Society.Business and economics   0.403
		History and Society.Education                0.42
		History and Society.History                  0.173
		History and Society.Military and warfare     0.504
		History and Society.Politics and government  0.245
		History and Society.Society                  0.106
		History and Society.Transportation           0.765
		STEM.Biology                                 0.753
		STEM.Chemistry                               0.615
		STEM.Computing                               0.553
		STEM.Earth and environment                   0.491
		STEM.Engineering                             0.544
		STEM.Libraries & Information                 0.313
		STEM.Mathematics                             0.506
		STEM.Medicine & Health                       0.548
		STEM.Physics                                 0.5
		STEM.STEM*                                   0.791
		STEM.Space                                   0.706
		STEM.Technology                              0.474
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.955
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.998
		History and Society.Transportation           0.994
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.997
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.585, macro=0.402):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.771
		Culture.Biography.Women                      0.249
		Culture.Food and drink                       0.465
		Culture.Internet culture                     0.364
		Culture.Linguistics                          0.727
		Culture.Literature                           0.44
		Culture.Media.Books                          0.363
		Culture.Media.Entertainment                  0.279
		Culture.Media.Films                          0.71
		Culture.Media.Media*                         0.522
		Culture.Media.Music                          0.769
		Culture.Media.Radio                          0.561
		Culture.Media.Software                       0.079
		Culture.Media.Television                     0.514
		Culture.Media.Video games                    0.66
		Culture.Performing arts                      0.335
		Culture.Philosophy and religion              0.422
		Culture.Sports                               0.891
		Culture.Visual arts.Architecture             0.514
		Culture.Visual arts.Comics and Anime         0.342
		Culture.Visual arts.Fashion                  0.215
		Culture.Visual arts.Visual arts*             0.444
		Geography.Geographical                       0.695
		Geography.Regions.Africa.Africa*             0.158
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.044
		Geography.Regions.Africa.Northern Africa     0.051
		Geography.Regions.Africa.Southern Africa     0.103
		Geography.Regions.Africa.Western Africa      0.046
		Geography.Regions.Americas.Central America   0.057
		Geography.Regions.Americas.North America     0.669
		Geography.Regions.Americas.South America     0.259
		Geography.Regions.Asia.Asia*                 0.464
		Geography.Regions.Asia.Central Asia          0.091
		Geography.Regions.Asia.East Asia             0.454
		Geography.Regions.Asia.North Asia            0.062
		Geography.Regions.Asia.South Asia            0.585
		Geography.Regions.Asia.Southeast Asia        0.103
		Geography.Regions.Asia.West Asia             0.728
		Geography.Regions.Europe.Eastern Europe      0.526
		Geography.Regions.Europe.Europe*             0.465
		Geography.Regions.Europe.Northern Europe     0.568
		Geography.Regions.Europe.Southern Europe     0.421
		Geography.Regions.Europe.Western Europe      0.473
		Geography.Regions.Oceania                    0.502
		History and Society.Business and economics   0.303
		History and Society.Education                0.454
		History and Society.History                  0.245
		History and Society.Military and warfare     0.517
		History and Society.Politics and government  0.476
		History and Society.Society                  0.407
		History and Society.Transportation           0.674
		STEM.Biology                                 0.888
		STEM.Chemistry                               0.206
		STEM.Computing                               0.168
		STEM.Earth and environment                   0.453
		STEM.Engineering                             0.458
		STEM.Libraries & Information                 0.098
		STEM.Mathematics                             0.072
		STEM.Medicine & Health                       0.518
		STEM.Physics                                 0.11
		STEM.STEM*                                   0.644
		STEM.Space                                   0.748
		STEM.Technology                              0.154
		-------------------------------------------  -----
	!precision (micro=0.981, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.987
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.978
		History and Society.Society                  0.989
		History and Society.Transportation           0.996
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.984
		STEM.Space                                   0.998
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.799
		Culture.Biography.Women                      0.224
		Culture.Food and drink                       0.533
		Culture.Internet culture                     0.471
		Culture.Linguistics                          0.689
		Culture.Literature                           0.521
		Culture.Media.Books                          0.453
		Culture.Media.Entertainment                  0.239
		Culture.Media.Films                          0.724
		Culture.Media.Media*                         0.629
		Culture.Media.Music                          0.761
		Culture.Media.Radio                          0.638
		Culture.Media.Software                       0.135
		Culture.Media.Television                     0.504
		Culture.Media.Video games                    0.728
		Culture.Performing arts                      0.371
		Culture.Philosophy and religion              0.372
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.568
		Culture.Visual arts.Comics and Anime         0.41
		Culture.Visual arts.Fashion                  0.289
		Culture.Visual arts.Visual arts*             0.47
		Geography.Geographical                       0.601
		Geography.Regions.Africa.Africa*             0.14
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.064
		Geography.Regions.Africa.Northern Africa     0.062
		Geography.Regions.Africa.Southern Africa     0.117
		Geography.Regions.Africa.Western Africa      0.061
		Geography.Regions.Americas.Central America   0.043
		Geography.Regions.Americas.North America     0.433
		Geography.Regions.Americas.South America     0.193
		Geography.Regions.Asia.Asia*                 0.359
		Geography.Regions.Asia.Central Asia          0.103
		Geography.Regions.Asia.East Asia             0.252
		Geography.Regions.Asia.North Asia            0.081
		Geography.Regions.Asia.South Asia            0.2
		Geography.Regions.Asia.Southeast Asia        0.035
		Geography.Regions.Asia.West Asia             0.516
		Geography.Regions.Europe.Eastern Europe      0.283
		Geography.Regions.Europe.Europe*             0.348
		Geography.Regions.Europe.Northern Europe     0.182
		Geography.Regions.Europe.Southern Europe     0.182
		Geography.Regions.Europe.Western Europe      0.304
		Geography.Regions.Oceania                    0.139
		History and Society.Business and economics   0.345
		History and Society.Education                0.436
		History and Society.History                  0.203
		History and Society.Military and warfare     0.51
		History and Society.Politics and government  0.323
		History and Society.Society                  0.168
		History and Society.Transportation           0.717
		STEM.Biology                                 0.815
		STEM.Chemistry                               0.309
		STEM.Computing                               0.258
		STEM.Earth and environment                   0.471
		STEM.Engineering                             0.497
		STEM.Libraries & Information                 0.149
		STEM.Mathematics                             0.126
		STEM.Medicine & Health                       0.533
		STEM.Physics                                 0.18
		STEM.STEM*                                   0.71
		STEM.Space                                   0.726
		STEM.Technology                              0.232
		-------------------------------------------  -----
	!f1 (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.972
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.985
		History and Society.Society                  0.993
		History and Society.Transportation           0.995
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.976
		STEM.Space                                   0.998
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.968, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.949
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.945
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.952
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.921
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.971
		History and Society.Society                  0.987
		History and Society.Transportation           0.991
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.997
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.955
		STEM.Space                                   0.997
		STEM.Technology                              0.984
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.034
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.013
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.045
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.008
		Culture.Visual arts.Architecture             0.006
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.012
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.002
		Geography.Regions.Europe.Europe*             0.026
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.005
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.002
		History and Society.Transportation           0.006
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.003
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.033
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.921, macro=0.919):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.924
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.958
		Culture.Literature                           0.965
		Culture.Media.Books                          0.973
		Culture.Media.Entertainment                  0.939
		Culture.Media.Films                          0.977
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.98
		Culture.Media.Software                       0.972
		Culture.Media.Television                     0.964
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.933
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.975
		Culture.Visual arts.Comics and Anime         0.974
		Culture.Visual arts.Fashion                  0.968
		Culture.Visual arts.Visual arts*             0.947
		Geography.Geographical                       0.954
		Geography.Regions.Africa.Africa*             0.843
		Geography.Regions.Africa.Central Africa      0.498
		Geography.Regions.Africa.Eastern Africa      0.872
		Geography.Regions.Africa.Northern Africa     0.862
		Geography.Regions.Africa.Southern Africa     0.842
		Geography.Regions.Africa.Western Africa      0.886
		Geography.Regions.Americas.Central America   0.834
		Geography.Regions.Americas.North America     0.877
		Geography.Regions.Americas.South America     0.899
		Geography.Regions.Asia.Asia*                 0.85
		Geography.Regions.Asia.Central Asia          0.886
		Geography.Regions.Asia.East Asia             0.86
		Geography.Regions.Asia.North Asia            0.911
		Geography.Regions.Asia.South Asia            0.865
		Geography.Regions.Asia.Southeast Asia        0.79
		Geography.Regions.Asia.West Asia             0.886
		Geography.Regions.Europe.Eastern Europe      0.889
		Geography.Regions.Europe.Europe*             0.832
		Geography.Regions.Europe.Northern Europe     0.828
		Geography.Regions.Europe.Southern Europe     0.862
		Geography.Regions.Europe.Western Europe      0.888
		Geography.Regions.Oceania                    0.841
		History and Society.Business and economics   0.943
		History and Society.Education                0.95
		History and Society.History                  0.897
		History and Society.Military and warfare     0.941
		History and Society.Politics and government  0.871
		History and Society.Society                  0.821
		History and Society.Transportation           0.979
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.981
		STEM.Computing                               0.977
		STEM.Earth and environment                   0.961
		STEM.Engineering                             0.963
		STEM.Libraries & Information                 0.946
		STEM.Mathematics                             0.969
		STEM.Medicine & Health                       0.966
		STEM.Physics                                 0.976
		STEM.STEM*                                   0.959
		STEM.Space                                   0.981
		STEM.Technology                              0.951
		-------------------------------------------  -----
	pr_auc (micro=0.545, macro=0.351):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.859
		Culture.Biography.Women                      0.175
		Culture.Food and drink                       0.558
		Culture.Internet culture                     0.554
		Culture.Linguistics                          0.616
		Culture.Literature                           0.536
		Culture.Media.Books                          0.371
		Culture.Media.Entertainment                  0.16
		Culture.Media.Films                          0.707
		Culture.Media.Media*                         0.727
		Culture.Media.Music                          0.807
		Culture.Media.Radio                          0.7
		Culture.Media.Software                       0.069
		Culture.Media.Television                     0.454
		Culture.Media.Video games                    0.829
		Culture.Performing arts                      0.279
		Culture.Philosophy and religion              0.275
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.585
		Culture.Visual arts.Comics and Anime         0.341
		Culture.Visual arts.Fashion                  0.173
		Culture.Visual arts.Visual arts*             0.439
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.075
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.017
		Geography.Regions.Africa.Northern Africa     0.017
		Geography.Regions.Africa.Southern Africa     0.03
		Geography.Regions.Africa.Western Africa      0.014
		Geography.Regions.Americas.Central America   0.034
		Geography.Regions.Americas.North America     0.487
		Geography.Regions.Americas.South America     0.129
		Geography.Regions.Asia.Asia*                 0.369
		Geography.Regions.Asia.Central Asia          0.028
		Geography.Regions.Asia.East Asia             0.219
		Geography.Regions.Asia.North Asia            0.025
		Geography.Regions.Asia.South Asia            0.235
		Geography.Regions.Asia.Southeast Asia        0.031
		Geography.Regions.Asia.West Asia             0.467
		Geography.Regions.Europe.Eastern Europe      0.285
		Geography.Regions.Europe.Europe*             0.378
		Geography.Regions.Europe.Northern Europe     0.234
		Geography.Regions.Europe.Southern Europe     0.165
		Geography.Regions.Europe.Western Europe      0.288
		Geography.Regions.Oceania                    0.162
		History and Society.Business and economics   0.246
		History and Society.Education                0.346
		History and Society.History                  0.134
		History and Society.Military and warfare     0.496
		History and Society.Politics and government  0.317
		History and Society.Society                  0.15
		History and Society.Transportation           0.739
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.277
		STEM.Computing                               0.173
		STEM.Earth and environment                   0.39
		STEM.Engineering                             0.486
		STEM.Libraries & Information                 0.069
		STEM.Mathematics                             0.066
		STEM.Medicine & Health                       0.47
		STEM.Physics                                 0.12
		STEM.STEM*                                   0.804
		STEM.Space                                   0.771
		STEM.Technology                              0.148
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}}, 'title': 'Scikit learn-based classifier score with probability'}

