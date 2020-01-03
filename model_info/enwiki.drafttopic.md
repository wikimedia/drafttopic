Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'max_depth': 5, 'max_features': 'log2', 'tol': 0.0001, 'learning_rate': 0.1, 'verbose': 0, 'label_weights': {}, 'warm_start': False, 'min_samples_leaf': 1, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'subsample': 1.0, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'presort': 'auto', 'center': False, 'random_state': None, 'population_rates': None, 'validation_fraction': 0.1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'criterion': 'friedman_mse', 'n_estimators': 150, 'min_impurity_split': None, 'scale': False, 'min_samples_split': 2, 'multilabel': True, 'init': None}
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
	counts (n=60052):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16350  -->  12343  4007  1985  41717
			'Culture.Biography.Women'                       4056  -->   1135  2921   493  55503
			'Culture.Food and drink'                        1245  -->    781   464    89  58718
			'Culture.Internet culture'                      2681  -->   1739   942   212  57159
			'Culture.Linguistics'                           1210  -->    661   549   109  58733
			'Culture.Literature'                            4977  -->   2907  2070   631  54444
			'Culture.Media.Books'                           1810  -->    924   886   224  58018
			'Culture.Media.Entertainment'                   1737  -->    321  1416   107  58208
			'Culture.Media.Films'                           2225  -->   1536   689   219  57608
			'Culture.Media.Media*'                         13453  -->  10326  3127  1976  44623
			'Culture.Media.Music'                           2532  -->   1805   727   286  57234
			'Culture.Media.Radio'                           1116  -->    843   273    61  58875
			'Culture.Media.Software'                        1667  -->    772   895   366  58019
			'Culture.Media.Television'                      2008  -->   1053   955   272  57772
			'Culture.Media.Video games'                     1881  -->   1484   397    80  58091
			'Culture.Performing arts'                       1273  -->    619   654   128  58651
			'Culture.Philosophy and religion'               2505  -->   1110  1395   350  57197
			'Culture.Sports'                                5720  -->   4945   775   375  53957
			'Culture.Visual arts.Architecture'              2468  -->   1524   944   277  57307
			'Culture.Visual arts.Comics and Anime'          1384  -->    744   640   126  58542
			'Culture.Visual arts.Fashion'                   1118  -->    680   438    72  58862
			'Culture.Visual arts.Visual arts*'              5691  -->   3131  2560   526  53835
			'Geography.Geographical'                        3224  -->   1832  1392   285  56543
			'Geography.Regions.Africa.Africa*'              5529  -->   3867  1662   278  54245
			'Geography.Regions.Africa.Central Africa'         27  -->      0    27    59  59966
			'Geography.Regions.Africa.Eastern Africa'       1079  -->    612   467    51  58922
			'Geography.Regions.Africa.Northern Africa'      1228  -->    606   622    96  58728
			'Geography.Regions.Africa.Southern Africa'      1244  -->    728   516    56  58752
			'Geography.Regions.Africa.Western Africa'       1131  -->    754   377    58  58863
			'Geography.Regions.Americas.Central America'    1282  -->    422   860    89  58681
			'Geography.Regions.Americas.North America'      7247  -->   3861  3386   940  51865
			'Geography.Regions.Americas.South America'      1480  -->    675   805   148  58424
			'Geography.Regions.Asia.Asia*'                 10642  -->   7322  3320   967  48443
			'Geography.Regions.Asia.Central Asia'           1125  -->    554   571    51  58876
			'Geography.Regions.Asia.East Asia'              2594  -->   1391  1203   294  57164
			'Geography.Regions.Asia.North Asia'             1317  -->    682   635   191  58544
			'Geography.Regions.Asia.South Asia'             2361  -->   1707   654   126  57565
			'Geography.Regions.Asia.Southeast Asia'         1623  -->    733   890   105  58324
			'Geography.Regions.Asia.West Asia'              2154  -->   1286   868   120  57778
			'Geography.Regions.Europe.Eastern Europe'       2996  -->   1692  1304   336  56720
			'Geography.Regions.Europe.Europe*'             11970  -->   7229  4741  1774  46308
			'Geography.Regions.Europe.Northern Europe'      4083  -->   1653  2430   460  55509
			'Geography.Regions.Europe.Southern Europe'      2233  -->    878  1355   240  57579
			'Geography.Regions.Europe.Western Europe'       3035  -->   1508  1527   401  56616
			'Geography.Regions.Oceania'                     2466  -->   1401  1065    96  57490
			'History and Society.Business and economics'    3248  -->   1161  2087   492  56312
			'History and Society.Education'                 2097  -->    886  1211   249  57706
			'History and Society.History'                   3062  -->    616  2446   291  56699
			'History and Society.Military and warfare'      3819  -->   2293  1526   434  55799
			'History and Society.Politics and government'   4473  -->   1786  2687   448  55131
			'History and Society.Society'                   3850  -->    767  3083   288  55914
			'History and Society.Transportation'            3424  -->   2558   866   274  56354
			'STEM.Biology'                                  2735  -->   1986   749   147  57170
			'STEM.Chemistry'                                1251  -->    691   560   181  58620
			'STEM.Computing'                                1902  -->    976   926   403  57747
			'STEM.Earth and environment'                    1590  -->    800   790   116  58346
			'STEM.Engineering'                              2145  -->   1227   918   197  57710
			'STEM.Libraries & Information'                  1110  -->    519   591    70  58872
			'STEM.Mathematics'                              1026  -->    454   572   117  58909
			'STEM.Medicine & Health'                        1613  -->    849   764   176  58263
			'STEM.Physics'                                  1135  -->    523   612   152  58765
			'STEM.STEM*'                                   15592  -->  12285  3307  1433  43027
			'STEM.Space'                                    1330  -->   1038   292    51  58671
			'STEM.Technology'                               3436  -->   1552  1884   629  55987
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.272         0.123
		Culture.Biography.Women                         0.068         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.02          0.007
		Culture.Literature                              0.083         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.224         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.054         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.019         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.121         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.177         0.046
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.199         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.057         0.005
	match_rate (micro=0.051, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.133
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.085
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.05
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.08
		Geography.Regions.Europe.Northern Europe     0.02
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.016
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.007
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.019
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.004
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.915
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.95
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.92
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.993
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.981
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.628, macro=0.541):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.755
		Culture.Biography.Women                      0.28
		Culture.Food and drink                       0.627
		Culture.Internet culture                     0.649
		Culture.Linguistics                          0.546
		Culture.Literature                           0.584
		Culture.Media.Books                          0.51
		Culture.Media.Entertainment                  0.185
		Culture.Media.Films                          0.69
		Culture.Media.Media*                         0.768
		Culture.Media.Music                          0.713
		Culture.Media.Radio                          0.755
		Culture.Media.Software                       0.463
		Culture.Media.Television                     0.524
		Culture.Media.Video games                    0.789
		Culture.Performing arts                      0.486
		Culture.Philosophy and religion              0.443
		Culture.Sports                               0.865
		Culture.Visual arts.Architecture             0.618
		Culture.Visual arts.Comics and Anime         0.538
		Culture.Visual arts.Fashion                  0.608
		Culture.Visual arts.Visual arts*             0.55
		Geography.Geographical                       0.568
		Geography.Regions.Africa.Africa*             0.699
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.567
		Geography.Regions.Africa.Northern Africa     0.493
		Geography.Regions.Africa.Southern Africa     0.585
		Geography.Regions.Africa.Western Africa      0.667
		Geography.Regions.Americas.Central America   0.329
		Geography.Regions.Americas.North America     0.533
		Geography.Regions.Americas.South America     0.456
		Geography.Regions.Asia.Asia*                 0.688
		Geography.Regions.Asia.Central Asia          0.492
		Geography.Regions.Asia.East Asia             0.536
		Geography.Regions.Asia.North Asia            0.518
		Geography.Regions.Asia.South Asia            0.723
		Geography.Regions.Asia.Southeast Asia        0.452
		Geography.Regions.Asia.West Asia             0.597
		Geography.Regions.Europe.Eastern Europe      0.565
		Geography.Regions.Europe.Europe*             0.604
		Geography.Regions.Europe.Northern Europe     0.405
		Geography.Regions.Europe.Southern Europe     0.393
		Geography.Regions.Europe.Western Europe      0.497
		Geography.Regions.Oceania                    0.568
		History and Society.Business and economics   0.357
		History and Society.Education                0.423
		History and Society.History                  0.201
		History and Society.Military and warfare     0.6
		History and Society.Politics and government  0.399
		History and Society.Society                  0.199
		History and Society.Transportation           0.747
		STEM.Biology                                 0.726
		STEM.Chemistry                               0.552
		STEM.Computing                               0.513
		STEM.Earth and environment                   0.503
		STEM.Engineering                             0.572
		STEM.Libraries & Information                 0.468
		STEM.Mathematics                             0.442
		STEM.Medicine & Health                       0.526
		STEM.Physics                                 0.461
		STEM.STEM*                                   0.788
		STEM.Space                                   0.78
		STEM.Technology                              0.452
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.995
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.628, macro=0.479):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.7
		Culture.Biography.Women                      0.32
		Culture.Food and drink                       0.506
		Culture.Internet culture                     0.381
		Culture.Linguistics                          0.685
		Culture.Literature                           0.445
		Culture.Media.Books                          0.349
		Culture.Media.Entertainment                  0.266
		Culture.Media.Films                          0.66
		Culture.Media.Media*                         0.529
		Culture.Media.Music                          0.778
		Culture.Media.Radio                          0.612
		Culture.Media.Software                       0.09
		Culture.Media.Television                     0.499
		Culture.Media.Video games                    0.6
		Culture.Performing arts                      0.393
		Culture.Philosophy and religion              0.44
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.578
		Culture.Visual arts.Comics and Anime         0.355
		Culture.Visual arts.Fashion                  0.287
		Culture.Visual arts.Visual arts*             0.515
		Geography.Geographical                       0.732
		Geography.Regions.Africa.Africa*             0.519
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.23
		Geography.Regions.Africa.Northern Africa     0.271
		Geography.Regions.Africa.Southern Africa     0.42
		Geography.Regions.Africa.Western Africa      0.317
		Geography.Regions.Americas.Central America   0.419
		Geography.Regions.Americas.North America     0.673
		Geography.Regions.Americas.South America     0.534
		Geography.Regions.Asia.Asia*                 0.626
		Geography.Regions.Asia.Central Asia          0.33
		Geography.Regions.Asia.East Asia             0.548
		Geography.Regions.Asia.North Asia            0.128
		Geography.Regions.Asia.South Asia            0.836
		Geography.Regions.Asia.Southeast Asia        0.603
		Geography.Regions.Asia.West Asia             0.761
		Geography.Regions.Europe.Eastern Europe      0.555
		Geography.Regions.Europe.Europe*             0.575
		Geography.Regions.Europe.Northern Europe     0.609
		Geography.Regions.Europe.Southern Europe     0.556
		Geography.Regions.Europe.Western Europe      0.58
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.296
		History and Society.Education                0.422
		History and Society.History                  0.302
		History and Society.Military and warfare     0.526
		History and Society.Politics and government  0.59
		History and Society.Society                  0.332
		History and Society.Transportation           0.703
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.219
		STEM.Computing                               0.167
		STEM.Earth and environment                   0.536
		STEM.Engineering                             0.47
		STEM.Libraries & Information                 0.197
		STEM.Mathematics                             0.085
		STEM.Medicine & Health                       0.53
		STEM.Physics                                 0.132
		STEM.STEM*                                   0.645
		STEM.Space                                   0.845
		STEM.Technology                              0.173
		-------------------------------------------  -----
	!precision (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.993
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
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.983
		History and Society.Society                  0.99
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
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.727
		Culture.Biography.Women                      0.298
		Culture.Food and drink                       0.56
		Culture.Internet culture                     0.48
		Culture.Linguistics                          0.608
		Culture.Literature                           0.505
		Culture.Media.Books                          0.415
		Culture.Media.Entertainment                  0.218
		Culture.Media.Films                          0.675
		Culture.Media.Media*                         0.627
		Culture.Media.Music                          0.744
		Culture.Media.Radio                          0.676
		Culture.Media.Software                       0.15
		Culture.Media.Television                     0.511
		Culture.Media.Video games                    0.682
		Culture.Performing arts                      0.435
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.597
		Culture.Visual arts.Comics and Anime         0.428
		Culture.Visual arts.Fashion                  0.39
		Culture.Visual arts.Visual arts*             0.532
		Geography.Geographical                       0.64
		Geography.Regions.Africa.Africa*             0.596
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.327
		Geography.Regions.Africa.Northern Africa     0.35
		Geography.Regions.Africa.Southern Africa     0.489
		Geography.Regions.Africa.Western Africa      0.429
		Geography.Regions.Americas.Central America   0.369
		Geography.Regions.Americas.North America     0.595
		Geography.Regions.Americas.South America     0.492
		Geography.Regions.Asia.Asia*                 0.656
		Geography.Regions.Asia.Central Asia          0.395
		Geography.Regions.Asia.East Asia             0.542
		Geography.Regions.Asia.North Asia            0.206
		Geography.Regions.Asia.South Asia            0.776
		Geography.Regions.Asia.Southeast Asia        0.516
		Geography.Regions.Asia.West Asia             0.669
		Geography.Regions.Europe.Eastern Europe      0.56
		Geography.Regions.Europe.Europe*             0.589
		Geography.Regions.Europe.Northern Europe     0.486
		Geography.Regions.Europe.Southern Europe     0.461
		Geography.Regions.Europe.Western Europe      0.535
		Geography.Regions.Oceania                    0.678
		History and Society.Business and economics   0.324
		History and Society.Education                0.422
		History and Society.History                  0.241
		History and Society.Military and warfare     0.561
		History and Society.Politics and government  0.476
		History and Society.Society                  0.249
		History and Society.Transportation           0.724
		STEM.Biology                                 0.807
		STEM.Chemistry                               0.314
		STEM.Computing                               0.251
		STEM.Earth and environment                   0.519
		STEM.Engineering                             0.516
		STEM.Libraries & Information                 0.277
		STEM.Mathematics                             0.143
		STEM.Medicine & Health                       0.528
		STEM.Physics                                 0.205
		STEM.STEM*                                   0.709
		STEM.Space                                   0.811
		STEM.Technology                              0.251
		-------------------------------------------  -----
	!f1 (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.99
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
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
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
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
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
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.968, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.93
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.946
		Culture.Media.Music                          0.988
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.985
		History and Society.Education                0.991
		History and Society.History                  0.986
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.975
		History and Society.Society                  0.985
		History and Society.Transportation           0.991
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.955
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.045
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.042
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.005
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.005
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.005
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.954, macro=0.955):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.946
		Culture.Biography.Women                      0.935
		Culture.Food and drink                       0.973
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.959
		Culture.Literature                           0.96
		Culture.Media.Books                          0.97
		Culture.Media.Entertainment                  0.94
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.983
		Culture.Media.Software                       0.974
		Culture.Media.Television                     0.969
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.978
		Culture.Visual arts.Fashion                  0.978
		Culture.Visual arts.Visual arts*             0.952
		Geography.Geographical                       0.957
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.553
		Geography.Regions.Africa.Eastern Africa      0.97
		Geography.Regions.Africa.Northern Africa     0.966
		Geography.Regions.Africa.Southern Africa     0.972
		Geography.Regions.Africa.Western Africa      0.981
		Geography.Regions.Americas.Central America   0.952
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.962
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.973
		Geography.Regions.Asia.East Asia             0.965
		Geography.Regions.Asia.North Asia            0.974
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.96
		Geography.Regions.Asia.West Asia             0.971
		Geography.Regions.Europe.Eastern Europe      0.966
		Geography.Regions.Europe.Europe*             0.934
		Geography.Regions.Europe.Northern Europe     0.939
		Geography.Regions.Europe.Southern Europe     0.955
		Geography.Regions.Europe.Western Europe      0.954
		Geography.Regions.Oceania                    0.964
		History and Society.Business and economics   0.938
		History and Society.Education                0.952
		History and Society.History                  0.903
		History and Society.Military and warfare     0.963
		History and Society.Politics and government  0.929
		History and Society.Society                  0.866
		History and Society.Transportation           0.98
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.98
		STEM.Computing                               0.977
		STEM.Earth and environment                   0.963
		STEM.Engineering                             0.966
		STEM.Libraries & Information                 0.957
		STEM.Mathematics                             0.972
		STEM.Medicine & Health                       0.966
		STEM.Physics                                 0.977
		STEM.STEM*                                   0.958
		STEM.Space                                   0.986
		STEM.Technology                              0.953
		-------------------------------------------  -----
	pr_auc (micro=0.651, macro=0.483):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.795
		Culture.Biography.Women                      0.244
		Culture.Food and drink                       0.562
		Culture.Internet culture                     0.546
		Culture.Linguistics                          0.627
		Culture.Literature                           0.522
		Culture.Media.Books                          0.36
		Culture.Media.Entertainment                  0.15
		Culture.Media.Films                          0.695
		Culture.Media.Media*                         0.693
		Culture.Media.Music                          0.775
		Culture.Media.Radio                          0.766
		Culture.Media.Software                       0.103
		Culture.Media.Television                     0.49
		Culture.Media.Video games                    0.747
		Culture.Performing arts                      0.377
		Culture.Philosophy and religion              0.363
		Culture.Sports                               0.925
		Culture.Visual arts.Architecture             0.631
		Culture.Visual arts.Comics and Anime         0.443
		Culture.Visual arts.Fashion                  0.334
		Culture.Visual arts.Visual arts*             0.549
		Geography.Geographical                       0.686
		Geography.Regions.Africa.Africa*             0.587
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.217
		Geography.Regions.Africa.Northern Africa     0.322
		Geography.Regions.Africa.Southern Africa     0.436
		Geography.Regions.Africa.Western Africa      0.376
		Geography.Regions.Americas.Central America   0.316
		Geography.Regions.Americas.North America     0.652
		Geography.Regions.Americas.South America     0.443
		Geography.Regions.Asia.Asia*                 0.692
		Geography.Regions.Asia.Central Asia          0.414
		Geography.Regions.Asia.East Asia             0.517
		Geography.Regions.Asia.North Asia            0.181
		Geography.Regions.Asia.South Asia            0.808
		Geography.Regions.Asia.Southeast Asia        0.493
		Geography.Regions.Asia.West Asia             0.726
		Geography.Regions.Europe.Eastern Europe      0.569
		Geography.Regions.Europe.Europe*             0.614
		Geography.Regions.Europe.Northern Europe     0.51
		Geography.Regions.Europe.Southern Europe     0.453
		Geography.Regions.Europe.Western Europe      0.528
		Geography.Regions.Oceania                    0.729
		History and Society.Business and economics   0.249
		History and Society.Education                0.347
		History and Society.History                  0.174
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.506
		History and Society.Society                  0.207
		History and Society.Transportation           0.766
		STEM.Biology                                 0.861
		STEM.Chemistry                               0.228
		STEM.Computing                               0.186
		STEM.Earth and environment                   0.495
		STEM.Engineering                             0.536
		STEM.Libraries & Information                 0.229
		STEM.Mathematics                             0.11
		STEM.Medicine & Health                       0.487
		STEM.Physics                                 0.157
		STEM.STEM*                                   0.795
		STEM.Space                                   0.845
		STEM.Technology                              0.211
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

