Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.9'
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
	counts (n=59344):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15526  -->  14154  1372   779  43039
			'Culture.Biography.Women'                       3586  -->   2498  1088   353  55405
			'Culture.Food and drink'                        1513  -->    985   528   131  57700
			'Culture.Internet culture'                      3266  -->   2754   512   198  55880
			'Culture.Linguistics'                           1643  -->   1170   473    97  57604
			'Culture.Literature'                            5570  -->   4162  1408   514  53260
			'Culture.Media.Books'                           1732  -->   1384   348   105  57507
			'Culture.Media.Entertainment'                   2340  -->   1064  1276   284  56720
			'Culture.Media.Films'                           2888  -->   2403   485   145  56311
			'Culture.Media.Media*'                         14392  -->  12706  1686  1219  43733
			'Culture.Media.Music'                           3309  -->   2800   509   246  55789
			'Culture.Media.Radio'                            330  -->    161   169    15  58999
			'Culture.Media.Software'                        2170  -->   1752   418   274  56900
			'Culture.Media.Television'                      2469  -->   1986   483   136  56739
			'Culture.Media.Video games'                     2087  -->   1941   146    48  57209
			'Culture.Performing arts'                       1491  -->    948   543   114  57739
			'Culture.Philosophy and religion'               4003  -->   2356  1647   417  54924
			'Culture.Sports'                                6230  -->   5587   643   179  52935
			'Culture.Visual arts.Architecture'              2030  -->   1416   614   250  57064
			'Culture.Visual arts.Comics and Anime'          1854  -->   1526   328    95  57395
			'Culture.Visual arts.Fashion'                    806  -->    485   321    54  58484
			'Culture.Visual arts.Visual arts*'              5379  -->   3710  1669   421  53544
			'Geography.Geographical'                        3887  -->   2579  1308   537  54920
			'Geography.Regions.Africa.Africa*'              4049  -->   2762  1287   331  54964
			'Geography.Regions.Africa.Central Africa'        880  -->    570   310    72  58392
			'Geography.Regions.Africa.Eastern Africa'        369  -->    233   136    41  58934
			'Geography.Regions.Africa.Northern Africa'      1503  -->    940   563   126  57715
			'Geography.Regions.Africa.Southern Africa'       695  -->    515   180    47  58602
			'Geography.Regions.Africa.Western Africa'        155  -->     64    91    29  59160
			'Geography.Regions.Americas.Central America'    1381  -->    789   592   102  57861
			'Geography.Regions.Americas.North America'      5628  -->   3631  1997   930  52786
			'Geography.Regions.Americas.South America'      1610  -->   1097   513   126  57608
			'Geography.Regions.Asia.Asia*'                 10749  -->   8632  2117   945  47650
			'Geography.Regions.Asia.Central Asia'           1349  -->    938   411   103  57892
			'Geography.Regions.Asia.East Asia'              3424  -->   2703   721   219  55701
			'Geography.Regions.Asia.North Asia'             1888  -->   1385   503   229  57227
			'Geography.Regions.Asia.South Asia'             1826  -->   1268   558   110  57408
			'Geography.Regions.Asia.Southeast Asia'         1601  -->    974   627   116  57627
			'Geography.Regions.Asia.West Asia'              2495  -->   1794   701   200  56649
			'Geography.Regions.Europe.Eastern Europe'       4951  -->   3665  1286   556  53837
			'Geography.Regions.Europe.Europe*'             16846  -->  13610  3236  2259  40239
			'Geography.Regions.Europe.Northern Europe'      3617  -->   2386  1231   378  55349
			'Geography.Regions.Europe.Southern Europe'      4056  -->   2998  1058   359  54929
			'Geography.Regions.Europe.Western Europe'       5217  -->   4004  1213   551  53576
			'Geography.Regions.Oceania'                     1853  -->   1310   543   121  57370
			'History and Society.Business and economics'    3192  -->   1728  1464   324  55828
			'History and Society.Education'                 1612  -->    735   877   165  57567
			'History and Society.History'                   6143  -->   3880  2263   739  52462
			'History and Society.Military and warfare'      5039  -->   3575  1464   471  53834
			'History and Society.Politics and government'   4453  -->   2632  1821   436  54455
			'History and Society.Society'                   6223  -->   2897  3326   552  52569
			'History and Society.Transportation'            4094  -->   3714   380   159  55091
			'STEM.Biology'                                  4751  -->   4126   625   137  54456
			'STEM.Chemistry'                                1620  -->   1312   308   166  57558
			'STEM.Computing'                                2449  -->   1986   463   283  56612
			'STEM.Earth and environment'                    1882  -->   1335   547   131  57331
			'STEM.Engineering'                              2505  -->   1786   719   215  56624
			'STEM.Libraries & Information'                   510  -->    289   221    38  58796
			'STEM.Mathematics'                               990  -->    785   205    63  58291
			'STEM.Medicine & Health'                        1939  -->   1405   534   160  57245
			'STEM.Physics'                                  1419  -->    958   461   166  57759
			'STEM.STEM*'                                   18523  -->  16670  1853   917  39904
			'STEM.Space'                                    2372  -->   2227   145    42  56930
			'STEM.Technology'                               4874  -->   3669  1205   597  53873
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.262         0.123
		Culture.Biography.Women                         0.06          0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.055         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.243         0.058
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.006         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.067         0.011
		Culture.Sports                                  0.105         0.071
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.031         0.002
		Culture.Visual arts.Fashion                     0.014         0.001
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
		Geography.Regions.Europe.Europe*                0.284         0.076
		Geography.Regions.Europe.Northern Europe        0.061         0.031
		Geography.Regions.Europe.Southern Europe        0.068         0.013
		Geography.Regions.Europe.Western Europe         0.088         0.019
		Geography.Regions.Oceania                       0.031         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.027         0.007
		History and Society.History                     0.104         0.011
		History and Society.Military and warfare        0.085         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.105         0.013
		History and Society.Transportation              0.069         0.015
		STEM.Biology                                    0.08          0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.042         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.312         0.069
		STEM.Space                                      0.04          0.006
		STEM.Technology                                 0.082         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.025
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.024
		History and Society.Society                  0.016
		History and Society.Transportation           0.017
		STEM.Biology                                 0.032
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.976
		History and Society.Society                  0.984
		History and Society.Transportation           0.983
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.78, macro=0.714):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.912
		Culture.Biography.Women                      0.697
		Culture.Food and drink                       0.651
		Culture.Internet culture                     0.843
		Culture.Linguistics                          0.712
		Culture.Literature                           0.747
		Culture.Media.Books                          0.799
		Culture.Media.Entertainment                  0.455
		Culture.Media.Films                          0.832
		Culture.Media.Media*                         0.883
		Culture.Media.Music                          0.846
		Culture.Media.Radio                          0.488
		Culture.Media.Software                       0.807
		Culture.Media.Television                     0.804
		Culture.Media.Video games                    0.93
		Culture.Performing arts                      0.636
		Culture.Philosophy and religion              0.589
		Culture.Sports                               0.897
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.823
		Culture.Visual arts.Fashion                  0.602
		Culture.Visual arts.Visual arts*             0.69
		Geography.Geographical                       0.663
		Geography.Regions.Africa.Africa*             0.682
		Geography.Regions.Africa.Central Africa      0.648
		Geography.Regions.Africa.Eastern Africa      0.631
		Geography.Regions.Africa.Northern Africa     0.625
		Geography.Regions.Africa.Southern Africa     0.741
		Geography.Regions.Africa.Western Africa      0.413
		Geography.Regions.Americas.Central America   0.571
		Geography.Regions.Americas.North America     0.645
		Geography.Regions.Americas.South America     0.681
		Geography.Regions.Asia.Asia*                 0.803
		Geography.Regions.Asia.Central Asia          0.695
		Geography.Regions.Asia.East Asia             0.789
		Geography.Regions.Asia.North Asia            0.734
		Geography.Regions.Asia.South Asia            0.694
		Geography.Regions.Asia.Southeast Asia        0.608
		Geography.Regions.Asia.West Asia             0.719
		Geography.Regions.Europe.Eastern Europe      0.74
		Geography.Regions.Europe.Europe*             0.808
		Geography.Regions.Europe.Northern Europe     0.66
		Geography.Regions.Europe.Southern Europe     0.739
		Geography.Regions.Europe.Western Europe      0.767
		Geography.Regions.Oceania                    0.707
		History and Society.Business and economics   0.541
		History and Society.Education                0.456
		History and Society.History                  0.632
		History and Society.Military and warfare     0.709
		History and Society.Politics and government  0.591
		History and Society.Society                  0.466
		History and Society.Transportation           0.907
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.81
		STEM.Computing                               0.811
		STEM.Earth and environment                   0.709
		STEM.Engineering                             0.713
		STEM.Libraries & Information                 0.567
		STEM.Mathematics                             0.793
		STEM.Medicine & Health                       0.725
		STEM.Physics                                 0.675
		STEM.STEM*                                   0.9
		STEM.Space                                   0.939
		STEM.Technology                              0.753
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.986
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.992
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.704, macro=0.554):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.619
		Culture.Food and drink                       0.415
		Culture.Internet culture                     0.456
		Culture.Linguistics                          0.758
		Culture.Literature                           0.552
		Culture.Media.Books                          0.639
		Culture.Media.Entertainment                  0.247
		Culture.Media.Films                          0.775
		Culture.Media.Media*                         0.669
		Culture.Media.Music                          0.825
		Culture.Media.Radio                          0.806
		Culture.Media.Software                       0.183
		Culture.Media.Television                     0.749
		Culture.Media.Video games                    0.744
		Culture.Performing arts                      0.483
		Culture.Philosophy and religion              0.457
		Culture.Sports                               0.953
		Culture.Visual arts.Architecture             0.631
		Culture.Visual arts.Comics and Anime         0.523
		Culture.Visual arts.Fashion                  0.346
		Culture.Visual arts.Visual arts*             0.622
		Geography.Geographical                       0.623
		Geography.Regions.Africa.Africa*             0.472
		Geography.Regions.Africa.Central Africa      0.249
		Geography.Regions.Africa.Eastern Africa      0.292
		Geography.Regions.Africa.Northern Africa     0.261
		Geography.Regions.Africa.Southern Africa     0.521
		Geography.Regions.Africa.Western Africa      0.366
		Geography.Regions.Americas.Central America   0.518
		Geography.Regions.Americas.North America     0.719
		Geography.Regions.Americas.South America     0.665
		Geography.Regions.Asia.Asia*                 0.663
		Geography.Regions.Asia.Central Asia          0.253
		Geography.Regions.Asia.East Asia             0.699
		Geography.Regions.Asia.North Asia            0.145
		Geography.Regions.Asia.South Asia            0.848
		Geography.Regions.Asia.Southeast Asia        0.647
		Geography.Regions.Asia.West Asia             0.693
		Geography.Regions.Europe.Eastern Europe      0.485
		Geography.Regions.Europe.Europe*             0.556
		Geography.Regions.Europe.Northern Europe     0.754
		Geography.Regions.Europe.Southern Europe     0.601
		Geography.Regions.Europe.Western Europe      0.596
		Geography.Regions.Oceania                    0.838
		History and Society.Business and economics   0.489
		History and Society.Education                0.542
		History and Society.History                  0.332
		History and Society.Military and warfare     0.539
		History and Society.Politics and government  0.683
		History and Society.Society                  0.364
		History and Society.Transportation           0.828
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.305
		STEM.Computing                               0.305
		STEM.Earth and environment                   0.586
		STEM.Engineering                             0.498
		STEM.Libraries & Information                 0.353
		STEM.Mathematics                             0.234
		STEM.Medicine & Health                       0.626
		STEM.Physics                                 0.167
		STEM.STEM*                                   0.748
		STEM.Space                                   0.885
		STEM.Technology                              0.262
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.988
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.995
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.733, macro=0.603):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.656
		Culture.Food and drink                       0.507
		Culture.Internet culture                     0.592
		Culture.Linguistics                          0.734
		Culture.Literature                           0.635
		Culture.Media.Books                          0.71
		Culture.Media.Entertainment                  0.32
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.761
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.608
		Culture.Media.Software                       0.298
		Culture.Media.Television                     0.776
		Culture.Media.Video games                    0.827
		Culture.Performing arts                      0.549
		Culture.Philosophy and religion              0.514
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.662
		Culture.Visual arts.Comics and Anime         0.64
		Culture.Visual arts.Fashion                  0.439
		Culture.Visual arts.Visual arts*             0.654
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.558
		Geography.Regions.Africa.Central Africa      0.36
		Geography.Regions.Africa.Eastern Africa      0.4
		Geography.Regions.Africa.Northern Africa     0.368
		Geography.Regions.Africa.Southern Africa     0.612
		Geography.Regions.Africa.Western Africa      0.388
		Geography.Regions.Americas.Central America   0.543
		Geography.Regions.Americas.North America     0.68
		Geography.Regions.Americas.South America     0.673
		Geography.Regions.Asia.Asia*                 0.726
		Geography.Regions.Asia.Central Asia          0.371
		Geography.Regions.Asia.East Asia             0.742
		Geography.Regions.Asia.North Asia            0.243
		Geography.Regions.Asia.South Asia            0.764
		Geography.Regions.Asia.Southeast Asia        0.627
		Geography.Regions.Asia.West Asia             0.706
		Geography.Regions.Europe.Eastern Europe      0.586
		Geography.Regions.Europe.Europe*             0.659
		Geography.Regions.Europe.Northern Europe     0.704
		Geography.Regions.Europe.Southern Europe     0.663
		Geography.Regions.Europe.Western Europe      0.671
		Geography.Regions.Oceania                    0.767
		History and Society.Business and economics   0.514
		History and Society.Education                0.495
		History and Society.History                  0.436
		History and Society.Military and warfare     0.612
		History and Society.Politics and government  0.634
		History and Society.Society                  0.409
		History and Society.Transportation           0.866
		STEM.Biology                                 0.895
		STEM.Chemistry                               0.443
		STEM.Computing                               0.444
		STEM.Earth and environment                   0.642
		STEM.Engineering                             0.586
		STEM.Libraries & Information                 0.435
		STEM.Mathematics                             0.362
		STEM.Medicine & Health                       0.672
		STEM.Physics                                 0.267
		STEM.STEM*                                   0.817
		STEM.Space                                   0.911
		STEM.Technology                              0.388
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.99
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.981
		History and Society.Society                  0.983
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.053
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.014
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.008
		History and Society.Society                  0.01
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.974, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.973
		Culture.Literature                           0.977
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.938
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.958
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.969
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.971
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.96
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.881
		Geography.Regions.Americas.Central America   0.969
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.975
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.972
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.958
		History and Society.Education                0.961
		History and Society.History                  0.961
		History and Society.Military and warfare     0.973
		History and Society.Politics and government  0.954
		History and Society.Society                  0.93
		History and Society.Transportation           0.986
		STEM.Biology                                 0.982
		STEM.Chemistry                               0.984
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.963
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.978
		STEM.Space                                   0.994
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.782, macro=0.608):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.953
		Culture.Biography.Women                      0.687
		Culture.Food and drink                       0.477
		Culture.Internet culture                     0.678
		Culture.Linguistics                          0.719
		Culture.Literature                           0.722
		Culture.Media.Books                          0.798
		Culture.Media.Entertainment                  0.226
		Culture.Media.Films                          0.844
		Culture.Media.Media*                         0.866
		Culture.Media.Music                          0.88
		Culture.Media.Radio                          0.438
		Culture.Media.Software                       0.347
		Culture.Media.Television                     0.807
		Culture.Media.Video games                    0.857
		Culture.Performing arts                      0.575
		Culture.Philosophy and religion              0.495
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.701
		Culture.Visual arts.Fashion                  0.303
		Culture.Visual arts.Visual arts*             0.667
		Geography.Geographical                       0.66
		Geography.Regions.Africa.Africa*             0.534
		Geography.Regions.Africa.Central Africa      0.266
		Geography.Regions.Africa.Eastern Africa      0.195
		Geography.Regions.Africa.Northern Africa     0.336
		Geography.Regions.Africa.Southern Africa     0.51
		Geography.Regions.Africa.Western Africa      0.24
		Geography.Regions.Americas.Central America   0.442
		Geography.Regions.Americas.North America     0.752
		Geography.Regions.Americas.South America     0.663
		Geography.Regions.Asia.Asia*                 0.794
		Geography.Regions.Asia.Central Asia          0.305
		Geography.Regions.Asia.East Asia             0.799
		Geography.Regions.Asia.North Asia            0.202
		Geography.Regions.Asia.South Asia            0.796
		Geography.Regions.Asia.Southeast Asia        0.578
		Geography.Regions.Asia.West Asia             0.73
		Geography.Regions.Europe.Eastern Europe      0.616
		Geography.Regions.Europe.Europe*             0.762
		Geography.Regions.Europe.Northern Europe     0.767
		Geography.Regions.Europe.Southern Europe     0.714
		Geography.Regions.Europe.Western Europe      0.755
		Geography.Regions.Oceania                    0.803
		History and Society.Business and economics   0.472
		History and Society.Education                0.432
		History and Society.History                  0.486
		History and Society.Military and warfare     0.668
		History and Society.Politics and government  0.662
		History and Society.Society                  0.37
		History and Society.Transportation           0.905
		STEM.Biology                                 0.931
		STEM.Chemistry                               0.544
		STEM.Computing                               0.489
		STEM.Earth and environment                   0.648
		STEM.Engineering                             0.624
		STEM.Libraries & Information                 0.22
		STEM.Mathematics                             0.389
		STEM.Medicine & Health                       0.648
		STEM.Physics                                 0.168
		STEM.STEM*                                   0.896
		STEM.Space                                   0.963
		STEM.Technology                              0.51
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

