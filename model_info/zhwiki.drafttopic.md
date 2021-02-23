Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'subsample': 1.0, 'random_state': None, 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'label_weights': {}, 'ccp_alpha': 0.0, 'min_weight_fraction_leaf': 0.0, 'scale': False, 'max_leaf_nodes': None, 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'warm_start': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_estimators': 150, 'min_impurity_split': None, 'multilabel': True, 'max_features': 'log2', 'population_rates': None, 'validation_fraction': 0.1, 'tol': 0.0001, 'verbose': 0, 'loss': 'deviance', 'learning_rate': 0.1, 'max_depth': 5, 'min_samples_leaf': 1, 'center': False, 'init': None, 'presort': 'deprecated'}
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
	counts (n=60821):
			label                                              n         TP     FP    FN     TN
			---------------------------------------------  -----  ---  ----  -----  ----  -----
			'Culture.Biography.Biography*'                 13231  -->  1942  11289   733  46857
			'Culture.Biography.Women'                       3158  -->   220   2938   133  57530
			'Culture.Food and drink'                        1331  -->    44   1287    62  59428
			'Culture.Internet culture'                      3323  -->  1201   2122   280  57218
			'Culture.Linguistics'                           1478  -->   274   1204    58  59285
			'Culture.Literature'                            5376  -->   648   4728   239  55206
			'Culture.Media.Books'                           1614  -->    58   1556    62  59145
			'Culture.Media.Entertainment'                   1853  -->   140   1713    88  58880
			'Culture.Media.Films'                           2386  -->   330   2056   135  58300
			'Culture.Media.Media*'                         13361  -->  5111   8250  1651  45809
			'Culture.Media.Music'                           2460  -->   421   2039   181  58180
			'Culture.Media.Radio'                            747  -->   200    547    76  59998
			'Culture.Media.Software'                        2060  -->   895   1165   340  58421
			'Culture.Media.Television'                      1993  -->   387   1606   155  58673
			'Culture.Media.Video games'                     2332  -->   957   1375   164  58325
			'Culture.Performing arts'                       1307  -->   103   1204    59  59455
			'Culture.Philosophy and religion'               3511  -->   196   3315    88  57222
			'Culture.Sports'                                4122  -->  1013   3109   160  56539
			'Culture.Visual arts.Architecture'              2397  -->   421   1976   172  58252
			'Culture.Visual arts.Comics and Anime'          2306  -->   597   1709   185  58330
			'Culture.Visual arts.Fashion'                   1137  -->    59   1078    67  59617
			'Culture.Visual arts.Visual arts*'              6313  -->  1059   5254   393  54115
			'Geography.Geographical'                        5388  -->   613   4775   205  55228
			'Geography.Regions.Africa.Africa*'              5466  -->   528   4938   217  55138
			'Geography.Regions.Africa.Central Africa'       1185  -->    96   1089    46  59590
			'Geography.Regions.Africa.Eastern Africa'        959  -->   227    732   112  59750
			'Geography.Regions.Africa.Northern Africa'      1355  -->   145   1210    76  59390
			'Geography.Regions.Africa.Southern Africa'      1155  -->   144   1011    61  59605
			'Geography.Regions.Africa.Western Africa'        448  -->    80    368    47  60326
			'Geography.Regions.Americas.Central America'    1260  -->   106   1154    40  59521
			'Geography.Regions.Americas.North America'      5583  -->   764   4819   342  54896
			'Geography.Regions.Americas.South America'      1466  -->   291   1175    78  59277
			'Geography.Regions.Asia.Asia*'                 16494  -->  3489  13005  1500  42827
			'Geography.Regions.Asia.Central Asia'           1191  -->    76   1115    55  59575
			'Geography.Regions.Asia.East Asia'              8341  -->  1186   7155   516  51964
			'Geography.Regions.Asia.North Asia'             2681  -->   544   2137   215  57925
			'Geography.Regions.Asia.South Asia'             1759  -->   169   1590    72  58990
			'Geography.Regions.Asia.Southeast Asia'         2007  -->   230   1777   105  58709
			'Geography.Regions.Asia.West Asia'              1925  -->   197   1728   117  58779
			'Geography.Regions.Europe.Eastern Europe'       3923  -->   936   2987   316  56582
			'Geography.Regions.Europe.Europe*'             13222  -->  4359   8863  1601  45998
			'Geography.Regions.Europe.Northern Europe'      3278  -->   334   2944   215  57328
			'Geography.Regions.Europe.Southern Europe'      2874  -->   896   1978   144  57803
			'Geography.Regions.Europe.Western Europe'       3721  -->  1114   2607   341  56759
			'Geography.Regions.Oceania'                     1901  -->   135   1766    51  58869
			'History and Society.Business and economics'    3508  -->   159   3349   110  57203
			'History and Society.Education'                 1830  -->   286   1544   101  58890
			'History and Society.History'                   3966  -->   127   3839    96  56759
			'History and Society.Military and warfare'      3605  -->   321   3284   148  57068
			'History and Society.Politics and government'   3646  -->   175   3471    90  57085
			'History and Society.Society'                   4309  -->   179   4130    68  56444
			'History and Society.Transportation'            3605  -->   859   2746   174  57042
			'STEM.Biology'                                  3042  -->   464   2578   103  57676
			'STEM.Chemistry'                                1413  -->   247   1166    81  59327
			'STEM.Computing'                                2429  -->   960   1469   368  58024
			'STEM.Earth and environment'                    2379  -->   186   2193    52  58390
			'STEM.Engineering'                              2395  -->   479   1916    96  58330
			'STEM.Libraries & Information'                  1148  -->   127   1021    65  59608
			'STEM.Mathematics'                              1122  -->   252    870   113  59586
			'STEM.Medicine & Health'                        1745  -->   110   1635    66  59010
			'STEM.Physics'                                  1275  -->   109   1166    57  59489
			'STEM.STEM*'                                   17854  -->  6568  11286  1787  41180
			'STEM.Space'                                    1687  -->   557   1130    51  59083
			'STEM.Technology'                               4108  -->  1083   3025   433  56280
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.218         0.121
		Culture.Biography.Women                         0.052         0.015
		Culture.Food and drink                          0.022         0.003
		Culture.Internet culture                        0.055         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.088         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.039         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.04          0.021
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.034         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.058         0.01
		Culture.Sports                                  0.068         0.061
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.038         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.104         0.018
		Geography.Geographical                          0.089         0.021
		Geography.Regions.Africa.Africa*                0.09          0.009
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.016         0.001
		Geography.Regions.Africa.Northern Africa        0.022         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.007         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.092         0.064
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.271         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.137         0.012
		Geography.Regions.Asia.North Asia               0.044         0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.033         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.065         0.018
		Geography.Regions.Europe.Europe*                0.217         0.082
		Geography.Regions.Europe.Northern Europe        0.054         0.029
		Geography.Regions.Europe.Southern Europe        0.047         0.014
		Geography.Regions.Europe.Western Europe         0.061         0.021
		Geography.Regions.Oceania                       0.031         0.017
		History and Society.Business and economics      0.058         0.01
		History and Society.Education                   0.03          0.008
		History and Society.History                     0.065         0.011
		History and Society.Military and warfare        0.059         0.015
		History and Society.Politics and government     0.06          0.016
		History and Society.Society                     0.071         0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.05          0.035
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.039         0.005
		STEM.Engineering                                0.039         0.006
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.021         0.001
		STEM.STEM*                                      0.294         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.068         0.005
	match_rate (micro=0.023, macro=0.008):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.031
		Culture.Biography.Women                      0.003
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.002
		Culture.Literature                           0.006
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.054
		Culture.Media.Music                          0.007
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.002
		Culture.Sports                               0.018
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.002
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.043
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.003
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.058
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.002
		History and Society.Education                0.003
		History and Society.History                  0.002
		History and Society.Military and warfare     0.004
		History and Society.Politics and government  0.002
		History and Society.Society                  0.002
		History and Society.Transportation           0.007
		STEM.Biology                                 0.007
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.063
		STEM.Space                                   0.002
		STEM.Technology                              0.009
		-------------------------------------------  -----
	filter_rate (micro=0.977, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.946
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.998
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.998
		History and Society.Education                0.997
		History and Society.History                  0.998
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.998
		History and Society.Society                  0.998
		History and Society.Transportation           0.993
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.937
		STEM.Space                                   0.998
		STEM.Technology                              0.991
		-------------------------------------------  -----
	recall (micro=0.198, macro=0.169):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.147
		Culture.Biography.Women                      0.07
		Culture.Food and drink                       0.033
		Culture.Internet culture                     0.361
		Culture.Linguistics                          0.185
		Culture.Literature                           0.121
		Culture.Media.Books                          0.036
		Culture.Media.Entertainment                  0.076
		Culture.Media.Films                          0.138
		Culture.Media.Media*                         0.383
		Culture.Media.Music                          0.171
		Culture.Media.Radio                          0.268
		Culture.Media.Software                       0.434
		Culture.Media.Television                     0.194
		Culture.Media.Video games                    0.41
		Culture.Performing arts                      0.079
		Culture.Philosophy and religion              0.056
		Culture.Sports                               0.246
		Culture.Visual arts.Architecture             0.176
		Culture.Visual arts.Comics and Anime         0.259
		Culture.Visual arts.Fashion                  0.052
		Culture.Visual arts.Visual arts*             0.168
		Geography.Geographical                       0.114
		Geography.Regions.Africa.Africa*             0.097
		Geography.Regions.Africa.Central Africa      0.081
		Geography.Regions.Africa.Eastern Africa      0.237
		Geography.Regions.Africa.Northern Africa     0.107
		Geography.Regions.Africa.Southern Africa     0.125
		Geography.Regions.Africa.Western Africa      0.179
		Geography.Regions.Americas.Central America   0.084
		Geography.Regions.Americas.North America     0.137
		Geography.Regions.Americas.South America     0.198
		Geography.Regions.Asia.Asia*                 0.212
		Geography.Regions.Asia.Central Asia          0.064
		Geography.Regions.Asia.East Asia             0.142
		Geography.Regions.Asia.North Asia            0.203
		Geography.Regions.Asia.South Asia            0.096
		Geography.Regions.Asia.Southeast Asia        0.115
		Geography.Regions.Asia.West Asia             0.102
		Geography.Regions.Europe.Eastern Europe      0.239
		Geography.Regions.Europe.Europe*             0.33
		Geography.Regions.Europe.Northern Europe     0.102
		Geography.Regions.Europe.Southern Europe     0.312
		Geography.Regions.Europe.Western Europe      0.299
		Geography.Regions.Oceania                    0.071
		History and Society.Business and economics   0.045
		History and Society.Education                0.156
		History and Society.History                  0.032
		History and Society.Military and warfare     0.089
		History and Society.Politics and government  0.048
		History and Society.Society                  0.042
		History and Society.Transportation           0.238
		STEM.Biology                                 0.153
		STEM.Chemistry                               0.175
		STEM.Computing                               0.395
		STEM.Earth and environment                   0.078
		STEM.Engineering                             0.2
		STEM.Libraries & Information                 0.111
		STEM.Mathematics                             0.225
		STEM.Medicine & Health                       0.063
		STEM.Physics                                 0.085
		STEM.STEM*                                   0.368
		STEM.Space                                   0.33
		STEM.Technology                              0.264
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.998
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.998
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.996
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.994
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.998
		History and Society.Education                0.998
		History and Society.History                  0.998
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.998
		History and Society.Society                  0.999
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.999
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.958
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	precision (micro=0.46, macro=0.318):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.569
		Culture.Biography.Women                      0.317
		Culture.Food and drink                       0.076
		Culture.Internet culture                     0.219
		Culture.Linguistics                          0.608
		Culture.Literature                           0.299
		Culture.Media.Books                          0.131
		Culture.Media.Entertainment                  0.168
		Culture.Media.Films                          0.414
		Culture.Media.Media*                         0.392
		Culture.Media.Music                          0.544
		Culture.Media.Radio                          0.332
		Culture.Media.Software                       0.09
		Culture.Media.Television                     0.4
		Culture.Media.Video games                    0.301
		Culture.Performing arts                      0.197
		Culture.Philosophy and religion              0.278
		Culture.Sports                               0.85
		Culture.Visual arts.Architecture             0.397
		Culture.Visual arts.Comics and Anime         0.165
		Culture.Visual arts.Fashion                  0.04
		Culture.Visual arts.Visual arts*             0.302
		Geography.Geographical                       0.401
		Geography.Regions.Africa.Africa*             0.176
		Geography.Regions.Africa.Central Africa      0.069
		Geography.Regions.Africa.Eastern Africa      0.06
		Geography.Regions.Africa.Northern Africa     0.103
		Geography.Regions.Africa.Southern Africa     0.139
		Geography.Regions.Africa.Western Africa      0.147
		Geography.Regions.Americas.Central America   0.305
		Geography.Regions.Americas.North America     0.6
		Geography.Regions.Americas.South America     0.513
		Geography.Regions.Asia.Asia*                 0.259
		Geography.Regions.Asia.Central Asia          0.053
		Geography.Regions.Asia.East Asia             0.152
		Geography.Regions.Asia.North Asia            0.238
		Geography.Regions.Asia.South Asia            0.572
		Geography.Regions.Asia.Southeast Asia        0.289
		Geography.Regions.Asia.West Asia             0.381
		Geography.Regions.Europe.Eastern Europe      0.447
		Geography.Regions.Europe.Europe*             0.466
		Geography.Regions.Europe.Northern Europe     0.451
		Geography.Regions.Europe.Southern Europe     0.641
		Geography.Regions.Europe.Western Europe      0.514
		Geography.Regions.Oceania                    0.58
		History and Society.Business and economics   0.19
		History and Society.Education                0.424
		History and Society.History                  0.173
		History and Society.Military and warfare     0.351
		History and Society.Politics and government  0.338
		History and Society.Society                  0.225
		History and Society.Transportation           0.567
		STEM.Biology                                 0.755
		STEM.Chemistry                               0.18
		STEM.Computing                               0.152
		STEM.Earth and environment                   0.296
		STEM.Engineering                             0.415
		STEM.Libraries & Information                 0.066
		STEM.Mathematics                             0.052
		STEM.Medicine & Health                       0.27
		STEM.Physics                                 0.078
		STEM.STEM*                                   0.383
		STEM.Space                                   0.623
		STEM.Technology                              0.153
		-------------------------------------------  -----
	!precision (micro=0.962, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.893
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.993
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.953
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.956
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.987
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.956
		STEM.Space                                   0.997
		STEM.Technology                              0.996
		-------------------------------------------  -----
	f1 (micro=0.256, macro=0.192):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.233
		Culture.Biography.Women                      0.114
		Culture.Food and drink                       0.046
		Culture.Internet culture                     0.273
		Culture.Linguistics                          0.284
		Culture.Literature                           0.172
		Culture.Media.Books                          0.056
		Culture.Media.Entertainment                  0.104
		Culture.Media.Films                          0.207
		Culture.Media.Media*                         0.387
		Culture.Media.Music                          0.26
		Culture.Media.Radio                          0.297
		Culture.Media.Software                       0.15
		Culture.Media.Television                     0.261
		Culture.Media.Video games                    0.347
		Culture.Performing arts                      0.113
		Culture.Philosophy and religion              0.093
		Culture.Sports                               0.381
		Culture.Visual arts.Architecture             0.243
		Culture.Visual arts.Comics and Anime         0.202
		Culture.Visual arts.Fashion                  0.045
		Culture.Visual arts.Visual arts*             0.216
		Geography.Geographical                       0.177
		Geography.Regions.Africa.Africa*             0.125
		Geography.Regions.Africa.Central Africa      0.075
		Geography.Regions.Africa.Eastern Africa      0.096
		Geography.Regions.Africa.Northern Africa     0.105
		Geography.Regions.Africa.Southern Africa     0.131
		Geography.Regions.Africa.Western Africa      0.161
		Geography.Regions.Americas.Central America   0.132
		Geography.Regions.Americas.North America     0.223
		Geography.Regions.Americas.South America     0.286
		Geography.Regions.Asia.Asia*                 0.233
		Geography.Regions.Asia.Central Asia          0.058
		Geography.Regions.Asia.East Asia             0.147
		Geography.Regions.Asia.North Asia            0.219
		Geography.Regions.Asia.South Asia            0.165
		Geography.Regions.Asia.Southeast Asia        0.164
		Geography.Regions.Asia.West Asia             0.161
		Geography.Regions.Europe.Eastern Europe      0.311
		Geography.Regions.Europe.Europe*             0.386
		Geography.Regions.Europe.Northern Europe     0.166
		Geography.Regions.Europe.Southern Europe     0.419
		Geography.Regions.Europe.Western Europe      0.378
		Geography.Regions.Oceania                    0.127
		History and Society.Business and economics   0.073
		History and Society.Education                0.228
		History and Society.History                  0.054
		History and Society.Military and warfare     0.142
		History and Society.Politics and government  0.084
		History and Society.Society                  0.07
		History and Society.Transportation           0.336
		STEM.Biology                                 0.254
		STEM.Chemistry                               0.177
		STEM.Computing                               0.22
		STEM.Earth and environment                   0.124
		STEM.Engineering                             0.27
		STEM.Libraries & Information                 0.082
		STEM.Mathematics                             0.085
		STEM.Medicine & Health                       0.102
		STEM.Physics                                 0.082
		STEM.STEM*                                   0.375
		STEM.Space                                   0.432
		STEM.Technology                              0.193
		-------------------------------------------  -----
	!f1 (micro=0.974, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.937
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.992
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.957
		STEM.Space                                   0.998
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.951, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.983
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.933
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.951
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.998
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.926
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.987
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.914
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.983
		History and Society.Society                  0.991
		History and Society.Transportation           0.984
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.92
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.015
		Culture.Biography.Women                      0.002
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.004
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.001
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.002
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.004
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.002
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.006
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.034
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.01
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.002
		History and Society.Education                0.002
		History and Society.History                  0.002
		History and Society.Military and warfare     0.003
		History and Society.Politics and government  0.002
		History and Society.Society                  0.001
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.001
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.001
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.042
		STEM.Space                                   0.001
		STEM.Technology                              0.008
		-------------------------------------------  -----
	roc_auc (micro=0.773, macro=0.782):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.731
		Culture.Biography.Women                      0.726
		Culture.Food and drink                       0.721
		Culture.Internet culture                     0.867
		Culture.Linguistics                          0.802
		Culture.Literature                           0.744
		Culture.Media.Books                          0.725
		Culture.Media.Entertainment                  0.746
		Culture.Media.Films                          0.787
		Culture.Media.Media*                         0.797
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.788
		Culture.Media.Software                       0.902
		Culture.Media.Television                     0.814
		Culture.Media.Video games                    0.878
		Culture.Performing arts                      0.739
		Culture.Philosophy and religion              0.744
		Culture.Sports                               0.794
		Culture.Visual arts.Architecture             0.811
		Culture.Visual arts.Comics and Anime         0.832
		Culture.Visual arts.Fashion                  0.7
		Culture.Visual arts.Visual arts*             0.749
		Geography.Geographical                       0.785
		Geography.Regions.Africa.Africa*             0.771
		Geography.Regions.Africa.Central Africa      0.783
		Geography.Regions.Africa.Eastern Africa      0.801
		Geography.Regions.Africa.Northern Africa     0.787
		Geography.Regions.Africa.Southern Africa     0.781
		Geography.Regions.Africa.Western Africa      0.782
		Geography.Regions.Americas.Central America   0.755
		Geography.Regions.Americas.North America     0.762
		Geography.Regions.Americas.South America     0.816
		Geography.Regions.Asia.Asia*                 0.754
		Geography.Regions.Asia.Central Asia          0.775
		Geography.Regions.Asia.East Asia             0.788
		Geography.Regions.Asia.North Asia            0.815
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.743
		Geography.Regions.Asia.West Asia             0.776
		Geography.Regions.Europe.Eastern Europe      0.818
		Geography.Regions.Europe.Europe*             0.785
		Geography.Regions.Europe.Northern Europe     0.755
		Geography.Regions.Europe.Southern Europe     0.838
		Geography.Regions.Europe.Western Europe      0.837
		Geography.Regions.Oceania                    0.746
		History and Society.Business and economics   0.707
		History and Society.Education                0.78
		History and Society.History                  0.741
		History and Society.Military and warfare     0.75
		History and Society.Politics and government  0.718
		History and Society.Society                  0.686
		History and Society.Transportation           0.816
		STEM.Biology                                 0.787
		STEM.Chemistry                               0.814
		STEM.Computing                               0.875
		STEM.Earth and environment                   0.782
		STEM.Engineering                             0.791
		STEM.Libraries & Information                 0.76
		STEM.Mathematics                             0.82
		STEM.Medicine & Health                       0.739
		STEM.Physics                                 0.763
		STEM.STEM*                                   0.777
		STEM.Space                                   0.838
		STEM.Technology                              0.809
		-------------------------------------------  -----
	pr_auc (micro=0.253, macro=0.147):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.339
		Culture.Biography.Women                      0.088
		Culture.Food and drink                       0.012
		Culture.Internet culture                     0.259
		Culture.Linguistics                          0.252
		Culture.Literature                           0.121
		Culture.Media.Books                          0.037
		Culture.Media.Entertainment                  0.053
		Culture.Media.Films                          0.165
		Culture.Media.Media*                         0.348
		Culture.Media.Music                          0.232
		Culture.Media.Radio                          0.127
		Culture.Media.Software                       0.076
		Culture.Media.Television                     0.182
		Culture.Media.Video games                    0.307
		Culture.Performing arts                      0.04
		Culture.Philosophy and religion              0.063
		Culture.Sports                               0.432
		Culture.Visual arts.Architecture             0.158
		Culture.Visual arts.Comics and Anime         0.125
		Culture.Visual arts.Fashion                  0.006
		Culture.Visual arts.Visual arts*             0.153
		Geography.Geographical                       0.147
		Geography.Regions.Africa.Africa*             0.057
		Geography.Regions.Africa.Central Africa      0.012
		Geography.Regions.Africa.Eastern Africa      0.024
		Geography.Regions.Africa.Northern Africa     0.042
		Geography.Regions.Africa.Southern Africa     0.034
		Geography.Regions.Africa.Western Africa      0.044
		Geography.Regions.Americas.Central America   0.069
		Geography.Regions.Americas.North America     0.306
		Geography.Regions.Americas.South America     0.221
		Geography.Regions.Asia.Asia*                 0.186
		Geography.Regions.Asia.Central Asia          0.009
		Geography.Regions.Asia.East Asia             0.068
		Geography.Regions.Asia.North Asia            0.117
		Geography.Regions.Asia.South Asia            0.186
		Geography.Regions.Asia.Southeast Asia        0.077
		Geography.Regions.Asia.West Asia             0.128
		Geography.Regions.Europe.Eastern Europe      0.262
		Geography.Regions.Europe.Europe*             0.387
		Geography.Regions.Europe.Northern Europe     0.177
		Geography.Regions.Europe.Southern Europe     0.366
		Geography.Regions.Europe.Western Europe      0.313
		Geography.Regions.Oceania                    0.121
		History and Society.Business and economics   0.049
		History and Society.Education                0.162
		History and Society.History                  0.049
		History and Society.Military and warfare     0.123
		History and Society.Politics and government  0.083
		History and Society.Society                  0.046
		History and Society.Transportation           0.291
		STEM.Biology                                 0.281
		STEM.Chemistry                               0.071
		STEM.Computing                               0.116
		STEM.Earth and environment                   0.062
		STEM.Engineering                             0.193
		STEM.Libraries & Information                 0.014
		STEM.Mathematics                             0.038
		STEM.Medicine & Health                       0.051
		STEM.Physics                                 0.015
		STEM.STEM*                                   0.354
		STEM.Space                                   0.356
		STEM.Technology                              0.11
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

