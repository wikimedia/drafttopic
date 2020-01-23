Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'tol': 0.0001, 'min_impurity_split': None, 'multilabel': True, 'verbose': 0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_leaf_nodes': None, 'warm_start': False, 'population_rates': None, 'center': False, 'min_weight_fraction_leaf': 0.0, 'subsample': 1.0, 'n_estimators': 150, 'random_state': None, 'criterion': 'friedman_mse', 'validation_fraction': 0.1, 'max_features': 'log2', 'n_iter_no_change': None, 'init': None, 'max_depth': 5, 'min_samples_split': 2, 'loss': 'deviance', 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'scale': False, 'label_weights': {}, 'learning_rate': 0.1, 'presort': 'auto'}
	Environment:
	 - revscoring_version: '2.6.4-mmap'
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
	counts (n=59878):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13840  -->  12383  1457   829  45209
			'Culture.Biography.Women'                       5034  -->   4093   941   723  54121
			'Culture.Food and drink'                        1365  -->   1041   324    91  58422
			'Culture.Internet culture'                      3536  -->   3122   414   203  56139
			'Culture.Linguistics'                           1486  -->   1122   364    64  58328
			'Culture.Literature'                            5569  -->   4382  1187   400  53909
			'Culture.Media.Books'                           1422  -->   1095   327    82  58374
			'Culture.Media.Entertainment'                   2003  -->   1353   650   158  57717
			'Culture.Media.Films'                           2638  -->   2212   426   142  57098
			'Culture.Media.Media*'                         13246  -->  11665  1581  1169  45463
			'Culture.Media.Music'                           2946  -->   2574   372   170  56762
			'Culture.Media.Radio'                            312  -->    227    85    28  59538
			'Culture.Media.Software'                        2345  -->   2006   339   265  57268
			'Culture.Media.Television'                      1979  -->   1519   460   129  57770
			'Culture.Media.Video games'                     2103  -->   1995   108    32  57743
			'Culture.Performing arts'                       1413  -->   1062   351   107  58358
			'Culture.Philosophy and religion'               3030  -->   1793  1237   257  56591
			'Culture.Sports'                                3756  -->   3283   473   119  56003
			'Culture.Visual arts.Architecture'              1817  -->   1376   441   141  57920
			'Culture.Visual arts.Comics and Anime'          2218  -->   2053   165    71  57589
			'Culture.Visual arts.Fashion'                   1512  -->   1292   220    65  58301
			'Culture.Visual arts.Visual arts*'              6060  -->   4857  1203   321  53497
			'Geography.Geographical'                        3880  -->   2464  1416   574  55424
			'Geography.Regions.Africa.Africa*'              4938  -->   3975   963   327  54613
			'Geography.Regions.Africa.Central Africa'         28  -->      5    23    89  59761
			'Geography.Regions.Africa.Eastern Africa'        448  -->    322   126    29  59401
			'Geography.Regions.Africa.Northern Africa'      1462  -->   1134   328   105  58311
			'Geography.Regions.Africa.Southern Africa'      1167  -->    832   335    63  58648
			'Geography.Regions.Africa.Western Africa'        683  -->    572   111    53  59142
			'Geography.Regions.Americas.Central America'    1620  -->   1137   483   107  58151
			'Geography.Regions.Americas.North America'      5475  -->   3825  1650   634  53769
			'Geography.Regions.Americas.South America'      2140  -->   1699   441   170  57568
			'Geography.Regions.Asia.Asia*'                 13825  -->  11745  2080  1127  44926
			'Geography.Regions.Asia.Central Asia'           1239  -->   1020   219    55  58584
			'Geography.Regions.Asia.East Asia'              5508  -->   4598   910   449  53921
			'Geography.Regions.Asia.North Asia'             1727  -->   1395   332   204  57947
			'Geography.Regions.Asia.South Asia'             1998  -->   1627   371    71  57809
			'Geography.Regions.Asia.Southeast Asia'         2596  -->   1927   669   227  57055
			'Geography.Regions.Asia.West Asia'              2251  -->   1871   380   107  57520
			'Geography.Regions.Europe.Eastern Europe'       3586  -->   3010   576   271  56021
			'Geography.Regions.Europe.Europe*'             12616  -->  10370  2246  1127  46135
			'Geography.Regions.Europe.Northern Europe'      2912  -->   1991   921   235  56731
			'Geography.Regions.Europe.Southern Europe'      2780  -->   2153   627   160  56938
			'Geography.Regions.Europe.Western Europe'       4017  -->   3120   897   208  55653
			'Geography.Regions.Oceania'                     2190  -->   1604   586   140  57548
			'History and Society.Business and economics'    3336  -->   2188  1148   305  56237
			'History and Society.Education'                 1647  -->   1015   632   113  58118
			'History and Society.History'                   4423  -->   2500  1923   545  54910
			'History and Society.Military and warfare'      5028  -->   4045   983   466  54384
			'History and Society.Politics and government'   4560  -->   2631  1929   481  54837
			'History and Society.Society'                   6042  -->   3165  2877   519  53317
			'History and Society.Transportation'            3550  -->   3319   231    84  56244
			'STEM.Biology'                                  6608  -->   6120   488   140  53130
			'STEM.Chemistry'                                1464  -->   1167   297   163  58251
			'STEM.Computing'                                2467  -->   2122   345   252  57159
			'STEM.Earth and environment'                    1636  -->   1175   461   114  58128
			'STEM.Engineering'                              3046  -->   2576   470   136  56696
			'STEM.Libraries & Information'                   482  -->    372   110    31  59365
			'STEM.Mathematics'                               950  -->    830   120    45  58883
			'STEM.Medicine & Health'                        1834  -->   1434   400   161  57883
			'STEM.Physics'                                  1406  -->   1130   276   149  58323
			'STEM.STEM*'                                   20185  -->  18544  1641   821  38872
			'STEM.Space'                                    1642  -->   1529   113    44  58192
			'STEM.Technology'                               4343  -->   3366   977   545  54990
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.231         0.123
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.093         0.016
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.044         0.011
		Culture.Media.Media*                            0.221         0.059
		Culture.Media.Music                             0.049         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.051         0.011
		Culture.Sports                                  0.063         0.071
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.082         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.007         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.091         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.231         0.046
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
		Geography.Regions.Asia.North Asia               0.029         0.001
		Geography.Regions.Asia.South Asia               0.033         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.038         0.011
		Geography.Regions.Europe.Eastern Europe         0.06          0.013
		Geography.Regions.Europe.Europe*                0.211         0.076
		Geography.Regions.Europe.Northern Europe        0.049         0.031
		Geography.Regions.Europe.Southern Europe        0.046         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.028         0.007
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.084         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.11          0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.051         0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.031         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.337         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.073         0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.075
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
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.025
		History and Society.Society                  0.016
		History and Society.Transportation           0.016
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.925
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
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.975
		History and Society.Society                  0.984
		History and Society.Transportation           0.984
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.81, macro=0.776):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.813
		Culture.Food and drink                       0.763
		Culture.Internet culture                     0.883
		Culture.Linguistics                          0.755
		Culture.Literature                           0.787
		Culture.Media.Books                          0.77
		Culture.Media.Entertainment                  0.675
		Culture.Media.Films                          0.839
		Culture.Media.Media*                         0.881
		Culture.Media.Music                          0.874
		Culture.Media.Radio                          0.728
		Culture.Media.Software                       0.855
		Culture.Media.Television                     0.768
		Culture.Media.Video games                    0.949
		Culture.Performing arts                      0.752
		Culture.Philosophy and religion              0.592
		Culture.Sports                               0.874
		Culture.Visual arts.Architecture             0.757
		Culture.Visual arts.Comics and Anime         0.926
		Culture.Visual arts.Fashion                  0.854
		Culture.Visual arts.Visual arts*             0.801
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.805
		Geography.Regions.Africa.Central Africa      0.179
		Geography.Regions.Africa.Eastern Africa      0.719
		Geography.Regions.Africa.Northern Africa     0.776
		Geography.Regions.Africa.Southern Africa     0.713
		Geography.Regions.Africa.Western Africa      0.837
		Geography.Regions.Americas.Central America   0.702
		Geography.Regions.Americas.North America     0.699
		Geography.Regions.Americas.South America     0.794
		Geography.Regions.Asia.Asia*                 0.85
		Geography.Regions.Asia.Central Asia          0.823
		Geography.Regions.Asia.East Asia             0.835
		Geography.Regions.Asia.North Asia            0.808
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.742
		Geography.Regions.Asia.West Asia             0.831
		Geography.Regions.Europe.Eastern Europe      0.839
		Geography.Regions.Europe.Europe*             0.822
		Geography.Regions.Europe.Northern Europe     0.684
		Geography.Regions.Europe.Southern Europe     0.774
		Geography.Regions.Europe.Western Europe      0.777
		Geography.Regions.Oceania                    0.732
		History and Society.Business and economics   0.656
		History and Society.Education                0.616
		History and Society.History                  0.565
		History and Society.Military and warfare     0.804
		History and Society.Politics and government  0.577
		History and Society.Society                  0.524
		History and Society.Transportation           0.935
		STEM.Biology                                 0.926
		STEM.Chemistry                               0.797
		STEM.Computing                               0.86
		STEM.Earth and environment                   0.718
		STEM.Engineering                             0.846
		STEM.Libraries & Information                 0.772
		STEM.Mathematics                             0.874
		STEM.Medicine & Health                       0.782
		STEM.Physics                                 0.804
		STEM.STEM*                                   0.919
		STEM.Space                                   0.931
		STEM.Technology                              0.775
		-------------------------------------------  -----
	!recall (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.988
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.99
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.749, macro=0.602):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.477
		Culture.Food and drink                       0.548
		Culture.Internet culture                     0.463
		Culture.Linguistics                          0.836
		Culture.Literature                           0.627
		Culture.Media.Books                          0.689
		Culture.Media.Entertainment                  0.471
		Culture.Media.Films                          0.782
		Culture.Media.Media*                         0.686
		Culture.Media.Music                          0.878
		Culture.Media.Radio                          0.77
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.754
		Culture.Media.Video games                    0.818
		Culture.Performing arts                      0.543
		Culture.Philosophy and religion              0.585
		Culture.Sports                               0.969
		Culture.Visual arts.Architecture             0.769
		Culture.Visual arts.Comics and Anime         0.623
		Culture.Visual arts.Fashion                  0.383
		Culture.Visual arts.Visual arts*             0.715
		Geography.Geographical                       0.599
		Geography.Regions.Africa.Africa*             0.515
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.401
		Geography.Regions.Africa.Northern Africa     0.347
		Geography.Regions.Africa.Southern Africa     0.439
		Geography.Regions.Africa.Western Africa      0.39
		Geography.Regions.Americas.Central America   0.559
		Geography.Regions.Americas.North America     0.805
		Geography.Regions.Americas.South America     0.631
		Geography.Regions.Asia.Asia*                 0.623
		Geography.Regions.Asia.Central Asia          0.432
		Geography.Regions.Asia.East Asia             0.539
		Geography.Regions.Asia.North Asia            0.176
		Geography.Regions.Asia.South Asia            0.911
		Geography.Regions.Asia.Southeast Asia        0.531
		Geography.Regions.Asia.West Asia             0.832
		Geography.Regions.Europe.Eastern Europe      0.694
		Geography.Regions.Europe.Europe*             0.74
		Geography.Regions.Europe.Northern Europe     0.84
		Geography.Regions.Europe.Southern Europe     0.785
		Geography.Regions.Europe.Western Europe      0.803
		Geography.Regions.Oceania                    0.823
		History and Society.Business and economics   0.554
		History and Society.Education                0.702
		History and Society.History                  0.387
		History and Society.Military and warfare     0.575
		History and Society.Politics and government  0.658
		History and Society.Society                  0.41
		History and Society.Transportation           0.906
		STEM.Biology                                 0.925
		STEM.Chemistry                               0.309
		STEM.Computing                               0.346
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.65
		STEM.Libraries & Information                 0.479
		STEM.Mathematics                             0.323
		STEM.Medicine & Health                       0.645
		STEM.Physics                                 0.211
		STEM.STEM*                                   0.767
		STEM.Space                                   0.882
		STEM.Technology                              0.289
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.771, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.885
		Culture.Biography.Women                      0.601
		Culture.Food and drink                       0.638
		Culture.Internet culture                     0.607
		Culture.Linguistics                          0.793
		Culture.Literature                           0.698
		Culture.Media.Books                          0.728
		Culture.Media.Entertainment                  0.555
		Culture.Media.Films                          0.809
		Culture.Media.Media*                         0.771
		Culture.Media.Music                          0.876
		Culture.Media.Radio                          0.748
		Culture.Media.Software                       0.322
		Culture.Media.Television                     0.761
		Culture.Media.Video games                    0.878
		Culture.Performing arts                      0.631
		Culture.Philosophy and religion              0.588
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.763
		Culture.Visual arts.Comics and Anime         0.745
		Culture.Visual arts.Fashion                  0.529
		Culture.Visual arts.Visual arts*             0.756
		Geography.Geographical                       0.617
		Geography.Regions.Africa.Africa*             0.628
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.515
		Geography.Regions.Africa.Northern Africa     0.479
		Geography.Regions.Africa.Southern Africa     0.543
		Geography.Regions.Africa.Western Africa      0.532
		Geography.Regions.Americas.Central America   0.622
		Geography.Regions.Americas.North America     0.748
		Geography.Regions.Americas.South America     0.703
		Geography.Regions.Asia.Asia*                 0.719
		Geography.Regions.Asia.Central Asia          0.567
		Geography.Regions.Asia.East Asia             0.655
		Geography.Regions.Asia.North Asia            0.289
		Geography.Regions.Asia.South Asia            0.86
		Geography.Regions.Asia.Southeast Asia        0.619
		Geography.Regions.Asia.West Asia             0.831
		Geography.Regions.Europe.Eastern Europe      0.76
		Geography.Regions.Europe.Europe*             0.779
		Geography.Regions.Europe.Northern Europe     0.754
		Geography.Regions.Europe.Southern Europe     0.78
		Geography.Regions.Europe.Western Europe      0.79
		Geography.Regions.Oceania                    0.775
		History and Society.Business and economics   0.6
		History and Society.Education                0.656
		History and Society.History                  0.459
		History and Society.Military and warfare     0.671
		History and Society.Politics and government  0.615
		History and Society.Society                  0.46
		History and Society.Transportation           0.92
		STEM.Biology                                 0.925
		STEM.Chemistry                               0.445
		STEM.Computing                               0.493
		STEM.Earth and environment                   0.669
		STEM.Engineering                             0.735
		STEM.Libraries & Information                 0.591
		STEM.Mathematics                             0.472
		STEM.Medicine & Health                       0.707
		STEM.Physics                                 0.335
		STEM.STEM*                                   0.836
		STEM.Space                                   0.906
		STEM.Technology                              0.422
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.984
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.992
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.98
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.011, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.025
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.006
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.012
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.024
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.024
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.01
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.004
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.021
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.979, macro=0.976):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.986
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.976
		Culture.Literature                           0.983
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.979
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.971
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.984
		Culture.Philosophy and religion              0.965
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.657
		Geography.Regions.Africa.Eastern Africa      0.974
		Geography.Regions.Africa.Northern Africa     0.984
		Geography.Regions.Africa.Southern Africa     0.979
		Geography.Regions.Africa.Western Africa      0.984
		Geography.Regions.Americas.Central America   0.981
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.984
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.987
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.98
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.98
		History and Society.Business and economics   0.974
		History and Society.Education                0.977
		History and Society.History                  0.959
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.959
		History and Society.Society                  0.946
		History and Society.Transportation           0.99
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.987
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.982
		STEM.Engineering                             0.988
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.987
		STEM.Medicine & Health                       0.982
		STEM.Physics                                 0.988
		STEM.STEM*                                   0.983
		STEM.Space                                   0.992
		STEM.Technology                              0.981
		-------------------------------------------  -----
	pr_auc (micro=0.827, macro=0.692):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.933
		Culture.Biography.Women                      0.603
		Culture.Food and drink                       0.722
		Culture.Internet culture                     0.805
		Culture.Linguistics                          0.793
		Culture.Literature                           0.796
		Culture.Media.Books                          0.769
		Culture.Media.Entertainment                  0.554
		Culture.Media.Films                          0.855
		Culture.Media.Media*                         0.874
		Culture.Media.Music                          0.918
		Culture.Media.Radio                          0.6
		Culture.Media.Software                       0.383
		Culture.Media.Television                     0.772
		Culture.Media.Video games                    0.938
		Culture.Performing arts                      0.628
		Culture.Philosophy and religion              0.591
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.795
		Culture.Visual arts.Comics and Anime         0.858
		Culture.Visual arts.Fashion                  0.566
		Culture.Visual arts.Visual arts*             0.821
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.677
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.344
		Geography.Regions.Africa.Northern Africa     0.379
		Geography.Regions.Africa.Southern Africa     0.455
		Geography.Regions.Africa.Western Africa      0.364
		Geography.Regions.Americas.Central America   0.595
		Geography.Regions.Americas.North America     0.825
		Geography.Regions.Americas.South America     0.751
		Geography.Regions.Asia.Asia*                 0.819
		Geography.Regions.Asia.Central Asia          0.581
		Geography.Regions.Asia.East Asia             0.686
		Geography.Regions.Asia.North Asia            0.366
		Geography.Regions.Asia.South Asia            0.897
		Geography.Regions.Asia.Southeast Asia        0.613
		Geography.Regions.Asia.West Asia             0.888
		Geography.Regions.Europe.Eastern Europe      0.839
		Geography.Regions.Europe.Europe*             0.854
		Geography.Regions.Europe.Northern Europe     0.81
		Geography.Regions.Europe.Southern Europe     0.809
		Geography.Regions.Europe.Western Europe      0.84
		Geography.Regions.Oceania                    0.823
		History and Society.Business and economics   0.611
		History and Society.Education                0.671
		History and Society.History                  0.458
		History and Society.Military and warfare     0.75
		History and Society.Politics and government  0.639
		History and Society.Society                  0.456
		History and Society.Transportation           0.955
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.536
		STEM.Computing                               0.623
		STEM.Earth and environment                   0.676
		STEM.Engineering                             0.847
		STEM.Libraries & Information                 0.596
		STEM.Mathematics                             0.573
		STEM.Medicine & Health                       0.773
		STEM.Physics                                 0.361
		STEM.STEM*                                   0.934
		STEM.Space                                   0.952
		STEM.Technology                              0.508
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'properties': {'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}}

