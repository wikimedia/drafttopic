Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'min_impurity_split': None, 'warm_start': False, 'scale': False, 'max_depth': 5, 'validation_fraction': 0.1, 'criterion': 'friedman_mse', 'population_rates': None, 'label_weights': {}, 'center': False, 'min_samples_leaf': 1, 'presort': 'auto', 'max_features': 'log2', 'subsample': 1.0, 'tol': 0.0001, 'loss': 'deviance', 'verbose': 0, 'n_estimators': 150, 'min_samples_split': 2, 'learning_rate': 0.1, 'init': None, 'multilabel': True, 'random_state': None, 'n_iter_no_change': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology']}
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
	counts (n=60150):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15672  -->  14248  1424   750  43728
			'Culture.Biography.Women'                       4475  -->   3537   938   394  55281
			'Culture.Food and drink'                        1819  -->   1531   288    74  58257
			'Culture.Internet culture'                      3397  -->   2846   551   214  56539
			'Culture.Linguistics'                           1625  -->   1287   338    82  58443
			'Culture.Literature'                            5881  -->   4724  1157   377  53892
			'Culture.Media.Books'                           1634  -->   1344   290    69  58447
			'Culture.Media.Entertainment'                   2333  -->   1489   844   185  57632
			'Culture.Media.Films'                           2960  -->   2536   424    84  57106
			'Culture.Media.Media*'                         15008  -->  13321  1687  1224  43918
			'Culture.Media.Music'                           3173  -->   2676   497   244  56733
			'Culture.Media.Radio'                            699  -->    497   202    35  59416
			'Culture.Media.Software'                        2364  -->   1993   371   262  57524
			'Culture.Media.Television'                      2484  -->   1862   622   121  57545
			'Culture.Media.Video games'                     2223  -->   2023   200    45  57882
			'Culture.Performing arts'                       1501  -->   1027   474   107  58542
			'Culture.Philosophy and religion'               3876  -->   2441  1435   246  56028
			'Culture.Sports'                                4964  -->   4391   573   179  55007
			'Culture.Visual arts.Architecture'              2131  -->   1620   511   159  57860
			'Culture.Visual arts.Comics and Anime'          2410  -->   2157   253    86  57654
			'Culture.Visual arts.Fashion'                   1336  -->   1083   253    71  58743
			'Culture.Visual arts.Visual arts*'              6373  -->   5027  1346   377  53400
			'Geography.Geographical'                        3933  -->   2830  1103   502  55715
			'Geography.Regions.Africa.Africa*'              3848  -->   3088   760   185  56117
			'Geography.Regions.Africa.Central Africa'         31  -->      8    23    36  60083
			'Geography.Regions.Africa.Eastern Africa'        482  -->    391    91    58  59610
			'Geography.Regions.Africa.Northern Africa'      1522  -->   1208   314    91  58537
			'Geography.Regions.Africa.Southern Africa'       685  -->    557   128    27  59438
			'Geography.Regions.Africa.Western Africa'        281  -->    205    76    53  59816
			'Geography.Regions.Americas.Central America'    1372  -->   1046   326    42  58736
			'Geography.Regions.Americas.North America'      6575  -->   4578  1997   919  52656
			'Geography.Regions.Americas.South America'      1548  -->   1179   369    88  58514
			'Geography.Regions.Asia.Asia*'                 14972  -->  12939  2033  1243  43935
			'Geography.Regions.Asia.Central Asia'           1337  -->   1103   234    63  58750
			'Geography.Regions.Asia.East Asia'              7339  -->   6130  1209   627  52184
			'Geography.Regions.Asia.North Asia'             1895  -->   1560   335   170  58085
			'Geography.Regions.Asia.South Asia'             1895  -->   1543   352    43  58212
			'Geography.Regions.Asia.Southeast Asia'         1955  -->   1535   420    80  58115
			'Geography.Regions.Asia.West Asia'              2422  -->   1934   488   129  57599
			'Geography.Regions.Europe.Eastern Europe'       3438  -->   2839   599   235  56477
			'Geography.Regions.Europe.Europe*'             13539  -->  11321  2218  1398  45213
			'Geography.Regions.Europe.Northern Europe'      3935  -->   2955   980   302  55913
			'Geography.Regions.Europe.Southern Europe'      3358  -->   2641   717   242  56550
			'Geography.Regions.Europe.Western Europe'       4055  -->   3107   948   311  55784
			'Geography.Regions.Oceania'                     1799  -->   1409   390    51  58300
			'History and Society.Business and economics'    3922  -->   2665  1257   350  55878
			'History and Society.Education'                 1913  -->   1372   541   112  58125
			'History and Society.History'                   5571  -->   3679  1892   474  54105
			'History and Society.Military and warfare'      5194  -->   3893  1301   415  54541
			'History and Society.Politics and government'   5121  -->   3245  1876   455  54574
			'History and Society.Society'                   6681  -->   3748  2933   515  52954
			'History and Society.Transportation'            3741  -->   3400   341   140  56269
			'STEM.Biology'                                  3435  -->   2894   541   127  56588
			'STEM.Chemistry'                                1504  -->   1301   203    93  58553
			'STEM.Computing'                                2806  -->   2404   402   316  57028
			'STEM.Earth and environment'                    1895  -->   1451   444    92  58163
			'STEM.Engineering'                              2650  -->   2113   537   139  57361
			'STEM.Libraries & Information'                   781  -->    619   162    37  59332
			'STEM.Mathematics'                              1168  -->   1024   144    34  58948
			'STEM.Medicine & Health'                        2004  -->   1545   459   122  58024
			'STEM.Physics'                                  1520  -->   1250   270   109  58521
			'STEM.STEM*'                                   17833  -->  16122  1711   794  41523
			'STEM.Space'                                    1710  -->   1594   116    29  58411
			'STEM.Technology'                               4761  -->   3751  1010   505  54884
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.261         0.123
		Culture.Biography.Women                         0.074         0.015
		Culture.Food and drink                          0.03          0.002
		Culture.Internet culture                        0.056         0.004
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.098         0.016
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.25          0.059
		Culture.Media.Music                             0.053         0.024
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.064         0.011
		Culture.Sports                                  0.083         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.106         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.064         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.109         0.064
		Geography.Regions.Americas.South America        0.026         0.006
		Geography.Regions.Asia.Asia*                    0.249         0.046
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.122         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.032         0.015
		Geography.Regions.Asia.Southeast Asia           0.033         0.006
		Geography.Regions.Asia.West Asia                0.04          0.011
		Geography.Regions.Europe.Eastern Europe         0.057         0.013
		Geography.Regions.Europe.Europe*                0.225         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.056         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.065         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.086         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.111         0.013
		History and Society.Transportation              0.062         0.015
		STEM.Biology                                    0.057         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.044         0.005
		STEM.Libraries & Information                    0.013         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.296         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.079         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.066
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.021
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.091
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.016
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.026
		History and Society.Society                  0.017
		History and Society.Transportation           0.016
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.08
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.934
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.974
		History and Society.Society                  0.983
		History and Society.Transportation           0.984
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.92
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.817, macro=0.785):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.909
		Culture.Biography.Women                      0.79
		Culture.Food and drink                       0.842
		Culture.Internet culture                     0.838
		Culture.Linguistics                          0.792
		Culture.Literature                           0.803
		Culture.Media.Books                          0.823
		Culture.Media.Entertainment                  0.638
		Culture.Media.Films                          0.857
		Culture.Media.Media*                         0.888
		Culture.Media.Music                          0.843
		Culture.Media.Radio                          0.711
		Culture.Media.Software                       0.843
		Culture.Media.Television                     0.75
		Culture.Media.Video games                    0.91
		Culture.Performing arts                      0.684
		Culture.Philosophy and religion              0.63
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.76
		Culture.Visual arts.Comics and Anime         0.895
		Culture.Visual arts.Fashion                  0.811
		Culture.Visual arts.Visual arts*             0.789
		Geography.Geographical                       0.72
		Geography.Regions.Africa.Africa*             0.802
		Geography.Regions.Africa.Central Africa      0.258
		Geography.Regions.Africa.Eastern Africa      0.811
		Geography.Regions.Africa.Northern Africa     0.794
		Geography.Regions.Africa.Southern Africa     0.813
		Geography.Regions.Africa.Western Africa      0.73
		Geography.Regions.Americas.Central America   0.762
		Geography.Regions.Americas.North America     0.696
		Geography.Regions.Americas.South America     0.762
		Geography.Regions.Asia.Asia*                 0.864
		Geography.Regions.Asia.Central Asia          0.825
		Geography.Regions.Asia.East Asia             0.835
		Geography.Regions.Asia.North Asia            0.823
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.785
		Geography.Regions.Asia.West Asia             0.799
		Geography.Regions.Europe.Eastern Europe      0.826
		Geography.Regions.Europe.Europe*             0.836
		Geography.Regions.Europe.Northern Europe     0.751
		Geography.Regions.Europe.Southern Europe     0.786
		Geography.Regions.Europe.Western Europe      0.766
		Geography.Regions.Oceania                    0.783
		History and Society.Business and economics   0.68
		History and Society.Education                0.717
		History and Society.History                  0.66
		History and Society.Military and warfare     0.75
		History and Society.Politics and government  0.634
		History and Society.Society                  0.561
		History and Society.Transportation           0.909
		STEM.Biology                                 0.843
		STEM.Chemistry                               0.865
		STEM.Computing                               0.857
		STEM.Earth and environment                   0.766
		STEM.Engineering                             0.797
		STEM.Libraries & Information                 0.793
		STEM.Mathematics                             0.877
		STEM.Medicine & Health                       0.771
		STEM.Physics                                 0.822
		STEM.STEM*                                   0.904
		STEM.Space                                   0.932
		STEM.Technology                              0.788
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.981
		STEM.Space                                   1
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.747, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.623
		Culture.Food and drink                       0.621
		Culture.Internet culture                     0.438
		Culture.Linguistics                          0.807
		Culture.Literature                           0.646
		Culture.Media.Books                          0.738
		Culture.Media.Entertainment                  0.418
		Culture.Media.Films                          0.861
		Culture.Media.Media*                         0.67
		Culture.Media.Music                          0.828
		Culture.Media.Radio                          0.723
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.761
		Culture.Media.Video games                    0.754
		Culture.Performing arts                      0.521
		Culture.Philosophy and religion              0.608
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.748
		Culture.Visual arts.Comics and Anime         0.57
		Culture.Visual arts.Fashion                  0.352
		Culture.Visual arts.Visual arts*             0.677
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.658
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.275
		Geography.Regions.Africa.Northern Africa     0.386
		Geography.Regions.Africa.Southern Africa     0.678
		Geography.Regions.Africa.Western Africa      0.361
		Geography.Regions.Americas.Central America   0.779
		Geography.Regions.Americas.North America     0.736
		Geography.Regions.Americas.South America     0.763
		Geography.Regions.Asia.Asia*                 0.6
		Geography.Regions.Asia.Central Asia          0.4
		Geography.Regions.Asia.East Asia             0.448
		Geography.Regions.Asia.North Asia            0.207
		Geography.Regions.Asia.South Asia            0.944
		Geography.Regions.Asia.Southeast Asia        0.775
		Geography.Regions.Asia.West Asia             0.798
		Geography.Regions.Europe.Eastern Europe      0.722
		Geography.Regions.Europe.Europe*             0.697
		Geography.Regions.Europe.Northern Europe     0.815
		Geography.Regions.Europe.Southern Europe     0.709
		Geography.Regions.Europe.Western Europe      0.73
		Geography.Regions.Oceania                    0.932
		History and Society.Business and economics   0.527
		History and Society.Education                0.734
		History and Society.History                  0.455
		History and Society.Military and warfare     0.586
		History and Society.Politics and government  0.69
		History and Society.Society                  0.427
		History and Society.Transportation           0.849
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.46
		STEM.Computing                               0.296
		STEM.Earth and environment                   0.689
		STEM.Engineering                             0.635
		STEM.Libraries & Information                 0.442
		STEM.Mathematics                             0.388
		STEM.Medicine & Health                       0.703
		STEM.Physics                                 0.273
		STEM.STEM*                                   0.782
		STEM.Space                                   0.919
		STEM.Technology                              0.308
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.987
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       1
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.991
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
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.986
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.997
		History and Society.Education                0.998
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
	f1 (micro=0.775, macro=0.672):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.697
		Culture.Food and drink                       0.715
		Culture.Internet culture                     0.576
		Culture.Linguistics                          0.799
		Culture.Literature                           0.716
		Culture.Media.Books                          0.778
		Culture.Media.Entertainment                  0.505
		Culture.Media.Films                          0.859
		Culture.Media.Media*                         0.764
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.717
		Culture.Media.Software                       0.321
		Culture.Media.Television                     0.755
		Culture.Media.Video games                    0.825
		Culture.Performing arts                      0.591
		Culture.Philosophy and religion              0.619
		Culture.Sports                               0.918
		Culture.Visual arts.Architecture             0.754
		Culture.Visual arts.Comics and Anime         0.696
		Culture.Visual arts.Fashion                  0.491
		Culture.Visual arts.Visual arts*             0.729
		Geography.Geographical                       0.689
		Geography.Regions.Africa.Africa*             0.723
		Geography.Regions.Africa.Central Africa      0.004
		Geography.Regions.Africa.Eastern Africa      0.411
		Geography.Regions.Africa.Northern Africa     0.519
		Geography.Regions.Africa.Southern Africa     0.74
		Geography.Regions.Africa.Western Africa      0.483
		Geography.Regions.Americas.Central America   0.771
		Geography.Regions.Americas.North America     0.716
		Geography.Regions.Americas.South America     0.762
		Geography.Regions.Asia.Asia*                 0.708
		Geography.Regions.Asia.Central Asia          0.539
		Geography.Regions.Asia.East Asia             0.583
		Geography.Regions.Asia.North Asia            0.331
		Geography.Regions.Asia.South Asia            0.875
		Geography.Regions.Asia.Southeast Asia        0.78
		Geography.Regions.Asia.West Asia             0.798
		Geography.Regions.Europe.Eastern Europe      0.77
		Geography.Regions.Europe.Europe*             0.76
		Geography.Regions.Europe.Northern Europe     0.782
		Geography.Regions.Europe.Southern Europe     0.746
		Geography.Regions.Europe.Western Europe      0.748
		Geography.Regions.Oceania                    0.851
		History and Society.Business and economics   0.593
		History and Society.Education                0.726
		History and Society.History                  0.538
		History and Society.Military and warfare     0.658
		History and Society.Politics and government  0.661
		History and Society.Society                  0.485
		History and Society.Transportation           0.878
		STEM.Biology                                 0.884
		STEM.Chemistry                               0.601
		STEM.Computing                               0.439
		STEM.Earth and environment                   0.725
		STEM.Engineering                             0.707
		STEM.Libraries & Information                 0.567
		STEM.Mathematics                             0.538
		STEM.Medicine & Health                       0.735
		STEM.Physics                                 0.41
		STEM.STEM*                                   0.838
		STEM.Space                                   0.926
		STEM.Technology                              0.443
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.987
		STEM.Space                                   1
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.988
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.982
		History and Society.Society                  0.985
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.001
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.003
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.028
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.03
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.009
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.01
		History and Society.Transportation           0.002
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.019
		STEM.Space                                   0
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.98, macro=0.979):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.99
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.987
		Culture.Literature                           0.982
		Culture.Media.Books                          0.988
		Culture.Media.Entertainment                  0.979
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.984
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.981
		Culture.Philosophy and religion              0.969
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.985
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.77
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.984
		Geography.Regions.Africa.Southern Africa     0.981
		Geography.Regions.Africa.Western Africa      0.969
		Geography.Regions.Americas.Central America   0.984
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.984
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.989
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.985
		Geography.Regions.Asia.West Asia             0.985
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.982
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.975
		History and Society.Education                0.982
		History and Society.History                  0.967
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.969
		History and Society.Society                  0.949
		History and Society.Transportation           0.987
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.989
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.987
		STEM.Engineering                             0.984
		STEM.Libraries & Information                 0.987
		STEM.Mathematics                             0.988
		STEM.Medicine & Health                       0.987
		STEM.Physics                                 0.989
		STEM.STEM*                                   0.981
		STEM.Space                                   0.993
		STEM.Technology                              0.981
		-------------------------------------------  -----
	pr_auc (micro=0.836, macro=0.725):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.707
		Culture.Food and drink                       0.798
		Culture.Internet culture                     0.777
		Culture.Linguistics                          0.844
		Culture.Literature                           0.804
		Culture.Media.Books                          0.816
		Culture.Media.Entertainment                  0.542
		Culture.Media.Films                          0.889
		Culture.Media.Media*                         0.877
		Culture.Media.Music                          0.86
		Culture.Media.Radio                          0.723
		Culture.Media.Software                       0.523
		Culture.Media.Television                     0.783
		Culture.Media.Video games                    0.895
		Culture.Performing arts                      0.636
		Culture.Philosophy and religion              0.651
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.815
		Culture.Visual arts.Comics and Anime         0.845
		Culture.Visual arts.Fashion                  0.487
		Culture.Visual arts.Visual arts*             0.807
		Geography.Geographical                       0.72
		Geography.Regions.Africa.Africa*             0.75
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.309
		Geography.Regions.Africa.Northern Africa     0.557
		Geography.Regions.Africa.Southern Africa     0.708
		Geography.Regions.Africa.Western Africa      0.361
		Geography.Regions.Americas.Central America   0.768
		Geography.Regions.Americas.North America     0.769
		Geography.Regions.Americas.South America     0.799
		Geography.Regions.Asia.Asia*                 0.815
		Geography.Regions.Asia.Central Asia          0.681
		Geography.Regions.Asia.East Asia             0.681
		Geography.Regions.Asia.North Asia            0.517
		Geography.Regions.Asia.South Asia            0.917
		Geography.Regions.Asia.Southeast Asia        0.822
		Geography.Regions.Asia.West Asia             0.834
		Geography.Regions.Europe.Eastern Europe      0.832
		Geography.Regions.Europe.Europe*             0.837
		Geography.Regions.Europe.Northern Europe     0.847
		Geography.Regions.Europe.Southern Europe     0.799
		Geography.Regions.Europe.Western Europe      0.795
		Geography.Regions.Oceania                    0.896
		History and Society.Business and economics   0.595
		History and Society.Education                0.739
		History and Society.History                  0.595
		History and Society.Military and warfare     0.756
		History and Society.Politics and government  0.705
		History and Society.Society                  0.474
		History and Society.Transportation           0.905
		STEM.Biology                                 0.94
		STEM.Chemistry                               0.661
		STEM.Computing                               0.541
		STEM.Earth and environment                   0.788
		STEM.Engineering                             0.771
		STEM.Libraries & Information                 0.554
		STEM.Mathematics                             0.597
		STEM.Medicine & Health                       0.804
		STEM.Physics                                 0.517
		STEM.STEM*                                   0.929
		STEM.Space                                   0.953
		STEM.Technology                              0.581
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

