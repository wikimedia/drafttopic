Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'random_state': None, 'max_features': 'log2', 'presort': 'auto', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_weight_fraction_leaf': 0.0, 'center': False, 'n_iter_no_change': None, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'scale': False, 'population_rates': None, 'n_estimators': 150, 'subsample': 1.0, 'label_weights': {}, 'min_impurity_split': None, 'min_samples_split': 2, 'loss': 'deviance', 'max_leaf_nodes': None, 'verbose': 0, 'warm_start': False, 'min_samples_leaf': 1, 'multilabel': True, 'criterion': 'friedman_mse', 'learning_rate': 0.1, 'init': None, 'max_depth': 5, 'tol': 0.0001}
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
	counts (n=60646):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14308  -->  12928  1380   789  45549
			'Culture.Biography.Women'                       5088  -->   4071  1017   797  54761
			'Culture.Food and drink'                        1396  -->    992   404   121  59129
			'Culture.Internet culture'                      3603  -->   2958   645   243  56800
			'Culture.Linguistics'                           1507  -->   1167   340    77  59062
			'Culture.Literature'                            5561  -->   4342  1219   510  54575
			'Culture.Media.Books'                           1441  -->   1063   378   128  59077
			'Culture.Media.Entertainment'                   1929  -->   1014   915   178  58539
			'Culture.Media.Films'                           2614  -->   2094   520   161  57871
			'Culture.Media.Media*'                         13178  -->  11589  1589  1316  46152
			'Culture.Media.Music'                           2804  -->   2362   442   206  57636
			'Culture.Media.Radio'                            285  -->    176   109    28  60333
			'Culture.Media.Software'                        2207  -->   1795   412   289  58150
			'Culture.Media.Television'                      2018  -->   1437   581   143  58485
			'Culture.Media.Video games'                     2249  -->   2069   180    61  58336
			'Culture.Performing arts'                       1347  -->    907   440   118  59181
			'Culture.Philosophy and religion'               3005  -->   1684  1321   256  57385
			'Culture.Sports'                                4062  -->   3573   489   121  56463
			'Culture.Visual arts.Architecture'              1846  -->   1302   544   180  58620
			'Culture.Visual arts.Comics and Anime'          2304  -->   2072   232    80  58262
			'Culture.Visual arts.Fashion'                   1508  -->   1271   237    87  59051
			'Culture.Visual arts.Visual arts*'              6164  -->   4767  1397   417  54065
			'Geography.Geographical'                        3924  -->   2580  1344   508  56214
			'Geography.Regions.Africa.Africa*'              5698  -->   4434  1264   474  54474
			'Geography.Regions.Africa.Central Africa'       1206  -->    790   416   128  59312
			'Geography.Regions.Africa.Eastern Africa'        432  -->    194   238    44  60170
			'Geography.Regions.Africa.Northern Africa'      1460  -->   1021   439   103  59083
			'Geography.Regions.Africa.Southern Africa'      1181  -->    806   375    73  59392
			'Geography.Regions.Africa.Western Africa'        675  -->    543   132    48  59923
			'Geography.Regions.Americas.Central America'    1628  -->   1054   574   110  58908
			'Geography.Regions.Americas.North America'      5263  -->   3611  1652   629  54754
			'Geography.Regions.Americas.South America'      2183  -->   1661   522   183  58280
			'Geography.Regions.Asia.Asia*'                 14557  -->  12287  2270  1139  44950
			'Geography.Regions.Asia.Central Asia'           1081  -->    778   303    87  59478
			'Geography.Regions.Asia.East Asia'              5678  -->   4604  1074   472  54496
			'Geography.Regions.Asia.North Asia'             2532  -->   1889   643   203  57911
			'Geography.Regions.Asia.South Asia'             1907  -->   1514   393    92  58647
			'Geography.Regions.Asia.Southeast Asia'         2609  -->   1976   633   191  57846
			'Geography.Regions.Asia.West Asia'              2095  -->   1703   392    77  58474
			'Geography.Regions.Europe.Eastern Europe'       4157  -->   3272   885   254  56235
			'Geography.Regions.Europe.Europe*'             13143  -->  10671  2472  1161  46342
			'Geography.Regions.Europe.Northern Europe'      2793  -->   1742  1051   246  57607
			'Geography.Regions.Europe.Southern Europe'      2768  -->   2113   655   173  57705
			'Geography.Regions.Europe.Western Europe'       3947  -->   3071   876   217  56482
			'Geography.Regions.Oceania'                     2351  -->   1752   599   141  58154
			'History and Society.Business and economics'    3221  -->   1898  1323   345  57080
			'History and Society.Education'                 1625  -->    929   696   120  58901
			'History and Society.History'                   4244  -->   2183  2061   562  55840
			'History and Society.Military and warfare'      4173  -->   3143  1030   412  56061
			'History and Society.Politics and government'   4307  -->   2380  1927   463  55876
			'History and Society.Society'                   4318  -->   1654  2664   303  56025
			'History and Society.Transportation'            3507  -->   3229   278    85  57054
			'STEM.Biology'                                  7279  -->   6713   566   190  53177
			'STEM.Chemistry'                                1430  -->   1074   356   173  59043
			'STEM.Computing'                                2385  -->   1938   447   328  57933
			'STEM.Earth and environment'                    1621  -->   1085   536   137  58888
			'STEM.Engineering'                              2963  -->   2468   495   131  57552
			'STEM.Libraries & Information'                   493  -->    357   136    34  60119
			'STEM.Mathematics'                               898  -->    710   188    64  59684
			'STEM.Medicine & Health'                        1782  -->   1293   489   139  58725
			'STEM.Physics'                                  1404  -->   1011   393   166  59076
			'STEM.STEM*'                                   20497  -->  18772  1725   929  39220
			'STEM.Space'                                    1588  -->   1444   144    42  59016
			'STEM.Technology'                               4165  -->   3029  1136   573  55908
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.236         0.12
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.217         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.022         0.003
		Culture.Philosophy and religion                 0.05          0.01
		Culture.Sports                                  0.067         0.06
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.038         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.102         0.018
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
		Geography.Regions.Asia.East Asia                0.094         0.012
		Geography.Regions.Asia.North Asia               0.042         0.006
		Geography.Regions.Asia.South Asia               0.031         0.016
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.069         0.018
		Geography.Regions.Europe.Europe*                0.217         0.081
		Geography.Regions.Europe.Northern Europe        0.046         0.029
		Geography.Regions.Europe.Southern Europe        0.046         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.02
		Geography.Regions.Oceania                       0.039         0.016
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.07          0.011
		History and Society.Military and warfare        0.069         0.015
		History and Society.Politics and government     0.071         0.028
		History and Society.Society                     0.071         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.12          0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.338         0.065
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.05, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.123
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.074
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.068
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.019
		Geography.Regions.Europe.Europe*             0.088
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.015
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.023
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.926
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.932
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.912
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.985
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.977
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.794, macro=0.743):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.904
		Culture.Biography.Women                      0.8
		Culture.Food and drink                       0.711
		Culture.Internet culture                     0.821
		Culture.Linguistics                          0.774
		Culture.Literature                           0.781
		Culture.Media.Books                          0.738
		Culture.Media.Entertainment                  0.526
		Culture.Media.Films                          0.801
		Culture.Media.Media*                         0.879
		Culture.Media.Music                          0.842
		Culture.Media.Radio                          0.618
		Culture.Media.Software                       0.813
		Culture.Media.Television                     0.712
		Culture.Media.Video games                    0.92
		Culture.Performing arts                      0.673
		Culture.Philosophy and religion              0.56
		Culture.Sports                               0.88
		Culture.Visual arts.Architecture             0.705
		Culture.Visual arts.Comics and Anime         0.899
		Culture.Visual arts.Fashion                  0.843
		Culture.Visual arts.Visual arts*             0.773
		Geography.Geographical                       0.657
		Geography.Regions.Africa.Africa*             0.778
		Geography.Regions.Africa.Central Africa      0.655
		Geography.Regions.Africa.Eastern Africa      0.449
		Geography.Regions.Africa.Northern Africa     0.699
		Geography.Regions.Africa.Southern Africa     0.682
		Geography.Regions.Africa.Western Africa      0.804
		Geography.Regions.Americas.Central America   0.647
		Geography.Regions.Americas.North America     0.686
		Geography.Regions.Americas.South America     0.761
		Geography.Regions.Asia.Asia*                 0.844
		Geography.Regions.Asia.Central Asia          0.72
		Geography.Regions.Asia.East Asia             0.811
		Geography.Regions.Asia.North Asia            0.746
		Geography.Regions.Asia.South Asia            0.794
		Geography.Regions.Asia.Southeast Asia        0.757
		Geography.Regions.Asia.West Asia             0.813
		Geography.Regions.Europe.Eastern Europe      0.787
		Geography.Regions.Europe.Europe*             0.812
		Geography.Regions.Europe.Northern Europe     0.624
		Geography.Regions.Europe.Southern Europe     0.763
		Geography.Regions.Europe.Western Europe      0.778
		Geography.Regions.Oceania                    0.745
		History and Society.Business and economics   0.589
		History and Society.Education                0.572
		History and Society.History                  0.514
		History and Society.Military and warfare     0.753
		History and Society.Politics and government  0.553
		History and Society.Society                  0.383
		History and Society.Transportation           0.921
		STEM.Biology                                 0.922
		STEM.Chemistry                               0.751
		STEM.Computing                               0.813
		STEM.Earth and environment                   0.669
		STEM.Engineering                             0.833
		STEM.Libraries & Information                 0.724
		STEM.Mathematics                             0.791
		STEM.Medicine & Health                       0.726
		STEM.Physics                                 0.72
		STEM.STEM*                                   0.916
		STEM.Space                                   0.909
		STEM.Technology                              0.727
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
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
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.999
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.736, macro=0.588):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.458
		Culture.Food and drink                       0.47
		Culture.Internet culture                     0.419
		Culture.Linguistics                          0.828
		Culture.Literature                           0.559
		Culture.Media.Books                          0.596
		Culture.Media.Entertainment                  0.407
		Culture.Media.Films                          0.771
		Culture.Media.Media*                         0.647
		Culture.Media.Music                          0.835
		Culture.Media.Radio                          0.756
		Culture.Media.Software                       0.165
		Culture.Media.Television                     0.723
		Culture.Media.Video games                    0.719
		Culture.Performing arts                      0.508
		Culture.Philosophy and religion              0.569
		Culture.Sports                               0.963
		Culture.Visual arts.Architecture             0.715
		Culture.Visual arts.Comics and Anime         0.611
		Culture.Visual arts.Fashion                  0.339
		Culture.Visual arts.Visual arts*             0.65
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.435
		Geography.Regions.Africa.Central Africa      0.176
		Geography.Regions.Africa.Eastern Africa      0.236
		Geography.Regions.Africa.Northern Africa     0.352
		Geography.Regions.Africa.Southern Africa     0.421
		Geography.Regions.Africa.Western Africa      0.428
		Geography.Regions.Americas.Central America   0.546
		Geography.Regions.Americas.North America     0.802
		Geography.Regions.Americas.South America     0.626
		Geography.Regions.Asia.Asia*                 0.654
		Geography.Regions.Asia.Central Asia          0.282
		Geography.Regions.Asia.East Asia             0.537
		Geography.Regions.Asia.North Asia            0.546
		Geography.Regions.Asia.South Asia            0.895
		Geography.Regions.Asia.Southeast Asia        0.59
		Geography.Regions.Asia.West Asia             0.88
		Geography.Regions.Europe.Eastern Europe      0.765
		Geography.Regions.Europe.Europe*             0.745
		Geography.Regions.Europe.Northern Europe     0.814
		Geography.Regions.Europe.Southern Europe     0.781
		Geography.Regions.Europe.Western Europe      0.809
		Geography.Regions.Oceania                    0.837
		History and Society.Business and economics   0.49
		History and Society.Education                0.692
		History and Society.History                  0.362
		History and Society.Military and warfare     0.616
		History and Society.Politics and government  0.659
		History and Society.Society                  0.372
		History and Society.Transportation           0.911
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.303
		STEM.Computing                               0.296
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.679
		STEM.Libraries & Information                 0.467
		STEM.Mathematics                             0.254
		STEM.Medicine & Health                       0.665
		STEM.Physics                                 0.194
		STEM.STEM*                                   0.733
		STEM.Space                                   0.845
		STEM.Technology                              0.266
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.987
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.987
		History and Society.Society                  0.995
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.756, macro=0.637):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.891
		Culture.Biography.Women                      0.583
		Culture.Food and drink                       0.566
		Culture.Internet culture                     0.555
		Culture.Linguistics                          0.8
		Culture.Literature                           0.652
		Culture.Media.Books                          0.66
		Culture.Media.Entertainment                  0.459
		Culture.Media.Films                          0.786
		Culture.Media.Media*                         0.746
		Culture.Media.Music                          0.839
		Culture.Media.Radio                          0.68
		Culture.Media.Software                       0.274
		Culture.Media.Television                     0.718
		Culture.Media.Video games                    0.807
		Culture.Performing arts                      0.579
		Culture.Philosophy and religion              0.565
		Culture.Sports                               0.92
		Culture.Visual arts.Architecture             0.71
		Culture.Visual arts.Comics and Anime         0.727
		Culture.Visual arts.Fashion                  0.484
		Culture.Visual arts.Visual arts*             0.706
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.558
		Geography.Regions.Africa.Central Africa      0.277
		Geography.Regions.Africa.Eastern Africa      0.309
		Geography.Regions.Africa.Northern Africa     0.468
		Geography.Regions.Africa.Southern Africa     0.521
		Geography.Regions.Africa.Western Africa      0.559
		Geography.Regions.Americas.Central America   0.592
		Geography.Regions.Americas.North America     0.74
		Geography.Regions.Americas.South America     0.687
		Geography.Regions.Asia.Asia*                 0.737
		Geography.Regions.Asia.Central Asia          0.405
		Geography.Regions.Asia.East Asia             0.646
		Geography.Regions.Asia.North Asia            0.63
		Geography.Regions.Asia.South Asia            0.841
		Geography.Regions.Asia.Southeast Asia        0.664
		Geography.Regions.Asia.West Asia             0.845
		Geography.Regions.Europe.Eastern Europe      0.776
		Geography.Regions.Europe.Europe*             0.777
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.772
		Geography.Regions.Europe.Western Europe      0.793
		Geography.Regions.Oceania                    0.788
		History and Society.Business and economics   0.535
		History and Society.Education                0.626
		History and Society.History                  0.425
		History and Society.Military and warfare     0.677
		History and Society.Politics and government  0.601
		History and Society.Society                  0.377
		History and Society.Transportation           0.916
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.432
		STEM.Computing                               0.433
		STEM.Earth and environment                   0.62
		STEM.Engineering                             0.748
		STEM.Libraries & Information                 0.568
		STEM.Mathematics                             0.384
		STEM.Medicine & Health                       0.694
		STEM.Physics                                 0.305
		STEM.STEM*                                   0.814
		STEM.Space                                   0.876
		STEM.Technology                              0.39
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.979
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.995
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.985
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.98
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
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
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.024
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.001
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.979
		Culture.Literature                           0.98
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.953
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.961
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.975
		Geography.Geographical                       0.967
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.967
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.98
		Geography.Regions.Americas.Central America   0.975
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.983
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.976
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.977
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.968
		History and Society.Education                0.974
		History and Society.History                  0.955
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.955
		History and Society.Society                  0.93
		History and Society.Transportation           0.987
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.987
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.984
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.982
		STEM.Space                                   0.991
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.807, macro=0.657):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.941
		Culture.Biography.Women                      0.569
		Culture.Food and drink                       0.602
		Culture.Internet culture                     0.65
		Culture.Linguistics                          0.809
		Culture.Literature                           0.739
		Culture.Media.Books                          0.709
		Culture.Media.Entertainment                  0.406
		Culture.Media.Films                          0.789
		Culture.Media.Media*                         0.838
		Culture.Media.Music                          0.872
		Culture.Media.Radio                          0.539
		Culture.Media.Software                       0.294
		Culture.Media.Television                     0.716
		Culture.Media.Video games                    0.884
		Culture.Performing arts                      0.557
		Culture.Philosophy and religion              0.546
		Culture.Sports                               0.955
		Culture.Visual arts.Architecture             0.748
		Culture.Visual arts.Comics and Anime         0.797
		Culture.Visual arts.Fashion                  0.534
		Culture.Visual arts.Visual arts*             0.769
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.582
		Geography.Regions.Africa.Central Africa      0.206
		Geography.Regions.Africa.Eastern Africa      0.154
		Geography.Regions.Africa.Northern Africa     0.473
		Geography.Regions.Africa.Southern Africa     0.415
		Geography.Regions.Africa.Western Africa      0.467
		Geography.Regions.Americas.Central America   0.531
		Geography.Regions.Americas.North America     0.82
		Geography.Regions.Americas.South America     0.665
		Geography.Regions.Asia.Asia*                 0.807
		Geography.Regions.Asia.Central Asia          0.478
		Geography.Regions.Asia.East Asia             0.677
		Geography.Regions.Asia.North Asia            0.654
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.688
		Geography.Regions.Asia.West Asia             0.895
		Geography.Regions.Europe.Eastern Europe      0.793
		Geography.Regions.Europe.Europe*             0.86
		Geography.Regions.Europe.Northern Europe     0.773
		Geography.Regions.Europe.Southern Europe     0.827
		Geography.Regions.Europe.Western Europe      0.856
		Geography.Regions.Oceania                    0.831
		History and Society.Business and economics   0.517
		History and Society.Education                0.636
		History and Society.History                  0.404
		History and Society.Military and warfare     0.76
		History and Society.Politics and government  0.652
		History and Society.Society                  0.342
		History and Society.Transportation           0.939
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.496
		STEM.Computing                               0.449
		STEM.Earth and environment                   0.613
		STEM.Engineering                             0.819
		STEM.Libraries & Information                 0.482
		STEM.Mathematics                             0.462
		STEM.Medicine & Health                       0.744
		STEM.Physics                                 0.287
		STEM.STEM*                                   0.897
		STEM.Space                                   0.933
		STEM.Technology                              0.432
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'type': 'object', 'properties': {'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

