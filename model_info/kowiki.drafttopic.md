Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'validation_fraction': 0.1, 'min_weight_fraction_leaf': 0.0, 'label_weights': {}, 'subsample': 1.0, 'max_depth': 5, 'min_samples_split': 2, 'center': False, 'max_leaf_nodes': None, 'population_rates': None, 'learning_rate': 0.1, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'min_samples_leaf': 1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'tol': 0.0001, 'multilabel': True, 'scale': False, 'presort': 'deprecated', 'random_state': None, 'n_estimators': 150, 'warm_start': False, 'max_features': 'log2', 'min_impurity_split': None, 'verbose': 0, 'criterion': 'friedman_mse', 'ccp_alpha': 0.0, 'init': None}
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
	counts (n=58530):
			label                                              n         TP     FP    FN     TN
			---------------------------------------------  -----  ---  ----  -----  ----  -----
			'Culture.Biography.Biography*'                 15435  -->  5200  10235  1804  41291
			'Culture.Biography.Women'                       4173  -->   389   3784   154  54203
			'Culture.Food and drink'                        1639  -->   136   1503    57  56834
			'Culture.Internet culture'                      3296  -->   674   2622   228  55006
			'Culture.Linguistics'                           1556  -->   138   1418    61  56913
			'Culture.Literature'                            5590  -->   507   5083   261  52679
			'Culture.Media.Books'                           1515  -->   140   1375    50  56965
			'Culture.Media.Entertainment'                   2210  -->   403   1807   144  56176
			'Culture.Media.Films'                           2963  -->   514   2449   189  55378
			'Culture.Media.Media*'                         14625  -->  5094   9531  1657  42248
			'Culture.Media.Music'                           3033  -->   355   2678   162  55335
			'Culture.Media.Radio'                            623  -->   174    449    68  57839
			'Culture.Media.Software'                        2176  -->   712   1464   270  56084
			'Culture.Media.Television'                      2480  -->   525   1955   178  55872
			'Culture.Media.Video games'                     2285  -->   509   1776   148  56097
			'Culture.Performing arts'                       1491  -->    83   1408    48  56991
			'Culture.Philosophy and religion'               3635  -->   115   3520    41  54854
			'Culture.Sports'                                5090  -->  1947   3143   270  53170
			'Culture.Visual arts.Architecture'              1999  -->   202   1797    58  56473
			'Culture.Visual arts.Comics and Anime'          2390  -->   384   2006   179  55961
			'Culture.Visual arts.Fashion'                   1291  -->   172   1119    54  57185
			'Culture.Visual arts.Visual arts*'              6149  -->   577   5572   248  52133
			'Geography.Geographical'                        3729  -->   656   3073   284  54517
			'Geography.Regions.Africa.Africa*'              4106  -->   243   3863    98  54326
			'Geography.Regions.Africa.Central Africa'        784  -->   112    672    56  57690
			'Geography.Regions.Africa.Eastern Africa'        446  -->   100    346    46  58038
			'Geography.Regions.Africa.Northern Africa'      1410  -->   142   1268    46  57074
			'Geography.Regions.Africa.Southern Africa'       673  -->   141    532    46  57811
			'Geography.Regions.Africa.Western Africa'        254  -->    69    185    33  58243
			'Geography.Regions.Americas.Central America'    1325  -->    74   1251    79  57126
			'Geography.Regions.Americas.North America'      6296  -->   529   5767   306  51928
			'Geography.Regions.Americas.South America'      1458  -->   100   1358    71  57001
			'Geography.Regions.Asia.Asia*'                 15664  -->  2642  13022  1088  41778
			'Geography.Regions.Asia.Central Asia'           1231  -->   124   1107    32  57267
			'Geography.Regions.Asia.East Asia'              7462  -->   972   6490   341  50727
			'Geography.Regions.Asia.North Asia'             2946  -->   304   2642    79  55505
			'Geography.Regions.Asia.South Asia'             1715  -->   101   1614    36  56779
			'Geography.Regions.Asia.Southeast Asia'         1882  -->   150   1732    66  56582
			'Geography.Regions.Asia.West Asia'              2163  -->   118   2045    49  56318
			'Geography.Regions.Europe.Eastern Europe'       3968  -->   424   3544   118  54444
			'Geography.Regions.Europe.Europe*'             13625  -->  2564  11061  1193  43712
			'Geography.Regions.Europe.Northern Europe'      3639  -->   178   3461    83  54808
			'Geography.Regions.Europe.Southern Europe'      3106  -->   183   2923    59  55365
			'Geography.Regions.Europe.Western Europe'       3832  -->   486   3346   191  54507
			'Geography.Regions.Oceania'                     1664  -->   126   1538    49  56817
			'History and Society.Business and economics'    3691  -->   186   3505    95  54744
			'History and Society.Education'                 1852  -->   321   1531    76  56602
			'History and Society.History'                   4831  -->   282   4549    77  53622
			'History and Society.Military and warfare'      4223  -->   261   3962    65  54242
			'History and Society.Politics and government'   3869  -->   143   3726    54  54607
			'History and Society.Society'                   4291  -->   149   4142    35  54204
			'History and Society.Transportation'            3736  -->  1025   2711   179  54615
			'STEM.Biology'                                  3346  -->   492   2854   156  55028
			'STEM.Chemistry'                                1417  -->   227   1190    58  57055
			'STEM.Computing'                                2614  -->   860   1754   284  55632
			'STEM.Earth and environment'                    1798  -->   107   1691    53  56679
			'STEM.Engineering'                              2584  -->   520   2064    81  55865
			'STEM.Libraries & Information'                   723  -->   171    552    85  57722
			'STEM.Mathematics'                              1116  -->   352    764    79  57335
			'STEM.Medicine & Health'                        1866  -->   125   1741    37  56627
			'STEM.Physics'                                  1428  -->   150   1278    51  57051
			'STEM.STEM*'                                   17051  -->  6210  10841  1758  39721
			'STEM.Space'                                    1626  -->   465   1161    47  56857
			'STEM.Technology'                               4359  -->   895   3464   353  53818
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.264         0.121
		Culture.Biography.Women                         0.071         0.015
		Culture.Food and drink                          0.028         0.003
		Culture.Internet culture                        0.056         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.051         0.012
		Culture.Media.Media*                            0.25          0.055
		Culture.Media.Music                             0.052         0.021
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.039         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.062         0.01
		Culture.Sports                                  0.087         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.041         0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.064         0.021
		Geography.Regions.Africa.Africa*                0.07          0.009
		Geography.Regions.Africa.Central Africa         0.013         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.004         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.108         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.268         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.127         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.068         0.018
		Geography.Regions.Europe.Europe*                0.233         0.082
		Geography.Regions.Europe.Northern Europe        0.062         0.029
		Geography.Regions.Europe.Southern Europe        0.053         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.083         0.011
		History and Society.Military and warfare        0.072         0.015
		History and Society.Politics and government     0.066         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.064         0.016
		STEM.Biology                                    0.057         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.044         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.291         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.074         0.005
	match_rate (micro=0.026, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.078
		Culture.Biography.Women                      0.004
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.006
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.005
		Culture.Media.Media*                         0.055
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.005
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.028
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.006
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.002
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.033
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.04
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.002
		History and Society.Education                0.003
		History and Society.History                  0.002
		History and Society.Military and warfare     0.002
		History and Society.Politics and government  0.002
		History and Society.Society                  0.001
		History and Society.Transportation           0.008
		STEM.Biology                                 0.008
		STEM.Chemistry                               0.001
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.001
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.064
		STEM.Space                                   0.002
		STEM.Technology                              0.008
		-------------------------------------------  -----
	filter_rate (micro=0.974, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.922
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.945
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.972
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.998
		History and Society.Education                0.997
		History and Society.History                  0.998
		History and Society.Military and warfare     0.998
		History and Society.Politics and government  0.998
		History and Society.Society                  0.999
		History and Society.Transportation           0.992
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.936
		STEM.Space                                   0.998
		STEM.Technology                              0.992
		-------------------------------------------  -----
	recall (micro=0.193, macro=0.151):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.337
		Culture.Biography.Women                      0.093
		Culture.Food and drink                       0.083
		Culture.Internet culture                     0.204
		Culture.Linguistics                          0.089
		Culture.Literature                           0.091
		Culture.Media.Books                          0.092
		Culture.Media.Entertainment                  0.182
		Culture.Media.Films                          0.173
		Culture.Media.Media*                         0.348
		Culture.Media.Music                          0.117
		Culture.Media.Radio                          0.279
		Culture.Media.Software                       0.327
		Culture.Media.Television                     0.212
		Culture.Media.Video games                    0.223
		Culture.Performing arts                      0.056
		Culture.Philosophy and religion              0.032
		Culture.Sports                               0.383
		Culture.Visual arts.Architecture             0.101
		Culture.Visual arts.Comics and Anime         0.161
		Culture.Visual arts.Fashion                  0.133
		Culture.Visual arts.Visual arts*             0.094
		Geography.Geographical                       0.176
		Geography.Regions.Africa.Africa*             0.059
		Geography.Regions.Africa.Central Africa      0.143
		Geography.Regions.Africa.Eastern Africa      0.224
		Geography.Regions.Africa.Northern Africa     0.101
		Geography.Regions.Africa.Southern Africa     0.21
		Geography.Regions.Africa.Western Africa      0.272
		Geography.Regions.Americas.Central America   0.056
		Geography.Regions.Americas.North America     0.084
		Geography.Regions.Americas.South America     0.069
		Geography.Regions.Asia.Asia*                 0.169
		Geography.Regions.Asia.Central Asia          0.101
		Geography.Regions.Asia.East Asia             0.13
		Geography.Regions.Asia.North Asia            0.103
		Geography.Regions.Asia.South Asia            0.059
		Geography.Regions.Asia.Southeast Asia        0.08
		Geography.Regions.Asia.West Asia             0.055
		Geography.Regions.Europe.Eastern Europe      0.107
		Geography.Regions.Europe.Europe*             0.188
		Geography.Regions.Europe.Northern Europe     0.049
		Geography.Regions.Europe.Southern Europe     0.059
		Geography.Regions.Europe.Western Europe      0.127
		Geography.Regions.Oceania                    0.076
		History and Society.Business and economics   0.05
		History and Society.Education                0.173
		History and Society.History                  0.058
		History and Society.Military and warfare     0.062
		History and Society.Politics and government  0.037
		History and Society.Society                  0.035
		History and Society.Transportation           0.274
		STEM.Biology                                 0.147
		STEM.Chemistry                               0.16
		STEM.Computing                               0.329
		STEM.Earth and environment                   0.06
		STEM.Engineering                             0.201
		STEM.Libraries & Information                 0.237
		STEM.Mathematics                             0.315
		STEM.Medicine & Health                       0.067
		STEM.Physics                                 0.105
		STEM.STEM*                                   0.364
		STEM.Space                                   0.286
		STEM.Technology                              0.205
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.999
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.999
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.994
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.973
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.999
		Geography.Regions.Europe.Western Europe      0.997
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.998
		History and Society.Education                0.999
		History and Society.History                  0.999
		History and Society.Military and warfare     0.999
		History and Society.Politics and government  0.999
		History and Society.Society                  0.999
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.958
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	precision (micro=0.437, macro=0.323):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.527
		Culture.Biography.Women                      0.335
		Culture.Food and drink                       0.176
		Culture.Internet culture                     0.158
		Culture.Linguistics                          0.404
		Culture.Literature                           0.219
		Culture.Media.Books                          0.316
		Culture.Media.Entertainment                  0.222
		Culture.Media.Films                          0.375
		Culture.Media.Media*                         0.351
		Culture.Media.Music                          0.465
		Culture.Media.Radio                          0.359
		Culture.Media.Software                       0.083
		Culture.Media.Television                     0.376
		Culture.Media.Video games                    0.199
		Culture.Performing arts                      0.17
		Culture.Philosophy and religion              0.309
		Culture.Sports                               0.831
		Culture.Visual arts.Architecture             0.52
		Culture.Visual arts.Comics and Anime         0.109
		Culture.Visual arts.Fashion                  0.113
		Culture.Visual arts.Visual arts*             0.269
		Geography.Geographical                       0.425
		Geography.Regions.Africa.Africa*             0.221
		Geography.Regions.Africa.Central Africa      0.095
		Geography.Regions.Africa.Eastern Africa      0.126
		Geography.Regions.Africa.Northern Africa     0.146
		Geography.Regions.Africa.Southern Africa     0.258
		Geography.Regions.Africa.Western Africa      0.265
		Geography.Regions.Americas.Central America   0.124
		Geography.Regions.Americas.North America     0.494
		Geography.Regions.Americas.South America     0.277
		Geography.Regions.Asia.Asia*                 0.271
		Geography.Regions.Asia.Central Asia          0.127
		Geography.Regions.Asia.East Asia             0.195
		Geography.Regions.Asia.North Asia            0.292
		Geography.Regions.Asia.South Asia            0.612
		Geography.Regions.Asia.Southeast Asia        0.302
		Geography.Regions.Asia.West Asia             0.429
		Geography.Regions.Europe.Eastern Europe      0.482
		Geography.Regions.Europe.Europe*             0.386
		Geography.Regions.Europe.Northern Europe     0.494
		Geography.Regions.Europe.Southern Europe     0.44
		Geography.Regions.Europe.Western Europe      0.434
		Geography.Regions.Oceania                    0.597
		History and Society.Business and economics   0.224
		History and Society.Education                0.51
		History and Society.History                  0.311
		History and Society.Military and warfare     0.448
		History and Society.Politics and government  0.385
		History and Society.Society                  0.312
		History and Society.Transportation           0.584
		STEM.Biology                                 0.652
		STEM.Chemistry                               0.212
		STEM.Computing                               0.156
		STEM.Earth and environment                   0.234
		STEM.Engineering                             0.448
		STEM.Libraries & Information                 0.1
		STEM.Mathematics                             0.097
		STEM.Medicine & Health                       0.401
		STEM.Physics                                 0.1
		STEM.STEM*                                   0.376
		STEM.Space                                   0.599
		STEM.Technology                              0.141
		-------------------------------------------  -----
	!precision (micro=0.963, macro=0.987):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.913
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.993
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.961
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
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.954
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.931
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.99
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.988
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.955
		STEM.Space                                   0.997
		STEM.Technology                              0.996
		-------------------------------------------  -----
	f1 (micro=0.247, macro=0.177):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.411
		Culture.Biography.Women                      0.146
		Culture.Food and drink                       0.113
		Culture.Internet culture                     0.178
		Culture.Linguistics                          0.145
		Culture.Literature                           0.128
		Culture.Media.Books                          0.143
		Culture.Media.Entertainment                  0.2
		Culture.Media.Films                          0.237
		Culture.Media.Media*                         0.35
		Culture.Media.Music                          0.187
		Culture.Media.Radio                          0.314
		Culture.Media.Software                       0.132
		Culture.Media.Television                     0.271
		Culture.Media.Video games                    0.21
		Culture.Performing arts                      0.084
		Culture.Philosophy and religion              0.057
		Culture.Sports                               0.524
		Culture.Visual arts.Architecture             0.169
		Culture.Visual arts.Comics and Anime         0.13
		Culture.Visual arts.Fashion                  0.123
		Culture.Visual arts.Visual arts*             0.139
		Geography.Geographical                       0.249
		Geography.Regions.Africa.Africa*             0.093
		Geography.Regions.Africa.Central Africa      0.114
		Geography.Regions.Africa.Eastern Africa      0.161
		Geography.Regions.Africa.Northern Africa     0.119
		Geography.Regions.Africa.Southern Africa     0.231
		Geography.Regions.Africa.Western Africa      0.269
		Geography.Regions.Americas.Central America   0.077
		Geography.Regions.Americas.North America     0.144
		Geography.Regions.Americas.South America     0.11
		Geography.Regions.Asia.Asia*                 0.208
		Geography.Regions.Asia.Central Asia          0.112
		Geography.Regions.Asia.East Asia             0.156
		Geography.Regions.Asia.North Asia            0.153
		Geography.Regions.Asia.South Asia            0.107
		Geography.Regions.Asia.Southeast Asia        0.126
		Geography.Regions.Asia.West Asia             0.097
		Geography.Regions.Europe.Eastern Europe      0.175
		Geography.Regions.Europe.Europe*             0.253
		Geography.Regions.Europe.Northern Europe     0.089
		Geography.Regions.Europe.Southern Europe     0.104
		Geography.Regions.Europe.Western Europe      0.196
		Geography.Regions.Oceania                    0.134
		History and Society.Business and economics   0.082
		History and Society.Education                0.259
		History and Society.History                  0.098
		History and Society.Military and warfare     0.109
		History and Society.Politics and government  0.067
		History and Society.Society                  0.062
		History and Society.Transportation           0.373
		STEM.Biology                                 0.24
		STEM.Chemistry                               0.183
		STEM.Computing                               0.212
		STEM.Earth and environment                   0.095
		STEM.Engineering                             0.278
		STEM.Libraries & Information                 0.141
		STEM.Mathematics                             0.148
		STEM.Medicine & Health                       0.115
		STEM.Physics                                 0.103
		STEM.STEM*                                   0.37
		STEM.Space                                   0.387
		STEM.Technology                              0.167
		-------------------------------------------  -----
	!f1 (micro=0.974, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.935
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.988
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
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.996
		History and Society.Transportation           0.992
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.957
		STEM.Space                                   0.998
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.951, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.982
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.928
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.958
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.936
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.932
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.983
		History and Society.Society                  0.991
		History and Society.Transportation           0.985
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.919
		STEM.Space                                   0.996
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.042
		Culture.Biography.Women                      0.003
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.005
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.038
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.001
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.001
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.005
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.002
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.006
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.025
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.007
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.002
		Geography.Regions.Europe.Europe*             0.027
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.001
		Geography.Regions.Europe.Western Europe      0.003
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.002
		History and Society.Education                0.001
		History and Society.History                  0.001
		History and Society.Military and warfare     0.001
		History and Society.Politics and government  0.001
		History and Society.Society                  0.001
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.001
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.001
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.001
		STEM.Physics                                 0.001
		STEM.STEM*                                   0.042
		STEM.Space                                   0.001
		STEM.Technology                              0.007
		-------------------------------------------  -----
	roc_auc (micro=0.781, macro=0.782):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.823
		Culture.Biography.Women                      0.818
		Culture.Food and drink                       0.807
		Culture.Internet culture                     0.821
		Culture.Linguistics                          0.773
		Culture.Literature                           0.748
		Culture.Media.Books                          0.783
		Culture.Media.Entertainment                  0.799
		Culture.Media.Films                          0.826
		Culture.Media.Media*                         0.801
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.807
		Culture.Media.Software                       0.881
		Culture.Media.Television                     0.848
		Culture.Media.Video games                    0.836
		Culture.Performing arts                      0.775
		Culture.Philosophy and religion              0.732
		Culture.Sports                               0.849
		Culture.Visual arts.Architecture             0.774
		Culture.Visual arts.Comics and Anime         0.831
		Culture.Visual arts.Fashion                  0.773
		Culture.Visual arts.Visual arts*             0.726
		Geography.Geographical                       0.837
		Geography.Regions.Africa.Africa*             0.753
		Geography.Regions.Africa.Central Africa      0.78
		Geography.Regions.Africa.Eastern Africa      0.764
		Geography.Regions.Africa.Northern Africa     0.787
		Geography.Regions.Africa.Southern Africa     0.764
		Geography.Regions.Africa.Western Africa      0.755
		Geography.Regions.Americas.Central America   0.74
		Geography.Regions.Americas.North America     0.752
		Geography.Regions.Americas.South America     0.766
		Geography.Regions.Asia.Asia*                 0.735
		Geography.Regions.Asia.Central Asia          0.782
		Geography.Regions.Asia.East Asia             0.769
		Geography.Regions.Asia.North Asia            0.791
		Geography.Regions.Asia.South Asia            0.738
		Geography.Regions.Asia.Southeast Asia        0.743
		Geography.Regions.Asia.West Asia             0.752
		Geography.Regions.Europe.Eastern Europe      0.774
		Geography.Regions.Europe.Europe*             0.739
		Geography.Regions.Europe.Northern Europe     0.74
		Geography.Regions.Europe.Southern Europe     0.753
		Geography.Regions.Europe.Western Europe      0.779
		Geography.Regions.Oceania                    0.714
		History and Society.Business and economics   0.721
		History and Society.Education                0.79
		History and Society.History                  0.767
		History and Society.Military and warfare     0.773
		History and Society.Politics and government  0.738
		History and Society.Society                  0.689
		History and Society.Transportation           0.819
		STEM.Biology                                 0.812
		STEM.Chemistry                               0.816
		STEM.Computing                               0.879
		STEM.Earth and environment                   0.76
		STEM.Engineering                             0.81
		STEM.Libraries & Information                 0.765
		STEM.Mathematics                             0.836
		STEM.Medicine & Health                       0.764
		STEM.Physics                                 0.783
		STEM.STEM*                                   0.792
		STEM.Space                                   0.819
		STEM.Technology                              0.807
		-------------------------------------------  -----
	pr_auc (micro=0.243, macro=0.13):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.455
		Culture.Biography.Women                      0.125
		Culture.Food and drink                       0.034
		Culture.Internet culture                     0.1
		Culture.Linguistics                          0.097
		Culture.Literature                           0.076
		Culture.Media.Books                          0.069
		Culture.Media.Entertainment                  0.106
		Culture.Media.Films                          0.153
		Culture.Media.Media*                         0.307
		Culture.Media.Music                          0.184
		Culture.Media.Radio                          0.168
		Culture.Media.Software                       0.057
		Culture.Media.Television                     0.198
		Culture.Media.Video games                    0.11
		Culture.Performing arts                      0.036
		Culture.Philosophy and religion              0.063
		Culture.Sports                               0.557
		Culture.Visual arts.Architecture             0.14
		Culture.Visual arts.Comics and Anime         0.049
		Culture.Visual arts.Fashion                  0.03
		Culture.Visual arts.Visual arts*             0.102
		Geography.Geographical                       0.247
		Geography.Regions.Africa.Africa*             0.069
		Geography.Regions.Africa.Central Africa      0.034
		Geography.Regions.Africa.Eastern Africa      0.033
		Geography.Regions.Africa.Northern Africa     0.046
		Geography.Regions.Africa.Southern Africa     0.072
		Geography.Regions.Africa.Western Africa      0.068
		Geography.Regions.Americas.Central America   0.03
		Geography.Regions.Americas.North America     0.231
		Geography.Regions.Americas.South America     0.078
		Geography.Regions.Asia.Asia*                 0.165
		Geography.Regions.Asia.Central Asia          0.026
		Geography.Regions.Asia.East Asia             0.091
		Geography.Regions.Asia.North Asia            0.094
		Geography.Regions.Asia.South Asia            0.127
		Geography.Regions.Asia.Southeast Asia        0.08
		Geography.Regions.Asia.West Asia             0.103
		Geography.Regions.Europe.Eastern Europe      0.166
		Geography.Regions.Europe.Europe*             0.255
		Geography.Regions.Europe.Northern Europe     0.141
		Geography.Regions.Europe.Southern Europe     0.104
		Geography.Regions.Europe.Western Europe      0.178
		Geography.Regions.Oceania                    0.143
		History and Society.Business and economics   0.067
		History and Society.Education                0.192
		History and Society.History                  0.068
		History and Society.Military and warfare     0.117
		History and Society.Politics and government  0.082
		History and Society.Society                  0.052
		History and Society.Transportation           0.321
		STEM.Biology                                 0.284
		STEM.Chemistry                               0.056
		STEM.Computing                               0.106
		STEM.Earth and environment                   0.048
		STEM.Engineering                             0.192
		STEM.Libraries & Information                 0.034
		STEM.Mathematics                             0.072
		STEM.Medicine & Health                       0.075
		STEM.Physics                                 0.025
		STEM.STEM*                                   0.347
		STEM.Space                                   0.308
		STEM.Technology                              0.084
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}}

