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
	counts (n=58260):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15310  -->  13188  2122  1128  41822
			'Culture.Biography.Women'                       3531  -->   2147  1384   378  54351
			'Culture.Food and drink'                        1437  -->    828   609   122  56701
			'Culture.Internet culture'                      3201  -->   2503   698   246  54813
			'Culture.Linguistics'                           1596  -->    970   626   134  56530
			'Culture.Literature'                            5484  -->   3747  1737   533  52243
			'Culture.Media.Books'                           1715  -->   1272   443   123  56422
			'Culture.Media.Entertainment'                   2307  -->    847  1460   234  55719
			'Culture.Media.Films'                           2816  -->   2197   619   180  55264
			'Culture.Media.Media*'                         14125  -->  12089  2036  1429  42706
			'Culture.Media.Music'                           3252  -->   2583   669   246  54762
			'Culture.Media.Radio'                            323  -->    168   155    43  57894
			'Culture.Media.Software'                        2128  -->   1630   498   290  55842
			'Culture.Media.Television'                      2434  -->   1823   611   162  55664
			'Culture.Media.Video games'                     2038  -->   1772   266    64  56158
			'Culture.Performing arts'                       1459  -->    816   643   139  56662
			'Culture.Philosophy and religion'               3909  -->   1983  1926   377  53974
			'Culture.Sports'                                6193  -->   5459   734   192  51875
			'Culture.Visual arts.Architecture'              1992  -->   1213   779   235  56033
			'Culture.Visual arts.Comics and Anime'          1824  -->   1394   430   109  56327
			'Culture.Visual arts.Fashion'                    776  -->    410   366    60  57424
			'Culture.Visual arts.Visual arts*'              5280  -->   3199  2081   449  52531
			'Geography.Geographical'                        3799  -->   2329  1470   514  53947
			'Geography.Regions.Africa.Africa*'              3983  -->   2411  1572   364  53913
			'Geography.Regions.Africa.Central Africa'        874  -->    528   346    65  57321
			'Geography.Regions.Africa.Eastern Africa'        361  -->    222   139    34  57865
			'Geography.Regions.Africa.Northern Africa'      1468  -->    835   633   118  56674
			'Geography.Regions.Africa.Southern Africa'       683  -->    451   232    49  57528
			'Geography.Regions.Africa.Western Africa'        155  -->     71    84    29  58076
			'Geography.Regions.Americas.Central America'    1354  -->    716   638   102  56804
			'Geography.Regions.Americas.North America'      5506  -->   3143  2363   789  51965
			'Geography.Regions.Americas.South America'      1602  -->   1026   576   135  56523
			'Geography.Regions.Asia.Asia*'                 10551  -->   7924  2627  1079  46630
			'Geography.Regions.Asia.Central Asia'           1318  -->    851   467   106  56836
			'Geography.Regions.Asia.East Asia'              3361  -->   2428   933   234  54665
			'Geography.Regions.Asia.North Asia'             1840  -->   1225   615   230  56190
			'Geography.Regions.Asia.South Asia'             1780  -->   1170   610   109  56371
			'Geography.Regions.Asia.Southeast Asia'         1584  -->    835   749   105  56571
			'Geography.Regions.Asia.West Asia'              2439  -->   1608   831   218  55603
			'Geography.Regions.Europe.Eastern Europe'       4845  -->   3306  1539   598  52817
			'Geography.Regions.Europe.Europe*'             16576  -->  12822  3754  2334  39350
			'Geography.Regions.Europe.Northern Europe'      3563  -->   2170  1393   391  54306
			'Geography.Regions.Europe.Southern Europe'      4000  -->   2756  1244   370  53890
			'Geography.Regions.Europe.Western Europe'       5143  -->   3650  1493   574  52543
			'Geography.Regions.Oceania'                     1821  -->   1188   633   127  56312
			'History and Society.Business and economics'    3106  -->   1499  1607   313  54841
			'History and Society.Education'                 1568  -->    616   952   122  56570
			'History and Society.History'                   6030  -->   3430  2600   688  51542
			'History and Society.Military and warfare'      4947  -->   3234  1713   505  52808
			'History and Society.Politics and government'   4355  -->   2253  2102   403  53502
			'History and Society.Society'                   6075  -->   2523  3552   512  51673
			'History and Society.Transportation'            4015  -->   3497   518   203  54042
			'STEM.Biology'                                  4621  -->   3881   740   166  53473
			'STEM.Chemistry'                                1581  -->   1187   394   197  56482
			'STEM.Computing'                                2399  -->   1829   570   296  55565
			'STEM.Earth and environment'                    1842  -->   1146   696   154  56264
			'STEM.Engineering'                              2439  -->   1574   865   213  55608
			'STEM.Libraries & Information'                   498  -->    264   234    23  57739
			'STEM.Mathematics'                               979  -->    731   248    45  57236
			'STEM.Medicine & Health'                        1865  -->   1231   634   182  56213
			'STEM.Physics'                                  1378  -->    757   621   194  56688
			'STEM.STEM*'                                   18114  -->  15835  2279  1145  39001
			'STEM.Space'                                    2331  -->   2124   207    66  55863
			'STEM.Technology'                               4782  -->   3384  1398   582  52896
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.263         0.123
		Culture.Biography.Women                         0.061         0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.055         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.04          0.004
		Culture.Media.Films                             0.048         0.011
		Culture.Media.Media*                            0.242         0.058
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.006         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.067         0.011
		Culture.Sports                                  0.106         0.071
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.031         0.002
		Culture.Visual arts.Fashion                     0.013         0.001
		Culture.Visual arts.Visual arts*                0.091         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.012         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.095         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.181         0.045
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.058         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.042         0.011
		Geography.Regions.Europe.Eastern Europe         0.083         0.013
		Geography.Regions.Europe.Europe*                0.285         0.076
		Geography.Regions.Europe.Northern Europe        0.061         0.031
		Geography.Regions.Europe.Southern Europe        0.069         0.013
		Geography.Regions.Europe.Western Europe         0.088         0.019
		Geography.Regions.Oceania                       0.031         0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.027         0.007
		History and Society.History                     0.104         0.011
		History and Society.Military and warfare        0.085         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.104         0.013
		History and Society.Transportation              0.069         0.015
		STEM.Biology                                    0.079         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.042         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.311         0.069
		STEM.Space                                      0.04          0.006
		STEM.Technology                                 0.082         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.019
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.056
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.01
		History and Society.Education                0.005
		History and Society.History                  0.019
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.022
		History and Society.Society                  0.015
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.005
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.087
		STEM.Space                                   0.007
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.944
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.981
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.978
		History and Society.Society                  0.985
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.995
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.913
		STEM.Space                                   0.993
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.731, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.608
		Culture.Food and drink                       0.576
		Culture.Internet culture                     0.782
		Culture.Linguistics                          0.608
		Culture.Literature                           0.683
		Culture.Media.Books                          0.742
		Culture.Media.Entertainment                  0.367
		Culture.Media.Films                          0.78
		Culture.Media.Media*                         0.856
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.52
		Culture.Media.Software                       0.766
		Culture.Media.Television                     0.749
		Culture.Media.Video games                    0.869
		Culture.Performing arts                      0.559
		Culture.Philosophy and religion              0.507
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.609
		Culture.Visual arts.Comics and Anime         0.764
		Culture.Visual arts.Fashion                  0.528
		Culture.Visual arts.Visual arts*             0.606
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.605
		Geography.Regions.Africa.Central Africa      0.604
		Geography.Regions.Africa.Eastern Africa      0.615
		Geography.Regions.Africa.Northern Africa     0.569
		Geography.Regions.Africa.Southern Africa     0.66
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.529
		Geography.Regions.Americas.North America     0.571
		Geography.Regions.Americas.South America     0.64
		Geography.Regions.Asia.Asia*                 0.751
		Geography.Regions.Asia.Central Asia          0.646
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.666
		Geography.Regions.Asia.South Asia            0.657
		Geography.Regions.Asia.Southeast Asia        0.527
		Geography.Regions.Asia.West Asia             0.659
		Geography.Regions.Europe.Eastern Europe      0.682
		Geography.Regions.Europe.Europe*             0.774
		Geography.Regions.Europe.Northern Europe     0.609
		Geography.Regions.Europe.Southern Europe     0.689
		Geography.Regions.Europe.Western Europe      0.71
		Geography.Regions.Oceania                    0.652
		History and Society.Business and economics   0.483
		History and Society.Education                0.393
		History and Society.History                  0.569
		History and Society.Military and warfare     0.654
		History and Society.Politics and government  0.517
		History and Society.Society                  0.415
		History and Society.Transportation           0.871
		STEM.Biology                                 0.84
		STEM.Chemistry                               0.751
		STEM.Computing                               0.762
		STEM.Earth and environment                   0.622
		STEM.Engineering                             0.645
		STEM.Libraries & Information                 0.53
		STEM.Mathematics                             0.747
		STEM.Medicine & Health                       0.66
		STEM.Physics                                 0.549
		STEM.STEM*                                   0.874
		STEM.Space                                   0.911
		STEM.Technology                              0.708
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.993
		History and Society.Society                  0.99
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.671, macro=0.522):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.822
		Culture.Biography.Women                      0.565
		Culture.Food and drink                       0.399
		Culture.Internet culture                     0.381
		Culture.Linguistics                          0.655
		Culture.Literature                           0.516
		Culture.Media.Books                          0.579
		Culture.Media.Entertainment                  0.24
		Culture.Media.Films                          0.719
		Culture.Media.Media*                         0.621
		Culture.Media.Music                          0.813
		Culture.Media.Radio                          0.602
		Culture.Media.Software                       0.165
		Culture.Media.Television                     0.696
		Culture.Media.Video games                    0.667
		Culture.Performing arts                      0.398
		Culture.Philosophy and religion              0.44
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.609
		Culture.Visual arts.Comics and Anime         0.465
		Culture.Visual arts.Fashion                  0.291
		Culture.Visual arts.Visual arts*             0.571
		Geography.Geographical                       0.611
		Geography.Regions.Africa.Africa*             0.415
		Geography.Regions.Africa.Central Africa      0.252
		Geography.Regions.Africa.Eastern Africa      0.323
		Geography.Regions.Africa.Northern Africa     0.252
		Geography.Regions.Africa.Southern Africa     0.477
		Geography.Regions.Africa.Western Africa      0.386
		Geography.Regions.Americas.Central America   0.494
		Geography.Regions.Americas.North America     0.724
		Geography.Regions.Americas.South America     0.63
		Geography.Regions.Asia.Asia*                 0.613
		Geography.Regions.Asia.Central Asia          0.231
		Geography.Regions.Asia.East Asia             0.662
		Geography.Regions.Asia.North Asia            0.131
		Geography.Regions.Asia.South Asia            0.84
		Geography.Regions.Asia.Southeast Asia        0.632
		Geography.Regions.Asia.West Asia             0.65
		Geography.Regions.Europe.Eastern Europe      0.442
		Geography.Regions.Europe.Europe*             0.532
		Geography.Regions.Europe.Northern Europe     0.729
		Geography.Regions.Europe.Southern Europe     0.572
		Geography.Regions.Europe.Western Europe      0.562
		Geography.Regions.Oceania                    0.817
		History and Society.Business and economics   0.464
		History and Society.Education                0.575
		History and Society.History                  0.321
		History and Society.Military and warfare     0.496
		History and Society.Politics and government  0.667
		History and Society.Society                  0.351
		History and Society.Transportation           0.781
		STEM.Biology                                 0.904
		STEM.Chemistry                               0.252
		STEM.Computing                               0.28
		STEM.Earth and environment                   0.509
		STEM.Engineering                             0.471
		STEM.Libraries & Information                 0.453
		STEM.Mathematics                             0.284
		STEM.Medicine & Health                       0.568
		STEM.Physics                                 0.12
		STEM.STEM*                                   0.695
		STEM.Space                                   0.824
		STEM.Technology                              0.251
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
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
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.691, macro=0.563):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.841
		Culture.Biography.Women                      0.586
		Culture.Food and drink                       0.471
		Culture.Internet culture                     0.512
		Culture.Linguistics                          0.63
		Culture.Literature                           0.588
		Culture.Media.Books                          0.651
		Culture.Media.Entertainment                  0.29
		Culture.Media.Films                          0.748
		Culture.Media.Media*                         0.72
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.558
		Culture.Media.Software                       0.271
		Culture.Media.Television                     0.722
		Culture.Media.Video games                    0.755
		Culture.Performing arts                      0.465
		Culture.Philosophy and religion              0.472
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.609
		Culture.Visual arts.Comics and Anime         0.579
		Culture.Visual arts.Fashion                  0.375
		Culture.Visual arts.Visual arts*             0.588
		Geography.Geographical                       0.612
		Geography.Regions.Africa.Africa*             0.492
		Geography.Regions.Africa.Central Africa      0.356
		Geography.Regions.Africa.Eastern Africa      0.423
		Geography.Regions.Africa.Northern Africa     0.349
		Geography.Regions.Africa.Southern Africa     0.554
		Geography.Regions.Africa.Western Africa      0.419
		Geography.Regions.Americas.Central America   0.511
		Geography.Regions.Americas.North America     0.638
		Geography.Regions.Americas.South America     0.635
		Geography.Regions.Asia.Asia*                 0.675
		Geography.Regions.Asia.Central Asia          0.34
		Geography.Regions.Asia.East Asia             0.691
		Geography.Regions.Asia.North Asia            0.219
		Geography.Regions.Asia.South Asia            0.738
		Geography.Regions.Asia.Southeast Asia        0.575
		Geography.Regions.Asia.West Asia             0.655
		Geography.Regions.Europe.Eastern Europe      0.536
		Geography.Regions.Europe.Europe*             0.631
		Geography.Regions.Europe.Northern Europe     0.664
		Geography.Regions.Europe.Southern Europe     0.625
		Geography.Regions.Europe.Western Europe      0.627
		Geography.Regions.Oceania                    0.725
		History and Society.Business and economics   0.473
		History and Society.Education                0.467
		History and Society.History                  0.41
		History and Society.Military and warfare     0.564
		History and Society.Politics and government  0.583
		History and Society.Society                  0.38
		History and Society.Transportation           0.823
		STEM.Biology                                 0.871
		STEM.Chemistry                               0.378
		STEM.Computing                               0.409
		STEM.Earth and environment                   0.56
		STEM.Engineering                             0.544
		STEM.Libraries & Information                 0.488
		STEM.Mathematics                             0.411
		STEM.Medicine & Health                       0.611
		STEM.Physics                                 0.197
		STEM.STEM*                                   0.774
		STEM.Space                                   0.865
		STEM.Technology                              0.371
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.931
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.983
		History and Society.Transportation           0.994
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.965
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.023
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.007
		History and Society.Society                  0.01
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.029
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.965, macro=0.965):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.968
		Culture.Food and drink                       0.965
		Culture.Internet culture                     0.98
		Culture.Linguistics                          0.962
		Culture.Literature                           0.967
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.917
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.967
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.956
		Culture.Visual arts.Visual arts*             0.956
		Geography.Geographical                       0.962
		Geography.Regions.Africa.Africa*             0.96
		Geography.Regions.Africa.Central Africa      0.98
		Geography.Regions.Africa.Eastern Africa      0.946
		Geography.Regions.Africa.Northern Africa     0.962
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.903
		Geography.Regions.Americas.Central America   0.966
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.973
		Geography.Regions.Asia.East Asia             0.974
		Geography.Regions.Asia.North Asia            0.982
		Geography.Regions.Asia.South Asia            0.97
		Geography.Regions.Asia.Southeast Asia        0.964
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.968
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.96
		Geography.Regions.Europe.Southern Europe     0.967
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.967
		History and Society.Business and economics   0.947
		History and Society.Education                0.952
		History and Society.History                  0.947
		History and Society.Military and warfare     0.964
		History and Society.Politics and government  0.938
		History and Society.Society                  0.909
		History and Society.Transportation           0.983
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.983
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.97
		STEM.Libraries & Information                 0.962
		STEM.Mathematics                             0.976
		STEM.Medicine & Health                       0.969
		STEM.Physics                                 0.97
		STEM.STEM*                                   0.971
		STEM.Space                                   0.99
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.734, macro=0.552):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.908
		Culture.Biography.Women                      0.574
		Culture.Food and drink                       0.386
		Culture.Internet culture                     0.635
		Culture.Linguistics                          0.587
		Culture.Literature                           0.629
		Culture.Media.Books                          0.698
		Culture.Media.Entertainment                  0.188
		Culture.Media.Films                          0.808
		Culture.Media.Media*                         0.825
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.299
		Culture.Media.Software                       0.269
		Culture.Media.Television                     0.745
		Culture.Media.Video games                    0.822
		Culture.Performing arts                      0.413
		Culture.Philosophy and religion              0.421
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.586
		Culture.Visual arts.Comics and Anime         0.621
		Culture.Visual arts.Fashion                  0.221
		Culture.Visual arts.Visual arts*             0.586
		Geography.Geographical                       0.597
		Geography.Regions.Africa.Africa*             0.467
		Geography.Regions.Africa.Central Africa      0.237
		Geography.Regions.Africa.Eastern Africa      0.189
		Geography.Regions.Africa.Northern Africa     0.232
		Geography.Regions.Africa.Southern Africa     0.407
		Geography.Regions.Africa.Western Africa      0.216
		Geography.Regions.Americas.Central America   0.42
		Geography.Regions.Americas.North America     0.708
		Geography.Regions.Americas.South America     0.615
		Geography.Regions.Asia.Asia*                 0.73
		Geography.Regions.Asia.Central Asia          0.226
		Geography.Regions.Asia.East Asia             0.713
		Geography.Regions.Asia.North Asia            0.21
		Geography.Regions.Asia.South Asia            0.787
		Geography.Regions.Asia.Southeast Asia        0.545
		Geography.Regions.Asia.West Asia             0.629
		Geography.Regions.Europe.Eastern Europe      0.533
		Geography.Regions.Europe.Europe*             0.727
		Geography.Regions.Europe.Northern Europe     0.703
		Geography.Regions.Europe.Southern Europe     0.652
		Geography.Regions.Europe.Western Europe      0.711
		Geography.Regions.Oceania                    0.743
		History and Society.Business and economics   0.413
		History and Society.Education                0.426
		History and Society.History                  0.415
		History and Society.Military and warfare     0.599
		History and Society.Politics and government  0.6
		History and Society.Society                  0.339
		History and Society.Transportation           0.879
		STEM.Biology                                 0.895
		STEM.Chemistry                               0.381
		STEM.Computing                               0.418
		STEM.Earth and environment                   0.519
		STEM.Engineering                             0.551
		STEM.Libraries & Information                 0.28
		STEM.Mathematics                             0.606
		STEM.Medicine & Health                       0.593
		STEM.Physics                                 0.109
		STEM.STEM*                                   0.882
		STEM.Space                                   0.932
		STEM.Technology                              0.467
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

