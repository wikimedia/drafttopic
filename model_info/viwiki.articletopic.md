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
	counts (n=60764):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14139  -->  12644  1495   784  45841
			'Culture.Biography.Women'                       5153  -->   4121  1032   763  54848
			'Culture.Food and drink'                        1399  -->   1015   384   117  59248
			'Culture.Internet culture'                      3531  -->   2926   605   232  57001
			'Culture.Linguistics'                           1509  -->   1184   325    83  59172
			'Culture.Literature'                            5659  -->   4417  1242   454  54651
			'Culture.Media.Books'                           1467  -->   1079   388   117  59180
			'Culture.Media.Entertainment'                   1984  -->   1033   951   193  58587
			'Culture.Media.Films'                           2612  -->   2080   532   164  57988
			'Culture.Media.Media*'                         13270  -->  11677  1593  1279  46215
			'Culture.Media.Music'                           2908  -->   2503   405   183  57673
			'Culture.Media.Radio'                            285  -->    174   111    32  60447
			'Culture.Media.Software'                        2291  -->   1873   418   273  58200
			'Culture.Media.Television'                      1983  -->   1425   558   132  58649
			'Culture.Media.Video games'                     2139  -->   1962   177    58  58567
			'Culture.Performing arts'                       1374  -->    940   434   124  59266
			'Culture.Philosophy and religion'               3040  -->   1717  1323   280  57444
			'Culture.Sports'                                3871  -->   3413   458    96  56797
			'Culture.Visual arts.Architecture'              1854  -->   1342   512   163  58747
			'Culture.Visual arts.Comics and Anime'          2239  -->   2046   193    77  58448
			'Culture.Visual arts.Fashion'                   1501  -->   1217   284   104  59159
			'Culture.Visual arts.Visual arts*'              6119  -->   4723  1396   404  54241
			'Geography.Geographical'                        3991  -->   2604  1387   527  56246
			'Geography.Regions.Africa.Africa*'              5744  -->   4457  1287   489  54531
			'Geography.Regions.Africa.Central Africa'       1214  -->    823   391   125  59425
			'Geography.Regions.Africa.Eastern Africa'        451  -->    231   220    55  60258
			'Geography.Regions.Africa.Northern Africa'      1474  -->   1041   433    99  59191
			'Geography.Regions.Africa.Southern Africa'      1178  -->    797   381    67  59519
			'Geography.Regions.Africa.Western Africa'        672  -->    529   143    51  60041
			'Geography.Regions.Americas.Central America'    1588  -->    989   599   101  59075
			'Geography.Regions.Americas.North America'      5438  -->   3685  1753   607  54719
			'Geography.Regions.Americas.South America'      2210  -->   1699   511   177  58377
			'Geography.Regions.Asia.Asia*'                 13867  -->  11664  2203  1213  45684
			'Geography.Regions.Asia.Central Asia'           1211  -->    947   264    79  59474
			'Geography.Regions.Asia.East Asia'              5571  -->   4462  1109   473  54720
			'Geography.Regions.Asia.North Asia'             1693  -->   1264   429   222  58849
			'Geography.Regions.Asia.South Asia'             2038  -->   1603   435   120  58606
			'Geography.Regions.Asia.Southeast Asia'         2632  -->   1976   656   184  57948
			'Geography.Regions.Asia.West Asia'              2178  -->   1749   429    92  58494
			'Geography.Regions.Europe.Eastern Europe'       3590  -->   2856   734   272  56902
			'Geography.Regions.Europe.Europe*'             12682  -->  10198  2484  1206  46876
			'Geography.Regions.Europe.Northern Europe'      2896  -->   1823  1073   263  57605
			'Geography.Regions.Europe.Southern Europe'      2854  -->   2125   729   204  57706
			'Geography.Regions.Europe.Western Europe'       4043  -->   3153   890   242  56479
			'Geography.Regions.Oceania'                     2238  -->   1657   581   127  58399
			'History and Society.Business and economics'    3404  -->   2076  1328   352  57008
			'History and Society.Education'                 1589  -->    916   673   118  59057
			'History and Society.History'                   4595  -->   2476  2119   550  55619
			'History and Society.Military and warfare'      5048  -->   3964  1084   442  55274
			'History and Society.Politics and government'   4595  -->   2596  1999   506  55663
			'History and Society.Society'                   6148  -->   2959  3189   515  54101
			'History and Society.Transportation'            3573  -->   3290   283    64  57127
			'STEM.Biology'                                  7137  -->   6591   546   166  53461
			'STEM.Chemistry'                                1506  -->   1177   329   165  59093
			'STEM.Computing'                                2452  -->   2056   396   288  58024
			'STEM.Earth and environment'                    1649  -->   1114   535   132  58983
			'STEM.Engineering'                              3027  -->   2511   516   144  57593
			'STEM.Libraries & Information'                   489  -->    361   128    33  60242
			'STEM.Mathematics'                               942  -->    774   168    53  59769
			'STEM.Medicine & Health'                        1774  -->   1257   517   154  58836
			'STEM.Physics'                                  1374  -->   1036   338   162  59228
			'STEM.STEM*'                                   20595  -->  18909  1686   857  39312
			'STEM.Space'                                    1637  -->   1485   152    28  59099
			'STEM.Technology'                               4233  -->   3131  1102   581  55950
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.218         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.05          0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.095         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.228         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
		Geography.Regions.Asia.North Asia               0.028         0.001
		Geography.Regions.Asia.South Asia               0.034         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.059         0.013
		Geography.Regions.Europe.Europe*                0.209         0.076
		Geography.Regions.Europe.Northern Europe        0.048         0.031
		Geography.Regions.Europe.Southern Europe        0.047         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.026         0.007
		History and Society.History                     0.076         0.011
		History and Society.Military and warfare        0.083         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.117         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.339         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.063
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.084
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.025
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
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
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.937
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.916
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.975
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
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
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.795, macro=0.75):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.894
		Culture.Biography.Women                      0.8
		Culture.Food and drink                       0.726
		Culture.Internet culture                     0.829
		Culture.Linguistics                          0.785
		Culture.Literature                           0.781
		Culture.Media.Books                          0.736
		Culture.Media.Entertainment                  0.521
		Culture.Media.Films                          0.796
		Culture.Media.Media*                         0.88
		Culture.Media.Music                          0.861
		Culture.Media.Radio                          0.611
		Culture.Media.Software                       0.818
		Culture.Media.Television                     0.719
		Culture.Media.Video games                    0.917
		Culture.Performing arts                      0.684
		Culture.Philosophy and religion              0.565
		Culture.Sports                               0.882
		Culture.Visual arts.Architecture             0.724
		Culture.Visual arts.Comics and Anime         0.914
		Culture.Visual arts.Fashion                  0.811
		Culture.Visual arts.Visual arts*             0.772
		Geography.Geographical                       0.652
		Geography.Regions.Africa.Africa*             0.776
		Geography.Regions.Africa.Central Africa      0.678
		Geography.Regions.Africa.Eastern Africa      0.512
		Geography.Regions.Africa.Northern Africa     0.706
		Geography.Regions.Africa.Southern Africa     0.677
		Geography.Regions.Africa.Western Africa      0.787
		Geography.Regions.Americas.Central America   0.623
		Geography.Regions.Americas.North America     0.678
		Geography.Regions.Americas.South America     0.769
		Geography.Regions.Asia.Asia*                 0.841
		Geography.Regions.Asia.Central Asia          0.782
		Geography.Regions.Asia.East Asia             0.801
		Geography.Regions.Asia.North Asia            0.747
		Geography.Regions.Asia.South Asia            0.787
		Geography.Regions.Asia.Southeast Asia        0.751
		Geography.Regions.Asia.West Asia             0.803
		Geography.Regions.Europe.Eastern Europe      0.796
		Geography.Regions.Europe.Europe*             0.804
		Geography.Regions.Europe.Northern Europe     0.629
		Geography.Regions.Europe.Southern Europe     0.745
		Geography.Regions.Europe.Western Europe      0.78
		Geography.Regions.Oceania                    0.74
		History and Society.Business and economics   0.61
		History and Society.Education                0.576
		History and Society.History                  0.539
		History and Society.Military and warfare     0.785
		History and Society.Politics and government  0.565
		History and Society.Society                  0.481
		History and Society.Transportation           0.921
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.782
		STEM.Computing                               0.838
		STEM.Earth and environment                   0.676
		STEM.Engineering                             0.83
		STEM.Libraries & Information                 0.738
		STEM.Mathematics                             0.822
		STEM.Medicine & Health                       0.709
		STEM.Physics                                 0.754
		STEM.STEM*                                   0.918
		STEM.Space                                   0.907
		STEM.Technology                              0.74
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.993
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
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.979
		STEM.Space                                   1
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.738, macro=0.577):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.882
		Culture.Biography.Women                      0.463
		Culture.Food and drink                       0.476
		Culture.Internet culture                     0.418
		Culture.Linguistics                          0.805
		Culture.Literature                           0.599
		Culture.Media.Books                          0.601
		Culture.Media.Entertainment                  0.363
		Culture.Media.Films                          0.75
		Culture.Media.Media*                         0.67
		Culture.Media.Music                          0.869
		Culture.Media.Radio                          0.714
		Culture.Media.Software                       0.189
		Culture.Media.Television                     0.74
		Culture.Media.Video games                    0.708
		Culture.Performing arts                      0.487
		Culture.Philosophy and religion              0.556
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.736
		Culture.Visual arts.Comics and Anime         0.605
		Culture.Visual arts.Fashion                  0.272
		Culture.Visual arts.Visual arts*             0.66
		Geography.Geographical                       0.629
		Geography.Regions.Africa.Africa*             0.407
		Geography.Regions.Africa.Central Africa      0.17
		Geography.Regions.Africa.Eastern Africa      0.204
		Geography.Regions.Africa.Northern Africa     0.342
		Geography.Regions.Africa.Southern Africa     0.414
		Geography.Regions.Africa.Western Africa      0.388
		Geography.Regions.Americas.Central America   0.547
		Geography.Regions.Americas.North America     0.809
		Geography.Regions.Americas.South America     0.617
		Geography.Regions.Asia.Asia*                 0.608
		Geography.Regions.Asia.Central Asia          0.338
		Geography.Regions.Asia.East Asia             0.519
		Geography.Regions.Asia.North Asia            0.155
		Geography.Regions.Asia.South Asia            0.856
		Geography.Regions.Asia.Southeast Asia        0.589
		Geography.Regions.Asia.West Asia             0.849
		Geography.Regions.Europe.Eastern Europe      0.685
		Geography.Regions.Europe.Europe*             0.726
		Geography.Regions.Europe.Northern Europe     0.814
		Geography.Regions.Europe.Southern Europe     0.736
		Geography.Regions.Europe.Western Europe      0.781
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.503
		History and Society.Education                0.682
		History and Society.History                  0.376
		History and Society.Military and warfare     0.585
		History and Society.Politics and government  0.645
		History and Society.Society                  0.395
		History and Society.Transportation           0.926
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.305
		STEM.Computing                               0.314
		STEM.Earth and environment                   0.58
		STEM.Engineering                             0.636
		STEM.Libraries & Information                 0.456
		STEM.Mathematics                             0.279
		STEM.Medicine & Health                       0.636
		STEM.Physics                                 0.19
		STEM.STEM*                                   0.762
		STEM.Space                                   0.921
		STEM.Technology                              0.271
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.758, macro=0.63):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.888
		Culture.Biography.Women                      0.586
		Culture.Food and drink                       0.575
		Culture.Internet culture                     0.556
		Culture.Linguistics                          0.795
		Culture.Literature                           0.678
		Culture.Media.Books                          0.662
		Culture.Media.Entertainment                  0.428
		Culture.Media.Films                          0.773
		Culture.Media.Media*                         0.761
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.658
		Culture.Media.Software                       0.307
		Culture.Media.Television                     0.729
		Culture.Media.Video games                    0.799
		Culture.Performing arts                      0.569
		Culture.Philosophy and religion              0.56
		Culture.Sports                               0.926
		Culture.Visual arts.Architecture             0.73
		Culture.Visual arts.Comics and Anime         0.728
		Culture.Visual arts.Fashion                  0.408
		Culture.Visual arts.Visual arts*             0.712
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.534
		Geography.Regions.Africa.Central Africa      0.271
		Geography.Regions.Africa.Eastern Africa      0.291
		Geography.Regions.Africa.Northern Africa     0.461
		Geography.Regions.Africa.Southern Africa     0.514
		Geography.Regions.Africa.Western Africa      0.52
		Geography.Regions.Americas.Central America   0.582
		Geography.Regions.Americas.North America     0.738
		Geography.Regions.Americas.South America     0.685
		Geography.Regions.Asia.Asia*                 0.706
		Geography.Regions.Asia.Central Asia          0.472
		Geography.Regions.Asia.East Asia             0.63
		Geography.Regions.Asia.North Asia            0.257
		Geography.Regions.Asia.South Asia            0.82
		Geography.Regions.Asia.Southeast Asia        0.66
		Geography.Regions.Asia.West Asia             0.826
		Geography.Regions.Europe.Eastern Europe      0.736
		Geography.Regions.Europe.Europe*             0.763
		Geography.Regions.Europe.Northern Europe     0.71
		Geography.Regions.Europe.Southern Europe     0.74
		Geography.Regions.Europe.Western Europe      0.781
		Geography.Regions.Oceania                    0.787
		History and Society.Business and economics   0.551
		History and Society.Education                0.625
		History and Society.History                  0.443
		History and Society.Military and warfare     0.671
		History and Society.Politics and government  0.602
		History and Society.Society                  0.434
		History and Society.Transportation           0.924
		STEM.Biology                                 0.918
		STEM.Chemistry                               0.438
		STEM.Computing                               0.457
		STEM.Earth and environment                   0.624
		STEM.Engineering                             0.72
		STEM.Libraries & Information                 0.564
		STEM.Mathematics                             0.416
		STEM.Medicine & Health                       0.67
		STEM.Physics                                 0.304
		STEM.STEM*                                   0.833
		STEM.Space                                   0.914
		STEM.Technology                              0.396
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
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
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.986
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.981, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.985
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.979
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.007
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
		Geography.Regions.Asia.Asia*                 0.026
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.009
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.025
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.021
		STEM.Space                                   0
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.978
		Culture.Literature                           0.98
		Culture.Media.Books                          0.982
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.95
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.98
		Culture.Philosophy and religion              0.963
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.99
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.969
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.977
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.984
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.98
		Geography.Regions.Asia.West Asia             0.982
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.98
		History and Society.Business and economics   0.971
		History and Society.Education                0.975
		History and Society.History                  0.956
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.956
		History and Society.Society                  0.94
		History and Society.Transportation           0.988
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.987
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.984
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.981
		STEM.Space                                   0.993
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.81, macro=0.652):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.94
		Culture.Biography.Women                      0.578
		Culture.Food and drink                       0.61
		Culture.Internet culture                     0.729
		Culture.Linguistics                          0.787
		Culture.Literature                           0.758
		Culture.Media.Books                          0.683
		Culture.Media.Entertainment                  0.424
		Culture.Media.Films                          0.79
		Culture.Media.Media*                         0.856
		Culture.Media.Music                          0.898
		Culture.Media.Radio                          0.469
		Culture.Media.Software                       0.372
		Culture.Media.Television                     0.74
		Culture.Media.Video games                    0.901
		Culture.Performing arts                      0.578
		Culture.Philosophy and religion              0.554
		Culture.Sports                               0.962
		Culture.Visual arts.Architecture             0.759
		Culture.Visual arts.Comics and Anime         0.807
		Culture.Visual arts.Fashion                  0.362
		Culture.Visual arts.Visual arts*             0.757
		Geography.Geographical                       0.695
		Geography.Regions.Africa.Africa*             0.607
		Geography.Regions.Africa.Central Africa      0.193
		Geography.Regions.Africa.Eastern Africa      0.125
		Geography.Regions.Africa.Northern Africa     0.437
		Geography.Regions.Africa.Southern Africa     0.42
		Geography.Regions.Africa.Western Africa      0.404
		Geography.Regions.Americas.Central America   0.555
		Geography.Regions.Americas.North America     0.804
		Geography.Regions.Americas.South America     0.687
		Geography.Regions.Asia.Asia*                 0.791
		Geography.Regions.Asia.Central Asia          0.428
		Geography.Regions.Asia.East Asia             0.632
		Geography.Regions.Asia.North Asia            0.227
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.664
		Geography.Regions.Asia.West Asia             0.867
		Geography.Regions.Europe.Eastern Europe      0.817
		Geography.Regions.Europe.Europe*             0.847
		Geography.Regions.Europe.Northern Europe     0.778
		Geography.Regions.Europe.Southern Europe     0.78
		Geography.Regions.Europe.Western Europe      0.83
		Geography.Regions.Oceania                    0.835
		History and Society.Business and economics   0.553
		History and Society.Education                0.647
		History and Society.History                  0.416
		History and Society.Military and warfare     0.739
		History and Society.Politics and government  0.649
		History and Society.Society                  0.431
		History and Society.Transportation           0.96
		STEM.Biology                                 0.959
		STEM.Chemistry                               0.529
		STEM.Computing                               0.44
		STEM.Earth and environment                   0.634
		STEM.Engineering                             0.827
		STEM.Libraries & Information                 0.472
		STEM.Mathematics                             0.537
		STEM.Medicine & Health                       0.681
		STEM.Physics                                 0.345
		STEM.STEM*                                   0.909
		STEM.Space                                   0.954
		STEM.Technology                              0.461
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

