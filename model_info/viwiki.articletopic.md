Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'validation_fraction': 0.1, 'criterion': 'friedman_mse', 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_split': 2, 'init': None, 'loss': 'deviance', 'random_state': None, 'multilabel': True, 'learning_rate': 0.1, 'n_iter_no_change': None, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'max_depth': 5, 'warm_start': False, 'max_leaf_nodes': None, 'presort': 'auto', 'scale': False, 'subsample': 1.0, 'n_estimators': 150, 'min_impurity_split': None, 'min_samples_leaf': 1, 'center': False, 'max_features': 'log2', 'verbose': 0}
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
	counts (n=60772):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14138  -->  12738  1400   748  45886
			'Culture.Biography.Women'                       5222  -->   4221  1001   742  54808
			'Culture.Food and drink'                        1399  -->   1035   364   123  59250
			'Culture.Internet culture'                      3585  -->   3017   568   240  56947
			'Culture.Linguistics'                           1530  -->   1192   338    68  59174
			'Culture.Literature'                            5579  -->   4365  1214   476  54717
			'Culture.Media.Books'                           1449  -->   1073   376   132  59191
			'Culture.Media.Entertainment'                   1969  -->   1044   925   183  58620
			'Culture.Media.Films'                           2641  -->   2087   554   158  57973
			'Culture.Media.Media*'                         13313  -->  11727  1586  1189  46270
			'Culture.Media.Music'                           2956  -->   2565   391   174  57642
			'Culture.Media.Radio'                            312  -->    218    94    41  60419
			'Culture.Media.Software'                        2332  -->   1970   362   265  58175
			'Culture.Media.Television'                      1996  -->   1456   540   152  58624
			'Culture.Media.Video games'                     2140  -->   1963   177    49  58583
			'Culture.Performing arts'                       1373  -->    947   426   122  59277
			'Culture.Philosophy and religion'               3073  -->   1771  1302   241  57458
			'Culture.Sports'                                3923  -->   3455   468   116  56733
			'Culture.Visual arts.Architecture'              1858  -->   1348   510   174  58740
			'Culture.Visual arts.Comics and Anime'          2172  -->   1973   199    77  58523
			'Culture.Visual arts.Fashion'                   1501  -->   1240   261   101  59170
			'Culture.Visual arts.Visual arts*'              6025  -->   4735  1290   393  54354
			'Geography.Geographical'                        4036  -->   2629  1407   497  56239
			'Geography.Regions.Africa.Africa*'              5693  -->   4462  1231   454  54625
			'Geography.Regions.Africa.Central Africa'       1196  -->    778   418   108  59468
			'Geography.Regions.Africa.Eastern Africa'        450  -->    227   223    58  60264
			'Geography.Regions.Africa.Northern Africa'      1504  -->   1082   422    96  59172
			'Geography.Regions.Africa.Southern Africa'      1162  -->    787   375    81  59529
			'Geography.Regions.Africa.Western Africa'        710  -->    571   139    47  60015
			'Geography.Regions.Americas.Central America'    1601  -->   1065   536   107  59064
			'Geography.Regions.Americas.North America'      5406  -->   3702  1704   629  54737
			'Geography.Regions.Americas.South America'      2233  -->   1730   503   214  58325
			'Geography.Regions.Asia.Asia*'                 13787  -->  11579  2208  1093  45892
			'Geography.Regions.Asia.Central Asia'           1209  -->    877   332    76  59487
			'Geography.Regions.Asia.East Asia'              5547  -->   4485  1062   463  54762
			'Geography.Regions.Asia.North Asia'             1674  -->   1228   446   190  58908
			'Geography.Regions.Asia.South Asia'             1986  -->   1578   408   100  58686
			'Geography.Regions.Asia.Southeast Asia'         2650  -->   1985   665   194  57928
			'Geography.Regions.Asia.West Asia'              2210  -->   1792   418    97  58465
			'Geography.Regions.Europe.Eastern Europe'       3591  -->   2877   714   275  56906
			'Geography.Regions.Europe.Europe*'             12599  -->  10210  2389  1101  47072
			'Geography.Regions.Europe.Northern Europe'      2840  -->   1868   972   266  57666
			'Geography.Regions.Europe.Southern Europe'      2860  -->   2219   641   159  57753
			'Geography.Regions.Europe.Western Europe'       3982  -->   3089   893   239  56551
			'Geography.Regions.Oceania'                     2216  -->   1712   504    97  58459
			'History and Society.Business and economics'    3387  -->   2129  1258   334  57051
			'History and Society.Education'                 1643  -->   1012   631   129  59000
			'History and Society.History'                   4516  -->   2477  2039   566  55690
			'History and Society.Military and warfare'      5029  -->   3932  1097   433  55310
			'History and Society.Politics and government'   4546  -->   2595  1951   432  55794
			'History and Society.Society'                   6117  -->   3013  3104   508  54147
			'History and Society.Transportation'            3544  -->   3281   263    64  57164
			'STEM.Biology'                                  7093  -->   6538   555   153  53526
			'STEM.Chemistry'                                1440  -->   1124   316   166  59166
			'STEM.Computing'                                2496  -->   2076   420   291  57985
			'STEM.Earth and environment'                    1703  -->   1191   512   146  58923
			'STEM.Engineering'                              2986  -->   2472   514   122  57664
			'STEM.Libraries & Information'                   497  -->    389   108    31  60244
			'STEM.Mathematics'                               930  -->    761   169    57  59785
			'STEM.Medicine & Health'                        1776  -->   1311   465   140  58856
			'STEM.Physics'                                  1379  -->   1046   333   169  59224
			'STEM.STEM*'                                   20610  -->  18903  1707   849  39313
			'STEM.Space'                                    1609  -->   1467   142    40  59123
			'STEM.Technology'                               4302  -->   3236  1066   532  55938
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.121
		Culture.Biography.Women                         0.086         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.219         0.055
		Culture.Media.Music                             0.049         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.051         0.01
		Culture.Sports                                  0.065         0.061
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.066         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.037         0.007
		Geography.Regions.Asia.Asia*                    0.227         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.091         0.012
		Geography.Regions.Asia.North Asia               0.028         0.006
		Geography.Regions.Asia.South Asia               0.033         0.017
		Geography.Regions.Asia.Southeast Asia           0.044         0.006
		Geography.Regions.Asia.West Asia                0.036         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.018
		Geography.Regions.Europe.Europe*                0.207         0.082
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.047         0.014
		Geography.Regions.Europe.Western Europe         0.066         0.021
		Geography.Regions.Oceania                       0.036         0.017
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.083         0.015
		History and Society.Politics and government     0.075         0.016
		History and Society.Society                     0.101         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.117         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.339         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.071         0.005
	match_rate (micro=0.05, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.124
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.072
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
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.009
		Geography.Regions.Asia.Asia*                 0.067
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.087
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.016
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.017
		History and Society.Society                  0.013
		History and Society.Transportation           0.016
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.08
		STEM.Space                                   0.005
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.928
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
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.991
		Geography.Regions.Asia.Asia*                 0.933
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.913
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.983
		History and Society.Society                  0.987
		History and Society.Transportation           0.984
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.92
		STEM.Space                                   0.995
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.803, macro=0.758):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.901
		Culture.Biography.Women                      0.808
		Culture.Food and drink                       0.74
		Culture.Internet culture                     0.842
		Culture.Linguistics                          0.779
		Culture.Literature                           0.782
		Culture.Media.Books                          0.741
		Culture.Media.Entertainment                  0.53
		Culture.Media.Films                          0.79
		Culture.Media.Media*                         0.881
		Culture.Media.Music                          0.868
		Culture.Media.Radio                          0.699
		Culture.Media.Software                       0.845
		Culture.Media.Television                     0.729
		Culture.Media.Video games                    0.917
		Culture.Performing arts                      0.69
		Culture.Philosophy and religion              0.576
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.726
		Culture.Visual arts.Comics and Anime         0.908
		Culture.Visual arts.Fashion                  0.826
		Culture.Visual arts.Visual arts*             0.786
		Geography.Geographical                       0.651
		Geography.Regions.Africa.Africa*             0.784
		Geography.Regions.Africa.Central Africa      0.651
		Geography.Regions.Africa.Eastern Africa      0.504
		Geography.Regions.Africa.Northern Africa     0.719
		Geography.Regions.Africa.Southern Africa     0.677
		Geography.Regions.Africa.Western Africa      0.804
		Geography.Regions.Americas.Central America   0.665
		Geography.Regions.Americas.North America     0.685
		Geography.Regions.Americas.South America     0.775
		Geography.Regions.Asia.Asia*                 0.84
		Geography.Regions.Asia.Central Asia          0.725
		Geography.Regions.Asia.East Asia             0.809
		Geography.Regions.Asia.North Asia            0.734
		Geography.Regions.Asia.South Asia            0.795
		Geography.Regions.Asia.Southeast Asia        0.749
		Geography.Regions.Asia.West Asia             0.811
		Geography.Regions.Europe.Eastern Europe      0.801
		Geography.Regions.Europe.Europe*             0.81
		Geography.Regions.Europe.Northern Europe     0.658
		Geography.Regions.Europe.Southern Europe     0.776
		Geography.Regions.Europe.Western Europe      0.776
		Geography.Regions.Oceania                    0.773
		History and Society.Business and economics   0.629
		History and Society.Education                0.616
		History and Society.History                  0.548
		History and Society.Military and warfare     0.782
		History and Society.Politics and government  0.571
		History and Society.Society                  0.493
		History and Society.Transportation           0.926
		STEM.Biology                                 0.922
		STEM.Chemistry                               0.781
		STEM.Computing                               0.832
		STEM.Earth and environment                   0.699
		STEM.Engineering                             0.828
		STEM.Libraries & Information                 0.783
		STEM.Mathematics                             0.818
		STEM.Medicine & Health                       0.738
		STEM.Physics                                 0.759
		STEM.STEM*                                   0.917
		STEM.Space                                   0.912
		STEM.Technology                              0.752
		-------------------------------------------  -----
	!recall (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.991
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.745, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.886
		Culture.Biography.Women                      0.481
		Culture.Food and drink                       0.48
		Culture.Internet culture                     0.431
		Culture.Linguistics                          0.847
		Culture.Literature                           0.58
		Culture.Media.Books                          0.593
		Culture.Media.Entertainment                  0.405
		Culture.Media.Films                          0.774
		Culture.Media.Media*                         0.673
		Culture.Media.Music                          0.862
		Culture.Media.Radio                          0.708
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.719
		Culture.Media.Video games                    0.764
		Culture.Performing arts                      0.509
		Culture.Philosophy and religion              0.593
		Culture.Sports                               0.966
		Culture.Visual arts.Architecture             0.73
		Culture.Visual arts.Comics and Anime         0.626
		Culture.Visual arts.Fashion                  0.305
		Culture.Visual arts.Visual arts*             0.671
		Geography.Geographical                       0.619
		Geography.Regions.Africa.Africa*             0.451
		Geography.Regions.Africa.Central Africa      0.203
		Geography.Regions.Africa.Eastern Africa      0.21
		Geography.Regions.Africa.Northern Africa     0.377
		Geography.Regions.Africa.Southern Africa     0.397
		Geography.Regions.Africa.Western Africa      0.436
		Geography.Regions.Americas.Central America   0.563
		Geography.Regions.Americas.North America     0.804
		Geography.Regions.Americas.South America     0.596
		Geography.Regions.Asia.Asia*                 0.669
		Geography.Regions.Asia.Central Asia          0.314
		Geography.Regions.Asia.East Asia             0.545
		Geography.Regions.Asia.North Asia            0.565
		Geography.Regions.Asia.South Asia            0.888
		Geography.Regions.Asia.Southeast Asia        0.587
		Geography.Regions.Asia.West Asia             0.854
		Geography.Regions.Europe.Eastern Europe      0.758
		Geography.Regions.Europe.Europe*             0.759
		Geography.Regions.Europe.Northern Europe     0.812
		Geography.Regions.Europe.Southern Europe     0.8
		Geography.Regions.Europe.Western Europe      0.796
		Geography.Regions.Oceania                    0.887
		History and Society.Business and economics   0.517
		History and Society.Education                0.695
		History and Society.History                  0.378
		History and Society.Military and warfare     0.612
		History and Society.Politics and government  0.554
		History and Society.Society                  0.308
		History and Society.Transportation           0.933
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.323
		STEM.Computing                               0.322
		STEM.Earth and environment                   0.576
		STEM.Engineering                             0.696
		STEM.Libraries & Information                 0.513
		STEM.Mathematics                             0.286
		STEM.Medicine & Health                       0.67
		STEM.Physics                                 0.201
		STEM.STEM*                                   0.753
		STEM.Space                                   0.853
		STEM.Technology                              0.294
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.993
		History and Society.Society                  0.996
		History and Society.Transportation           0.999
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
	f1 (micro=0.766, macro=0.649):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.893
		Culture.Biography.Women                      0.603
		Culture.Food and drink                       0.582
		Culture.Internet culture                     0.57
		Culture.Linguistics                          0.812
		Culture.Literature                           0.666
		Culture.Media.Books                          0.659
		Culture.Media.Entertainment                  0.459
		Culture.Media.Films                          0.782
		Culture.Media.Media*                         0.763
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.703
		Culture.Media.Software                       0.32
		Culture.Media.Television                     0.724
		Culture.Media.Video games                    0.833
		Culture.Performing arts                      0.586
		Culture.Philosophy and religion              0.585
		Culture.Sports                               0.921
		Culture.Visual arts.Architecture             0.728
		Culture.Visual arts.Comics and Anime         0.741
		Culture.Visual arts.Fashion                  0.446
		Culture.Visual arts.Visual arts*             0.724
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.573
		Geography.Regions.Africa.Central Africa      0.31
		Geography.Regions.Africa.Eastern Africa      0.297
		Geography.Regions.Africa.Northern Africa     0.495
		Geography.Regions.Africa.Southern Africa     0.501
		Geography.Regions.Africa.Western Africa      0.566
		Geography.Regions.Americas.Central America   0.61
		Geography.Regions.Americas.North America     0.74
		Geography.Regions.Americas.South America     0.674
		Geography.Regions.Asia.Asia*                 0.745
		Geography.Regions.Asia.Central Asia          0.438
		Geography.Regions.Asia.East Asia             0.651
		Geography.Regions.Asia.North Asia            0.638
		Geography.Regions.Asia.South Asia            0.839
		Geography.Regions.Asia.Southeast Asia        0.658
		Geography.Regions.Asia.West Asia             0.832
		Geography.Regions.Europe.Eastern Europe      0.779
		Geography.Regions.Europe.Europe*             0.784
		Geography.Regions.Europe.Northern Europe     0.727
		Geography.Regions.Europe.Southern Europe     0.788
		Geography.Regions.Europe.Western Europe      0.786
		Geography.Regions.Oceania                    0.826
		History and Society.Business and economics   0.567
		History and Society.Education                0.653
		History and Society.History                  0.447
		History and Society.Military and warfare     0.687
		History and Society.Politics and government  0.562
		History and Society.Society                  0.379
		History and Society.Transportation           0.929
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.457
		STEM.Computing                               0.465
		STEM.Earth and environment                   0.632
		STEM.Engineering                             0.756
		STEM.Libraries & Information                 0.62
		STEM.Mathematics                             0.424
		STEM.Medicine & Health                       0.703
		STEM.Physics                                 0.318
		STEM.STEM*                                   0.827
		STEM.Space                                   0.882
		STEM.Technology                              0.423
		-------------------------------------------  -----
	!f1 (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.984
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.993
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.986
		STEM.Space                                   0.999
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.985
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.985
		History and Society.Society                  0.987
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.011, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.025
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.004
		Geography.Regions.Asia.Asia*                 0.023
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.023
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.009
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.021
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.978, macro=0.979):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.979
		Culture.Literature                           0.98
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.973
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.967
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.98
		Culture.Philosophy and religion              0.961
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.992
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.968
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.975
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.974
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.981
		Geography.Regions.Asia.West Asia             0.98
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.972
		History and Society.Education                0.976
		History and Society.History                  0.955
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.959
		History and Society.Society                  0.939
		History and Society.Transportation           0.99
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.988
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.978
		STEM.Engineering                             0.986
		STEM.Libraries & Information                 0.974
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.982
		STEM.Space                                   0.992
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.82, macro=0.672):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.599
		Culture.Food and drink                       0.662
		Culture.Internet culture                     0.681
		Culture.Linguistics                          0.826
		Culture.Literature                           0.754
		Culture.Media.Books                          0.668
		Culture.Media.Entertainment                  0.428
		Culture.Media.Films                          0.847
		Culture.Media.Media*                         0.864
		Culture.Media.Music                          0.916
		Culture.Media.Radio                          0.556
		Culture.Media.Software                       0.334
		Culture.Media.Television                     0.747
		Culture.Media.Video games                    0.89
		Culture.Performing arts                      0.506
		Culture.Philosophy and religion              0.545
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.752
		Culture.Visual arts.Comics and Anime         0.867
		Culture.Visual arts.Fashion                  0.544
		Culture.Visual arts.Visual arts*             0.759
		Geography.Geographical                       0.649
		Geography.Regions.Africa.Africa*             0.606
		Geography.Regions.Africa.Central Africa      0.221
		Geography.Regions.Africa.Eastern Africa      0.133
		Geography.Regions.Africa.Northern Africa     0.489
		Geography.Regions.Africa.Southern Africa     0.464
		Geography.Regions.Africa.Western Africa      0.5
		Geography.Regions.Americas.Central America   0.56
		Geography.Regions.Americas.North America     0.824
		Geography.Regions.Americas.South America     0.661
		Geography.Regions.Asia.Asia*                 0.804
		Geography.Regions.Asia.Central Asia          0.332
		Geography.Regions.Asia.East Asia             0.688
		Geography.Regions.Asia.North Asia            0.64
		Geography.Regions.Asia.South Asia            0.892
		Geography.Regions.Asia.Southeast Asia        0.676
		Geography.Regions.Asia.West Asia             0.863
		Geography.Regions.Europe.Eastern Europe      0.835
		Geography.Regions.Europe.Europe*             0.866
		Geography.Regions.Europe.Northern Europe     0.788
		Geography.Regions.Europe.Southern Europe     0.845
		Geography.Regions.Europe.Western Europe      0.843
		Geography.Regions.Oceania                    0.882
		History and Society.Business and economics   0.603
		History and Society.Education                0.658
		History and Society.History                  0.416
		History and Society.Military and warfare     0.749
		History and Society.Politics and government  0.603
		History and Society.Society                  0.366
		History and Society.Transportation           0.963
		STEM.Biology                                 0.96
		STEM.Chemistry                               0.54
		STEM.Computing                               0.478
		STEM.Earth and environment                   0.675
		STEM.Engineering                             0.856
		STEM.Libraries & Information                 0.493
		STEM.Mathematics                             0.576
		STEM.Medicine & Health                       0.746
		STEM.Physics                                 0.274
		STEM.STEM*                                   0.933
		STEM.Space                                   0.926
		STEM.Technology                              0.492
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

