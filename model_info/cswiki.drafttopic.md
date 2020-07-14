Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'verbose': 0, 'n_iter_no_change': None, 'label_weights': {}, 'center': False, 'population_rates': None, 'n_estimators': 150, 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'presort': 'deprecated', 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'validation_fraction': 0.1, 'learning_rate': 0.1, 'tol': 0.0001, 'loss': 'deviance', 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'random_state': None, 'max_leaf_nodes': None, 'scale': False, 'init': None, 'subsample': 1.0, 'min_samples_split': 2, 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=58736):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16082  -->  14136  1946  1171  41483
			'Culture.Biography.Women'                       4134  -->   3280   854   329  54273
			'Culture.Food and drink'                        1541  -->    996   545   147  57048
			'Culture.Internet culture'                      3075  -->   2347   728   277  55384
			'Culture.Linguistics'                           1548  -->   1013   535    98  57090
			'Culture.Literature'                            4853  -->   3265  1588   491  53392
			'Culture.Media.Books'                           1658  -->   1204   454   181  56897
			'Culture.Media.Entertainment'                   2214  -->    885  1329   278  56244
			'Culture.Media.Films'                           2464  -->   1917   547   149  56123
			'Culture.Media.Media*'                         14000  -->  11803  2197  1431  43305
			'Culture.Media.Music'                           3257  -->   2616   641   286  55193
			'Culture.Media.Radio'                            417  -->    183   234    50  58269
			'Culture.Media.Software'                        2301  -->   1705   596   374  56061
			'Culture.Media.Television'                      2495  -->   1954   541   155  56086
			'Culture.Media.Video games'                     1832  -->   1597   235    68  56836
			'Culture.Performing arts'                       1480  -->    854   626   121  57135
			'Culture.Philosophy and religion'               4308  -->   2148  2160   439  53989
			'Culture.Sports'                                5661  -->   4951   710   202  52873
			'Culture.Visual arts.Architecture'              2272  -->   1510   762   237  56227
			'Culture.Visual arts.Comics and Anime'          1653  -->   1342   311    76  57007
			'Culture.Visual arts.Fashion'                   1010  -->    584   426    82  57644
			'Culture.Visual arts.Visual arts*'              5793  -->   3952  1841   459  52484
			'Geography.Geographical'                        4552  -->   3044  1508   648  53536
			'Geography.Regions.Africa.Africa*'              4005  -->   2395  1610   323  54408
			'Geography.Regions.Africa.Central Africa'        719  -->    301   418    65  57952
			'Geography.Regions.Africa.Eastern Africa'        470  -->    233   237    49  58217
			'Geography.Regions.Africa.Northern Africa'      1517  -->    835   682   137  57082
			'Geography.Regions.Africa.Southern Africa'       660  -->    272   388    60  58016
			'Geography.Regions.Africa.Western Africa'        182  -->     87    95    25  58529
			'Geography.Regions.Americas.Central America'    1324  -->    585   739    74  57338
			'Geography.Regions.Americas.North America'      5900  -->   3222  2678   968  51868
			'Geography.Regions.Americas.South America'      1453  -->    916   537   103  57180
			'Geography.Regions.Asia.Asia*'                 10657  -->   8023  2634   935  47144
			'Geography.Regions.Asia.Central Asia'           1288  -->    751   537   108  57340
			'Geography.Regions.Asia.East Asia'              2908  -->   2099   809   210  55618
			'Geography.Regions.Asia.North Asia'             1912  -->   1180   732   314  56510
			'Geography.Regions.Asia.South Asia'             1779  -->   1190   589    92  56865
			'Geography.Regions.Asia.Southeast Asia'         1582  -->    832   750    93  57061
			'Geography.Regions.Asia.West Asia'              2824  -->   2089   735   153  55759
			'Geography.Regions.Europe.Eastern Europe'       5143  -->   3448  1695   675  52918
			'Geography.Regions.Europe.Europe*'             16514  -->  12301  4213  2624  39598
			'Geography.Regions.Europe.Northern Europe'      3933  -->   2238  1695   434  54369
			'Geography.Regions.Europe.Southern Europe'      3385  -->   2067  1318   344  55007
			'Geography.Regions.Europe.Western Europe'       5102  -->   3301  1801   676  52958
			'Geography.Regions.Oceania'                     1711  -->   1063   648   100  56925
			'History and Society.Business and economics'    3464  -->   1812  1652   360  54912
			'History and Society.Education'                 1793  -->    759  1034   145  56798
			'History and Society.History'                   5442  -->   2907  2535   760  52534
			'History and Society.Military and warfare'      5679  -->   3775  1904   596  52461
			'History and Society.Politics and government'   4572  -->   2077  2495   447  53717
			'History and Society.Society'                   6690  -->   2806  3884   626  51420
			'History and Society.Transportation'            4217  -->   3700   517   192  54327
			'STEM.Biology'                                  3716  -->   2831   885   195  54825
			'STEM.Chemistry'                                1567  -->   1149   418   152  57017
			'STEM.Computing'                                2762  -->   2124   638   401  55573
			'STEM.Earth and environment'                    2186  -->   1317   869   165  56385
			'STEM.Engineering'                              2908  -->   2074   834   227  55601
			'STEM.Libraries & Information'                   706  -->    451   255    50  57980
			'STEM.Mathematics'                              1186  -->    863   323    73  57477
			'STEM.Medicine & Health'                        2029  -->   1172   857   195  56512
			'STEM.Physics'                                  1433  -->    819   614   174  57129
			'STEM.STEM*'                                   18575  -->  16102  2473  1251  38910
			'STEM.Space'                                    2040  -->   1784   256    51  56645
			'STEM.Technology'                               5041  -->   3472  1569   679  53016
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.274         0.123
		Culture.Biography.Women                         0.07          0.015
		Culture.Food and drink                          0.026         0.002
		Culture.Internet culture                        0.052         0.003
		Culture.Linguistics                             0.026         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.055         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.096         0.071
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.017         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.181         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.05          0.011
		Geography.Regions.Asia.North Asia               0.033         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.088         0.013
		Geography.Regions.Europe.Europe*                0.281         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.058         0.013
		Geography.Regions.Europe.Western Europe         0.087         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.097         0.014
		History and Society.Politics and government     0.078         0.028
		History and Society.Society                     0.114         0.013
		History and Society.Transportation              0.072         0.015
		STEM.Biology                                    0.063         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.316         0.069
		STEM.Space                                      0.035         0.006
		STEM.Technology                                 0.086         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.006
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.027
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.052
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.114
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.02
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.021
		History and Society.Society                  0.017
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.089
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.994
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.948
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.886
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.98
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.979
		History and Society.Society                  0.983
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.911
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.727, macro=0.65):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.793
		Culture.Food and drink                       0.646
		Culture.Internet culture                     0.763
		Culture.Linguistics                          0.654
		Culture.Literature                           0.673
		Culture.Media.Books                          0.726
		Culture.Media.Entertainment                  0.4
		Culture.Media.Films                          0.778
		Culture.Media.Media*                         0.843
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.439
		Culture.Media.Software                       0.741
		Culture.Media.Television                     0.783
		Culture.Media.Video games                    0.872
		Culture.Performing arts                      0.577
		Culture.Philosophy and religion              0.499
		Culture.Sports                               0.875
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.812
		Culture.Visual arts.Fashion                  0.578
		Culture.Visual arts.Visual arts*             0.682
		Geography.Geographical                       0.669
		Geography.Regions.Africa.Africa*             0.598
		Geography.Regions.Africa.Central Africa      0.419
		Geography.Regions.Africa.Eastern Africa      0.496
		Geography.Regions.Africa.Northern Africa     0.55
		Geography.Regions.Africa.Southern Africa     0.412
		Geography.Regions.Africa.Western Africa      0.478
		Geography.Regions.Americas.Central America   0.442
		Geography.Regions.Americas.North America     0.546
		Geography.Regions.Americas.South America     0.63
		Geography.Regions.Asia.Asia*                 0.753
		Geography.Regions.Asia.Central Asia          0.583
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.617
		Geography.Regions.Asia.South Asia            0.669
		Geography.Regions.Asia.Southeast Asia        0.526
		Geography.Regions.Asia.West Asia             0.74
		Geography.Regions.Europe.Eastern Europe      0.67
		Geography.Regions.Europe.Europe*             0.745
		Geography.Regions.Europe.Northern Europe     0.569
		Geography.Regions.Europe.Southern Europe     0.611
		Geography.Regions.Europe.Western Europe      0.647
		Geography.Regions.Oceania                    0.621
		History and Society.Business and economics   0.523
		History and Society.Education                0.423
		History and Society.History                  0.534
		History and Society.Military and warfare     0.665
		History and Society.Politics and government  0.454
		History and Society.Society                  0.419
		History and Society.Transportation           0.877
		STEM.Biology                                 0.762
		STEM.Chemistry                               0.733
		STEM.Computing                               0.769
		STEM.Earth and environment                   0.602
		STEM.Engineering                             0.713
		STEM.Libraries & Information                 0.639
		STEM.Mathematics                             0.728
		STEM.Medicine & Health                       0.578
		STEM.Physics                                 0.572
		STEM.STEM*                                   0.867
		STEM.Space                                   0.875
		STEM.Technology                              0.689
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.992
		History and Society.Society                  0.988
		History and Society.Transportation           0.996
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.661, macro=0.511):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.818
		Culture.Biography.Women                      0.66
		Culture.Food and drink                       0.383
		Culture.Internet culture                     0.35
		Culture.Linguistics                          0.738
		Culture.Literature                           0.537
		Culture.Media.Books                          0.481
		Culture.Media.Entertainment                  0.226
		Culture.Media.Films                          0.757
		Culture.Media.Media*                         0.621
		Culture.Media.Music                          0.792
		Culture.Media.Radio                          0.525
		Culture.Media.Software                       0.129
		Culture.Media.Television                     0.716
		Culture.Media.Video games                    0.656
		Culture.Performing arts                      0.441
		Culture.Philosophy and religion              0.4
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.628
		Culture.Visual arts.Comics and Anime         0.573
		Culture.Visual arts.Fashion                  0.248
		Culture.Visual arts.Visual arts*             0.595
		Geography.Geographical                       0.574
		Geography.Regions.Africa.Africa*             0.443
		Geography.Regions.Africa.Central Africa      0.191
		Geography.Regions.Africa.Eastern Africa      0.211
		Geography.Regions.Africa.Northern Africa     0.22
		Geography.Regions.Africa.Southern Africa     0.319
		Geography.Regions.Africa.Western Africa      0.434
		Geography.Regions.Americas.Central America   0.532
		Geography.Regions.Americas.North America     0.672
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.649
		Geography.Regions.Asia.Central Asia          0.212
		Geography.Regions.Asia.East Asia             0.689
		Geography.Regions.Asia.North Asia            0.094
		Geography.Regions.Asia.South Asia            0.865
		Geography.Regions.Asia.Southeast Asia        0.661
		Geography.Regions.Asia.West Asia             0.749
		Geography.Regions.Europe.Eastern Europe      0.409
		Geography.Regions.Europe.Europe*             0.497
		Geography.Regions.Europe.Northern Europe     0.694
		Geography.Regions.Europe.Southern Europe     0.565
		Geography.Regions.Europe.Western Europe      0.501
		Geography.Regions.Oceania                    0.845
		History and Society.Business and economics   0.45
		History and Society.Education                0.552
		History and Society.History                  0.291
		History and Society.Military and warfare     0.458
		History and Society.Politics and government  0.615
		History and Society.Society                  0.308
		History and Society.Transportation           0.792
		STEM.Biology                                 0.882
		STEM.Chemistry                               0.301
		STEM.Computing                               0.224
		STEM.Earth and environment                   0.485
		STEM.Engineering                             0.48
		STEM.Libraries & Information                 0.315
		STEM.Mathematics                             0.193
		STEM.Medicine & Health                       0.52
		STEM.Physics                                 0.138
		STEM.STEM*                                   0.674
		STEM.Space                                   0.855
		STEM.Technology                              0.219
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.984
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.683, macro=0.55):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.847
		Culture.Biography.Women                      0.721
		Culture.Food and drink                       0.481
		Culture.Internet culture                     0.48
		Culture.Linguistics                          0.694
		Culture.Literature                           0.598
		Culture.Media.Books                          0.578
		Culture.Media.Entertainment                  0.289
		Culture.Media.Films                          0.768
		Culture.Media.Media*                         0.715
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.478
		Culture.Media.Software                       0.22
		Culture.Media.Television                     0.748
		Culture.Media.Video games                    0.749
		Culture.Performing arts                      0.5
		Culture.Philosophy and religion              0.444
		Culture.Sports                               0.909
		Culture.Visual arts.Architecture             0.646
		Culture.Visual arts.Comics and Anime         0.672
		Culture.Visual arts.Fashion                  0.347
		Culture.Visual arts.Visual arts*             0.635
		Geography.Geographical                       0.618
		Geography.Regions.Africa.Africa*             0.509
		Geography.Regions.Africa.Central Africa      0.262
		Geography.Regions.Africa.Eastern Africa      0.296
		Geography.Regions.Africa.Northern Africa     0.315
		Geography.Regions.Africa.Southern Africa     0.36
		Geography.Regions.Africa.Western Africa      0.455
		Geography.Regions.Americas.Central America   0.483
		Geography.Regions.Americas.North America     0.602
		Geography.Regions.Americas.South America     0.659
		Geography.Regions.Asia.Asia*                 0.697
		Geography.Regions.Asia.Central Asia          0.311
		Geography.Regions.Asia.East Asia             0.705
		Geography.Regions.Asia.North Asia            0.163
		Geography.Regions.Asia.South Asia            0.754
		Geography.Regions.Asia.Southeast Asia        0.586
		Geography.Regions.Asia.West Asia             0.744
		Geography.Regions.Europe.Eastern Europe      0.508
		Geography.Regions.Europe.Europe*             0.596
		Geography.Regions.Europe.Northern Europe     0.625
		Geography.Regions.Europe.Southern Europe     0.587
		Geography.Regions.Europe.Western Europe      0.565
		Geography.Regions.Oceania                    0.716
		History and Society.Business and economics   0.484
		History and Society.Education                0.479
		History and Society.History                  0.377
		History and Society.Military and warfare     0.542
		History and Society.Politics and government  0.523
		History and Society.Society                  0.355
		History and Society.Transportation           0.833
		STEM.Biology                                 0.818
		STEM.Chemistry                               0.427
		STEM.Computing                               0.348
		STEM.Earth and environment                   0.537
		STEM.Engineering                             0.574
		STEM.Libraries & Information                 0.422
		STEM.Mathematics                             0.305
		STEM.Medicine & Health                       0.547
		STEM.Physics                                 0.222
		STEM.STEM*                                   0.758
		STEM.Space                                   0.865
		STEM.Technology                              0.333
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.988
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.961
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.923
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.977
		History and Society.Society                  0.981
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.027
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.062
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.013
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.014
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.008
		History and Society.Society                  0.012
		History and Society.Transportation           0.004
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.965):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.978
		Culture.Linguistics                          0.966
		Culture.Literature                           0.966
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.956
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.934
		Culture.Media.Software                       0.982
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.97
		Culture.Philosophy and religion              0.938
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.962
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.959
		Geography.Regions.Africa.Central Africa      0.966
		Geography.Regions.Africa.Eastern Africa      0.955
		Geography.Regions.Africa.Northern Africa     0.969
		Geography.Regions.Africa.Southern Africa     0.943
		Geography.Regions.Africa.Western Africa      0.898
		Geography.Regions.Americas.Central America   0.954
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.965
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.967
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.977
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.959
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.964
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.954
		Geography.Regions.Europe.Southern Europe     0.962
		Geography.Regions.Europe.Western Europe      0.961
		Geography.Regions.Oceania                    0.968
		History and Society.Business and economics   0.951
		History and Society.Education                0.949
		History and Society.History                  0.944
		History and Society.Military and warfare     0.965
		History and Society.Politics and government  0.932
		History and Society.Society                  0.899
		History and Society.Transportation           0.984
		STEM.Biology                                 0.975
		STEM.Chemistry                               0.982
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.974
		STEM.Libraries & Information                 0.964
		STEM.Mathematics                             0.976
		STEM.Medicine & Health                       0.968
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.971
		STEM.Space                                   0.988
		STEM.Technology                              0.969
		-------------------------------------------  -----
	pr_auc (micro=0.724, macro=0.541):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.912
		Culture.Biography.Women                      0.717
		Culture.Food and drink                       0.54
		Culture.Internet culture                     0.565
		Culture.Linguistics                          0.672
		Culture.Literature                           0.644
		Culture.Media.Books                          0.582
		Culture.Media.Entertainment                  0.206
		Culture.Media.Films                          0.781
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.846
		Culture.Media.Radio                          0.259
		Culture.Media.Software                       0.244
		Culture.Media.Television                     0.801
		Culture.Media.Video games                    0.806
		Culture.Performing arts                      0.446
		Culture.Philosophy and religion              0.399
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.647
		Culture.Visual arts.Comics and Anime         0.682
		Culture.Visual arts.Fashion                  0.283
		Culture.Visual arts.Visual arts*             0.663
		Geography.Geographical                       0.619
		Geography.Regions.Africa.Africa*             0.469
		Geography.Regions.Africa.Central Africa      0.118
		Geography.Regions.Africa.Eastern Africa      0.116
		Geography.Regions.Africa.Northern Africa     0.246
		Geography.Regions.Africa.Southern Africa     0.206
		Geography.Regions.Africa.Western Africa      0.195
		Geography.Regions.Americas.Central America   0.392
		Geography.Regions.Americas.North America     0.666
		Geography.Regions.Americas.South America     0.64
		Geography.Regions.Asia.Asia*                 0.751
		Geography.Regions.Asia.Central Asia          0.207
		Geography.Regions.Asia.East Asia             0.734
		Geography.Regions.Asia.North Asia            0.111
		Geography.Regions.Asia.South Asia            0.779
		Geography.Regions.Asia.Southeast Asia        0.541
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.508
		Geography.Regions.Europe.Europe*             0.649
		Geography.Regions.Europe.Northern Europe     0.666
		Geography.Regions.Europe.Southern Europe     0.571
		Geography.Regions.Europe.Western Europe      0.555
		Geography.Regions.Oceania                    0.756
		History and Society.Business and economics   0.427
		History and Society.Education                0.446
		History and Society.History                  0.369
		History and Society.Military and warfare     0.598
		History and Society.Politics and government  0.534
		History and Society.Society                  0.3
		History and Society.Transportation           0.894
		STEM.Biology                                 0.875
		STEM.Chemistry                               0.343
		STEM.Computing                               0.332
		STEM.Earth and environment                   0.54
		STEM.Engineering                             0.627
		STEM.Libraries & Information                 0.349
		STEM.Mathematics                             0.382
		STEM.Medicine & Health                       0.529
		STEM.Physics                                 0.173
		STEM.STEM*                                   0.873
		STEM.Space                                   0.908
		STEM.Technology                              0.417
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'properties': {'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}, 'type': 'object'}

