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
	counts (n=63903):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16772  -->  15836   936   473  46658
			'Culture.Biography.Women'                       4235  -->   3161  1074   730  58938
			'Culture.Food and drink'                        1310  -->    630   680    79  62514
			'Culture.Internet culture'                      2918  -->   1920   998   130  60855
			'Culture.Linguistics'                           1348  -->    846   502    61  62494
			'Culture.Literature'                            5284  -->   3836  1448   419  58200
			'Culture.Media.Books'                           1860  -->   1462   398   130  61913
			'Culture.Media.Entertainment'                   1828  -->    874   954   181  61894
			'Culture.Media.Films'                           2316  -->   1927   389   115  61472
			'Culture.Media.Media*'                         14359  -->  11633  2726  1159  48385
			'Culture.Media.Music'                           2667  -->   2071   596   255  60981
			'Culture.Media.Radio'                           1175  -->    895   280    30  62698
			'Culture.Media.Software'                        1781  -->    671  1110   343  61779
			'Culture.Media.Television'                      2229  -->   1526   703   189  61485
			'Culture.Media.Video games'                     2060  -->   1711   349    50  61793
			'Culture.Performing arts'                       1332  -->    772   560    89  62482
			'Culture.Philosophy and religion'               2759  -->   1123  1636   281  60863
			'Culture.Sports'                                5998  -->   5306   692   238  57667
			'Culture.Visual arts.Architecture'              2631  -->   1863   768   240  61032
			'Culture.Visual arts.Comics and Anime'          1465  -->   1004   461   139  62299
			'Culture.Visual arts.Fashion'                   1137  -->    653   484    93  62673
			'Culture.Visual arts.Visual arts*'              5955  -->   4123  1832   561  57387
			'Geography.Geographical'                        3488  -->   2258  1230   343  60072
			'Geography.Regions.Africa.Africa*'              6434  -->   4644  1790   419  57050
			'Geography.Regions.Africa.Central Africa'       1149  -->    748   401    66  62688
			'Geography.Regions.Africa.Eastern Africa'       1096  -->    670   426    58  62749
			'Geography.Regions.Africa.Northern Africa'      1278  -->    831   447    98  62527
			'Geography.Regions.Africa.Southern Africa'      1265  -->    876   389    78  62560
			'Geography.Regions.Africa.Western Africa'       1120  -->    754   366    75  62708
			'Geography.Regions.Americas.Central America'    1331  -->    681   650    94  62478
			'Geography.Regions.Americas.North America'      7625  -->   5110  2515  1270  55008
			'Geography.Regions.Americas.South America'      1538  -->   1092   446   138  62227
			'Geography.Regions.Asia.Asia*'                 11079  -->   8028  3051   816  52008
			'Geography.Regions.Asia.Central Asia'           1121  -->    716   405    78  62704
			'Geography.Regions.Asia.East Asia'              2625  -->   1716   909   246  61032
			'Geography.Regions.Asia.North Asia'             1403  -->    777   626   192  62308
			'Geography.Regions.Asia.South Asia'             2385  -->   1684   701   118  61400
			'Geography.Regions.Asia.Southeast Asia'         1658  -->   1051   607   119  62126
			'Geography.Regions.Asia.West Asia'              2344  -->   1592   752   131  61428
			'Geography.Regions.Europe.Eastern Europe'       3081  -->   2110   971   286  60536
			'Geography.Regions.Europe.Europe*'             12459  -->   9044  3415  1775  49669
			'Geography.Regions.Europe.Northern Europe'      4198  -->   2577  1621   543  59162
			'Geography.Regions.Europe.Southern Europe'      2461  -->   1525   936   309  61133
			'Geography.Regions.Europe.Western Europe'       3096  -->   2006  1090   392  60415
			'Geography.Regions.Oceania'                     2502  -->   1812   690   156  61245
			'History and Society.Business and economics'    3362  -->   1473  1889   561  59980
			'History and Society.Education'                 2177  -->   1046  1131   224  61502
			'History and Society.History'                   3329  -->   1261  2068   401  60173
			'History and Society.Military and warfare'      4058  -->   2304  1754   399  59446
			'History and Society.Politics and government'   4630  -->   2462  2168   360  58913
			'History and Society.Society'                   4091  -->   1621  2470   385  59427
			'History and Society.Transportation'            3596  -->   2603   993   186  60121
			'STEM.Biology'                                  2954  -->   2240   714   122  60827
			'STEM.Chemistry'                                1302  -->    685   617   122  62479
			'STEM.Computing'                                2021  -->    804  1217   328  61554
			'STEM.Earth and environment'                    1643  -->    947   696    90  62170
			'STEM.Engineering'                              2356  -->   1361   995   139  61408
			'STEM.Libraries & Information'                  1167  -->    616   551    65  62671
			'STEM.Mathematics'                              1128  -->    351   777   105  62670
			'STEM.Medicine & Health'                        1760  -->    775   985   170  61973
			'STEM.Physics'                                  1208  -->    489   719   112  62583
			'STEM.STEM*'                                   16613  -->  14054  2559  3679  43611
			'STEM.Space'                                    1399  -->    977   422    39  62465
			'STEM.Technology'                               3693  -->   1366  2327   501  59709
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.262         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.046         0.003
		Culture.Linguistics                             0.021         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.225         0.058
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.043         0.011
		Culture.Sports                                  0.094         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.055         0.024
		Geography.Regions.Africa.Africa*                0.101         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.173         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.041         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.037         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.037         0.011
		Geography.Regions.Europe.Eastern Europe         0.048         0.013
		Geography.Regions.Europe.Europe*                0.195         0.076
		Geography.Regions.Europe.Northern Europe        0.066         0.031
		Geography.Regions.Europe.Southern Europe        0.039         0.013
		Geography.Regions.Europe.Western Europe         0.048         0.019
		Geography.Regions.Oceania                       0.039         0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.037         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.054, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.023
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.006
		Culture.Literature                           0.018
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.069
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.064
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.048
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.087
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.014
		History and Society.Education                0.007
		History and Society.History                  0.011
		History and Society.Military and warfare     0.015
		History and Society.Politics and government  0.021
		History and Society.Society                  0.011
		History and Society.Transportation           0.014
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.004
		STEM.Engineering                             0.005
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.131
		STEM.Space                                   0.005
		STEM.Technology                              0.01
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.994
		Culture.Literature                           0.982
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.931
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.936
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.952
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.913
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.979
		History and Society.Society                  0.989
		History and Society.Transportation           0.986
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.869
		STEM.Space                                   0.995
		STEM.Technology                              0.99
		-------------------------------------------  -----
	recall (micro=0.73, macro=0.627):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.944
		Culture.Biography.Women                      0.746
		Culture.Food and drink                       0.481
		Culture.Internet culture                     0.658
		Culture.Linguistics                          0.628
		Culture.Literature                           0.726
		Culture.Media.Books                          0.786
		Culture.Media.Entertainment                  0.478
		Culture.Media.Films                          0.832
		Culture.Media.Media*                         0.81
		Culture.Media.Music                          0.777
		Culture.Media.Radio                          0.762
		Culture.Media.Software                       0.377
		Culture.Media.Television                     0.685
		Culture.Media.Video games                    0.831
		Culture.Performing arts                      0.58
		Culture.Philosophy and religion              0.407
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.708
		Culture.Visual arts.Comics and Anime         0.685
		Culture.Visual arts.Fashion                  0.574
		Culture.Visual arts.Visual arts*             0.692
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.722
		Geography.Regions.Africa.Central Africa      0.651
		Geography.Regions.Africa.Eastern Africa      0.611
		Geography.Regions.Africa.Northern Africa     0.65
		Geography.Regions.Africa.Southern Africa     0.692
		Geography.Regions.Africa.Western Africa      0.673
		Geography.Regions.Americas.Central America   0.512
		Geography.Regions.Americas.North America     0.67
		Geography.Regions.Americas.South America     0.71
		Geography.Regions.Asia.Asia*                 0.725
		Geography.Regions.Asia.Central Asia          0.639
		Geography.Regions.Asia.East Asia             0.654
		Geography.Regions.Asia.North Asia            0.554
		Geography.Regions.Asia.South Asia            0.706
		Geography.Regions.Asia.Southeast Asia        0.634
		Geography.Regions.Asia.West Asia             0.679
		Geography.Regions.Europe.Eastern Europe      0.685
		Geography.Regions.Europe.Europe*             0.726
		Geography.Regions.Europe.Northern Europe     0.614
		Geography.Regions.Europe.Southern Europe     0.62
		Geography.Regions.Europe.Western Europe      0.648
		Geography.Regions.Oceania                    0.724
		History and Society.Business and economics   0.438
		History and Society.Education                0.48
		History and Society.History                  0.379
		History and Society.Military and warfare     0.568
		History and Society.Politics and government  0.532
		History and Society.Society                  0.396
		History and Society.Transportation           0.724
		STEM.Biology                                 0.758
		STEM.Chemistry                               0.526
		STEM.Computing                               0.398
		STEM.Earth and environment                   0.576
		STEM.Engineering                             0.578
		STEM.Libraries & Information                 0.528
		STEM.Mathematics                             0.311
		STEM.Medicine & Health                       0.44
		STEM.Physics                                 0.405
		STEM.STEM*                                   0.846
		STEM.Space                                   0.698
		STEM.Technology                              0.37
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.99
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.994
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.922
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.695, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.93
		Culture.Biography.Women                      0.474
		Culture.Food and drink                       0.485
		Culture.Internet culture                     0.52
		Culture.Linguistics                          0.826
		Culture.Literature                           0.615
		Culture.Media.Books                          0.603
		Culture.Media.Entertainment                  0.371
		Culture.Media.Films                          0.826
		Culture.Media.Media*                         0.683
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.775
		Culture.Media.Software                       0.083
		Culture.Media.Television                     0.665
		Culture.Media.Video games                    0.729
		Culture.Performing arts                      0.541
		Culture.Philosophy and religion              0.488
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.659
		Culture.Visual arts.Comics and Anime         0.404
		Culture.Visual arts.Fashion                  0.239
		Culture.Visual arts.Visual arts*             0.571
		Geography.Geographical                       0.734
		Geography.Regions.Africa.Africa*             0.438
		Geography.Regions.Africa.Central Africa      0.281
		Geography.Regions.Africa.Eastern Africa      0.231
		Geography.Regions.Africa.Northern Africa     0.338
		Geography.Regions.Africa.Southern Africa     0.395
		Geography.Regions.Africa.Western Africa      0.278
		Geography.Regions.Americas.Central America   0.53
		Geography.Regions.Americas.North America     0.671
		Geography.Regions.Americas.South America     0.671
		Geography.Regions.Asia.Asia*                 0.691
		Geography.Regions.Asia.Central Asia          0.308
		Geography.Regions.Asia.East Asia             0.653
		Geography.Regions.Asia.North Asia            0.143
		Geography.Regions.Asia.South Asia            0.85
		Geography.Regions.Asia.Southeast Asia        0.667
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.654
		Geography.Regions.Europe.Europe*             0.634
		Geography.Regions.Europe.Northern Europe     0.68
		Geography.Regions.Europe.Southern Europe     0.619
		Geography.Regions.Europe.Western Europe      0.663
		Geography.Regions.Oceania                    0.814
		History and Society.Business and economics   0.325
		History and Society.Education                0.495
		History and Society.History                  0.385
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.717
		History and Society.Society                  0.44
		History and Society.Transportation           0.782
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.296
		STEM.Computing                               0.168
		STEM.Earth and environment                   0.645
		STEM.Engineering                             0.574
		STEM.Libraries & Information                 0.241
		STEM.Mathematics                             0.072
		STEM.Medicine & Health                       0.509
		STEM.Physics                                 0.161
		STEM.STEM*                                   0.447
		STEM.Space                                   0.871
		STEM.Technology                              0.186
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.992
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.988
		Culture.Media.Music                          0.995
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
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.996
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.988
		STEM.Space                                   0.998
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.704, macro=0.566):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.937
		Culture.Biography.Women                      0.58
		Culture.Food and drink                       0.483
		Culture.Internet culture                     0.581
		Culture.Linguistics                          0.713
		Culture.Literature                           0.666
		Culture.Media.Books                          0.682
		Culture.Media.Entertainment                  0.418
		Culture.Media.Films                          0.829
		Culture.Media.Media*                         0.741
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.768
		Culture.Media.Software                       0.136
		Culture.Media.Television                     0.675
		Culture.Media.Video games                    0.776
		Culture.Performing arts                      0.56
		Culture.Philosophy and religion              0.444
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.508
		Culture.Visual arts.Fashion                  0.337
		Culture.Visual arts.Visual arts*             0.626
		Geography.Geographical                       0.688
		Geography.Regions.Africa.Africa*             0.545
		Geography.Regions.Africa.Central Africa      0.393
		Geography.Regions.Africa.Eastern Africa      0.336
		Geography.Regions.Africa.Northern Africa     0.445
		Geography.Regions.Africa.Southern Africa     0.503
		Geography.Regions.Africa.Western Africa      0.394
		Geography.Regions.Americas.Central America   0.521
		Geography.Regions.Americas.North America     0.671
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.707
		Geography.Regions.Asia.Central Asia          0.416
		Geography.Regions.Asia.East Asia             0.653
		Geography.Regions.Asia.North Asia            0.227
		Geography.Regions.Asia.South Asia            0.771
		Geography.Regions.Asia.Southeast Asia        0.65
		Geography.Regions.Asia.West Asia             0.726
		Geography.Regions.Europe.Eastern Europe      0.669
		Geography.Regions.Europe.Europe*             0.677
		Geography.Regions.Europe.Northern Europe     0.645
		Geography.Regions.Europe.Southern Europe     0.62
		Geography.Regions.Europe.Western Europe      0.655
		Geography.Regions.Oceania                    0.766
		History and Society.Business and economics   0.373
		History and Society.Education                0.488
		History and Society.History                  0.382
		History and Society.Military and warfare     0.558
		History and Society.Politics and government  0.611
		History and Society.Society                  0.417
		History and Society.Transportation           0.752
		STEM.Biology                                 0.835
		STEM.Chemistry                               0.379
		STEM.Computing                               0.237
		STEM.Earth and environment                   0.609
		STEM.Engineering                             0.576
		STEM.Libraries & Information                 0.33
		STEM.Mathematics                             0.117
		STEM.Medicine & Health                       0.472
		STEM.Physics                                 0.231
		STEM.STEM*                                   0.585
		STEM.Space                                   0.775
		STEM.Technology                              0.248
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.991
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.954
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.996
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.993
		History and Society.History                  0.987
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.981
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.917
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.01
		Culture.Biography.Women                      0.012
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.002
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.023
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.023
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.015
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.035
		Geography.Regions.Europe.Northern Europe     0.009
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.007
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.006
		History and Society.Society                  0.006
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.078
		STEM.Space                                   0.001
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.958, macro=0.953):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.972
		Culture.Food and drink                       0.941
		Culture.Internet culture                     0.959
		Culture.Linguistics                          0.953
		Culture.Literature                           0.963
		Culture.Media.Books                          0.972
		Culture.Media.Entertainment                  0.946
		Culture.Media.Films                          0.975
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.961
		Culture.Media.Software                       0.942
		Culture.Media.Television                     0.966
		Culture.Media.Video games                    0.977
		Culture.Performing arts                      0.949
		Culture.Philosophy and religion              0.914
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.97
		Culture.Visual arts.Comics and Anime         0.965
		Culture.Visual arts.Fashion                  0.955
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.954
		Geography.Regions.Africa.Africa*             0.963
		Geography.Regions.Africa.Central Africa      0.965
		Geography.Regions.Africa.Eastern Africa      0.954
		Geography.Regions.Africa.Northern Africa     0.955
		Geography.Regions.Africa.Southern Africa     0.963
		Geography.Regions.Africa.Western Africa      0.963
		Geography.Regions.Americas.Central America   0.939
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.965
		Geography.Regions.Asia.Asia*                 0.952
		Geography.Regions.Asia.Central Asia          0.961
		Geography.Regions.Asia.East Asia             0.947
		Geography.Regions.Asia.North Asia            0.957
		Geography.Regions.Asia.South Asia            0.957
		Geography.Regions.Asia.Southeast Asia        0.949
		Geography.Regions.Asia.West Asia             0.957
		Geography.Regions.Europe.Eastern Europe      0.962
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.95
		Geography.Regions.Europe.Southern Europe     0.951
		Geography.Regions.Europe.Western Europe      0.951
		Geography.Regions.Oceania                    0.958
		History and Society.Business and economics   0.937
		History and Society.Education                0.941
		History and Society.History                  0.915
		History and Society.Military and warfare     0.941
		History and Society.Politics and government  0.924
		History and Society.Society                  0.889
		History and Society.Transportation           0.964
		STEM.Biology                                 0.961
		STEM.Chemistry                               0.961
		STEM.Computing                               0.951
		STEM.Earth and environment                   0.947
		STEM.Engineering                             0.95
		STEM.Libraries & Information                 0.949
		STEM.Mathematics                             0.941
		STEM.Medicine & Health                       0.933
		STEM.Physics                                 0.95
		STEM.STEM*                                   0.957
		STEM.Space                                   0.965
		STEM.Technology                              0.929
		-------------------------------------------  -----
	pr_auc (micro=0.727, macro=0.538):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.573
		Culture.Food and drink                       0.406
		Culture.Internet culture                     0.546
		Culture.Linguistics                          0.604
		Culture.Literature                           0.705
		Culture.Media.Books                          0.625
		Culture.Media.Entertainment                  0.365
		Culture.Media.Films                          0.815
		Culture.Media.Media*                         0.831
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.767
		Culture.Media.Software                       0.085
		Culture.Media.Television                     0.658
		Culture.Media.Video games                    0.806
		Culture.Performing arts                      0.552
		Culture.Philosophy and religion              0.323
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.677
		Culture.Visual arts.Comics and Anime         0.58
		Culture.Visual arts.Fashion                  0.274
		Culture.Visual arts.Visual arts*             0.655
		Geography.Geographical                       0.705
		Geography.Regions.Africa.Africa*             0.591
		Geography.Regions.Africa.Central Africa      0.339
		Geography.Regions.Africa.Eastern Africa      0.274
		Geography.Regions.Africa.Northern Africa     0.346
		Geography.Regions.Africa.Southern Africa     0.439
		Geography.Regions.Africa.Western Africa      0.309
		Geography.Regions.Americas.Central America   0.447
		Geography.Regions.Americas.North America     0.718
		Geography.Regions.Americas.South America     0.678
		Geography.Regions.Asia.Asia*                 0.746
		Geography.Regions.Asia.Central Asia          0.376
		Geography.Regions.Asia.East Asia             0.596
		Geography.Regions.Asia.North Asia            0.163
		Geography.Regions.Asia.South Asia            0.74
		Geography.Regions.Asia.Southeast Asia        0.585
		Geography.Regions.Asia.West Asia             0.683
		Geography.Regions.Europe.Eastern Europe      0.675
		Geography.Regions.Europe.Europe*             0.744
		Geography.Regions.Europe.Northern Europe     0.673
		Geography.Regions.Europe.Southern Europe     0.587
		Geography.Regions.Europe.Western Europe      0.649
		Geography.Regions.Oceania                    0.753
		History and Society.Business and economics   0.264
		History and Society.Education                0.419
		History and Society.History                  0.306
		History and Society.Military and warfare     0.533
		History and Society.Politics and government  0.602
		History and Society.Society                  0.367
		History and Society.Transportation           0.719
		STEM.Biology                                 0.786
		STEM.Chemistry                               0.334
		STEM.Computing                               0.134
		STEM.Earth and environment                   0.535
		STEM.Engineering                             0.469
		STEM.Libraries & Information                 0.223
		STEM.Mathematics                             0.052
		STEM.Medicine & Health                       0.377
		STEM.Physics                                 0.176
		STEM.STEM*                                   0.785
		STEM.Space                                   0.751
		STEM.Technology                              0.208
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

