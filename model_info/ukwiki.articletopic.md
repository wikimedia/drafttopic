Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'verbose': 0, 'presort': 'deprecated', 'n_iter_no_change': None, 'multilabel': True, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'center': False, 'warm_start': False, 'min_samples_leaf': 1, 'loss': 'deviance', 'max_leaf_nodes': None, 'learning_rate': 0.1, 'random_state': None, 'label_weights': {}, 'subsample': 1.0, 'validation_fraction': 0.1, 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'min_weight_fraction_leaf': 0.0, 'min_samples_split': 2, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'n_estimators': 150, 'max_features': 'log2', 'population_rates': None, 'init': None, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.8.2'
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
	counts (n=61827):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15166  -->  13791  1375   861  45800
			'Culture.Biography.Women'                       3789  -->   2889   900   359  57679
			'Culture.Food and drink'                        1445  -->   1030   415    86  60296
			'Culture.Internet culture'                      3148  -->   2586   562   213  58466
			'Culture.Linguistics'                           1672  -->   1192   480   107  60048
			'Culture.Literature'                            5363  -->   4083  1280   516  55948
			'Culture.Media.Books'                           1832  -->   1430   402   147  59848
			'Culture.Media.Entertainment'                   2162  -->    930  1232   283  59382
			'Culture.Media.Films'                           2933  -->   2522   411   121  58773
			'Culture.Media.Media*'                         13712  -->  11856  1856  1274  46841
			'Culture.Media.Music'                           2739  -->   2204   535   207  58881
			'Culture.Media.Radio'                            468  -->    186   282    50  61309
			'Culture.Media.Software'                        2119  -->   1568   551   357  59351
			'Culture.Media.Television'                      1940  -->   1427   513   128  59759
			'Culture.Media.Video games'                     2071  -->   1868   203    55  59701
			'Culture.Performing arts'                       1433  -->    809   624   131  60263
			'Culture.Philosophy and religion'               3515  -->   1802  1713   370  57942
			'Culture.Sports'                                5614  -->   4968   646   182  56031
			'Culture.Visual arts.Architecture'              2163  -->   1497   666   246  59418
			'Culture.Visual arts.Comics and Anime'          1640  -->   1351   289    74  60113
			'Culture.Visual arts.Fashion'                   1229  -->    884   345    87  60511
			'Culture.Visual arts.Visual arts*'              5742  -->   4125  1617   466  55619
			'Geography.Geographical'                        4540  -->   3096  1444   605  56682
			'Geography.Regions.Africa.Africa*'              5072  -->   3795  1277   443  56312
			'Geography.Regions.Africa.Central Africa'       1164  -->    835   329    86  60577
			'Geography.Regions.Africa.Eastern Africa'        727  -->    541   186    44  61056
			'Geography.Regions.Africa.Northern Africa'      1422  -->    882   540   128  60277
			'Geography.Regions.Africa.Southern Africa'       905  -->    541   364    57  60865
			'Geography.Regions.Africa.Western Africa'        370  -->    215   155    46  61411
			'Geography.Regions.Americas.Central America'    1329  -->    788   541    77  60421
			'Geography.Regions.Americas.North America'      5433  -->   3333  2100   774  55620
			'Geography.Regions.Americas.South America'      1517  -->    998   519    91  60219
			'Geography.Regions.Asia.Asia*'                 12648  -->  10108  2540  1153  48026
			'Geography.Regions.Asia.Central Asia'           1310  -->    880   430    98  60419
			'Geography.Regions.Asia.East Asia'              2929  -->   2187   742   242  58656
			'Geography.Regions.Asia.North Asia'             3840  -->   2607  1233   493  57494
			'Geography.Regions.Asia.South Asia'             1742  -->   1282   460    68  60017
			'Geography.Regions.Asia.Southeast Asia'         1528  -->   1029   499    79  60220
			'Geography.Regions.Asia.West Asia'              2514  -->   1823   691   176  59137
			'Geography.Regions.Europe.Eastern Europe'       6703  -->   5086  1617   706  54418
			'Geography.Regions.Europe.Europe*'             17567  -->  13864  3703  2331  41929
			'Geography.Regions.Europe.Northern Europe'      3575  -->   2180  1395   387  57865
			'Geography.Regions.Europe.Southern Europe'      3636  -->   2526  1110   335  57856
			'Geography.Regions.Europe.Western Europe'       4437  -->   3195  1242   473  56917
			'Geography.Regions.Oceania'                     1810  -->   1267   543   119  59898
			'History and Society.Business and economics'    3639  -->   2090  1549   466  57722
			'History and Society.Education'                 1730  -->    892   838   151  59946
			'History and Society.History'                   5140  -->   2835  2305   718  55969
			'History and Society.Military and warfare'      4576  -->   3054  1522   543  56708
			'History and Society.Politics and government'   4178  -->   2243  1935   473  57176
			'History and Society.Society'                   3965  -->   1044  2921   253  57609
			'History and Society.Transportation'            3659  -->   3233   426   159  58009
			'STEM.Biology'                                  3859  -->   3183   676   189  57779
			'STEM.Chemistry'                                1465  -->   1023   442   190  60172
			'STEM.Computing'                                2683  -->   2099   584   433  58711
			'STEM.Earth and environment'                    1966  -->   1214   752   170  59691
			'STEM.Engineering'                              3036  -->   2298   738   226  58565
			'STEM.Libraries & Information'                  1052  -->    700   352    69  60706
			'STEM.Mathematics'                              1217  -->    897   320    91  60519
			'STEM.Medicine & Health'                        1842  -->   1218   624   173  59812
			'STEM.Physics'                                  1449  -->    937   512   205  60173
			'STEM.STEM*'                                   18828  -->  16748  2080  1108  41891
			'STEM.Space'                                    1841  -->   1627   214    62  59924
			'STEM.Technology'                               4780  -->   3320  1460   779  56268
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.245         0.12
		Culture.Biography.Women                         0.061         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.051         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.087         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.035         0.004
		Culture.Media.Films                             0.047         0.012
		Culture.Media.Media*                            0.222         0.055
		Culture.Media.Music                             0.044         0.021
		Culture.Media.Radio                             0.008         0.002
		Culture.Media.Software                          0.034         0.001
		Culture.Media.Television                        0.031         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.057         0.01
		Culture.Sports                                  0.091         0.06
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.02          0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.073         0.021
		Geography.Regions.Africa.Africa*                0.082         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.012         0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.015         0.001
		Geography.Regions.Africa.Western Africa         0.006         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.088         0.063
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.205         0.052
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.047         0.012
		Geography.Regions.Asia.North Asia               0.062         0.006
		Geography.Regions.Asia.South Asia               0.028         0.016
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.041         0.012
		Geography.Regions.Europe.Eastern Europe         0.108         0.018
		Geography.Regions.Europe.Europe*                0.284         0.081
		Geography.Regions.Europe.Northern Europe        0.058         0.029
		Geography.Regions.Europe.Southern Europe        0.059         0.014
		Geography.Regions.Europe.Western Europe         0.072         0.02
		Geography.Regions.Oceania                       0.029         0.016
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.028         0.008
		History and Society.History                     0.083         0.011
		History and Society.Military and warfare        0.074         0.015
		History and Society.Politics and government     0.068         0.028
		History and Society.Society                     0.064         0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.062         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.043         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.017         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.305         0.065
		STEM.Space                                      0.03          0.004
		STEM.Technology                                 0.077         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.072
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.064
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.012
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.026
		Geography.Regions.Europe.Europe*             0.112
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.014
		History and Society.Education                0.007
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.023
		History and Society.Society                  0.007
		History and Society.Transportation           0.017
		STEM.Biology                                 0.032
		STEM.Chemistry                               0.004
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.082
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.928
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.936
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.888
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.977
		History and Society.Society                  0.993
		History and Society.Transportation           0.983
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.996
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.918
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.763, macro=0.7):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.909
		Culture.Biography.Women                      0.762
		Culture.Food and drink                       0.713
		Culture.Internet culture                     0.821
		Culture.Linguistics                          0.713
		Culture.Literature                           0.761
		Culture.Media.Books                          0.781
		Culture.Media.Entertainment                  0.43
		Culture.Media.Films                          0.86
		Culture.Media.Media*                         0.865
		Culture.Media.Music                          0.805
		Culture.Media.Radio                          0.397
		Culture.Media.Software                       0.74
		Culture.Media.Television                     0.736
		Culture.Media.Video games                    0.902
		Culture.Performing arts                      0.565
		Culture.Philosophy and religion              0.513
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.692
		Culture.Visual arts.Comics and Anime         0.824
		Culture.Visual arts.Fashion                  0.719
		Culture.Visual arts.Visual arts*             0.718
		Geography.Geographical                       0.682
		Geography.Regions.Africa.Africa*             0.748
		Geography.Regions.Africa.Central Africa      0.717
		Geography.Regions.Africa.Eastern Africa      0.744
		Geography.Regions.Africa.Northern Africa     0.62
		Geography.Regions.Africa.Southern Africa     0.598
		Geography.Regions.Africa.Western Africa      0.581
		Geography.Regions.Americas.Central America   0.593
		Geography.Regions.Americas.North America     0.613
		Geography.Regions.Americas.South America     0.658
		Geography.Regions.Asia.Asia*                 0.799
		Geography.Regions.Asia.Central Asia          0.672
		Geography.Regions.Asia.East Asia             0.747
		Geography.Regions.Asia.North Asia            0.679
		Geography.Regions.Asia.South Asia            0.736
		Geography.Regions.Asia.Southeast Asia        0.673
		Geography.Regions.Asia.West Asia             0.725
		Geography.Regions.Europe.Eastern Europe      0.759
		Geography.Regions.Europe.Europe*             0.789
		Geography.Regions.Europe.Northern Europe     0.61
		Geography.Regions.Europe.Southern Europe     0.695
		Geography.Regions.Europe.Western Europe      0.72
		Geography.Regions.Oceania                    0.7
		History and Society.Business and economics   0.574
		History and Society.Education                0.516
		History and Society.History                  0.552
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.537
		History and Society.Society                  0.263
		History and Society.Transportation           0.884
		STEM.Biology                                 0.825
		STEM.Chemistry                               0.698
		STEM.Computing                               0.782
		STEM.Earth and environment                   0.617
		STEM.Engineering                             0.757
		STEM.Libraries & Information                 0.665
		STEM.Mathematics                             0.737
		STEM.Medicine & Health                       0.661
		STEM.Physics                                 0.647
		STEM.STEM*                                   0.89
		STEM.Space                                   0.884
		STEM.Technology                              0.695
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.992
		History and Society.Society                  0.996
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	precision (micro=0.696, macro=0.553):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.651
		Culture.Food and drink                       0.561
		Culture.Internet culture                     0.458
		Culture.Linguistics                          0.764
		Culture.Literature                           0.556
		Culture.Media.Books                          0.58
		Culture.Media.Entertainment                  0.264
		Culture.Media.Films                          0.83
		Culture.Media.Media*                         0.654
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.531
		Culture.Media.Software                       0.139
		Culture.Media.Television                     0.755
		Culture.Media.Video games                    0.74
		Culture.Performing arts                      0.443
		Culture.Philosophy and religion              0.458
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.646
		Culture.Visual arts.Comics and Anime         0.616
		Culture.Visual arts.Fashion                  0.31
		Culture.Visual arts.Visual arts*             0.614
		Geography.Geographical                       0.582
		Geography.Regions.Africa.Africa*             0.45
		Geography.Regions.Africa.Central Africa      0.262
		Geography.Regions.Africa.Eastern Africa      0.341
		Geography.Regions.Africa.Northern Africa     0.283
		Geography.Regions.Africa.Southern Africa     0.455
		Geography.Regions.Africa.Western Africa      0.366
		Geography.Regions.Americas.Central America   0.617
		Geography.Regions.Americas.North America     0.75
		Geography.Regions.Americas.South America     0.75
		Geography.Regions.Asia.Asia*                 0.654
		Geography.Regions.Asia.Central Asia          0.248
		Geography.Regions.Asia.East Asia             0.691
		Geography.Regions.Asia.North Asia            0.31
		Geography.Regions.Asia.South Asia            0.916
		Geography.Regions.Asia.Southeast Asia        0.763
		Geography.Regions.Asia.West Asia             0.743
		Geography.Regions.Europe.Eastern Europe      0.524
		Geography.Regions.Europe.Europe*             0.568
		Geography.Regions.Europe.Northern Europe     0.732
		Geography.Regions.Europe.Southern Europe     0.628
		Geography.Regions.Europe.Western Europe      0.646
		Geography.Regions.Oceania                    0.855
		History and Society.Business and economics   0.413
		History and Society.Education                0.621
		History and Society.History                  0.324
		History and Society.Military and warfare     0.522
		History and Society.Politics and government  0.653
		History and Society.Society                  0.334
		History and Society.Transportation           0.842
		STEM.Biology                                 0.9
		STEM.Chemistry                               0.273
		STEM.Computing                               0.232
		STEM.Earth and environment                   0.508
		STEM.Engineering                             0.532
		STEM.Libraries & Information                 0.286
		STEM.Mathematics                             0.185
		STEM.Medicine & Health                       0.597
		STEM.Physics                                 0.151
		STEM.STEM*                                   0.705
		STEM.Space                                   0.785
		STEM.Technology                              0.208
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
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.72, macro=0.597):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.703
		Culture.Food and drink                       0.628
		Culture.Internet culture                     0.588
		Culture.Linguistics                          0.738
		Culture.Literature                           0.643
		Culture.Media.Books                          0.665
		Culture.Media.Entertainment                  0.327
		Culture.Media.Films                          0.845
		Culture.Media.Media*                         0.745
		Culture.Media.Music                          0.818
		Culture.Media.Radio                          0.455
		Culture.Media.Software                       0.234
		Culture.Media.Television                     0.745
		Culture.Media.Video games                    0.813
		Culture.Performing arts                      0.496
		Culture.Philosophy and religion              0.484
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.705
		Culture.Visual arts.Fashion                  0.433
		Culture.Visual arts.Visual arts*             0.662
		Geography.Geographical                       0.628
		Geography.Regions.Africa.Africa*             0.562
		Geography.Regions.Africa.Central Africa      0.384
		Geography.Regions.Africa.Eastern Africa      0.468
		Geography.Regions.Africa.Northern Africa     0.389
		Geography.Regions.Africa.Southern Africa     0.517
		Geography.Regions.Africa.Western Africa      0.449
		Geography.Regions.Americas.Central America   0.605
		Geography.Regions.Americas.North America     0.675
		Geography.Regions.Americas.South America     0.701
		Geography.Regions.Asia.Asia*                 0.719
		Geography.Regions.Asia.Central Asia          0.362
		Geography.Regions.Asia.East Asia             0.718
		Geography.Regions.Asia.North Asia            0.426
		Geography.Regions.Asia.South Asia            0.816
		Geography.Regions.Asia.Southeast Asia        0.715
		Geography.Regions.Asia.West Asia             0.734
		Geography.Regions.Europe.Eastern Europe      0.62
		Geography.Regions.Europe.Europe*             0.661
		Geography.Regions.Europe.Northern Europe     0.665
		Geography.Regions.Europe.Southern Europe     0.659
		Geography.Regions.Europe.Western Europe      0.681
		Geography.Regions.Oceania                    0.77
		History and Society.Business and economics   0.48
		History and Society.Education                0.563
		History and Society.History                  0.408
		History and Society.Military and warfare     0.586
		History and Society.Politics and government  0.589
		History and Society.Society                  0.294
		History and Society.Transportation           0.862
		STEM.Biology                                 0.861
		STEM.Chemistry                               0.392
		STEM.Computing                               0.358
		STEM.Earth and environment                   0.557
		STEM.Engineering                             0.625
		STEM.Libraries & Information                 0.4
		STEM.Mathematics                             0.295
		STEM.Medicine & Health                       0.627
		STEM.Physics                                 0.245
		STEM.STEM*                                   0.787
		STEM.Space                                   0.831
		STEM.Technology                              0.32
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.99
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.935
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.99
		History and Society.Transportation           0.995
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.969
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.026
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.023
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.053
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.008
		History and Society.Society                  0.004
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.014
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.976
		Culture.Literature                           0.977
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.959
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.973
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.976
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.979
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.974
		Geography.Regions.Africa.Central Africa      0.984
		Geography.Regions.Africa.Eastern Africa      0.976
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.964
		Geography.Regions.Americas.Central America   0.974
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.971
		Geography.Regions.Asia.South Asia            0.981
		Geography.Regions.Asia.Southeast Asia        0.974
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.976
		Geography.Regions.Europe.Western Europe      0.973
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.963
		History and Society.Education                0.965
		History and Society.History                  0.951
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.951
		History and Society.Society                  0.9
		History and Society.Transportation           0.986
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.982
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.969
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.978
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.977
		STEM.Space                                   0.991
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.77, macro=0.611):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.944
		Culture.Biography.Women                      0.715
		Culture.Food and drink                       0.636
		Culture.Internet culture                     0.749
		Culture.Linguistics                          0.759
		Culture.Literature                           0.707
		Culture.Media.Books                          0.733
		Culture.Media.Entertainment                  0.256
		Culture.Media.Films                          0.888
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.841
		Culture.Media.Radio                          0.284
		Culture.Media.Software                       0.243
		Culture.Media.Television                     0.772
		Culture.Media.Video games                    0.876
		Culture.Performing arts                      0.473
		Culture.Philosophy and religion              0.427
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.7
		Culture.Visual arts.Fashion                  0.372
		Culture.Visual arts.Visual arts*             0.703
		Geography.Geographical                       0.669
		Geography.Regions.Africa.Africa*             0.614
		Geography.Regions.Africa.Central Africa      0.315
		Geography.Regions.Africa.Eastern Africa      0.487
		Geography.Regions.Africa.Northern Africa     0.327
		Geography.Regions.Africa.Southern Africa     0.39
		Geography.Regions.Africa.Western Africa      0.281
		Geography.Regions.Americas.Central America   0.592
		Geography.Regions.Americas.North America     0.744
		Geography.Regions.Americas.South America     0.73
		Geography.Regions.Asia.Asia*                 0.794
		Geography.Regions.Asia.Central Asia          0.33
		Geography.Regions.Asia.East Asia             0.771
		Geography.Regions.Asia.North Asia            0.436
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.705
		Geography.Regions.Asia.West Asia             0.769
		Geography.Regions.Europe.Eastern Europe      0.677
		Geography.Regions.Europe.Europe*             0.758
		Geography.Regions.Europe.Northern Europe     0.714
		Geography.Regions.Europe.Southern Europe     0.708
		Geography.Regions.Europe.Western Europe      0.723
		Geography.Regions.Oceania                    0.82
		History and Society.Business and economics   0.458
		History and Society.Education                0.558
		History and Society.History                  0.375
		History and Society.Military and warfare     0.626
		History and Society.Politics and government  0.61
		History and Society.Society                  0.238
		History and Society.Transportation           0.898
		STEM.Biology                                 0.9
		STEM.Chemistry                               0.429
		STEM.Computing                               0.357
		STEM.Earth and environment                   0.545
		STEM.Engineering                             0.713
		STEM.Libraries & Information                 0.343
		STEM.Mathematics                             0.338
		STEM.Medicine & Health                       0.596
		STEM.Physics                                 0.182
		STEM.STEM*                                   0.882
		STEM.Space                                   0.904
		STEM.Technology                              0.379
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

