Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'min_samples_leaf': 1, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'init': None, 'subsample': 1.0, 'label_weights': {}, 'presort': 'deprecated', 'multilabel': True, 'min_samples_split': 2, 'n_estimators': 150, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'criterion': 'friedman_mse', 'warm_start': False, 'scale': False, 'ccp_alpha': 0.0, 'verbose': 0, 'validation_fraction': 0.1, 'population_rates': None, 'center': False, 'loss': 'deviance', 'max_depth': 5, 'random_state': None, 'tol': 0.0001, 'min_weight_fraction_leaf': 0.0, 'max_features': 'log2', 'learning_rate': 0.1}
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
	counts (n=63525):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 27188  -->  26047  1141  1271  35066
			'Culture.Biography.Women'                       6275  -->   4692  1583   769  56481
			'Culture.Food and drink'                        1416  -->    966   450    78  62031
			'Culture.Internet culture'                      3329  -->   2725   604   200  59996
			'Culture.Linguistics'                           1449  -->    961   488    89  61987
			'Culture.Literature'                            5787  -->   4291  1496   510  57228
			'Culture.Media.Books'                           1568  -->   1172   396   107  61850
			'Culture.Media.Entertainment'                   2144  -->   1054  1090   210  61171
			'Culture.Media.Films'                           2097  -->   1651   446   101  61327
			'Culture.Media.Media*'                         14069  -->  11743  2326  1479  47977
			'Culture.Media.Music'                           2793  -->   2123   670   303  60429
			'Culture.Media.Radio'                           1151  -->    599   552   113  62261
			'Culture.Media.Software'                        2061  -->   1580   481   301  61163
			'Culture.Media.Television'                      2333  -->   1398   935   192  61000
			'Culture.Media.Video games'                     2147  -->   1893   254    31  61347
			'Culture.Performing arts'                       1554  -->    799   755   129  61842
			'Culture.Philosophy and religion'               3422  -->   1739  1683   316  59787
			'Culture.Sports'                                8671  -->   7953   718   371  54483
			'Culture.Visual arts.Architecture'              1833  -->   1252   581   163  61529
			'Culture.Visual arts.Comics and Anime'          1863  -->   1505   358    81  61581
			'Culture.Visual arts.Fashion'                   1321  -->    988   333    80  62124
			'Culture.Visual arts.Visual arts*'              5894  -->   4272  1622   427  57204
			'Geography.Geographical'                        3582  -->   2539  1043   376  59567
			'Geography.Regions.Africa.Africa*'              6496  -->   5368  1128   453  56576
			'Geography.Regions.Africa.Central Africa'       1120  -->    630   490   125  62280
			'Geography.Regions.Africa.Eastern Africa'        981  -->    739   242    41  62503
			'Geography.Regions.Africa.Northern Africa'      2066  -->   1580   486   207  61252
			'Geography.Regions.Africa.Southern Africa'      1179  -->    921   258    50  62296
			'Geography.Regions.Africa.Western Africa'        744  -->    574   170    57  62724
			'Geography.Regions.Americas.Central America'    1380  -->    891   489    90  62055
			'Geography.Regions.Americas.North America'      8341  -->   5569  2772  2039  53145
			'Geography.Regions.Americas.South America'      1616  -->   1228   388   110  61799
			'Geography.Regions.Asia.Asia*'                 12017  -->   9930  2087   888  50620
			'Geography.Regions.Asia.Central Asia'           1200  -->    934   266    58  62267
			'Geography.Regions.Asia.East Asia'              2947  -->   2168   779   240  60338
			'Geography.Regions.Asia.North Asia'             1541  -->   1077   464   177  61807
			'Geography.Regions.Asia.South Asia'             1892  -->   1472   420    66  61567
			'Geography.Regions.Asia.Southeast Asia'         1620  -->   1218   402    50  61855
			'Geography.Regions.Asia.West Asia'              4084  -->   3324   760   329  59112
			'Geography.Regions.Europe.Eastern Europe'       2928  -->   2203   725   242  60355
			'Geography.Regions.Europe.Europe*'             13221  -->  10380  2841  1854  48450
			'Geography.Regions.Europe.Northern Europe'      4088  -->   2744  1344   623  58814
			'Geography.Regions.Europe.Southern Europe'      2937  -->   2197   740   304  60284
			'Geography.Regions.Europe.Western Europe'       4016  -->   2957  1059   475  59034
			'Geography.Regions.Oceania'                     2289  -->   1882   407    73  61163
			'History and Society.Business and economics'    3707  -->   2050  1657   423  59395
			'History and Society.Education'                 2041  -->    841  1200   194  61290
			'History and Society.History'                   4767  -->   2238  2529   668  58090
			'History and Society.Military and warfare'      4771  -->   3240  1531   438  58316
			'History and Society.Politics and government'   5513  -->   3396  2117   635  57377
			'History and Society.Society'                   6035  -->   2511  3524   540  56950
			'History and Society.Transportation'            3305  -->   2849   456   146  60074
			'STEM.Biology'                                  2960  -->   2310   650   202  60363
			'STEM.Chemistry'                                1521  -->   1148   373   137  61867
			'STEM.Computing'                                2413  -->   1880   533   335  60777
			'STEM.Earth and environment'                    1682  -->   1103   579   129  61714
			'STEM.Engineering'                              2964  -->   2162   802   237  60324
			'STEM.Libraries & Information'                  1198  -->    815   383    58  62269
			'STEM.Mathematics'                              1168  -->    909   259    55  62302
			'STEM.Medicine & Health'                        2266  -->   1602   664   197  61062
			'STEM.Physics'                                  1472  -->   1017   455   175  61878
			'STEM.STEM*'                                   18018  -->  15740  2278  1047  44460
			'STEM.Space'                                    1751  -->   1545   206    66  61708
			'STEM.Technology'                               4452  -->   3228  1224   583  58490
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.428         0.123
		Culture.Biography.Women                         0.099         0.015
		Culture.Food and drink                          0.022         0.002
		Culture.Internet culture                        0.052         0.003
		Culture.Linguistics                             0.023         0.007
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.025         0.004
		Culture.Media.Entertainment                     0.034         0.004
		Culture.Media.Films                             0.033         0.011
		Culture.Media.Media*                            0.221         0.058
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.034         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.136         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.029         0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0
		Geography.Regions.Africa.Northern Africa        0.033         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.131         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.189         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.064         0.011
		Geography.Regions.Europe.Eastern Europe         0.046         0.013
		Geography.Regions.Europe.Europe*                0.208         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.046         0.013
		Geography.Regions.Europe.Western Europe         0.063         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.058         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.075         0.014
		History and Society.Politics and government     0.087         0.028
		History and Society.Society                     0.095         0.013
		History and Society.Transportation              0.052         0.015
		STEM.Biology                                    0.047         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.038         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.047         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.284         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.149
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.072
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.077
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.028
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
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
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.851
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.923
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.972
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
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
	recall (micro=0.78, macro=0.72):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.958
		Culture.Biography.Women                      0.748
		Culture.Food and drink                       0.682
		Culture.Internet culture                     0.819
		Culture.Linguistics                          0.663
		Culture.Literature                           0.741
		Culture.Media.Books                          0.747
		Culture.Media.Entertainment                  0.492
		Culture.Media.Films                          0.787
		Culture.Media.Media*                         0.835
		Culture.Media.Music                          0.76
		Culture.Media.Radio                          0.52
		Culture.Media.Software                       0.767
		Culture.Media.Television                     0.599
		Culture.Media.Video games                    0.882
		Culture.Performing arts                      0.514
		Culture.Philosophy and religion              0.508
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.808
		Culture.Visual arts.Fashion                  0.748
		Culture.Visual arts.Visual arts*             0.725
		Geography.Geographical                       0.709
		Geography.Regions.Africa.Africa*             0.826
		Geography.Regions.Africa.Central Africa      0.562
		Geography.Regions.Africa.Eastern Africa      0.753
		Geography.Regions.Africa.Northern Africa     0.765
		Geography.Regions.Africa.Southern Africa     0.781
		Geography.Regions.Africa.Western Africa      0.772
		Geography.Regions.Americas.Central America   0.646
		Geography.Regions.Americas.North America     0.668
		Geography.Regions.Americas.South America     0.76
		Geography.Regions.Asia.Asia*                 0.826
		Geography.Regions.Asia.Central Asia          0.778
		Geography.Regions.Asia.East Asia             0.736
		Geography.Regions.Asia.North Asia            0.699
		Geography.Regions.Asia.South Asia            0.778
		Geography.Regions.Asia.Southeast Asia        0.752
		Geography.Regions.Asia.West Asia             0.814
		Geography.Regions.Europe.Eastern Europe      0.752
		Geography.Regions.Europe.Europe*             0.785
		Geography.Regions.Europe.Northern Europe     0.671
		Geography.Regions.Europe.Southern Europe     0.748
		Geography.Regions.Europe.Western Europe      0.736
		Geography.Regions.Oceania                    0.822
		History and Society.Business and economics   0.553
		History and Society.Education                0.412
		History and Society.History                  0.469
		History and Society.Military and warfare     0.679
		History and Society.Politics and government  0.616
		History and Society.Society                  0.416
		History and Society.Transportation           0.862
		STEM.Biology                                 0.78
		STEM.Chemistry                               0.755
		STEM.Computing                               0.779
		STEM.Earth and environment                   0.656
		STEM.Engineering                             0.729
		STEM.Libraries & Information                 0.68
		STEM.Mathematics                             0.778
		STEM.Medicine & Health                       0.707
		STEM.Physics                                 0.691
		STEM.STEM*                                   0.874
		STEM.Space                                   0.882
		STEM.Technology                              0.725
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.687, macro=0.558):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.794
		Culture.Biography.Women                      0.451
		Culture.Food and drink                       0.573
		Culture.Internet culture                     0.464
		Culture.Linguistics                          0.773
		Culture.Literature                           0.569
		Culture.Media.Books                          0.636
		Culture.Media.Entertainment                  0.341
		Culture.Media.Films                          0.836
		Culture.Media.Media*                         0.634
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.383
		Culture.Media.Software                       0.172
		Culture.Media.Television                     0.629
		Culture.Media.Video games                    0.82
		Culture.Performing arts                      0.417
		Culture.Philosophy and religion              0.51
		Culture.Sports                               0.912
		Culture.Visual arts.Architecture             0.734
		Culture.Visual arts.Comics and Anime         0.575
		Culture.Visual arts.Fashion                  0.32
		Culture.Visual arts.Visual arts*             0.646
		Geography.Geographical                       0.732
		Geography.Regions.Africa.Africa*             0.45
		Geography.Regions.Africa.Central Africa      0.151
		Geography.Regions.Africa.Eastern Africa      0.343
		Geography.Regions.Africa.Northern Africa     0.218
		Geography.Regions.Africa.Southern Africa     0.534
		Geography.Regions.Africa.Western Africa      0.367
		Geography.Regions.Americas.Central America   0.596
		Geography.Regions.Americas.North America     0.554
		Geography.Regions.Americas.South America     0.731
		Geography.Regions.Asia.Asia*                 0.696
		Geography.Regions.Asia.Central Asia          0.42
		Geography.Regions.Asia.East Asia             0.682
		Geography.Regions.Asia.North Asia            0.185
		Geography.Regions.Asia.South Asia            0.918
		Geography.Regions.Asia.Southeast Asia        0.849
		Geography.Regions.Asia.West Asia             0.618
		Geography.Regions.Europe.Eastern Europe      0.71
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.669
		Geography.Regions.Europe.Southern Europe     0.663
		Geography.Regions.Europe.Western Europe      0.643
		Geography.Regions.Oceania                    0.914
		History and Society.Business and economics   0.443
		History and Society.Education                0.492
		History and Society.History                  0.311
		History and Society.Military and warfare     0.565
		History and Society.Politics and government  0.62
		History and Society.Society                  0.361
		History and Society.Transportation           0.845
		STEM.Biology                                 0.891
		STEM.Chemistry                               0.348
		STEM.Computing                               0.277
		STEM.Earth and environment                   0.589
		STEM.Engineering                             0.495
		STEM.Libraries & Information                 0.312
		STEM.Mathematics                             0.269
		STEM.Medicine & Health                       0.586
		STEM.Physics                                 0.172
		STEM.STEM*                                   0.738
		STEM.Space                                   0.833
		STEM.Technology                              0.275
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.994
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.725, macro=0.609):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.563
		Culture.Food and drink                       0.623
		Culture.Internet culture                     0.592
		Culture.Linguistics                          0.714
		Culture.Literature                           0.644
		Culture.Media.Books                          0.687
		Culture.Media.Entertainment                  0.402
		Culture.Media.Films                          0.811
		Culture.Media.Media*                         0.721
		Culture.Media.Music                          0.774
		Culture.Media.Radio                          0.441
		Culture.Media.Software                       0.281
		Culture.Media.Television                     0.614
		Culture.Media.Video games                    0.85
		Culture.Performing arts                      0.46
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.708
		Culture.Visual arts.Comics and Anime         0.672
		Culture.Visual arts.Fashion                  0.448
		Culture.Visual arts.Visual arts*             0.683
		Geography.Geographical                       0.72
		Geography.Regions.Africa.Africa*             0.583
		Geography.Regions.Africa.Central Africa      0.238
		Geography.Regions.Africa.Eastern Africa      0.472
		Geography.Regions.Africa.Northern Africa     0.339
		Geography.Regions.Africa.Southern Africa     0.634
		Geography.Regions.Africa.Western Africa      0.498
		Geography.Regions.Americas.Central America   0.62
		Geography.Regions.Americas.North America     0.605
		Geography.Regions.Americas.South America     0.745
		Geography.Regions.Asia.Asia*                 0.755
		Geography.Regions.Asia.Central Asia          0.546
		Geography.Regions.Asia.East Asia             0.708
		Geography.Regions.Asia.North Asia            0.292
		Geography.Regions.Asia.South Asia            0.842
		Geography.Regions.Asia.Southeast Asia        0.797
		Geography.Regions.Asia.West Asia             0.703
		Geography.Regions.Europe.Eastern Europe      0.731
		Geography.Regions.Europe.Europe*             0.703
		Geography.Regions.Europe.Northern Europe     0.67
		Geography.Regions.Europe.Southern Europe     0.703
		Geography.Regions.Europe.Western Europe      0.687
		Geography.Regions.Oceania                    0.866
		History and Society.Business and economics   0.492
		History and Society.Education                0.448
		History and Society.History                  0.374
		History and Society.Military and warfare     0.617
		History and Society.Politics and government  0.618
		History and Society.Society                  0.387
		History and Society.Transportation           0.853
		STEM.Biology                                 0.832
		STEM.Chemistry                               0.476
		STEM.Computing                               0.409
		STEM.Earth and environment                   0.621
		STEM.Engineering                             0.59
		STEM.Libraries & Information                 0.428
		STEM.Mathematics                             0.4
		STEM.Medicine & Health                       0.641
		STEM.Physics                                 0.276
		STEM.STEM*                                   0.8
		STEM.Space                                   0.857
		STEM.Technology                              0.398
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.979
		History and Society.Society                  0.983
		History and Society.Transportation           0.996
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.035
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.037
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.006
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.011
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.974, macro=0.976):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.976
		Culture.Literature                           0.977
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.97
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.977
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.953
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.98
		Geography.Regions.Africa.Central Africa      0.979
		Geography.Regions.Africa.Eastern Africa      0.985
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.979
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.974
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.981
		Geography.Regions.Asia.Southeast Asia        0.979
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.982
		History and Society.Business and economics   0.959
		History and Society.Education                0.955
		History and Society.History                  0.944
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.959
		History and Society.Society                  0.922
		History and Society.Transportation           0.985
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.987
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.979
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.978
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.977
		STEM.Space                                   0.99
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.772, macro=0.627):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.943
		Culture.Biography.Women                      0.566
		Culture.Food and drink                       0.66
		Culture.Internet culture                     0.743
		Culture.Linguistics                          0.748
		Culture.Literature                           0.708
		Culture.Media.Books                          0.738
		Culture.Media.Entertainment                  0.402
		Culture.Media.Films                          0.823
		Culture.Media.Media*                         0.815
		Culture.Media.Music                          0.809
		Culture.Media.Radio                          0.324
		Culture.Media.Software                       0.263
		Culture.Media.Television                     0.657
		Culture.Media.Video games                    0.898
		Culture.Performing arts                      0.424
		Culture.Philosophy and religion              0.461
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.753
		Culture.Visual arts.Comics and Anime         0.72
		Culture.Visual arts.Fashion                  0.458
		Culture.Visual arts.Visual arts*             0.728
		Geography.Geographical                       0.774
		Geography.Regions.Africa.Africa*             0.587
		Geography.Regions.Africa.Central Africa      0.156
		Geography.Regions.Africa.Eastern Africa      0.404
		Geography.Regions.Africa.Northern Africa     0.355
		Geography.Regions.Africa.Southern Africa     0.576
		Geography.Regions.Africa.Western Africa      0.407
		Geography.Regions.Americas.Central America   0.578
		Geography.Regions.Americas.North America     0.64
		Geography.Regions.Americas.South America     0.685
		Geography.Regions.Asia.Asia*                 0.831
		Geography.Regions.Asia.Central Asia          0.503
		Geography.Regions.Asia.East Asia             0.742
		Geography.Regions.Asia.North Asia            0.246
		Geography.Regions.Asia.South Asia            0.89
		Geography.Regions.Asia.Southeast Asia        0.786
		Geography.Regions.Asia.West Asia             0.755
		Geography.Regions.Europe.Eastern Europe      0.755
		Geography.Regions.Europe.Europe*             0.761
		Geography.Regions.Europe.Northern Europe     0.716
		Geography.Regions.Europe.Southern Europe     0.727
		Geography.Regions.Europe.Western Europe      0.705
		Geography.Regions.Oceania                    0.886
		History and Society.Business and economics   0.458
		History and Society.Education                0.426
		History and Society.History                  0.333
		History and Society.Military and warfare     0.658
		History and Society.Politics and government  0.665
		History and Society.Society                  0.335
		History and Society.Transportation           0.898
		STEM.Biology                                 0.893
		STEM.Chemistry                               0.52
		STEM.Computing                               0.429
		STEM.Earth and environment                   0.616
		STEM.Engineering                             0.694
		STEM.Libraries & Information                 0.412
		STEM.Mathematics                             0.48
		STEM.Medicine & Health                       0.695
		STEM.Physics                                 0.268
		STEM.STEM*                                   0.898
		STEM.Space                                   0.913
		STEM.Technology                              0.468
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

