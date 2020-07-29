Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'population_rates': None, 'learning_rate': 0.1, 'min_impurity_split': None, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'ccp_alpha': 0.0, 'random_state': None, 'multilabel': True, 'subsample': 1.0, 'init': None, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'presort': 'deprecated', 'min_samples_leaf': 1, 'n_estimators': 150, 'max_leaf_nodes': None, 'label_weights': {}, 'validation_fraction': 0.1, 'min_samples_split': 2, 'verbose': 0, 'tol': 0.0001, 'center': False, 'max_depth': 5, 'max_features': 'log2', 'warm_start': False}
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
	counts (n=53413):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15127  -->  13222  1905   872  37414
			'Culture.Biography.Women'                       4262  -->   2860  1402   490  48661
			'Culture.Food and drink'                        1593  -->   1160   433   111  51709
			'Culture.Internet culture'                      2207  -->   1758   449   156  51050
			'Culture.Linguistics'                           1569  -->   1009   560    81  51763
			'Culture.Literature'                            5002  -->   3514  1488   508  47903
			'Culture.Media.Books'                           1730  -->   1373   357   132  51551
			'Culture.Media.Entertainment'                   2007  -->    869  1138   143  51263
			'Culture.Media.Films'                           2857  -->   2414   443   133  50423
			'Culture.Media.Media*'                         12391  -->  10469  1922  1241  39781
			'Culture.Media.Music'                           3219  -->   2555   664   271  49923
			'Culture.Media.Radio'                            214  -->    155    59    20  53179
			'Culture.Media.Software'                        1880  -->   1689   191   183  51350
			'Culture.Media.Television'                      2100  -->   1608   492   104  51209
			'Culture.Media.Video games'                      698  -->    657    41    12  52703
			'Culture.Performing arts'                       1678  -->   1050   628   140  51595
			'Culture.Philosophy and religion'               3688  -->   1702  1986   336  49389
			'Culture.Sports'                                3158  -->   2515   643   120  50135
			'Culture.Visual arts.Architecture'              2415  -->   1782   633   270  50728
			'Culture.Visual arts.Comics and Anime'          1032  -->    852   180    51  52330
			'Culture.Visual arts.Fashion'                    832  -->    619   213    43  52538
			'Culture.Visual arts.Visual arts*'              5299  -->   3681  1618   485  47629
			'Geography.Geographical'                        4332  -->   2745  1587   548  48533
			'Geography.Regions.Africa.Africa*'              3138  -->   1682  1456   236  50039
			'Geography.Regions.Africa.Central Africa'        387  -->    228   159    34  52992
			'Geography.Regions.Africa.Eastern Africa'        211  -->    140    71    27  53175
			'Geography.Regions.Africa.Northern Africa'      1202  -->    675   527    85  52126
			'Geography.Regions.Africa.Southern Africa'       585  -->    450   135    28  52800
			'Geography.Regions.Africa.Western Africa'        140  -->     97    43    16  53257
			'Geography.Regions.Americas.Central America'    1074  -->    361   713    63  52276
			'Geography.Regions.Americas.North America'      5502  -->   3549  1953   784  47127
			'Geography.Regions.Americas.South America'      1603  -->   1198   405    84  51726
			'Geography.Regions.Asia.Asia*'                 13547  -->  10566  2981  1401  38465
			'Geography.Regions.Asia.Central Asia'            867  -->    453   414    76  52470
			'Geography.Regions.Asia.East Asia'              2421  -->   1790   631   133  50859
			'Geography.Regions.Asia.North Asia'             5048  -->   3800  1248   394  47971
			'Geography.Regions.Asia.South Asia'             1710  -->   1029   681    92  51611
			'Geography.Regions.Asia.Southeast Asia'         1102  -->    400   702    53  52258
			'Geography.Regions.Asia.West Asia'              4004  -->   2752  1252   412  48997
			'Geography.Regions.Europe.Eastern Europe'       6444  -->   4803  1641   522  46447
			'Geography.Regions.Europe.Europe*'             18698  -->  15116  3582  2196  32519
			'Geography.Regions.Europe.Northern Europe'      4051  -->   2695  1356   314  49048
			'Geography.Regions.Europe.Southern Europe'      4291  -->   3114  1177   329  48793
			'Geography.Regions.Europe.Western Europe'       4808  -->   3483  1325   391  48214
			'Geography.Regions.Oceania'                      716  -->    354   362    54  52643
			'History and Society.Business and economics'    3313  -->   1910  1403   306  49794
			'History and Society.Education'                 1791  -->   1000   791   110  51512
			'History and Society.History'                   5372  -->   2806  2566   655  47386
			'History and Society.Military and warfare'      3913  -->   2345  1568   456  49044
			'History and Society.Politics and government'   3603  -->   1672  1931   461  49349
			'History and Society.Society'                   4648  -->   1152  3496   268  48497
			'History and Society.Transportation'            2412  -->   1991   421   110  50891
			'STEM.Biology'                                  2994  -->   2239   755   186  50233
			'STEM.Chemistry'                                1533  -->   1220   313   117  51763
			'STEM.Computing'                                2059  -->   1676   383   184  51170
			'STEM.Earth and environment'                    1835  -->   1137   698   146  51432
			'STEM.Engineering'                              2585  -->   1877   708   196  50632
			'STEM.Libraries & Information'                   476  -->    358   118    36  52901
			'STEM.Mathematics'                               561  -->    451   110    24  52828
			'STEM.Medicine & Health'                        2034  -->   1407   627   163  51216
			'STEM.Physics'                                  1620  -->   1188   432   159  51634
			'STEM.STEM*'                                   15902  -->  13810  2092  1138  36373
			'STEM.Space'                                    1936  -->   1785   151    32  51445
			'STEM.Technology'                               4113  -->   2924  1189   578  48722
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.283         0.13
		Culture.Biography.Women                         0.08          0.015
		Culture.Food and drink                          0.03          0.003
		Culture.Internet culture                        0.041         0.004
		Culture.Linguistics                             0.029         0.008
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.032         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.053         0.012
		Culture.Media.Media*                            0.232         0.056
		Culture.Media.Music                             0.06          0.021
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.039         0.009
		Culture.Media.Video games                       0.013         0.003
		Culture.Performing arts                         0.031         0.003
		Culture.Philosophy and religion                 0.069         0.011
		Culture.Sports                                  0.059         0.061
		Culture.Visual arts.Architecture                0.045         0.011
		Culture.Visual arts.Comics and Anime            0.019         0.002
		Culture.Visual arts.Fashion                     0.016         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.081         0.021
		Geography.Regions.Africa.Africa*                0.059         0.009
		Geography.Regions.Africa.Central Africa         0.007         0.001
		Geography.Regions.Africa.Eastern Africa         0.004         0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.02          0.004
		Geography.Regions.Americas.North America        0.103         0.064
		Geography.Regions.Americas.South America        0.03          0.007
		Geography.Regions.Asia.Asia*                    0.254         0.053
		Geography.Regions.Asia.Central Asia             0.016         0.001
		Geography.Regions.Asia.East Asia                0.045         0.012
		Geography.Regions.Asia.North Asia               0.095         0.006
		Geography.Regions.Asia.South Asia               0.032         0.017
		Geography.Regions.Asia.Southeast Asia           0.021         0.006
		Geography.Regions.Asia.West Asia                0.075         0.012
		Geography.Regions.Europe.Eastern Europe         0.121         0.019
		Geography.Regions.Europe.Europe*                0.35          0.082
		Geography.Regions.Europe.Northern Europe        0.076         0.029
		Geography.Regions.Europe.Southern Europe        0.08          0.014
		Geography.Regions.Europe.Western Europe         0.09          0.021
		Geography.Regions.Oceania                       0.013         0.005
		History and Society.Business and economics      0.062         0.01
		History and Society.Education                   0.034         0.008
		History and Society.History                     0.101         0.011
		History and Society.Military and warfare        0.073         0.016
		History and Society.Politics and government     0.067         0.017
		History and Society.Society                     0.087         0.008
		History and Society.Transportation              0.045         0.016
		STEM.Biology                                    0.056         0.035
		STEM.Chemistry                                  0.029         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.034         0.005
		STEM.Engineering                                0.048         0.006
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.011         0
		STEM.Medicine & Health                          0.038         0.007
		STEM.Physics                                    0.03          0.001
		STEM.STEM*                                      0.298         0.066
		STEM.Space                                      0.036         0.004
		STEM.Technology                                 0.077         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.133
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.005
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.051
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.075
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.012
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.016
		Geography.Regions.Europe.Eastern Europe      0.025
		Geography.Regions.Europe.Europe*             0.124
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.017
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.019
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.017
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.086
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.995
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.925
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.876
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.983
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.914
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.743, macro=0.689):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.671
		Culture.Food and drink                       0.728
		Culture.Internet culture                     0.797
		Culture.Linguistics                          0.643
		Culture.Literature                           0.703
		Culture.Media.Books                          0.794
		Culture.Media.Entertainment                  0.433
		Culture.Media.Films                          0.845
		Culture.Media.Media*                         0.845
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.724
		Culture.Media.Software                       0.898
		Culture.Media.Television                     0.766
		Culture.Media.Video games                    0.941
		Culture.Performing arts                      0.626
		Culture.Philosophy and religion              0.461
		Culture.Sports                               0.796
		Culture.Visual arts.Architecture             0.738
		Culture.Visual arts.Comics and Anime         0.826
		Culture.Visual arts.Fashion                  0.744
		Culture.Visual arts.Visual arts*             0.695
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.536
		Geography.Regions.Africa.Central Africa      0.589
		Geography.Regions.Africa.Eastern Africa      0.664
		Geography.Regions.Africa.Northern Africa     0.562
		Geography.Regions.Africa.Southern Africa     0.769
		Geography.Regions.Africa.Western Africa      0.693
		Geography.Regions.Americas.Central America   0.336
		Geography.Regions.Americas.North America     0.645
		Geography.Regions.Americas.South America     0.747
		Geography.Regions.Asia.Asia*                 0.78
		Geography.Regions.Asia.Central Asia          0.522
		Geography.Regions.Asia.East Asia             0.739
		Geography.Regions.Asia.North Asia            0.753
		Geography.Regions.Asia.South Asia            0.602
		Geography.Regions.Asia.Southeast Asia        0.363
		Geography.Regions.Asia.West Asia             0.687
		Geography.Regions.Europe.Eastern Europe      0.745
		Geography.Regions.Europe.Europe*             0.808
		Geography.Regions.Europe.Northern Europe     0.665
		Geography.Regions.Europe.Southern Europe     0.726
		Geography.Regions.Europe.Western Europe      0.724
		Geography.Regions.Oceania                    0.494
		History and Society.Business and economics   0.577
		History and Society.Education                0.558
		History and Society.History                  0.522
		History and Society.Military and warfare     0.599
		History and Society.Politics and government  0.464
		History and Society.Society                  0.248
		History and Society.Transportation           0.825
		STEM.Biology                                 0.748
		STEM.Chemistry                               0.796
		STEM.Computing                               0.814
		STEM.Earth and environment                   0.62
		STEM.Engineering                             0.726
		STEM.Libraries & Information                 0.752
		STEM.Mathematics                             0.804
		STEM.Medicine & Health                       0.692
		STEM.Physics                                 0.733
		STEM.STEM*                                   0.868
		STEM.Space                                   0.922
		STEM.Technology                              0.711
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.937
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.671, macro=0.57):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.851
		Culture.Biography.Women                      0.509
		Culture.Food and drink                       0.468
		Culture.Internet culture                     0.498
		Culture.Linguistics                          0.772
		Culture.Literature                           0.506
		Culture.Media.Books                          0.577
		Culture.Media.Entertainment                  0.385
		Culture.Media.Films                          0.792
		Culture.Media.Media*                         0.622
		Culture.Media.Music                          0.762
		Culture.Media.Radio                          0.82
		Culture.Media.Software                       0.252
		Culture.Media.Television                     0.774
		Culture.Media.Video games                    0.924
		Culture.Performing arts                      0.418
		Culture.Philosophy and religion              0.42
		Culture.Sports                               0.956
		Culture.Visual arts.Architecture             0.607
		Culture.Visual arts.Comics and Anime         0.673
		Culture.Visual arts.Fashion                  0.453
		Culture.Visual arts.Visual arts*             0.563
		Geography.Geographical                       0.554
		Geography.Regions.Africa.Africa*             0.498
		Geography.Regions.Africa.Central Africa      0.396
		Geography.Regions.Africa.Eastern Africa      0.4
		Geography.Regions.Africa.Northern Africa     0.321
		Geography.Regions.Africa.Southern Africa     0.658
		Geography.Regions.Africa.Western Africa      0.636
		Geography.Regions.Americas.Central America   0.495
		Geography.Regions.Americas.North America     0.729
		Geography.Regions.Americas.South America     0.763
		Geography.Regions.Asia.Asia*                 0.555
		Geography.Regions.Asia.Central Asia          0.226
		Geography.Regions.Asia.East Asia             0.78
		Geography.Regions.Asia.North Asia            0.346
		Geography.Regions.Asia.South Asia            0.852
		Geography.Regions.Asia.Southeast Asia        0.695
		Geography.Regions.Asia.West Asia             0.497
		Geography.Regions.Europe.Eastern Europe      0.559
		Geography.Regions.Europe.Europe*             0.533
		Geography.Regions.Europe.Northern Europe     0.76
		Geography.Regions.Europe.Southern Europe     0.607
		Geography.Regions.Europe.Western Europe      0.656
		Geography.Regions.Oceania                    0.691
		History and Society.Business and economics   0.485
		History and Society.Education                0.68
		History and Society.History                  0.299
		History and Society.Military and warfare     0.506
		History and Society.Politics and government  0.457
		History and Society.Society                  0.276
		History and Society.Transportation           0.865
		STEM.Biology                                 0.88
		STEM.Chemistry                               0.377
		STEM.Computing                               0.395
		STEM.Earth and environment                   0.513
		STEM.Engineering                             0.524
		STEM.Libraries & Information                 0.434
		STEM.Mathematics                             0.453
		STEM.Medicine & Health                       0.589
		STEM.Physics                                 0.185
		STEM.STEM*                                   0.669
		STEM.Space                                   0.865
		STEM.Technology                              0.241
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.696, macro=0.607):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.862
		Culture.Biography.Women                      0.579
		Culture.Food and drink                       0.57
		Culture.Internet culture                     0.613
		Culture.Linguistics                          0.702
		Culture.Literature                           0.588
		Culture.Media.Books                          0.669
		Culture.Media.Entertainment                  0.407
		Culture.Media.Films                          0.818
		Culture.Media.Media*                         0.716
		Culture.Media.Music                          0.777
		Culture.Media.Radio                          0.769
		Culture.Media.Software                       0.393
		Culture.Media.Television                     0.77
		Culture.Media.Video games                    0.933
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.44
		Culture.Sports                               0.869
		Culture.Visual arts.Architecture             0.666
		Culture.Visual arts.Comics and Anime         0.742
		Culture.Visual arts.Fashion                  0.563
		Culture.Visual arts.Visual arts*             0.622
		Geography.Geographical                       0.591
		Geography.Regions.Africa.Africa*             0.516
		Geography.Regions.Africa.Central Africa      0.474
		Geography.Regions.Africa.Eastern Africa      0.499
		Geography.Regions.Africa.Northern Africa     0.409
		Geography.Regions.Africa.Southern Africa     0.709
		Geography.Regions.Africa.Western Africa      0.663
		Geography.Regions.Americas.Central America   0.4
		Geography.Regions.Americas.North America     0.684
		Geography.Regions.Americas.South America     0.755
		Geography.Regions.Asia.Asia*                 0.649
		Geography.Regions.Asia.Central Asia          0.316
		Geography.Regions.Asia.East Asia             0.759
		Geography.Regions.Asia.North Asia            0.474
		Geography.Regions.Asia.South Asia            0.705
		Geography.Regions.Asia.Southeast Asia        0.477
		Geography.Regions.Asia.West Asia             0.577
		Geography.Regions.Europe.Eastern Europe      0.639
		Geography.Regions.Europe.Europe*             0.643
		Geography.Regions.Europe.Northern Europe     0.709
		Geography.Regions.Europe.Southern Europe     0.661
		Geography.Regions.Europe.Western Europe      0.689
		Geography.Regions.Oceania                    0.576
		History and Society.Business and economics   0.527
		History and Society.Education                0.613
		History and Society.History                  0.38
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.461
		History and Society.Society                  0.261
		History and Society.Transportation           0.845
		STEM.Biology                                 0.809
		STEM.Chemistry                               0.512
		STEM.Computing                               0.532
		STEM.Earth and environment                   0.561
		STEM.Engineering                             0.609
		STEM.Libraries & Information                 0.551
		STEM.Mathematics                             0.58
		STEM.Medicine & Health                       0.636
		STEM.Physics                                 0.296
		STEM.STEM*                                   0.756
		STEM.Space                                   0.893
		STEM.Technology                              0.36
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   1
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.99
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.926
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.982
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.023
		Culture.Biography.Women                      0.01
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.016
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.035
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.063
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.004
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.967, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.972
		Culture.Literature                           0.97
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.968
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.914
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.972
		Culture.Philosophy and religion              0.938
		Culture.Sports                               0.97
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.973
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.963
		Geography.Regions.Africa.Central Africa      0.953
		Geography.Regions.Africa.Eastern Africa      0.921
		Geography.Regions.Africa.Northern Africa     0.972
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.92
		Geography.Regions.Americas.Central America   0.947
		Geography.Regions.Americas.North America     0.959
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.967
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.965
		Geography.Regions.Asia.Southeast Asia        0.949
		Geography.Regions.Asia.West Asia             0.971
		Geography.Regions.Europe.Eastern Europe      0.967
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.97
		Geography.Regions.Europe.Western Europe      0.971
		Geography.Regions.Oceania                    0.954
		History and Society.Business and economics   0.963
		History and Society.Education                0.966
		History and Society.History                  0.94
		History and Society.Military and warfare     0.96
		History and Society.Politics and government  0.942
		History and Society.Society                  0.893
		History and Society.Transportation           0.982
		STEM.Biology                                 0.974
		STEM.Chemistry                               0.985
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.97
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.962
		STEM.Mathematics                             0.968
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.972
		STEM.Space                                   0.99
		STEM.Technology                              0.973
		-------------------------------------------  -----
	pr_auc (micro=0.741, macro=0.589):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.555
		Culture.Food and drink                       0.624
		Culture.Internet culture                     0.616
		Culture.Linguistics                          0.716
		Culture.Literature                           0.627
		Culture.Media.Books                          0.712
		Culture.Media.Entertainment                  0.366
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.828
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.519
		Culture.Media.Software                       0.487
		Culture.Media.Television                     0.81
		Culture.Media.Video games                    0.924
		Culture.Performing arts                      0.479
		Culture.Philosophy and religion              0.395
		Culture.Sports                               0.897
		Culture.Visual arts.Architecture             0.682
		Culture.Visual arts.Comics and Anime         0.729
		Culture.Visual arts.Fashion                  0.381
		Culture.Visual arts.Visual arts*             0.647
		Geography.Geographical                       0.591
		Geography.Regions.Africa.Africa*             0.506
		Geography.Regions.Africa.Central Africa      0.25
		Geography.Regions.Africa.Eastern Africa      0.208
		Geography.Regions.Africa.Northern Africa     0.272
		Geography.Regions.Africa.Southern Africa     0.592
		Geography.Regions.Africa.Western Africa      0.372
		Geography.Regions.Americas.Central America   0.297
		Geography.Regions.Americas.North America     0.734
		Geography.Regions.Americas.South America     0.789
		Geography.Regions.Asia.Asia*                 0.727
		Geography.Regions.Asia.Central Asia          0.157
		Geography.Regions.Asia.East Asia             0.791
		Geography.Regions.Asia.North Asia            0.58
		Geography.Regions.Asia.South Asia            0.745
		Geography.Regions.Asia.Southeast Asia        0.44
		Geography.Regions.Asia.West Asia             0.588
		Geography.Regions.Europe.Eastern Europe      0.705
		Geography.Regions.Europe.Europe*             0.754
		Geography.Regions.Europe.Northern Europe     0.753
		Geography.Regions.Europe.Southern Europe     0.687
		Geography.Regions.Europe.Western Europe      0.728
		Geography.Regions.Oceania                    0.472
		History and Society.Business and economics   0.527
		History and Society.Education                0.562
		History and Society.History                  0.346
		History and Society.Military and warfare     0.554
		History and Society.Politics and government  0.398
		History and Society.Society                  0.184
		History and Society.Transportation           0.868
		STEM.Biology                                 0.869
		STEM.Chemistry                               0.454
		STEM.Computing                               0.503
		STEM.Earth and environment                   0.538
		STEM.Engineering                             0.684
		STEM.Libraries & Information                 0.461
		STEM.Mathematics                             0.457
		STEM.Medicine & Health                       0.638
		STEM.Physics                                 0.2
		STEM.STEM*                                   0.859
		STEM.Space                                   0.931
		STEM.Technology                              0.398
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

