Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.9'
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
	counts (n=56444):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14111  -->  12792  1319   690  41643
			'Culture.Biography.Women'                       3558  -->   2491  1067   324  52562
			'Culture.Food and drink'                        1464  -->   1064   400   111  54869
			'Culture.Internet culture'                      2157  -->   1885   272   144  54143
			'Culture.Linguistics'                           2171  -->   1623   548   142  54131
			'Culture.Literature'                            4875  -->   3743  1132   407  51162
			'Culture.Media.Books'                           1305  -->   1083   222    73  55066
			'Culture.Media.Entertainment'                   2110  -->   1216   894   252  54082
			'Culture.Media.Films'                           3102  -->   2853   249    83  53259
			'Culture.Media.Media*'                         11523  -->  10170  1353   956  43965
			'Culture.Media.Music'                           2715  -->   2334   381   133  53596
			'Culture.Media.Radio'                            253  -->    189    64    28  56163
			'Culture.Media.Software'                        2005  -->   1867   138   178  54261
			'Culture.Media.Television'                      1733  -->   1403   330    86  54625
			'Culture.Media.Video games'                      651  -->    615    36    20  55773
			'Culture.Performing arts'                       1551  -->    977   574   110  54783
			'Culture.Philosophy and religion'               4242  -->   2436  1806   370  51832
			'Culture.Sports'                                3639  -->   2935   704   137  52668
			'Culture.Visual arts.Architecture'              2502  -->   1953   549   243  53699
			'Culture.Visual arts.Comics and Anime'          1161  -->   1008   153    39  55244
			'Culture.Visual arts.Fashion'                    618  -->    428   190    40  55786
			'Culture.Visual arts.Visual arts*'              4969  -->   3733  1236   384  51091
			'Geography.Geographical'                        4627  -->   3220  1407   643  51174
			'Geography.Regions.Africa.Africa*'              3906  -->   2632  1274   322  52216
			'Geography.Regions.Africa.Central Africa'        808  -->    503   305    85  55551
			'Geography.Regions.Africa.Eastern Africa'        360  -->    234   126    22  56062
			'Geography.Regions.Africa.Northern Africa'      1527  -->   1045   482   115  54802
			'Geography.Regions.Africa.Southern Africa'       590  -->    387   203    41  55813
			'Geography.Regions.Africa.Western Africa'         77  -->     49    28    24  56343
			'Geography.Regions.Americas.Central America'    1406  -->    814   592   138  54900
			'Geography.Regions.Americas.North America'      6544  -->   4963  1581   763  49137
			'Geography.Regions.Americas.South America'      1784  -->   1373   411   122  54538
			'Geography.Regions.Asia.Asia*'                  9866  -->   7962  1904   829  45749
			'Geography.Regions.Asia.Central Asia'            928  -->    688   240    74  55442
			'Geography.Regions.Asia.East Asia'              3315  -->   2750   565   180  52949
			'Geography.Regions.Asia.North Asia'             1410  -->   1202   208   120  54914
			'Geography.Regions.Asia.South Asia'             1800  -->   1294   506   104  54540
			'Geography.Regions.Asia.Southeast Asia'         1750  -->    968   782   191  54503
			'Geography.Regions.Asia.West Asia'              2383  -->   1862   521   135  53926
			'Geography.Regions.Europe.Eastern Europe'       3057  -->   2564   493   162  53225
			'Geography.Regions.Europe.Europe*'             16976  -->  14458  2518  1901  37567
			'Geography.Regions.Europe.Northern Europe'      4149  -->   3271   878   310  51985
			'Geography.Regions.Europe.Southern Europe'      5477  -->   4245  1232   644  50323
			'Geography.Regions.Europe.Western Europe'       5201  -->   4151  1050   393  50850
			'Geography.Regions.Oceania'                     1895  -->   1318   577   149  54400
			'History and Society.Business and economics'    3125  -->   2030  1095   230  53089
			'History and Society.Education'                 1777  -->    921   856   116  54551
			'History and Society.History'                   6150  -->   4002  2148   725  49569
			'History and Society.Military and warfare'      4199  -->   2821  1378   408  51837
			'History and Society.Politics and government'   4713  -->   2715  1998   504  51227
			'History and Society.Society'                   6946  -->   3529  3417   657  48841
			'History and Society.Transportation'            2533  -->   2132   401    73  53838
			'STEM.Biology'                                  6821  -->   6232   589   159  49464
			'STEM.Chemistry'                                1541  -->   1273   268   107  54796
			'STEM.Computing'                                2464  -->   2198   266   142  53838
			'STEM.Earth and environment'                    1875  -->   1366   509   103  54466
			'STEM.Engineering'                              2557  -->   1862   695   201  53686
			'STEM.Libraries & Information'                   476  -->    371   105    31  55937
			'STEM.Mathematics'                              1069  -->    950   119    33  55342
			'STEM.Medicine & Health'                        1942  -->   1393   549   132  54370
			'STEM.Physics'                                  1574  -->   1210   364   138  54732
			'STEM.STEM*'                                   19988  -->  18321  1667   805  35651
			'STEM.Space'                                    1879  -->   1736   143    28  54537
			'STEM.Technology'                               4389  -->   3453   936   530  51525
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.25          0.123
		Culture.Biography.Women                         0.063         0.015
		Culture.Food and drink                          0.026         0.002
		Culture.Internet culture                        0.038         0.003
		Culture.Linguistics                             0.038         0.007
		Culture.Literature                              0.086         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.055         0.011
		Culture.Media.Media*                            0.204         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.031         0.009
		Culture.Media.Video games                       0.012         0.003
		Culture.Performing arts                         0.027         0.003
		Culture.Philosophy and religion                 0.075         0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.088         0.018
		Geography.Geographical                          0.082         0.024
		Geography.Regions.Africa.Africa*                0.069         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.027         0.001
		Geography.Regions.Africa.Southern Africa        0.01          0.001
		Geography.Regions.Africa.Western Africa         0.001         0.001
		Geography.Regions.Americas.Central America      0.025         0.003
		Geography.Regions.Americas.North America        0.116         0.064
		Geography.Regions.Americas.South America        0.032         0.006
		Geography.Regions.Asia.Asia*                    0.175         0.045
		Geography.Regions.Asia.Central Asia             0.016         0.001
		Geography.Regions.Asia.East Asia                0.059         0.011
		Geography.Regions.Asia.North Asia               0.025         0.001
		Geography.Regions.Asia.South Asia               0.032         0.015
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.042         0.011
		Geography.Regions.Europe.Eastern Europe         0.054         0.013
		Geography.Regions.Europe.Europe*                0.301         0.076
		Geography.Regions.Europe.Northern Europe        0.074         0.031
		Geography.Regions.Europe.Southern Europe        0.097         0.013
		Geography.Regions.Europe.Western Europe         0.092         0.019
		Geography.Regions.Oceania                       0.034         0.015
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.109         0.011
		History and Society.Military and warfare        0.074         0.014
		History and Society.Politics and government     0.083         0.028
		History and Society.Society                     0.123         0.013
		History and Society.Transportation              0.045         0.015
		STEM.Biology                                    0.121         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.044         0.003
		STEM.Earth and environment                      0.033         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.028         0.001
		STEM.STEM*                                      0.354         0.069
		STEM.Space                                      0.033         0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.008
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.072
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.06
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.063
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.109
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.02
		History and Society.Transportation           0.014
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.992
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.928
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.891
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.98
		History and Society.Transportation           0.986
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.802, macro=0.756):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.907
		Culture.Biography.Women                      0.7
		Culture.Food and drink                       0.727
		Culture.Internet culture                     0.874
		Culture.Linguistics                          0.748
		Culture.Literature                           0.768
		Culture.Media.Books                          0.83
		Culture.Media.Entertainment                  0.576
		Culture.Media.Films                          0.92
		Culture.Media.Media*                         0.883
		Culture.Media.Music                          0.86
		Culture.Media.Radio                          0.747
		Culture.Media.Software                       0.931
		Culture.Media.Television                     0.81
		Culture.Media.Video games                    0.945
		Culture.Performing arts                      0.63
		Culture.Philosophy and religion              0.574
		Culture.Sports                               0.807
		Culture.Visual arts.Architecture             0.781
		Culture.Visual arts.Comics and Anime         0.868
		Culture.Visual arts.Fashion                  0.693
		Culture.Visual arts.Visual arts*             0.751
		Geography.Geographical                       0.696
		Geography.Regions.Africa.Africa*             0.674
		Geography.Regions.Africa.Central Africa      0.623
		Geography.Regions.Africa.Eastern Africa      0.65
		Geography.Regions.Africa.Northern Africa     0.684
		Geography.Regions.Africa.Southern Africa     0.656
		Geography.Regions.Africa.Western Africa      0.636
		Geography.Regions.Americas.Central America   0.579
		Geography.Regions.Americas.North America     0.758
		Geography.Regions.Americas.South America     0.77
		Geography.Regions.Asia.Asia*                 0.807
		Geography.Regions.Asia.Central Asia          0.741
		Geography.Regions.Asia.East Asia             0.83
		Geography.Regions.Asia.North Asia            0.852
		Geography.Regions.Asia.South Asia            0.719
		Geography.Regions.Asia.Southeast Asia        0.553
		Geography.Regions.Asia.West Asia             0.781
		Geography.Regions.Europe.Eastern Europe      0.839
		Geography.Regions.Europe.Europe*             0.852
		Geography.Regions.Europe.Northern Europe     0.788
		Geography.Regions.Europe.Southern Europe     0.775
		Geography.Regions.Europe.Western Europe      0.798
		Geography.Regions.Oceania                    0.696
		History and Society.Business and economics   0.65
		History and Society.Education                0.518
		History and Society.History                  0.651
		History and Society.Military and warfare     0.672
		History and Society.Politics and government  0.576
		History and Society.Society                  0.508
		History and Society.Transportation           0.842
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.826
		STEM.Computing                               0.892
		STEM.Earth and environment                   0.729
		STEM.Engineering                             0.728
		STEM.Libraries & Information                 0.779
		STEM.Mathematics                             0.889
		STEM.Medicine & Health                       0.717
		STEM.Physics                                 0.769
		STEM.STEM*                                   0.917
		STEM.Space                                   0.924
		STEM.Technology                              0.787
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.998
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.987
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.728, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.886
		Culture.Biography.Women                      0.628
		Culture.Food and drink                       0.471
		Culture.Internet culture                     0.536
		Culture.Linguistics                          0.678
		Culture.Literature                           0.605
		Culture.Media.Books                          0.717
		Culture.Media.Entertainment                  0.309
		Culture.Media.Films                          0.863
		Culture.Media.Media*                         0.72
		Culture.Media.Music                          0.895
		Culture.Media.Radio                          0.764
		Culture.Media.Software                       0.275
		Culture.Media.Television                     0.821
		Culture.Media.Video games                    0.873
		Culture.Performing arts                      0.476
		Culture.Philosophy and religion              0.466
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.649
		Culture.Visual arts.Comics and Anime         0.73
		Culture.Visual arts.Fashion                  0.439
		Culture.Visual arts.Visual arts*             0.652
		Geography.Geographical                       0.575
		Geography.Regions.Africa.Africa*             0.464
		Geography.Regions.Africa.Central Africa      0.205
		Geography.Regions.Africa.Eastern Africa      0.43
		Geography.Regions.Africa.Northern Africa     0.286
		Geography.Regions.Africa.Southern Africa     0.512
		Geography.Regions.Africa.Western Africa      0.505
		Geography.Regions.Americas.Central America   0.433
		Geography.Regions.Americas.North America     0.773
		Geography.Regions.Americas.South America     0.686
		Geography.Regions.Asia.Asia*                 0.684
		Geography.Regions.Asia.Central Asia          0.325
		Geography.Regions.Asia.East Asia             0.739
		Geography.Regions.Asia.North Asia            0.266
		Geography.Regions.Asia.South Asia            0.853
		Geography.Regions.Asia.Southeast Asia        0.489
		Geography.Regions.Asia.West Asia             0.775
		Geography.Regions.Europe.Eastern Europe      0.782
		Geography.Regions.Europe.Europe*             0.593
		Geography.Regions.Europe.Northern Europe     0.807
		Geography.Regions.Europe.Southern Europe     0.448
		Geography.Regions.Europe.Western Europe      0.67
		Geography.Regions.Oceania                    0.796
		History and Society.Business and economics   0.605
		History and Society.Education                0.644
		History and Society.History                  0.331
		History and Society.Military and warfare     0.551
		History and Society.Politics and government  0.632
		History and Society.Society                  0.328
		History and Society.Transportation           0.905
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.398
		STEM.Computing                               0.478
		STEM.Earth and environment                   0.637
		STEM.Engineering                             0.507
		STEM.Libraries & Information                 0.467
		STEM.Mathematics                             0.383
		STEM.Medicine & Health                       0.656
		STEM.Physics                                 0.206
		STEM.STEM*                                   0.755
		STEM.Space                                   0.916
		STEM.Technology                              0.285
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.987
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.987
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.757, macro=0.65):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.662
		Culture.Food and drink                       0.571
		Culture.Internet culture                     0.665
		Culture.Linguistics                          0.711
		Culture.Literature                           0.677
		Culture.Media.Books                          0.769
		Culture.Media.Entertainment                  0.402
		Culture.Media.Films                          0.89
		Culture.Media.Media*                         0.793
		Culture.Media.Music                          0.877
		Culture.Media.Radio                          0.755
		Culture.Media.Software                       0.424
		Culture.Media.Television                     0.815
		Culture.Media.Video games                    0.908
		Culture.Performing arts                      0.543
		Culture.Philosophy and religion              0.514
		Culture.Sports                               0.876
		Culture.Visual arts.Architecture             0.709
		Culture.Visual arts.Comics and Anime         0.793
		Culture.Visual arts.Fashion                  0.537
		Culture.Visual arts.Visual arts*             0.698
		Geography.Geographical                       0.63
		Geography.Regions.Africa.Africa*             0.549
		Geography.Regions.Africa.Central Africa      0.308
		Geography.Regions.Africa.Eastern Africa      0.517
		Geography.Regions.Africa.Northern Africa     0.404
		Geography.Regions.Africa.Southern Africa     0.575
		Geography.Regions.Africa.Western Africa      0.563
		Geography.Regions.Americas.Central America   0.496
		Geography.Regions.Americas.North America     0.766
		Geography.Regions.Americas.South America     0.726
		Geography.Regions.Asia.Asia*                 0.74
		Geography.Regions.Asia.Central Asia          0.452
		Geography.Regions.Asia.East Asia             0.781
		Geography.Regions.Asia.North Asia            0.405
		Geography.Regions.Asia.South Asia            0.78
		Geography.Regions.Asia.Southeast Asia        0.519
		Geography.Regions.Asia.West Asia             0.778
		Geography.Regions.Europe.Eastern Europe      0.809
		Geography.Regions.Europe.Europe*             0.699
		Geography.Regions.Europe.Northern Europe     0.798
		Geography.Regions.Europe.Southern Europe     0.567
		Geography.Regions.Europe.Western Europe      0.729
		Geography.Regions.Oceania                    0.742
		History and Society.Business and economics   0.627
		History and Society.Education                0.574
		History and Society.History                  0.439
		History and Society.Military and warfare     0.605
		History and Society.Politics and government  0.603
		History and Society.Society                  0.399
		History and Society.Transportation           0.872
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.537
		STEM.Computing                               0.622
		STEM.Earth and environment                   0.68
		STEM.Engineering                             0.598
		STEM.Libraries & Information                 0.584
		STEM.Mathematics                             0.536
		STEM.Medicine & Health                       0.685
		STEM.Physics                                 0.325
		STEM.STEM*                                   0.828
		STEM.Space                                   0.92
		STEM.Technology                              0.418
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.986
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.986
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.98, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.996
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.992
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.979
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.003
		Culture.Literature                           0.008
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.021
		Culture.Media.Music                          0.002
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.048
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.004
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.013
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.975):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.983
		Culture.Literature                           0.98
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.973
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.948
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.983
		Culture.Performing arts                      0.975
		Culture.Philosophy and religion              0.959
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.978
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.974
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.964
		Geography.Regions.Africa.Northern Africa     0.978
		Geography.Regions.Africa.Southern Africa     0.968
		Geography.Regions.Africa.Western Africa      0.832
		Geography.Regions.Americas.Central America   0.971
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.972
		History and Society.Education                0.97
		History and Society.History                  0.963
		History and Society.Military and warfare     0.974
		History and Society.Politics and government  0.956
		History and Society.Society                  0.938
		History and Society.Transportation           0.985
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.987
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.981
		STEM.Engineering                             0.978
		STEM.Libraries & Information                 0.951
		STEM.Mathematics                             0.99
		STEM.Medicine & Health                       0.978
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.98
		STEM.Space                                   0.992
		STEM.Technology                              0.98
		-------------------------------------------  -----
	pr_auc (micro=0.813, macro=0.667):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.684
		Culture.Food and drink                       0.623
		Culture.Internet culture                     0.76
		Culture.Linguistics                          0.773
		Culture.Literature                           0.743
		Culture.Media.Books                          0.789
		Culture.Media.Entertainment                  0.342
		Culture.Media.Films                          0.929
		Culture.Media.Media*                         0.892
		Culture.Media.Music                          0.903
		Culture.Media.Radio                          0.58
		Culture.Media.Software                       0.569
		Culture.Media.Television                     0.844
		Culture.Media.Video games                    0.936
		Culture.Performing arts                      0.528
		Culture.Philosophy and religion              0.52
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.763
		Culture.Visual arts.Comics and Anime         0.837
		Culture.Visual arts.Fashion                  0.503
		Culture.Visual arts.Visual arts*             0.739
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.584
		Geography.Regions.Africa.Central Africa      0.233
		Geography.Regions.Africa.Eastern Africa      0.324
		Geography.Regions.Africa.Northern Africa     0.364
		Geography.Regions.Africa.Southern Africa     0.423
		Geography.Regions.Africa.Western Africa      0.313
		Geography.Regions.Americas.Central America   0.467
		Geography.Regions.Americas.North America     0.842
		Geography.Regions.Americas.South America     0.806
		Geography.Regions.Asia.Asia*                 0.825
		Geography.Regions.Asia.Central Asia          0.355
		Geography.Regions.Asia.East Asia             0.81
		Geography.Regions.Asia.North Asia            0.362
		Geography.Regions.Asia.South Asia            0.801
		Geography.Regions.Asia.Southeast Asia        0.538
		Geography.Regions.Asia.West Asia             0.778
		Geography.Regions.Europe.Eastern Europe      0.838
		Geography.Regions.Europe.Europe*             0.804
		Geography.Regions.Europe.Northern Europe     0.841
		Geography.Regions.Europe.Southern Europe     0.639
		Geography.Regions.Europe.Western Europe      0.806
		Geography.Regions.Oceania                    0.782
		History and Society.Business and economics   0.64
		History and Society.Education                0.544
		History and Society.History                  0.463
		History and Society.Military and warfare     0.637
		History and Society.Politics and government  0.636
		History and Society.Society                  0.381
		History and Society.Transportation           0.918
		STEM.Biology                                 0.954
		STEM.Chemistry                               0.58
		STEM.Computing                               0.702
		STEM.Earth and environment                   0.705
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.605
		STEM.Mathematics                             0.538
		STEM.Medicine & Health                       0.719
		STEM.Physics                                 0.341
		STEM.STEM*                                   0.922
		STEM.Space                                   0.947
		STEM.Technology                              0.474
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

