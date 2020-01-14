Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'min_weight_fraction_leaf': 0.0, 'max_features': 'log2', 'max_depth': 5, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'label_weights': {}, 'loss': 'deviance', 'multilabel': True, 'init': None, 'n_iter_no_change': None, 'scale': False, 'learning_rate': 0.1, 'random_state': None, 'tol': 0.0001, 'population_rates': None, 'center': False, 'min_impurity_split': None, 'validation_fraction': 0.1, 'n_estimators': 150, 'verbose': 0, 'subsample': 1.0, 'presort': 'auto', 'warm_start': False}
	Environment:
	 - revscoring_version: '2.6.3'
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
	counts (n=62977):
			label                                              n          TP    FP     FN     TN
			---------------------------------------------  -----  ---  -----  ----  -----  -----
			'Culture.Biography.Biography*'                 16480  -->  14106  2374   1209  45288
			'Culture.Biography.Women'                       4061  -->   2800  1261    675  58241
			'Culture.Food and drink'                        1307  -->    937   370     80  61590
			'Culture.Internet culture'                      2976  -->   2241   735    186  59815
			'Culture.Linguistics'                           1364  -->    928   436    124  61489
			'Culture.Literature'                            5280  -->   3651  1629    569  57128
			'Culture.Media.Books'                           1882  -->   1195   687    202  60893
			'Culture.Media.Entertainment'                   1830  -->    590  1240    125  61022
			'Culture.Media.Films'                           2259  -->   1721   538    199  60519
			'Culture.Media.Media*'                         14334  -->  11797  2537   1932  46711
			'Culture.Media.Music'                           2713  -->   2165   548    302  59962
			'Culture.Media.Radio'                           1187  -->    958   229     55  61735
			'Culture.Media.Software'                        1744  -->    939   805    397  60836
			'Culture.Media.Television'                      2240  -->   1456   784    241  60496
			'Culture.Media.Video games'                     2101  -->   1812   289     51  60825
			'Culture.Performing arts'                       1333  -->    786   547    113  61531
			'Culture.Philosophy and religion'               2735  -->   1403  1332    375  59867
			'Culture.Sports'                                5747  -->   5051   696    338  56892
			'Culture.Visual arts.Architecture'              2594  -->   1768   826    307  60076
			'Culture.Visual arts.Comics and Anime'          1558  -->   1028   530    127  61292
			'Culture.Visual arts.Fashion'                   1192  -->    817   375     64  61721
			'Culture.Visual arts.Visual arts*'              6044  -->   3894  2150    580  56353
			'Geography.Geographical'                        3465  -->   1999  1466    320  59192
			'Geography.Regions.Africa.Africa*'              5650  -->   4267  1383    269  57058
			'Geography.Regions.Africa.Central Africa'         29  -->      7    22  12002  50946
			'Geography.Regions.Africa.Eastern Africa'       1099  -->    651   448     40  61838
			'Geography.Regions.Africa.Northern Africa'      1282  -->    684   598    129  61566
			'Geography.Regions.Africa.Southern Africa'      1293  -->    801   492     47  61637
			'Geography.Regions.Africa.Western Africa'       1148  -->    866   282     72  61757
			'Geography.Regions.Americas.Central America'    1275  -->    462   813     92  61610
			'Geography.Regions.Americas.North America'      7582  -->   4633  2949   1130  54265
			'Geography.Regions.Americas.South America'      1522  -->    809   713    180  61275
			'Geography.Regions.Asia.Asia*'                 10920  -->   8209  2711    977  51080
			'Geography.Regions.Asia.Central Asia'           1152  -->    644   508     73  61752
			'Geography.Regions.Asia.East Asia'              2640  -->   1595  1045    285  60052
			'Geography.Regions.Asia.North Asia'             1407  -->    825   582    175  61395
			'Geography.Regions.Asia.South Asia'             2350  -->   1881   469    123  60504
			'Geography.Regions.Asia.Southeast Asia'         1648  -->    869   779     91  61238
			'Geography.Regions.Asia.West Asia'              2239  -->   1430   809    148  60590
			'Geography.Regions.Europe.Eastern Europe'       3095  -->   1869  1226    349  59533
			'Geography.Regions.Europe.Europe*'             12440  -->   8377  4063   1855  48682
			'Geography.Regions.Europe.Northern Europe'      4118  -->   2090  2028    507  58352
			'Geography.Regions.Europe.Southern Europe'      2395  -->   1079  1316    254  60328
			'Geography.Regions.Europe.Western Europe'       3166  -->   1724  1442    425  59386
			'Geography.Regions.Oceania'                     2569  -->   1708   861     96  60312
			'History and Society.Business and economics'    3434  -->   1481  1953    517  59026
			'History and Society.Education'                 2151  -->    996  1155    243  60583
			'History and Society.History'                   3287  -->   1032  2255    386  59304
			'History and Society.Military and warfare'      4024  -->   2701  1323    415  58538
			'History and Society.Politics and government'   4585  -->   2168  2417    472  57920
			'History and Society.Society'                   4008  -->    933  3075    299  58670
			'History and Society.Transportation'            3545  -->   2883   662    266  59166
			'STEM.Biology'                                  2858  -->   2168   690    170  59949
			'STEM.Chemistry'                                1280  -->    840   440    184  61513
			'STEM.Computing'                                2029  -->   1298   731    400  60548
			'STEM.Earth and environment'                    1685  -->    967   718    123  61169
			'STEM.Engineering'                              2251  -->   1401   850    198  60528
			'STEM.Libraries & Information'                  1159  -->    648   511     90  61728
			'STEM.Mathematics'                              1104  -->    634   470    103  61770
			'STEM.Medicine & Health'                        1729  -->   1108   621    176  61072
			'STEM.Physics'                                  1187  -->    637   550    176  61614
			'STEM.STEM*'                                   16385  -->  13639  2746   1263  45329
			'STEM.Space'                                    1408  -->   1173   235     56  61513
			'STEM.Technology'                               3627  -->   1970  1657    621  58729
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.262         0.123
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.047         0.004
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.228         0.058
		Culture.Media.Music                             0.043         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.036         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.043         0.011
		Culture.Sports                                  0.091         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.025         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.096         0.018
		Geography.Geographical                          0.055         0.024
		Geography.Regions.Africa.Africa*                0.09          0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.02          0.003
		Geography.Regions.Americas.North America        0.12          0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.173         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.042         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.037         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.198         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.05          0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.051, macro=0.02):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.021
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.085
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.191
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.01
		Geography.Regions.Europe.Western Europe      0.017
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.01
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.021
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.98):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.915
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.809
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.99
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.979
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.701, macro=0.623):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.856
		Culture.Biography.Women                      0.689
		Culture.Food and drink                       0.717
		Culture.Internet culture                     0.753
		Culture.Linguistics                          0.68
		Culture.Literature                           0.691
		Culture.Media.Books                          0.635
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.762
		Culture.Media.Media*                         0.823
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.807
		Culture.Media.Software                       0.538
		Culture.Media.Television                     0.65
		Culture.Media.Video games                    0.862
		Culture.Performing arts                      0.59
		Culture.Philosophy and religion              0.513
		Culture.Sports                               0.879
		Culture.Visual arts.Architecture             0.682
		Culture.Visual arts.Comics and Anime         0.66
		Culture.Visual arts.Fashion                  0.685
		Culture.Visual arts.Visual arts*             0.644
		Geography.Geographical                       0.577
		Geography.Regions.Africa.Africa*             0.755
		Geography.Regions.Africa.Central Africa      0.241
		Geography.Regions.Africa.Eastern Africa      0.592
		Geography.Regions.Africa.Northern Africa     0.534
		Geography.Regions.Africa.Southern Africa     0.619
		Geography.Regions.Africa.Western Africa      0.754
		Geography.Regions.Americas.Central America   0.362
		Geography.Regions.Americas.North America     0.611
		Geography.Regions.Americas.South America     0.532
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.559
		Geography.Regions.Asia.East Asia             0.604
		Geography.Regions.Asia.North Asia            0.586
		Geography.Regions.Asia.South Asia            0.8
		Geography.Regions.Asia.Southeast Asia        0.527
		Geography.Regions.Asia.West Asia             0.639
		Geography.Regions.Europe.Eastern Europe      0.604
		Geography.Regions.Europe.Europe*             0.673
		Geography.Regions.Europe.Northern Europe     0.508
		Geography.Regions.Europe.Southern Europe     0.451
		Geography.Regions.Europe.Western Europe      0.545
		Geography.Regions.Oceania                    0.665
		History and Society.Business and economics   0.431
		History and Society.Education                0.463
		History and Society.History                  0.314
		History and Society.Military and warfare     0.671
		History and Society.Politics and government  0.473
		History and Society.Society                  0.233
		History and Society.Transportation           0.813
		STEM.Biology                                 0.759
		STEM.Chemistry                               0.656
		STEM.Computing                               0.64
		STEM.Earth and environment                   0.574
		STEM.Engineering                             0.622
		STEM.Libraries & Information                 0.559
		STEM.Mathematics                             0.574
		STEM.Medicine & Health                       0.641
		STEM.Physics                                 0.537
		STEM.STEM*                                   0.832
		STEM.Space                                   0.833
		STEM.Technology                              0.543
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.96
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
		Geography.Regions.Africa.Central Africa      0.809
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.671, macro=0.517):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.822
		Culture.Biography.Women                      0.471
		Culture.Food and drink                       0.577
		Culture.Internet culture                     0.461
		Culture.Linguistics                          0.714
		Culture.Literature                           0.525
		Culture.Media.Books                          0.437
		Culture.Media.Entertainment                  0.362
		Culture.Media.Films                          0.712
		Culture.Media.Media*                         0.562
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.662
		Culture.Media.Software                       0.091
		Culture.Media.Television                     0.593
		Culture.Media.Video games                    0.73
		Culture.Performing arts                      0.482
		Culture.Philosophy and religion              0.47
		Culture.Sports                               0.92
		Culture.Visual arts.Architecture             0.589
		Culture.Visual arts.Comics and Anime         0.413
		Culture.Visual arts.Fashion                  0.349
		Culture.Visual arts.Visual arts*             0.541
		Geography.Geographical                       0.722
		Geography.Regions.Africa.Africa*             0.559
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.294
		Geography.Regions.Africa.Northern Africa     0.239
		Geography.Regions.Africa.Southern Africa     0.489
		Geography.Regions.Africa.Western Africa      0.307
		Geography.Regions.Americas.Central America   0.446
		Geography.Regions.Americas.North America     0.673
		Geography.Regions.Americas.South America     0.536
		Geography.Regions.Asia.Asia*                 0.657
		Geography.Regions.Asia.Central Asia          0.291
		Geography.Regions.Asia.East Asia             0.596
		Geography.Regions.Asia.North Asia            0.16
		Geography.Regions.Asia.South Asia            0.859
		Geography.Regions.Asia.Southeast Asia        0.682
		Geography.Regions.Asia.West Asia             0.743
		Geography.Regions.Europe.Eastern Europe      0.574
		Geography.Regions.Europe.Europe*             0.602
		Geography.Regions.Europe.Northern Europe     0.65
		Geography.Regions.Europe.Southern Europe     0.585
		Geography.Regions.Europe.Western Europe      0.6
		Geography.Regions.Oceania                    0.865
		History and Society.Business and economics   0.336
		History and Society.Education                0.462
		History and Society.History                  0.349
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.629
		History and Society.Society                  0.37
		History and Society.Transportation           0.736
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.256
		STEM.Computing                               0.216
		STEM.Earth and environment                   0.566
		STEM.Engineering                             0.501
		STEM.Libraries & Information                 0.193
		STEM.Mathematics                             0.126
		STEM.Medicine & Health                       0.59
		STEM.Physics                                 0.138
		STEM.STEM*                                   0.695
		STEM.Space                                   0.847
		STEM.Technology                              0.207
		-------------------------------------------  -----
	!precision (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.995
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
		Geography.Regions.Europe.Europe*             0.973
		Geography.Regions.Europe.Northern Europe     0.985
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
	f1 (micro=0.679, macro=0.545):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.839
		Culture.Biography.Women                      0.56
		Culture.Food and drink                       0.64
		Culture.Internet culture                     0.572
		Culture.Linguistics                          0.697
		Culture.Literature                           0.597
		Culture.Media.Books                          0.518
		Culture.Media.Entertainment                  0.341
		Culture.Media.Films                          0.736
		Culture.Media.Media*                         0.668
		Culture.Media.Music                          0.797
		Culture.Media.Radio                          0.727
		Culture.Media.Software                       0.156
		Culture.Media.Television                     0.62
		Culture.Media.Video games                    0.79
		Culture.Performing arts                      0.531
		Culture.Philosophy and religion              0.491
		Culture.Sports                               0.899
		Culture.Visual arts.Architecture             0.632
		Culture.Visual arts.Comics and Anime         0.508
		Culture.Visual arts.Fashion                  0.462
		Culture.Visual arts.Visual arts*             0.588
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.642
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.393
		Geography.Regions.Africa.Northern Africa     0.33
		Geography.Regions.Africa.Southern Africa     0.547
		Geography.Regions.Africa.Western Africa      0.437
		Geography.Regions.Americas.Central America   0.4
		Geography.Regions.Americas.North America     0.641
		Geography.Regions.Americas.South America     0.534
		Geography.Regions.Asia.Asia*                 0.701
		Geography.Regions.Asia.Central Asia          0.383
		Geography.Regions.Asia.East Asia             0.6
		Geography.Regions.Asia.North Asia            0.252
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.595
		Geography.Regions.Asia.West Asia             0.687
		Geography.Regions.Europe.Eastern Europe      0.589
		Geography.Regions.Europe.Europe*             0.636
		Geography.Regions.Europe.Northern Europe     0.57
		Geography.Regions.Europe.Southern Europe     0.509
		Geography.Regions.Europe.Western Europe      0.571
		Geography.Regions.Oceania                    0.752
		History and Society.Business and economics   0.378
		History and Society.Education                0.463
		History and Society.History                  0.331
		History and Society.Military and warfare     0.62
		History and Society.Politics and government  0.54
		History and Society.Society                  0.286
		History and Society.Transportation           0.773
		STEM.Biology                                 0.825
		STEM.Chemistry                               0.368
		STEM.Computing                               0.323
		STEM.Earth and environment                   0.57
		STEM.Engineering                             0.555
		STEM.Libraries & Information                 0.287
		STEM.Mathematics                             0.206
		STEM.Medicine & Health                       0.614
		STEM.Physics                                 0.22
		STEM.STEM*                                   0.758
		STEM.Space                                   0.84
		STEM.Technology                              0.3
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
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
		Geography.Regions.Africa.Central Africa      0.895
		Geography.Regions.Africa.Eastern Africa      1
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
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.959
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.952
		Culture.Media.Music                          0.99
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
		Geography.Regions.Africa.Central Africa      0.809
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.977
		History and Society.Society                  0.985
		History and Society.Transportation           0.993
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.009):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.011
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.04
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
		Geography.Regions.Africa.Central Africa      0.191
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.02
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.009
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.968, macro=0.967):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.985
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.974
		Culture.Literature                           0.974
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.959
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.986
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.957
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.985
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.576
		Geography.Regions.Africa.Eastern Africa      0.981
		Geography.Regions.Africa.Northern Africa     0.977
		Geography.Regions.Africa.Southern Africa     0.981
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.967
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.975
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.973
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.977
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.959
		Geography.Regions.Europe.Southern Europe     0.968
		Geography.Regions.Europe.Western Europe      0.968
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.952
		History and Society.Education                0.961
		History and Society.History                  0.927
		History and Society.Military and warfare     0.977
		History and Society.Politics and government  0.948
		History and Society.Society                  0.89
		History and Society.Transportation           0.985
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.984
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.975
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.978
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.968
		STEM.Space                                   0.992
		STEM.Technology                              0.963
		-------------------------------------------  -----
	pr_auc (micro=0.718, macro=0.555):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.901
		Culture.Biography.Women                      0.522
		Culture.Food and drink                       0.642
		Culture.Internet culture                     0.73
		Culture.Linguistics                          0.65
		Culture.Literature                           0.649
		Culture.Media.Books                          0.527
		Culture.Media.Entertainment                  0.319
		Culture.Media.Films                          0.772
		Culture.Media.Media*                         0.763
		Culture.Media.Music                          0.854
		Culture.Media.Radio                          0.812
		Culture.Media.Software                       0.105
		Culture.Media.Television                     0.646
		Culture.Media.Video games                    0.895
		Culture.Performing arts                      0.507
		Culture.Philosophy and religion              0.42
		Culture.Sports                               0.926
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.508
		Culture.Visual arts.Fashion                  0.422
		Culture.Visual arts.Visual arts*             0.617
		Geography.Geographical                       0.688
		Geography.Regions.Africa.Africa*             0.645
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.414
		Geography.Regions.Africa.Northern Africa     0.275
		Geography.Regions.Africa.Southern Africa     0.485
		Geography.Regions.Africa.Western Africa      0.434
		Geography.Regions.Americas.Central America   0.352
		Geography.Regions.Americas.North America     0.707
		Geography.Regions.Americas.South America     0.519
		Geography.Regions.Asia.Asia*                 0.744
		Geography.Regions.Asia.Central Asia          0.45
		Geography.Regions.Asia.East Asia             0.607
		Geography.Regions.Asia.North Asia            0.185
		Geography.Regions.Asia.South Asia            0.858
		Geography.Regions.Asia.Southeast Asia        0.605
		Geography.Regions.Asia.West Asia             0.752
		Geography.Regions.Europe.Eastern Europe      0.622
		Geography.Regions.Europe.Europe*             0.668
		Geography.Regions.Europe.Northern Europe     0.593
		Geography.Regions.Europe.Southern Europe     0.506
		Geography.Regions.Europe.Western Europe      0.577
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.314
		History and Society.Education                0.419
		History and Society.History                  0.25
		History and Society.Military and warfare     0.672
		History and Society.Politics and government  0.57
		History and Society.Society                  0.235
		History and Society.Transportation           0.833
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.302
		STEM.Computing                               0.271
		STEM.Earth and environment                   0.506
		STEM.Engineering                             0.597
		STEM.Libraries & Information                 0.294
		STEM.Mathematics                             0.214
		STEM.Medicine & Health                       0.62
		STEM.Physics                                 0.174
		STEM.STEM*                                   0.847
		STEM.Space                                   0.885
		STEM.Technology                              0.26
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}}}}}

