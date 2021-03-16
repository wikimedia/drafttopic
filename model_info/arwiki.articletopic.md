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
	counts (n=63509):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 27100  -->  26011  1089   866  35543
			'Culture.Biography.Women'                       6315  -->   4670  1645   906  56288
			'Culture.Food and drink'                        1386  -->    871   515   106  62017
			'Culture.Internet culture'                      3384  -->   2728   656   204  59921
			'Culture.Linguistics'                           1445  -->    946   499    88  61976
			'Culture.Literature'                            5803  -->   4203  1600   524  57182
			'Culture.Media.Books'                           1554  -->   1145   409   109  61846
			'Culture.Media.Entertainment'                   2113  -->    992  1121   219  61177
			'Culture.Media.Films'                           2128  -->   1691   437   100  61281
			'Culture.Media.Media*'                         14066  -->  11727  2339  1576  47867
			'Culture.Media.Music'                           2797  -->   2087   710   297  60415
			'Culture.Media.Radio'                           1137  -->    504   633    99  62273
			'Culture.Media.Software'                        2101  -->   1508   593   328  61080
			'Culture.Media.Television'                      2253  -->   1251  1002   207  61049
			'Culture.Media.Video games'                     2193  -->   1966   227    51  61265
			'Culture.Performing arts'                       1484  -->    737   747   145  61880
			'Culture.Philosophy and religion'               3448  -->   1665  1783   334  59727
			'Culture.Sports'                                8610  -->   7875   735   338  54561
			'Culture.Visual arts.Architecture'              1861  -->   1213   648   179  61469
			'Culture.Visual arts.Comics and Anime'          1848  -->   1458   390    97  61564
			'Culture.Visual arts.Fashion'                   1317  -->    932   385   107  62085
			'Culture.Visual arts.Visual arts*'              5874  -->   4185  1689   432  57203
			'Geography.Geographical'                        3642  -->   2581  1061   353  59514
			'Geography.Regions.Africa.Africa*'              6510  -->   5198  1312   460  56539
			'Geography.Regions.Africa.Central Africa'       1122  -->    798   324    61  62326
			'Geography.Regions.Africa.Eastern Africa'        973  -->    656   317    53  62483
			'Geography.Regions.Africa.Northern Africa'      2129  -->   1557   572   216  61164
			'Geography.Regions.Africa.Southern Africa'      1197  -->    893   304    51  62261
			'Geography.Regions.Africa.Western Africa'        756  -->    559   197    34  62719
			'Geography.Regions.Americas.Central America'    1367  -->    838   529    77  62065
			'Geography.Regions.Americas.North America'      8359  -->   5642  2717  2167  52983
			'Geography.Regions.Americas.South America'      1696  -->   1246   450   127  61686
			'Geography.Regions.Asia.Asia*'                 12021  -->  10051  1970   907  50581
			'Geography.Regions.Asia.Central Asia'           1198  -->    871   327    71  62240
			'Geography.Regions.Asia.East Asia'              2922  -->   2090   832   256  60331
			'Geography.Regions.Asia.North Asia'             1515  -->   1042   473   196  61798
			'Geography.Regions.Asia.South Asia'             1955  -->   1479   476    57  61497
			'Geography.Regions.Asia.Southeast Asia'         1549  -->   1135   414    71  61889
			'Geography.Regions.Asia.West Asia'              4115  -->   3342   773   278  59116
			'Geography.Regions.Europe.Eastern Europe'       2860  -->   2102   758   249  60400
			'Geography.Regions.Europe.Europe*'             13100  -->  10295  2805  1958  48451
			'Geography.Regions.Europe.Northern Europe'      4039  -->   2595  1444   657  58813
			'Geography.Regions.Europe.Southern Europe'      2863  -->   2036   827   305  60341
			'Geography.Regions.Europe.Western Europe'       4084  -->   3030  1054   558  58867
			'Geography.Regions.Oceania'                     2283  -->   1828   455    72  61154
			'History and Society.Business and economics'    3611  -->   2003  1608   473  59425
			'History and Society.Education'                 2059  -->    871  1188   173  61277
			'History and Society.History'                   4740  -->   2045  2695   685  58084
			'History and Society.Military and warfare'      4742  -->   3237  1505   462  58305
			'History and Society.Politics and government'   5471  -->   3283  2188   641  57397
			'History and Society.Society'                   6099  -->   2506  3593   533  56877
			'History and Society.Transportation'            3249  -->   2753   496   160  60100
			'STEM.Biology'                                  3025  -->   2276   749   203  60281
			'STEM.Chemistry'                                1516  -->   1103   413   157  61836
			'STEM.Computing'                                2434  -->   1773   661   352  60723
			'STEM.Earth and environment'                    1702  -->    983   719   165  61642
			'STEM.Engineering'                              2883  -->   2045   838   241  60385
			'STEM.Libraries & Information'                  1186  -->    797   389    52  62271
			'STEM.Mathematics'                              1176  -->    777   399    69  62264
			'STEM.Medicine & Health'                        2280  -->   1548   732   221  61008
			'STEM.Physics'                                  1470  -->    948   522   194  61845
			'STEM.STEM*'                                   18041  -->  15679  2362  1126  44342
			'STEM.Space'                                    1751  -->   1519   232    64  61694
			'STEM.Technology'                               4518  -->   3026  1492   649  58342
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.427         0.123
		Culture.Biography.Women                         0.099         0.015
		Culture.Food and drink                          0.022         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.023         0.007
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.034         0.011
		Culture.Media.Media*                            0.221         0.058
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.033         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.136         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.029         0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.092         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.103         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0
		Geography.Regions.Africa.Northern Africa        0.034         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.132         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.189         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.024         0.006
		Geography.Regions.Asia.West Asia                0.065         0.011
		Geography.Regions.Europe.Eastern Europe         0.045         0.013
		Geography.Regions.Europe.Europe*                0.206         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.064         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.057         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.075         0.014
		History and Society.Politics and government     0.086         0.028
		History and Society.Society                     0.096         0.013
		History and Society.Transportation              0.051         0.015
		STEM.Biology                                    0.048         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.038         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.284         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.071         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.139
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.071
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.08
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.013
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.096
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.028
		History and Society.Society                  0.014
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.92
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.987
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.904
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.972
		History and Society.Society                  0.986
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.772, macro=0.7):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.74
		Culture.Food and drink                       0.628
		Culture.Internet culture                     0.806
		Culture.Linguistics                          0.655
		Culture.Literature                           0.724
		Culture.Media.Books                          0.737
		Culture.Media.Entertainment                  0.469
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.834
		Culture.Media.Music                          0.746
		Culture.Media.Radio                          0.443
		Culture.Media.Software                       0.718
		Culture.Media.Television                     0.555
		Culture.Media.Video games                    0.896
		Culture.Performing arts                      0.497
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.652
		Culture.Visual arts.Comics and Anime         0.789
		Culture.Visual arts.Fashion                  0.708
		Culture.Visual arts.Visual arts*             0.712
		Geography.Geographical                       0.709
		Geography.Regions.Africa.Africa*             0.798
		Geography.Regions.Africa.Central Africa      0.711
		Geography.Regions.Africa.Eastern Africa      0.674
		Geography.Regions.Africa.Northern Africa     0.731
		Geography.Regions.Africa.Southern Africa     0.746
		Geography.Regions.Africa.Western Africa      0.739
		Geography.Regions.Americas.Central America   0.613
		Geography.Regions.Americas.North America     0.675
		Geography.Regions.Americas.South America     0.735
		Geography.Regions.Asia.Asia*                 0.836
		Geography.Regions.Asia.Central Asia          0.727
		Geography.Regions.Asia.East Asia             0.715
		Geography.Regions.Asia.North Asia            0.688
		Geography.Regions.Asia.South Asia            0.757
		Geography.Regions.Asia.Southeast Asia        0.733
		Geography.Regions.Asia.West Asia             0.812
		Geography.Regions.Europe.Eastern Europe      0.735
		Geography.Regions.Europe.Europe*             0.786
		Geography.Regions.Europe.Northern Europe     0.642
		Geography.Regions.Europe.Southern Europe     0.711
		Geography.Regions.Europe.Western Europe      0.742
		Geography.Regions.Oceania                    0.801
		History and Society.Business and economics   0.555
		History and Society.Education                0.423
		History and Society.History                  0.431
		History and Society.Military and warfare     0.683
		History and Society.Politics and government  0.6
		History and Society.Society                  0.411
		History and Society.Transportation           0.847
		STEM.Biology                                 0.752
		STEM.Chemistry                               0.728
		STEM.Computing                               0.728
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.709
		STEM.Libraries & Information                 0.672
		STEM.Mathematics                             0.661
		STEM.Medicine & Health                       0.679
		STEM.Physics                                 0.645
		STEM.STEM*                                   0.869
		STEM.Space                                   0.868
		STEM.Technology                              0.67
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.684, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.85
		Culture.Biography.Women                      0.408
		Culture.Food and drink                       0.476
		Culture.Internet culture                     0.455
		Culture.Linguistics                          0.773
		Culture.Literature                           0.557
		Culture.Media.Books                          0.629
		Culture.Media.Entertainment                  0.321
		Culture.Media.Films                          0.838
		Culture.Media.Media*                         0.619
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.376
		Culture.Media.Software                       0.152
		Culture.Media.Television                     0.594
		Culture.Media.Video games                    0.738
		Culture.Performing arts                      0.381
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.525
		Culture.Visual arts.Fashion                  0.25
		Culture.Visual arts.Visual arts*             0.639
		Geography.Geographical                       0.744
		Geography.Regions.Africa.Africa*             0.437
		Geography.Regions.Africa.Central Africa      0.315
		Geography.Regions.Africa.Eastern Africa      0.266
		Geography.Regions.Africa.Northern Africa     0.203
		Geography.Regions.Africa.Southern Africa     0.517
		Geography.Regions.Africa.Western Africa      0.483
		Geography.Regions.Americas.Central America   0.621
		Geography.Regions.Americas.North America     0.541
		Geography.Regions.Americas.South America     0.694
		Geography.Regions.Asia.Asia*                 0.693
		Geography.Regions.Asia.Central Asia          0.356
		Geography.Regions.Asia.East Asia             0.661
		Geography.Regions.Asia.North Asia            0.167
		Geography.Regions.Asia.South Asia            0.926
		Geography.Regions.Asia.Southeast Asia        0.794
		Geography.Regions.Asia.West Asia             0.657
		Geography.Regions.Europe.Eastern Europe      0.699
		Geography.Regions.Europe.Europe*             0.625
		Geography.Regions.Europe.Northern Europe     0.647
		Geography.Regions.Europe.Southern Europe     0.651
		Geography.Regions.Europe.Western Europe      0.607
		Geography.Regions.Oceania                    0.913
		History and Society.Business and economics   0.417
		History and Society.Education                0.527
		History and Society.History                  0.288
		History and Society.Military and warfare     0.553
		History and Society.Politics and government  0.612
		History and Society.Society                  0.361
		History and Society.Transportation           0.83
		STEM.Biology                                 0.886
		STEM.Chemistry                               0.31
		STEM.Computing                               0.254
		STEM.Earth and environment                   0.496
		STEM.Engineering                             0.484
		STEM.Libraries & Information                 0.334
		STEM.Mathematics                             0.199
		STEM.Medicine & Health                       0.548
		STEM.Physics                                 0.149
		STEM.STEM*                                   0.723
		STEM.Space                                   0.835
		STEM.Technology                              0.239
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.994
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.991
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
	f1 (micro=0.72, macro=0.591):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.902
		Culture.Biography.Women                      0.526
		Culture.Food and drink                       0.542
		Culture.Internet culture                     0.582
		Culture.Linguistics                          0.709
		Culture.Literature                           0.629
		Culture.Media.Books                          0.678
		Culture.Media.Entertainment                  0.381
		Culture.Media.Films                          0.816
		Culture.Media.Media*                         0.71
		Culture.Media.Music                          0.767
		Culture.Media.Radio                          0.407
		Culture.Media.Software                       0.25
		Culture.Media.Television                     0.574
		Culture.Media.Video games                    0.81
		Culture.Performing arts                      0.431
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.678
		Culture.Visual arts.Comics and Anime         0.63
		Culture.Visual arts.Fashion                  0.369
		Culture.Visual arts.Visual arts*             0.674
		Geography.Geographical                       0.726
		Geography.Regions.Africa.Africa*             0.565
		Geography.Regions.Africa.Central Africa      0.437
		Geography.Regions.Africa.Eastern Africa      0.381
		Geography.Regions.Africa.Northern Africa     0.318
		Geography.Regions.Africa.Southern Africa     0.611
		Geography.Regions.Africa.Western Africa      0.584
		Geography.Regions.Americas.Central America   0.617
		Geography.Regions.Americas.North America     0.601
		Geography.Regions.Americas.South America     0.714
		Geography.Regions.Asia.Asia*                 0.758
		Geography.Regions.Asia.Central Asia          0.478
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.269
		Geography.Regions.Asia.South Asia            0.833
		Geography.Regions.Asia.Southeast Asia        0.762
		Geography.Regions.Asia.West Asia             0.726
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.696
		Geography.Regions.Europe.Northern Europe     0.645
		Geography.Regions.Europe.Southern Europe     0.68
		Geography.Regions.Europe.Western Europe      0.668
		Geography.Regions.Oceania                    0.853
		History and Society.Business and economics   0.476
		History and Society.Education                0.469
		History and Society.History                  0.346
		History and Society.Military and warfare     0.611
		History and Society.Politics and government  0.606
		History and Society.Society                  0.384
		History and Society.Transportation           0.839
		STEM.Biology                                 0.814
		STEM.Chemistry                               0.434
		STEM.Computing                               0.377
		STEM.Earth and environment                   0.534
		STEM.Engineering                             0.576
		STEM.Libraries & Information                 0.446
		STEM.Mathematics                             0.306
		STEM.Medicine & Health                       0.606
		STEM.Physics                                 0.242
		STEM.STEM*                                   0.789
		STEM.Space                                   0.851
		STEM.Technology                              0.352
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.978
		History and Society.Society                  0.983
		History and Society.Transportation           0.995
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.039
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.039
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.011
		History and Society.Society                  0.009
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.968
		Culture.Literature                           0.972
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.966
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.943
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.969
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.977
		Geography.Regions.Africa.Central Africa      0.979
		Geography.Regions.Africa.Eastern Africa      0.976
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.977
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.972
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.976
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.982
		Geography.Regions.Asia.South Asia            0.978
		Geography.Regions.Asia.Southeast Asia        0.977
		Geography.Regions.Asia.West Asia             0.98
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.967
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.958
		History and Society.Education                0.953
		History and Society.History                  0.937
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.951
		History and Society.Society                  0.912
		History and Society.Transportation           0.982
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.987
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.967
		STEM.Engineering                             0.975
		STEM.Libraries & Information                 0.97
		STEM.Mathematics                             0.974
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.975
		STEM.Space                                   0.99
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.758, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.475
		Culture.Food and drink                       0.503
		Culture.Internet culture                     0.72
		Culture.Linguistics                          0.706
		Culture.Literature                           0.691
		Culture.Media.Books                          0.662
		Culture.Media.Entertainment                  0.359
		Culture.Media.Films                          0.848
		Culture.Media.Media*                         0.801
		Culture.Media.Music                          0.81
		Culture.Media.Radio                          0.298
		Culture.Media.Software                       0.231
		Culture.Media.Television                     0.594
		Culture.Media.Video games                    0.9
		Culture.Performing arts                      0.403
		Culture.Philosophy and religion              0.411
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.732
		Culture.Visual arts.Comics and Anime         0.59
		Culture.Visual arts.Fashion                  0.3
		Culture.Visual arts.Visual arts*             0.717
		Geography.Geographical                       0.777
		Geography.Regions.Africa.Africa*             0.559
		Geography.Regions.Africa.Central Africa      0.281
		Geography.Regions.Africa.Eastern Africa      0.292
		Geography.Regions.Africa.Northern Africa     0.265
		Geography.Regions.Africa.Southern Africa     0.489
		Geography.Regions.Africa.Western Africa      0.49
		Geography.Regions.Americas.Central America   0.556
		Geography.Regions.Americas.North America     0.623
		Geography.Regions.Americas.South America     0.67
		Geography.Regions.Asia.Asia*                 0.831
		Geography.Regions.Asia.Central Asia          0.439
		Geography.Regions.Asia.East Asia             0.699
		Geography.Regions.Asia.North Asia            0.23
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.773
		Geography.Regions.Asia.West Asia             0.804
		Geography.Regions.Europe.Eastern Europe      0.745
		Geography.Regions.Europe.Europe*             0.753
		Geography.Regions.Europe.Northern Europe     0.677
		Geography.Regions.Europe.Southern Europe     0.698
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.861
		History and Society.Business and economics   0.445
		History and Society.Education                0.419
		History and Society.History                  0.295
		History and Society.Military and warfare     0.677
		History and Society.Politics and government  0.625
		History and Society.Society                  0.329
		History and Society.Transportation           0.87
		STEM.Biology                                 0.857
		STEM.Chemistry                               0.561
		STEM.Computing                               0.336
		STEM.Earth and environment                   0.486
		STEM.Engineering                             0.633
		STEM.Libraries & Information                 0.445
		STEM.Mathematics                             0.349
		STEM.Medicine & Health                       0.641
		STEM.Physics                                 0.227
		STEM.STEM*                                   0.89
		STEM.Space                                   0.91
		STEM.Technology                              0.395
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

