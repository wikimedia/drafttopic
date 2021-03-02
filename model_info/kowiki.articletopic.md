Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'warm_start': False, 'population_rates': None, 'random_state': None, 'learning_rate': 0.1, 'n_estimators': 150, 'n_iter_no_change': None, 'scale': False, 'max_leaf_nodes': None, 'min_samples_split': 2, 'criterion': 'friedman_mse', 'label_weights': {}, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'ccp_alpha': 0.0, 'tol': 0.0001, 'center': False, 'max_depth': 5, 'presort': 'deprecated', 'max_features': 'log2', 'validation_fraction': 0.1, 'verbose': 0, 'min_weight_fraction_leaf': 0.0, 'subsample': 1.0, 'min_samples_leaf': 1, 'init': None, 'loss': 'deviance', 'multilabel': True}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=60594):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15726  -->  14324  1402   779  44089
			'Culture.Biography.Women'                       4248  -->   3162  1086   488  55858
			'Culture.Food and drink'                        1755  -->   1369   386    90  58749
			'Culture.Internet culture'                      3450  -->   2701   749   231  56913
			'Culture.Linguistics'                           1694  -->   1173   521    85  58815
			'Culture.Literature'                            5799  -->   4326  1473   559  54236
			'Culture.Media.Books'                           1581  -->   1177   404   134  58879
			'Culture.Media.Entertainment'                   2264  -->   1089  1175   240  58090
			'Culture.Media.Films'                           3017  -->   2463   554   146  57431
			'Culture.Media.Media*'                         15079  -->  12930  2149  1526  43989
			'Culture.Media.Music'                           3109  -->   2453   656   295  57190
			'Culture.Media.Radio'                            648  -->    376   272    57  59889
			'Culture.Media.Software'                        2301  -->   1682   619   350  57943
			'Culture.Media.Television'                      2529  -->   1790   739   223  57842
			'Culture.Media.Video games'                     2379  -->   2073   306    84  58131
			'Culture.Performing arts'                       1555  -->    928   627   129  58910
			'Culture.Philosophy and religion'               3835  -->   2115  1720   364  56395
			'Culture.Sports'                                5165  -->   4500   665   198  55231
			'Culture.Visual arts.Architecture'              2057  -->   1390   667   214  58323
			'Culture.Visual arts.Comics and Anime'          2462  -->   2047   415   197  57935
			'Culture.Visual arts.Fashion'                   1336  -->    933   403    99  59159
			'Culture.Visual arts.Visual arts*'              6348  -->   4615  1733   584  53662
			'Geography.Geographical'                        3884  -->   2591  1293   540  56170
			'Geography.Regions.Africa.Africa*'              4222  -->   3197  1025   266  56106
			'Geography.Regions.Africa.Central Africa'        806  -->    586   220    59  59729
			'Geography.Regions.Africa.Eastern Africa'        460  -->    318   142    33  60101
			'Geography.Regions.Africa.Northern Africa'      1453  -->   1086   367    89  59052
			'Geography.Regions.Africa.Southern Africa'       686  -->    504   182    63  59845
			'Geography.Regions.Africa.Western Africa'        259  -->    140   119    54  60281
			'Geography.Regions.Americas.Central America'    1364  -->    878   486    63  59167
			'Geography.Regions.Americas.North America'      6430  -->   4356  2074  1131  53033
			'Geography.Regions.Americas.South America'      1491  -->   1090   401    92  59011
			'Geography.Regions.Asia.Asia*'                 16214  -->  13536  2678  1561  42819
			'Geography.Regions.Asia.Central Asia'           1293  -->    922   371    90  59211
			'Geography.Regions.Asia.East Asia'              7753  -->   6377  1376   944  51897
			'Geography.Regions.Asia.North Asia'             3025  -->   2130   895   246  57323
			'Geography.Regions.Asia.South Asia'             1789  -->   1391   398    70  58735
			'Geography.Regions.Asia.Southeast Asia'         1943  -->   1409   534    79  58572
			'Geography.Regions.Asia.West Asia'              2247  -->   1624   623   166  58181
			'Geography.Regions.Europe.Eastern Europe'       4060  -->   2966  1094   286  56248
			'Geography.Regions.Europe.Europe*'             13945  -->  11217  2728  1609  45040
			'Geography.Regions.Europe.Northern Europe'      3718  -->   2647  1071   384  56492
			'Geography.Regions.Europe.Southern Europe'      3202  -->   2375   827   304  57088
			'Geography.Regions.Europe.Western Europe'       3924  -->   2926   998   401  56269
			'Geography.Regions.Oceania'                     1699  -->   1168   531    70  58825
			'History and Society.Business and economics'    3866  -->   2334  1532   464  56264
			'History and Society.Education'                 1910  -->   1211   699   169  58515
			'History and Society.History'                   5055  -->   2863  2192   632  54907
			'History and Society.Military and warfare'      4359  -->   2844  1515   428  55807
			'History and Society.Politics and government'   4008  -->   2179  1829   538  56048
			'History and Society.Society'                   4516  -->   1350  3166   374  55704
			'History and Society.Transportation'            3860  -->   3385   475   158  56576
			'STEM.Biology'                                  3485  -->   2738   747   201  56908
			'STEM.Chemistry'                                1512  -->   1184   328   149  58933
			'STEM.Computing'                                2739  -->   2156   583   465  57390
			'STEM.Earth and environment'                    1917  -->   1328   589   150  58527
			'STEM.Engineering'                              2709  -->   1967   742   209  57676
			'STEM.Libraries & Information'                   744  -->    534   210    64  59786
			'STEM.Mathematics'                              1158  -->    893   265    57  59379
			'STEM.Medicine & Health'                        1974  -->   1348   626   166  58454
			'STEM.Physics'                                  1499  -->   1033   466   189  58906
			'STEM.STEM*'                                   17852  -->  15802  2050  1020  41722
			'STEM.Space'                                    1686  -->   1492   194    64  58844
			'STEM.Technology'                               4605  -->   3217  1388   709  55280
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.26          0.121
		Culture.Biography.Women                         0.07          0.015
		Culture.Food and drink                          0.029         0.003
		Culture.Internet culture                        0.057         0.004
		Culture.Linguistics                             0.028         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.05          0.012
		Culture.Media.Media*                            0.249         0.055
		Culture.Media.Music                             0.051         0.021
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.039         0.003
		Culture.Performing arts                         0.026         0.003
		Culture.Philosophy and religion                 0.063         0.01
		Culture.Sports                                  0.085         0.061
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
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.268         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.128         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.03          0.017
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.067         0.018
		Geography.Regions.Europe.Europe*                0.23          0.082
		Geography.Regions.Europe.Northern Europe        0.061         0.029
		Geography.Regions.Europe.Southern Europe        0.053         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.083         0.011
		History and Society.Military and warfare        0.072         0.015
		History and Society.Politics and government     0.066         0.016
		History and Society.Society                     0.075         0.008
		History and Society.Transportation              0.064         0.016
		STEM.Biology                                    0.058         0.035
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.045         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.295         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.076         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.063
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.078
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.028
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.097
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.017
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.018
		History and Society.Society                  0.009
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.08
		STEM.Space                                   0.005
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.922
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.903
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.983
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.982
		History and Society.Society                  0.991
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.92
		STEM.Space                                   0.995
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.777, macro=0.72):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.911
		Culture.Biography.Women                      0.744
		Culture.Food and drink                       0.78
		Culture.Internet culture                     0.783
		Culture.Linguistics                          0.692
		Culture.Literature                           0.746
		Culture.Media.Books                          0.744
		Culture.Media.Entertainment                  0.481
		Culture.Media.Films                          0.816
		Culture.Media.Media*                         0.857
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.58
		Culture.Media.Software                       0.731
		Culture.Media.Television                     0.708
		Culture.Media.Video games                    0.871
		Culture.Performing arts                      0.597
		Culture.Philosophy and religion              0.551
		Culture.Sports                               0.871
		Culture.Visual arts.Architecture             0.676
		Culture.Visual arts.Comics and Anime         0.831
		Culture.Visual arts.Fashion                  0.698
		Culture.Visual arts.Visual arts*             0.727
		Geography.Geographical                       0.667
		Geography.Regions.Africa.Africa*             0.757
		Geography.Regions.Africa.Central Africa      0.727
		Geography.Regions.Africa.Eastern Africa      0.691
		Geography.Regions.Africa.Northern Africa     0.747
		Geography.Regions.Africa.Southern Africa     0.735
		Geography.Regions.Africa.Western Africa      0.541
		Geography.Regions.Americas.Central America   0.644
		Geography.Regions.Americas.North America     0.677
		Geography.Regions.Americas.South America     0.731
		Geography.Regions.Asia.Asia*                 0.835
		Geography.Regions.Asia.Central Asia          0.713
		Geography.Regions.Asia.East Asia             0.823
		Geography.Regions.Asia.North Asia            0.704
		Geography.Regions.Asia.South Asia            0.778
		Geography.Regions.Asia.Southeast Asia        0.725
		Geography.Regions.Asia.West Asia             0.723
		Geography.Regions.Europe.Eastern Europe      0.731
		Geography.Regions.Europe.Europe*             0.804
		Geography.Regions.Europe.Northern Europe     0.712
		Geography.Regions.Europe.Southern Europe     0.742
		Geography.Regions.Europe.Western Europe      0.746
		Geography.Regions.Oceania                    0.687
		History and Society.Business and economics   0.604
		History and Society.Education                0.634
		History and Society.History                  0.566
		History and Society.Military and warfare     0.652
		History and Society.Politics and government  0.544
		History and Society.Society                  0.299
		History and Society.Transportation           0.877
		STEM.Biology                                 0.786
		STEM.Chemistry                               0.783
		STEM.Computing                               0.787
		STEM.Earth and environment                   0.693
		STEM.Engineering                             0.726
		STEM.Libraries & Information                 0.718
		STEM.Mathematics                             0.771
		STEM.Medicine & Health                       0.683
		STEM.Physics                                 0.689
		STEM.STEM*                                   0.885
		STEM.Space                                   0.885
		STEM.Technology                              0.699
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.695, macro=0.557):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.569
		Culture.Food and drink                       0.568
		Culture.Internet culture                     0.423
		Culture.Linguistics                          0.797
		Culture.Literature                           0.527
		Culture.Media.Books                          0.589
		Culture.Media.Entertainment                  0.319
		Culture.Media.Films                          0.791
		Culture.Media.Media*                         0.6
		Culture.Media.Music                          0.769
		Culture.Media.Radio                          0.589
		Culture.Media.Software                       0.139
		Culture.Media.Television                     0.625
		Culture.Media.Video games                    0.64
		Culture.Performing arts                      0.458
		Culture.Philosophy and religion              0.476
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.671
		Culture.Visual arts.Comics and Anime         0.373
		Culture.Visual arts.Fashion                  0.275
		Culture.Visual arts.Visual arts*             0.557
		Geography.Geographical                       0.604
		Geography.Regions.Africa.Africa*             0.581
		Geography.Regions.Africa.Central Africa      0.344
		Geography.Regions.Africa.Eastern Africa      0.39
		Geography.Regions.Africa.Northern Africa     0.404
		Geography.Regions.Africa.Southern Africa     0.48
		Geography.Regions.Africa.Western Africa      0.313
		Geography.Regions.Americas.Central America   0.679
		Geography.Regions.Americas.North America     0.688
		Geography.Regions.Americas.South America     0.766
		Geography.Regions.Asia.Asia*                 0.571
		Geography.Regions.Asia.Central Asia          0.274
		Geography.Regions.Asia.East Asia             0.364
		Geography.Regions.Asia.North Asia            0.484
		Geography.Regions.Asia.South Asia            0.917
		Geography.Regions.Asia.Southeast Asia        0.773
		Geography.Regions.Asia.West Asia             0.752
		Geography.Regions.Europe.Eastern Europe      0.731
		Geography.Regions.Europe.Europe*             0.675
		Geography.Regions.Europe.Northern Europe     0.761
		Geography.Regions.Europe.Southern Europe     0.665
		Geography.Regions.Europe.Western Europe      0.69
		Geography.Regions.Oceania                    0.907
		History and Society.Business and economics   0.423
		History and Society.Education                0.64
		History and Society.History                  0.355
		History and Society.Military and warfare     0.574
		History and Society.Politics and government  0.489
		History and Society.Society                  0.274
		History and Society.Transportation           0.84
		STEM.Biology                                 0.89
		STEM.Chemistry                               0.347
		STEM.Computing                               0.219
		STEM.Earth and environment                   0.565
		STEM.Engineering                             0.54
		STEM.Libraries & Information                 0.317
		STEM.Mathematics                             0.273
		STEM.Medicine & Health                       0.612
		STEM.Physics                                 0.169
		STEM.STEM*                                   0.723
		STEM.Space                                   0.779
		STEM.Technology                              0.224
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.988
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
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
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.726, macro=0.609):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.645
		Culture.Food and drink                       0.658
		Culture.Internet culture                     0.549
		Culture.Linguistics                          0.741
		Culture.Literature                           0.618
		Culture.Media.Books                          0.658
		Culture.Media.Entertainment                  0.383
		Culture.Media.Films                          0.804
		Culture.Media.Media*                         0.706
		Culture.Media.Music                          0.779
		Culture.Media.Radio                          0.585
		Culture.Media.Software                       0.233
		Culture.Media.Television                     0.664
		Culture.Media.Video games                    0.738
		Culture.Performing arts                      0.518
		Culture.Philosophy and religion              0.511
		Culture.Sports                               0.905
		Culture.Visual arts.Architecture             0.673
		Culture.Visual arts.Comics and Anime         0.515
		Culture.Visual arts.Fashion                  0.394
		Culture.Visual arts.Visual arts*             0.631
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.658
		Geography.Regions.Africa.Central Africa      0.467
		Geography.Regions.Africa.Eastern Africa      0.499
		Geography.Regions.Africa.Northern Africa     0.524
		Geography.Regions.Africa.Southern Africa     0.581
		Geography.Regions.Africa.Western Africa      0.396
		Geography.Regions.Americas.Central America   0.661
		Geography.Regions.Americas.North America     0.683
		Geography.Regions.Americas.South America     0.748
		Geography.Regions.Asia.Asia*                 0.678
		Geography.Regions.Asia.Central Asia          0.396
		Geography.Regions.Asia.East Asia             0.505
		Geography.Regions.Asia.North Asia            0.574
		Geography.Regions.Asia.South Asia            0.842
		Geography.Regions.Asia.Southeast Asia        0.748
		Geography.Regions.Asia.West Asia             0.737
		Geography.Regions.Europe.Eastern Europe      0.731
		Geography.Regions.Europe.Europe*             0.734
		Geography.Regions.Europe.Northern Europe     0.736
		Geography.Regions.Europe.Southern Europe     0.701
		Geography.Regions.Europe.Western Europe      0.717
		Geography.Regions.Oceania                    0.782
		History and Society.Business and economics   0.497
		History and Society.Education                0.637
		History and Society.History                  0.437
		History and Society.Military and warfare     0.61
		History and Society.Politics and government  0.515
		History and Society.Society                  0.286
		History and Society.Transportation           0.858
		STEM.Biology                                 0.834
		STEM.Chemistry                               0.481
		STEM.Computing                               0.342
		STEM.Earth and environment                   0.622
		STEM.Engineering                             0.619
		STEM.Libraries & Information                 0.44
		STEM.Mathematics                             0.403
		STEM.Medicine & Health                       0.645
		STEM.Physics                                 0.272
		STEM.STEM*                                   0.796
		STEM.Space                                   0.828
		STEM.Technology                              0.339
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.958
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.035
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.007
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.977
		Culture.Literature                           0.975
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.963
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.971
		Culture.Philosophy and religion              0.951
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.969
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.971
		Geography.Regions.Africa.Western Africa      0.956
		Geography.Regions.Americas.Central America   0.974
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.984
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.974
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.98
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.972
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.965
		History and Society.Education                0.973
		History and Society.History                  0.953
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.955
		History and Society.Society                  0.906
		History and Society.Transportation           0.985
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.987
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.978
		STEM.Engineering                             0.977
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.976
		STEM.Space                                   0.989
		STEM.Technology                              0.973
		-------------------------------------------  -----
	pr_auc (micro=0.775, macro=0.625):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.952
		Culture.Biography.Women                      0.62
		Culture.Food and drink                       0.701
		Culture.Internet culture                     0.677
		Culture.Linguistics                          0.762
		Culture.Literature                           0.678
		Culture.Media.Books                          0.695
		Culture.Media.Entertainment                  0.35
		Culture.Media.Films                          0.862
		Culture.Media.Media*                         0.825
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.479
		Culture.Media.Software                       0.277
		Culture.Media.Television                     0.651
		Culture.Media.Video games                    0.845
		Culture.Performing arts                      0.482
		Culture.Philosophy and religion              0.491
		Culture.Sports                               0.939
		Culture.Visual arts.Architecture             0.684
		Culture.Visual arts.Comics and Anime         0.594
		Culture.Visual arts.Fashion                  0.324
		Culture.Visual arts.Visual arts*             0.687
		Geography.Geographical                       0.665
		Geography.Regions.Africa.Africa*             0.69
		Geography.Regions.Africa.Central Africa      0.42
		Geography.Regions.Africa.Eastern Africa      0.348
		Geography.Regions.Africa.Northern Africa     0.474
		Geography.Regions.Africa.Southern Africa     0.438
		Geography.Regions.Africa.Western Africa      0.259
		Geography.Regions.Americas.Central America   0.638
		Geography.Regions.Americas.North America     0.725
		Geography.Regions.Americas.South America     0.742
		Geography.Regions.Asia.Asia*                 0.754
		Geography.Regions.Asia.Central Asia          0.36
		Geography.Regions.Asia.East Asia             0.557
		Geography.Regions.Asia.North Asia            0.561
		Geography.Regions.Asia.South Asia            0.892
		Geography.Regions.Asia.Southeast Asia        0.759
		Geography.Regions.Asia.West Asia             0.769
		Geography.Regions.Europe.Eastern Europe      0.751
		Geography.Regions.Europe.Europe*             0.799
		Geography.Regions.Europe.Northern Europe     0.79
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.754
		Geography.Regions.Oceania                    0.844
		History and Society.Business and economics   0.482
		History and Society.Education                0.667
		History and Society.History                  0.417
		History and Society.Military and warfare     0.663
		History and Society.Politics and government  0.503
		History and Society.Society                  0.244
		History and Society.Transportation           0.906
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.482
		STEM.Computing                               0.344
		STEM.Earth and environment                   0.643
		STEM.Engineering                             0.679
		STEM.Libraries & Information                 0.371
		STEM.Mathematics                             0.585
		STEM.Medicine & Health                       0.662
		STEM.Physics                                 0.242
		STEM.STEM*                                   0.898
		STEM.Space                                   0.849
		STEM.Technology                              0.401
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Media.Media*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}}}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}}

