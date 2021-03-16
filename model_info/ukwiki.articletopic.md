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
	counts (n=61872):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15285  -->  13864  1421   854  45733
			'Culture.Biography.Women'                       3895  -->   3033   862   375  57602
			'Culture.Food and drink'                        1539  -->   1115   424   121  60212
			'Culture.Internet culture'                      3161  -->   2549   612   202  58509
			'Culture.Linguistics'                           1654  -->   1145   509   103  60115
			'Culture.Literature'                            5468  -->   4167  1301   507  55897
			'Culture.Media.Books'                           1863  -->   1464   399   139  59870
			'Culture.Media.Entertainment'                   2250  -->   1006  1244   327  59295
			'Culture.Media.Films'                           2900  -->   2453   447   128  58844
			'Culture.Media.Media*'                         13856  -->  11998  1858  1345  46671
			'Culture.Media.Music'                           2799  -->   2298   501   224  58849
			'Culture.Media.Radio'                            499  -->    223   276    36  61337
			'Culture.Media.Software'                        2159  -->   1591   568   360  59353
			'Culture.Media.Television'                      1945  -->   1482   463   114  59813
			'Culture.Media.Video games'                     2036  -->   1820   216    56  59780
			'Culture.Performing arts'                       1440  -->    873   567   131  60301
			'Culture.Philosophy and religion'               3441  -->   1777  1664   340  58091
			'Culture.Sports'                                5618  -->   5005   613   173  56081
			'Culture.Visual arts.Architecture'              2171  -->   1477   694   249  59452
			'Culture.Visual arts.Comics and Anime'          1656  -->   1367   289    77  60139
			'Culture.Visual arts.Fashion'                   1222  -->    865   357    87  60563
			'Culture.Visual arts.Visual arts*'              5790  -->   4252  1538   487  55595
			'Geography.Geographical'                        4618  -->   3151  1467   590  56664
			'Geography.Regions.Africa.Africa*'              5132  -->   3762  1370   380  56360
			'Geography.Regions.Africa.Central Africa'       1180  -->    844   336    75  60617
			'Geography.Regions.Africa.Eastern Africa'        740  -->    548   192    38  61094
			'Geography.Regions.Africa.Northern Africa'      1497  -->    924   573   125  60250
			'Geography.Regions.Africa.Southern Africa'       915  -->    495   420    42  60915
			'Geography.Regions.Africa.Western Africa'        408  -->    271   137    48  61416
			'Geography.Regions.Americas.Central America'    1307  -->    841   466    60  60505
			'Geography.Regions.Americas.North America'      5578  -->   3500  2078   796  55498
			'Geography.Regions.Americas.South America'      1541  -->   1069   472    84  60247
			'Geography.Regions.Asia.Asia*'                 11303  -->   8985  2318   932  49637
			'Geography.Regions.Asia.Central Asia'           1384  -->    983   401    88  60400
			'Geography.Regions.Asia.East Asia'              2959  -->   2211   748   225  58688
			'Geography.Regions.Asia.North Asia'             2202  -->   1475   727   375  59295
			'Geography.Regions.Asia.South Asia'             1802  -->   1354   448    79  59991
			'Geography.Regions.Asia.Southeast Asia'         1577  -->   1027   550    82  60213
			'Geography.Regions.Asia.West Asia'              2657  -->   1870   787   167  59048
			'Geography.Regions.Europe.Eastern Europe'       5352  -->   4013  1339   611  55909
			'Geography.Regions.Europe.Europe*'             16339  -->  12667  3672  2087  43446
			'Geography.Regions.Europe.Northern Europe'      3593  -->   2238  1355   384  57895
			'Geography.Regions.Europe.Southern Europe'      3717  -->   2569  1148   325  57830
			'Geography.Regions.Europe.Western Europe'       4408  -->   3184  1224   452  57012
			'Geography.Regions.Oceania'                     1809  -->   1234   575    91  59972
			'History and Society.Business and economics'    3779  -->   2229  1550   464  57629
			'History and Society.Education'                 1723  -->    913   810   134  60015
			'History and Society.History'                   5359  -->   3062  2297   739  55774
			'History and Society.Military and warfare'      5421  -->   3704  1717   615  55836
			'History and Society.Politics and government'   4244  -->   2312  1932   457  57171
			'History and Society.Society'                   6559  -->   3089  3470   792  54521
			'History and Society.Transportation'            3606  -->   3183   423   174  58092
			'STEM.Biology'                                  3746  -->   3028   718   180  57946
			'STEM.Chemistry'                                1514  -->   1111   403   180  60178
			'STEM.Computing'                                2701  -->   2072   629   433  58738
			'STEM.Earth and environment'                    1914  -->   1240   674   143  59815
			'STEM.Engineering'                              3106  -->   2370   736   234  58532
			'STEM.Libraries & Information'                  1069  -->    745   324    60  60743
			'STEM.Mathematics'                              1210  -->    873   337   105  60557
			'STEM.Medicine & Health'                        1872  -->   1239   633   148  59852
			'STEM.Physics'                                  1505  -->    965   540   192  60175
			'STEM.STEM*'                                   18776  -->  16695  2081  1056  42040
			'STEM.Space'                                    1843  -->   1643   200    52  59977
			'STEM.Technology'                               4773  -->   3219  1554   714  56385
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.247         0.123
		Culture.Biography.Women                         0.063         0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.051         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.088         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.036         0.004
		Culture.Media.Films                             0.047         0.011
		Culture.Media.Media*                            0.224         0.058
		Culture.Media.Music                             0.045         0.024
		Culture.Media.Radio                             0.008         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.031         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.056         0.011
		Culture.Sports                                  0.091         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.02          0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.075         0.024
		Geography.Regions.Africa.Africa*                0.083         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.012         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.015         0.001
		Geography.Regions.Africa.Western Africa         0.007         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.09          0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.183         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.048         0.011
		Geography.Regions.Asia.North Asia               0.036         0.001
		Geography.Regions.Asia.South Asia               0.029         0.015
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.043         0.011
		Geography.Regions.Europe.Eastern Europe         0.087         0.013
		Geography.Regions.Europe.Europe*                0.264         0.076
		Geography.Regions.Europe.Northern Europe        0.058         0.031
		Geography.Regions.Europe.Southern Europe        0.06          0.013
		Geography.Regions.Europe.Western Europe         0.071         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.061         0.01
		History and Society.Education                   0.028         0.007
		History and Society.History                     0.087         0.011
		History and Society.Military and warfare        0.088         0.014
		History and Society.Politics and government     0.069         0.028
		History and Society.Society                     0.106         0.013
		History and Society.Transportation              0.058         0.015
		STEM.Biology                                    0.061         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.044         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.017         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.303         0.069
		STEM.Space                                      0.03          0.006
		STEM.Technology                                 0.077         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.101
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.014
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.023
		History and Society.Society                  0.02
		History and Society.Transportation           0.016
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.899
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.986
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.977
		History and Society.Society                  0.98
		History and Society.Transportation           0.984
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.768, macro=0.708):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.907
		Culture.Biography.Women                      0.779
		Culture.Food and drink                       0.724
		Culture.Internet culture                     0.806
		Culture.Linguistics                          0.692
		Culture.Literature                           0.762
		Culture.Media.Books                          0.786
		Culture.Media.Entertainment                  0.447
		Culture.Media.Films                          0.846
		Culture.Media.Media*                         0.866
		Culture.Media.Music                          0.821
		Culture.Media.Radio                          0.447
		Culture.Media.Software                       0.737
		Culture.Media.Television                     0.762
		Culture.Media.Video games                    0.894
		Culture.Performing arts                      0.606
		Culture.Philosophy and religion              0.516
		Culture.Sports                               0.891
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.825
		Culture.Visual arts.Fashion                  0.708
		Culture.Visual arts.Visual arts*             0.734
		Geography.Geographical                       0.682
		Geography.Regions.Africa.Africa*             0.733
		Geography.Regions.Africa.Central Africa      0.715
		Geography.Regions.Africa.Eastern Africa      0.741
		Geography.Regions.Africa.Northern Africa     0.617
		Geography.Regions.Africa.Southern Africa     0.541
		Geography.Regions.Africa.Western Africa      0.664
		Geography.Regions.Americas.Central America   0.643
		Geography.Regions.Americas.North America     0.627
		Geography.Regions.Americas.South America     0.694
		Geography.Regions.Asia.Asia*                 0.795
		Geography.Regions.Asia.Central Asia          0.71
		Geography.Regions.Asia.East Asia             0.747
		Geography.Regions.Asia.North Asia            0.67
		Geography.Regions.Asia.South Asia            0.751
		Geography.Regions.Asia.Southeast Asia        0.651
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.75
		Geography.Regions.Europe.Europe*             0.775
		Geography.Regions.Europe.Northern Europe     0.623
		Geography.Regions.Europe.Southern Europe     0.691
		Geography.Regions.Europe.Western Europe      0.722
		Geography.Regions.Oceania                    0.682
		History and Society.Business and economics   0.59
		History and Society.Education                0.53
		History and Society.History                  0.571
		History and Society.Military and warfare     0.683
		History and Society.Politics and government  0.545
		History and Society.Society                  0.471
		History and Society.Transportation           0.883
		STEM.Biology                                 0.808
		STEM.Chemistry                               0.734
		STEM.Computing                               0.767
		STEM.Earth and environment                   0.648
		STEM.Engineering                             0.763
		STEM.Libraries & Information                 0.697
		STEM.Mathematics                             0.721
		STEM.Medicine & Health                       0.662
		STEM.Physics                                 0.641
		STEM.STEM*                                   0.889
		STEM.Space                                   0.891
		STEM.Technology                              0.674
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.972
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
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.992
		History and Society.Society                  0.986
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.707, macro=0.552):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.64
		Culture.Food and drink                       0.471
		Culture.Internet culture                     0.451
		Culture.Linguistics                          0.749
		Culture.Literature                           0.572
		Culture.Media.Books                          0.578
		Culture.Media.Entertainment                  0.227
		Culture.Media.Films                          0.806
		Culture.Media.Media*                         0.658
		Culture.Media.Music                          0.841
		Culture.Media.Radio                          0.622
		Culture.Media.Software                       0.14
		Culture.Media.Television                     0.781
		Culture.Media.Video games                    0.714
		Culture.Performing arts                      0.447
		Culture.Philosophy and religion              0.489
		Culture.Sports                               0.957
		Culture.Visual arts.Architecture             0.635
		Culture.Visual arts.Comics and Anime         0.587
		Culture.Visual arts.Fashion                  0.285
		Culture.Visual arts.Visual arts*             0.612
		Geography.Geographical                       0.615
		Geography.Regions.Africa.Africa*             0.462
		Geography.Regions.Africa.Central Africa      0.268
		Geography.Regions.Africa.Eastern Africa      0.352
		Geography.Regions.Africa.Northern Africa     0.268
		Geography.Regions.Africa.Southern Africa     0.48
		Geography.Regions.Africa.Western Africa      0.368
		Geography.Regions.Americas.Central America   0.683
		Geography.Regions.Americas.North America     0.753
		Geography.Regions.Americas.South America     0.76
		Geography.Regions.Asia.Asia*                 0.673
		Geography.Regions.Asia.Central Asia          0.297
		Geography.Regions.Asia.East Asia             0.693
		Geography.Regions.Asia.North Asia            0.09
		Geography.Regions.Asia.South Asia            0.898
		Geography.Regions.Asia.Southeast Asia        0.743
		Geography.Regions.Asia.West Asia             0.733
		Geography.Regions.Europe.Eastern Europe      0.474
		Geography.Regions.Europe.Europe*             0.582
		Geography.Regions.Europe.Northern Europe     0.749
		Geography.Regions.Europe.Southern Europe     0.62
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.874
		History and Society.Business and economics   0.429
		History and Society.Education                0.638
		History and Society.History                  0.324
		History and Society.Military and warfare     0.472
		History and Society.Politics and government  0.666
		History and Society.Society                  0.296
		History and Society.Transportation           0.819
		STEM.Biology                                 0.901
		STEM.Chemistry                               0.277
		STEM.Computing                               0.22
		STEM.Earth and environment                   0.553
		STEM.Engineering                             0.502
		STEM.Libraries & Information                 0.305
		STEM.Mathematics                             0.148
		STEM.Medicine & Health                       0.633
		STEM.Physics                                 0.146
		STEM.STEM*                                   0.729
		STEM.Space                                   0.862
		STEM.Technology                              0.218
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.987
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
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.728, macro=0.597):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.703
		Culture.Food and drink                       0.571
		Culture.Internet culture                     0.579
		Culture.Linguistics                          0.72
		Culture.Literature                           0.653
		Culture.Media.Books                          0.666
		Culture.Media.Entertainment                  0.301
		Culture.Media.Films                          0.825
		Culture.Media.Media*                         0.747
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.52
		Culture.Media.Software                       0.235
		Culture.Media.Television                     0.771
		Culture.Media.Video games                    0.794
		Culture.Performing arts                      0.515
		Culture.Philosophy and religion              0.502
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.657
		Culture.Visual arts.Comics and Anime         0.686
		Culture.Visual arts.Fashion                  0.407
		Culture.Visual arts.Visual arts*             0.667
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.567
		Geography.Regions.Africa.Central Africa      0.39
		Geography.Regions.Africa.Eastern Africa      0.477
		Geography.Regions.Africa.Northern Africa     0.374
		Geography.Regions.Africa.Southern Africa     0.509
		Geography.Regions.Africa.Western Africa      0.473
		Geography.Regions.Americas.Central America   0.662
		Geography.Regions.Americas.North America     0.685
		Geography.Regions.Americas.South America     0.725
		Geography.Regions.Asia.Asia*                 0.729
		Geography.Regions.Asia.Central Asia          0.419
		Geography.Regions.Asia.East Asia             0.719
		Geography.Regions.Asia.North Asia            0.158
		Geography.Regions.Asia.South Asia            0.818
		Geography.Regions.Asia.Southeast Asia        0.694
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.581
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.68
		Geography.Regions.Europe.Southern Europe     0.654
		Geography.Regions.Europe.Western Europe      0.68
		Geography.Regions.Oceania                    0.766
		History and Society.Business and economics   0.497
		History and Society.Education                0.579
		History and Society.History                  0.413
		History and Society.Military and warfare     0.558
		History and Society.Politics and government  0.599
		History and Society.Society                  0.363
		History and Society.Transportation           0.85
		STEM.Biology                                 0.852
		STEM.Chemistry                               0.403
		STEM.Computing                               0.342
		STEM.Earth and environment                   0.597
		STEM.Engineering                             0.606
		STEM.Libraries & Information                 0.424
		STEM.Mathematics                             0.246
		STEM.Medicine & Health                       0.647
		STEM.Physics                                 0.238
		STEM.STEM*                                   0.801
		STEM.Space                                   0.876
		STEM.Technology                              0.329
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.989
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.979
		History and Society.Society                  0.979
		History and Society.Transportation           0.995
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.018
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.028
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
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.046
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.008
		History and Society.Society                  0.014
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.977
		Culture.Literature                           0.979
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.955
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.977
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.973
		Geography.Regions.Africa.Central Africa      0.984
		Geography.Regions.Africa.Eastern Africa      0.981
		Geography.Regions.Africa.Northern Africa     0.971
		Geography.Regions.Africa.Southern Africa     0.964
		Geography.Regions.Africa.Western Africa      0.964
		Geography.Regions.Americas.Central America   0.976
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.977
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.98
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.978
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.966
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.961
		History and Society.Education                0.97
		History and Society.History                  0.953
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.953
		History and Society.Society                  0.923
		History and Society.Transportation           0.985
		STEM.Biology                                 0.98
		STEM.Chemistry                               0.982
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.978
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.98
		STEM.STEM*                                   0.977
		STEM.Space                                   0.99
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.779, macro=0.611):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.691
		Culture.Food and drink                       0.575
		Culture.Internet culture                     0.738
		Culture.Linguistics                          0.732
		Culture.Literature                           0.749
		Culture.Media.Books                          0.727
		Culture.Media.Entertainment                  0.249
		Culture.Media.Films                          0.82
		Culture.Media.Media*                         0.856
		Culture.Media.Music                          0.859
		Culture.Media.Radio                          0.322
		Culture.Media.Software                       0.248
		Culture.Media.Television                     0.754
		Culture.Media.Video games                    0.867
		Culture.Performing arts                      0.455
		Culture.Philosophy and religion              0.48
		Culture.Sports                               0.955
		Culture.Visual arts.Architecture             0.655
		Culture.Visual arts.Comics and Anime         0.747
		Culture.Visual arts.Fashion                  0.44
		Culture.Visual arts.Visual arts*             0.721
		Geography.Geographical                       0.681
		Geography.Regions.Africa.Africa*             0.584
		Geography.Regions.Africa.Central Africa      0.412
		Geography.Regions.Africa.Eastern Africa      0.438
		Geography.Regions.Africa.Northern Africa     0.33
		Geography.Regions.Africa.Southern Africa     0.446
		Geography.Regions.Africa.Western Africa      0.315
		Geography.Regions.Americas.Central America   0.63
		Geography.Regions.Americas.North America     0.769
		Geography.Regions.Americas.South America     0.725
		Geography.Regions.Asia.Asia*                 0.789
		Geography.Regions.Asia.Central Asia          0.394
		Geography.Regions.Asia.East Asia             0.742
		Geography.Regions.Asia.North Asia            0.144
		Geography.Regions.Asia.South Asia            0.86
		Geography.Regions.Asia.Southeast Asia        0.651
		Geography.Regions.Asia.West Asia             0.76
		Geography.Regions.Europe.Eastern Europe      0.68
		Geography.Regions.Europe.Europe*             0.745
		Geography.Regions.Europe.Northern Europe     0.745
		Geography.Regions.Europe.Southern Europe     0.706
		Geography.Regions.Europe.Western Europe      0.745
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.449
		History and Society.Education                0.575
		History and Society.History                  0.402
		History and Society.Military and warfare     0.638
		History and Society.Politics and government  0.639
		History and Society.Society                  0.31
		History and Society.Transportation           0.877
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.406
		STEM.Computing                               0.35
		STEM.Earth and environment                   0.601
		STEM.Engineering                             0.635
		STEM.Libraries & Information                 0.358
		STEM.Mathematics                             0.269
		STEM.Medicine & Health                       0.643
		STEM.Physics                                 0.185
		STEM.STEM*                                   0.898
		STEM.Space                                   0.912
		STEM.Technology                              0.355
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

