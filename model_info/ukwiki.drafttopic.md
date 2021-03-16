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
	counts (n=60675):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15047  -->  13187  1860  1046  44582
			'Culture.Biography.Women'                       3787  -->   2710  1077   372  56516
			'Culture.Food and drink'                        1492  -->    980   512   133  59050
			'Culture.Internet culture'                      3134  -->   2344   790   238  57303
			'Culture.Linguistics'                           1563  -->    973   590   104  59008
			'Culture.Literature'                            5376  -->   3811  1565   521  54778
			'Culture.Media.Books'                           1829  -->   1349   480   158  58688
			'Culture.Media.Entertainment'                   2202  -->    826  1376   266  58207
			'Culture.Media.Films'                           2833  -->   2337   496   154  57688
			'Culture.Media.Media*'                         13658  -->  11417  2241  1406  45611
			'Culture.Media.Music'                           2761  -->   2182   579   245  57669
			'Culture.Media.Radio'                            499  -->    217   282    35  60141
			'Culture.Media.Software'                        2136  -->   1484   652   325  58214
			'Culture.Media.Television'                      1920  -->   1321   599   136  58619
			'Culture.Media.Video games'                     2022  -->   1760   262    75  58578
			'Culture.Performing arts'                       1426  -->    775   651   142  59107
			'Culture.Philosophy and religion'               3361  -->   1539  1822   324  56990
			'Culture.Sports'                                5576  -->   4908   668   196  54903
			'Culture.Visual arts.Architecture'              2128  -->   1294   834   246  58301
			'Culture.Visual arts.Comics and Anime'          1637  -->   1288   349    95  58943
			'Culture.Visual arts.Fashion'                   1147  -->    730   417    81  59447
			'Culture.Visual arts.Visual arts*'              5637  -->   3809  1828   513  54525
			'Geography.Geographical'                        4569  -->   2972  1597   584  55522
			'Geography.Regions.Africa.Africa*'              5020  -->   3470  1550   384  55271
			'Geography.Regions.Africa.Central Africa'       1151  -->    746   405    77  59447
			'Geography.Regions.Africa.Eastern Africa'        723  -->    512   211    41  59911
			'Geography.Regions.Africa.Northern Africa'      1477  -->    891   586   111  59087
			'Geography.Regions.Africa.Southern Africa'       888  -->    450   438    54  59733
			'Geography.Regions.Africa.Western Africa'        405  -->    259   146    46  60224
			'Geography.Regions.Americas.Central America'    1275  -->    728   547    70  59330
			'Geography.Regions.Americas.North America'      5496  -->   3153  2343   768  54411
			'Geography.Regions.Americas.South America'      1516  -->    946   570    96  59063
			'Geography.Regions.Asia.Asia*'                 11067  -->   8298  2769  1031  48577
			'Geography.Regions.Asia.Central Asia'           1347  -->    882   465    91  59237
			'Geography.Regions.Asia.East Asia'              2898  -->   2064   834   207  57570
			'Geography.Regions.Asia.North Asia'             2174  -->   1309   865   398  58103
			'Geography.Regions.Asia.South Asia'             1757  -->   1234   523   111  58807
			'Geography.Regions.Asia.Southeast Asia'         1527  -->    894   633   105  59043
			'Geography.Regions.Asia.West Asia'              2609  -->   1773   836   151  57915
			'Geography.Regions.Europe.Eastern Europe'       5286  -->   3688  1598   658  54731
			'Geography.Regions.Europe.Europe*'             16134  -->  12081  4053  2231  42310
			'Geography.Regions.Europe.Northern Europe'      3536  -->   2041  1495   376  56763
			'Geography.Regions.Europe.Southern Europe'      3671  -->   2416  1255   335  56669
			'Geography.Regions.Europe.Western Europe'       4351  -->   2976  1375   462  55862
			'Geography.Regions.Oceania'                     1744  -->   1072   672   127  58804
			'History and Society.Business and economics'    3724  -->   1985  1739   453  56498
			'History and Society.Education'                 1696  -->    783   913   142  58837
			'History and Society.History'                   5257  -->   2649  2608   721  54697
			'History and Society.Military and warfare'      5345  -->   3283  2062   623  54707
			'History and Society.Politics and government'   4130  -->   1886  2244   428  56117
			'History and Society.Society'                   6450  -->   2644  3806   771  53454
			'History and Society.Transportation'            3557  -->   2979   578   183  56935
			'STEM.Biology'                                  3542  -->   2742   800   202  56931
			'STEM.Chemistry'                                1468  -->    966   502   202  59005
			'STEM.Computing'                                2664  -->   1921   743   435  57576
			'STEM.Earth and environment'                    1828  -->   1020   808   161  58686
			'STEM.Engineering'                              3048  -->   2194   854   233  57394
			'STEM.Libraries & Information'                  1050  -->    661   389    78  59547
			'STEM.Mathematics'                              1186  -->    792   394   115  59374
			'STEM.Medicine & Health'                        1812  -->   1099   713   163  58700
			'STEM.Physics'                                  1475  -->    859   616   171  59029
			'STEM.STEM*'                                   18294  -->  15827  2467  1278  41103
			'STEM.Space'                                    1812  -->   1514   298    65  58798
			'STEM.Technology'                               4710  -->   2957  1753   702  55263
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.248         0.123
		Culture.Biography.Women                         0.062         0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.052         0.003
		Culture.Linguistics                             0.026         0.007
		Culture.Literature                              0.089         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.036         0.004
		Culture.Media.Films                             0.047         0.011
		Culture.Media.Media*                            0.225         0.058
		Culture.Media.Music                             0.046         0.024
		Culture.Media.Radio                             0.008         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.055         0.011
		Culture.Sports                                  0.092         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.075         0.024
		Geography.Regions.Africa.Africa*                0.083         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.012         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.015         0.001
		Geography.Regions.Africa.Western Africa         0.007         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.091         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.182         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.048         0.011
		Geography.Regions.Asia.North Asia               0.036         0.001
		Geography.Regions.Asia.South Asia               0.029         0.015
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.043         0.011
		Geography.Regions.Europe.Eastern Europe         0.087         0.013
		Geography.Regions.Europe.Europe*                0.266         0.076
		Geography.Regions.Europe.Northern Europe        0.058         0.031
		Geography.Regions.Europe.Southern Europe        0.061         0.013
		Geography.Regions.Europe.Western Europe         0.072         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.061         0.01
		History and Society.Education                   0.028         0.007
		History and Society.History                     0.087         0.011
		History and Society.Military and warfare        0.088         0.014
		History and Society.Politics and government     0.068         0.028
		History and Society.Society                     0.106         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.058         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.044         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.017         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.302         0.069
		STEM.Space                                      0.03          0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.05
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.103
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.02
		History and Society.Society                  0.019
		History and Society.Transportation           0.016
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.088
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.897
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.98
		History and Society.Society                  0.981
		History and Society.Transportation           0.984
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.912
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.727, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.716
		Culture.Food and drink                       0.657
		Culture.Internet culture                     0.748
		Culture.Linguistics                          0.623
		Culture.Literature                           0.709
		Culture.Media.Books                          0.738
		Culture.Media.Entertainment                  0.375
		Culture.Media.Films                          0.825
		Culture.Media.Media*                         0.836
		Culture.Media.Music                          0.79
		Culture.Media.Radio                          0.435
		Culture.Media.Software                       0.695
		Culture.Media.Television                     0.688
		Culture.Media.Video games                    0.87
		Culture.Performing arts                      0.543
		Culture.Philosophy and religion              0.458
		Culture.Sports                               0.88
		Culture.Visual arts.Architecture             0.608
		Culture.Visual arts.Comics and Anime         0.787
		Culture.Visual arts.Fashion                  0.636
		Culture.Visual arts.Visual arts*             0.676
		Geography.Geographical                       0.65
		Geography.Regions.Africa.Africa*             0.691
		Geography.Regions.Africa.Central Africa      0.648
		Geography.Regions.Africa.Eastern Africa      0.708
		Geography.Regions.Africa.Northern Africa     0.603
		Geography.Regions.Africa.Southern Africa     0.507
		Geography.Regions.Africa.Western Africa      0.64
		Geography.Regions.Americas.Central America   0.571
		Geography.Regions.Americas.North America     0.574
		Geography.Regions.Americas.South America     0.624
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.655
		Geography.Regions.Asia.East Asia             0.712
		Geography.Regions.Asia.North Asia            0.602
		Geography.Regions.Asia.South Asia            0.702
		Geography.Regions.Asia.Southeast Asia        0.585
		Geography.Regions.Asia.West Asia             0.68
		Geography.Regions.Europe.Eastern Europe      0.698
		Geography.Regions.Europe.Europe*             0.749
		Geography.Regions.Europe.Northern Europe     0.577
		Geography.Regions.Europe.Southern Europe     0.658
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.615
		History and Society.Business and economics   0.533
		History and Society.Education                0.462
		History and Society.History                  0.504
		History and Society.Military and warfare     0.614
		History and Society.Politics and government  0.457
		History and Society.Society                  0.41
		History and Society.Transportation           0.838
		STEM.Biology                                 0.774
		STEM.Chemistry                               0.658
		STEM.Computing                               0.721
		STEM.Earth and environment                   0.558
		STEM.Engineering                             0.72
		STEM.Libraries & Information                 0.63
		STEM.Mathematics                             0.668
		STEM.Medicine & Health                       0.607
		STEM.Physics                                 0.582
		STEM.STEM*                                   0.865
		STEM.Space                                   0.836
		STEM.Technology                              0.628
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.992
		History and Society.Society                  0.986
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.679, macro=0.521):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.843
		Culture.Biography.Women                      0.618
		Culture.Food and drink                       0.419
		Culture.Internet culture                     0.388
		Culture.Linguistics                          0.723
		Culture.Literature                           0.542
		Culture.Media.Books                          0.526
		Culture.Media.Entertainment                  0.229
		Culture.Media.Films                          0.767
		Culture.Media.Media*                         0.635
		Culture.Media.Music                          0.821
		Culture.Media.Radio                          0.617
		Culture.Media.Software                       0.143
		Culture.Media.Television                     0.725
		Culture.Media.Video games                    0.641
		Culture.Performing arts                      0.396
		Culture.Philosophy and religion              0.466
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.607
		Culture.Visual arts.Comics and Anime         0.518
		Culture.Visual arts.Fashion                  0.275
		Culture.Visual arts.Visual arts*             0.575
		Geography.Geographical                       0.601
		Geography.Regions.Africa.Africa*             0.44
		Geography.Regions.Africa.Central Africa      0.24
		Geography.Regions.Africa.Eastern Africa      0.32
		Geography.Regions.Africa.Northern Africa     0.283
		Geography.Regions.Africa.Southern Africa     0.398
		Geography.Regions.Africa.Western Africa      0.364
		Geography.Regions.Americas.Central America   0.616
		Geography.Regions.Americas.North America     0.739
		Geography.Regions.Americas.South America     0.709
		Geography.Regions.Asia.Asia*                 0.632
		Geography.Regions.Asia.Central Asia          0.27
		Geography.Regions.Asia.East Asia             0.696
		Geography.Regions.Asia.North Asia            0.076
		Geography.Regions.Asia.South Asia            0.852
		Geography.Regions.Asia.Southeast Asia        0.666
		Geography.Regions.Asia.West Asia             0.742
		Geography.Regions.Europe.Eastern Europe      0.433
		Geography.Regions.Europe.Europe*             0.552
		Geography.Regions.Europe.Northern Europe     0.735
		Geography.Regions.Europe.Southern Europe     0.597
		Geography.Regions.Europe.Western Europe      0.62
		Geography.Regions.Oceania                    0.814
		History and Society.Business and economics   0.406
		History and Society.Education                0.587
		History and Society.History                  0.298
		History and Society.Military and warfare     0.438
		History and Society.Politics and government  0.636
		History and Society.Society                  0.269
		History and Society.Transportation           0.8
		STEM.Biology                                 0.884
		STEM.Chemistry                               0.231
		STEM.Computing                               0.206
		STEM.Earth and environment                   0.482
		STEM.Engineering                             0.484
		STEM.Libraries & Information                 0.23
		STEM.Mathematics                             0.126
		STEM.Medicine & Health                       0.585
		STEM.Physics                                 0.146
		STEM.STEM*                                   0.681
		STEM.Space                                   0.821
		STEM.Technology                              0.205
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
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
		Geography.Regions.Europe.Europe*             0.979
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.693, macro=0.557):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.859
		Culture.Biography.Women                      0.663
		Culture.Food and drink                       0.512
		Culture.Internet culture                     0.511
		Culture.Linguistics                          0.669
		Culture.Literature                           0.614
		Culture.Media.Books                          0.614
		Culture.Media.Entertainment                  0.284
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.721
		Culture.Media.Music                          0.805
		Culture.Media.Radio                          0.51
		Culture.Media.Software                       0.237
		Culture.Media.Television                     0.706
		Culture.Media.Video games                    0.738
		Culture.Performing arts                      0.458
		Culture.Philosophy and religion              0.462
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.608
		Culture.Visual arts.Comics and Anime         0.625
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.621
		Geography.Geographical                       0.625
		Geography.Regions.Africa.Africa*             0.538
		Geography.Regions.Africa.Central Africa      0.351
		Geography.Regions.Africa.Eastern Africa      0.441
		Geography.Regions.Africa.Northern Africa     0.386
		Geography.Regions.Africa.Southern Africa     0.446
		Geography.Regions.Africa.Western Africa      0.464
		Geography.Regions.Americas.Central America   0.593
		Geography.Regions.Americas.North America     0.646
		Geography.Regions.Americas.South America     0.664
		Geography.Regions.Asia.Asia*                 0.686
		Geography.Regions.Asia.Central Asia          0.382
		Geography.Regions.Asia.East Asia             0.704
		Geography.Regions.Asia.North Asia            0.134
		Geography.Regions.Asia.South Asia            0.77
		Geography.Regions.Asia.Southeast Asia        0.623
		Geography.Regions.Asia.West Asia             0.71
		Geography.Regions.Europe.Eastern Europe      0.534
		Geography.Regions.Europe.Europe*             0.636
		Geography.Regions.Europe.Northern Europe     0.646
		Geography.Regions.Europe.Southern Europe     0.626
		Geography.Regions.Europe.Western Europe      0.65
		Geography.Regions.Oceania                    0.7
		History and Society.Business and economics   0.461
		History and Society.Education                0.517
		History and Society.History                  0.374
		History and Society.Military and warfare     0.511
		History and Society.Politics and government  0.532
		History and Society.Society                  0.325
		History and Society.Transportation           0.818
		STEM.Biology                                 0.825
		STEM.Chemistry                               0.342
		STEM.Computing                               0.32
		STEM.Earth and environment                   0.517
		STEM.Engineering                             0.579
		STEM.Libraries & Information                 0.337
		STEM.Mathematics                             0.212
		STEM.Medicine & Health                       0.596
		STEM.Physics                                 0.234
		STEM.STEM*                                   0.762
		STEM.Space                                   0.828
		STEM.Technology                              0.309
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
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
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.988
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.977
		History and Society.Society                  0.979
		History and Society.Transportation           0.994
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.023
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.021
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.05
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.008
		History and Society.Society                  0.014
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.972
		Culture.Internet culture                     0.977
		Culture.Linguistics                          0.967
		Culture.Literature                           0.972
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.956
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.952
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.983
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.939
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.96
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.962
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.973
		Geography.Regions.Africa.Northern Africa     0.966
		Geography.Regions.Africa.Southern Africa     0.946
		Geography.Regions.Africa.Western Africa      0.969
		Geography.Regions.Americas.Central America   0.963
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.973
		Geography.Regions.Asia.East Asia             0.969
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.959
		Geography.Regions.Asia.West Asia             0.967
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.943
		Geography.Regions.Europe.Northern Europe     0.956
		Geography.Regions.Europe.Southern Europe     0.966
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.962
		History and Society.Business and economics   0.952
		History and Society.Education                0.957
		History and Society.History                  0.941
		History and Society.Military and warfare     0.955
		History and Society.Politics and government  0.931
		History and Society.Society                  0.9
		History and Society.Transportation           0.981
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.976
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.963
		STEM.Engineering                             0.972
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.973
		STEM.Medicine & Health                       0.961
		STEM.Physics                                 0.974
		STEM.STEM*                                   0.97
		STEM.Space                                   0.985
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.734, macro=0.554):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.916
		Culture.Biography.Women                      0.634
		Culture.Food and drink                       0.476
		Culture.Internet culture                     0.595
		Culture.Linguistics                          0.619
		Culture.Literature                           0.67
		Culture.Media.Books                          0.666
		Culture.Media.Entertainment                  0.202
		Culture.Media.Films                          0.79
		Culture.Media.Media*                         0.819
		Culture.Media.Music                          0.822
		Culture.Media.Radio                          0.343
		Culture.Media.Software                       0.228
		Culture.Media.Television                     0.748
		Culture.Media.Video games                    0.793
		Culture.Performing arts                      0.392
		Culture.Philosophy and religion              0.408
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.671
		Culture.Visual arts.Fashion                  0.288
		Culture.Visual arts.Visual arts*             0.655
		Geography.Geographical                       0.663
		Geography.Regions.Africa.Africa*             0.531
		Geography.Regions.Africa.Central Africa      0.26
		Geography.Regions.Africa.Eastern Africa      0.313
		Geography.Regions.Africa.Northern Africa     0.307
		Geography.Regions.Africa.Southern Africa     0.337
		Geography.Regions.Africa.Western Africa      0.291
		Geography.Regions.Americas.Central America   0.554
		Geography.Regions.Americas.North America     0.713
		Geography.Regions.Americas.South America     0.676
		Geography.Regions.Asia.Asia*                 0.757
		Geography.Regions.Asia.Central Asia          0.367
		Geography.Regions.Asia.East Asia             0.745
		Geography.Regions.Asia.North Asia            0.112
		Geography.Regions.Asia.South Asia            0.819
		Geography.Regions.Asia.Southeast Asia        0.583
		Geography.Regions.Asia.West Asia             0.735
		Geography.Regions.Europe.Eastern Europe      0.621
		Geography.Regions.Europe.Europe*             0.721
		Geography.Regions.Europe.Northern Europe     0.684
		Geography.Regions.Europe.Southern Europe     0.667
		Geography.Regions.Europe.Western Europe      0.699
		Geography.Regions.Oceania                    0.727
		History and Society.Business and economics   0.392
		History and Society.Education                0.483
		History and Society.History                  0.335
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.534
		History and Society.Society                  0.254
		History and Society.Transportation           0.83
		STEM.Biology                                 0.858
		STEM.Chemistry                               0.291
		STEM.Computing                               0.33
		STEM.Earth and environment                   0.453
		STEM.Engineering                             0.584
		STEM.Libraries & Information                 0.29
		STEM.Mathematics                             0.283
		STEM.Medicine & Health                       0.592
		STEM.Physics                                 0.14
		STEM.STEM*                                   0.857
		STEM.Space                                   0.865
		STEM.Technology                              0.331
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

