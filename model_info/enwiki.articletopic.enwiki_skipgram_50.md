Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'verbose': 0, 'min_samples_split': 2, 'min_impurity_split': None, 'max_leaf_nodes': None, 'center': False, 'population_rates': None, 'multilabel': True, 'label_weights': {}, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 13, 'n_iter_no_change': None, 'warm_start': False, 'learning_rate': 0.1, 'scale': False, 'init': None, 'n_estimators': 500, 'validation_fraction': 0.1, 'loss': 'deviance', 'random_state': None, 'min_impurity_decrease': 0.0, 'criterion': 'friedman_mse', 'presort': 'auto', 'min_samples_leaf': 1, 'max_features': 'log2', 'tol': 0.0001, 'subsample': 1.0}
	Environment:
	 - revscoring_version: '2.6.2-no_zero_vectors'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.11'
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
	counts (n=63017):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16717  -->  14266  2451  1050  45250
			'Culture.Biography.Women'                       4173  -->    845  3328   292  58552
			'Culture.Food and drink'                        1323  -->    721   602    56  61638
			'Culture.Internet culture'                      2946  -->   1801  1145    95  59976
			'Culture.Linguistics'                           1384  -->    912   472    51  61582
			'Culture.Literature'                            5277  -->   3422  1855   440  57300
			'Culture.Media.Books'                           1919  -->    933   986   104  60994
			'Culture.Media.Entertainment'                   1876  -->    441  1435    42  61099
			'Culture.Media.Films'                           2307  -->   1559   748    70  60640
			'Culture.Media.Media*'                         14363  -->  11809  2554  1707  46947
			'Culture.Media.Music'                           2677  -->   1986   691   240  60100
			'Culture.Media.Radio'                           1174  -->    814   360    47  61796
			'Culture.Media.Software'                        1798  -->    780  1018   306  60913
			'Culture.Media.Television'                      2200  -->   1113  1087   143  60674
			'Culture.Media.Video games'                     2078  -->   1534   544    18  60921
			'Culture.Performing arts'                       1334  -->    472   862    76  61607
			'Culture.Philosophy and religion'               2638  -->    927  1711   185  60194
			'Culture.Sports'                                5843  -->   5124   719   361  56813
			'Culture.Visual arts.Architecture'              2565  -->   1623   942   255  60197
			'Culture.Visual arts.Comics and Anime'          1488  -->    605   883    68  61461
			'Culture.Visual arts.Fashion'                   1188  -->    449   739    40  61789
			'Culture.Visual arts.Visual arts*'              5987  -->   3484  2503   436  56594
			'Geography.Geographical'                        3344  -->   1894  1450   224  59449
			'Geography.Regions.Africa.Africa*'              5693  -->   1043  4650   210  57114
			'Geography.Regions.Africa.Central Africa'         28  -->      1    27    40  62949
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    163   951    23  61880
			'Geography.Regions.Africa.Northern Africa'      1266  -->    116  1150    50  61701
			'Geography.Regions.Africa.Southern Africa'      1288  -->    217  1071    24  61705
			'Geography.Regions.Africa.Western Africa'       1152  -->    103  1049    19  61846
			'Geography.Regions.Americas.Central America'    1326  -->     77  1249    25  61666
			'Geography.Regions.Americas.North America'      7565  -->   2462  5103   345  55107
			'Geography.Regions.Americas.South America'      1523  -->    176  1347    49  61445
			'Geography.Regions.Asia.Asia*'                 11060  -->   3671  7389   591  51366
			'Geography.Regions.Asia.Central Asia'           1163  -->    197   966    27  61827
			'Geography.Regions.Asia.East Asia'              2721  -->    374  2347    51  60245
			'Geography.Regions.Asia.North Asia'             1361  -->    157  1204    34  61622
			'Geography.Regions.Asia.South Asia'             2438  -->    478  1960    30  60549
			'Geography.Regions.Asia.Southeast Asia'         1688  -->     78  1610    11  61318
			'Geography.Regions.Asia.West Asia'              2264  -->    909  1355    13  60740
			'Geography.Regions.Europe.Eastern Europe'       3083  -->    643  2440    59  59875
			'Geography.Regions.Europe.Europe*'             12415  -->   4291  8124  1163  49439
			'Geography.Regions.Europe.Northern Europe'      4244  -->    503  3741    80  58693
			'Geography.Regions.Europe.Southern Europe'      2320  -->    278  2042    42  60655
			'Geography.Regions.Europe.Western Europe'       3160  -->    630  2530   121  59736
			'Geography.Regions.Oceania'                     2537  -->    257  2280    26  60454
			'History and Society.Business and economics'    3430  -->   1331  2099   377  59210
			'History and Society.Education'                 2178  -->    912  1266   151  60688
			'History and Society.History'                   3217  -->    588  2629   166  59634
			'History and Society.Military and warfare'      3977  -->   2020  1957   237  58803
			'History and Society.Politics and government'   4647  -->   1286  3361   298  58072
			'History and Society.Society'                   4057  -->    489  3568    53  58907
			'History and Society.Transportation'            3604  -->   2759   845   191  59222
			'STEM.Biology'                                  2834  -->   2147   687   101  60082
			'STEM.Chemistry'                                1344  -->    798   546   155  61518
			'STEM.Computing'                                2011  -->   1098   913   350  60656
			'STEM.Earth and environment'                    1683  -->    853   830    66  61268
			'STEM.Engineering'                              2272  -->   1219  1053    87  60658
			'STEM.Libraries & Information'                  1159  -->    323   836    44  61814
			'STEM.Mathematics'                              1121  -->    533   588    91  61805
			'STEM.Medicine & Health'                        1737  -->    967   770   136  61144
			'STEM.Physics'                                  1206  -->    551   655   114  61697
			'STEM.STEM*'                                   16499  -->  13539  2960  1068  45450
			'STEM.Space'                                    1398  -->    943   455    19  61600
			'STEM.Technology'                               3712  -->   1713  1999   552  58753
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.265         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.047         0.004
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.228         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.029         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.093         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.053         0.024
		Geography.Regions.Africa.Africa*                0.09          0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.12          0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.176         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.197         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.05          0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.262         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.059         0.005
	match_rate (micro=0.042, macro=0.012):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.006
		Culture.Literature                           0.018
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.008
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.007
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.018
		Geography.Geographical                       0.017
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.027
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.026
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.003
		Geography.Regions.Asia.Southeast Asia        0
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.048
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.01
		History and Society.Education                0.006
		History and Society.History                  0.005
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.013
		History and Society.Society                  0.002
		History and Society.Transportation           0.015
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.078
		STEM.Space                                   0.004
		STEM.Technology                              0.012
		-------------------------------------------  -----
	filter_rate (micro=0.958, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.994
		Culture.Literature                           0.982
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.992
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        1
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.995
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.987
		History and Society.Society                  0.998
		History and Society.Transportation           0.985
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.922
		STEM.Space                                   0.996
		STEM.Technology                              0.988
		-------------------------------------------  -----
	recall (micro=0.535, macro=0.407):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.853
		Culture.Biography.Women                      0.202
		Culture.Food and drink                       0.545
		Culture.Internet culture                     0.611
		Culture.Linguistics                          0.659
		Culture.Literature                           0.648
		Culture.Media.Books                          0.486
		Culture.Media.Entertainment                  0.235
		Culture.Media.Films                          0.676
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.742
		Culture.Media.Radio                          0.693
		Culture.Media.Software                       0.434
		Culture.Media.Television                     0.506
		Culture.Media.Video games                    0.738
		Culture.Performing arts                      0.354
		Culture.Philosophy and religion              0.351
		Culture.Sports                               0.877
		Culture.Visual arts.Architecture             0.633
		Culture.Visual arts.Comics and Anime         0.407
		Culture.Visual arts.Fashion                  0.378
		Culture.Visual arts.Visual arts*             0.582
		Geography.Geographical                       0.566
		Geography.Regions.Africa.Africa*             0.183
		Geography.Regions.Africa.Central Africa      0.036
		Geography.Regions.Africa.Eastern Africa      0.146
		Geography.Regions.Africa.Northern Africa     0.092
		Geography.Regions.Africa.Southern Africa     0.168
		Geography.Regions.Africa.Western Africa      0.089
		Geography.Regions.Americas.Central America   0.058
		Geography.Regions.Americas.North America     0.325
		Geography.Regions.Americas.South America     0.116
		Geography.Regions.Asia.Asia*                 0.332
		Geography.Regions.Asia.Central Asia          0.169
		Geography.Regions.Asia.East Asia             0.137
		Geography.Regions.Asia.North Asia            0.115
		Geography.Regions.Asia.South Asia            0.196
		Geography.Regions.Asia.Southeast Asia        0.046
		Geography.Regions.Asia.West Asia             0.402
		Geography.Regions.Europe.Eastern Europe      0.209
		Geography.Regions.Europe.Europe*             0.346
		Geography.Regions.Europe.Northern Europe     0.119
		Geography.Regions.Europe.Southern Europe     0.12
		Geography.Regions.Europe.Western Europe      0.199
		Geography.Regions.Oceania                    0.101
		History and Society.Business and economics   0.388
		History and Society.Education                0.419
		History and Society.History                  0.183
		History and Society.Military and warfare     0.508
		History and Society.Politics and government  0.277
		History and Society.Society                  0.121
		History and Society.Transportation           0.766
		STEM.Biology                                 0.758
		STEM.Chemistry                               0.594
		STEM.Computing                               0.546
		STEM.Earth and environment                   0.507
		STEM.Engineering                             0.537
		STEM.Libraries & Information                 0.279
		STEM.Mathematics                             0.475
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.457
		STEM.STEM*                                   0.821
		STEM.Space                                   0.675
		STEM.Technology                              0.461
		-------------------------------------------  -----
	!recall (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.997
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.996
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   1
		Geography.Regions.Americas.North America     0.994
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.999
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            1
		Geography.Regions.Asia.Southeast Asia        1
		Geography.Regions.Asia.West Asia             1
		Geography.Regions.Europe.Eastern Europe      0.999
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.999
		Geography.Regions.Europe.Southern Europe     0.999
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    1
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.997
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.995
		History and Society.Society                  0.999
		History and Society.Transportation           0.997
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.977
		STEM.Space                                   1
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.7, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.841
		Culture.Biography.Women                      0.376
		Culture.Food and drink                       0.597
		Culture.Internet culture                     0.576
		Culture.Linguistics                          0.855
		Culture.Literature                           0.573
		Culture.Media.Books                          0.536
		Culture.Media.Entertainment                  0.552
		Culture.Media.Films                          0.862
		Culture.Media.Media*                         0.593
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.663
		Culture.Media.Software                       0.104
		Culture.Media.Television                     0.657
		Culture.Media.Video games                    0.868
		Culture.Performing arts                      0.454
		Culture.Philosophy and religion              0.553
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.448
		Culture.Visual arts.Fashion                  0.321
		Culture.Visual arts.Visual arts*             0.587
		Geography.Geographical                       0.785
		Geography.Regions.Africa.Africa*             0.282
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.152
		Geography.Regions.Africa.Northern Africa     0.122
		Geography.Regions.Africa.Southern Africa     0.338
		Geography.Regions.Africa.Western Africa      0.166
		Geography.Regions.Americas.Central America   0.322
		Geography.Regions.Americas.North America     0.782
		Geography.Regions.Americas.South America     0.479
		Geography.Regions.Asia.Asia*                 0.582
		Geography.Regions.Asia.Central Asia          0.252
		Geography.Regions.Asia.East Asia             0.652
		Geography.Regions.Asia.North Asia            0.162
		Geography.Regions.Asia.South Asia            0.859
		Geography.Regions.Asia.Southeast Asia        0.609
		Geography.Regions.Asia.West Asia             0.954
		Geography.Regions.Europe.Eastern Europe      0.734
		Geography.Regions.Europe.Europe*             0.554
		Geography.Regions.Europe.Northern Europe     0.733
		Geography.Regions.Europe.Southern Europe     0.696
		Geography.Regions.Europe.Western Europe      0.659
		Geography.Regions.Oceania                    0.784
		History and Society.Business and economics   0.385
		History and Society.Education                0.556
		History and Society.History                  0.419
		History and Society.Military and warfare     0.644
		History and Society.Politics and government  0.611
		History and Society.Society                  0.631
		History and Society.Transportation           0.785
		STEM.Biology                                 0.94
		STEM.Chemistry                               0.27
		STEM.Computing                               0.204
		STEM.Earth and environment                   0.682
		STEM.Engineering                             0.664
		STEM.Libraries & Information                 0.196
		STEM.Mathematics                             0.119
		STEM.Medicine & Health                       0.618
		STEM.Physics                                 0.174
		STEM.STEM*                                   0.726
		STEM.Space                                   0.93
		STEM.Technology                              0.204
		-------------------------------------------  -----
	!precision (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.979
		History and Society.Society                  0.989
		History and Society.Transportation           0.996
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.998
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.572, macro=0.426):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.847
		Culture.Biography.Women                      0.263
		Culture.Food and drink                       0.57
		Culture.Internet culture                     0.593
		Culture.Linguistics                          0.744
		Culture.Literature                           0.608
		Culture.Media.Books                          0.51
		Culture.Media.Entertainment                  0.33
		Culture.Media.Films                          0.758
		Culture.Media.Media*                         0.689
		Culture.Media.Music                          0.779
		Culture.Media.Radio                          0.678
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.572
		Culture.Media.Video games                    0.798
		Culture.Performing arts                      0.398
		Culture.Philosophy and religion              0.43
		Culture.Sports                               0.895
		Culture.Visual arts.Architecture             0.624
		Culture.Visual arts.Comics and Anime         0.426
		Culture.Visual arts.Fashion                  0.347
		Culture.Visual arts.Visual arts*             0.584
		Geography.Geographical                       0.658
		Geography.Regions.Africa.Africa*             0.222
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.149
		Geography.Regions.Africa.Northern Africa     0.105
		Geography.Regions.Africa.Southern Africa     0.225
		Geography.Regions.Africa.Western Africa      0.116
		Geography.Regions.Americas.Central America   0.098
		Geography.Regions.Americas.North America     0.46
		Geography.Regions.Americas.South America     0.186
		Geography.Regions.Asia.Asia*                 0.423
		Geography.Regions.Asia.Central Asia          0.203
		Geography.Regions.Asia.East Asia             0.227
		Geography.Regions.Asia.North Asia            0.135
		Geography.Regions.Asia.South Asia            0.319
		Geography.Regions.Asia.Southeast Asia        0.086
		Geography.Regions.Asia.West Asia             0.565
		Geography.Regions.Europe.Eastern Europe      0.325
		Geography.Regions.Europe.Europe*             0.426
		Geography.Regions.Europe.Northern Europe     0.204
		Geography.Regions.Europe.Southern Europe     0.204
		Geography.Regions.Europe.Western Europe      0.306
		Geography.Regions.Oceania                    0.179
		History and Society.Business and economics   0.386
		History and Society.Education                0.478
		History and Society.History                  0.255
		History and Society.Military and warfare     0.568
		History and Society.Politics and government  0.381
		History and Society.Society                  0.202
		History and Society.Transportation           0.775
		STEM.Biology                                 0.839
		STEM.Chemistry                               0.371
		STEM.Computing                               0.297
		STEM.Earth and environment                   0.582
		STEM.Engineering                             0.593
		STEM.Libraries & Information                 0.23
		STEM.Mathematics                             0.19
		STEM.Medicine & Health                       0.586
		STEM.Physics                                 0.252
		STEM.STEM*                                   0.771
		STEM.Space                                   0.782
		STEM.Technology                              0.283
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.987
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
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
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.959
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.929
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.988
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.975
		History and Society.Society                  0.988
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.011, macro=0.004):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.023
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.002
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.001
		Culture.Media.Films                          0.001
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.001
		Culture.Philosophy and religion              0.003
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.004
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0
		Geography.Regions.Americas.North America     0.006
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.011
		Geography.Regions.Asia.Central Asia          0
		Geography.Regions.Asia.East Asia             0.001
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0
		Geography.Regions.Asia.Southeast Asia        0
		Geography.Regions.Asia.West Asia             0
		Geography.Regions.Europe.Eastern Europe      0.001
		Geography.Regions.Europe.Europe*             0.023
		Geography.Regions.Europe.Northern Europe     0.001
		Geography.Regions.Europe.Southern Europe     0.001
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.003
		History and Society.Military and warfare     0.004
		History and Society.Politics and government  0.005
		History and Society.Society                  0.001
		History and Society.Transportation           0.003
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.001
		STEM.Engineering                             0.001
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.023
		STEM.Space                                   0
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.899, macro=0.856):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.893
		Culture.Food and drink                       0.902
		Culture.Internet culture                     0.944
		Culture.Linguistics                          0.916
		Culture.Literature                           0.948
		Culture.Media.Books                          0.931
		Culture.Media.Entertainment                  0.87
		Culture.Media.Films                          0.941
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.96
		Culture.Media.Radio                          0.923
		Culture.Media.Software                       0.919
		Culture.Media.Television                     0.928
		Culture.Media.Video games                    0.948
		Culture.Performing arts                      0.885
		Culture.Philosophy and religion              0.885
		Culture.Sports                               0.97
		Culture.Visual arts.Architecture             0.938
		Culture.Visual arts.Comics and Anime         0.912
		Culture.Visual arts.Fashion                  0.904
		Culture.Visual arts.Visual arts*             0.944
		Geography.Geographical                       0.913
		Geography.Regions.Africa.Africa*             0.83
		Geography.Regions.Africa.Central Africa      0.518
		Geography.Regions.Africa.Eastern Africa      0.687
		Geography.Regions.Africa.Northern Africa     0.643
		Geography.Regions.Africa.Southern Africa     0.702
		Geography.Regions.Africa.Western Africa      0.694
		Geography.Regions.Americas.Central America   0.635
		Geography.Regions.Americas.North America     0.871
		Geography.Regions.Americas.South America     0.728
		Geography.Regions.Asia.Asia*                 0.867
		Geography.Regions.Asia.Central Asia          0.688
		Geography.Regions.Asia.East Asia             0.766
		Geography.Regions.Asia.North Asia            0.724
		Geography.Regions.Asia.South Asia            0.786
		Geography.Regions.Asia.Southeast Asia        0.636
		Geography.Regions.Asia.West Asia             0.794
		Geography.Regions.Europe.Eastern Europe      0.802
		Geography.Regions.Europe.Europe*             0.861
		Geography.Regions.Europe.Northern Europe     0.775
		Geography.Regions.Europe.Southern Europe     0.746
		Geography.Regions.Europe.Western Europe      0.802
		Geography.Regions.Oceania                    0.749
		History and Society.Business and economics   0.914
		History and Society.Education                0.875
		History and Society.History                  0.842
		History and Society.Military and warfare     0.897
		History and Society.Politics and government  0.836
		History and Society.Society                  0.77
		History and Society.Transportation           0.961
		STEM.Biology                                 0.946
		STEM.Chemistry                               0.935
		STEM.Computing                               0.938
		STEM.Earth and environment                   0.903
		STEM.Engineering                             0.916
		STEM.Libraries & Information                 0.851
		STEM.Mathematics                             0.897
		STEM.Medicine & Health                       0.91
		STEM.Physics                                 0.913
		STEM.STEM*                                   0.968
		STEM.Space                                   0.949
		STEM.Technology                              0.925
		-------------------------------------------  -----
	pr_auc (micro=0.617, macro=0.435):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.247
		Culture.Food and drink                       0.545
		Culture.Internet culture                     0.653
		Culture.Linguistics                          0.758
		Culture.Literature                           0.656
		Culture.Media.Books                          0.487
		Culture.Media.Entertainment                  0.312
		Culture.Media.Films                          0.775
		Culture.Media.Media*                         0.789
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.741
		Culture.Media.Software                       0.141
		Culture.Media.Television                     0.594
		Culture.Media.Video games                    0.828
		Culture.Performing arts                      0.383
		Culture.Philosophy and religion              0.41
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.672
		Culture.Visual arts.Comics and Anime         0.388
		Culture.Visual arts.Fashion                  0.266
		Culture.Visual arts.Visual arts*             0.594
		Geography.Geographical                       0.723
		Geography.Regions.Africa.Africa*             0.161
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.077
		Geography.Regions.Africa.Northern Africa     0.035
		Geography.Regions.Africa.Southern Africa     0.144
		Geography.Regions.Africa.Western Africa      0.063
		Geography.Regions.Americas.Central America   0.065
		Geography.Regions.Americas.North America     0.562
		Geography.Regions.Americas.South America     0.179
		Geography.Regions.Asia.Asia*                 0.453
		Geography.Regions.Asia.Central Asia          0.12
		Geography.Regions.Asia.East Asia             0.28
		Geography.Regions.Asia.North Asia            0.057
		Geography.Regions.Asia.South Asia            0.415
		Geography.Regions.Asia.Southeast Asia        0.085
		Geography.Regions.Asia.West Asia             0.525
		Geography.Regions.Europe.Eastern Europe      0.346
		Geography.Regions.Europe.Europe*             0.468
		Geography.Regions.Europe.Northern Europe     0.311
		Geography.Regions.Europe.Southern Europe     0.252
		Geography.Regions.Europe.Western Europe      0.349
		Geography.Regions.Oceania                    0.254
		History and Society.Business and economics   0.343
		History and Society.Education                0.426
		History and Society.History                  0.249
		History and Society.Military and warfare     0.571
		History and Society.Politics and government  0.41
		History and Society.Society                  0.213
		History and Society.Transportation           0.819
		STEM.Biology                                 0.892
		STEM.Chemistry                               0.433
		STEM.Computing                               0.235
		STEM.Earth and environment                   0.57
		STEM.Engineering                             0.59
		STEM.Libraries & Information                 0.212
		STEM.Mathematics                             0.274
		STEM.Medicine & Health                       0.593
		STEM.Physics                                 0.257
		STEM.STEM*                                   0.842
		STEM.Space                                   0.84
		STEM.Technology                              0.275
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}, 'type': 'object'}

