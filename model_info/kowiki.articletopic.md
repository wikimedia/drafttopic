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
	counts (n=60741):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15801  -->  14277  1524   795  44145
			'Culture.Biography.Women'                       4424  -->   3262  1162   461  55856
			'Culture.Food and drink'                        1776  -->   1367   409    78  58887
			'Culture.Internet culture'                      3463  -->   2738   725   233  57045
			'Culture.Linguistics'                           1688  -->   1146   542    92  58961
			'Culture.Literature'                            5858  -->   4319  1539   504  54379
			'Culture.Media.Books'                           1614  -->   1168   446   113  59014
			'Culture.Media.Entertainment'                   2343  -->   1227  1116   239  58159
			'Culture.Media.Films'                           2950  -->   2461   489   104  57687
			'Culture.Media.Media*'                         15181  -->  13007  2174  1513  44047
			'Culture.Media.Music'                           3247  -->   2578   669   278  57216
			'Culture.Media.Radio'                            702  -->    431   271    47  59992
			'Culture.Media.Software'                        2364  -->   1835   529   378  57999
			'Culture.Media.Television'                      2480  -->   1798   682   175  58086
			'Culture.Media.Video games'                     2305  -->   2026   279    84  58352
			'Culture.Performing arts'                       1527  -->    850   677   138  59076
			'Culture.Philosophy and religion'               3856  -->   2046  1810   328  56557
			'Culture.Sports'                                5207  -->   4494   713   164  55370
			'Culture.Visual arts.Architecture'              2141  -->   1424   717   209  58391
			'Culture.Visual arts.Comics and Anime'          2404  -->   2050   354   145  58192
			'Culture.Visual arts.Fashion'                   1355  -->    951   404    99  59287
			'Culture.Visual arts.Visual arts*'              6401  -->   4536  1865   552  53788
			'Geography.Geographical'                        3907  -->   2529  1378   535  56299
			'Geography.Regions.Africa.Africa*'              4310  -->   3221  1089   269  56162
			'Geography.Regions.Africa.Central Africa'        847  -->    612   235    46  59848
			'Geography.Regions.Africa.Eastern Africa'        475  -->    331   144    63  60203
			'Geography.Regions.Africa.Northern Africa'      1517  -->   1103   414    96  59128
			'Geography.Regions.Africa.Southern Africa'       690  -->    503   187    57  59994
			'Geography.Regions.Africa.Western Africa'        280  -->    192    88    65  60396
			'Geography.Regions.Americas.Central America'    1359  -->    870   489    53  59329
			'Geography.Regions.Americas.North America'      6585  -->   4547  2038  1165  52991
			'Geography.Regions.Americas.South America'      1532  -->   1119   413    91  59118
			'Geography.Regions.Asia.Asia*'                 15107  -->  12520  2587  1540  44094
			'Geography.Regions.Asia.Central Asia'           1328  -->    941   387   101  59312
			'Geography.Regions.Asia.East Asia'              7562  -->   6087  1475   833  52346
			'Geography.Regions.Asia.North Asia'             1823  -->   1358   465   205  58713
			'Geography.Regions.Asia.South Asia'             1867  -->   1431   436    78  58796
			'Geography.Regions.Asia.Southeast Asia'         1913  -->   1354   559    92  58736
			'Geography.Regions.Asia.West Asia'              2393  -->   1729   664   180  58168
			'Geography.Regions.Europe.Eastern Europe'       3409  -->   2586   823   323  57009
			'Geography.Regions.Europe.Europe*'             13405  -->  10872  2533  1627  45709
			'Geography.Regions.Europe.Northern Europe'      3936  -->   2821  1115   412  56393
			'Geography.Regions.Europe.Southern Europe'      3303  -->   2415   888   288  57150
			'Geography.Regions.Europe.Western Europe'       4084  -->   3062  1022   429  56228
			'Geography.Regions.Oceania'                     1829  -->   1360   469    58  58854
			'History and Society.Business and economics'    3915  -->   2138  1777   399  56427
			'History and Society.Education'                 1907  -->   1141   766   107  58727
			'History and Society.History'                   5526  -->   3204  2322   651  54564
			'History and Society.Military and warfare'      5276  -->   3578  1698   470  54995
			'History and Society.Politics and government'   5159  -->   2848  2311   527  55055
			'History and Society.Society'                   6675  -->   3101  3574   605  53461
			'History and Society.Transportation'            3768  -->   3254   514   184  56789
			'STEM.Biology'                                  3464  -->   2677   787   188  57089
			'STEM.Chemistry'                                1495  -->   1152   343   118  59128
			'STEM.Computing'                                2753  -->   2130   623   450  57538
			'STEM.Earth and environment'                    1903  -->   1237   666   142  58696
			'STEM.Engineering'                              2710  -->   1874   836   200  57831
			'STEM.Libraries & Information'                   753  -->    515   238    33  59955
			'STEM.Mathematics'                              1179  -->    878   301    69  59493
			'STEM.Medicine & Health'                        1993  -->   1266   727   185  58563
			'STEM.Physics'                                  1467  -->    941   526   188  59086
			'STEM.STEM*'                                   17902  -->  15696  2206  1102  41737
			'STEM.Space'                                    1703  -->   1508   195    36  59002
			'STEM.Technology'                               4764  -->   3341  1423   708  55269
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.26          0.123
		Culture.Biography.Women                         0.073         0.015
		Culture.Food and drink                          0.029         0.002
		Culture.Internet culture                        0.057         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.25          0.058
		Culture.Media.Music                             0.053         0.024
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.063         0.011
		Culture.Sports                                  0.086         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.064         0.024
		Geography.Regions.Africa.Africa*                0.071         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.108         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.249         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.124         0.011
		Geography.Regions.Asia.North Asia               0.03          0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.039         0.011
		Geography.Regions.Europe.Eastern Europe         0.056         0.013
		Geography.Regions.Europe.Europe*                0.221         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.054         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.091         0.011
		History and Society.Military and warfare        0.087         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.11          0.013
		History and Society.Transportation              0.062         0.015
		STEM.Biology                                    0.057         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.295         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.065
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.07
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.025
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.025
		History and Society.Society                  0.017
		History and Society.Transportation           0.016
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.935
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.93
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.975
		History and Society.Society                  0.983
		History and Society.Transportation           0.984
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.774, macro=0.721):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.904
		Culture.Biography.Women                      0.737
		Culture.Food and drink                       0.77
		Culture.Internet culture                     0.791
		Culture.Linguistics                          0.679
		Culture.Literature                           0.737
		Culture.Media.Books                          0.724
		Culture.Media.Entertainment                  0.524
		Culture.Media.Films                          0.834
		Culture.Media.Media*                         0.857
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.614
		Culture.Media.Software                       0.776
		Culture.Media.Television                     0.725
		Culture.Media.Video games                    0.879
		Culture.Performing arts                      0.557
		Culture.Philosophy and religion              0.531
		Culture.Sports                               0.863
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.853
		Culture.Visual arts.Fashion                  0.702
		Culture.Visual arts.Visual arts*             0.709
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.747
		Geography.Regions.Africa.Central Africa      0.723
		Geography.Regions.Africa.Eastern Africa      0.697
		Geography.Regions.Africa.Northern Africa     0.727
		Geography.Regions.Africa.Southern Africa     0.729
		Geography.Regions.Africa.Western Africa      0.686
		Geography.Regions.Americas.Central America   0.64
		Geography.Regions.Americas.North America     0.691
		Geography.Regions.Americas.South America     0.73
		Geography.Regions.Asia.Asia*                 0.829
		Geography.Regions.Asia.Central Asia          0.709
		Geography.Regions.Asia.East Asia             0.805
		Geography.Regions.Asia.North Asia            0.745
		Geography.Regions.Asia.South Asia            0.766
		Geography.Regions.Asia.Southeast Asia        0.708
		Geography.Regions.Asia.West Asia             0.723
		Geography.Regions.Europe.Eastern Europe      0.759
		Geography.Regions.Europe.Europe*             0.811
		Geography.Regions.Europe.Northern Europe     0.717
		Geography.Regions.Europe.Southern Europe     0.731
		Geography.Regions.Europe.Western Europe      0.75
		Geography.Regions.Oceania                    0.744
		History and Society.Business and economics   0.546
		History and Society.Education                0.598
		History and Society.History                  0.58
		History and Society.Military and warfare     0.678
		History and Society.Politics and government  0.552
		History and Society.Society                  0.465
		History and Society.Transportation           0.864
		STEM.Biology                                 0.773
		STEM.Chemistry                               0.771
		STEM.Computing                               0.774
		STEM.Earth and environment                   0.65
		STEM.Engineering                             0.692
		STEM.Libraries & Information                 0.684
		STEM.Mathematics                             0.745
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.641
		STEM.STEM*                                   0.877
		STEM.Space                                   0.885
		STEM.Technology                              0.701
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.699, macro=0.553):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.571
		Culture.Food and drink                       0.59
		Culture.Internet culture                     0.406
		Culture.Linguistics                          0.763
		Culture.Literature                           0.558
		Culture.Media.Books                          0.605
		Culture.Media.Entertainment                  0.315
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.616
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.629
		Culture.Media.Software                       0.138
		Culture.Media.Television                     0.682
		Culture.Media.Video games                    0.616
		Culture.Performing arts                      0.409
		Culture.Philosophy and religion              0.498
		Culture.Sports                               0.957
		Culture.Visual arts.Architecture             0.666
		Culture.Visual arts.Comics and Anime         0.43
		Culture.Visual arts.Fashion                  0.254
		Culture.Visual arts.Visual arts*             0.565
		Geography.Geographical                       0.624
		Geography.Regions.Africa.Africa*             0.552
		Geography.Regions.Africa.Central Africa      0.373
		Geography.Regions.Africa.Eastern Africa      0.233
		Geography.Regions.Africa.Northern Africa     0.355
		Geography.Regions.Africa.Southern Africa     0.475
		Geography.Regions.Africa.Western Africa      0.304
		Geography.Regions.Americas.Central America   0.704
		Geography.Regions.Americas.North America     0.688
		Geography.Regions.Americas.South America     0.751
		Geography.Regions.Asia.Asia*                 0.539
		Geography.Regions.Asia.Central Asia          0.265
		Geography.Regions.Asia.East Asia             0.372
		Geography.Regions.Asia.North Asia            0.165
		Geography.Regions.Asia.South Asia            0.899
		Geography.Regions.Asia.Southeast Asia        0.732
		Geography.Regions.Asia.West Asia             0.721
		Geography.Regions.Europe.Eastern Europe      0.636
		Geography.Regions.Europe.Europe*             0.66
		Geography.Regions.Europe.Northern Europe     0.757
		Geography.Regions.Europe.Southern Europe     0.658
		Geography.Regions.Europe.Western Europe      0.659
		Geography.Regions.Oceania                    0.921
		History and Society.Business and economics   0.442
		History and Society.Education                0.709
		History and Society.History                  0.35
		History and Society.Military and warfare     0.533
		History and Society.Politics and government  0.628
		History and Society.Society                  0.346
		History and Society.Transportation           0.804
		STEM.Biology                                 0.891
		STEM.Chemistry                               0.377
		STEM.Computing                               0.212
		STEM.Earth and environment                   0.551
		STEM.Engineering                             0.514
		STEM.Libraries & Information                 0.436
		STEM.Mathematics                             0.211
		STEM.Medicine & Health                       0.565
		STEM.Physics                                 0.147
		STEM.STEM*                                   0.717
		STEM.Space                                   0.898
		STEM.Technology                              0.222
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
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
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.727, macro=0.603):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.644
		Culture.Food and drink                       0.668
		Culture.Internet culture                     0.536
		Culture.Linguistics                          0.718
		Culture.Literature                           0.635
		Culture.Media.Books                          0.659
		Culture.Media.Entertainment                  0.393
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.717
		Culture.Media.Music                          0.797
		Culture.Media.Radio                          0.621
		Culture.Media.Software                       0.234
		Culture.Media.Television                     0.703
		Culture.Media.Video games                    0.724
		Culture.Performing arts                      0.471
		Culture.Philosophy and religion              0.514
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.572
		Culture.Visual arts.Fashion                  0.373
		Culture.Visual arts.Visual arts*             0.629
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.635
		Geography.Regions.Africa.Central Africa      0.492
		Geography.Regions.Africa.Eastern Africa      0.349
		Geography.Regions.Africa.Northern Africa     0.477
		Geography.Regions.Africa.Southern Africa     0.575
		Geography.Regions.Africa.Western Africa      0.421
		Geography.Regions.Americas.Central America   0.67
		Geography.Regions.Americas.North America     0.689
		Geography.Regions.Americas.South America     0.741
		Geography.Regions.Asia.Asia*                 0.653
		Geography.Regions.Asia.Central Asia          0.386
		Geography.Regions.Asia.East Asia             0.509
		Geography.Regions.Asia.North Asia            0.27
		Geography.Regions.Asia.South Asia            0.828
		Geography.Regions.Asia.Southeast Asia        0.72
		Geography.Regions.Asia.West Asia             0.722
		Geography.Regions.Europe.Eastern Europe      0.692
		Geography.Regions.Europe.Europe*             0.728
		Geography.Regions.Europe.Northern Europe     0.736
		Geography.Regions.Europe.Southern Europe     0.693
		Geography.Regions.Europe.Western Europe      0.702
		Geography.Regions.Oceania                    0.823
		History and Society.Business and economics   0.489
		History and Society.Education                0.649
		History and Society.History                  0.437
		History and Society.Military and warfare     0.597
		History and Society.Politics and government  0.588
		History and Society.Society                  0.397
		History and Society.Transportation           0.833
		STEM.Biology                                 0.828
		STEM.Chemistry                               0.506
		STEM.Computing                               0.333
		STEM.Earth and environment                   0.596
		STEM.Engineering                             0.589
		STEM.Libraries & Information                 0.532
		STEM.Mathematics                             0.329
		STEM.Medicine & Health                       0.598
		STEM.Physics                                 0.239
		STEM.STEM*                                   0.789
		STEM.Space                                   0.892
		STEM.Technology                              0.338
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.988
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.978
		History and Society.Society                  0.982
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.034
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.016
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.011
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.982
		Culture.Linguistics                          0.975
		Culture.Literature                           0.974
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.968
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.966
		Culture.Philosophy and religion              0.948
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.976
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.979
		Culture.Visual arts.Visual arts*             0.967
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.975
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.972
		Geography.Regions.Africa.Northern Africa     0.978
		Geography.Regions.Africa.Southern Africa     0.969
		Geography.Regions.Africa.Western Africa      0.952
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.979
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.979
		Geography.Regions.Asia.Southeast Asia        0.974
		Geography.Regions.Asia.West Asia             0.978
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.96
		History and Society.Education                0.971
		History and Society.History                  0.953
		History and Society.Military and warfare     0.97
		History and Society.Politics and government  0.95
		History and Society.Society                  0.925
		History and Society.Transportation           0.984
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.972
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.98
		STEM.STEM*                                   0.975
		STEM.Space                                   0.988
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.774, macro=0.615):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.944
		Culture.Biography.Women                      0.643
		Culture.Food and drink                       0.675
		Culture.Internet culture                     0.647
		Culture.Linguistics                          0.744
		Culture.Literature                           0.72
		Culture.Media.Books                          0.676
		Culture.Media.Entertainment                  0.381
		Culture.Media.Films                          0.83
		Culture.Media.Media*                         0.832
		Culture.Media.Music                          0.833
		Culture.Media.Radio                          0.479
		Culture.Media.Software                       0.25
		Culture.Media.Television                     0.708
		Culture.Media.Video games                    0.853
		Culture.Performing arts                      0.434
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.676
		Culture.Visual arts.Comics and Anime         0.621
		Culture.Visual arts.Fashion                  0.313
		Culture.Visual arts.Visual arts*             0.69
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.643
		Geography.Regions.Africa.Central Africa      0.358
		Geography.Regions.Africa.Eastern Africa      0.23
		Geography.Regions.Africa.Northern Africa     0.386
		Geography.Regions.Africa.Southern Africa     0.453
		Geography.Regions.Africa.Western Africa      0.247
		Geography.Regions.Americas.Central America   0.631
		Geography.Regions.Americas.North America     0.727
		Geography.Regions.Americas.South America     0.773
		Geography.Regions.Asia.Asia*                 0.748
		Geography.Regions.Asia.Central Asia          0.346
		Geography.Regions.Asia.East Asia             0.58
		Geography.Regions.Asia.North Asia            0.286
		Geography.Regions.Asia.South Asia            0.871
		Geography.Regions.Asia.Southeast Asia        0.741
		Geography.Regions.Asia.West Asia             0.739
		Geography.Regions.Europe.Eastern Europe      0.716
		Geography.Regions.Europe.Europe*             0.801
		Geography.Regions.Europe.Northern Europe     0.794
		Geography.Regions.Europe.Southern Europe     0.703
		Geography.Regions.Europe.Western Europe      0.735
		Geography.Regions.Oceania                    0.864
		History and Society.Business and economics   0.455
		History and Society.Education                0.644
		History and Society.History                  0.424
		History and Society.Military and warfare     0.64
		History and Society.Politics and government  0.622
		History and Society.Society                  0.376
		History and Society.Transportation           0.868
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.589
		STEM.Computing                               0.351
		STEM.Earth and environment                   0.557
		STEM.Engineering                             0.604
		STEM.Libraries & Information                 0.512
		STEM.Mathematics                             0.473
		STEM.Medicine & Health                       0.598
		STEM.Physics                                 0.166
		STEM.STEM*                                   0.877
		STEM.Space                                   0.917
		STEM.Technology                              0.364
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

