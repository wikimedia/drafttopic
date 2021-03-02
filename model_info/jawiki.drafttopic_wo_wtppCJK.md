Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'max_features': 'log2', 'init': None, 'presort': 'deprecated', 'validation_fraction': 0.1, 'subsample': 1.0, 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'learning_rate': 0.1, 'min_impurity_decrease': 0.0, 'random_state': None, 'scale': False, 'min_samples_leaf': 1, 'label_weights': {}, 'max_leaf_nodes': None, 'tol': 0.0001, 'criterion': 'friedman_mse', 'n_estimators': 150, 'warm_start': False, 'population_rates': None, 'verbose': 0, 'ccp_alpha': 0.0, 'n_iter_no_change': None, 'loss': 'deviance', 'center': False, 'max_depth': 5, 'min_samples_split': 2, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=59389):
			label                                              n         TP     FP    FN     TN
			---------------------------------------------  -----  ---  ----  -----  ----  -----
			'Culture.Biography.Biography*'                 17601  -->  7777   9824  2534  39254
			'Culture.Biography.Women'                       3879  -->   497   3382   189  55321
			'Culture.Food and drink'                        1483  -->    87   1396    62  57844
			'Culture.Internet culture'                      3043  -->  1106   1937   227  56119
			'Culture.Linguistics'                           1586  -->   431   1155    87  57716
			'Culture.Literature'                            5594  -->   527   5067   235  53560
			'Culture.Media.Books'                           1544  -->    85   1459    75  57770
			'Culture.Media.Entertainment'                   2182  -->   392   1790   106  57101
			'Culture.Media.Films'                           2629  -->   994   1635   187  56573
			'Culture.Media.Media*'                         14040  -->  6697   7343  1923  43426
			'Culture.Media.Music'                           3171  -->   872   2299   300  55918
			'Culture.Media.Radio'                            787  -->   185    602    86  58516
			'Culture.Media.Software'                        1888  -->   922    966   304  57197
			'Culture.Media.Television'                      2061  -->   510   1551   142  57186
			'Culture.Media.Video games'                     2181  -->   908   1273   153  57055
			'Culture.Performing arts'                       1414  -->    54   1360    63  57912
			'Culture.Philosophy and religion'               3192  -->    54   3138    58  56139
			'Culture.Sports'                                6570  -->  3686   2884   467  52352
			'Culture.Visual arts.Architecture'              1987  -->   260   1727   108  57294
			'Culture.Visual arts.Comics and Anime'          2405  -->   397   2008   132  56852
			'Culture.Visual arts.Fashion'                   1194  -->   139   1055    76  58119
			'Culture.Visual arts.Visual arts*'              6154  -->   713   5441   250  52985
			'Geography.Geographical'                        3395  -->   584   2811   207  55787
			'Geography.Regions.Africa.Africa*'              4858  -->   323   4535   115  54416
			'Geography.Regions.Africa.Central Africa'       1162  -->   130   1032    48  58179
			'Geography.Regions.Africa.Eastern Africa'        583  -->    95    488    54  58752
			'Geography.Regions.Africa.Northern Africa'      1377  -->   109   1268    42  57970
			'Geography.Regions.Africa.Southern Africa'      1002  -->   177    825    69  58318
			'Geography.Regions.Africa.Western Africa'        339  -->    71    268    60  58990
			'Geography.Regions.Americas.Central America'    1301  -->    68   1233    66  58022
			'Geography.Regions.Americas.North America'      5960  -->   824   5136   515  52914
			'Geography.Regions.Americas.South America'      1491  -->    84   1407    86  57812
			'Geography.Regions.Asia.Asia*'                 15101  -->  3619  11482  1421  42867
			'Geography.Regions.Asia.Central Asia'           1181  -->    86   1095    42  58166
			'Geography.Regions.Asia.East Asia'              7203  -->  1410   5793   597  51589
			'Geography.Regions.Asia.North Asia'             2820  -->   735   2085   219  56350
			'Geography.Regions.Asia.South Asia'             1640  -->   205   1435    63  57686
			'Geography.Regions.Asia.Southeast Asia'         1670  -->    86   1584    42  57677
			'Geography.Regions.Asia.West Asia'              1924  -->    96   1828    40  57425
			'Geography.Regions.Europe.Eastern Europe'       3865  -->   841   3024   253  55271
			'Geography.Regions.Europe.Europe*'             13524  -->  4143   9381  1880  43985
			'Geography.Regions.Europe.Northern Europe'      3345  -->   223   3122   117  55927
			'Geography.Regions.Europe.Southern Europe'      2992  -->   532   2460   149  56248
			'Geography.Regions.Europe.Western Europe'       4149  -->  1013   3136   425  54815
			'Geography.Regions.Oceania'                     1575  -->   124   1451    62  57752
			'History and Society.Business and economics'    3752  -->   238   3514   117  55520
			'History and Society.Education'                 1907  -->   356   1551    84  57398
			'History and Society.History'                   4604  -->   298   4306   141  54644
			'History and Society.Military and warfare'      4643  -->   799   3844   202  54544
			'History and Society.Politics and government'   3373  -->   170   3203    87  55929
			'History and Society.Society'                   3974  -->   126   3848    53  55362
			'History and Society.Transportation'            4763  -->  1877   2886   308  54318
			'STEM.Biology'                                  2779  -->   656   2123   139  56471
			'STEM.Chemistry'                                1414  -->   409   1005   164  57811
			'STEM.Computing'                                2448  -->  1048   1400   366  56575
			'STEM.Earth and environment'                    1773  -->    90   1683    56  57560
			'STEM.Engineering'                              2886  -->   889   1997   154  56349
			'STEM.Libraries & Information'                   957  -->   191    766    45  58387
			'STEM.Mathematics'                              1092  -->   225    867    97  58200
			'STEM.Medicine & Health'                        1855  -->   297   1558   127  57407
			'STEM.Physics'                                  1300  -->   100   1200    90  57999
			'STEM.STEM*'                                   17046  -->  7936   9110  1774  40569
			'STEM.Space'                                    1825  -->   728   1097    93  57471
			'STEM.Technology'                               4199  -->  1277   2922   437  54753
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.296         0.121
		Culture.Biography.Women                         0.065         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.051         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.044         0.012
		Culture.Media.Media*                            0.236         0.055
		Culture.Media.Music                             0.053         0.021
		Culture.Media.Radio                             0.013         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.01
		Culture.Sports                                  0.111         0.061
		Culture.Visual arts.Architecture                0.033         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.02          0.001
		Culture.Visual arts.Visual arts*                0.104         0.018
		Geography.Geographical                          0.057         0.021
		Geography.Regions.Africa.Africa*                0.082         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.01          0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.017         0.001
		Geography.Regions.Africa.Western Africa         0.006         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.254         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.121         0.012
		Geography.Regions.Asia.North Asia               0.047         0.006
		Geography.Regions.Asia.South Asia               0.028         0.017
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.065         0.018
		Geography.Regions.Europe.Europe*                0.228         0.082
		Geography.Regions.Europe.Northern Europe        0.056         0.029
		Geography.Regions.Europe.Southern Europe        0.05          0.014
		Geography.Regions.Europe.Western Europe         0.07          0.021
		Geography.Regions.Oceania                       0.027         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.078         0.011
		History and Society.Military and warfare        0.078         0.015
		History and Society.Politics and government     0.057         0.016
		History and Society.Society                     0.067         0.008
		History and Society.Transportation              0.08          0.016
		STEM.Biology                                    0.047         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.016         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.031         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.287         0.066
		STEM.Space                                      0.031         0.004
		STEM.Technology                                 0.071         0.005
	match_rate (micro=0.035, macro=0.01):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.107
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.004
		Culture.Literature                           0.006
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.008
		Culture.Media.Media*                         0.066
		Culture.Media.Music                          0.011
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.005
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.042
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.007
		Geography.Regions.Africa.Africa*             0.003
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.043
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.003
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.008
		Geography.Regions.Europe.Europe*             0.063
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.013
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.003
		History and Society.Education                0.003
		History and Society.History                  0.003
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.002
		History and Society.Society                  0.001
		History and Society.Transportation           0.012
		STEM.Biology                                 0.011
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.07
		STEM.Space                                   0.003
		STEM.Technology                              0.009
		-------------------------------------------  -----
	filter_rate (micro=0.965, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.893
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.992
		Culture.Media.Media*                         0.934
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.937
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.997
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.998
		History and Society.Society                  0.999
		History and Society.Transportation           0.988
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.93
		STEM.Space                                   0.997
		STEM.Technology                              0.991
		-------------------------------------------  -----
	recall (micro=0.275, macro=0.198):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.442
		Culture.Biography.Women                      0.128
		Culture.Food and drink                       0.059
		Culture.Internet culture                     0.363
		Culture.Linguistics                          0.272
		Culture.Literature                           0.094
		Culture.Media.Books                          0.055
		Culture.Media.Entertainment                  0.18
		Culture.Media.Films                          0.378
		Culture.Media.Media*                         0.477
		Culture.Media.Music                          0.275
		Culture.Media.Radio                          0.235
		Culture.Media.Software                       0.488
		Culture.Media.Television                     0.247
		Culture.Media.Video games                    0.416
		Culture.Performing arts                      0.038
		Culture.Philosophy and religion              0.017
		Culture.Sports                               0.561
		Culture.Visual arts.Architecture             0.131
		Culture.Visual arts.Comics and Anime         0.165
		Culture.Visual arts.Fashion                  0.116
		Culture.Visual arts.Visual arts*             0.116
		Geography.Geographical                       0.172
		Geography.Regions.Africa.Africa*             0.066
		Geography.Regions.Africa.Central Africa      0.112
		Geography.Regions.Africa.Eastern Africa      0.163
		Geography.Regions.Africa.Northern Africa     0.079
		Geography.Regions.Africa.Southern Africa     0.177
		Geography.Regions.Africa.Western Africa      0.209
		Geography.Regions.Americas.Central America   0.052
		Geography.Regions.Americas.North America     0.138
		Geography.Regions.Americas.South America     0.056
		Geography.Regions.Asia.Asia*                 0.24
		Geography.Regions.Asia.Central Asia          0.073
		Geography.Regions.Asia.East Asia             0.196
		Geography.Regions.Asia.North Asia            0.261
		Geography.Regions.Asia.South Asia            0.125
		Geography.Regions.Asia.Southeast Asia        0.051
		Geography.Regions.Asia.West Asia             0.05
		Geography.Regions.Europe.Eastern Europe      0.218
		Geography.Regions.Europe.Europe*             0.306
		Geography.Regions.Europe.Northern Europe     0.067
		Geography.Regions.Europe.Southern Europe     0.178
		Geography.Regions.Europe.Western Europe      0.244
		Geography.Regions.Oceania                    0.079
		History and Society.Business and economics   0.063
		History and Society.Education                0.187
		History and Society.History                  0.065
		History and Society.Military and warfare     0.172
		History and Society.Politics and government  0.05
		History and Society.Society                  0.032
		History and Society.Transportation           0.394
		STEM.Biology                                 0.236
		STEM.Chemistry                               0.289
		STEM.Computing                               0.428
		STEM.Earth and environment                   0.051
		STEM.Engineering                             0.308
		STEM.Libraries & Information                 0.2
		STEM.Mathematics                             0.206
		STEM.Medicine & Health                       0.16
		STEM.Physics                                 0.077
		STEM.STEM*                                   0.466
		STEM.Space                                   0.399
		STEM.Technology                              0.304
		-------------------------------------------  -----
	!recall (micro=0.98, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.939
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.996
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.99
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.998
		History and Society.Education                0.999
		History and Society.History                  0.997
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.998
		History and Society.Society                  0.999
		History and Society.Transportation           0.994
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.958
		STEM.Space                                   0.998
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.447, macro=0.317):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.502
		Culture.Biography.Women                      0.366
		Culture.Food and drink                       0.124
		Culture.Internet culture                     0.254
		Culture.Linguistics                          0.596
		Culture.Literature                           0.247
		Culture.Media.Books                          0.157
		Culture.Media.Entertainment                  0.279
		Culture.Media.Films                          0.575
		Culture.Media.Media*                         0.397
		Culture.Media.Music                          0.527
		Culture.Media.Radio                          0.274
		Culture.Media.Software                       0.109
		Culture.Media.Television                     0.475
		Culture.Media.Video games                    0.314
		Culture.Performing arts                      0.098
		Culture.Philosophy and religion              0.148
		Culture.Sports                               0.805
		Culture.Visual arts.Architecture             0.434
		Culture.Visual arts.Comics and Anime         0.147
		Culture.Visual arts.Fashion                  0.075
		Culture.Visual arts.Visual arts*             0.314
		Geography.Geographical                       0.504
		Geography.Regions.Africa.Africa*             0.214
		Geography.Regions.Africa.Central Africa      0.088
		Geography.Regions.Africa.Eastern Africa      0.083
		Geography.Regions.Africa.Northern Africa     0.13
		Geography.Regions.Africa.Southern Africa     0.165
		Geography.Regions.Africa.Western Africa      0.134
		Geography.Regions.Americas.Central America   0.139
		Geography.Regions.Americas.North America     0.494
		Geography.Regions.Americas.South America     0.209
		Geography.Regions.Asia.Asia*                 0.295
		Geography.Regions.Asia.Central Asia          0.075
		Geography.Regions.Asia.East Asia             0.175
		Geography.Regions.Asia.North Asia            0.277
		Geography.Regions.Asia.South Asia            0.66
		Geography.Regions.Asia.Southeast Asia        0.31
		Geography.Regions.Asia.West Asia             0.461
		Geography.Regions.Europe.Eastern Europe      0.473
		Geography.Regions.Europe.Europe*             0.399
		Geography.Regions.Europe.Northern Europe     0.49
		Geography.Regions.Europe.Southern Europe     0.489
		Geography.Regions.Europe.Western Europe      0.401
		Geography.Regions.Oceania                    0.553
		History and Society.Business and economics   0.23
		History and Society.Education                0.507
		History and Society.History                  0.218
		History and Society.Military and warfare     0.423
		History and Society.Politics and government  0.352
		History and Society.Society                  0.218
		History and Society.Transportation           0.539
		STEM.Biology                                 0.776
		STEM.Chemistry                               0.149
		STEM.Computing                               0.16
		STEM.Earth and environment                   0.2
		STEM.Engineering                             0.397
		STEM.Libraries & Information                 0.152
		STEM.Mathematics                             0.055
		STEM.Medicine & Health                       0.322
		STEM.Physics                                 0.045
		STEM.STEM*                                   0.438
		STEM.Space                                   0.516
		STEM.Technology                              0.167
		-------------------------------------------  -----
	!precision (micro=0.968, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.924
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.994
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.972
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.958
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.99
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.99
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.962
		STEM.Space                                   0.997
		STEM.Technology                              0.996
		-------------------------------------------  -----
	f1 (micro=0.318, macro=0.215):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.47
		Culture.Biography.Women                      0.19
		Culture.Food and drink                       0.08
		Culture.Internet culture                     0.299
		Culture.Linguistics                          0.373
		Culture.Literature                           0.136
		Culture.Media.Books                          0.081
		Culture.Media.Entertainment                  0.219
		Culture.Media.Films                          0.456
		Culture.Media.Media*                         0.434
		Culture.Media.Music                          0.361
		Culture.Media.Radio                          0.253
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.325
		Culture.Media.Video games                    0.358
		Culture.Performing arts                      0.055
		Culture.Philosophy and religion              0.03
		Culture.Sports                               0.661
		Culture.Visual arts.Architecture             0.201
		Culture.Visual arts.Comics and Anime         0.156
		Culture.Visual arts.Fashion                  0.091
		Culture.Visual arts.Visual arts*             0.169
		Geography.Geographical                       0.256
		Geography.Regions.Africa.Africa*             0.101
		Geography.Regions.Africa.Central Africa      0.098
		Geography.Regions.Africa.Eastern Africa      0.11
		Geography.Regions.Africa.Northern Africa     0.098
		Geography.Regions.Africa.Southern Africa     0.171
		Geography.Regions.Africa.Western Africa      0.164
		Geography.Regions.Americas.Central America   0.076
		Geography.Regions.Americas.North America     0.216
		Geography.Regions.Americas.South America     0.089
		Geography.Regions.Asia.Asia*                 0.264
		Geography.Regions.Asia.Central Asia          0.074
		Geography.Regions.Asia.East Asia             0.185
		Geography.Regions.Asia.North Asia            0.269
		Geography.Regions.Asia.South Asia            0.21
		Geography.Regions.Asia.Southeast Asia        0.088
		Geography.Regions.Asia.West Asia             0.09
		Geography.Regions.Europe.Eastern Europe      0.298
		Geography.Regions.Europe.Europe*             0.347
		Geography.Regions.Europe.Northern Europe     0.117
		Geography.Regions.Europe.Southern Europe     0.261
		Geography.Regions.Europe.Western Europe      0.304
		Geography.Regions.Oceania                    0.138
		History and Society.Business and economics   0.099
		History and Society.Education                0.273
		History and Society.History                  0.1
		History and Society.Military and warfare     0.245
		History and Society.Politics and government  0.088
		History and Society.Society                  0.055
		History and Society.Transportation           0.455
		STEM.Biology                                 0.362
		STEM.Chemistry                               0.197
		STEM.Computing                               0.233
		STEM.Earth and environment                   0.081
		STEM.Engineering                             0.347
		STEM.Libraries & Information                 0.173
		STEM.Mathematics                             0.086
		STEM.Medicine & Health                       0.214
		STEM.Physics                                 0.057
		STEM.STEM*                                   0.452
		STEM.Space                                   0.45
		STEM.Technology                              0.216
		-------------------------------------------  -----
	!f1 (micro=0.974, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.932
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.996
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.992
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.96
		STEM.Space                                   0.998
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.951, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.982
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.931
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.965
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.936
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.929
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.983
		History and Society.Society                  0.991
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.926
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.02, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.061
		Culture.Biography.Women                      0.003
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.004
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.042
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.009
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.005
		Geography.Geographical                       0.004
		Geography.Regions.Africa.Africa*             0.002
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.01
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.032
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.041
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.002
		History and Society.Education                0.001
		History and Society.History                  0.003
		History and Society.Military and warfare     0.004
		History and Society.Politics and government  0.002
		History and Society.Society                  0.001
		History and Society.Transportation           0.006
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.042
		STEM.Space                                   0.002
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.819, macro=0.821):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.818
		Culture.Biography.Women                      0.81
		Culture.Food and drink                       0.804
		Culture.Internet culture                     0.886
		Culture.Linguistics                          0.837
		Culture.Literature                           0.786
		Culture.Media.Books                          0.812
		Culture.Media.Entertainment                  0.825
		Culture.Media.Films                          0.883
		Culture.Media.Media*                         0.848
		Culture.Media.Music                          0.863
		Culture.Media.Radio                          0.824
		Culture.Media.Software                       0.925
		Culture.Media.Television                     0.87
		Culture.Media.Video games                    0.903
		Culture.Performing arts                      0.797
		Culture.Philosophy and religion              0.758
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.823
		Culture.Visual arts.Comics and Anime         0.861
		Culture.Visual arts.Fashion                  0.789
		Culture.Visual arts.Visual arts*             0.773
		Geography.Geographical                       0.843
		Geography.Regions.Africa.Africa*             0.791
		Geography.Regions.Africa.Central Africa      0.845
		Geography.Regions.Africa.Eastern Africa      0.796
		Geography.Regions.Africa.Northern Africa     0.789
		Geography.Regions.Africa.Southern Africa     0.819
		Geography.Regions.Africa.Western Africa      0.803
		Geography.Regions.Americas.Central America   0.775
		Geography.Regions.Americas.North America     0.797
		Geography.Regions.Americas.South America     0.813
		Geography.Regions.Asia.Asia*                 0.785
		Geography.Regions.Asia.Central Asia          0.79
		Geography.Regions.Asia.East Asia             0.852
		Geography.Regions.Asia.North Asia            0.847
		Geography.Regions.Asia.South Asia            0.784
		Geography.Regions.Asia.Southeast Asia        0.774
		Geography.Regions.Asia.West Asia             0.768
		Geography.Regions.Europe.Eastern Europe      0.821
		Geography.Regions.Europe.Europe*             0.792
		Geography.Regions.Europe.Northern Europe     0.772
		Geography.Regions.Europe.Southern Europe     0.826
		Geography.Regions.Europe.Western Europe      0.835
		Geography.Regions.Oceania                    0.767
		History and Society.Business and economics   0.752
		History and Society.Education                0.825
		History and Society.History                  0.789
		History and Society.Military and warfare     0.811
		History and Society.Politics and government  0.758
		History and Society.Society                  0.714
		History and Society.Transportation           0.874
		STEM.Biology                                 0.846
		STEM.Chemistry                               0.865
		STEM.Computing                               0.901
		STEM.Earth and environment                   0.794
		STEM.Engineering                             0.845
		STEM.Libraries & Information                 0.833
		STEM.Mathematics                             0.848
		STEM.Medicine & Health                       0.822
		STEM.Physics                                 0.814
		STEM.STEM*                                   0.831
		STEM.Space                                   0.877
		STEM.Technology                              0.839
		-------------------------------------------  -----
	pr_auc (micro=0.311, macro=0.172):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.496
		Culture.Biography.Women                      0.16
		Culture.Food and drink                       0.029
		Culture.Internet culture                     0.245
		Culture.Linguistics                          0.274
		Culture.Literature                           0.11
		Culture.Media.Books                          0.044
		Culture.Media.Entertainment                  0.125
		Culture.Media.Films                          0.392
		Culture.Media.Media*                         0.41
		Culture.Media.Music                          0.326
		Culture.Media.Radio                          0.098
		Culture.Media.Software                       0.118
		Culture.Media.Television                     0.265
		Culture.Media.Video games                    0.277
		Culture.Performing arts                      0.022
		Culture.Philosophy and religion              0.04
		Culture.Sports                               0.688
		Culture.Visual arts.Architecture             0.158
		Culture.Visual arts.Comics and Anime         0.074
		Culture.Visual arts.Fashion                  0.015
		Culture.Visual arts.Visual arts*             0.137
		Geography.Geographical                       0.246
		Geography.Regions.Africa.Africa*             0.079
		Geography.Regions.Africa.Central Africa      0.034
		Geography.Regions.Africa.Eastern Africa      0.033
		Geography.Regions.Africa.Northern Africa     0.029
		Geography.Regions.Africa.Southern Africa     0.051
		Geography.Regions.Africa.Western Africa      0.037
		Geography.Regions.Americas.Central America   0.035
		Geography.Regions.Americas.North America     0.295
		Geography.Regions.Americas.South America     0.073
		Geography.Regions.Asia.Asia*                 0.23
		Geography.Regions.Asia.Central Asia          0.013
		Geography.Regions.Asia.East Asia             0.111
		Geography.Regions.Asia.North Asia            0.165
		Geography.Regions.Asia.South Asia            0.213
		Geography.Regions.Asia.Southeast Asia        0.069
		Geography.Regions.Asia.West Asia             0.112
		Geography.Regions.Europe.Eastern Europe      0.258
		Geography.Regions.Europe.Europe*             0.336
		Geography.Regions.Europe.Northern Europe     0.168
		Geography.Regions.Europe.Southern Europe     0.224
		Geography.Regions.Europe.Western Europe      0.239
		Geography.Regions.Oceania                    0.176
		History and Society.Business and economics   0.06
		History and Society.Education                0.207
		History and Society.History                  0.074
		History and Society.Military and warfare     0.198
		History and Society.Politics and government  0.089
		History and Society.Society                  0.047
		History and Society.Transportation           0.421
		STEM.Biology                                 0.414
		STEM.Chemistry                               0.076
		STEM.Computing                               0.124
		STEM.Earth and environment                   0.06
		STEM.Engineering                             0.28
		STEM.Libraries & Information                 0.048
		STEM.Mathematics                             0.025
		STEM.Medicine & Health                       0.14
		STEM.Physics                                 0.012
		STEM.STEM*                                   0.456
		STEM.Space                                   0.383
		STEM.Technology                              0.14
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Space': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

