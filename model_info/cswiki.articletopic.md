Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'min_samples_leaf': 1, 'warm_start': False, 'min_impurity_split': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'random_state': None, 'center': False, 'validation_fraction': 0.1, 'verbose': 0, 'max_depth': 5, 'criterion': 'friedman_mse', 'min_impurity_decrease': 0.0, 'learning_rate': 0.1, 'loss': 'deviance', 'population_rates': None, 'multilabel': True, 'max_features': 'log2', 'n_iter_no_change': None, 'tol': 0.0001, 'init': None, 'max_leaf_nodes': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'label_weights': {}, 'scale': False, 'min_samples_split': 2, 'subsample': 1.0, 'presort': 'auto'}
	Environment:
	 - revscoring_version: '2.6.3'
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
	counts (n=59658):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16433  -->  15245  1188   735  42490
			'Culture.Biography.Women'                       4279  -->   3753   526   273  55106
			'Culture.Food and drink'                        1599  -->   1353   246    53  58006
			'Culture.Internet culture'                      3200  -->   2898   302   161  56297
			'Culture.Linguistics'                           1607  -->   1289   318    76  57975
			'Culture.Literature'                            5032  -->   3997  1035   365  54261
			'Culture.Media.Books'                           1699  -->   1472   227    67  57892
			'Culture.Media.Entertainment'                   2282  -->   1489   793   176  57200
			'Culture.Media.Films'                           2531  -->   2177   354   105  57022
			'Culture.Media.Media*'                         14310  -->  13016  1294  1048  44300
			'Culture.Media.Music'                           3319  -->   2945   374   284  56055
			'Culture.Media.Radio'                            424  -->    275   149    36  59198
			'Culture.Media.Software'                        2394  -->   2085   309   256  57008
			'Culture.Media.Television'                      2521  -->   2206   315    86  57051
			'Culture.Media.Video games'                     1891  -->   1805    86    20  57747
			'Culture.Performing arts'                       1489  -->   1140   349    99  58070
			'Culture.Philosophy and religion'               4421  -->   2901  1520   374  54863
			'Culture.Sports'                                5663  -->   5147   516   203  53792
			'Culture.Visual arts.Architecture'              2283  -->   1769   514   190  57185
			'Culture.Visual arts.Comics and Anime'          1695  -->   1565   130    30  57933
			'Culture.Visual arts.Fashion'                   1063  -->    891   172    46  58549
			'Culture.Visual arts.Visual arts*'              5896  -->   4857  1039   359  53403
			'Geography.Geographical'                        4621  -->   3508  1113   598  54439
			'Geography.Regions.Africa.Africa*'              3696  -->   2854   842   172  55790
			'Geography.Regions.Africa.Central Africa'         31  -->      9    22    40  59587
			'Geography.Regions.Africa.Eastern Africa'        471  -->    346   125    46  59141
			'Geography.Regions.Africa.Northern Africa'      1548  -->   1179   369   101  58009
			'Geography.Regions.Africa.Southern Africa'       677  -->    484   193    28  58953
			'Geography.Regions.Africa.Western Africa'        194  -->    106    88    44  59420
			'Geography.Regions.Americas.Central America'    1360  -->   1004   356    44  58254
			'Geography.Regions.Americas.North America'      6003  -->   3975  2028   820  52835
			'Geography.Regions.Americas.South America'      1502  -->   1127   375    71  58085
			'Geography.Regions.Asia.Asia*'                 10850  -->   9097  1753   745  48063
			'Geography.Regions.Asia.Central Asia'           1352  -->   1089   263    63  58243
			'Geography.Regions.Asia.East Asia'              2943  -->   2383   560   137  56578
			'Geography.Regions.Asia.North Asia'             1967  -->   1477   490   232  57459
			'Geography.Regions.Asia.South Asia'             1843  -->   1524   319    71  57744
			'Geography.Regions.Asia.Southeast Asia'         1643  -->   1297   346    50  57965
			'Geography.Regions.Asia.West Asia'              2881  -->   2363   518   193  56584
			'Geography.Regions.Europe.Eastern Europe'       5297  -->   4016  1281   594  53767
			'Geography.Regions.Europe.Europe*'             16868  -->  13678  3190  2273  40517
			'Geography.Regions.Europe.Northern Europe'      4065  -->   2757  1308   371  55222
			'Geography.Regions.Europe.Southern Europe'      3540  -->   2591   949   301  55817
			'Geography.Regions.Europe.Western Europe'       5074  -->   3731  1343   512  54072
			'Geography.Regions.Oceania'                     1769  -->   1290   479    86  57803
			'History and Society.Business and economics'    3605  -->   2469  1136   287  55766
			'History and Society.Education'                 1828  -->   1153   675   117  57713
			'History and Society.History'                   5571  -->   3792  1779   591  53496
			'History and Society.Military and warfare'      5707  -->   4297  1410   517  53434
			'History and Society.Politics and government'   4760  -->   2969  1791   468  54430
			'History and Society.Society'                   6846  -->   3739  3107   606  52206
			'History and Society.Transportation'            4252  -->   3950   302   146  55260
			'STEM.Biology'                                  3739  -->   3247   492   122  55797
			'STEM.Chemistry'                                1549  -->   1361   188    96  58013
			'STEM.Computing'                                2872  -->   2550   322   258  56528
			'STEM.Earth and environment'                    2183  -->   1730   453   128  57347
			'STEM.Engineering'                              2974  -->   2466   508   176  56508
			'STEM.Libraries & Information'                   720  -->    551   169    48  58890
			'STEM.Mathematics'                              1210  -->   1075   135    36  58412
			'STEM.Medicine & Health'                        2017  -->   1602   415   116  57525
			'STEM.Physics'                                  1499  -->   1202   297   110  58049
			'STEM.STEM*'                                   18910  -->  17249  1661   827  39921
			'STEM.Space'                                    2041  -->   1937   104    36  57581
			'STEM.Technology'                               5221  -->   4286   935   515  53922
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.275         0.123
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.027         0.002
		Culture.Internet culture                        0.054         0.004
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.24          0.059
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.074         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.062         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.101         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.182         0.046
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.049         0.011
		Geography.Regions.Asia.North Asia               0.033         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.089         0.013
		Geography.Regions.Europe.Europe*                0.283         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.059         0.013
		Geography.Regions.Europe.Western Europe         0.085         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.06          0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.096         0.014
		History and Society.Politics and government     0.08          0.028
		History and Society.Society                     0.115         0.013
		History and Society.Transportation              0.071         0.015
		STEM.Biology                                    0.063         0.034
		STEM.Chemistry                                  0.026         0.002
		STEM.Computing                                  0.048         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.317         0.069
		STEM.Space                                      0.034         0.006
		STEM.Technology                                 0.088         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.026
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.018
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.026
		History and Society.Society                  0.018
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.974
		History and Society.Society                  0.982
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.819, macro=0.785):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.877
		Culture.Food and drink                       0.846
		Culture.Internet culture                     0.906
		Culture.Linguistics                          0.802
		Culture.Literature                           0.794
		Culture.Media.Books                          0.866
		Culture.Media.Entertainment                  0.652
		Culture.Media.Films                          0.86
		Culture.Media.Media*                         0.91
		Culture.Media.Music                          0.887
		Culture.Media.Radio                          0.649
		Culture.Media.Software                       0.871
		Culture.Media.Television                     0.875
		Culture.Media.Video games                    0.955
		Culture.Performing arts                      0.766
		Culture.Philosophy and religion              0.656
		Culture.Sports                               0.909
		Culture.Visual arts.Architecture             0.775
		Culture.Visual arts.Comics and Anime         0.923
		Culture.Visual arts.Fashion                  0.838
		Culture.Visual arts.Visual arts*             0.824
		Geography.Geographical                       0.759
		Geography.Regions.Africa.Africa*             0.772
		Geography.Regions.Africa.Central Africa      0.29
		Geography.Regions.Africa.Eastern Africa      0.735
		Geography.Regions.Africa.Northern Africa     0.762
		Geography.Regions.Africa.Southern Africa     0.715
		Geography.Regions.Africa.Western Africa      0.546
		Geography.Regions.Americas.Central America   0.738
		Geography.Regions.Americas.North America     0.662
		Geography.Regions.Americas.South America     0.75
		Geography.Regions.Asia.Asia*                 0.838
		Geography.Regions.Asia.Central Asia          0.805
		Geography.Regions.Asia.East Asia             0.81
		Geography.Regions.Asia.North Asia            0.751
		Geography.Regions.Asia.South Asia            0.827
		Geography.Regions.Asia.Southeast Asia        0.789
		Geography.Regions.Asia.West Asia             0.82
		Geography.Regions.Europe.Eastern Europe      0.758
		Geography.Regions.Europe.Europe*             0.811
		Geography.Regions.Europe.Northern Europe     0.678
		Geography.Regions.Europe.Southern Europe     0.732
		Geography.Regions.Europe.Western Europe      0.735
		Geography.Regions.Oceania                    0.729
		History and Society.Business and economics   0.685
		History and Society.Education                0.631
		History and Society.History                  0.681
		History and Society.Military and warfare     0.753
		History and Society.Politics and government  0.624
		History and Society.Society                  0.546
		History and Society.Transportation           0.929
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.879
		STEM.Computing                               0.888
		STEM.Earth and environment                   0.792
		STEM.Engineering                             0.829
		STEM.Libraries & Information                 0.765
		STEM.Mathematics                             0.888
		STEM.Medicine & Health                       0.794
		STEM.Physics                                 0.802
		STEM.STEM*                                   0.912
		STEM.Space                                   0.949
		STEM.Technology                              0.821
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.989
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.991
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.738, macro=0.619):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.885
		Culture.Biography.Women                      0.725
		Culture.Food and drink                       0.696
		Culture.Internet culture                     0.527
		Culture.Linguistics                          0.819
		Culture.Literature                           0.652
		Culture.Media.Books                          0.752
		Culture.Media.Entertainment                  0.433
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.71
		Culture.Media.Music                          0.812
		Culture.Media.Radio                          0.697
		Culture.Media.Software                       0.206
		Culture.Media.Television                     0.838
		Culture.Media.Video games                    0.878
		Culture.Performing arts                      0.566
		Culture.Philosophy and religion              0.511
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.714
		Culture.Visual arts.Comics and Anime         0.797
		Culture.Visual arts.Fashion                  0.464
		Culture.Visual arts.Visual arts*             0.697
		Geography.Geographical                       0.628
		Geography.Regions.Africa.Africa*             0.664
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.301
		Geography.Regions.Africa.Northern Africa     0.35
		Geography.Regions.Africa.Southern Africa     0.639
		Geography.Regions.Africa.Western Africa      0.336
		Geography.Regions.Americas.Central America   0.764
		Geography.Regions.Americas.North America     0.749
		Geography.Regions.Americas.South America     0.796
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.393
		Geography.Regions.Asia.East Asia             0.795
		Geography.Regions.Asia.North Asia            0.147
		Geography.Regions.Asia.South Asia            0.912
		Geography.Regions.Asia.Southeast Asia        0.847
		Geography.Regions.Asia.West Asia             0.727
		Geography.Regions.Europe.Eastern Europe      0.474
		Geography.Regions.Europe.Europe*             0.557
		Geography.Regions.Europe.Northern Europe     0.762
		Geography.Regions.Europe.Southern Europe     0.643
		Geography.Regions.Europe.Western Europe      0.605
		Geography.Regions.Oceania                    0.883
		History and Society.Business and economics   0.577
		History and Society.Education                0.698
		History and Society.History                  0.406
		History and Society.Military and warfare     0.529
		History and Society.Politics and government  0.68
		History and Society.Society                  0.378
		History and Society.Transportation           0.844
		STEM.Biology                                 0.933
		STEM.Chemistry                               0.454
		STEM.Computing                               0.345
		STEM.Earth and environment                   0.619
		STEM.Engineering                             0.584
		STEM.Libraries & Information                 0.369
		STEM.Mathematics                             0.376
		STEM.Medicine & Health                       0.718
		STEM.Physics                                 0.265
		STEM.STEM*                                   0.77
		STEM.Space                                   0.902
		STEM.Technology                              0.309
		-------------------------------------------  -----
	!precision (micro=0.993, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.99
		Culture.Biography.Women                      0.998
		Culture.Food and drink                       1
		Culture.Internet culture                     1
		Culture.Linguistics                          0.999
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.994
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.997
		Geography.Geographical                       0.994
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
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.995
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.77, macro=0.673):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.906
		Culture.Biography.Women                      0.794
		Culture.Food and drink                       0.764
		Culture.Internet culture                     0.667
		Culture.Linguistics                          0.81
		Culture.Literature                           0.716
		Culture.Media.Books                          0.805
		Culture.Media.Entertainment                  0.521
		Culture.Media.Films                          0.846
		Culture.Media.Media*                         0.797
		Culture.Media.Music                          0.848
		Culture.Media.Radio                          0.672
		Culture.Media.Software                       0.333
		Culture.Media.Television                     0.856
		Culture.Media.Video games                    0.915
		Culture.Performing arts                      0.651
		Culture.Philosophy and religion              0.574
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.743
		Culture.Visual arts.Comics and Anime         0.856
		Culture.Visual arts.Fashion                  0.597
		Culture.Visual arts.Visual arts*             0.755
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.714
		Geography.Regions.Africa.Central Africa      0.004
		Geography.Regions.Africa.Eastern Africa      0.427
		Geography.Regions.Africa.Northern Africa     0.48
		Geography.Regions.Africa.Southern Africa     0.675
		Geography.Regions.Africa.Western Africa      0.416
		Geography.Regions.Americas.Central America   0.751
		Geography.Regions.Americas.North America     0.703
		Geography.Regions.Americas.South America     0.773
		Geography.Regions.Asia.Asia*                 0.777
		Geography.Regions.Asia.Central Asia          0.528
		Geography.Regions.Asia.East Asia             0.802
		Geography.Regions.Asia.North Asia            0.246
		Geography.Regions.Asia.South Asia            0.867
		Geography.Regions.Asia.Southeast Asia        0.817
		Geography.Regions.Asia.West Asia             0.771
		Geography.Regions.Europe.Eastern Europe      0.584
		Geography.Regions.Europe.Europe*             0.661
		Geography.Regions.Europe.Northern Europe     0.718
		Geography.Regions.Europe.Southern Europe     0.685
		Geography.Regions.Europe.Western Europe      0.664
		Geography.Regions.Oceania                    0.799
		History and Society.Business and economics   0.626
		History and Society.Education                0.663
		History and Society.History                  0.508
		History and Society.Military and warfare     0.621
		History and Society.Politics and government  0.651
		History and Society.Society                  0.447
		History and Society.Transportation           0.884
		STEM.Biology                                 0.899
		STEM.Chemistry                               0.598
		STEM.Computing                               0.497
		STEM.Earth and environment                   0.695
		STEM.Engineering                             0.686
		STEM.Libraries & Information                 0.498
		STEM.Mathematics                             0.528
		STEM.Medicine & Health                       0.754
		STEM.Physics                                 0.398
		STEM.STEM*                                   0.835
		STEM.Space                                   0.925
		STEM.Technology                              0.449
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.986
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.986
		STEM.Space                                   1
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.981, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.978
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.937
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.992
		History and Society.Education                0.995
		History and Society.History                  0.986
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.981
		History and Society.Society                  0.983
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.023
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.003
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.015
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.053
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.011
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.009
		History and Society.Society                  0.011
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.02
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.979, macro=0.977):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.988
		Culture.Internet culture                     0.991
		Culture.Linguistics                          0.985
		Culture.Literature                           0.981
		Culture.Media.Books                          0.989
		Culture.Media.Entertainment                  0.981
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.967
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.989
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.987
		Culture.Philosophy and religion              0.97
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.986
		Culture.Visual arts.Comics and Anime         0.992
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.689
		Geography.Regions.Africa.Eastern Africa      0.982
		Geography.Regions.Africa.Northern Africa     0.987
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.935
		Geography.Regions.Americas.Central America   0.984
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.984
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.987
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.984
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.975
		History and Society.Education                0.979
		History and Society.History                  0.968
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.967
		History and Society.Society                  0.948
		History and Society.Transportation           0.989
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.989
		STEM.Computing                               0.989
		STEM.Earth and environment                   0.985
		STEM.Engineering                             0.985
		STEM.Libraries & Information                 0.977
		STEM.Mathematics                             0.992
		STEM.Medicine & Health                       0.983
		STEM.Physics                                 0.988
		STEM.STEM*                                   0.981
		STEM.Space                                   0.994
		STEM.Technology                              0.981
		-------------------------------------------  -----
	pr_auc (micro=0.83, macro=0.721):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.818
		Culture.Food and drink                       0.828
		Culture.Internet culture                     0.845
		Culture.Linguistics                          0.851
		Culture.Literature                           0.793
		Culture.Media.Books                          0.861
		Culture.Media.Entertainment                  0.538
		Culture.Media.Films                          0.905
		Culture.Media.Media*                         0.891
		Culture.Media.Music                          0.877
		Culture.Media.Radio                          0.596
		Culture.Media.Software                       0.471
		Culture.Media.Television                     0.913
		Culture.Media.Video games                    0.941
		Culture.Performing arts                      0.676
		Culture.Philosophy and religion              0.584
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.802
		Culture.Visual arts.Comics and Anime         0.911
		Culture.Visual arts.Fashion                  0.66
		Culture.Visual arts.Visual arts*             0.844
		Geography.Geographical                       0.736
		Geography.Regions.Africa.Africa*             0.755
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.342
		Geography.Regions.Africa.Northern Africa     0.53
		Geography.Regions.Africa.Southern Africa     0.737
		Geography.Regions.Africa.Western Africa      0.23
		Geography.Regions.Americas.Central America   0.787
		Geography.Regions.Americas.North America     0.771
		Geography.Regions.Americas.South America     0.812
		Geography.Regions.Asia.Asia*                 0.86
		Geography.Regions.Asia.Central Asia          0.548
		Geography.Regions.Asia.East Asia             0.851
		Geography.Regions.Asia.North Asia            0.289
		Geography.Regions.Asia.South Asia            0.904
		Geography.Regions.Asia.Southeast Asia        0.831
		Geography.Regions.Asia.West Asia             0.807
		Geography.Regions.Europe.Eastern Europe      0.661
		Geography.Regions.Europe.Europe*             0.755
		Geography.Regions.Europe.Northern Europe     0.784
		Geography.Regions.Europe.Southern Europe     0.715
		Geography.Regions.Europe.Western Europe      0.705
		Geography.Regions.Oceania                    0.866
		History and Society.Business and economics   0.643
		History and Society.Education                0.682
		History and Society.History                  0.538
		History and Society.Military and warfare     0.71
		History and Society.Politics and government  0.69
		History and Society.Society                  0.426
		History and Society.Transportation           0.933
		STEM.Biology                                 0.948
		STEM.Chemistry                               0.701
		STEM.Computing                               0.639
		STEM.Earth and environment                   0.731
		STEM.Engineering                             0.762
		STEM.Libraries & Information                 0.502
		STEM.Mathematics                             0.735
		STEM.Medicine & Health                       0.801
		STEM.Physics                                 0.454
		STEM.STEM*                                   0.93
		STEM.Space                                   0.968
		STEM.Technology                              0.585
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

