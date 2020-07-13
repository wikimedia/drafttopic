Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'learning_rate': 0.1, 'warm_start': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'population_rates': None, 'init': None, 'criterion': 'friedman_mse', 'n_estimators': 150, 'label_weights': {}, 'n_iter_no_change': None, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'random_state': None, 'subsample': 1.0, 'min_samples_split': 2, 'tol': 0.0001, 'multilabel': True, 'min_samples_leaf': 1, 'loss': 'deviance', 'center': False, 'min_weight_fraction_leaf': 0.0, 'max_depth': 5, 'max_features': 'log2', 'min_impurity_split': None, 'presort': 'auto', 'scale': False, 'validation_fraction': 0.1, 'verbose': 0}
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
	counts (n=59866):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14397  -->  12567  1830   799  44670
			'Culture.Biography.Women'                       5043  -->   3858  1185   850  53973
			'Culture.Food and drink'                        1376  -->    854   522   136  58354
			'Culture.Internet culture'                      3458  -->   2645   813   285  56123
			'Culture.Linguistics'                           1483  -->   1086   397    87  58296
			'Culture.Literature'                            5328  -->   3882  1446   541  53997
			'Culture.Media.Books'                           1383  -->    869   514   146  58337
			'Culture.Media.Entertainment'                   1879  -->    728  1151   186  57801
			'Culture.Media.Films'                           2561  -->   1869   692   169  57136
			'Culture.Media.Media*'                         12945  -->  10755  2190  1517  45404
			'Culture.Media.Music'                           2781  -->   2223   558   223  56862
			'Culture.Media.Radio'                            289  -->    184   105    40  59537
			'Culture.Media.Software'                        2227  -->   1630   597   304  57335
			'Culture.Media.Television'                      1972  -->   1260   712   174  57720
			'Culture.Media.Video games'                     2134  -->   1870   264    80  57652
			'Culture.Performing arts'                       1379  -->    862   517   133  58354
			'Culture.Philosophy and religion'               2938  -->   1370  1568   271  56657
			'Culture.Sports'                                4082  -->   3547   535   159  55625
			'Culture.Visual arts.Architecture'              1813  -->   1262   551   183  57870
			'Culture.Visual arts.Comics and Anime'          2143  -->   1748   395   121  57602
			'Culture.Visual arts.Fashion'                   1500  -->   1149   351   121  58245
			'Culture.Visual arts.Visual arts*'              5972  -->   4246  1726   481  53413
			'Geography.Geographical'                        3887  -->   2471  1416   551  55428
			'Geography.Regions.Africa.Africa*'              5671  -->   2472  3199   723  53472
			'Geography.Regions.Africa.Central Africa'       1196  -->    232   964   100  58570
			'Geography.Regions.Africa.Eastern Africa'        428  -->    112   316    51  59387
			'Geography.Regions.Africa.Northern Africa'      1455  -->    602   853    87  58324
			'Geography.Regions.Africa.Southern Africa'      1174  -->    479   695    80  58612
			'Geography.Regions.Africa.Western Africa'        665  -->    286   379    87  59114
			'Geography.Regions.Americas.Central America'    1592  -->    202  1390    53  58221
			'Geography.Regions.Americas.North America'      5331  -->   1748  3583   247  54288
			'Geography.Regions.Americas.South America'      2180  -->    784  1396   166  57520
			'Geography.Regions.Asia.Asia*'                 14584  -->   7954  6630  1796  43486
			'Geography.Regions.Asia.Central Asia'           1052  -->    265   787    78  58736
			'Geography.Regions.Asia.East Asia'              5675  -->   2557  3118   443  53748
			'Geography.Regions.Asia.North Asia'             2535  -->    872  1663   102  57229
			'Geography.Regions.Asia.South Asia'             1962  -->    884  1078    73  57831
			'Geography.Regions.Asia.Southeast Asia'         2594  -->    381  2213   105  57167
			'Geography.Regions.Asia.West Asia'              2104  -->   1032  1072    96  57666
			'Geography.Regions.Europe.Eastern Europe'       4240  -->   1839  2401   149  55477
			'Geography.Regions.Europe.Europe*'             13157  -->   7125  6032  1448  45261
			'Geography.Regions.Europe.Northern Europe'      2797  -->    423  2374   123  56946
			'Geography.Regions.Europe.Southern Europe'      2706  -->   1209  1497    98  57062
			'Geography.Regions.Europe.Western Europe'       4003  -->   1759  2244   120  55743
			'Geography.Regions.Oceania'                     1704  -->    474  1230   182  57980
			'History and Society.Business and economics'    3264  -->   1801  1463   398  56204
			'History and Society.Education'                 1601  -->    832   769   121  58144
			'History and Society.History'                   4259  -->   1891  2368   638  54969
			'History and Society.Military and warfare'      4243  -->   2896  1347   415  55208
			'History and Society.Politics and government'   3147  -->   1334  1813   525  56194
			'History and Society.Society'                   4371  -->   1218  3153   269  55226
			'History and Society.Transportation'            3492  -->   3149   343   115  56259
			'STEM.Biology'                                  6713  -->   6049   664   175  52978
			'STEM.Chemistry'                                1401  -->    985   416   214  58251
			'STEM.Computing'                                2386  -->   1777   609   352  57128
			'STEM.Earth and environment'                    1690  -->   1051   639   175  58001
			'STEM.Engineering'                              2936  -->   2369   567   137  56793
			'STEM.Libraries & Information'                   483  -->    367   116    47  59336
			'STEM.Mathematics'                               907  -->    678   229    66  58893
			'STEM.Medicine & Health'                        1775  -->   1184   591   158  57933
			'STEM.Physics'                                  1358  -->    888   470   176  58332
			'STEM.STEM*'                                   19891  -->  17817  2074  1147  38828
			'STEM.Space'                                    1540  -->   1344   196    57  58269
			'STEM.Technology'                               4111  -->   2804  1307   618  55137
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.24          0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.089         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.031         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.216         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.049         0.01
		Culture.Sports                                  0.068         0.061
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.095         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.007
		Geography.Regions.Asia.Asia*                    0.244         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.095         0.012
		Geography.Regions.Asia.North Asia               0.042         0.006
		Geography.Regions.Asia.South Asia               0.033         0.017
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.071         0.018
		Geography.Regions.Europe.Europe*                0.22          0.082
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.045         0.014
		Geography.Regions.Europe.Western Europe         0.067         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.071         0.011
		History and Society.Military and warfare        0.071         0.015
		History and Society.Politics and government     0.053         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.112         0.035
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.332         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.046, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.121
		Culture.Biography.Women                      0.027
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.017
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.025
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.066
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.009
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.073
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.008
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.008
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.016
		History and Society.Society                  0.007
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.005
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.086
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.954, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.934
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.927
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.984
		History and Society.Society                  0.993
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.995
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.914
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.642, macro=0.58):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.765
		Culture.Food and drink                       0.621
		Culture.Internet culture                     0.765
		Culture.Linguistics                          0.732
		Culture.Literature                           0.729
		Culture.Media.Books                          0.628
		Culture.Media.Entertainment                  0.387
		Culture.Media.Films                          0.73
		Culture.Media.Media*                         0.831
		Culture.Media.Music                          0.799
		Culture.Media.Radio                          0.637
		Culture.Media.Software                       0.732
		Culture.Media.Television                     0.639
		Culture.Media.Video games                    0.876
		Culture.Performing arts                      0.625
		Culture.Philosophy and religion              0.466
		Culture.Sports                               0.869
		Culture.Visual arts.Architecture             0.696
		Culture.Visual arts.Comics and Anime         0.816
		Culture.Visual arts.Fashion                  0.766
		Culture.Visual arts.Visual arts*             0.711
		Geography.Geographical                       0.636
		Geography.Regions.Africa.Africa*             0.436
		Geography.Regions.Africa.Central Africa      0.194
		Geography.Regions.Africa.Eastern Africa      0.262
		Geography.Regions.Africa.Northern Africa     0.414
		Geography.Regions.Africa.Southern Africa     0.408
		Geography.Regions.Africa.Western Africa      0.43
		Geography.Regions.Americas.Central America   0.127
		Geography.Regions.Americas.North America     0.328
		Geography.Regions.Americas.South America     0.36
		Geography.Regions.Asia.Asia*                 0.545
		Geography.Regions.Asia.Central Asia          0.252
		Geography.Regions.Asia.East Asia             0.451
		Geography.Regions.Asia.North Asia            0.344
		Geography.Regions.Asia.South Asia            0.451
		Geography.Regions.Asia.Southeast Asia        0.147
		Geography.Regions.Asia.West Asia             0.49
		Geography.Regions.Europe.Eastern Europe      0.434
		Geography.Regions.Europe.Europe*             0.542
		Geography.Regions.Europe.Northern Europe     0.151
		Geography.Regions.Europe.Southern Europe     0.447
		Geography.Regions.Europe.Western Europe      0.439
		Geography.Regions.Oceania                    0.278
		History and Society.Business and economics   0.552
		History and Society.Education                0.52
		History and Society.History                  0.444
		History and Society.Military and warfare     0.683
		History and Society.Politics and government  0.424
		History and Society.Society                  0.279
		History and Society.Transportation           0.902
		STEM.Biology                                 0.901
		STEM.Chemistry                               0.703
		STEM.Computing                               0.745
		STEM.Earth and environment                   0.622
		STEM.Engineering                             0.807
		STEM.Libraries & Information                 0.76
		STEM.Mathematics                             0.748
		STEM.Medicine & Health                       0.667
		STEM.Physics                                 0.654
		STEM.STEM*                                   0.896
		STEM.Space                                   0.873
		STEM.Technology                              0.682
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.995
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.989
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.677, macro=0.515):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.431
		Culture.Food and drink                       0.408
		Culture.Internet culture                     0.364
		Culture.Linguistics                          0.801
		Culture.Literature                           0.528
		Culture.Media.Books                          0.524
		Culture.Media.Entertainment                  0.326
		Culture.Media.Films                          0.745
		Culture.Media.Media*                         0.601
		Culture.Media.Music                          0.816
		Culture.Media.Radio                          0.69
		Culture.Media.Software                       0.155
		Culture.Media.Television                     0.658
		Culture.Media.Video games                    0.651
		Culture.Performing arts                      0.459
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.709
		Culture.Visual arts.Comics and Anime         0.485
		Culture.Visual arts.Fashion                  0.251
		Culture.Visual arts.Visual arts*             0.597
		Geography.Geographical                       0.585
		Geography.Regions.Africa.Africa*             0.22
		Geography.Regions.Africa.Central Africa      0.075
		Geography.Regions.Africa.Eastern Africa      0.134
		Geography.Regions.Africa.Northern Africa     0.275
		Geography.Regions.Africa.Southern Africa     0.283
		Geography.Regions.Africa.Western Africa      0.181
		Geography.Regions.Americas.Central America   0.328
		Geography.Regions.Americas.North America     0.831
		Geography.Regions.Americas.South America     0.465
		Geography.Regions.Asia.Asia*                 0.435
		Geography.Regions.Asia.Central Asia          0.133
		Geography.Regions.Asia.East Asia             0.407
		Geography.Regions.Asia.North Asia            0.524
		Geography.Regions.Asia.South Asia            0.858
		Geography.Regions.Asia.Southeast Asia        0.337
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.753
		Geography.Regions.Europe.Europe*             0.608
		Geography.Regions.Europe.Northern Europe     0.679
		Geography.Regions.Europe.Southern Europe     0.786
		Geography.Regions.Europe.Western Europe      0.812
		Geography.Regions.Oceania                    0.6
		History and Society.Business and economics   0.438
		History and Society.Education                0.669
		History and Society.History                  0.301
		History and Society.Military and warfare     0.589
		History and Society.Politics and government  0.434
		History and Society.Society                  0.326
		History and Society.Transportation           0.881
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.247
		STEM.Computing                               0.258
		STEM.Earth and environment                   0.498
		STEM.Engineering                             0.662
		STEM.Libraries & Information                 0.399
		STEM.Mathematics                             0.238
		STEM.Medicine & Health                       0.616
		STEM.Physics                                 0.171
		STEM.STEM*                                   0.687
		STEM.Space                                   0.794
		STEM.Technology                              0.243
		-------------------------------------------  -----
	!precision (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.635, macro=0.514):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.551
		Culture.Food and drink                       0.492
		Culture.Internet culture                     0.493
		Culture.Linguistics                          0.765
		Culture.Literature                           0.612
		Culture.Media.Books                          0.572
		Culture.Media.Entertainment                  0.354
		Culture.Media.Films                          0.737
		Culture.Media.Media*                         0.698
		Culture.Media.Music                          0.807
		Culture.Media.Radio                          0.662
		Culture.Media.Software                       0.256
		Culture.Media.Television                     0.648
		Culture.Media.Video games                    0.747
		Culture.Performing arts                      0.53
		Culture.Philosophy and religion              0.487
		Culture.Sports                               0.909
		Culture.Visual arts.Architecture             0.702
		Culture.Visual arts.Comics and Anime         0.608
		Culture.Visual arts.Fashion                  0.378
		Culture.Visual arts.Visual arts*             0.649
		Geography.Geographical                       0.609
		Geography.Regions.Africa.Africa*             0.293
		Geography.Regions.Africa.Central Africa      0.108
		Geography.Regions.Africa.Eastern Africa      0.177
		Geography.Regions.Africa.Northern Africa     0.33
		Geography.Regions.Africa.Southern Africa     0.335
		Geography.Regions.Africa.Western Africa      0.254
		Geography.Regions.Americas.Central America   0.183
		Geography.Regions.Americas.North America     0.47
		Geography.Regions.Americas.South America     0.406
		Geography.Regions.Asia.Asia*                 0.484
		Geography.Regions.Asia.Central Asia          0.174
		Geography.Regions.Asia.East Asia             0.427
		Geography.Regions.Asia.North Asia            0.415
		Geography.Regions.Asia.South Asia            0.591
		Geography.Regions.Asia.Southeast Asia        0.205
		Geography.Regions.Asia.West Asia             0.602
		Geography.Regions.Europe.Eastern Europe      0.55
		Geography.Regions.Europe.Europe*             0.573
		Geography.Regions.Europe.Northern Europe     0.247
		Geography.Regions.Europe.Southern Europe     0.57
		Geography.Regions.Europe.Western Europe      0.57
		Geography.Regions.Oceania                    0.38
		History and Society.Business and economics   0.488
		History and Society.Education                0.585
		History and Society.History                  0.359
		History and Society.Military and warfare     0.633
		History and Society.Politics and government  0.429
		History and Society.Society                  0.301
		History and Society.Transportation           0.891
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.366
		STEM.Computing                               0.383
		STEM.Earth and environment                   0.553
		STEM.Engineering                             0.727
		STEM.Libraries & Information                 0.523
		STEM.Mathematics                             0.361
		STEM.Medicine & Health                       0.64
		STEM.Physics                                 0.271
		STEM.STEM*                                   0.777
		STEM.Space                                   0.832
		STEM.Technology                              0.359
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.982
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.934
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.981
		History and Society.Society                  0.989
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.005
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.04
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.031
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.011
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.029
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.949, macro=0.954):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.978
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.962
		Culture.Literature                           0.973
		Culture.Media.Books                          0.977
		Culture.Media.Entertainment                  0.957
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.944
		Culture.Media.Software                       0.982
		Culture.Media.Television                     0.975
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.977
		Culture.Philosophy and religion              0.937
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.975
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.98
		Culture.Visual arts.Visual arts*             0.964
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.928
		Geography.Regions.Africa.Central Africa      0.942
		Geography.Regions.Africa.Eastern Africa      0.899
		Geography.Regions.Africa.Northern Africa     0.933
		Geography.Regions.Africa.Southern Africa     0.95
		Geography.Regions.Africa.Western Africa      0.958
		Geography.Regions.Americas.Central America   0.908
		Geography.Regions.Americas.North America     0.903
		Geography.Regions.Americas.South America     0.932
		Geography.Regions.Asia.Asia*                 0.895
		Geography.Regions.Asia.Central Asia          0.936
		Geography.Regions.Asia.East Asia             0.928
		Geography.Regions.Asia.North Asia            0.929
		Geography.Regions.Asia.South Asia            0.92
		Geography.Regions.Asia.Southeast Asia        0.884
		Geography.Regions.Asia.West Asia             0.94
		Geography.Regions.Europe.Eastern Europe      0.928
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.896
		Geography.Regions.Europe.Southern Europe     0.927
		Geography.Regions.Europe.Western Europe      0.932
		Geography.Regions.Oceania                    0.905
		History and Society.Business and economics   0.959
		History and Society.Education                0.965
		History and Society.History                  0.937
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.948
		History and Society.Society                  0.891
		History and Society.Transportation           0.985
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.983
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.967
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.976
		STEM.Space                                   0.987
		STEM.Technology                              0.97
		-------------------------------------------  -----
	pr_auc (micro=0.671, macro=0.494):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.921
		Culture.Biography.Women                      0.535
		Culture.Food and drink                       0.448
		Culture.Internet culture                     0.605
		Culture.Linguistics                          0.742
		Culture.Literature                           0.655
		Culture.Media.Books                          0.511
		Culture.Media.Entertainment                  0.241
		Culture.Media.Films                          0.787
		Culture.Media.Media*                         0.786
		Culture.Media.Music                          0.834
		Culture.Media.Radio                          0.448
		Culture.Media.Software                       0.252
		Culture.Media.Television                     0.599
		Culture.Media.Video games                    0.819
		Culture.Performing arts                      0.454
		Culture.Philosophy and religion              0.417
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.7
		Culture.Visual arts.Comics and Anime         0.658
		Culture.Visual arts.Fashion                  0.308
		Culture.Visual arts.Visual arts*             0.673
		Geography.Geographical                       0.627
		Geography.Regions.Africa.Africa*             0.278
		Geography.Regions.Africa.Central Africa      0.037
		Geography.Regions.Africa.Eastern Africa      0.041
		Geography.Regions.Africa.Northern Africa     0.143
		Geography.Regions.Africa.Southern Africa     0.181
		Geography.Regions.Africa.Western Africa      0.118
		Geography.Regions.Americas.Central America   0.121
		Geography.Regions.Americas.North America     0.586
		Geography.Regions.Americas.South America     0.315
		Geography.Regions.Asia.Asia*                 0.528
		Geography.Regions.Asia.Central Asia          0.068
		Geography.Regions.Asia.East Asia             0.371
		Geography.Regions.Asia.North Asia            0.375
		Geography.Regions.Asia.South Asia            0.592
		Geography.Regions.Asia.Southeast Asia        0.152
		Geography.Regions.Asia.West Asia             0.575
		Geography.Regions.Europe.Eastern Europe      0.553
		Geography.Regions.Europe.Europe*             0.65
		Geography.Regions.Europe.Northern Europe     0.348
		Geography.Regions.Europe.Southern Europe     0.559
		Geography.Regions.Europe.Western Europe      0.594
		Geography.Regions.Oceania                    0.35
		History and Society.Business and economics   0.456
		History and Society.Education                0.551
		History and Society.History                  0.309
		History and Society.Military and warfare     0.688
		History and Society.Politics and government  0.381
		History and Society.Society                  0.226
		History and Society.Transportation           0.922
		STEM.Biology                                 0.949
		STEM.Chemistry                               0.331
		STEM.Computing                               0.392
		STEM.Earth and environment                   0.525
		STEM.Engineering                             0.757
		STEM.Libraries & Information                 0.374
		STEM.Mathematics                             0.328
		STEM.Medicine & Health                       0.644
		STEM.Physics                                 0.208
		STEM.STEM*                                   0.894
		STEM.Space                                   0.826
		STEM.Technology                              0.363
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'STEM.Space': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

