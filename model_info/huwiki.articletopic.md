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
	counts (n=59344):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15526  -->  14158  1368   792  43026
			'Culture.Biography.Women'                       3586  -->   2518  1068   361  55397
			'Culture.Food and drink'                        1513  -->    989   524   145  57686
			'Culture.Internet culture'                      3266  -->   2775   491   185  55893
			'Culture.Linguistics'                           1643  -->   1179   464    96  57605
			'Culture.Literature'                            5570  -->   4158  1412   488  53286
			'Culture.Media.Books'                           1732  -->   1391   341   100  57512
			'Culture.Media.Entertainment'                   2340  -->   1066  1274   285  56719
			'Culture.Media.Films'                           2888  -->   2395   493   132  56324
			'Culture.Media.Media*'                         14392  -->  12717  1675  1234  43718
			'Culture.Media.Music'                           3309  -->   2801   508   232  55803
			'Culture.Media.Radio'                            330  -->    166   164    20  58994
			'Culture.Media.Software'                        2170  -->   1763   407   261  56913
			'Culture.Media.Television'                      2469  -->   1983   486   143  56732
			'Culture.Media.Video games'                     2087  -->   1939   148    41  57216
			'Culture.Performing arts'                       1491  -->    942   549    99  57754
			'Culture.Philosophy and religion'               4003  -->   2349  1654   397  54944
			'Culture.Sports'                                6230  -->   5569   661   176  52938
			'Culture.Visual arts.Architecture'              2030  -->   1403   627   257  57057
			'Culture.Visual arts.Comics and Anime'          1854  -->   1537   317    89  57401
			'Culture.Visual arts.Fashion'                    806  -->    468   338    53  58485
			'Culture.Visual arts.Visual arts*'              5379  -->   3725  1654   431  53534
			'Geography.Geographical'                        3887  -->   2559  1328   566  54891
			'Geography.Regions.Africa.Africa*'              4049  -->   2746  1303   311  54984
			'Geography.Regions.Africa.Central Africa'        880  -->    558   322    69  58395
			'Geography.Regions.Africa.Eastern Africa'        369  -->    227   142    44  58931
			'Geography.Regions.Africa.Northern Africa'      1503  -->    912   591   110  57731
			'Geography.Regions.Africa.Southern Africa'       695  -->    493   202    56  58593
			'Geography.Regions.Africa.Western Africa'        155  -->     71    84    55  59134
			'Geography.Regions.Americas.Central America'    1381  -->    780   601    96  57867
			'Geography.Regions.Americas.North America'      5628  -->   3645  1983   942  52774
			'Geography.Regions.Americas.South America'      1610  -->   1091   519   115  57619
			'Geography.Regions.Asia.Asia*'                 10749  -->   8595  2154   950  47645
			'Geography.Regions.Asia.Central Asia'           1349  -->    946   403   110  57885
			'Geography.Regions.Asia.East Asia'              3424  -->   2691   733   211  55709
			'Geography.Regions.Asia.North Asia'             1888  -->   1376   512   237  57219
			'Geography.Regions.Asia.South Asia'             1826  -->   1274   552   106  57412
			'Geography.Regions.Asia.Southeast Asia'         1601  -->    955   646   108  57635
			'Geography.Regions.Asia.West Asia'              2495  -->   1792   703   212  56637
			'Geography.Regions.Europe.Eastern Europe'       4951  -->   3636  1315   562  53831
			'Geography.Regions.Europe.Europe*'             16846  -->  13599  3247  2276  40222
			'Geography.Regions.Europe.Northern Europe'      3617  -->   2400  1217   381  55346
			'Geography.Regions.Europe.Southern Europe'      4056  -->   2952  1104   345  54943
			'Geography.Regions.Europe.Western Europe'       5217  -->   3973  1244   552  53575
			'Geography.Regions.Oceania'                     1853  -->   1320   533   117  57374
			'History and Society.Business and economics'    3192  -->   1731  1461   343  55809
			'History and Society.Education'                 1612  -->    722   890   151  57581
			'History and Society.History'                   6143  -->   3862  2281   750  52451
			'History and Society.Military and warfare'      5039  -->   3573  1466   471  53834
			'History and Society.Politics and government'   4453  -->   2653  1800   432  54459
			'History and Society.Society'                   6223  -->   2884  3339   557  52564
			'History and Society.Transportation'            4094  -->   3691   403   163  55087
			'STEM.Biology'                                  4751  -->   4120   631   132  54461
			'STEM.Chemistry'                                1620  -->   1315   305   143  57581
			'STEM.Computing'                                2449  -->   1999   450   285  56610
			'STEM.Earth and environment'                    1882  -->   1321   561   108  57354
			'STEM.Engineering'                              2505  -->   1794   711   193  56646
			'STEM.Libraries & Information'                   510  -->    280   230    46  58788
			'STEM.Mathematics'                               990  -->    786   204    43  58311
			'STEM.Medicine & Health'                        1939  -->   1400   539   167  57238
			'STEM.Physics'                                  1419  -->    957   462   168  57757
			'STEM.STEM*'                                   18523  -->  16660  1863   928  39893
			'STEM.Space'                                    2372  -->   2217   155    41  56931
			'STEM.Technology'                               4874  -->   3679  1195   566  53904
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.262         0.123
		Culture.Biography.Women                         0.06          0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.055         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.243         0.058
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.006         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.067         0.011
		Culture.Sports                                  0.105         0.071
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.031         0.002
		Culture.Visual arts.Fashion                     0.014         0.001
		Culture.Visual arts.Visual arts*                0.091         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.012         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.095         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.181         0.045
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.058         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.042         0.011
		Geography.Regions.Europe.Eastern Europe         0.083         0.013
		Geography.Regions.Europe.Europe*                0.284         0.076
		Geography.Regions.Europe.Northern Europe        0.061         0.031
		Geography.Regions.Europe.Southern Europe        0.068         0.013
		Geography.Regions.Europe.Western Europe         0.088         0.019
		Geography.Regions.Oceania                       0.031         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.027         0.007
		History and Society.History                     0.104         0.011
		History and Society.Military and warfare        0.085         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.105         0.013
		History and Society.Transportation              0.069         0.015
		STEM.Biology                                    0.08          0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.042         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.312         0.069
		STEM.Space                                      0.04          0.006
		STEM.Technology                                 0.082         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.003
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.024
		History and Society.Society                  0.016
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
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
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.976
		History and Society.Society                  0.984
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
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
	recall (micro=0.78, macro=0.712):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.912
		Culture.Biography.Women                      0.702
		Culture.Food and drink                       0.654
		Culture.Internet culture                     0.85
		Culture.Linguistics                          0.718
		Culture.Literature                           0.746
		Culture.Media.Books                          0.803
		Culture.Media.Entertainment                  0.456
		Culture.Media.Films                          0.829
		Culture.Media.Media*                         0.884
		Culture.Media.Music                          0.846
		Culture.Media.Radio                          0.503
		Culture.Media.Software                       0.812
		Culture.Media.Television                     0.803
		Culture.Media.Video games                    0.929
		Culture.Performing arts                      0.632
		Culture.Philosophy and religion              0.587
		Culture.Sports                               0.894
		Culture.Visual arts.Architecture             0.691
		Culture.Visual arts.Comics and Anime         0.829
		Culture.Visual arts.Fashion                  0.581
		Culture.Visual arts.Visual arts*             0.693
		Geography.Geographical                       0.658
		Geography.Regions.Africa.Africa*             0.678
		Geography.Regions.Africa.Central Africa      0.634
		Geography.Regions.Africa.Eastern Africa      0.615
		Geography.Regions.Africa.Northern Africa     0.607
		Geography.Regions.Africa.Southern Africa     0.709
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.565
		Geography.Regions.Americas.North America     0.648
		Geography.Regions.Americas.South America     0.678
		Geography.Regions.Asia.Asia*                 0.8
		Geography.Regions.Asia.Central Asia          0.701
		Geography.Regions.Asia.East Asia             0.786
		Geography.Regions.Asia.North Asia            0.729
		Geography.Regions.Asia.South Asia            0.698
		Geography.Regions.Asia.Southeast Asia        0.597
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.734
		Geography.Regions.Europe.Europe*             0.807
		Geography.Regions.Europe.Northern Europe     0.664
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.762
		Geography.Regions.Oceania                    0.712
		History and Society.Business and economics   0.542
		History and Society.Education                0.448
		History and Society.History                  0.629
		History and Society.Military and warfare     0.709
		History and Society.Politics and government  0.596
		History and Society.Society                  0.463
		History and Society.Transportation           0.902
		STEM.Biology                                 0.867
		STEM.Chemistry                               0.812
		STEM.Computing                               0.816
		STEM.Earth and environment                   0.702
		STEM.Engineering                             0.716
		STEM.Libraries & Information                 0.549
		STEM.Mathematics                             0.794
		STEM.Medicine & Health                       0.722
		STEM.Physics                                 0.674
		STEM.STEM*                                   0.899
		STEM.Space                                   0.935
		STEM.Technology                              0.755
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.986
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.992
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.704, macro=0.555):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.616
		Culture.Food and drink                       0.392
		Culture.Internet culture                     0.475
		Culture.Linguistics                          0.761
		Culture.Literature                           0.564
		Culture.Media.Books                          0.652
		Culture.Media.Entertainment                  0.247
		Culture.Media.Films                          0.79
		Culture.Media.Media*                         0.667
		Culture.Media.Music                          0.833
		Culture.Media.Radio                          0.762
		Culture.Media.Software                       0.191
		Culture.Media.Television                     0.74
		Culture.Media.Video games                    0.773
		Culture.Performing arts                      0.517
		Culture.Philosophy and religion              0.468
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.622
		Culture.Visual arts.Comics and Anime         0.541
		Culture.Visual arts.Fashion                  0.342
		Culture.Visual arts.Visual arts*             0.618
		Geography.Geographical                       0.609
		Geography.Regions.Africa.Africa*             0.487
		Geography.Regions.Africa.Central Africa      0.253
		Geography.Regions.Africa.Eastern Africa      0.273
		Geography.Regions.Africa.Northern Africa     0.282
		Geography.Regions.Africa.Southern Africa     0.466
		Geography.Regions.Africa.Western Africa      0.252
		Geography.Regions.Americas.Central America   0.53
		Geography.Regions.Americas.North America     0.717
		Geography.Regions.Americas.South America     0.683
		Geography.Regions.Asia.Asia*                 0.661
		Geography.Regions.Asia.Central Asia          0.243
		Geography.Regions.Asia.East Asia             0.706
		Geography.Regions.Asia.North Asia            0.14
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.658
		Geography.Regions.Asia.West Asia             0.68
		Geography.Regions.Europe.Eastern Europe      0.48
		Geography.Regions.Europe.Europe*             0.554
		Geography.Regions.Europe.Northern Europe     0.754
		Geography.Regions.Europe.Southern Europe     0.606
		Geography.Regions.Europe.Western Europe      0.593
		Geography.Regions.Oceania                    0.843
		History and Society.Business and economics   0.475
		History and Society.Education                0.559
		History and Society.History                  0.328
		History and Society.Military and warfare     0.538
		History and Society.Politics and government  0.687
		History and Society.Society                  0.361
		History and Society.Transportation           0.824
		STEM.Biology                                 0.926
		STEM.Chemistry                               0.338
		STEM.Computing                               0.305
		STEM.Earth and environment                   0.63
		STEM.Engineering                             0.526
		STEM.Libraries & Information                 0.304
		STEM.Mathematics                             0.31
		STEM.Medicine & Health                       0.615
		STEM.Physics                                 0.165
		STEM.STEM*                                   0.746
		STEM.Space                                   0.887
		STEM.Technology                              0.272
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.988
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.733, macro=0.604):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.894
		Culture.Biography.Women                      0.656
		Culture.Food and drink                       0.49
		Culture.Internet culture                     0.609
		Culture.Linguistics                          0.739
		Culture.Literature                           0.643
		Culture.Media.Books                          0.719
		Culture.Media.Entertainment                  0.32
		Culture.Media.Films                          0.809
		Culture.Media.Media*                         0.76
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.606
		Culture.Media.Software                       0.31
		Culture.Media.Television                     0.77
		Culture.Media.Video games                    0.844
		Culture.Performing arts                      0.568
		Culture.Philosophy and religion              0.521
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.655
		Culture.Visual arts.Comics and Anime         0.655
		Culture.Visual arts.Fashion                  0.43
		Culture.Visual arts.Visual arts*             0.653
		Geography.Geographical                       0.633
		Geography.Regions.Africa.Africa*             0.567
		Geography.Regions.Africa.Central Africa      0.362
		Geography.Regions.Africa.Eastern Africa      0.378
		Geography.Regions.Africa.Northern Africa     0.385
		Geography.Regions.Africa.Southern Africa     0.563
		Geography.Regions.Africa.Western Africa      0.325
		Geography.Regions.Americas.Central America   0.547
		Geography.Regions.Americas.North America     0.681
		Geography.Regions.Americas.South America     0.681
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.361
		Geography.Regions.Asia.East Asia             0.744
		Geography.Regions.Asia.North Asia            0.235
		Geography.Regions.Asia.South Asia            0.768
		Geography.Regions.Asia.Southeast Asia        0.626
		Geography.Regions.Asia.West Asia             0.698
		Geography.Regions.Europe.Eastern Europe      0.581
		Geography.Regions.Europe.Europe*             0.657
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.662
		Geography.Regions.Europe.Western Europe      0.667
		Geography.Regions.Oceania                    0.772
		History and Society.Business and economics   0.506
		History and Society.Education                0.497
		History and Society.History                  0.431
		History and Society.Military and warfare     0.612
		History and Society.Politics and government  0.638
		History and Society.Society                  0.406
		History and Society.Transportation           0.861
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.478
		STEM.Computing                               0.444
		STEM.Earth and environment                   0.664
		STEM.Engineering                             0.607
		STEM.Libraries & Information                 0.391
		STEM.Mathematics                             0.446
		STEM.Medicine & Health                       0.664
		STEM.Physics                                 0.265
		STEM.STEM*                                   0.816
		STEM.Space                                   0.91
		STEM.Technology                              0.4
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.981
		History and Society.Society                  0.983
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.054
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.014
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.008
		History and Society.Society                  0.01
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.974
		Culture.Literature                           0.976
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.964
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.937
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.958
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.971
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.972
		Geography.Regions.Africa.Central Africa      0.982
		Geography.Regions.Africa.Eastern Africa      0.956
		Geography.Regions.Africa.Northern Africa     0.974
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.871
		Geography.Regions.Americas.Central America   0.968
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.975
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.971
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.956
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.958
		History and Society.Education                0.96
		History and Society.History                  0.961
		History and Society.Military and warfare     0.973
		History and Society.Politics and government  0.955
		History and Society.Society                  0.929
		History and Society.Transportation           0.986
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.985
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.965
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.978
		STEM.Space                                   0.995
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.781, macro=0.607):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.951
		Culture.Biography.Women                      0.661
		Culture.Food and drink                       0.431
		Culture.Internet culture                     0.721
		Culture.Linguistics                          0.752
		Culture.Literature                           0.707
		Culture.Media.Books                          0.782
		Culture.Media.Entertainment                  0.24
		Culture.Media.Films                          0.852
		Culture.Media.Media*                         0.867
		Culture.Media.Music                          0.863
		Culture.Media.Radio                          0.41
		Culture.Media.Software                       0.332
		Culture.Media.Television                     0.811
		Culture.Media.Video games                    0.88
		Culture.Performing arts                      0.58
		Culture.Philosophy and religion              0.497
		Culture.Sports                               0.957
		Culture.Visual arts.Architecture             0.667
		Culture.Visual arts.Comics and Anime         0.658
		Culture.Visual arts.Fashion                  0.364
		Culture.Visual arts.Visual arts*             0.684
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.541
		Geography.Regions.Africa.Central Africa      0.271
		Geography.Regions.Africa.Eastern Africa      0.18
		Geography.Regions.Africa.Northern Africa     0.31
		Geography.Regions.Africa.Southern Africa     0.372
		Geography.Regions.Africa.Western Africa      0.131
		Geography.Regions.Americas.Central America   0.465
		Geography.Regions.Americas.North America     0.755
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.788
		Geography.Regions.Asia.Central Asia          0.312
		Geography.Regions.Asia.East Asia             0.793
		Geography.Regions.Asia.North Asia            0.213
		Geography.Regions.Asia.South Asia            0.813
		Geography.Regions.Asia.Southeast Asia        0.58
		Geography.Regions.Asia.West Asia             0.708
		Geography.Regions.Europe.Eastern Europe      0.602
		Geography.Regions.Europe.Europe*             0.748
		Geography.Regions.Europe.Northern Europe     0.761
		Geography.Regions.Europe.Southern Europe     0.712
		Geography.Regions.Europe.Western Europe      0.737
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.476
		History and Society.Education                0.445
		History and Society.History                  0.473
		History and Society.Military and warfare     0.661
		History and Society.Politics and government  0.674
		History and Society.Society                  0.376
		History and Society.Transportation           0.911
		STEM.Biology                                 0.931
		STEM.Chemistry                               0.561
		STEM.Computing                               0.524
		STEM.Earth and environment                   0.643
		STEM.Engineering                             0.618
		STEM.Libraries & Information                 0.195
		STEM.Mathematics                             0.501
		STEM.Medicine & Health                       0.671
		STEM.Physics                                 0.191
		STEM.STEM*                                   0.897
		STEM.Space                                   0.964
		STEM.Technology                              0.537
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

