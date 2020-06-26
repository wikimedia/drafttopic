Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'scale': False, 'center': False, 'random_state': None, 'label_weights': {}, 'validation_fraction': 0.1, 'max_depth': 5, 'multilabel': True, 'warm_start': False, 'init': None, 'max_leaf_nodes': None, 'n_estimators': 150, 'loss': 'deviance', 'population_rates': None, 'subsample': 1.0, 'max_features': 'log2', 'min_samples_split': 2, 'criterion': 'friedman_mse', 'tol': 0.0001, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_leaf': 1, 'learning_rate': 0.1, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'presort': 'auto', 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'n_iter_no_change': None}
	Environment:
	 - revscoring_version: '2.6.9'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=58681):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15665  -->  13743  1922   956  42060
			'Culture.Biography.Women'                       4273  -->   2747  1526   641  53767
			'Culture.Food and drink'                        1677  -->   1162   515   112  56892
			'Culture.Internet culture'                      3311  -->   2374   937   244  55126
			'Culture.Linguistics'                           1543  -->    849   694   106  57032
			'Culture.Literature'                            5625  -->   3737  1888   515  52541
			'Culture.Media.Books'                           1505  -->   1006   499   134  57042
			'Culture.Media.Entertainment'                   2201  -->    888  1313   222  56258
			'Culture.Media.Films'                           2885  -->   2314   571   120  55676
			'Culture.Media.Media*'                         14506  -->  11814  2692  1655  42520
			'Culture.Media.Music'                           3057  -->   2273   784   319  55305
			'Culture.Media.Radio'                            612  -->    311   301    50  58019
			'Culture.Media.Software'                        2181  -->   1494   687   396  56104
			'Culture.Media.Television'                      2464  -->   1511   953   194  56023
			'Culture.Media.Video games'                     2266  -->   1851   415   107  56308
			'Culture.Performing arts'                       1468  -->    684   784   150  57063
			'Culture.Philosophy and religion'               3668  -->   1612  2056   335  54678
			'Culture.Sports'                                5214  -->   4380   834   216  53251
			'Culture.Visual arts.Architecture'              1991  -->   1167   824   199  56491
			'Culture.Visual arts.Comics and Anime'          2393  -->   1896   497   183  56105
			'Culture.Visual arts.Fashion'                   1307  -->    812   495   108  57266
			'Culture.Visual arts.Visual arts*'              6139  -->   3909  2230   571  51971
			'Geography.Geographical'                        3831  -->   2274  1557   519  54331
			'Geography.Regions.Africa.Africa*'              4148  -->   2849  1299   278  54255
			'Geography.Regions.Africa.Central Africa'        800  -->    543   257    54  57827
			'Geography.Regions.Africa.Eastern Africa'        473  -->    335   138    48  58160
			'Geography.Regions.Africa.Northern Africa'      1428  -->    950   478   109  57144
			'Geography.Regions.Africa.Southern Africa'       652  -->    419   233    75  57954
			'Geography.Regions.Africa.Western Africa'        275  -->    184    91    41  58365
			'Geography.Regions.Americas.Central America'    1324  -->    788   536    52  57305
			'Geography.Regions.Americas.North America'      6325  -->   3986  2339  1206  51150
			'Geography.Regions.Americas.South America'      1535  -->   1020   515   119  57027
			'Geography.Regions.Asia.Asia*'                 15534  -->  12340  3194  1666  41481
			'Geography.Regions.Asia.Central Asia'           1228  -->    749   479   117  57336
			'Geography.Regions.Asia.East Asia'              7401  -->   5638  1763   894  50386
			'Geography.Regions.Asia.North Asia'             2927  -->   1990   937   240  55514
			'Geography.Regions.Asia.South Asia'             1679  -->   1149   530    90  56912
			'Geography.Regions.Asia.Southeast Asia'         1858  -->   1217   641   104  56719
			'Geography.Regions.Asia.West Asia'              2156  -->   1441   715   191  56334
			'Geography.Regions.Europe.Eastern Europe'       4038  -->   2812  1226   278  54365
			'Geography.Regions.Europe.Europe*'             13661  -->  10639  3022  1697  43323
			'Geography.Regions.Europe.Northern Europe'      3667  -->   2478  1189   406  54608
			'Geography.Regions.Europe.Southern Europe'      3110  -->   2115   995   321  55250
			'Geography.Regions.Europe.Western Europe'       3816  -->   2668  1148   417  54448
			'Geography.Regions.Oceania'                     1667  -->   1067   600    83  56931
			'History and Society.Business and economics'    3696  -->   1733  1963   386  54599
			'History and Society.Education'                 1894  -->   1008   886   146  56641
			'History and Society.History'                   4993  -->   2463  2530   637  53051
			'History and Society.Military and warfare'      4316  -->   2405  1911   398  53967
			'History and Society.Politics and government'   3846  -->   1624  2222   443  54392
			'History and Society.Society'                   4337  -->    918  3419   255  54089
			'History and Society.Transportation'            3696  -->   3006   690   197  54788
			'STEM.Biology'                                  3354  -->   2456   898   181  55146
			'STEM.Chemistry'                                1373  -->    904   469   109  57199
			'STEM.Computing'                                2678  -->   1899   779   446  55557
			'STEM.Earth and environment'                    1770  -->    974   796   162  56749
			'STEM.Engineering'                              2524  -->   1615   909   183  55974
			'STEM.Libraries & Information'                   725  -->    457   268    47  57909
			'STEM.Mathematics'                              1109  -->    729   380   100  57472
			'STEM.Medicine & Health'                        1901  -->    995   906   181  56599
			'STEM.Physics'                                  1425  -->    765   660   208  57048
			'STEM.STEM*'                                   17124  -->  14411  2713  1296  40261
			'STEM.Space'                                    1657  -->   1375   282    66  56958
			'STEM.Technology'                               4370  -->   2700  1670   732  53579
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.267         0.121
		Culture.Biography.Women                         0.073         0.015
		Culture.Food and drink                          0.029         0.003
		Culture.Internet culture                        0.056         0.004
		Culture.Linguistics                             0.026         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.049         0.012
		Culture.Media.Media*                            0.247         0.055
		Culture.Media.Music                             0.052         0.021
		Culture.Media.Radio                             0.01          0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.039         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.063         0.01
		Culture.Sports                                  0.089         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.041         0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.071         0.009
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.108         0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.265         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.126         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.069         0.018
		Geography.Regions.Europe.Europe*                0.233         0.082
		Geography.Regions.Europe.Northern Europe        0.062         0.029
		Geography.Regions.Europe.Southern Europe        0.053         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.085         0.011
		History and Society.Military and warfare        0.074         0.015
		History and Society.Politics and government     0.066         0.016
		History and Society.Society                     0.074         0.008
		History and Society.Transportation              0.063         0.016
		STEM.Biology                                    0.057         0.035
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.043         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.292         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.074         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.021
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.062
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.079
		Geography.Regions.Asia.Central Asia          0.003
		Geography.Regions.Asia.East Asia             0.027
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.098
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.017
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.015
		History and Society.Society                  0.006
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.921
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.973
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.902
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.985
		History and Society.Society                  0.994
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.723, macro=0.649):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.643
		Culture.Food and drink                       0.693
		Culture.Internet culture                     0.717
		Culture.Linguistics                          0.55
		Culture.Literature                           0.664
		Culture.Media.Books                          0.668
		Culture.Media.Entertainment                  0.403
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.814
		Culture.Media.Music                          0.744
		Culture.Media.Radio                          0.508
		Culture.Media.Software                       0.685
		Culture.Media.Television                     0.613
		Culture.Media.Video games                    0.817
		Culture.Performing arts                      0.466
		Culture.Philosophy and religion              0.439
		Culture.Sports                               0.84
		Culture.Visual arts.Architecture             0.586
		Culture.Visual arts.Comics and Anime         0.792
		Culture.Visual arts.Fashion                  0.621
		Culture.Visual arts.Visual arts*             0.637
		Geography.Geographical                       0.594
		Geography.Regions.Africa.Africa*             0.687
		Geography.Regions.Africa.Central Africa      0.679
		Geography.Regions.Africa.Eastern Africa      0.708
		Geography.Regions.Africa.Northern Africa     0.665
		Geography.Regions.Africa.Southern Africa     0.643
		Geography.Regions.Africa.Western Africa      0.669
		Geography.Regions.Americas.Central America   0.595
		Geography.Regions.Americas.North America     0.63
		Geography.Regions.Americas.South America     0.664
		Geography.Regions.Asia.Asia*                 0.794
		Geography.Regions.Asia.Central Asia          0.61
		Geography.Regions.Asia.East Asia             0.762
		Geography.Regions.Asia.North Asia            0.68
		Geography.Regions.Asia.South Asia            0.684
		Geography.Regions.Asia.Southeast Asia        0.655
		Geography.Regions.Asia.West Asia             0.668
		Geography.Regions.Europe.Eastern Europe      0.696
		Geography.Regions.Europe.Europe*             0.779
		Geography.Regions.Europe.Northern Europe     0.676
		Geography.Regions.Europe.Southern Europe     0.68
		Geography.Regions.Europe.Western Europe      0.699
		Geography.Regions.Oceania                    0.64
		History and Society.Business and economics   0.469
		History and Society.Education                0.532
		History and Society.History                  0.493
		History and Society.Military and warfare     0.557
		History and Society.Politics and government  0.422
		History and Society.Society                  0.212
		History and Society.Transportation           0.813
		STEM.Biology                                 0.732
		STEM.Chemistry                               0.658
		STEM.Computing                               0.709
		STEM.Earth and environment                   0.55
		STEM.Engineering                             0.64
		STEM.Libraries & Information                 0.63
		STEM.Mathematics                             0.657
		STEM.Medicine & Health                       0.523
		STEM.Physics                                 0.537
		STEM.STEM*                                   0.842
		STEM.Space                                   0.83
		STEM.Technology                              0.618
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.661, macro=0.521):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.845
		Culture.Biography.Women                      0.456
		Culture.Food and drink                       0.477
		Culture.Internet culture                     0.381
		Culture.Linguistics                          0.708
		Culture.Literature                           0.51
		Culture.Media.Books                          0.555
		Culture.Media.Entertainment                  0.291
		Culture.Media.Films                          0.815
		Culture.Media.Media*                         0.56
		Culture.Media.Music                          0.737
		Culture.Media.Radio                          0.581
		Culture.Media.Software                       0.114
		Culture.Media.Television                     0.617
		Culture.Media.Video games                    0.559
		Culture.Performing arts                      0.355
		Culture.Philosophy and religion              0.433
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.648
		Culture.Visual arts.Comics and Anime         0.371
		Culture.Visual arts.Fashion                  0.23
		Culture.Visual arts.Visual arts*             0.521
		Geography.Geographical                       0.578
		Geography.Regions.Africa.Africa*             0.538
		Geography.Regions.Africa.Central Africa      0.341
		Geography.Regions.Africa.Eastern Africa      0.304
		Geography.Regions.Africa.Northern Africa     0.323
		Geography.Regions.Africa.Southern Africa     0.397
		Geography.Regions.Africa.Western Africa      0.418
		Geography.Regions.Americas.Central America   0.697
		Geography.Regions.Americas.North America     0.65
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.535
		Geography.Regions.Asia.Central Asia          0.194
		Geography.Regions.Asia.East Asia             0.352
		Geography.Regions.Asia.North Asia            0.473
		Geography.Regions.Asia.South Asia            0.88
		Geography.Regions.Asia.Southeast Asia        0.694
		Geography.Regions.Asia.West Asia             0.703
		Geography.Regions.Europe.Eastern Europe      0.72
		Geography.Regions.Europe.Europe*             0.647
		Geography.Regions.Europe.Northern Europe     0.734
		Geography.Regions.Europe.Southern Europe     0.625
		Geography.Regions.Europe.Western Europe      0.66
		Geography.Regions.Oceania                    0.881
		History and Society.Business and economics   0.398
		History and Society.Education                0.625
		History and Society.History                  0.316
		History and Society.Military and warfare     0.544
		History and Society.Politics and government  0.467
		History and Society.Society                  0.275
		History and Society.Transportation           0.791
		STEM.Biology                                 0.89
		STEM.Chemistry                               0.372
		STEM.Computing                               0.203
		STEM.Earth and environment                   0.481
		STEM.Engineering                             0.534
		STEM.Libraries & Information                 0.35
		STEM.Mathematics                             0.15
		STEM.Medicine & Health                       0.518
		STEM.Physics                                 0.123
		STEM.STEM*                                   0.655
		STEM.Space                                   0.756
		STEM.Technology                              0.193
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.996
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.989
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.682, macro=0.558):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.533
		Culture.Food and drink                       0.565
		Culture.Internet culture                     0.497
		Culture.Linguistics                          0.619
		Culture.Literature                           0.577
		Culture.Media.Books                          0.607
		Culture.Media.Entertainment                  0.338
		Culture.Media.Films                          0.808
		Culture.Media.Media*                         0.664
		Culture.Media.Music                          0.74
		Culture.Media.Radio                          0.542
		Culture.Media.Software                       0.196
		Culture.Media.Television                     0.615
		Culture.Media.Video games                    0.664
		Culture.Performing arts                      0.403
		Culture.Philosophy and religion              0.436
		Culture.Sports                               0.883
		Culture.Visual arts.Architecture             0.615
		Culture.Visual arts.Comics and Anime         0.505
		Culture.Visual arts.Fashion                  0.336
		Culture.Visual arts.Visual arts*             0.573
		Geography.Geographical                       0.586
		Geography.Regions.Africa.Africa*             0.603
		Geography.Regions.Africa.Central Africa      0.454
		Geography.Regions.Africa.Eastern Africa      0.425
		Geography.Regions.Africa.Northern Africa     0.435
		Geography.Regions.Africa.Southern Africa     0.49
		Geography.Regions.Africa.Western Africa      0.515
		Geography.Regions.Americas.Central America   0.642
		Geography.Regions.Americas.North America     0.64
		Geography.Regions.Americas.South America     0.677
		Geography.Regions.Asia.Asia*                 0.64
		Geography.Regions.Asia.Central Asia          0.295
		Geography.Regions.Asia.East Asia             0.481
		Geography.Regions.Asia.North Asia            0.558
		Geography.Regions.Asia.South Asia            0.77
		Geography.Regions.Asia.Southeast Asia        0.674
		Geography.Regions.Asia.West Asia             0.685
		Geography.Regions.Europe.Eastern Europe      0.708
		Geography.Regions.Europe.Europe*             0.707
		Geography.Regions.Europe.Northern Europe     0.704
		Geography.Regions.Europe.Southern Europe     0.651
		Geography.Regions.Europe.Western Europe      0.679
		Geography.Regions.Oceania                    0.741
		History and Society.Business and economics   0.431
		History and Society.Education                0.575
		History and Society.History                  0.385
		History and Society.Military and warfare     0.551
		History and Society.Politics and government  0.443
		History and Society.Society                  0.239
		History and Society.Transportation           0.802
		STEM.Biology                                 0.803
		STEM.Chemistry                               0.475
		STEM.Computing                               0.315
		STEM.Earth and environment                   0.513
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.45
		STEM.Mathematics                             0.244
		STEM.Medicine & Health                       0.521
		STEM.Physics                                 0.2
		STEM.STEM*                                   0.736
		STEM.Space                                   0.791
		STEM.Technology                              0.294
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.954
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.953
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.983
		History and Society.Society                  0.989
		History and Society.Transportation           0.993
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.998
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.96
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.022
		Culture.Biography.Women                      0.012
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.037
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.023
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.039
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.017
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.963, macro=0.963):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.965
		Culture.Food and drink                       0.974
		Culture.Internet culture                     0.977
		Culture.Linguistics                          0.958
		Culture.Literature                           0.961
		Culture.Media.Books                          0.974
		Culture.Media.Entertainment                  0.953
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.951
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.972
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.957
		Culture.Philosophy and religion              0.93
		Culture.Sports                               0.974
		Culture.Visual arts.Architecture             0.966
		Culture.Visual arts.Comics and Anime         0.983
		Culture.Visual arts.Fashion                  0.969
		Culture.Visual arts.Visual arts*             0.953
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.967
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.963
		Geography.Regions.Africa.Northern Africa     0.972
		Geography.Regions.Africa.Southern Africa     0.949
		Geography.Regions.Africa.Western Africa      0.961
		Geography.Regions.Americas.Central America   0.958
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.954
		Geography.Regions.Asia.Central Asia          0.97
		Geography.Regions.Asia.East Asia             0.968
		Geography.Regions.Asia.North Asia            0.965
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.968
		Geography.Regions.Asia.West Asia             0.963
		Geography.Regions.Europe.Eastern Europe      0.963
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.969
		Geography.Regions.Europe.Western Europe      0.972
		Geography.Regions.Oceania                    0.961
		History and Society.Business and economics   0.949
		History and Society.Education                0.957
		History and Society.History                  0.935
		History and Society.Military and warfare     0.953
		History and Society.Politics and government  0.931
		History and Society.Society                  0.868
		History and Society.Transportation           0.978
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.98
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.959
		STEM.Engineering                             0.968
		STEM.Libraries & Information                 0.965
		STEM.Mathematics                             0.975
		STEM.Medicine & Health                       0.959
		STEM.Physics                                 0.971
		STEM.STEM*                                   0.967
		STEM.Space                                   0.983
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.718, macro=0.55):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.926
		Culture.Biography.Women                      0.478
		Culture.Food and drink                       0.557
		Culture.Internet culture                     0.564
		Culture.Linguistics                          0.606
		Culture.Literature                           0.624
		Culture.Media.Books                          0.598
		Culture.Media.Entertainment                  0.286
		Culture.Media.Films                          0.841
		Culture.Media.Media*                         0.774
		Culture.Media.Music                          0.752
		Culture.Media.Radio                          0.431
		Culture.Media.Software                       0.165
		Culture.Media.Television                     0.599
		Culture.Media.Video games                    0.771
		Culture.Performing arts                      0.34
		Culture.Philosophy and religion              0.406
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.625
		Culture.Visual arts.Comics and Anime         0.575
		Culture.Visual arts.Fashion                  0.28
		Culture.Visual arts.Visual arts*             0.603
		Geography.Geographical                       0.576
		Geography.Regions.Africa.Africa*             0.616
		Geography.Regions.Africa.Central Africa      0.368
		Geography.Regions.Africa.Eastern Africa      0.271
		Geography.Regions.Africa.Northern Africa     0.339
		Geography.Regions.Africa.Southern Africa     0.344
		Geography.Regions.Africa.Western Africa      0.355
		Geography.Regions.Americas.Central America   0.585
		Geography.Regions.Americas.North America     0.669
		Geography.Regions.Americas.South America     0.686
		Geography.Regions.Asia.Asia*                 0.705
		Geography.Regions.Asia.Central Asia          0.23
		Geography.Regions.Asia.East Asia             0.509
		Geography.Regions.Asia.North Asia            0.548
		Geography.Regions.Asia.South Asia            0.807
		Geography.Regions.Asia.Southeast Asia        0.686
		Geography.Regions.Asia.West Asia             0.697
		Geography.Regions.Europe.Eastern Europe      0.734
		Geography.Regions.Europe.Europe*             0.758
		Geography.Regions.Europe.Northern Europe     0.742
		Geography.Regions.Europe.Southern Europe     0.674
		Geography.Regions.Europe.Western Europe      0.683
		Geography.Regions.Oceania                    0.776
		History and Society.Business and economics   0.367
		History and Society.Education                0.554
		History and Society.History                  0.341
		History and Society.Military and warfare     0.545
		History and Society.Politics and government  0.4
		History and Society.Society                  0.175
		History and Society.Transportation           0.828
		STEM.Biology                                 0.857
		STEM.Chemistry                               0.475
		STEM.Computing                               0.287
		STEM.Earth and environment                   0.513
		STEM.Engineering                             0.59
		STEM.Libraries & Information                 0.405
		STEM.Mathematics                             0.228
		STEM.Medicine & Health                       0.483
		STEM.Physics                                 0.131
		STEM.STEM*                                   0.849
		STEM.Space                                   0.837
		STEM.Technology                              0.259
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}}

