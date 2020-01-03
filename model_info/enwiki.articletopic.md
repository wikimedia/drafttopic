Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'max_leaf_nodes': None, 'center': False, 'learning_rate': 0.1, 'init': None, 'population_rates': None, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'multilabel': True, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 1, 'max_depth': 5, 'verbose': 0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'label_weights': {}, 'loss': 'deviance', 'criterion': 'friedman_mse', 'subsample': 1.0, 'min_samples_split': 2, 'presort': 'auto', 'n_estimators': 150, 'scale': False, 'tol': 0.0001, 'warm_start': False, 'max_features': 'log2'}
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
			'Culture.Biography.Biography*'                 16717  -->  13654  3063  1578  44722
			'Culture.Biography.Women'                       4173  -->   1502  2671   525  58319
			'Culture.Food and drink'                        1323  -->    949   374    81  61613
			'Culture.Internet culture'                      2946  -->   2198   748   217  59854
			'Culture.Linguistics'                           1384  -->    928   456   105  61528
			'Culture.Literature'                            5277  -->   3642  1635   593  57147
			'Culture.Media.Books'                           1919  -->   1211   708   215  60883
			'Culture.Media.Entertainment'                   1876  -->    615  1261   147  60994
			'Culture.Media.Films'                           2307  -->   1763   544   192  60518
			'Culture.Media.Media*'                         14363  -->  11790  2573  1990  46664
			'Culture.Media.Music'                           2677  -->   2138   539   277  60063
			'Culture.Media.Radio'                           1174  -->    934   240    52  61791
			'Culture.Media.Software'                        1798  -->    965   833   397  60822
			'Culture.Media.Television'                      2200  -->   1415   785   223  60594
			'Culture.Media.Video games'                     2078  -->   1779   299    55  60884
			'Culture.Performing arts'                       1334  -->    797   537   127  61556
			'Culture.Philosophy and religion'               2638  -->   1359  1279   381  59998
			'Culture.Sports'                                5843  -->   5174   669   371  56803
			'Culture.Visual arts.Architecture'              2565  -->   1733   832   281  60171
			'Culture.Visual arts.Comics and Anime'          1488  -->    968   520   120  61409
			'Culture.Visual arts.Fashion'                   1188  -->    799   389    76  61753
			'Culture.Visual arts.Visual arts*'              5987  -->   3885  2102   586  56444
			'Geography.Geographical'                        3344  -->   1896  1448   293  59380
			'Geography.Regions.Africa.Africa*'              5693  -->   4329  1364   285  57039
			'Geography.Regions.Africa.Central Africa'         28  -->      1    27    62  62927
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    665   449    54  61849
			'Geography.Regions.Africa.Northern Africa'      1266  -->    709   557   109  61642
			'Geography.Regions.Africa.Southern Africa'      1288  -->    851   437    55  61674
			'Geography.Regions.Africa.Western Africa'       1152  -->    855   297    56  61809
			'Geography.Regions.Americas.Central America'    1326  -->    501   825   104  61587
			'Geography.Regions.Americas.North America'      7565  -->   4613  2952  1113  54339
			'Geography.Regions.Americas.South America'      1523  -->    756   767   209  61285
			'Geography.Regions.Asia.Asia*'                 11060  -->   8311  2749   983  50974
			'Geography.Regions.Asia.Central Asia'           1163  -->    641   522    77  61777
			'Geography.Regions.Asia.East Asia'              2721  -->   1645  1076   292  60004
			'Geography.Regions.Asia.North Asia'             1361  -->    773   588   173  61483
			'Geography.Regions.Asia.South Asia'             2438  -->   1930   508   111  60468
			'Geography.Regions.Asia.Southeast Asia'         1688  -->    909   779   104  61225
			'Geography.Regions.Asia.West Asia'              2264  -->   1432   832   132  60621
			'Geography.Regions.Europe.Eastern Europe'       3083  -->   1845  1238   350  59584
			'Geography.Regions.Europe.Europe*'             12415  -->   8206  4209  1900  48702
			'Geography.Regions.Europe.Northern Europe'      4244  -->   2037  2207   553  58220
			'Geography.Regions.Europe.Southern Europe'      2320  -->   1023  1297   248  60449
			'Geography.Regions.Europe.Western Europe'       3160  -->   1731  1429   430  59427
			'Geography.Regions.Oceania'                     2537  -->   1695   842   103  60377
			'History and Society.Business and economics'    3430  -->   1501  1929   539  59048
			'History and Society.Education'                 2178  -->   1010  1168   237  60602
			'History and Society.History'                   3217  -->    855  2362   340  59460
			'History and Society.Military and warfare'      3977  -->   2609  1368   432  58608
			'History and Society.Politics and government'   4647  -->   2204  2443   514  57856
			'History and Society.Society'                   4057  -->    928  3129   348  58612
			'History and Society.Transportation'            3604  -->   2952   652   251  59162
			'STEM.Biology'                                  2834  -->   2144   690   162  60021
			'STEM.Chemistry'                                1344  -->    887   457   185  61488
			'STEM.Computing'                                2011  -->   1243   768   428  60578
			'STEM.Earth and environment'                    1683  -->    953   730   125  61209
			'STEM.Engineering'                              2272  -->   1430   842   172  60573
			'STEM.Libraries & Information'                  1159  -->    603   556    93  61765
			'STEM.Mathematics'                              1121  -->    648   473   135  61761
			'STEM.Medicine & Health'                        1737  -->   1073   664   191  61089
			'STEM.Physics'                                  1206  -->    707   499   166  61645
			'STEM.STEM*'                                   16499  -->  13631  2868  1310  45208
			'STEM.Space'                                    1398  -->   1166   232    49  61570
			'STEM.Technology'                               3712  -->   2024  1688   707  58598
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
	match_rate (micro=0.052, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.087
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.01
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.009
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.022
		History and Society.Society                  0.009
		History and Society.Transportation           0.017
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.913
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.991
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.978
		History and Society.Society                  0.991
		History and Society.Transportation           0.983
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.688, macro=0.612):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.817
		Culture.Biography.Women                      0.36
		Culture.Food and drink                       0.717
		Culture.Internet culture                     0.746
		Culture.Linguistics                          0.671
		Culture.Literature                           0.69
		Culture.Media.Books                          0.631
		Culture.Media.Entertainment                  0.328
		Culture.Media.Films                          0.764
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.799
		Culture.Media.Radio                          0.796
		Culture.Media.Software                       0.537
		Culture.Media.Television                     0.643
		Culture.Media.Video games                    0.856
		Culture.Performing arts                      0.597
		Culture.Philosophy and religion              0.515
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.676
		Culture.Visual arts.Comics and Anime         0.651
		Culture.Visual arts.Fashion                  0.673
		Culture.Visual arts.Visual arts*             0.649
		Geography.Geographical                       0.567
		Geography.Regions.Africa.Africa*             0.76
		Geography.Regions.Africa.Central Africa      0.036
		Geography.Regions.Africa.Eastern Africa      0.597
		Geography.Regions.Africa.Northern Africa     0.56
		Geography.Regions.Africa.Southern Africa     0.661
		Geography.Regions.Africa.Western Africa      0.742
		Geography.Regions.Americas.Central America   0.378
		Geography.Regions.Americas.North America     0.61
		Geography.Regions.Americas.South America     0.496
		Geography.Regions.Asia.Asia*                 0.751
		Geography.Regions.Asia.Central Asia          0.551
		Geography.Regions.Asia.East Asia             0.605
		Geography.Regions.Asia.North Asia            0.568
		Geography.Regions.Asia.South Asia            0.792
		Geography.Regions.Asia.Southeast Asia        0.539
		Geography.Regions.Asia.West Asia             0.633
		Geography.Regions.Europe.Eastern Europe      0.598
		Geography.Regions.Europe.Europe*             0.661
		Geography.Regions.Europe.Northern Europe     0.48
		Geography.Regions.Europe.Southern Europe     0.441
		Geography.Regions.Europe.Western Europe      0.548
		Geography.Regions.Oceania                    0.668
		History and Society.Business and economics   0.438
		History and Society.Education                0.464
		History and Society.History                  0.266
		History and Society.Military and warfare     0.656
		History and Society.Politics and government  0.474
		History and Society.Society                  0.229
		History and Society.Transportation           0.819
		STEM.Biology                                 0.757
		STEM.Chemistry                               0.66
		STEM.Computing                               0.618
		STEM.Earth and environment                   0.566
		STEM.Engineering                             0.629
		STEM.Libraries & Information                 0.52
		STEM.Mathematics                             0.578
		STEM.Medicine & Health                       0.618
		STEM.Physics                                 0.586
		STEM.STEM*                                   0.826
		STEM.Space                                   0.834
		STEM.Technology                              0.545
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.659, macro=0.51):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.771
		Culture.Biography.Women                      0.374
		Culture.Food and drink                       0.574
		Culture.Internet culture                     0.421
		Culture.Linguistics                          0.744
		Culture.Literature                           0.514
		Culture.Media.Books                          0.42
		Culture.Media.Entertainment                  0.329
		Culture.Media.Films                          0.72
		Culture.Media.Media*                         0.555
		Culture.Media.Music                          0.81
		Culture.Media.Radio                          0.672
		Culture.Media.Software                       0.099
		Culture.Media.Television                     0.609
		Culture.Media.Video games                    0.713
		Culture.Performing arts                      0.457
		Culture.Philosophy and religion              0.468
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.608
		Culture.Visual arts.Comics and Anime         0.423
		Culture.Visual arts.Fashion                  0.307
		Culture.Visual arts.Visual arts*             0.541
		Geography.Geographical                       0.736
		Geography.Regions.Africa.Africa*             0.546
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.238
		Geography.Regions.Africa.Northern Africa     0.281
		Geography.Regions.Africa.Southern Africa     0.466
		Geography.Regions.Africa.Western Africa      0.359
		Geography.Regions.Americas.Central America   0.426
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.481
		Geography.Regions.Asia.Asia*                 0.655
		Geography.Regions.Asia.Central Asia          0.277
		Geography.Regions.Asia.East Asia             0.59
		Geography.Regions.Asia.North Asia            0.158
		Geography.Regions.Asia.South Asia            0.87
		Geography.Regions.Asia.Southeast Asia        0.658
		Geography.Regions.Asia.West Asia             0.763
		Geography.Regions.Europe.Eastern Europe      0.571
		Geography.Regions.Europe.Europe*             0.592
		Geography.Regions.Europe.Northern Europe     0.617
		Geography.Regions.Europe.Southern Europe     0.588
		Geography.Regions.Europe.Western Europe      0.599
		Geography.Regions.Oceania                    0.858
		History and Society.Business and economics   0.33
		History and Society.Education                0.469
		History and Society.History                  0.339
		History and Society.Military and warfare     0.561
		History and Society.Politics and government  0.61
		History and Society.Society                  0.331
		History and Society.Transportation           0.748
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.256
		STEM.Computing                               0.192
		STEM.Earth and environment                   0.559
		STEM.Engineering                             0.539
		STEM.Libraries & Information                 0.177
		STEM.Mathematics                             0.1
		STEM.Medicine & Health                       0.561
		STEM.Physics                                 0.157
		STEM.STEM*                                   0.686
		STEM.Space                                   0.864
		STEM.Technology                              0.191
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.985
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.666, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.793
		Culture.Biography.Women                      0.367
		Culture.Food and drink                       0.638
		Culture.Internet culture                     0.538
		Culture.Linguistics                          0.705
		Culture.Literature                           0.589
		Culture.Media.Books                          0.505
		Culture.Media.Entertainment                  0.328
		Culture.Media.Films                          0.741
		Culture.Media.Media*                         0.662
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.728
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.626
		Culture.Media.Video games                    0.778
		Culture.Performing arts                      0.518
		Culture.Philosophy and religion              0.49
		Culture.Sports                               0.899
		Culture.Visual arts.Architecture             0.64
		Culture.Visual arts.Comics and Anime         0.513
		Culture.Visual arts.Fashion                  0.422
		Culture.Visual arts.Visual arts*             0.59
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.636
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.34
		Geography.Regions.Africa.Northern Africa     0.374
		Geography.Regions.Africa.Southern Africa     0.547
		Geography.Regions.Africa.Western Africa      0.484
		Geography.Regions.Americas.Central America   0.401
		Geography.Regions.Americas.North America     0.641
		Geography.Regions.Americas.South America     0.489
		Geography.Regions.Asia.Asia*                 0.7
		Geography.Regions.Asia.Central Asia          0.369
		Geography.Regions.Asia.East Asia             0.597
		Geography.Regions.Asia.North Asia            0.247
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.592
		Geography.Regions.Asia.West Asia             0.691
		Geography.Regions.Europe.Eastern Europe      0.585
		Geography.Regions.Europe.Europe*             0.625
		Geography.Regions.Europe.Northern Europe     0.54
		Geography.Regions.Europe.Southern Europe     0.504
		Geography.Regions.Europe.Western Europe      0.572
		Geography.Regions.Oceania                    0.751
		History and Society.Business and economics   0.376
		History and Society.Education                0.466
		History and Society.History                  0.298
		History and Society.Military and warfare     0.605
		History and Society.Politics and government  0.534
		History and Society.Society                  0.271
		History and Society.Transportation           0.782
		STEM.Biology                                 0.825
		STEM.Chemistry                               0.369
		STEM.Computing                               0.293
		STEM.Earth and environment                   0.563
		STEM.Engineering                             0.581
		STEM.Libraries & Information                 0.264
		STEM.Mathematics                             0.17
		STEM.Medicine & Health                       0.588
		STEM.Physics                                 0.247
		STEM.STEM*                                   0.749
		STEM.Space                                   0.849
		STEM.Technology                              0.283
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.948
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.951
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.977
		History and Society.Society                  0.984
		History and Society.Transportation           0.993
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.034
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.041
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.02
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.009
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.966, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.952
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.977
		Culture.Literature                           0.973
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.959
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.988
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.981
		Culture.Philosophy and religion              0.958
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.551
		Geography.Regions.Africa.Eastern Africa      0.982
		Geography.Regions.Africa.Northern Africa     0.974
		Geography.Regions.Africa.Southern Africa     0.982
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.969
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.973
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.973
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.956
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.968
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.953
		History and Society.Education                0.963
		History and Society.History                  0.921
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.95
		History and Society.Society                  0.896
		History and Society.Transportation           0.985
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.985
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.972
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.967
		STEM.Space                                   0.991
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.709, macro=0.548):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.306
		Culture.Food and drink                       0.664
		Culture.Internet culture                     0.71
		Culture.Linguistics                          0.727
		Culture.Literature                           0.635
		Culture.Media.Books                          0.527
		Culture.Media.Entertainment                  0.291
		Culture.Media.Films                          0.793
		Culture.Media.Media*                         0.767
		Culture.Media.Music                          0.855
		Culture.Media.Radio                          0.818
		Culture.Media.Software                       0.124
		Culture.Media.Television                     0.644
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.54
		Culture.Philosophy and religion              0.434
		Culture.Sports                               0.926
		Culture.Visual arts.Architecture             0.7
		Culture.Visual arts.Comics and Anime         0.562
		Culture.Visual arts.Fashion                  0.377
		Culture.Visual arts.Visual arts*             0.622
		Geography.Geographical                       0.701
		Geography.Regions.Africa.Africa*             0.673
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.22
		Geography.Regions.Africa.Northern Africa     0.328
		Geography.Regions.Africa.Southern Africa     0.519
		Geography.Regions.Africa.Western Africa      0.432
		Geography.Regions.Americas.Central America   0.341
		Geography.Regions.Americas.North America     0.701
		Geography.Regions.Americas.South America     0.429
		Geography.Regions.Asia.Asia*                 0.744
		Geography.Regions.Asia.Central Asia          0.375
		Geography.Regions.Asia.East Asia             0.593
		Geography.Regions.Asia.North Asia            0.215
		Geography.Regions.Asia.South Asia            0.862
		Geography.Regions.Asia.Southeast Asia        0.563
		Geography.Regions.Asia.West Asia             0.738
		Geography.Regions.Europe.Eastern Europe      0.621
		Geography.Regions.Europe.Europe*             0.661
		Geography.Regions.Europe.Northern Europe     0.575
		Geography.Regions.Europe.Southern Europe     0.522
		Geography.Regions.Europe.Western Europe      0.584
		Geography.Regions.Oceania                    0.8
		History and Society.Business and economics   0.321
		History and Society.Education                0.402
		History and Society.History                  0.226
		History and Society.Military and warfare     0.66
		History and Society.Politics and government  0.579
		History and Society.Society                  0.223
		History and Society.Transportation           0.84
		STEM.Biology                                 0.882
		STEM.Chemistry                               0.42
		STEM.Computing                               0.219
		STEM.Earth and environment                   0.56
		STEM.Engineering                             0.605
		STEM.Libraries & Information                 0.224
		STEM.Mathematics                             0.187
		STEM.Medicine & Health                       0.566
		STEM.Physics                                 0.199
		STEM.STEM*                                   0.842
		STEM.Space                                   0.901
		STEM.Technology                              0.255
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}}}}}

