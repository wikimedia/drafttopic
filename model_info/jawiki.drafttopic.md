Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'min_samples_leaf': 1, 'verbose': 0, 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'center': False, 'n_estimators': 150, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'max_features': 'log2', 'loss': 'deviance', 'min_impurity_split': None, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'random_state': None, 'validation_fraction': 0.1, 'scale': False, 'label_weights': {}, 'population_rates': None, 'init': None, 'warm_start': False, 'subsample': 1.0, 'presort': 'deprecated', 'max_depth': 5, 'ccp_alpha': 0.0, 'tol': 0.0001, 'min_samples_split': 2, 'min_impurity_decrease': 0.0}
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
			'Culture.Biography.Biography*'                 17601  -->  6280  11321  2251  39537
			'Culture.Biography.Women'                       3879  -->   530   3349   220  55290
			'Culture.Food and drink'                        1483  -->    65   1418    62  57844
			'Culture.Internet culture'                      3043  -->   923   2120   257  56089
			'Culture.Linguistics'                           1586  -->   231   1355    64  57739
			'Culture.Literature'                            5594  -->   457   5137   278  53517
			'Culture.Media.Books'                           1544  -->    79   1465    78  57767
			'Culture.Media.Entertainment'                   2182  -->   517   1665   186  57021
			'Culture.Media.Films'                           2629  -->   446   2183   133  56627
			'Culture.Media.Media*'                         14040  -->  5968   8072  1979  43370
			'Culture.Media.Music'                           3171  -->   597   2574   280  55938
			'Culture.Media.Radio'                            787  -->   180    607    74  58528
			'Culture.Media.Software'                        1888  -->   944    944   312  57189
			'Culture.Media.Television'                      2061  -->   493   1568   140  57188
			'Culture.Media.Video games'                     2181  -->   725   1456   162  57046
			'Culture.Performing arts'                       1414  -->    50   1364    62  57913
			'Culture.Philosophy and religion'               3192  -->    48   3144    43  56154
			'Culture.Sports'                                6570  -->  3264   3306   408  52411
			'Culture.Visual arts.Architecture'              1987  -->   181   1806   106  57296
			'Culture.Visual arts.Comics and Anime'          2405  -->   294   2111   140  56844
			'Culture.Visual arts.Fashion'                   1194  -->   135   1059    92  58103
			'Culture.Visual arts.Visual arts*'              6154  -->   522   5632   223  53012
			'Geography.Geographical'                        3395  -->   570   2825   213  55781
			'Geography.Regions.Africa.Africa*'              4858  -->   209   4649   134  54397
			'Geography.Regions.Africa.Central Africa'       1162  -->   117   1045    61  58166
			'Geography.Regions.Africa.Eastern Africa'        583  -->    91    492    83  58723
			'Geography.Regions.Africa.Northern Africa'      1377  -->   109   1268    61  57951
			'Geography.Regions.Africa.Southern Africa'      1002  -->   139    863    59  58328
			'Geography.Regions.Africa.Western Africa'        339  -->    68    271    80  58970
			'Geography.Regions.Americas.Central America'    1301  -->    77   1224    73  58015
			'Geography.Regions.Americas.North America'      5960  -->   675   5285   432  52997
			'Geography.Regions.Americas.South America'      1491  -->    92   1399    88  57810
			'Geography.Regions.Asia.Asia*'                 15101  -->  2492  12609  1147  43141
			'Geography.Regions.Asia.Central Asia'           1181  -->    55   1126    58  58150
			'Geography.Regions.Asia.East Asia'              7203  -->  1121   6082   432  51754
			'Geography.Regions.Asia.North Asia'             2820  -->   399   2421   209  56360
			'Geography.Regions.Asia.South Asia'             1640  -->    89   1551    70  57679
			'Geography.Regions.Asia.Southeast Asia'         1670  -->   101   1569    58  57661
			'Geography.Regions.Asia.West Asia'              1924  -->   104   1820    79  57386
			'Geography.Regions.Europe.Eastern Europe'       3865  -->   459   3406   244  55280
			'Geography.Regions.Europe.Europe*'             13524  -->  3495  10029  1748  44117
			'Geography.Regions.Europe.Northern Europe'      3345  -->   149   3196    89  55955
			'Geography.Regions.Europe.Southern Europe'      2992  -->   445   2547   136  56261
			'Geography.Regions.Europe.Western Europe'       4149  -->   943   3206   405  54835
			'Geography.Regions.Oceania'                     1575  -->    96   1479    63  57751
			'History and Society.Business and economics'    3752  -->   161   3591   114  55523
			'History and Society.Education'                 1907  -->   327   1580    97  57385
			'History and Society.History'                   4604  -->   230   4374   147  54638
			'History and Society.Military and warfare'      4643  -->   686   3957   164  54582
			'History and Society.Politics and government'   3373  -->    97   3276    72  55944
			'History and Society.Society'                   3974  -->   124   3850    64  55351
			'History and Society.Transportation'            4763  -->  1599   3164   343  54283
			'STEM.Biology'                                  2779  -->   416   2363   176  56434
			'STEM.Chemistry'                                1414  -->   238   1176   124  57851
			'STEM.Computing'                                2448  -->  1083   1365   370  56571
			'STEM.Earth and environment'                    1773  -->    70   1703    57  57559
			'STEM.Engineering'                              2886  -->   698   2188   133  56370
			'STEM.Libraries & Information'                   957  -->   189    768    59  58373
			'STEM.Mathematics'                              1092  -->   230    862    77  58220
			'STEM.Medicine & Health'                        1855  -->    85   1770    69  57465
			'STEM.Physics'                                  1300  -->    81   1219    66  58023
			'STEM.STEM*'                                   17046  -->  7077   9969  2130  40213
			'STEM.Space'                                    1825  -->   572   1253    79  57485
			'STEM.Technology'                               4199  -->  1229   2970   416  54774
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
	match_rate (micro=0.032, macro=0.009):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.091
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.002
		Culture.Literature                           0.006
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.065
		Culture.Media.Music                          0.009
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.005
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.038
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.006
		Geography.Geographical                       0.007
		Geography.Regions.Africa.Africa*             0.003
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.033
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.01
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.002
		History and Society.Education                0.003
		History and Society.History                  0.003
		History and Society.Military and warfare     0.005
		History and Society.Politics and government  0.002
		History and Society.Society                  0.001
		History and Society.Transportation           0.012
		STEM.Biology                                 0.008
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.001
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.074
		STEM.Space                                   0.003
		STEM.Technology                              0.009
		-------------------------------------------  -----
	filter_rate (micro=0.968, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.909
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.935
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.962
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.998
		History and Society.Education                0.997
		History and Society.History                  0.997
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.998
		History and Society.Society                  0.999
		History and Society.Transportation           0.988
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.926
		STEM.Space                                   0.997
		STEM.Technology                              0.991
		-------------------------------------------  -----
	recall (micro=0.226, macro=0.163):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.357
		Culture.Biography.Women                      0.137
		Culture.Food and drink                       0.044
		Culture.Internet culture                     0.303
		Culture.Linguistics                          0.146
		Culture.Literature                           0.082
		Culture.Media.Books                          0.051
		Culture.Media.Entertainment                  0.237
		Culture.Media.Films                          0.17
		Culture.Media.Media*                         0.425
		Culture.Media.Music                          0.188
		Culture.Media.Radio                          0.229
		Culture.Media.Software                       0.5
		Culture.Media.Television                     0.239
		Culture.Media.Video games                    0.332
		Culture.Performing arts                      0.035
		Culture.Philosophy and religion              0.015
		Culture.Sports                               0.497
		Culture.Visual arts.Architecture             0.091
		Culture.Visual arts.Comics and Anime         0.122
		Culture.Visual arts.Fashion                  0.113
		Culture.Visual arts.Visual arts*             0.085
		Geography.Geographical                       0.168
		Geography.Regions.Africa.Africa*             0.043
		Geography.Regions.Africa.Central Africa      0.101
		Geography.Regions.Africa.Eastern Africa      0.156
		Geography.Regions.Africa.Northern Africa     0.079
		Geography.Regions.Africa.Southern Africa     0.139
		Geography.Regions.Africa.Western Africa      0.201
		Geography.Regions.Americas.Central America   0.059
		Geography.Regions.Americas.North America     0.113
		Geography.Regions.Americas.South America     0.062
		Geography.Regions.Asia.Asia*                 0.165
		Geography.Regions.Asia.Central Asia          0.047
		Geography.Regions.Asia.East Asia             0.156
		Geography.Regions.Asia.North Asia            0.141
		Geography.Regions.Asia.South Asia            0.054
		Geography.Regions.Asia.Southeast Asia        0.06
		Geography.Regions.Asia.West Asia             0.054
		Geography.Regions.Europe.Eastern Europe      0.119
		Geography.Regions.Europe.Europe*             0.258
		Geography.Regions.Europe.Northern Europe     0.045
		Geography.Regions.Europe.Southern Europe     0.149
		Geography.Regions.Europe.Western Europe      0.227
		Geography.Regions.Oceania                    0.061
		History and Society.Business and economics   0.043
		History and Society.Education                0.171
		History and Society.History                  0.05
		History and Society.Military and warfare     0.148
		History and Society.Politics and government  0.029
		History and Society.Society                  0.031
		History and Society.Transportation           0.336
		STEM.Biology                                 0.15
		STEM.Chemistry                               0.168
		STEM.Computing                               0.442
		STEM.Earth and environment                   0.039
		STEM.Engineering                             0.242
		STEM.Libraries & Information                 0.197
		STEM.Mathematics                             0.211
		STEM.Medicine & Health                       0.046
		STEM.Physics                                 0.062
		STEM.STEM*                                   0.415
		STEM.Space                                   0.313
		STEM.Technology                              0.293
		-------------------------------------------  -----
	!recall (micro=0.981, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.946
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.956
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.996
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.992
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.998
		History and Society.Education                0.998
		History and Society.History                  0.997
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.999
		History and Society.Society                  0.999
		History and Society.Transportation           0.994
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.95
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.404, macro=0.277):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.478
		Culture.Biography.Women                      0.346
		Culture.Food and drink                       0.096
		Culture.Internet culture                     0.201
		Culture.Linguistics                          0.518
		Culture.Literature                           0.194
		Culture.Media.Books                          0.142
		Culture.Media.Entertainment                  0.226
		Culture.Media.Films                          0.46
		Culture.Media.Media*                         0.363
		Culture.Media.Music                          0.45
		Culture.Media.Radio                          0.299
		Culture.Media.Software                       0.109
		Culture.Media.Television                     0.47
		Culture.Media.Video games                    0.257
		Culture.Performing arts                      0.093
		Culture.Philosophy and religion              0.172
		Culture.Sports                               0.807
		Culture.Visual arts.Architecture             0.352
		Culture.Visual arts.Comics and Anime         0.107
		Culture.Visual arts.Fashion                  0.061
		Culture.Visual arts.Visual arts*             0.273
		Geography.Geographical                       0.49
		Geography.Regions.Africa.Africa*             0.131
		Geography.Regions.Africa.Central Africa      0.064
		Geography.Regions.Africa.Eastern Africa      0.053
		Geography.Regions.Africa.Northern Africa     0.093
		Geography.Regions.Africa.Southern Africa     0.154
		Geography.Regions.Africa.Western Africa      0.1
		Geography.Regions.Americas.Central America   0.141
		Geography.Regions.Americas.North America     0.488
		Geography.Regions.Americas.South America     0.22
		Geography.Regions.Asia.Asia*                 0.263
		Geography.Regions.Asia.Central Asia          0.036
		Geography.Regions.Asia.East Asia             0.189
		Geography.Regions.Asia.North Asia            0.179
		Geography.Regions.Asia.South Asia            0.431
		Geography.Regions.Asia.Southeast Asia        0.276
		Geography.Regions.Asia.West Asia             0.32
		Geography.Regions.Europe.Eastern Europe      0.337
		Geography.Regions.Europe.Europe*             0.376
		Geography.Regions.Europe.Northern Europe     0.458
		Geography.Regions.Europe.Southern Europe     0.467
		Geography.Regions.Europe.Western Europe      0.396
		Geography.Regions.Oceania                    0.485
		History and Society.Business and economics   0.172
		History and Society.Education                0.45
		History and Society.History                  0.171
		History and Society.Military and warfare     0.436
		History and Society.Politics and government  0.272
		History and Society.Society                  0.185
		History and Society.Transportation           0.472
		STEM.Biology                                 0.635
		STEM.Chemistry                               0.119
		STEM.Computing                               0.163
		STEM.Earth and environment                   0.161
		STEM.Engineering                             0.375
		STEM.Libraries & Information                 0.119
		STEM.Mathematics                             0.069
		STEM.Medicine & Health                       0.2
		STEM.Physics                                 0.049
		STEM.STEM*                                   0.367
		STEM.Space                                   0.496
		STEM.Technology                              0.169
		-------------------------------------------  -----
	!precision (micro=0.965, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.914
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.993
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.968
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.954
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.99
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.989
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.959
		STEM.Space                                   0.997
		STEM.Technology                              0.996
		-------------------------------------------  -----
	f1 (micro=0.268, macro=0.178):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.409
		Culture.Biography.Women                      0.196
		Culture.Food and drink                       0.06
		Culture.Internet culture                     0.242
		Culture.Linguistics                          0.227
		Culture.Literature                           0.115
		Culture.Media.Books                          0.075
		Culture.Media.Entertainment                  0.231
		Culture.Media.Films                          0.248
		Culture.Media.Media*                         0.392
		Culture.Media.Music                          0.265
		Culture.Media.Radio                          0.259
		Culture.Media.Software                       0.179
		Culture.Media.Television                     0.317
		Culture.Media.Video games                    0.29
		Culture.Performing arts                      0.051
		Culture.Philosophy and religion              0.028
		Culture.Sports                               0.615
		Culture.Visual arts.Architecture             0.145
		Culture.Visual arts.Comics and Anime         0.114
		Culture.Visual arts.Fashion                  0.079
		Culture.Visual arts.Visual arts*             0.129
		Geography.Geographical                       0.25
		Geography.Regions.Africa.Africa*             0.065
		Geography.Regions.Africa.Central Africa      0.078
		Geography.Regions.Africa.Eastern Africa      0.079
		Geography.Regions.Africa.Northern Africa     0.086
		Geography.Regions.Africa.Southern Africa     0.146
		Geography.Regions.Africa.Western Africa      0.134
		Geography.Regions.Americas.Central America   0.083
		Geography.Regions.Americas.North America     0.184
		Geography.Regions.Americas.South America     0.096
		Geography.Regions.Asia.Asia*                 0.203
		Geography.Regions.Asia.Central Asia          0.041
		Geography.Regions.Asia.East Asia             0.171
		Geography.Regions.Asia.North Asia            0.158
		Geography.Regions.Asia.South Asia            0.096
		Geography.Regions.Asia.Southeast Asia        0.099
		Geography.Regions.Asia.West Asia             0.092
		Geography.Regions.Europe.Eastern Europe      0.176
		Geography.Regions.Europe.Europe*             0.306
		Geography.Regions.Europe.Northern Europe     0.081
		Geography.Regions.Europe.Southern Europe     0.226
		Geography.Regions.Europe.Western Europe      0.289
		Geography.Regions.Oceania                    0.108
		History and Society.Business and economics   0.069
		History and Society.Education                0.248
		History and Society.History                  0.077
		History and Society.Military and warfare     0.221
		History and Society.Politics and government  0.052
		History and Society.Society                  0.053
		History and Society.Transportation           0.392
		STEM.Biology                                 0.242
		STEM.Chemistry                               0.139
		STEM.Computing                               0.238
		STEM.Earth and environment                   0.063
		STEM.Engineering                             0.294
		STEM.Libraries & Information                 0.149
		STEM.Mathematics                             0.104
		STEM.Medicine & Health                       0.075
		STEM.Physics                                 0.055
		STEM.STEM*                                   0.39
		STEM.Space                                   0.384
		STEM.Technology                              0.214
		-------------------------------------------  -----
	!f1 (micro=0.973, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.93
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.98
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
		Geography.Regions.Asia.Asia*                 0.964
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
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
		History and Society.History                  0.993
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.991
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.954
		STEM.Space                                   0.998
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.927
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.962
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.936
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.931
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.987
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.904
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.983
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.983
		History and Society.Society                  0.991
		History and Society.Transportation           0.983
		STEM.Biology                                 0.967
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.915
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.019, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.054
		Culture.Biography.Women                      0.004
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.005
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.044
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.008
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.004
		Geography.Geographical                       0.004
		Geography.Regions.Africa.Africa*             0.002
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.008
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.026
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.002
		History and Society.Education                0.002
		History and Society.History                  0.003
		History and Society.Military and warfare     0.003
		History and Society.Politics and government  0.001
		History and Society.Society                  0.001
		History and Society.Transportation           0.006
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.001
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.05
		STEM.Space                                   0.001
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.789, macro=0.793):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.781
		Culture.Biography.Women                      0.78
		Culture.Food and drink                       0.769
		Culture.Internet culture                     0.862
		Culture.Linguistics                          0.785
		Culture.Literature                           0.773
		Culture.Media.Books                          0.799
		Culture.Media.Entertainment                  0.824
		Culture.Media.Films                          0.813
		Culture.Media.Media*                         0.824
		Culture.Media.Music                          0.827
		Culture.Media.Radio                          0.819
		Culture.Media.Software                       0.92
		Culture.Media.Television                     0.856
		Culture.Media.Video games                    0.87
		Culture.Performing arts                      0.78
		Culture.Philosophy and religion              0.747
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.793
		Culture.Visual arts.Comics and Anime         0.838
		Culture.Visual arts.Fashion                  0.776
		Culture.Visual arts.Visual arts*             0.742
		Geography.Geographical                       0.831
		Geography.Regions.Africa.Africa*             0.763
		Geography.Regions.Africa.Central Africa      0.83
		Geography.Regions.Africa.Eastern Africa      0.75
		Geography.Regions.Africa.Northern Africa     0.771
		Geography.Regions.Africa.Southern Africa     0.803
		Geography.Regions.Africa.Western Africa      0.74
		Geography.Regions.Americas.Central America   0.745
		Geography.Regions.Americas.North America     0.772
		Geography.Regions.Americas.South America     0.785
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.771
		Geography.Regions.Asia.East Asia             0.823
		Geography.Regions.Asia.North Asia            0.802
		Geography.Regions.Asia.South Asia            0.724
		Geography.Regions.Asia.Southeast Asia        0.733
		Geography.Regions.Asia.West Asia             0.742
		Geography.Regions.Europe.Eastern Europe      0.779
		Geography.Regions.Europe.Europe*             0.764
		Geography.Regions.Europe.Northern Europe     0.743
		Geography.Regions.Europe.Southern Europe     0.796
		Geography.Regions.Europe.Western Europe      0.814
		Geography.Regions.Oceania                    0.73
		History and Society.Business and economics   0.722
		History and Society.Education                0.807
		History and Society.History                  0.772
		History and Society.Military and warfare     0.776
		History and Society.Politics and government  0.728
		History and Society.Society                  0.697
		History and Society.Transportation           0.85
		STEM.Biology                                 0.801
		STEM.Chemistry                               0.828
		STEM.Computing                               0.904
		STEM.Earth and environment                   0.761
		STEM.Engineering                             0.817
		STEM.Libraries & Information                 0.823
		STEM.Mathematics                             0.848
		STEM.Medicine & Health                       0.757
		STEM.Physics                                 0.786
		STEM.STEM*                                   0.797
		STEM.Space                                   0.855
		STEM.Technology                              0.829
		-------------------------------------------  -----
	pr_auc (micro=0.257, macro=0.135):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.424
		Culture.Biography.Women                      0.146
		Culture.Food and drink                       0.016
		Culture.Internet culture                     0.182
		Culture.Linguistics                          0.179
		Culture.Literature                           0.078
		Culture.Media.Books                          0.041
		Culture.Media.Entertainment                  0.137
		Culture.Media.Films                          0.201
		Culture.Media.Media*                         0.359
		Culture.Media.Music                          0.231
		Culture.Media.Radio                          0.117
		Culture.Media.Software                       0.1
		Culture.Media.Television                     0.244
		Culture.Media.Video games                    0.194
		Culture.Performing arts                      0.032
		Culture.Philosophy and religion              0.037
		Culture.Sports                               0.634
		Culture.Visual arts.Architecture             0.112
		Culture.Visual arts.Comics and Anime         0.04
		Culture.Visual arts.Fashion                  0.013
		Culture.Visual arts.Visual arts*             0.102
		Geography.Geographical                       0.23
		Geography.Regions.Africa.Africa*             0.053
		Geography.Regions.Africa.Central Africa      0.016
		Geography.Regions.Africa.Eastern Africa      0.011
		Geography.Regions.Africa.Northern Africa     0.021
		Geography.Regions.Africa.Southern Africa     0.047
		Geography.Regions.Africa.Western Africa      0.027
		Geography.Regions.Americas.Central America   0.04
		Geography.Regions.Americas.North America     0.264
		Geography.Regions.Americas.South America     0.06
		Geography.Regions.Asia.Asia*                 0.178
		Geography.Regions.Asia.Central Asia          0.007
		Geography.Regions.Asia.East Asia             0.099
		Geography.Regions.Asia.North Asia            0.066
		Geography.Regions.Asia.South Asia            0.09
		Geography.Regions.Asia.Southeast Asia        0.05
		Geography.Regions.Asia.West Asia             0.09
		Geography.Regions.Europe.Eastern Europe      0.136
		Geography.Regions.Europe.Europe*             0.294
		Geography.Regions.Europe.Northern Europe     0.129
		Geography.Regions.Europe.Southern Europe     0.191
		Geography.Regions.Europe.Western Europe      0.219
		Geography.Regions.Oceania                    0.122
		History and Society.Business and economics   0.047
		History and Society.Education                0.16
		History and Society.History                  0.063
		History and Society.Military and warfare     0.18
		History and Society.Politics and government  0.076
		History and Society.Society                  0.044
		History and Society.Transportation           0.333
		STEM.Biology                                 0.276
		STEM.Chemistry                               0.045
		STEM.Computing                               0.127
		STEM.Earth and environment                   0.048
		STEM.Engineering                             0.218
		STEM.Libraries & Information                 0.034
		STEM.Mathematics                             0.033
		STEM.Medicine & Health                       0.042
		STEM.Physics                                 0.012
		STEM.STEM*                                   0.375
		STEM.Space                                   0.315
		STEM.Technology                              0.132
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}}

