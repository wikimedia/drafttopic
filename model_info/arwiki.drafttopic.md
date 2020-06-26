Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'min_weight_fraction_leaf': 0.0, 'ccp_alpha': 0.0, 'learning_rate': 0.1, 'loss': 'deviance', 'subsample': 1.0, 'label_weights': {}, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'center': False, 'population_rates': None, 'max_leaf_nodes': None, 'min_impurity_split': None, 'presort': 'deprecated', 'scale': False, 'validation_fraction': 0.1, 'verbose': 0, 'init': None, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'max_depth': 5, 'max_features': 'log2', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'random_state': None, 'n_estimators': 150, 'warm_start': False, 'tol': 0.0001}
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
	counts (n=62795):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 26992  -->  25511  1481  1004  34799
			'Culture.Biography.Women'                       6281  -->   4693  1588   969  55545
			'Culture.Food and drink'                        1344  -->    720   624   144  61307
			'Culture.Internet culture'                      3343  -->   2492   851   253  59199
			'Culture.Linguistics'                           1383  -->    740   643   110  61302
			'Culture.Literature'                            5742  -->   3848  1894   612  56441
			'Culture.Media.Books'                           1533  -->   1013   520   135  61127
			'Culture.Media.Entertainment'                   2093  -->    799  1294   226  60476
			'Culture.Media.Films'                           2108  -->   1542   566   116  60571
			'Culture.Media.Media*'                         13935  -->  11057  2878  1681  47179
			'Culture.Media.Music'                           2781  -->   1938   843   348  59666
			'Culture.Media.Radio'                           1131  -->    427   704   103  61561
			'Culture.Media.Software'                        2065  -->   1375   690   349  60381
			'Culture.Media.Television'                      2239  -->   1124  1115   206  60350
			'Culture.Media.Video games'                     2171  -->   1823   348    57  60567
			'Culture.Performing arts'                       1478  -->    595   883   135  61182
			'Culture.Philosophy and religion'               3372  -->   1320  2052   332  59091
			'Culture.Sports'                                8592  -->   7733   859   434  53769
			'Culture.Visual arts.Architecture'              1842  -->   1132   710   190  60763
			'Culture.Visual arts.Comics and Anime'          1830  -->   1260   570   146  60819
			'Culture.Visual arts.Fashion'                   1307  -->    805   502   121  61367
			'Culture.Visual arts.Visual arts*'              5819  -->   3757  2062   540  56436
			'Geography.Geographical'                        3599  -->   2477  1122   353  58843
			'Geography.Regions.Africa.Africa*'              6398  -->   4683  1715   526  55871
			'Geography.Regions.Africa.Central Africa'       1108  -->    692   416    63  61624
			'Geography.Regions.Africa.Eastern Africa'        959  -->    556   403    61  61775
			'Geography.Regions.Africa.Northern Africa'      2066  -->   1316   750   258  60471
			'Geography.Regions.Africa.Southern Africa'      1186  -->    837   349    75  61534
			'Geography.Regions.Africa.Western Africa'        752  -->    500   252    53  61990
			'Geography.Regions.Americas.Central America'    1364  -->    735   629    81  61350
			'Geography.Regions.Americas.North America'      8316  -->   5074  3242  2137  52342
			'Geography.Regions.Americas.South America'      1694  -->   1118   576   117  60984
			'Geography.Regions.Asia.Asia*'                 11871  -->   9229  2642  1057  49867
			'Geography.Regions.Asia.Central Asia'           1163  -->    744   419    74  61558
			'Geography.Regions.Asia.East Asia'              2887  -->   1911   976   259  59649
			'Geography.Regions.Asia.North Asia'             1493  -->    917   576   229  61073
			'Geography.Regions.Asia.South Asia'             1919  -->   1304   615    87  60789
			'Geography.Regions.Asia.Southeast Asia'         1539  -->    982   557    74  61182
			'Geography.Regions.Asia.West Asia'              4041  -->   3038  1003   322  58432
			'Geography.Regions.Europe.Eastern Europe'       2828  -->   1862   966   297  59670
			'Geography.Regions.Europe.Europe*'             13010  -->   9559  3451  2073  47712
			'Geography.Regions.Europe.Northern Europe'      4018  -->   2329  1689   636  58141
			'Geography.Regions.Europe.Southern Europe'      2834  -->   1788  1046   297  59664
			'Geography.Regions.Europe.Western Europe'       4060  -->   2747  1313   523  58212
			'Geography.Regions.Oceania'                     2280  -->   1713   567    82  60433
			'History and Society.Business and economics'    3538  -->   1711  1827   451  58806
			'History and Society.Education'                 2034  -->    710  1324   142  60619
			'History and Society.History'                   4654  -->   1734  2920   674  57467
			'History and Society.Military and warfare'      4697  -->   2906  1791   514  57584
			'History and Society.Politics and government'   5419  -->   2930  2489   662  56714
			'History and Society.Society'                   5993  -->   2092  3901   559  56243
			'History and Society.Transportation'            3223  -->   2599   624   191  59381
			'STEM.Biology'                                  2978  -->   2148   830   235  59582
			'STEM.Chemistry'                                1476  -->    974   502   167  61152
			'STEM.Computing'                                2392  -->   1602   790   381  60022
			'STEM.Earth and environment'                    1682  -->    848   834   165  60948
			'STEM.Engineering'                              2828  -->   1841   987   248  59719
			'STEM.Libraries & Information'                  1175  -->    735   440    93  61527
			'STEM.Mathematics'                              1163  -->    690   473    84  61548
			'STEM.Medicine & Health'                        2224  -->   1375   849   238  60333
			'STEM.Physics'                                  1432  -->    817   615   182  61181
			'STEM.STEM*'                                   17757  -->  14997  2760  1350  43688
			'STEM.Space'                                    1742  -->   1420   322    79  60974
			'STEM.Technology'                               4421  -->   2721  1700   662  57712
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.43          0.123
		Culture.Biography.Women                         0.1           0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.034         0.011
		Culture.Media.Media*                            0.222         0.058
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.033         0.001
		Culture.Media.Television                        0.036         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.137         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.029         0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0
		Geography.Regions.Africa.Northern Africa        0.033         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.132         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.189         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.064         0.011
		Geography.Regions.Europe.Eastern Europe         0.045         0.013
		Geography.Regions.Europe.Europe*                0.207         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.065         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.075         0.014
		History and Society.Politics and government     0.086         0.028
		History and Society.Society                     0.095         0.013
		History and Society.Transportation              0.051         0.015
		STEM.Biology                                    0.047         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.038         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.283         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.141
		Culture.Biography.Women                      0.028
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.072
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.076
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.005
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.014
		History and Society.Transportation           0.015
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.859
		Culture.Biography.Women                      0.972
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.924
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.986
		History and Society.Transportation           0.985
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.725, macro=0.636):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.747
		Culture.Food and drink                       0.536
		Culture.Internet culture                     0.745
		Culture.Linguistics                          0.535
		Culture.Literature                           0.67
		Culture.Media.Books                          0.661
		Culture.Media.Entertainment                  0.382
		Culture.Media.Films                          0.731
		Culture.Media.Media*                         0.793
		Culture.Media.Music                          0.697
		Culture.Media.Radio                          0.378
		Culture.Media.Software                       0.666
		Culture.Media.Television                     0.502
		Culture.Media.Video games                    0.84
		Culture.Performing arts                      0.403
		Culture.Philosophy and religion              0.391
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.615
		Culture.Visual arts.Comics and Anime         0.689
		Culture.Visual arts.Fashion                  0.616
		Culture.Visual arts.Visual arts*             0.646
		Geography.Geographical                       0.688
		Geography.Regions.Africa.Africa*             0.732
		Geography.Regions.Africa.Central Africa      0.625
		Geography.Regions.Africa.Eastern Africa      0.58
		Geography.Regions.Africa.Northern Africa     0.637
		Geography.Regions.Africa.Southern Africa     0.706
		Geography.Regions.Africa.Western Africa      0.665
		Geography.Regions.Americas.Central America   0.539
		Geography.Regions.Americas.North America     0.61
		Geography.Regions.Americas.South America     0.66
		Geography.Regions.Asia.Asia*                 0.777
		Geography.Regions.Asia.Central Asia          0.64
		Geography.Regions.Asia.East Asia             0.662
		Geography.Regions.Asia.North Asia            0.614
		Geography.Regions.Asia.South Asia            0.68
		Geography.Regions.Asia.Southeast Asia        0.638
		Geography.Regions.Asia.West Asia             0.752
		Geography.Regions.Europe.Eastern Europe      0.658
		Geography.Regions.Europe.Europe*             0.735
		Geography.Regions.Europe.Northern Europe     0.58
		Geography.Regions.Europe.Southern Europe     0.631
		Geography.Regions.Europe.Western Europe      0.677
		Geography.Regions.Oceania                    0.751
		History and Society.Business and economics   0.484
		History and Society.Education                0.349
		History and Society.History                  0.373
		History and Society.Military and warfare     0.619
		History and Society.Politics and government  0.541
		History and Society.Society                  0.349
		History and Society.Transportation           0.806
		STEM.Biology                                 0.721
		STEM.Chemistry                               0.66
		STEM.Computing                               0.67
		STEM.Earth and environment                   0.504
		STEM.Engineering                             0.651
		STEM.Libraries & Information                 0.626
		STEM.Mathematics                             0.593
		STEM.Medicine & Health                       0.618
		STEM.Physics                                 0.571
		STEM.STEM*                                   0.845
		STEM.Space                                   0.815
		STEM.Technology                              0.615
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.988
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.65, macro=0.498):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.826
		Culture.Biography.Women                      0.392
		Culture.Food and drink                       0.361
		Culture.Internet culture                     0.381
		Culture.Linguistics                          0.688
		Culture.Literature                           0.496
		Culture.Media.Books                          0.548
		Culture.Media.Entertainment                  0.269
		Culture.Media.Films                          0.803
		Culture.Media.Media*                         0.589
		Culture.Media.Music                          0.746
		Culture.Media.Radio                          0.328
		Culture.Media.Software                       0.134
		Culture.Media.Television                     0.567
		Culture.Media.Video games                    0.7
		Culture.Performing arts                      0.346
		Culture.Philosophy and religion              0.43
		Culture.Sports                               0.896
		Culture.Visual arts.Architecture             0.678
		Culture.Visual arts.Comics and Anime         0.388
		Culture.Visual arts.Fashion                  0.202
		Culture.Visual arts.Visual arts*             0.559
		Geography.Geographical                       0.736
		Geography.Regions.Africa.Africa*             0.381
		Geography.Regions.Africa.Central Africa      0.279
		Geography.Regions.Africa.Eastern Africa      0.211
		Geography.Regions.Africa.Northern Africa     0.156
		Geography.Regions.Africa.Southern Africa     0.405
		Geography.Regions.Africa.Western Africa      0.347
		Geography.Regions.Americas.Central America   0.575
		Geography.Regions.Americas.North America     0.517
		Geography.Regions.Americas.South America     0.686
		Geography.Regions.Asia.Asia*                 0.641
		Geography.Regions.Asia.Central Asia          0.316
		Geography.Regions.Asia.East Asia             0.639
		Geography.Regions.Asia.North Asia            0.132
		Geography.Regions.Asia.South Asia            0.88
		Geography.Regions.Asia.Southeast Asia        0.761
		Geography.Regions.Asia.West Asia             0.602
		Geography.Regions.Europe.Eastern Europe      0.633
		Geography.Regions.Europe.Europe*             0.593
		Geography.Regions.Europe.Northern Europe     0.628
		Geography.Regions.Europe.Southern Europe     0.627
		Geography.Regions.Europe.Western Europe      0.598
		Geography.Regions.Oceania                    0.895
		History and Society.Business and economics   0.393
		History and Society.Education                0.525
		History and Society.History                  0.26
		History and Society.Military and warfare     0.499
		History and Society.Politics and government  0.576
		History and Society.Society                  0.312
		History and Society.Transportation           0.794
		STEM.Biology                                 0.865
		STEM.Chemistry                               0.274
		STEM.Computing                               0.223
		STEM.Earth and environment                   0.46
		STEM.Engineering                             0.453
		STEM.Libraries & Information                 0.205
		STEM.Mathematics                             0.154
		STEM.Medicine & Health                       0.503
		STEM.Physics                                 0.14
		STEM.STEM*                                   0.677
		STEM.Space                                   0.792
		STEM.Technology                              0.219
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.992
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.987
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.679, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.881
		Culture.Biography.Women                      0.514
		Culture.Food and drink                       0.431
		Culture.Internet culture                     0.504
		Culture.Linguistics                          0.602
		Culture.Literature                           0.57
		Culture.Media.Books                          0.599
		Culture.Media.Entertainment                  0.316
		Culture.Media.Films                          0.765
		Culture.Media.Media*                         0.676
		Culture.Media.Music                          0.721
		Culture.Media.Radio                          0.351
		Culture.Media.Software                       0.222
		Culture.Media.Television                     0.533
		Culture.Media.Video games                    0.764
		Culture.Performing arts                      0.372
		Culture.Philosophy and religion              0.41
		Culture.Sports                               0.898
		Culture.Visual arts.Architecture             0.645
		Culture.Visual arts.Comics and Anime         0.496
		Culture.Visual arts.Fashion                  0.304
		Culture.Visual arts.Visual arts*             0.599
		Geography.Geographical                       0.711
		Geography.Regions.Africa.Africa*             0.502
		Geography.Regions.Africa.Central Africa      0.385
		Geography.Regions.Africa.Eastern Africa      0.309
		Geography.Regions.Africa.Northern Africa     0.25
		Geography.Regions.Africa.Southern Africa     0.515
		Geography.Regions.Africa.Western Africa      0.456
		Geography.Regions.Americas.Central America   0.556
		Geography.Regions.Americas.North America     0.559
		Geography.Regions.Americas.South America     0.673
		Geography.Regions.Asia.Asia*                 0.703
		Geography.Regions.Asia.Central Asia          0.423
		Geography.Regions.Asia.East Asia             0.65
		Geography.Regions.Asia.North Asia            0.217
		Geography.Regions.Asia.South Asia            0.767
		Geography.Regions.Asia.Southeast Asia        0.694
		Geography.Regions.Asia.West Asia             0.669
		Geography.Regions.Europe.Eastern Europe      0.646
		Geography.Regions.Europe.Europe*             0.656
		Geography.Regions.Europe.Northern Europe     0.603
		Geography.Regions.Europe.Southern Europe     0.629
		Geography.Regions.Europe.Western Europe      0.635
		Geography.Regions.Oceania                    0.817
		History and Society.Business and economics   0.434
		History and Society.Education                0.419
		History and Society.History                  0.307
		History and Society.Military and warfare     0.553
		History and Society.Politics and government  0.558
		History and Society.Society                  0.329
		History and Society.Transportation           0.8
		STEM.Biology                                 0.786
		STEM.Chemistry                               0.388
		STEM.Computing                               0.334
		STEM.Earth and environment                   0.481
		STEM.Engineering                             0.534
		STEM.Libraries & Information                 0.309
		STEM.Mathematics                             0.244
		STEM.Medicine & Health                       0.555
		STEM.Physics                                 0.225
		STEM.STEM*                                   0.751
		STEM.Space                                   0.804
		STEM.Technology                              0.323
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
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
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.984
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.956
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.994
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.028
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.008
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.039
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.021
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.042
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.012
		History and Society.Society                  0.01
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.962, macro=0.963):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.961
		Culture.Internet culture                     0.978
		Culture.Linguistics                          0.95
		Culture.Literature                           0.962
		Culture.Media.Books                          0.971
		Culture.Media.Entertainment                  0.949
		Culture.Media.Films                          0.976
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.958
		Culture.Media.Software                       0.979
		Culture.Media.Television                     0.963
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.956
		Culture.Philosophy and religion              0.915
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.97
		Culture.Visual arts.Comics and Anime         0.975
		Culture.Visual arts.Fashion                  0.969
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.967
		Geography.Regions.Africa.Central Africa      0.974
		Geography.Regions.Africa.Eastern Africa      0.965
		Geography.Regions.Africa.Northern Africa     0.969
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.974
		Geography.Regions.Americas.Central America   0.952
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.971
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.971
		Geography.Regions.Asia.East Asia             0.969
		Geography.Regions.Asia.North Asia            0.975
		Geography.Regions.Asia.South Asia            0.965
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.968
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.955
		Geography.Regions.Europe.Southern Europe     0.963
		Geography.Regions.Europe.Western Europe      0.968
		Geography.Regions.Oceania                    0.968
		History and Society.Business and economics   0.941
		History and Society.Education                0.933
		History and Society.History                  0.924
		History and Society.Military and warfare     0.957
		History and Society.Politics and government  0.934
		History and Society.Society                  0.886
		History and Society.Transportation           0.976
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.982
		STEM.Computing                               0.979
		STEM.Earth and environment                   0.954
		STEM.Engineering                             0.966
		STEM.Libraries & Information                 0.965
		STEM.Mathematics                             0.965
		STEM.Medicine & Health                       0.963
		STEM.Physics                                 0.976
		STEM.STEM*                                   0.967
		STEM.Space                                   0.985
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.705, macro=0.517):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.468
		Culture.Food and drink                       0.36
		Culture.Internet culture                     0.616
		Culture.Linguistics                          0.568
		Culture.Literature                           0.614
		Culture.Media.Books                          0.544
		Culture.Media.Entertainment                  0.25
		Culture.Media.Films                          0.787
		Culture.Media.Media*                         0.776
		Culture.Media.Music                          0.724
		Culture.Media.Radio                          0.218
		Culture.Media.Software                       0.177
		Culture.Media.Television                     0.538
		Culture.Media.Video games                    0.822
		Culture.Performing arts                      0.293
		Culture.Philosophy and religion              0.352
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.634
		Culture.Visual arts.Comics and Anime         0.451
		Culture.Visual arts.Fashion                  0.245
		Culture.Visual arts.Visual arts*             0.6
		Geography.Geographical                       0.735
		Geography.Regions.Africa.Africa*             0.466
		Geography.Regions.Africa.Central Africa      0.311
		Geography.Regions.Africa.Eastern Africa      0.175
		Geography.Regions.Africa.Northern Africa     0.167
		Geography.Regions.Africa.Southern Africa     0.388
		Geography.Regions.Africa.Western Africa      0.367
		Geography.Regions.Americas.Central America   0.512
		Geography.Regions.Americas.North America     0.569
		Geography.Regions.Americas.South America     0.588
		Geography.Regions.Asia.Asia*                 0.768
		Geography.Regions.Asia.Central Asia          0.413
		Geography.Regions.Asia.East Asia             0.628
		Geography.Regions.Asia.North Asia            0.149
		Geography.Regions.Asia.South Asia            0.793
		Geography.Regions.Asia.Southeast Asia        0.694
		Geography.Regions.Asia.West Asia             0.68
		Geography.Regions.Europe.Eastern Europe      0.66
		Geography.Regions.Europe.Europe*             0.7
		Geography.Regions.Europe.Northern Europe     0.633
		Geography.Regions.Europe.Southern Europe     0.608
		Geography.Regions.Europe.Western Europe      0.636
		Geography.Regions.Oceania                    0.837
		History and Society.Business and economics   0.353
		History and Society.Education                0.358
		History and Society.History                  0.231
		History and Society.Military and warfare     0.568
		History and Society.Politics and government  0.572
		History and Society.Society                  0.286
		History and Society.Transportation           0.831
		STEM.Biology                                 0.815
		STEM.Chemistry                               0.388
		STEM.Computing                               0.264
		STEM.Earth and environment                   0.416
		STEM.Engineering                             0.502
		STEM.Libraries & Information                 0.195
		STEM.Mathematics                             0.227
		STEM.Medicine & Health                       0.531
		STEM.Physics                                 0.151
		STEM.STEM*                                   0.855
		STEM.Space                                   0.855
		STEM.Technology                              0.32
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Literature': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}}}}}

