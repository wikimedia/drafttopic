Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'scale': False, 'random_state': None, 'verbose': 0, 'min_impurity_split': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'warm_start': False, 'max_leaf_nodes': None, 'learning_rate': 0.1, 'n_iter_no_change': None, 'loss': 'deviance', 'n_estimators': 150, 'label_weights': {}, 'multilabel': True, 'presort': 'auto', 'min_samples_split': 2, 'validation_fraction': 0.1, 'max_features': 'log2', 'center': False, 'init': None, 'subsample': 1.0, 'min_impurity_decrease': 0.0, 'tol': 0.0001, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'population_rates': None}
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
	counts (n=63816):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16704  -->  14861  1843  1150  45962
			'Culture.Biography.Women'                       4023  -->   3119   904   754  59039
			'Culture.Food and drink'                        1341  -->    965   376    65  62410
			'Culture.Internet culture'                      2957  -->   2304   653   206  60653
			'Culture.Linguistics'                           1413  -->   1066   347   109  62294
			'Culture.Literature'                            5241  -->   3975  1266   437  58138
			'Culture.Media.Books'                           1875  -->   1405   470   165  61776
			'Culture.Media.Entertainment'                   1822  -->    973   849   209  61785
			'Culture.Media.Films'                           2365  -->   1940   425   149  61302
			'Culture.Media.Media*'                         14419  -->  12401  2018  1435  47962
			'Culture.Media.Music'                           2647  -->   2136   511   265  60904
			'Culture.Media.Radio'                           1168  -->    936   232    21  62627
			'Culture.Media.Software'                        1762  -->   1001   761   343  61711
			'Culture.Media.Television'                      2243  -->   1702   541   194  61379
			'Culture.Media.Video games'                     2093  -->   1871   222    34  61689
			'Culture.Performing arts'                       1350  -->    916   434    99  62367
			'Culture.Philosophy and religion'               2641  -->   1482  1159   321  60854
			'Culture.Sports'                                5873  -->   5283   590   277  57666
			'Culture.Visual arts.Architecture'              2615  -->   1928   687   287  60914
			'Culture.Visual arts.Comics and Anime'          1519  -->   1236   283    85  62212
			'Culture.Visual arts.Fashion'                   1153  -->    781   372    75  62588
			'Culture.Visual arts.Visual arts*'              5958  -->   4523  1435   532  57326
			'Geography.Geographical'                        3452  -->   2245  1207   274  60090
			'Geography.Regions.Africa.Africa*'              6464  -->   5661   803   393  56959
			'Geography.Regions.Africa.Central Africa'       1127  -->    865   262    40  62649
			'Geography.Regions.Africa.Eastern Africa'       1090  -->    899   191    45  62681
			'Geography.Regions.Africa.Northern Africa'      1267  -->    931   336    97  62452
			'Geography.Regions.Africa.Southern Africa'      1286  -->   1021   265    51  62479
			'Geography.Regions.Africa.Western Africa'       1157  -->    961   196    74  62585
			'Geography.Regions.Americas.Central America'    1331  -->    976   355    73  62412
			'Geography.Regions.Americas.North America'      7814  -->   5570  2244  1299  54703
			'Geography.Regions.Americas.South America'      1525  -->   1161   364   124  62167
			'Geography.Regions.Asia.Asia*'                 11727  -->  10121  1606   854  51235
			'Geography.Regions.Asia.Central Asia'           1090  -->    828   262    50  62676
			'Geography.Regions.Asia.East Asia'              2763  -->   2144   619   240  60813
			'Geography.Regions.Asia.North Asia'             2104  -->   1519   585   217  61495
			'Geography.Regions.Asia.South Asia'             2388  -->   2082   306   109  61319
			'Geography.Regions.Asia.Southeast Asia'         1676  -->   1322   354   115  62025
			'Geography.Regions.Asia.West Asia'              2158  -->   1748   410   136  61522
			'Geography.Regions.Europe.Eastern Europe'       3520  -->   2763   757   291  60005
			'Geography.Regions.Europe.Europe*'             12911  -->  10048  2863  1875  49030
			'Geography.Regions.Europe.Northern Europe'      4196  -->   2961  1235   663  58957
			'Geography.Regions.Europe.Southern Europe'      2360  -->   1699   661   289  61167
			'Geography.Regions.Europe.Western Europe'       3140  -->   2220   920   463  60213
			'Geography.Regions.Oceania'                     2195  -->   1813   382   125  61496
			'History and Society.Business and economics'    3389  -->   1629  1760   511  59916
			'History and Society.Education'                 2247  -->   1074  1173   232  61337
			'History and Society.History'                   3160  -->   1287  1873   490  60166
			'History and Society.Military and warfare'      3261  -->   2236  1025   332  60223
			'History and Society.Politics and government'   3042  -->   1500  1542   399  60375
			'History and Society.Society'                   2877  -->    824  2053   231  60708
			'History and Society.Transportation'            3615  -->   3129   486   199  60002
			'STEM.Biology'                                  2852  -->   2345   507   138  60826
			'STEM.Chemistry'                                1287  -->    899   388   148  62381
			'STEM.Computing'                                2072  -->   1399   673   441  61303
			'STEM.Earth and environment'                    1639  -->   1135   504   117  62060
			'STEM.Engineering'                              2212  -->   1585   627   181  61423
			'STEM.Libraries & Information'                  1148  -->    700   448    61  62607
			'STEM.Mathematics'                              1126  -->    758   368    70  62620
			'STEM.Medicine & Health'                        1753  -->   1161   592   180  61883
			'STEM.Physics'                                  1202  -->    746   456   136  62478
			'STEM.STEM*'                                   16322  -->  14195  2127  1007  46487
			'STEM.Space'                                    1337  -->   1148   189    65  62414
			'STEM.Technology'                               3682  -->   2249  1433   654  59480
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.262         0.121
		Culture.Biography.Women                         0.063         0.015
		Culture.Food and drink                          0.021         0.003
		Culture.Internet culture                        0.046         0.004
		Culture.Linguistics                             0.022         0.008
		Culture.Literature                              0.082         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.012
		Culture.Media.Media*                            0.226         0.055
		Culture.Media.Music                             0.041         0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.041         0.01
		Culture.Sports                                  0.092         0.061
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.054         0.021
		Geography.Regions.Africa.Africa*                0.101         0.009
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0.001
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.122         0.064
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.184         0.053
		Geography.Regions.Asia.Central Asia             0.017         0.001
		Geography.Regions.Asia.East Asia                0.043         0.012
		Geography.Regions.Asia.North Asia               0.033         0.006
		Geography.Regions.Asia.South Asia               0.037         0.017
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.034         0.012
		Geography.Regions.Europe.Eastern Europe         0.055         0.018
		Geography.Regions.Europe.Europe*                0.202         0.082
		Geography.Regions.Europe.Northern Europe        0.066         0.029
		Geography.Regions.Europe.Southern Europe        0.037         0.014
		Geography.Regions.Europe.Western Europe         0.049         0.021
		Geography.Regions.Oceania                       0.034         0.017
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.035         0.008
		History and Society.History                     0.05          0.011
		History and Society.Military and warfare        0.051         0.015
		History and Society.Politics and government     0.048         0.016
		History and Society.Society                     0.045         0.008
		History and Society.Transportation              0.057         0.016
		STEM.Biology                                    0.045         0.035
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.035         0.006
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.256         0.066
		STEM.Space                                      0.021         0.004
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.008
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.067
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.016
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.019
		Geography.Regions.Europe.Europe*             0.097
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.016
		History and Society.Business and economics   0.013
		History and Society.Education                0.008
		History and Society.History                  0.012
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.015
		History and Society.Society                  0.006
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.077
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.992
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.933
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.903
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.985
		History and Society.Society                  0.994
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.923
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.782, macro=0.728):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.775
		Culture.Food and drink                       0.72
		Culture.Internet culture                     0.779
		Culture.Linguistics                          0.754
		Culture.Literature                           0.758
		Culture.Media.Books                          0.749
		Culture.Media.Entertainment                  0.534
		Culture.Media.Films                          0.82
		Culture.Media.Media*                         0.86
		Culture.Media.Music                          0.807
		Culture.Media.Radio                          0.801
		Culture.Media.Software                       0.568
		Culture.Media.Television                     0.759
		Culture.Media.Video games                    0.894
		Culture.Performing arts                      0.679
		Culture.Philosophy and religion              0.561
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.737
		Culture.Visual arts.Comics and Anime         0.814
		Culture.Visual arts.Fashion                  0.677
		Culture.Visual arts.Visual arts*             0.759
		Geography.Geographical                       0.65
		Geography.Regions.Africa.Africa*             0.876
		Geography.Regions.Africa.Central Africa      0.768
		Geography.Regions.Africa.Eastern Africa      0.825
		Geography.Regions.Africa.Northern Africa     0.735
		Geography.Regions.Africa.Southern Africa     0.794
		Geography.Regions.Africa.Western Africa      0.831
		Geography.Regions.Americas.Central America   0.733
		Geography.Regions.Americas.North America     0.713
		Geography.Regions.Americas.South America     0.761
		Geography.Regions.Asia.Asia*                 0.863
		Geography.Regions.Asia.Central Asia          0.76
		Geography.Regions.Asia.East Asia             0.776
		Geography.Regions.Asia.North Asia            0.722
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.789
		Geography.Regions.Asia.West Asia             0.81
		Geography.Regions.Europe.Eastern Europe      0.785
		Geography.Regions.Europe.Europe*             0.778
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.72
		Geography.Regions.Europe.Western Europe      0.707
		Geography.Regions.Oceania                    0.826
		History and Society.Business and economics   0.481
		History and Society.Education                0.478
		History and Society.History                  0.407
		History and Society.Military and warfare     0.686
		History and Society.Politics and government  0.493
		History and Society.Society                  0.286
		History and Society.Transportation           0.866
		STEM.Biology                                 0.822
		STEM.Chemistry                               0.699
		STEM.Computing                               0.675
		STEM.Earth and environment                   0.692
		STEM.Engineering                             0.717
		STEM.Libraries & Information                 0.61
		STEM.Mathematics                             0.673
		STEM.Medicine & Health                       0.662
		STEM.Physics                                 0.621
		STEM.STEM*                                   0.87
		STEM.Space                                   0.859
		STEM.Technology                              0.611
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.993
		History and Society.Society                  0.996
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
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.71, macro=0.59):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.834
		Culture.Biography.Women                      0.485
		Culture.Food and drink                       0.641
		Culture.Internet culture                     0.465
		Culture.Linguistics                          0.779
		Culture.Literature                           0.608
		Culture.Media.Books                          0.552
		Culture.Media.Entertainment                  0.388
		Culture.Media.Films                          0.8
		Culture.Media.Media*                         0.634
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.849
		Culture.Media.Software                       0.12
		Culture.Media.Television                     0.685
		Culture.Media.Video games                    0.827
		Culture.Performing arts                      0.57
		Culture.Philosophy and religion              0.531
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.634
		Culture.Visual arts.Comics and Anime         0.591
		Culture.Visual arts.Fashion                  0.339
		Culture.Visual arts.Visual arts*             0.606
		Geography.Geographical                       0.758
		Geography.Regions.Africa.Africa*             0.525
		Geography.Regions.Africa.Central Africa      0.461
		Geography.Regions.Africa.Eastern Africa      0.369
		Geography.Regions.Africa.Northern Africa     0.393
		Geography.Regions.Africa.Southern Africa     0.563
		Geography.Regions.Africa.Western Africa      0.346
		Geography.Regions.Americas.Central America   0.687
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.727
		Geography.Regions.Asia.Asia*                 0.747
		Geography.Regions.Asia.Central Asia          0.434
		Geography.Regions.Asia.East Asia             0.71
		Geography.Regions.Asia.North Asia            0.539
		Geography.Regions.Asia.South Asia            0.893
		Geography.Regions.Asia.Southeast Asia        0.73
		Geography.Regions.Asia.West Asia             0.814
		Geography.Regions.Europe.Eastern Europe      0.754
		Geography.Regions.Europe.Europe*             0.652
		Geography.Regions.Europe.Northern Europe     0.657
		Geography.Regions.Europe.Southern Europe     0.684
		Geography.Regions.Europe.Western Europe      0.662
		Geography.Regions.Oceania                    0.873
		History and Society.Business and economics   0.361
		History and Society.Education                0.506
		History and Society.History                  0.359
		History and Society.Military and warfare     0.662
		History and Society.Politics and government  0.557
		History and Society.Society                  0.389
		History and Society.Transportation           0.814
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.335
		STEM.Computing                               0.213
		STEM.Earth and environment                   0.638
		STEM.Engineering                             0.587
		STEM.Libraries & Information                 0.302
		STEM.Mathematics                             0.22
		STEM.Medicine & Health                       0.599
		STEM.Physics                                 0.213
		STEM.STEM*                                   0.742
		STEM.Space                                   0.781
		STEM.Technology                              0.227
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
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
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.74, macro=0.638):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.597
		Culture.Food and drink                       0.678
		Culture.Internet culture                     0.583
		Culture.Linguistics                          0.767
		Culture.Literature                           0.675
		Culture.Media.Books                          0.636
		Culture.Media.Entertainment                  0.449
		Culture.Media.Films                          0.81
		Culture.Media.Media*                         0.73
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.825
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.72
		Culture.Media.Video games                    0.859
		Culture.Performing arts                      0.619
		Culture.Philosophy and religion              0.546
		Culture.Sports                               0.912
		Culture.Visual arts.Architecture             0.682
		Culture.Visual arts.Comics and Anime         0.685
		Culture.Visual arts.Fashion                  0.452
		Culture.Visual arts.Visual arts*             0.674
		Geography.Geographical                       0.7
		Geography.Regions.Africa.Africa*             0.656
		Geography.Regions.Africa.Central Africa      0.576
		Geography.Regions.Africa.Eastern Africa      0.509
		Geography.Regions.Africa.Northern Africa     0.512
		Geography.Regions.Africa.Southern Africa     0.659
		Geography.Regions.Africa.Western Africa      0.489
		Geography.Regions.Americas.Central America   0.709
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.744
		Geography.Regions.Asia.Asia*                 0.801
		Geography.Regions.Asia.Central Asia          0.553
		Geography.Regions.Asia.East Asia             0.742
		Geography.Regions.Asia.North Asia            0.617
		Geography.Regions.Asia.South Asia            0.882
		Geography.Regions.Asia.Southeast Asia        0.758
		Geography.Regions.Asia.West Asia             0.812
		Geography.Regions.Europe.Eastern Europe      0.769
		Geography.Regions.Europe.Europe*             0.71
		Geography.Regions.Europe.Northern Europe     0.68
		Geography.Regions.Europe.Southern Europe     0.701
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.849
		History and Society.Business and economics   0.412
		History and Society.Education                0.491
		History and Society.History                  0.382
		History and Society.Military and warfare     0.674
		History and Society.Politics and government  0.523
		History and Society.Society                  0.33
		History and Society.Transportation           0.839
		STEM.Biology                                 0.872
		STEM.Chemistry                               0.453
		STEM.Computing                               0.323
		STEM.Earth and environment                   0.664
		STEM.Engineering                             0.645
		STEM.Libraries & Information                 0.404
		STEM.Mathematics                             0.331
		STEM.Medicine & Health                       0.629
		STEM.Physics                                 0.317
		STEM.STEM*                                   0.801
		STEM.Space                                   0.818
		STEM.Technology                              0.331
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.985
		History and Society.Society                  0.99
		History and Society.Transportation           0.995
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.007
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.023
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.005
		History and Society.Politics and government  0.007
		History and Society.Society                  0.004
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
		STEM.STEM*                                   0.021
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.989
		Culture.Linguistics                          0.981
		Culture.Literature                           0.977
		Culture.Media.Books                          0.982
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.986
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.979
		Culture.Philosophy and religion              0.965
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.974
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.987
		Geography.Regions.Africa.Eastern Africa      0.985
		Geography.Regions.Africa.Northern Africa     0.983
		Geography.Regions.Africa.Southern Africa     0.984
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.984
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.986
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.979
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.978
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.956
		History and Society.Education                0.962
		History and Society.History                  0.945
		History and Society.Military and warfare     0.977
		History and Society.Politics and government  0.957
		History and Society.Society                  0.918
		History and Society.Transportation           0.986
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.983
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.979
		STEM.Engineering                             0.977
		STEM.Libraries & Information                 0.977
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.976
		STEM.Space                                   0.986
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.785, macro=0.66):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.908
		Culture.Biography.Women                      0.579
		Culture.Food and drink                       0.675
		Culture.Internet culture                     0.773
		Culture.Linguistics                          0.77
		Culture.Literature                           0.737
		Culture.Media.Books                          0.672
		Culture.Media.Entertainment                  0.433
		Culture.Media.Films                          0.852
		Culture.Media.Media*                         0.842
		Culture.Media.Music                          0.83
		Culture.Media.Radio                          0.84
		Culture.Media.Software                       0.183
		Culture.Media.Television                     0.735
		Culture.Media.Video games                    0.918
		Culture.Performing arts                      0.615
		Culture.Philosophy and religion              0.524
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.731
		Culture.Visual arts.Comics and Anime         0.7
		Culture.Visual arts.Fashion                  0.441
		Culture.Visual arts.Visual arts*             0.747
		Geography.Geographical                       0.744
		Geography.Regions.Africa.Africa*             0.741
		Geography.Regions.Africa.Central Africa      0.664
		Geography.Regions.Africa.Eastern Africa      0.39
		Geography.Regions.Africa.Northern Africa     0.571
		Geography.Regions.Africa.Southern Africa     0.633
		Geography.Regions.Africa.Western Africa      0.406
		Geography.Regions.Americas.Central America   0.71
		Geography.Regions.Americas.North America     0.757
		Geography.Regions.Americas.South America     0.754
		Geography.Regions.Asia.Asia*                 0.851
		Geography.Regions.Asia.Central Asia          0.617
		Geography.Regions.Asia.East Asia             0.773
		Geography.Regions.Asia.North Asia            0.626
		Geography.Regions.Asia.South Asia            0.915
		Geography.Regions.Asia.Southeast Asia        0.765
		Geography.Regions.Asia.West Asia             0.869
		Geography.Regions.Europe.Eastern Europe      0.809
		Geography.Regions.Europe.Europe*             0.783
		Geography.Regions.Europe.Northern Europe     0.715
		Geography.Regions.Europe.Southern Europe     0.715
		Geography.Regions.Europe.Western Europe      0.698
		Geography.Regions.Oceania                    0.881
		History and Society.Business and economics   0.354
		History and Society.Education                0.455
		History and Society.History                  0.323
		History and Society.Military and warfare     0.734
		History and Society.Politics and government  0.506
		History and Society.Society                  0.294
		History and Society.Transportation           0.88
		STEM.Biology                                 0.917
		STEM.Chemistry                               0.444
		STEM.Computing                               0.287
		STEM.Earth and environment                   0.675
		STEM.Engineering                             0.66
		STEM.Libraries & Information                 0.421
		STEM.Mathematics                             0.407
		STEM.Medicine & Health                       0.615
		STEM.Physics                                 0.294
		STEM.STEM*                                   0.89
		STEM.Space                                   0.855
		STEM.Technology                              0.374
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}}, 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

