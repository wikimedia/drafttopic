Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'learning_rate': 0.1, 'subsample': 1.0, 'loss': 'deviance', 'center': False, 'presort': 'deprecated', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_weight_fraction_leaf': 0.0, 'validation_fraction': 0.1, 'min_samples_split': 2, 'tol': 0.0001, 'n_iter_no_change': None, 'max_leaf_nodes': None, 'multilabel': True, 'n_estimators': 150, 'max_depth': 5, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'random_state': None, 'warm_start': False, 'max_features': 'log2', 'min_samples_leaf': 1, 'verbose': 0, 'ccp_alpha': 0.0, 'population_rates': None, 'criterion': 'friedman_mse', 'scale': False, 'init': None, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.12'
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
	counts (n=60857):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16286  -->  13781  2505  1337  43234
			'Culture.Biography.Women'                       4089  -->   2833  1256   734  56034
			'Culture.Food and drink'                        1229  -->    848   381    87  59541
			'Culture.Internet culture'                      2696  -->   1983   713   225  57936
			'Culture.Linguistics'                           1194  -->    755   439    82  59581
			'Culture.Literature'                            5049  -->   3448  1601   564  55244
			'Culture.Media.Books'                           1880  -->   1196   684   206  58771
			'Culture.Media.Entertainment'                   1721  -->    719  1002   190  58946
			'Culture.Media.Films'                           2177  -->   1633   544   211  58469
			'Culture.Media.Media*'                         13482  -->  11071  2411  1576  45799
			'Culture.Media.Music'                           2458  -->   1887   571   284  58115
			'Culture.Media.Radio'                           1117  -->    844   273    46  59694
			'Culture.Media.Software'                        1687  -->    916   771   381  58789
			'Culture.Media.Television'                      2038  -->   1304   734   230  58589
			'Culture.Media.Video games'                     1929  -->   1644   285    78  58850
			'Culture.Performing arts'                       1301  -->    806   495   110  59446
			'Culture.Philosophy and religion'               2622  -->   1309  1313   355  57880
			'Culture.Sports'                                5790  -->   5211   579   352  54715
			'Culture.Visual arts.Architecture'              2429  -->   1677   752   282  58146
			'Culture.Visual arts.Comics and Anime'          1379  -->   1030   349   131  59347
			'Culture.Visual arts.Fashion'                   1105  -->    752   353    59  59693
			'Culture.Visual arts.Visual arts*'              5629  -->   4006  1623   577  54651
			'Geography.Geographical'                        3409  -->   2206  1203   296  57152
			'Geography.Regions.Africa.Africa*'              6235  -->   5132  1103   329  54293
			'Geography.Regions.Africa.Central Africa'       1108  -->    500   608   104  59645
			'Geography.Regions.Africa.Eastern Africa'       1053  -->    788   265    34  59770
			'Geography.Regions.Africa.Northern Africa'      1234  -->    870   364    93  59530
			'Geography.Regions.Africa.Southern Africa'      1246  -->    883   363    51  59560
			'Geography.Regions.Africa.Western Africa'       1110  -->    860   250    70  59677
			'Geography.Regions.Americas.Central America'    1264  -->    792   472    64  59529
			'Geography.Regions.Americas.North America'      7241  -->   4557  2684  1178  52438
			'Geography.Regions.Americas.South America'      1504  -->   1038   466   112  59241
			'Geography.Regions.Asia.Asia*'                 10581  -->   8685  1896   872  49404
			'Geography.Regions.Asia.Central Asia'           1090  -->    806   284    44  59723
			'Geography.Regions.Asia.East Asia'              2542  -->   1797   745   277  58038
			'Geography.Regions.Asia.North Asia'             1316  -->    798   518   178  59363
			'Geography.Regions.Asia.South Asia'             2335  -->   1866   469   118  58404
			'Geography.Regions.Asia.Southeast Asia'         1596  -->   1166   430    93  59168
			'Geography.Regions.Asia.West Asia'              2159  -->   1629   530   166  58532
			'Geography.Regions.Europe.Eastern Europe'       2991  -->   2149   842   284  57582
			'Geography.Regions.Europe.Europe*'             12061  -->   8770  3291  1801  46995
			'Geography.Regions.Europe.Northern Europe'      4121  -->   2594  1527   599  56137
			'Geography.Regions.Europe.Southern Europe'      2333  -->   1510   823   273  58251
			'Geography.Regions.Europe.Western Europe'       3005  -->   1798  1207   380  57472
			'Geography.Regions.Oceania'                     2471  -->   1828   643   148  58238
			'History and Society.Business and economics'    3187  -->   1306  1881   487  57183
			'History and Society.Education'                 2066  -->    946  1120   260  58531
			'History and Society.History'                   3104  -->   1229  1875   483  57270
			'History and Society.Military and warfare'      3925  -->   2617  1308   422  56510
			'History and Society.Politics and government'   4412  -->   2454  1958   483  55962
			'History and Society.Society'                   3820  -->   1170  2650   349  56688
			'History and Society.Transportation'            3428  -->   2819   609   247  57182
			'STEM.Biology'                                  2888  -->   2303   585   133  57836
			'STEM.Chemistry'                                1231  -->    790   441   164  59462
			'STEM.Computing'                                1884  -->   1193   691   431  58542
			'STEM.Earth and environment'                    1566  -->   1041   525   113  59178
			'STEM.Engineering'                              2193  -->   1486   707   171  58493
			'STEM.Libraries & Information'                  1100  -->    583   517    74  59683
			'STEM.Mathematics'                              1037  -->    691   346    95  59725
			'STEM.Medicine & Health'                        1666  -->   1032   634   189  59002
			'STEM.Physics'                                  1138  -->    682   456   132  59587
			'STEM.STEM*'                                   15681  -->  13212  2469  1123  44053
			'STEM.Space'                                    1276  -->   1089   187    54  59527
			'STEM.Technology'                               3405  -->   1939  1466   587  56865
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.268         0.123
		Culture.Biography.Women                         0.067         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.044         0.003
		Culture.Linguistics                             0.02          0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.031         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.222         0.058
		Culture.Media.Music                             0.04          0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.043         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.092         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.174         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.042         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.035         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.198         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.049         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.052         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.047         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.031         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.021         0.006
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.023
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.02
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.089
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.008
		History and Society.History                  0.013
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.024
		History and Society.Society                  0.01
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.911
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.99
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.734, macro=0.673):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.846
		Culture.Biography.Women                      0.693
		Culture.Food and drink                       0.69
		Culture.Internet culture                     0.736
		Culture.Linguistics                          0.632
		Culture.Literature                           0.683
		Culture.Media.Books                          0.636
		Culture.Media.Entertainment                  0.418
		Culture.Media.Films                          0.75
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.768
		Culture.Media.Radio                          0.756
		Culture.Media.Software                       0.543
		Culture.Media.Television                     0.64
		Culture.Media.Video games                    0.852
		Culture.Performing arts                      0.62
		Culture.Philosophy and religion              0.499
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.69
		Culture.Visual arts.Comics and Anime         0.747
		Culture.Visual arts.Fashion                  0.681
		Culture.Visual arts.Visual arts*             0.712
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.823
		Geography.Regions.Africa.Central Africa      0.451
		Geography.Regions.Africa.Eastern Africa      0.748
		Geography.Regions.Africa.Northern Africa     0.705
		Geography.Regions.Africa.Southern Africa     0.709
		Geography.Regions.Africa.Western Africa      0.775
		Geography.Regions.Americas.Central America   0.627
		Geography.Regions.Americas.North America     0.629
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.821
		Geography.Regions.Asia.Central Asia          0.739
		Geography.Regions.Asia.East Asia             0.707
		Geography.Regions.Asia.North Asia            0.606
		Geography.Regions.Asia.South Asia            0.799
		Geography.Regions.Asia.Southeast Asia        0.731
		Geography.Regions.Asia.West Asia             0.755
		Geography.Regions.Europe.Eastern Europe      0.718
		Geography.Regions.Europe.Europe*             0.727
		Geography.Regions.Europe.Northern Europe     0.629
		Geography.Regions.Europe.Southern Europe     0.647
		Geography.Regions.Europe.Western Europe      0.598
		Geography.Regions.Oceania                    0.74
		History and Society.Business and economics   0.41
		History and Society.Education                0.458
		History and Society.History                  0.396
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.556
		History and Society.Society                  0.306
		History and Society.Transportation           0.822
		STEM.Biology                                 0.797
		STEM.Chemistry                               0.642
		STEM.Computing                               0.633
		STEM.Earth and environment                   0.665
		STEM.Engineering                             0.678
		STEM.Libraries & Information                 0.53
		STEM.Mathematics                             0.666
		STEM.Medicine & Health                       0.619
		STEM.Physics                                 0.599
		STEM.STEM*                                   0.843
		STEM.Space                                   0.853
		STEM.Technology                              0.569
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.679, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.798
		Culture.Biography.Women                      0.442
		Culture.Food and drink                       0.539
		Culture.Internet culture                     0.4
		Culture.Linguistics                          0.773
		Culture.Literature                           0.515
		Culture.Media.Books                          0.424
		Culture.Media.Entertainment                  0.318
		Culture.Media.Films                          0.689
		Culture.Media.Media*                         0.605
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.679
		Culture.Media.Software                       0.101
		Culture.Media.Television                     0.593
		Culture.Media.Video games                    0.628
		Culture.Performing arts                      0.493
		Culture.Philosophy and religion              0.469
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.604
		Culture.Visual arts.Comics and Anime         0.427
		Culture.Visual arts.Fashion                  0.358
		Culture.Visual arts.Visual arts*             0.559
		Geography.Geographical                       0.752
		Geography.Regions.Africa.Africa*             0.518
		Geography.Regions.Africa.Central Africa      0.141
		Geography.Regions.Africa.Eastern Africa      0.375
		Geography.Regions.Africa.Northern Africa     0.357
		Geography.Regions.Africa.Southern Africa     0.494
		Geography.Regions.Africa.Western Africa      0.311
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.663
		Geography.Regions.Americas.South America     0.699
		Geography.Regions.Asia.Asia*                 0.693
		Geography.Regions.Asia.Central Asia          0.465
		Geography.Regions.Asia.East Asia             0.632
		Geography.Regions.Asia.North Asia            0.158
		Geography.Regions.Asia.South Asia            0.859
		Geography.Regions.Asia.Southeast Asia        0.738
		Geography.Regions.Asia.West Asia             0.746
		Geography.Regions.Europe.Eastern Europe      0.655
		Geography.Regions.Europe.Europe*             0.619
		Geography.Regions.Europe.Northern Europe     0.653
		Geography.Regions.Europe.Southern Europe     0.647
		Geography.Regions.Europe.Western Europe      0.64
		Geography.Regions.Oceania                    0.818
		History and Society.Business and economics   0.331
		History and Society.Education                0.434
		History and Society.History                  0.341
		History and Society.Military and warfare     0.562
		History and Society.Politics and government  0.653
		History and Society.Society                  0.39
		History and Society.Transportation           0.745
		STEM.Biology                                 0.924
		STEM.Chemistry                               0.267
		STEM.Computing                               0.189
		STEM.Earth and environment                   0.614
		STEM.Engineering                             0.55
		STEM.Libraries & Information                 0.21
		STEM.Mathematics                             0.149
		STEM.Medicine & Health                       0.555
		STEM.Physics                                 0.187
		STEM.STEM*                                   0.716
		STEM.Space                                   0.851
		STEM.Technology                              0.223
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
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
	f1 (micro=0.701, macro=0.579):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.822
		Culture.Biography.Women                      0.54
		Culture.Food and drink                       0.605
		Culture.Internet culture                     0.518
		Culture.Linguistics                          0.695
		Culture.Literature                           0.587
		Culture.Media.Books                          0.509
		Culture.Media.Entertainment                  0.361
		Culture.Media.Films                          0.718
		Culture.Media.Media*                         0.697
		Culture.Media.Music                          0.781
		Culture.Media.Radio                          0.715
		Culture.Media.Software                       0.17
		Culture.Media.Television                     0.615
		Culture.Media.Video games                    0.723
		Culture.Performing arts                      0.549
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.645
		Culture.Visual arts.Comics and Anime         0.544
		Culture.Visual arts.Fashion                  0.469
		Culture.Visual arts.Visual arts*             0.626
		Geography.Geographical                       0.696
		Geography.Regions.Africa.Africa*             0.636
		Geography.Regions.Africa.Central Africa      0.215
		Geography.Regions.Africa.Eastern Africa      0.499
		Geography.Regions.Africa.Northern Africa     0.474
		Geography.Regions.Africa.Southern Africa     0.582
		Geography.Regions.Africa.Western Africa      0.444
		Geography.Regions.Americas.Central America   0.642
		Geography.Regions.Americas.North America     0.646
		Geography.Regions.Americas.South America     0.695
		Geography.Regions.Asia.Asia*                 0.751
		Geography.Regions.Asia.Central Asia          0.571
		Geography.Regions.Asia.East Asia             0.667
		Geography.Regions.Asia.North Asia            0.251
		Geography.Regions.Asia.South Asia            0.828
		Geography.Regions.Asia.Southeast Asia        0.734
		Geography.Regions.Asia.West Asia             0.75
		Geography.Regions.Europe.Eastern Europe      0.686
		Geography.Regions.Europe.Europe*             0.669
		Geography.Regions.Europe.Northern Europe     0.641
		Geography.Regions.Europe.Southern Europe     0.647
		Geography.Regions.Europe.Western Europe      0.619
		Geography.Regions.Oceania                    0.777
		History and Society.Business and economics   0.366
		History and Society.Education                0.446
		History and Society.History                  0.367
		History and Society.Military and warfare     0.61
		History and Society.Politics and government  0.601
		History and Society.Society                  0.343
		History and Society.Transportation           0.782
		STEM.Biology                                 0.856
		STEM.Chemistry                               0.377
		STEM.Computing                               0.292
		STEM.Earth and environment                   0.638
		STEM.Engineering                             0.607
		STEM.Libraries & Information                 0.301
		STEM.Mathematics                             0.243
		STEM.Medicine & Health                       0.586
		STEM.Physics                                 0.285
		STEM.STEM*                                   0.774
		STEM.Space                                   0.852
		STEM.Technology                              0.321
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.945
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.979
		History and Society.Society                  0.985
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.03
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.968, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.972
		Culture.Food and drink                       0.978
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.971
		Culture.Literature                           0.97
		Culture.Media.Books                          0.974
		Culture.Media.Entertainment                  0.961
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.986
		Culture.Media.Software                       0.979
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.974
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.977
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.979
		Geography.Regions.Africa.Central Africa      0.975
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.976
		Geography.Regions.Africa.Southern Africa     0.975
		Geography.Regions.Africa.Western Africa      0.978
		Geography.Regions.Americas.Central America   0.975
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.978
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.966
		Geography.Regions.Europe.Southern Europe     0.973
		Geography.Regions.Europe.Western Europe      0.965
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.941
		History and Society.Education                0.956
		History and Society.History                  0.934
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.95
		History and Society.Society                  0.905
		History and Society.Transportation           0.985
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.98
		STEM.Computing                               0.98
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.975
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.983
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.971
		STEM.Space                                   0.989
		STEM.Technology                              0.965
		-------------------------------------------  -----
	pr_auc (micro=0.738, macro=0.584):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.512
		Culture.Food and drink                       0.602
		Culture.Internet culture                     0.663
		Culture.Linguistics                          0.717
		Culture.Literature                           0.624
		Culture.Media.Books                          0.495
		Culture.Media.Entertainment                  0.318
		Culture.Media.Films                          0.723
		Culture.Media.Media*                         0.786
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.794
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.629
		Culture.Media.Video games                    0.807
		Culture.Performing arts                      0.486
		Culture.Philosophy and religion              0.438
		Culture.Sports                               0.927
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.53
		Culture.Visual arts.Fashion                  0.453
		Culture.Visual arts.Visual arts*             0.675
		Geography.Geographical                       0.727
		Geography.Regions.Africa.Africa*             0.665
		Geography.Regions.Africa.Central Africa      0.15
		Geography.Regions.Africa.Eastern Africa      0.359
		Geography.Regions.Africa.Northern Africa     0.44
		Geography.Regions.Africa.Southern Africa     0.577
		Geography.Regions.Africa.Western Africa      0.35
		Geography.Regions.Americas.Central America   0.598
		Geography.Regions.Americas.North America     0.702
		Geography.Regions.Americas.South America     0.693
		Geography.Regions.Asia.Asia*                 0.8
		Geography.Regions.Asia.Central Asia          0.573
		Geography.Regions.Asia.East Asia             0.647
		Geography.Regions.Asia.North Asia            0.182
		Geography.Regions.Asia.South Asia            0.853
		Geography.Regions.Asia.Southeast Asia        0.724
		Geography.Regions.Asia.West Asia             0.757
		Geography.Regions.Europe.Eastern Europe      0.718
		Geography.Regions.Europe.Europe*             0.722
		Geography.Regions.Europe.Northern Europe     0.676
		Geography.Regions.Europe.Southern Europe     0.676
		Geography.Regions.Europe.Western Europe      0.618
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.299
		History and Society.Education                0.359
		History and Society.History                  0.3
		History and Society.Military and warfare     0.645
		History and Society.Politics and government  0.635
		History and Society.Society                  0.311
		History and Society.Transportation           0.83
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.379
		STEM.Computing                               0.232
		STEM.Earth and environment                   0.669
		STEM.Engineering                             0.581
		STEM.Libraries & Information                 0.215
		STEM.Mathematics                             0.406
		STEM.Medicine & Health                       0.57
		STEM.Physics                                 0.311
		STEM.STEM*                                   0.866
		STEM.Space                                   0.897
		STEM.Technology                              0.273
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object'}

