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
	counts (n=55551):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15686  -->  14424  1262   645  39220
			'Culture.Biography.Women'                       4518  -->   3337  1181   472  50561
			'Culture.Food and drink'                        1662  -->   1334   328   104  53785
			'Culture.Internet culture'                      2507  -->   2103   404   138  52906
			'Culture.Linguistics'                           1693  -->   1255   438    60  53798
			'Culture.Literature'                            5298  -->   4039  1259   484  49769
			'Culture.Media.Books'                           1758  -->   1494   264   102  53691
			'Culture.Media.Entertainment'                   2153  -->   1065  1088   181  53217
			'Culture.Media.Films'                           3018  -->   2661   357   127  52406
			'Culture.Media.Media*'                         13233  -->  11675  1558  1184  41134
			'Culture.Media.Music'                           3428  -->   2919   509   238  51885
			'Culture.Media.Radio'                            233  -->    172    61    27  55291
			'Culture.Media.Software'                        2201  -->   2044   157   157  53193
			'Culture.Media.Television'                      2078  -->   1685   393    81  53392
			'Culture.Media.Video games'                      766  -->    727    39    14  54771
			'Culture.Performing arts'                       1734  -->   1213   521   133  53684
			'Culture.Philosophy and religion'               3901  -->   2224  1677   332  51318
			'Culture.Sports'                                3288  -->   2757   531    92  52171
			'Culture.Visual arts.Architecture'              2452  -->   1944   508   257  52842
			'Culture.Visual arts.Comics and Anime'          1071  -->    902   169    36  54444
			'Culture.Visual arts.Fashion'                    820  -->    616   204    39  54692
			'Culture.Visual arts.Visual arts*'              5439  -->   4109  1330   473  49639
			'Geography.Geographical'                        4862  -->   3573  1289   594  50095
			'Geography.Regions.Africa.Africa*'              3298  -->   2028  1270   195  52058
			'Geography.Regions.Africa.Central Africa'        401  -->    267   134    28  55122
			'Geography.Regions.Africa.Eastern Africa'        256  -->    189    67    32  55263
			'Geography.Regions.Africa.Northern Africa'      1335  -->    911   424    92  54124
			'Geography.Regions.Africa.Southern Africa'       605  -->    461   144    30  54916
			'Geography.Regions.Africa.Western Africa'        140  -->     97    43    27  55384
			'Geography.Regions.Americas.Central America'    1256  -->    626   630    52  54243
			'Geography.Regions.Americas.North America'      5910  -->   4266  1644   773  48868
			'Geography.Regions.Americas.South America'      1669  -->   1321   348    59  53823
			'Geography.Regions.Asia.Asia*'                 12149  -->   9910  2239  1082  42320
			'Geography.Regions.Asia.Central Asia'           1088  -->    727   361    64  54399
			'Geography.Regions.Asia.East Asia'              2652  -->   2212   440   102  52797
			'Geography.Regions.Asia.North Asia'             2562  -->   1917   645   312  52677
			'Geography.Regions.Asia.South Asia'             1924  -->   1384   540    58  53569
			'Geography.Regions.Asia.Southeast Asia'         1456  -->    781   675    44  54051
			'Geography.Regions.Asia.West Asia'              4499  -->   3549   950   353  50699
			'Geography.Regions.Europe.Eastern Europe'       4478  -->   3392  1086   429  50644
			'Geography.Regions.Europe.Europe*'             16951  -->  13930  3021  1879  36721
			'Geography.Regions.Europe.Northern Europe'      4245  -->   3154  1091   300  51006
			'Geography.Regions.Europe.Southern Europe'      4409  -->   3415   994   300  50842
			'Geography.Regions.Europe.Western Europe'       4936  -->   3957   979   384  50231
			'Geography.Regions.Oceania'                     1674  -->   1048   626    60  53817
			'History and Society.Business and economics'    3475  -->   2351  1124   304  51772
			'History and Society.Education'                 1893  -->   1233   660   128  53530
			'History and Society.History'                   5858  -->   3536  2322   747  48946
			'History and Society.Military and warfare'      5200  -->   3681  1519   602  49749
			'History and Society.Politics and government'   4691  -->   2669  2022   476  50384
			'History and Society.Society'                   7986  -->   4379  3607   782  46783
			'History and Society.Transportation'            2514  -->   2174   340    79  52958
			'STEM.Biology'                                  3086  -->   2434   652   156  52309
			'STEM.Chemistry'                                1651  -->   1407   244   118  53782
			'STEM.Computing'                                2282  -->   1969   313   172  53097
			'STEM.Earth and environment'                    1861  -->   1290   571   109  53581
			'STEM.Engineering'                              2812  -->   2141   671   200  52539
			'STEM.Libraries & Information'                   503  -->    391   112    24  55024
			'STEM.Mathematics'                               592  -->    490   102    33  54926
			'STEM.Medicine & Health'                        2084  -->   1584   500   148  53319
			'STEM.Physics'                                  1667  -->   1299   368   144  53740
			'STEM.STEM*'                                   16786  -->  15013  1773   829  37936
			'STEM.Space'                                    2077  -->   1958   119    28  53446
			'STEM.Technology'                               4483  -->   3501   982   528  50540
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.282         0.123
		Culture.Biography.Women                         0.081         0.015
		Culture.Food and drink                          0.03          0.002
		Culture.Internet culture                        0.045         0.003
		Culture.Linguistics                             0.03          0.007
		Culture.Literature                              0.095         0.015
		Culture.Media.Books                             0.032         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.054         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.062         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.014         0.003
		Culture.Performing arts                         0.031         0.003
		Culture.Philosophy and religion                 0.07          0.011
		Culture.Sports                                  0.059         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.019         0.002
		Culture.Visual arts.Fashion                     0.015         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.088         0.024
		Geography.Regions.Africa.Africa*                0.059         0.008
		Geography.Regions.Africa.Central Africa         0.007         0.001
		Geography.Regions.Africa.Eastern Africa         0.005         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.03          0.006
		Geography.Regions.Asia.Asia*                    0.219         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.048         0.011
		Geography.Regions.Asia.North Asia               0.046         0.001
		Geography.Regions.Asia.South Asia               0.035         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.081         0.011
		Geography.Regions.Europe.Eastern Europe         0.081         0.013
		Geography.Regions.Europe.Europe*                0.305         0.076
		Geography.Regions.Europe.Northern Europe        0.076         0.031
		Geography.Regions.Europe.Southern Europe        0.079         0.013
		Geography.Regions.Europe.Western Europe         0.089         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.105         0.011
		History and Society.Military and warfare        0.094         0.014
		History and Society.Politics and government     0.084         0.028
		History and Society.Society                     0.144         0.013
		History and Society.Transportation              0.045         0.015
		STEM.Biology                                    0.056         0.034
		STEM.Chemistry                                  0.03          0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.034         0.005
		STEM.Engineering                                0.051         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.011         0
		STEM.Medicine & Health                          0.038         0.006
		STEM.Physics                                    0.03          0.001
		STEM.STEM*                                      0.302         0.069
		STEM.Space                                      0.037         0.006
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.025
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.061
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.015
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.108
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.021
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.025
		History and Society.Society                  0.023
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.939
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.985
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.892
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.979
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.975
		History and Society.Society                  0.977
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.795, macro=0.755):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.92
		Culture.Biography.Women                      0.739
		Culture.Food and drink                       0.803
		Culture.Internet culture                     0.839
		Culture.Linguistics                          0.741
		Culture.Literature                           0.762
		Culture.Media.Books                          0.85
		Culture.Media.Entertainment                  0.495
		Culture.Media.Films                          0.882
		Culture.Media.Media*                         0.882
		Culture.Media.Music                          0.852
		Culture.Media.Radio                          0.738
		Culture.Media.Software                       0.929
		Culture.Media.Television                     0.811
		Culture.Media.Video games                    0.949
		Culture.Performing arts                      0.7
		Culture.Philosophy and religion              0.57
		Culture.Sports                               0.839
		Culture.Visual arts.Architecture             0.793
		Culture.Visual arts.Comics and Anime         0.842
		Culture.Visual arts.Fashion                  0.751
		Culture.Visual arts.Visual arts*             0.755
		Geography.Geographical                       0.735
		Geography.Regions.Africa.Africa*             0.615
		Geography.Regions.Africa.Central Africa      0.666
		Geography.Regions.Africa.Eastern Africa      0.738
		Geography.Regions.Africa.Northern Africa     0.682
		Geography.Regions.Africa.Southern Africa     0.762
		Geography.Regions.Africa.Western Africa      0.693
		Geography.Regions.Americas.Central America   0.498
		Geography.Regions.Americas.North America     0.722
		Geography.Regions.Americas.South America     0.791
		Geography.Regions.Asia.Asia*                 0.816
		Geography.Regions.Asia.Central Asia          0.668
		Geography.Regions.Asia.East Asia             0.834
		Geography.Regions.Asia.North Asia            0.748
		Geography.Regions.Asia.South Asia            0.719
		Geography.Regions.Asia.Southeast Asia        0.536
		Geography.Regions.Asia.West Asia             0.789
		Geography.Regions.Europe.Eastern Europe      0.757
		Geography.Regions.Europe.Europe*             0.822
		Geography.Regions.Europe.Northern Europe     0.743
		Geography.Regions.Europe.Southern Europe     0.775
		Geography.Regions.Europe.Western Europe      0.802
		Geography.Regions.Oceania                    0.626
		History and Society.Business and economics   0.677
		History and Society.Education                0.651
		History and Society.History                  0.604
		History and Society.Military and warfare     0.708
		History and Society.Politics and government  0.569
		History and Society.Society                  0.548
		History and Society.Transportation           0.865
		STEM.Biology                                 0.789
		STEM.Chemistry                               0.852
		STEM.Computing                               0.863
		STEM.Earth and environment                   0.693
		STEM.Engineering                             0.761
		STEM.Libraries & Information                 0.777
		STEM.Mathematics                             0.828
		STEM.Medicine & Health                       0.76
		STEM.Physics                                 0.779
		STEM.STEM*                                   0.894
		STEM.Space                                   0.943
		STEM.Technology                              0.781
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.951
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.991
		History and Society.Society                  0.984
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.719, macro=0.601):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.889
		Culture.Biography.Women                      0.541
		Culture.Food and drink                       0.507
		Culture.Internet culture                     0.531
		Culture.Linguistics                          0.831
		Culture.Literature                           0.555
		Culture.Media.Books                          0.644
		Culture.Media.Entertainment                  0.344
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.662
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.766
		Culture.Media.Software                       0.296
		Culture.Media.Television                     0.826
		Culture.Media.Video games                    0.907
		Culture.Performing arts                      0.45
		Culture.Philosophy and religion              0.488
		Culture.Sports                               0.973
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.737
		Culture.Visual arts.Fashion                  0.46
		Culture.Visual arts.Visual arts*             0.599
		Geography.Geographical                       0.602
		Geography.Regions.Africa.Africa*             0.564
		Geography.Regions.Africa.Central Africa      0.453
		Geography.Regions.Africa.Eastern Africa      0.367
		Geography.Regions.Africa.Northern Africa     0.331
		Geography.Regions.Africa.Southern Africa     0.621
		Geography.Regions.Africa.Western Africa      0.493
		Geography.Regions.Americas.Central America   0.633
		Geography.Regions.Americas.North America     0.761
		Geography.Regions.Americas.South America     0.821
		Geography.Regions.Asia.Asia*                 0.609
		Geography.Regions.Asia.Central Asia          0.33
		Geography.Regions.Asia.East Asia             0.833
		Geography.Regions.Asia.North Asia            0.105
		Geography.Regions.Asia.South Asia            0.911
		Geography.Regions.Asia.Southeast Asia        0.799
		Geography.Regions.Asia.West Asia             0.557
		Geography.Regions.Europe.Eastern Europe      0.54
		Geography.Regions.Europe.Europe*             0.582
		Geography.Regions.Europe.Northern Europe     0.8
		Geography.Regions.Europe.Southern Europe     0.636
		Geography.Regions.Europe.Western Europe      0.674
		Geography.Regions.Oceania                    0.896
		History and Society.Business and economics   0.541
		History and Society.Education                0.669
		History and Society.History                  0.305
		History and Society.Military and warfare     0.458
		History and Society.Politics and government  0.638
		History and Society.Society                  0.299
		History and Society.Transportation           0.899
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.378
		STEM.Computing                               0.419
		STEM.Earth and environment                   0.609
		STEM.Engineering                             0.514
		STEM.Libraries & Information                 0.526
		STEM.Mathematics                             0.365
		STEM.Medicine & Health                       0.639
		STEM.Physics                                 0.199
		STEM.STEM*                                   0.756
		STEM.Space                                   0.916
		STEM.Technology                              0.28
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       1
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
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
	f1 (micro=0.747, macro=0.65):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.904
		Culture.Biography.Women                      0.625
		Culture.Food and drink                       0.621
		Culture.Internet culture                     0.65
		Culture.Linguistics                          0.784
		Culture.Literature                           0.642
		Culture.Media.Books                          0.733
		Culture.Media.Entertainment                  0.406
		Culture.Media.Films                          0.836
		Culture.Media.Media*                         0.756
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.752
		Culture.Media.Software                       0.448
		Culture.Media.Television                     0.819
		Culture.Media.Video games                    0.927
		Culture.Performing arts                      0.548
		Culture.Philosophy and religion              0.526
		Culture.Sports                               0.901
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.786
		Culture.Visual arts.Fashion                  0.571
		Culture.Visual arts.Visual arts*             0.668
		Geography.Geographical                       0.662
		Geography.Regions.Africa.Africa*             0.588
		Geography.Regions.Africa.Central Africa      0.539
		Geography.Regions.Africa.Eastern Africa      0.491
		Geography.Regions.Africa.Northern Africa     0.445
		Geography.Regions.Africa.Southern Africa     0.685
		Geography.Regions.Africa.Western Africa      0.576
		Geography.Regions.Americas.Central America   0.558
		Geography.Regions.Americas.North America     0.741
		Geography.Regions.Americas.South America     0.806
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.442
		Geography.Regions.Asia.East Asia             0.834
		Geography.Regions.Asia.North Asia            0.184
		Geography.Regions.Asia.South Asia            0.804
		Geography.Regions.Asia.Southeast Asia        0.642
		Geography.Regions.Asia.West Asia             0.653
		Geography.Regions.Europe.Eastern Europe      0.63
		Geography.Regions.Europe.Europe*             0.681
		Geography.Regions.Europe.Northern Europe     0.771
		Geography.Regions.Europe.Southern Europe     0.698
		Geography.Regions.Europe.Western Europe      0.732
		Geography.Regions.Oceania                    0.737
		History and Society.Business and economics   0.602
		History and Society.Education                0.66
		History and Society.History                  0.406
		History and Society.Military and warfare     0.556
		History and Society.Politics and government  0.602
		History and Society.Society                  0.387
		History and Society.Transportation           0.881
		STEM.Biology                                 0.842
		STEM.Chemistry                               0.524
		STEM.Computing                               0.564
		STEM.Earth and environment                   0.648
		STEM.Engineering                             0.613
		STEM.Libraries & Information                 0.627
		STEM.Mathematics                             0.507
		STEM.Medicine & Health                       0.694
		STEM.Physics                                 0.316
		STEM.STEM*                                   0.82
		STEM.Space                                   0.929
		STEM.Technology                              0.413
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
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
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.989
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.981
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.979
		History and Society.Society                  0.978
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.016
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.025
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.008
		Geography.Regions.Europe.Europe*             0.049
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.015
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.009
		History and Society.Society                  0.016
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.021
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.975, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.977
		Culture.Literature                           0.976
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.97
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.919
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.979
		Culture.Philosophy and religion              0.957
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.985
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.973
		Geography.Regions.Africa.Eastern Africa      0.951
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.886
		Geography.Regions.Americas.Central America   0.958
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.975
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.977
		Geography.Regions.Asia.Southeast Asia        0.961
		Geography.Regions.Asia.West Asia             0.982
		Geography.Regions.Europe.Eastern Europe      0.978
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.97
		History and Society.Business and economics   0.971
		History and Society.Education                0.973
		History and Society.History                  0.953
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.957
		History and Society.Society                  0.934
		History and Society.Transportation           0.986
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.988
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.974
		STEM.Medicine & Health                       0.98
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.979
		STEM.Space                                   0.994
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.796, macro=0.652):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.618
		Culture.Food and drink                       0.65
		Culture.Internet culture                     0.711
		Culture.Linguistics                          0.766
		Culture.Literature                           0.701
		Culture.Media.Books                          0.815
		Culture.Media.Entertainment                  0.343
		Culture.Media.Films                          0.893
		Culture.Media.Media*                         0.869
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.506
		Culture.Media.Software                       0.58
		Culture.Media.Television                     0.834
		Culture.Media.Video games                    0.931
		Culture.Performing arts                      0.502
		Culture.Philosophy and religion              0.529
		Culture.Sports                               0.947
		Culture.Visual arts.Architecture             0.741
		Culture.Visual arts.Comics and Anime         0.789
		Culture.Visual arts.Fashion                  0.458
		Culture.Visual arts.Visual arts*             0.669
		Geography.Geographical                       0.7
		Geography.Regions.Africa.Africa*             0.576
		Geography.Regions.Africa.Central Africa      0.357
		Geography.Regions.Africa.Eastern Africa      0.215
		Geography.Regions.Africa.Northern Africa     0.324
		Geography.Regions.Africa.Southern Africa     0.545
		Geography.Regions.Africa.Western Africa      0.284
		Geography.Regions.Americas.Central America   0.527
		Geography.Regions.Americas.North America     0.796
		Geography.Regions.Americas.South America     0.828
		Geography.Regions.Asia.Asia*                 0.766
		Geography.Regions.Asia.Central Asia          0.323
		Geography.Regions.Asia.East Asia             0.846
		Geography.Regions.Asia.North Asia            0.191
		Geography.Regions.Asia.South Asia            0.852
		Geography.Regions.Asia.Southeast Asia        0.628
		Geography.Regions.Asia.West Asia             0.691
		Geography.Regions.Europe.Eastern Europe      0.662
		Geography.Regions.Europe.Europe*             0.778
		Geography.Regions.Europe.Northern Europe     0.819
		Geography.Regions.Europe.Southern Europe     0.739
		Geography.Regions.Europe.Western Europe      0.781
		Geography.Regions.Oceania                    0.773
		History and Society.Business and economics   0.591
		History and Society.Education                0.622
		History and Society.History                  0.414
		History and Society.Military and warfare     0.596
		History and Society.Politics and government  0.63
		History and Society.Society                  0.385
		History and Society.Transportation           0.916
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.6
		STEM.Computing                               0.624
		STEM.Earth and environment                   0.648
		STEM.Engineering                             0.652
		STEM.Libraries & Information                 0.518
		STEM.Mathematics                             0.502
		STEM.Medicine & Health                       0.733
		STEM.Physics                                 0.323
		STEM.STEM*                                   0.912
		STEM.Space                                   0.966
		STEM.Technology                              0.541
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

