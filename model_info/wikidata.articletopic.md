Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-5.3.0-62-generic-x86_64-with-Ubuntu-18.04-bionic'
	 - machine: 'x86_64'
	 - version: '#56~18.04.1-Ubuntu SMP Wed Jun 24 16:17:03 UTC 2020'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Apr 18 2020 01:56:04')
	 - python_compiler: 'GCC 8.4.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.6.9'
	 - release: '5.3.0-62-generic'
	
	Statistics:
	counts (n=63944):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16670  -->  15762   908   464  46810
			'Culture.Biography.Women'                       4110  -->   3125   985   679  59155
			'Culture.Food and drink'                        1318  -->    613   705   126  62500
			'Culture.Internet culture'                      2966  -->   1948  1018   140  60838
			'Culture.Linguistics'                           1466  -->    934   532    56  62422
			'Culture.Literature'                            5367  -->   3996  1371   404  58173
			'Culture.Media.Books'                           1974  -->   1560   414   136  61834
			'Culture.Media.Entertainment'                   1733  -->    857   876   162  62049
			'Culture.Media.Films'                           2295  -->   1896   399   122  61527
			'Culture.Media.Media*'                         14383  -->  11572  2811  1135  48426
			'Culture.Media.Music'                           2583  -->   2027   556   247  61114
			'Culture.Media.Radio'                           1156  -->    857   299    44  62744
			'Culture.Media.Software'                        1750  -->    685  1065   307  61887
			'Culture.Media.Television'                      2230  -->   1510   720   176  61538
			'Culture.Media.Video games'                     2147  -->   1758   389    54  61743
			'Culture.Performing arts'                       1334  -->    741   593   116  62494
			'Culture.Philosophy and religion'               2702  -->   1074  1628   285  60957
			'Culture.Sports'                                5925  -->   5186   739   249  57770
			'Culture.Visual arts.Architecture'              2648  -->   1867   781   230  61066
			'Culture.Visual arts.Comics and Anime'          1508  -->   1007   501   140  62296
			'Culture.Visual arts.Fashion'                   1199  -->    669   530    98  62647
			'Culture.Visual arts.Visual arts*'              6070  -->   4131  1939   554  57320
			'Geography.Geographical'                        3464  -->   2226  1238   359  60121
			'Geography.Regions.Africa.Africa*'              6449  -->   4664  1785   414  57081
			'Geography.Regions.Africa.Central Africa'       1145  -->    697   448    83  62716
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    704   410    56  62774
			'Geography.Regions.Africa.Northern Africa'      1280  -->    774   506   108  62556
			'Geography.Regions.Africa.Southern Africa'      1244  -->    859   385    81  62619
			'Geography.Regions.Africa.Western Africa'       1142  -->    774   368    75  62727
			'Geography.Regions.Americas.Central America'    1331  -->    707   624    87  62526
			'Geography.Regions.Americas.North America'      7625  -->   5064  2561  1169  55150
			'Geography.Regions.Americas.South America'      1532  -->   1082   450   142  62270
			'Geography.Regions.Asia.Asia*'                 11647  -->   8432  3215   835  51462
			'Geography.Regions.Asia.Central Asia'           1086  -->    671   415    70  62788
			'Geography.Regions.Asia.East Asia'              2717  -->   1727   990   241  60986
			'Geography.Regions.Asia.North Asia'             2076  -->   1336   740   163  61705
			'Geography.Regions.Asia.South Asia'             2366  -->   1612   754   135  61443
			'Geography.Regions.Asia.Southeast Asia'         1721  -->   1059   662   119  62104
			'Geography.Regions.Asia.West Asia'              2160  -->   1473   687   129  61655
			'Geography.Regions.Europe.Eastern Europe'       3533  -->   2472  1061   234  60177
			'Geography.Regions.Europe.Europe*'             12939  -->   9372  3567  1810  49195
			'Geography.Regions.Europe.Northern Europe'      4221  -->   2571  1650   601  59122
			'Geography.Regions.Europe.Southern Europe'      2438  -->   1565   873   268  61238
			'Geography.Regions.Europe.Western Europe'       3076  -->   1934  1142   417  60451
			'Geography.Regions.Oceania'                     2638  -->   1859   779   138  61168
			'History and Society.Business and economics'    3502  -->   1544  1958   569  59873
			'History and Society.Education'                 2243  -->   1113  1130   255  61446
			'History and Society.History'                   3172  -->   1154  2018   360  60412
			'History and Society.Military and warfare'      3238  -->   1677  1561   296  60410
			'History and Society.Politics and government'   4590  -->   2406  2184   329  59025
			'History and Society.Society'                   2971  -->    897  2074   166  60807
			'History and Society.Transportation'            3629  -->   2615  1014   169  60146
			'STEM.Biology'                                  2916  -->   2237   679    91  60937
			'STEM.Chemistry'                                1270  -->    690   580   138  62536
			'STEM.Computing'                                1968  -->    828  1140   332  61644
			'STEM.Earth and environment'                    1627  -->    918   709   114  62203
			'STEM.Engineering'                              2195  -->   1284   911   141  61608
			'STEM.Libraries & Information'                  1174  -->    605   569    87  62683
			'STEM.Mathematics'                              1137  -->    307   830   107  62700
			'STEM.Medicine & Health'                        1726  -->    769   957   180  62038
			'STEM.Physics'                                  1219  -->    448   771   107  62618
			'STEM.STEM*'                                   16449  -->  12609  3840  2766  44729
			'STEM.Space'                                    1365  -->    932   433    47  62532
			'STEM.Technology'                               3648  -->   1396  2252   424  59872
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.261         0.12
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.021         0.003
		Culture.Internet culture                        0.046         0.004
		Culture.Linguistics                             0.023         0.008
		Culture.Literature                              0.084         0.015
		Culture.Media.Books                             0.031         0.004
		Culture.Media.Entertainment                     0.027         0.004
		Culture.Media.Films                             0.036         0.012
		Culture.Media.Media*                            0.225         0.055
		Culture.Media.Music                             0.04          0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.034         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.01
		Culture.Sports                                  0.093         0.06
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.054         0.021
		Geography.Regions.Africa.Africa*                0.101         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0.001
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.063
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.182         0.052
		Geography.Regions.Asia.Central Asia             0.017         0.001
		Geography.Regions.Asia.East Asia                0.042         0.012
		Geography.Regions.Asia.North Asia               0.032         0.006
		Geography.Regions.Asia.South Asia               0.037         0.016
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.034         0.012
		Geography.Regions.Europe.Eastern Europe         0.055         0.018
		Geography.Regions.Europe.Europe*                0.202         0.081
		Geography.Regions.Europe.Northern Europe        0.066         0.029
		Geography.Regions.Europe.Southern Europe        0.038         0.014
		Geography.Regions.Europe.Western Europe         0.048         0.02
		Geography.Regions.Oceania                       0.041         0.016
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.035         0.008
		History and Society.History                     0.05          0.011
		History and Society.Military and warfare        0.051         0.015
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.046         0.008
		History and Society.Transportation              0.057         0.016
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.031         0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.034         0.006
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.257         0.065
		STEM.Space                                      0.021         0.004
		STEM.Technology                                 0.057         0.005
	match_rate (micro=0.05, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.023
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.006
		Culture.Literature                           0.018
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.066
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.057
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.091
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.01
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.02
		History and Society.Society                  0.005
		History and Society.Transportation           0.014
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.004
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.104
		STEM.Space                                   0.004
		STEM.Technology                              0.009
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.994
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.934
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.943
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.99
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.98
		History and Society.Society                  0.995
		History and Society.Transportation           0.986
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.896
		STEM.Space                                   0.996
		STEM.Technology                              0.991
		-------------------------------------------  -----
	recall (micro=0.719, macro=0.621):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.946
		Culture.Biography.Women                      0.76
		Culture.Food and drink                       0.465
		Culture.Internet culture                     0.657
		Culture.Linguistics                          0.637
		Culture.Literature                           0.745
		Culture.Media.Books                          0.79
		Culture.Media.Entertainment                  0.495
		Culture.Media.Films                          0.826
		Culture.Media.Media*                         0.805
		Culture.Media.Music                          0.785
		Culture.Media.Radio                          0.741
		Culture.Media.Software                       0.391
		Culture.Media.Television                     0.677
		Culture.Media.Video games                    0.819
		Culture.Performing arts                      0.555
		Culture.Philosophy and religion              0.397
		Culture.Sports                               0.875
		Culture.Visual arts.Architecture             0.705
		Culture.Visual arts.Comics and Anime         0.668
		Culture.Visual arts.Fashion                  0.558
		Culture.Visual arts.Visual arts*             0.681
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.723
		Geography.Regions.Africa.Central Africa      0.609
		Geography.Regions.Africa.Eastern Africa      0.632
		Geography.Regions.Africa.Northern Africa     0.605
		Geography.Regions.Africa.Southern Africa     0.691
		Geography.Regions.Africa.Western Africa      0.678
		Geography.Regions.Americas.Central America   0.531
		Geography.Regions.Americas.North America     0.664
		Geography.Regions.Americas.South America     0.706
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.618
		Geography.Regions.Asia.East Asia             0.636
		Geography.Regions.Asia.North Asia            0.644
		Geography.Regions.Asia.South Asia            0.681
		Geography.Regions.Asia.Southeast Asia        0.615
		Geography.Regions.Asia.West Asia             0.682
		Geography.Regions.Europe.Eastern Europe      0.7
		Geography.Regions.Europe.Europe*             0.724
		Geography.Regions.Europe.Northern Europe     0.609
		Geography.Regions.Europe.Southern Europe     0.642
		Geography.Regions.Europe.Western Europe      0.629
		Geography.Regions.Oceania                    0.705
		History and Society.Business and economics   0.441
		History and Society.Education                0.496
		History and Society.History                  0.364
		History and Society.Military and warfare     0.518
		History and Society.Politics and government  0.524
		History and Society.Society                  0.302
		History and Society.Transportation           0.721
		STEM.Biology                                 0.767
		STEM.Chemistry                               0.543
		STEM.Computing                               0.421
		STEM.Earth and environment                   0.564
		STEM.Engineering                             0.585
		STEM.Libraries & Information                 0.515
		STEM.Mathematics                             0.27
		STEM.Medicine & Health                       0.446
		STEM.Physics                                 0.368
		STEM.STEM*                                   0.767
		STEM.Space                                   0.683
		STEM.Technology                              0.383
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.99
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.994
		History and Society.Society                  0.997
		History and Society.Transportation           0.997
		STEM.Biology                                 0.999
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.942
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	precision (micro=0.7, macro=0.554):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.504
		Culture.Food and drink                       0.371
		Culture.Internet culture                     0.517
		Culture.Linguistics                          0.852
		Culture.Literature                           0.619
		Culture.Media.Books                          0.609
		Culture.Media.Entertainment                  0.429
		Culture.Media.Films                          0.829
		Culture.Media.Media*                         0.67
		Culture.Media.Music                          0.807
		Culture.Media.Radio                          0.711
		Culture.Media.Software                       0.094
		Culture.Media.Television                     0.68
		Culture.Media.Video games                    0.732
		Culture.Performing arts                      0.478
		Culture.Philosophy and religion              0.472
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.672
		Culture.Visual arts.Comics and Anime         0.416
		Culture.Visual arts.Fashion                  0.242
		Culture.Visual arts.Visual arts*             0.566
		Geography.Geographical                       0.7
		Geography.Regions.Africa.Africa*             0.462
		Geography.Regions.Africa.Central Africa      0.244
		Geography.Regions.Africa.Eastern Africa      0.262
		Geography.Regions.Africa.Northern Africa     0.321
		Geography.Regions.Africa.Southern Africa     0.411
		Geography.Regions.Africa.Western Africa      0.297
		Geography.Regions.Americas.Central America   0.569
		Geography.Regions.Americas.North America     0.682
		Geography.Regions.Americas.South America     0.681
		Geography.Regions.Asia.Asia*                 0.715
		Geography.Regions.Asia.Central Asia          0.306
		Geography.Regions.Asia.East Asia             0.665
		Geography.Regions.Asia.North Asia            0.579
		Geography.Regions.Asia.South Asia            0.839
		Geography.Regions.Asia.Southeast Asia        0.668
		Geography.Regions.Asia.West Asia             0.794
		Geography.Regions.Europe.Eastern Europe      0.771
		Geography.Regions.Europe.Europe*             0.642
		Geography.Regions.Europe.Northern Europe     0.643
		Geography.Regions.Europe.Southern Europe     0.673
		Geography.Regions.Europe.Western Europe      0.657
		Geography.Regions.Oceania                    0.839
		History and Society.Business and economics   0.315
		History and Society.Education                0.489
		History and Society.History                  0.403
		History and Society.Military and warfare     0.622
		History and Society.Politics and government  0.731
		History and Society.Society                  0.48
		History and Society.Transportation           0.809
		STEM.Biology                                 0.948
		STEM.Chemistry                               0.294
		STEM.Computing                               0.182
		STEM.Earth and environment                   0.594
		STEM.Engineering                             0.596
		STEM.Libraries & Information                 0.203
		STEM.Mathematics                             0.068
		STEM.Medicine & Health                       0.499
		STEM.Physics                                 0.168
		STEM.STEM*                                   0.477
		STEM.Space                                   0.795
		STEM.Technology                              0.219
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.993
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.986
		History and Society.Society                  0.994
		History and Society.Transportation           0.995
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.703, macro=0.571):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.937
		Culture.Biography.Women                      0.606
		Culture.Food and drink                       0.413
		Culture.Internet culture                     0.578
		Culture.Linguistics                          0.729
		Culture.Literature                           0.676
		Culture.Media.Books                          0.688
		Culture.Media.Entertainment                  0.459
		Culture.Media.Films                          0.828
		Culture.Media.Media*                         0.731
		Culture.Media.Music                          0.795
		Culture.Media.Radio                          0.726
		Culture.Media.Software                       0.152
		Culture.Media.Television                     0.678
		Culture.Media.Video games                    0.773
		Culture.Performing arts                      0.514
		Culture.Philosophy and religion              0.431
		Culture.Sports                               0.901
		Culture.Visual arts.Architecture             0.688
		Culture.Visual arts.Comics and Anime         0.513
		Culture.Visual arts.Fashion                  0.338
		Culture.Visual arts.Visual arts*             0.618
		Geography.Geographical                       0.67
		Geography.Regions.Africa.Africa*             0.564
		Geography.Regions.Africa.Central Africa      0.349
		Geography.Regions.Africa.Eastern Africa      0.371
		Geography.Regions.Africa.Northern Africa     0.42
		Geography.Regions.Africa.Southern Africa     0.515
		Geography.Regions.Africa.Western Africa      0.413
		Geography.Regions.Americas.Central America   0.55
		Geography.Regions.Americas.North America     0.673
		Geography.Regions.Americas.South America     0.693
		Geography.Regions.Asia.Asia*                 0.719
		Geography.Regions.Asia.Central Asia          0.41
		Geography.Regions.Asia.East Asia             0.65
		Geography.Regions.Asia.North Asia            0.609
		Geography.Regions.Asia.South Asia            0.752
		Geography.Regions.Asia.Southeast Asia        0.641
		Geography.Regions.Asia.West Asia             0.734
		Geography.Regions.Europe.Eastern Europe      0.733
		Geography.Regions.Europe.Europe*             0.681
		Geography.Regions.Europe.Northern Europe     0.626
		Geography.Regions.Europe.Southern Europe     0.657
		Geography.Regions.Europe.Western Europe      0.643
		Geography.Regions.Oceania                    0.766
		History and Society.Business and economics   0.367
		History and Society.Education                0.493
		History and Society.History                  0.382
		History and Society.Military and warfare     0.565
		History and Society.Politics and government  0.611
		History and Society.Society                  0.371
		History and Society.Transportation           0.762
		STEM.Biology                                 0.848
		STEM.Chemistry                               0.382
		STEM.Computing                               0.254
		STEM.Earth and environment                   0.579
		STEM.Engineering                             0.591
		STEM.Libraries & Information                 0.291
		STEM.Mathematics                             0.109
		STEM.Medicine & Health                       0.471
		STEM.Physics                                 0.23
		STEM.STEM*                                   0.588
		STEM.Space                                   0.735
		STEM.Technology                              0.279
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.991
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.996
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.962
		STEM.Space                                   0.999
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.959
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.945
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.981
		History and Society.Society                  0.992
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.93
		STEM.Space                                   0.998
		STEM.Technology                              0.99
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.01
		Culture.Biography.Women                      0.011
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.002
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.023
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.035
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.005
		History and Society.Politics and government  0.006
		History and Society.Society                  0.003
		History and Society.Transportation           0.003
		STEM.Biology                                 0.001
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.058
		STEM.Space                                   0.001
		STEM.Technology                              0.007
		-------------------------------------------  -----
	roc_auc (micro=0.956, macro=0.951):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.937
		Culture.Internet culture                     0.96
		Culture.Linguistics                          0.954
		Culture.Literature                           0.965
		Culture.Media.Books                          0.971
		Culture.Media.Entertainment                  0.947
		Culture.Media.Films                          0.974
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.962
		Culture.Media.Software                       0.946
		Culture.Media.Television                     0.964
		Culture.Media.Video games                    0.977
		Culture.Performing arts                      0.947
		Culture.Philosophy and religion              0.91
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.969
		Culture.Visual arts.Comics and Anime         0.966
		Culture.Visual arts.Fashion                  0.95
		Culture.Visual arts.Visual arts*             0.952
		Geography.Geographical                       0.956
		Geography.Regions.Africa.Africa*             0.96
		Geography.Regions.Africa.Central Africa      0.954
		Geography.Regions.Africa.Eastern Africa      0.957
		Geography.Regions.Africa.Northern Africa     0.945
		Geography.Regions.Africa.Southern Africa     0.959
		Geography.Regions.Africa.Western Africa      0.96
		Geography.Regions.Americas.Central America   0.932
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.963
		Geography.Regions.Asia.Asia*                 0.949
		Geography.Regions.Asia.Central Asia          0.952
		Geography.Regions.Asia.East Asia             0.95
		Geography.Regions.Asia.North Asia            0.946
		Geography.Regions.Asia.South Asia            0.953
		Geography.Regions.Asia.Southeast Asia        0.942
		Geography.Regions.Asia.West Asia             0.953
		Geography.Regions.Europe.Eastern Europe      0.951
		Geography.Regions.Europe.Europe*             0.943
		Geography.Regions.Europe.Northern Europe     0.948
		Geography.Regions.Europe.Southern Europe     0.949
		Geography.Regions.Europe.Western Europe      0.95
		Geography.Regions.Oceania                    0.96
		History and Society.Business and economics   0.936
		History and Society.Education                0.944
		History and Society.History                  0.916
		History and Society.Military and warfare     0.933
		History and Society.Politics and government  0.925
		History and Society.Society                  0.871
		History and Society.Transportation           0.963
		STEM.Biology                                 0.962
		STEM.Chemistry                               0.958
		STEM.Computing                               0.951
		STEM.Earth and environment                   0.947
		STEM.Engineering                             0.947
		STEM.Libraries & Information                 0.948
		STEM.Mathematics                             0.942
		STEM.Medicine & Health                       0.933
		STEM.Physics                                 0.945
		STEM.STEM*                                   0.955
		STEM.Space                                   0.963
		STEM.Technology                              0.928
		-------------------------------------------  -----
	pr_auc (micro=0.721, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.952
		Culture.Biography.Women                      0.589
		Culture.Food and drink                       0.352
		Culture.Internet culture                     0.549
		Culture.Linguistics                          0.656
		Culture.Literature                           0.726
		Culture.Media.Books                          0.659
		Culture.Media.Entertainment                  0.433
		Culture.Media.Films                          0.813
		Culture.Media.Media*                         0.813
		Culture.Media.Music                          0.818
		Culture.Media.Radio                          0.741
		Culture.Media.Software                       0.094
		Culture.Media.Television                     0.664
		Culture.Media.Video games                    0.801
		Culture.Performing arts                      0.414
		Culture.Philosophy and religion              0.339
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.673
		Culture.Visual arts.Comics and Anime         0.558
		Culture.Visual arts.Fashion                  0.215
		Culture.Visual arts.Visual arts*             0.666
		Geography.Geographical                       0.698
		Geography.Regions.Africa.Africa*             0.639
		Geography.Regions.Africa.Central Africa      0.321
		Geography.Regions.Africa.Eastern Africa      0.253
		Geography.Regions.Africa.Northern Africa     0.343
		Geography.Regions.Africa.Southern Africa     0.514
		Geography.Regions.Africa.Western Africa      0.277
		Geography.Regions.Americas.Central America   0.494
		Geography.Regions.Americas.North America     0.726
		Geography.Regions.Americas.South America     0.691
		Geography.Regions.Asia.Asia*                 0.756
		Geography.Regions.Asia.Central Asia          0.462
		Geography.Regions.Asia.East Asia             0.625
		Geography.Regions.Asia.North Asia            0.55
		Geography.Regions.Asia.South Asia            0.708
		Geography.Regions.Asia.Southeast Asia        0.557
		Geography.Regions.Asia.West Asia             0.662
		Geography.Regions.Europe.Eastern Europe      0.71
		Geography.Regions.Europe.Europe*             0.744
		Geography.Regions.Europe.Northern Europe     0.644
		Geography.Regions.Europe.Southern Europe     0.618
		Geography.Regions.Europe.Western Europe      0.63
		Geography.Regions.Oceania                    0.75
		History and Society.Business and economics   0.248
		History and Society.Education                0.4
		History and Society.History                  0.315
		History and Society.Military and warfare     0.521
		History and Society.Politics and government  0.603
		History and Society.Society                  0.318
		History and Society.Transportation           0.712
		STEM.Biology                                 0.816
		STEM.Chemistry                               0.27
		STEM.Computing                               0.149
		STEM.Earth and environment                   0.522
		STEM.Engineering                             0.51
		STEM.Libraries & Information                 0.238
		STEM.Mathematics                             0.125
		STEM.Medicine & Health                       0.398
		STEM.Physics                                 0.126
		STEM.STEM*                                   0.768
		STEM.Space                                   0.686
		STEM.Technology                              0.213
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

