Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'max_features': 'log2', 'min_weight_fraction_leaf': 0.0, 'validation_fraction': 0.1, 'criterion': 'friedman_mse', 'max_depth': 5, 'center': False, 'population_rates': None, 'min_samples_split': 2, 'init': None, 'loss': 'deviance', 'n_estimators': 150, 'learning_rate': 0.1, 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_leaf': 1, 'label_weights': {}, 'min_impurity_split': None, 'subsample': 1.0, 'verbose': 0, 'tol': 0.0001, 'random_state': None, 'warm_start': False, 'multilabel': True, 'max_leaf_nodes': None, 'n_iter_no_change': None, 'min_impurity_decrease': 0.0, 'presort': 'auto'}
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
	counts (n=60785):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14154  -->  12680  1474   663  45968
			'Culture.Biography.Women'                       5106  -->   4137   969   772  54907
			'Culture.Food and drink'                        1427  -->   1011   416   132  59226
			'Culture.Internet culture'                      3514  -->   2851   663   272  56999
			'Culture.Linguistics'                           1461  -->   1103   358   105  59219
			'Culture.Literature'                            5626  -->   4374  1252   535  54624
			'Culture.Media.Books'                           1460  -->   1051   409   131  59194
			'Culture.Media.Entertainment'                   2021  -->    995  1026   202  58562
			'Culture.Media.Films'                           2631  -->   2097   534   136  58018
			'Culture.Media.Media*'                         13375  -->  11582  1793  1389  46021
			'Culture.Media.Music'                           2976  -->   2561   415   217  57592
			'Culture.Media.Radio'                            298  -->    192   106    26  60461
			'Culture.Media.Software'                        2308  -->   1839   469   308  58169
			'Culture.Media.Television'                      1966  -->   1367   599   138  58681
			'Culture.Media.Video games'                     2143  -->   1939   204    64  58578
			'Culture.Performing arts'                       1373  -->    921   452   153  59259
			'Culture.Philosophy and religion'               3023  -->   1627  1396   317  57445
			'Culture.Sports'                                3926  -->   3432   494   151  56708
			'Culture.Visual arts.Architecture'              1817  -->   1347   470   161  58807
			'Culture.Visual arts.Comics and Anime'          2183  -->   1887   296   105  58497
			'Culture.Visual arts.Fashion'                   1508  -->   1247   261    96  59181
			'Culture.Visual arts.Visual arts*'              6028  -->   4613  1415   454  54303
			'Geography.Geographical'                        3984  -->   2606  1378   650  56151
			'Geography.Regions.Africa.Africa*'              5687  -->   2477  3210   617  54481
			'Geography.Regions.Africa.Central Africa'       1207  -->    332   875   107  59471
			'Geography.Regions.Africa.Eastern Africa'        447  -->    137   310    53  60285
			'Geography.Regions.Africa.Northern Africa'      1500  -->    606   894    90  59195
			'Geography.Regions.Africa.Southern Africa'      1196  -->    480   716    79  59510
			'Geography.Regions.Africa.Western Africa'        673  -->    280   393    95  60017
			'Geography.Regions.Americas.Central America'    1589  -->    240  1349    85  59111
			'Geography.Regions.Americas.North America'      5460  -->   2186  3274   335  54990
			'Geography.Regions.Americas.South America'      2210  -->    786  1424   147  58428
			'Geography.Regions.Asia.Asia*'                 13836  -->   8038  5798  1624  45325
			'Geography.Regions.Asia.Central Asia'           1227  -->    488   739    92  59466
			'Geography.Regions.Asia.East Asia'              5565  -->   2813  2752   426  54794
			'Geography.Regions.Asia.North Asia'             1683  -->    791   892   171  58931
			'Geography.Regions.Asia.South Asia'             2061  -->    880  1181    83  58641
			'Geography.Regions.Asia.Southeast Asia'         2569  -->    457  2112    88  58128
			'Geography.Regions.Asia.West Asia'              2205  -->   1172  1033   100  58480
			'Geography.Regions.Europe.Eastern Europe'       3565  -->   1786  1779   209  57011
			'Geography.Regions.Europe.Europe*'             12591  -->   7225  5366  1360  46834
			'Geography.Regions.Europe.Northern Europe'      2897  -->    678  2219   175  57713
			'Geography.Regions.Europe.Southern Europe'      2787  -->   1240  1547   123  57875
			'Geography.Regions.Europe.Western Europe'       4017  -->   1870  2147    97  56671
			'Geography.Regions.Oceania'                     2306  -->    819  1487   244  58235
			'History and Society.Business and economics'    3386  -->   2179  1207   380  57019
			'History and Society.Education'                 1645  -->    929   716   125  59015
			'History and Society.History'                   4439  -->   2221  2218   683  55663
			'History and Society.Military and warfare'      4997  -->   3589  1408   483  55305
			'History and Society.Politics and government'   4645  -->   1959  2686   594  55546
			'History and Society.Society'                   6080  -->   1777  4303   407  54298
			'History and Society.Transportation'            3589  -->   3303   286   109  57087
			'STEM.Biology'                                  7095  -->   6533   562   186  53504
			'STEM.Chemistry'                                1451  -->   1135   316   173  59161
			'STEM.Computing'                                2466  -->   2014   452   346  57973
			'STEM.Earth and environment'                    1619  -->   1100   519   139  59027
			'STEM.Engineering'                              3035  -->   2549   486   129  57621
			'STEM.Libraries & Information'                   502  -->    393   109    53  60230
			'STEM.Mathematics'                               919  -->    725   194    59  59807
			'STEM.Medicine & Health'                        1778  -->   1284   494   160  58847
			'STEM.Physics'                                  1387  -->   1038   349   172  59226
			'STEM.STEM*'                                   20576  -->  18857  1719   898  39311
			'STEM.Space'                                    1608  -->   1464   144    42  59135
			'STEM.Technology'                               4222  -->   3086  1136   592  55971
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.024         0.008
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.22          0.055
		Culture.Media.Music                             0.049         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.05          0.01
		Culture.Sports                                  0.065         0.061
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.066         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.09          0.064
		Geography.Regions.Americas.South America        0.036         0.007
		Geography.Regions.Asia.Asia*                    0.228         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.092         0.012
		Geography.Regions.Asia.North Asia               0.028         0.006
		Geography.Regions.Asia.South Asia               0.034         0.017
		Geography.Regions.Asia.Southeast Asia           0.042         0.006
		Geography.Regions.Asia.West Asia                0.036         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.018
		Geography.Regions.Europe.Europe*                0.207         0.082
		Geography.Regions.Europe.Northern Europe        0.048         0.029
		Geography.Regions.Europe.Southern Europe        0.046         0.014
		Geography.Regions.Europe.Western Europe         0.066         0.021
		Geography.Regions.Oceania                       0.038         0.017
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.073         0.011
		History and Society.Military and warfare        0.082         0.015
		History and Society.Politics and government     0.076         0.016
		History and Society.Society                     0.1           0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.117         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.339         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.046, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.121
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.008
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.005
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.031
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.064
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.009
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.073
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.008
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.017
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.017
		History and Society.Society                  0.01
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.081
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.954, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.879
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.992
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.995
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.936
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.927
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.983
		History and Society.Society                  0.99
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.919
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.679, macro=0.625):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.81
		Culture.Food and drink                       0.708
		Culture.Internet culture                     0.811
		Culture.Linguistics                          0.755
		Culture.Literature                           0.777
		Culture.Media.Books                          0.72
		Culture.Media.Entertainment                  0.492
		Culture.Media.Films                          0.797
		Culture.Media.Media*                         0.866
		Culture.Media.Music                          0.861
		Culture.Media.Radio                          0.644
		Culture.Media.Software                       0.797
		Culture.Media.Television                     0.695
		Culture.Media.Video games                    0.905
		Culture.Performing arts                      0.671
		Culture.Philosophy and religion              0.538
		Culture.Sports                               0.874
		Culture.Visual arts.Architecture             0.741
		Culture.Visual arts.Comics and Anime         0.864
		Culture.Visual arts.Fashion                  0.827
		Culture.Visual arts.Visual arts*             0.765
		Geography.Geographical                       0.654
		Geography.Regions.Africa.Africa*             0.436
		Geography.Regions.Africa.Central Africa      0.275
		Geography.Regions.Africa.Eastern Africa      0.306
		Geography.Regions.Africa.Northern Africa     0.404
		Geography.Regions.Africa.Southern Africa     0.401
		Geography.Regions.Africa.Western Africa      0.416
		Geography.Regions.Americas.Central America   0.151
		Geography.Regions.Americas.North America     0.4
		Geography.Regions.Americas.South America     0.356
		Geography.Regions.Asia.Asia*                 0.581
		Geography.Regions.Asia.Central Asia          0.398
		Geography.Regions.Asia.East Asia             0.505
		Geography.Regions.Asia.North Asia            0.47
		Geography.Regions.Asia.South Asia            0.427
		Geography.Regions.Asia.Southeast Asia        0.178
		Geography.Regions.Asia.West Asia             0.532
		Geography.Regions.Europe.Eastern Europe      0.501
		Geography.Regions.Europe.Europe*             0.574
		Geography.Regions.Europe.Northern Europe     0.234
		Geography.Regions.Europe.Southern Europe     0.445
		Geography.Regions.Europe.Western Europe      0.466
		Geography.Regions.Oceania                    0.355
		History and Society.Business and economics   0.644
		History and Society.Education                0.565
		History and Society.History                  0.5
		History and Society.Military and warfare     0.718
		History and Society.Politics and government  0.422
		History and Society.Society                  0.292
		History and Society.Transportation           0.92
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.782
		STEM.Computing                               0.817
		STEM.Earth and environment                   0.679
		STEM.Engineering                             0.84
		STEM.Libraries & Information                 0.783
		STEM.Mathematics                             0.789
		STEM.Medicine & Health                       0.722
		STEM.Physics                                 0.748
		STEM.STEM*                                   0.916
		STEM.Space                                   0.91
		STEM.Technology                              0.731
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.994
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.696, macro=0.535):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.897
		Culture.Biography.Women                      0.473
		Culture.Food and drink                       0.451
		Culture.Internet culture                     0.392
		Culture.Linguistics                          0.777
		Culture.Literature                           0.55
		Culture.Media.Books                          0.588
		Culture.Media.Entertainment                  0.364
		Culture.Media.Films                          0.801
		Culture.Media.Media*                         0.634
		Culture.Media.Music                          0.832
		Culture.Media.Radio                          0.779
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.728
		Culture.Media.Video games                    0.709
		Culture.Performing arts                      0.446
		Culture.Philosophy and religion              0.509
		Culture.Sports                               0.955
		Culture.Visual arts.Architecture             0.749
		Culture.Visual arts.Comics and Anime         0.539
		Culture.Visual arts.Fashion                  0.316
		Culture.Visual arts.Visual arts*             0.632
		Geography.Geographical                       0.555
		Geography.Regions.Africa.Africa*             0.252
		Geography.Regions.Africa.Central Africa      0.098
		Geography.Regions.Africa.Eastern Africa      0.15
		Geography.Regions.Africa.Northern Africa     0.266
		Geography.Regions.Africa.Southern Africa     0.286
		Geography.Regions.Africa.Western Africa      0.166
		Geography.Regions.Americas.Central America   0.269
		Geography.Regions.Americas.North America     0.818
		Geography.Regions.Americas.South America     0.497
		Geography.Regions.Asia.Asia*                 0.485
		Geography.Regions.Asia.Central Asia          0.172
		Geography.Regions.Asia.East Asia             0.449
		Geography.Regions.Asia.North Asia            0.48
		Geography.Regions.Asia.South Asia            0.837
		Geography.Regions.Asia.Southeast Asia        0.427
		Geography.Regions.Asia.West Asia             0.788
		Geography.Regions.Europe.Eastern Europe      0.721
		Geography.Regions.Europe.Europe*             0.644
		Geography.Regions.Europe.Northern Europe     0.7
		Geography.Regions.Europe.Southern Europe     0.748
		Geography.Regions.Europe.Western Europe      0.852
		Geography.Regions.Oceania                    0.589
		History and Society.Business and economics   0.491
		History and Society.Education                0.683
		History and Society.History                  0.315
		History and Society.Military and warfare     0.566
		History and Society.Politics and government  0.4
		History and Society.Society                  0.248
		History and Society.Transportation           0.89
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.315
		STEM.Computing                               0.282
		STEM.Earth and environment                   0.581
		STEM.Engineering                             0.687
		STEM.Libraries & Information                 0.381
		STEM.Mathematics                             0.272
		STEM.Medicine & Health                       0.635
		STEM.Physics                                 0.197
		STEM.STEM*                                   0.742
		STEM.Space                                   0.847
		STEM.Technology                              0.267
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
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
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.99
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.668, macro=0.547):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.597
		Culture.Food and drink                       0.551
		Culture.Internet culture                     0.529
		Culture.Linguistics                          0.766
		Culture.Literature                           0.644
		Culture.Media.Books                          0.647
		Culture.Media.Entertainment                  0.419
		Culture.Media.Films                          0.799
		Culture.Media.Media*                         0.732
		Culture.Media.Music                          0.846
		Culture.Media.Radio                          0.705
		Culture.Media.Software                       0.276
		Culture.Media.Television                     0.711
		Culture.Media.Video games                    0.795
		Culture.Performing arts                      0.536
		Culture.Philosophy and religion              0.523
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.745
		Culture.Visual arts.Comics and Anime         0.664
		Culture.Visual arts.Fashion                  0.458
		Culture.Visual arts.Visual arts*             0.692
		Geography.Geographical                       0.6
		Geography.Regions.Africa.Africa*             0.319
		Geography.Regions.Africa.Central Africa      0.145
		Geography.Regions.Africa.Eastern Africa      0.202
		Geography.Regions.Africa.Northern Africa     0.321
		Geography.Regions.Africa.Southern Africa     0.334
		Geography.Regions.Africa.Western Africa      0.237
		Geography.Regions.Americas.Central America   0.193
		Geography.Regions.Americas.North America     0.538
		Geography.Regions.Americas.South America     0.415
		Geography.Regions.Asia.Asia*                 0.529
		Geography.Regions.Asia.Central Asia          0.24
		Geography.Regions.Asia.East Asia             0.475
		Geography.Regions.Asia.North Asia            0.475
		Geography.Regions.Asia.South Asia            0.565
		Geography.Regions.Asia.Southeast Asia        0.251
		Geography.Regions.Asia.West Asia             0.635
		Geography.Regions.Europe.Eastern Europe      0.591
		Geography.Regions.Europe.Europe*             0.607
		Geography.Regions.Europe.Northern Europe     0.351
		Geography.Regions.Europe.Southern Europe     0.558
		Geography.Regions.Europe.Western Europe      0.602
		Geography.Regions.Oceania                    0.443
		History and Society.Business and economics   0.557
		History and Society.Education                0.618
		History and Society.History                  0.386
		History and Society.Military and warfare     0.633
		History and Society.Politics and government  0.411
		History and Society.Society                  0.269
		History and Society.Transportation           0.905
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.449
		STEM.Computing                               0.42
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.756
		STEM.Libraries & Information                 0.513
		STEM.Mathematics                             0.404
		STEM.Medicine & Health                       0.676
		STEM.Physics                                 0.311
		STEM.STEM*                                   0.82
		STEM.Space                                   0.878
		STEM.Technology                              0.391
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.986
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.98
		History and Society.Society                  0.987
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.014
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.006
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.035
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.028
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.011
		History and Society.Society                  0.007
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.958, macro=0.961):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.975
		Culture.Literature                           0.979
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.968
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.946
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.978
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.977
		Culture.Philosophy and religion              0.957
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.977
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.934
		Geography.Regions.Africa.Central Africa      0.953
		Geography.Regions.Africa.Eastern Africa      0.907
		Geography.Regions.Africa.Northern Africa     0.939
		Geography.Regions.Africa.Southern Africa     0.951
		Geography.Regions.Africa.Western Africa      0.965
		Geography.Regions.Americas.Central America   0.912
		Geography.Regions.Americas.North America     0.926
		Geography.Regions.Americas.South America     0.936
		Geography.Regions.Asia.Asia*                 0.915
		Geography.Regions.Asia.Central Asia          0.957
		Geography.Regions.Asia.East Asia             0.946
		Geography.Regions.Asia.North Asia            0.968
		Geography.Regions.Asia.South Asia            0.932
		Geography.Regions.Asia.Southeast Asia        0.908
		Geography.Regions.Asia.West Asia             0.95
		Geography.Regions.Europe.Eastern Europe      0.951
		Geography.Regions.Europe.Europe*             0.926
		Geography.Regions.Europe.Northern Europe     0.921
		Geography.Regions.Europe.Southern Europe     0.934
		Geography.Regions.Europe.Western Europe      0.94
		Geography.Regions.Oceania                    0.923
		History and Society.Business and economics   0.97
		History and Society.Education                0.972
		History and Society.History                  0.948
		History and Society.Military and warfare     0.975
		History and Society.Politics and government  0.922
		History and Society.Society                  0.899
		History and Society.Transportation           0.986
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.988
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.983
		STEM.Libraries & Information                 0.964
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.982
		STEM.Space                                   0.99
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.706, macro=0.541):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.936
		Culture.Biography.Women                      0.605
		Culture.Food and drink                       0.567
		Culture.Internet culture                     0.664
		Culture.Linguistics                          0.753
		Culture.Literature                           0.721
		Culture.Media.Books                          0.66
		Culture.Media.Entertainment                  0.334
		Culture.Media.Films                          0.797
		Culture.Media.Media*                         0.819
		Culture.Media.Music                          0.883
		Culture.Media.Radio                          0.526
		Culture.Media.Software                       0.281
		Culture.Media.Television                     0.694
		Culture.Media.Video games                    0.858
		Culture.Performing arts                      0.44
		Culture.Philosophy and religion              0.501
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.746
		Culture.Visual arts.Comics and Anime         0.755
		Culture.Visual arts.Fashion                  0.373
		Culture.Visual arts.Visual arts*             0.704
		Geography.Geographical                       0.623
		Geography.Regions.Africa.Africa*             0.275
		Geography.Regions.Africa.Central Africa      0.056
		Geography.Regions.Africa.Eastern Africa      0.05
		Geography.Regions.Africa.Northern Africa     0.153
		Geography.Regions.Africa.Southern Africa     0.192
		Geography.Regions.Africa.Western Africa      0.104
		Geography.Regions.Americas.Central America   0.113
		Geography.Regions.Americas.North America     0.66
		Geography.Regions.Americas.South America     0.345
		Geography.Regions.Asia.Asia*                 0.571
		Geography.Regions.Asia.Central Asia          0.117
		Geography.Regions.Asia.East Asia             0.411
		Geography.Regions.Asia.North Asia            0.404
		Geography.Regions.Asia.South Asia            0.574
		Geography.Regions.Asia.Southeast Asia        0.204
		Geography.Regions.Asia.West Asia             0.614
		Geography.Regions.Europe.Eastern Europe      0.613
		Geography.Regions.Europe.Europe*             0.689
		Geography.Regions.Europe.Northern Europe     0.449
		Geography.Regions.Europe.Southern Europe     0.56
		Geography.Regions.Europe.Western Europe      0.634
		Geography.Regions.Oceania                    0.419
		History and Society.Business and economics   0.561
		History and Society.Education                0.592
		History and Society.History                  0.354
		History and Society.Military and warfare     0.699
		History and Society.Politics and government  0.351
		History and Society.Society                  0.213
		History and Society.Transportation           0.933
		STEM.Biology                                 0.964
		STEM.Chemistry                               0.524
		STEM.Computing                               0.422
		STEM.Earth and environment                   0.631
		STEM.Engineering                             0.805
		STEM.Libraries & Information                 0.381
		STEM.Mathematics                             0.484
		STEM.Medicine & Health                       0.677
		STEM.Physics                                 0.331
		STEM.STEM*                                   0.926
		STEM.Space                                   0.938
		STEM.Technology                              0.441
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'History and Society.History': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

