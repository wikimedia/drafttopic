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
	counts (n=63880):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16539  -->  14614  1925  1215  46126
			'Culture.Biography.Women'                       4162  -->   3177   985   807  58911
			'Culture.Food and drink'                        1301  -->    889   412    73  62506
			'Culture.Internet culture'                      2969  -->   2293   676   195  60716
			'Culture.Linguistics'                           1367  -->   1017   350    97  62416
			'Culture.Literature'                            5298  -->   3929  1369   430  58152
			'Culture.Media.Books'                           1906  -->   1356   550   206  61768
			'Culture.Media.Entertainment'                   1825  -->    928   897   186  61869
			'Culture.Media.Films'                           2347  -->   1930   417   147  61386
			'Culture.Media.Media*'                         14457  -->  12395  2062  1470  47953
			'Culture.Media.Music'                           2665  -->   2141   524   299  60916
			'Culture.Media.Radio'                           1191  -->    960   231    28  62661
			'Culture.Media.Software'                        1784  -->   1037   747   354  61742
			'Culture.Media.Television'                      2224  -->   1686   538   173  61483
			'Culture.Media.Video games'                     2114  -->   1903   211    40  61726
			'Culture.Performing arts'                       1324  -->    877   447    93  62463
			'Culture.Philosophy and religion'               2712  -->   1568  1144   323  60845
			'Culture.Sports'                                5901  -->   5321   580   302  57677
			'Culture.Visual arts.Architecture'              2571  -->   1896   675   248  61061
			'Culture.Visual arts.Comics and Anime'          1509  -->   1216   293   100  62271
			'Culture.Visual arts.Fashion'                   1173  -->    814   359    48  62659
			'Culture.Visual arts.Visual arts*'              5989  -->   4582  1407   517  57374
			'Geography.Geographical'                        3518  -->   2293  1225   283  60079
			'Geography.Regions.Africa.Africa*'              6484  -->   5680   804   356  57040
			'Geography.Regions.Africa.Central Africa'       1155  -->    901   254    40  62685
			'Geography.Regions.Africa.Eastern Africa'       1100  -->    903   197    34  62746
			'Geography.Regions.Africa.Northern Africa'      1309  -->    984   325    85  62486
			'Geography.Regions.Africa.Southern Africa'      1260  -->   1001   259    53  62567
			'Geography.Regions.Africa.Western Africa'       1151  -->    966   185    70  62659
			'Geography.Regions.Americas.Central America'    1302  -->    933   369    80  62498
			'Geography.Regions.Americas.North America'      7482  -->   5319  2163  1318  55080
			'Geography.Regions.Americas.South America'      1575  -->   1180   395   115  62190
			'Geography.Regions.Asia.Asia*'                 11206  -->   9669  1537   833  51841
			'Geography.Regions.Asia.Central Asia'           1133  -->    890   243    39  62708
			'Geography.Regions.Asia.East Asia'              2749  -->   2094   655   261  60870
			'Geography.Regions.Asia.North Asia'             1369  -->    928   441   170  62341
			'Geography.Regions.Asia.South Asia'             2428  -->   2094   334   120  61332
			'Geography.Regions.Asia.Southeast Asia'         1726  -->   1363   363   103  62051
			'Geography.Regions.Asia.West Asia'              2301  -->   1880   421   131  61448
			'Geography.Regions.Europe.Eastern Europe'       3088  -->   2463   625   290  60502
			'Geography.Regions.Europe.Europe*'             12265  -->   9577  2688  1745  49870
			'Geography.Regions.Europe.Northern Europe'      4099  -->   2852  1247   629  59152
			'Geography.Regions.Europe.Southern Europe'      2397  -->   1713   684   296  61187
			'Geography.Regions.Europe.Western Europe'       3062  -->   2144   918   465  60353
			'Geography.Regions.Oceania'                     2535  -->   2112   423   141  61204
			'History and Society.Business and economics'    3458  -->   1650  1808   545  59877
			'History and Society.Education'                 2204  -->   1092  1112   238  61438
			'History and Society.History'                   3307  -->   1379  1928   504  60069
			'History and Society.Military and warfare'      4048  -->   2899  1149   385  59447
			'History and Society.Politics and government'   4604  -->   2919  1685   445  58831
			'History and Society.Society'                   4009  -->   1652  2357   393  59478
			'History and Society.Transportation'            3601  -->   3113   488   198  60081
			'STEM.Biology'                                  2951  -->   2407   544   133  60796
			'STEM.Chemistry'                                1319  -->    942   377   139  62422
			'STEM.Computing'                                2102  -->   1395   707   404  61374
			'STEM.Earth and environment'                    1619  -->   1155   464   102  62159
			'STEM.Engineering'                              2361  -->   1709   652   185  61334
			'STEM.Libraries & Information'                  1165  -->    692   473    75  62640
			'STEM.Mathematics'                              1136  -->    764   372    70  62674
			'STEM.Medicine & Health'                        1784  -->   1199   585   179  61917
			'STEM.Physics'                                  1173  -->    749   424   136  62571
			'STEM.STEM*'                                   16613  -->  14492  2121  1053  46214
			'STEM.Space'                                    1412  -->   1226   186    48  62420
			'STEM.Technology'                               3691  -->   2296  1395   616  59573
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.259         0.123
		Culture.Biography.Women                         0.065         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.046         0.003
		Culture.Linguistics                             0.021         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.226         0.058
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.092         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.055         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.02          0.003
		Geography.Regions.Americas.North America        0.117         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.175         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.021         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.048         0.013
		Geography.Regions.Europe.Europe*                0.192         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.048         0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.033         0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.037         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.018         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.02
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.068
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.091
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.014
		History and Society.Education                0.007
		History and Society.History                  0.013
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.025
		History and Society.Society                  0.012
		History and Society.Transportation           0.016
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.932
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.987
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.975
		History and Society.Society                  0.988
		History and Society.Transportation           0.984
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.783, macro=0.732):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.884
		Culture.Biography.Women                      0.763
		Culture.Food and drink                       0.683
		Culture.Internet culture                     0.772
		Culture.Linguistics                          0.744
		Culture.Literature                           0.742
		Culture.Media.Books                          0.711
		Culture.Media.Entertainment                  0.508
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.857
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.806
		Culture.Media.Software                       0.581
		Culture.Media.Television                     0.758
		Culture.Media.Video games                    0.9
		Culture.Performing arts                      0.662
		Culture.Philosophy and religion              0.578
		Culture.Sports                               0.902
		Culture.Visual arts.Architecture             0.737
		Culture.Visual arts.Comics and Anime         0.806
		Culture.Visual arts.Fashion                  0.694
		Culture.Visual arts.Visual arts*             0.765
		Geography.Geographical                       0.652
		Geography.Regions.Africa.Africa*             0.876
		Geography.Regions.Africa.Central Africa      0.78
		Geography.Regions.Africa.Eastern Africa      0.821
		Geography.Regions.Africa.Northern Africa     0.752
		Geography.Regions.Africa.Southern Africa     0.794
		Geography.Regions.Africa.Western Africa      0.839
		Geography.Regions.Americas.Central America   0.717
		Geography.Regions.Americas.North America     0.711
		Geography.Regions.Americas.South America     0.749
		Geography.Regions.Asia.Asia*                 0.863
		Geography.Regions.Asia.Central Asia          0.786
		Geography.Regions.Asia.East Asia             0.762
		Geography.Regions.Asia.North Asia            0.678
		Geography.Regions.Asia.South Asia            0.862
		Geography.Regions.Asia.Southeast Asia        0.79
		Geography.Regions.Asia.West Asia             0.817
		Geography.Regions.Europe.Eastern Europe      0.798
		Geography.Regions.Europe.Europe*             0.781
		Geography.Regions.Europe.Northern Europe     0.696
		Geography.Regions.Europe.Southern Europe     0.715
		Geography.Regions.Europe.Western Europe      0.7
		Geography.Regions.Oceania                    0.833
		History and Society.Business and economics   0.477
		History and Society.Education                0.495
		History and Society.History                  0.417
		History and Society.Military and warfare     0.716
		History and Society.Politics and government  0.634
		History and Society.Society                  0.412
		History and Society.Transportation           0.864
		STEM.Biology                                 0.816
		STEM.Chemistry                               0.714
		STEM.Computing                               0.664
		STEM.Earth and environment                   0.713
		STEM.Engineering                             0.724
		STEM.Libraries & Information                 0.594
		STEM.Mathematics                             0.673
		STEM.Medicine & Health                       0.672
		STEM.Physics                                 0.639
		STEM.STEM*                                   0.872
		STEM.Space                                   0.868
		STEM.Technology                              0.622
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.711, macro=0.581):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.829
		Culture.Biography.Women                      0.455
		Culture.Food and drink                       0.591
		Culture.Internet culture                     0.459
		Culture.Linguistics                          0.78
		Culture.Literature                           0.614
		Culture.Media.Books                          0.464
		Culture.Media.Entertainment                  0.379
		Culture.Media.Films                          0.785
		Culture.Media.Media*                         0.642
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.796
		Culture.Media.Software                       0.119
		Culture.Media.Television                     0.706
		Culture.Media.Video games                    0.784
		Culture.Performing arts                      0.563
		Culture.Philosophy and religion              0.541
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.661
		Culture.Visual arts.Comics and Anime         0.525
		Culture.Visual arts.Fashion                  0.423
		Culture.Visual arts.Visual arts*             0.615
		Geography.Geographical                       0.77
		Geography.Regions.Africa.Africa*             0.526
		Geography.Regions.Africa.Central Africa      0.436
		Geography.Regions.Africa.Eastern Africa      0.408
		Geography.Regions.Africa.Northern Africa     0.405
		Geography.Regions.Africa.Southern Africa     0.525
		Geography.Regions.Africa.Western Africa      0.34
		Geography.Regions.Americas.Central America   0.65
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.72
		Geography.Regions.Asia.Asia*                 0.722
		Geography.Regions.Asia.Central Asia          0.523
		Geography.Regions.Asia.East Asia             0.673
		Geography.Regions.Asia.North Asia            0.187
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.742
		Geography.Regions.Asia.West Asia             0.809
		Geography.Regions.Europe.Eastern Europe      0.685
		Geography.Regions.Europe.Europe*             0.656
		Geography.Regions.Europe.Northern Europe     0.676
		Geography.Regions.Europe.Southern Europe     0.662
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.848
		History and Society.Business and economics   0.35
		History and Society.Education                0.488
		History and Society.History                  0.354
		History and Society.Military and warfare     0.614
		History and Society.Politics and government  0.71
		History and Society.Society                  0.445
		History and Society.Transportation           0.801
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.334
		STEM.Computing                               0.215
		STEM.Earth and environment                   0.665
		STEM.Engineering                             0.559
		STEM.Libraries & Information                 0.236
		STEM.Mathematics                             0.201
		STEM.Medicine & Health                       0.6
		STEM.Physics                                 0.2
		STEM.STEM*                                   0.744
		STEM.Space                                   0.872
		STEM.Technology                              0.239
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.741, macro=0.632):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.855
		Culture.Biography.Women                      0.57
		Culture.Food and drink                       0.634
		Culture.Internet culture                     0.575
		Culture.Linguistics                          0.761
		Culture.Literature                           0.672
		Culture.Media.Books                          0.562
		Culture.Media.Entertainment                  0.434
		Culture.Media.Films                          0.803
		Culture.Media.Media*                         0.734
		Culture.Media.Music                          0.802
		Culture.Media.Radio                          0.801
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.731
		Culture.Media.Video games                    0.838
		Culture.Performing arts                      0.609
		Culture.Philosophy and religion              0.559
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.697
		Culture.Visual arts.Comics and Anime         0.636
		Culture.Visual arts.Fashion                  0.526
		Culture.Visual arts.Visual arts*             0.682
		Geography.Geographical                       0.706
		Geography.Regions.Africa.Africa*             0.657
		Geography.Regions.Africa.Central Africa      0.559
		Geography.Regions.Africa.Eastern Africa      0.545
		Geography.Regions.Africa.Northern Africa     0.526
		Geography.Regions.Africa.Southern Africa     0.632
		Geography.Regions.Africa.Western Africa      0.484
		Geography.Regions.Americas.Central America   0.682
		Geography.Regions.Americas.North America     0.693
		Geography.Regions.Americas.South America     0.735
		Geography.Regions.Asia.Asia*                 0.786
		Geography.Regions.Asia.Central Asia          0.628
		Geography.Regions.Asia.East Asia             0.715
		Geography.Regions.Asia.North Asia            0.294
		Geography.Regions.Asia.South Asia            0.867
		Geography.Regions.Asia.Southeast Asia        0.765
		Geography.Regions.Asia.West Asia             0.813
		Geography.Regions.Europe.Eastern Europe      0.737
		Geography.Regions.Europe.Europe*             0.713
		Geography.Regions.Europe.Northern Europe     0.686
		Geography.Regions.Europe.Southern Europe     0.687
		Geography.Regions.Europe.Western Europe      0.67
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.404
		History and Society.Education                0.491
		History and Society.History                  0.383
		History and Society.Military and warfare     0.661
		History and Society.Politics and government  0.67
		History and Society.Society                  0.428
		History and Society.Transportation           0.832
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.455
		STEM.Computing                               0.325
		STEM.Earth and environment                   0.688
		STEM.Engineering                             0.631
		STEM.Libraries & Information                 0.338
		STEM.Mathematics                             0.309
		STEM.Medicine & Health                       0.634
		STEM.Physics                                 0.305
		STEM.STEM*                                   0.803
		STEM.Space                                   0.87
		STEM.Technology                              0.345
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.982
		History and Society.Society                  0.986
		History and Society.Transportation           0.995
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.007
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.023
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.008
		History and Society.Society                  0.007
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.979
		Culture.Literature                           0.977
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.967
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.987
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.98
		Culture.Philosophy and religion              0.965
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.988
		Geography.Regions.Africa.Eastern Africa      0.987
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.984
		Geography.Regions.Africa.Western Africa      0.984
		Geography.Regions.Americas.Central America   0.982
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.984
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.988
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.983
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.957
		History and Society.Education                0.96
		History and Society.History                  0.945
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.964
		History and Society.Society                  0.927
		History and Society.Transportation           0.986
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.985
		STEM.Computing                               0.98
		STEM.Earth and environment                   0.978
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.975
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.977
		STEM.Space                                   0.989
		STEM.Technology                              0.97
		-------------------------------------------  -----
	pr_auc (micro=0.787, macro=0.654):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.902
		Culture.Biography.Women                      0.573
		Culture.Food and drink                       0.658
		Culture.Internet culture                     0.739
		Culture.Linguistics                          0.78
		Culture.Literature                           0.729
		Culture.Media.Books                          0.561
		Culture.Media.Entertainment                  0.454
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.846
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.848
		Culture.Media.Software                       0.175
		Culture.Media.Television                     0.772
		Culture.Media.Video games                    0.911
		Culture.Performing arts                      0.627
		Culture.Philosophy and religion              0.528
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.749
		Culture.Visual arts.Comics and Anime         0.705
		Culture.Visual arts.Fashion                  0.494
		Culture.Visual arts.Visual arts*             0.749
		Geography.Geographical                       0.757
		Geography.Regions.Africa.Africa*             0.739
		Geography.Regions.Africa.Central Africa      0.582
		Geography.Regions.Africa.Eastern Africa      0.426
		Geography.Regions.Africa.Northern Africa     0.522
		Geography.Regions.Africa.Southern Africa     0.61
		Geography.Regions.Africa.Western Africa      0.363
		Geography.Regions.Americas.Central America   0.646
		Geography.Regions.Americas.North America     0.762
		Geography.Regions.Americas.South America     0.768
		Geography.Regions.Asia.Asia*                 0.844
		Geography.Regions.Asia.Central Asia          0.677
		Geography.Regions.Asia.East Asia             0.716
		Geography.Regions.Asia.North Asia            0.276
		Geography.Regions.Asia.South Asia            0.884
		Geography.Regions.Asia.Southeast Asia        0.737
		Geography.Regions.Asia.West Asia             0.874
		Geography.Regions.Europe.Eastern Europe      0.784
		Geography.Regions.Europe.Europe*             0.771
		Geography.Regions.Europe.Northern Europe     0.723
		Geography.Regions.Europe.Southern Europe     0.717
		Geography.Regions.Europe.Western Europe      0.681
		Geography.Regions.Oceania                    0.86
		History and Society.Business and economics   0.342
		History and Society.Education                0.452
		History and Society.History                  0.335
		History and Society.Military and warfare     0.707
		History and Society.Politics and government  0.707
		History and Society.Society                  0.395
		History and Society.Transportation           0.852
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.44
		STEM.Computing                               0.307
		STEM.Earth and environment                   0.732
		STEM.Engineering                             0.659
		STEM.Libraries & Information                 0.338
		STEM.Mathematics                             0.335
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.377
		STEM.STEM*                                   0.897
		STEM.Space                                   0.914
		STEM.Technology                              0.38
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

