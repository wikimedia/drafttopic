Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'min_samples_leaf': 1, 'max_leaf_nodes': None, 'warm_start': False, 'multilabel': True, 'n_iter_no_change': None, 'min_samples_split': 2, 'init': None, 'population_rates': None, 'center': False, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'max_depth': 5, 'scale': False, 'validation_fraction': 0.1, 'loss': 'deviance', 'label_weights': {}, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_estimators': 150, 'verbose': 0, 'tol': 0.0001, 'max_features': 'log2', 'subsample': 1.0, 'random_state': None, 'learning_rate': 0.1, 'presort': 'auto'}
	Environment:
	 - revscoring_version: '2.6.2'
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
			'Culture.Biography.Biography*'                 16717  -->  13633  3084  1613  44687
			'Culture.Biography.Women'                       4173  -->   1502  2671   485  58359
			'Culture.Food and drink'                        1323  -->    939   384    84  61610
			'Culture.Internet culture'                      2946  -->   2194   752   200  59871
			'Culture.Linguistics'                           1384  -->    932   452    81  61552
			'Culture.Literature'                            5277  -->   3644  1633   573  57167
			'Culture.Media.Books'                           1919  -->   1201   718   205  60893
			'Culture.Media.Entertainment'                   1876  -->    590  1286   145  60996
			'Culture.Media.Films'                           2307  -->   1761   546   184  60526
			'Culture.Media.Media*'                         14363  -->  11784  2579  1941  46713
			'Culture.Media.Music'                           2677  -->   2124   553   297  60043
			'Culture.Media.Radio'                           1174  -->    929   245    50  61793
			'Culture.Media.Software'                        1798  -->    957   841   394  60825
			'Culture.Media.Television'                      2200  -->   1394   806   235  60582
			'Culture.Media.Video games'                     2078  -->   1789   289    54  60885
			'Culture.Performing arts'                       1334  -->    797   537    95  61588
			'Culture.Philosophy and religion'               2638  -->   1338  1300   393  59986
			'Culture.Sports'                                5843  -->   5191   652   359  56815
			'Culture.Visual arts.Architecture'              2565  -->   1717   848   286  60166
			'Culture.Visual arts.Comics and Anime'          1488  -->    975   513   112  61417
			'Culture.Visual arts.Fashion'                   1188  -->    787   401    80  61749
			'Culture.Visual arts.Visual arts*'              5987  -->   3883  2104   582  56448
			'Geography.Geographical'                        3344  -->   1917  1427   304  59369
			'Geography.Regions.Africa.Africa*'              5693  -->   4318  1375   266  57058
			'Geography.Regions.Africa.Central Africa'         28  -->      1    27    22  62967
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    675   439    56  61847
			'Geography.Regions.Africa.Northern Africa'      1266  -->    701   565   109  61642
			'Geography.Regions.Africa.Southern Africa'      1288  -->    841   447    69  61660
			'Geography.Regions.Africa.Western Africa'       1152  -->    836   316    54  61811
			'Geography.Regions.Americas.Central America'    1326  -->    510   816   114  61577
			'Geography.Regions.Americas.North America'      7565  -->   4621  2944  1121  54331
			'Geography.Regions.Americas.South America'      1523  -->    762   761   179  61315
			'Geography.Regions.Asia.Asia*'                 11060  -->   8279  2781   954  51003
			'Geography.Regions.Asia.Central Asia'           1163  -->    615   548    77  61777
			'Geography.Regions.Asia.East Asia'              2721  -->   1680  1041   291  60005
			'Geography.Regions.Asia.North Asia'             1361  -->    788   573   190  61466
			'Geography.Regions.Asia.South Asia'             2438  -->   1918   520   133  60446
			'Geography.Regions.Asia.Southeast Asia'         1688  -->    893   795   106  61223
			'Geography.Regions.Asia.West Asia'              2264  -->   1435   829   136  60617
			'Geography.Regions.Europe.Eastern Europe'       3083  -->   1840  1243   346  59588
			'Geography.Regions.Europe.Europe*'             12415  -->   8289  4126  1899  48703
			'Geography.Regions.Europe.Northern Europe'      4244  -->   2034  2210   547  58226
			'Geography.Regions.Europe.Southern Europe'      2320  -->   1037  1283   259  60438
			'Geography.Regions.Europe.Western Europe'       3160  -->   1748  1412   426  59431
			'Geography.Regions.Oceania'                     2537  -->   1670   867   114  60366
			'History and Society.Business and economics'    3430  -->   1505  1925   544  59043
			'History and Society.Education'                 2178  -->   1025  1153   235  60604
			'History and Society.History'                   3217  -->    892  2325   339  59461
			'History and Society.Military and warfare'      3977  -->   2651  1326   407  58633
			'History and Society.Politics and government'   4647  -->   2205  2442   527  57843
			'History and Society.Society'                   4057  -->    943  3114   338  58622
			'History and Society.Transportation'            3604  -->   2932   672   257  59156
			'STEM.Biology'                                  2834  -->   2158   676   161  60022
			'STEM.Chemistry'                                1344  -->    887   457   187  61486
			'STEM.Computing'                                2011  -->   1202   809   456  60550
			'STEM.Earth and environment'                    1683  -->    960   723   119  61215
			'STEM.Engineering'                              2272  -->   1439   833   190  60555
			'STEM.Libraries & Information'                  1159  -->    596   563    82  61776
			'STEM.Mathematics'                              1121  -->    641   480   124  61772
			'STEM.Medicine & Health'                        1737  -->   1051   686   197  61083
			'STEM.Physics'                                  1206  -->    700   506   181  61630
			'STEM.STEM*'                                   16499  -->  13640  2859  1278  45240
			'STEM.Space'                                    1398  -->   1167   231    53  61566
			'STEM.Technology'                               3712  -->   1984  1728   691  58614
	rates:
		              'Culture.Biography.Biography*'    'Culture.Biography.Women'    'Culture.Food and drink'    'Culture.Internet culture'    'Culture.Linguistics'    'Culture.Literature'    'Culture.Media.Books'    'Culture.Media.Entertainment'    'Culture.Media.Films'    'Culture.Media.Media*'    'Culture.Media.Music'    'Culture.Media.Radio'    'Culture.Media.Software'    'Culture.Media.Television'    'Culture.Media.Video games'    'Culture.Performing arts'    'Culture.Philosophy and religion'    'Culture.Sports'    'Culture.Visual arts.Architecture'    'Culture.Visual arts.Comics and Anime'    'Culture.Visual arts.Fashion'    'Culture.Visual arts.Visual arts*'    'Geography.Geographical'    'Geography.Regions.Africa.Africa*'    'Geography.Regions.Africa.Central Africa'    'Geography.Regions.Africa.Eastern Africa'    'Geography.Regions.Africa.Northern Africa'    'Geography.Regions.Africa.Southern Africa'    'Geography.Regions.Africa.Western Africa'    'Geography.Regions.Americas.Central America'    'Geography.Regions.Americas.North America'    'Geography.Regions.Americas.South America'    'Geography.Regions.Asia.Asia*'    'Geography.Regions.Asia.Central Asia'    'Geography.Regions.Asia.East Asia'    'Geography.Regions.Asia.North Asia'    'Geography.Regions.Asia.South Asia'    'Geography.Regions.Asia.Southeast Asia'    'Geography.Regions.Asia.West Asia'    'Geography.Regions.Europe.Eastern Europe'    'Geography.Regions.Europe.Europe*'    'Geography.Regions.Europe.Northern Europe'    'Geography.Regions.Europe.Southern Europe'    'Geography.Regions.Europe.Western Europe'    'Geography.Regions.Oceania'    'History and Society.Business and economics'    'History and Society.Education'    'History and Society.History'    'History and Society.Military and warfare'    'History and Society.Politics and government'    'History and Society.Society'    'History and Society.Transportation'    'STEM.Biology'    'STEM.Chemistry'    'STEM.Computing'    'STEM.Earth and environment'    'STEM.Engineering'    'STEM.Libraries & Information'    'STEM.Mathematics'    'STEM.Medicine & Health'    'STEM.Physics'    'STEM.STEM*'    'STEM.Space'    'STEM.Technology'
		----------  --------------------------------  ---------------------------  --------------------------  ----------------------------  -----------------------  ----------------------  -----------------------  -------------------------------  -----------------------  ------------------------  -----------------------  -----------------------  --------------------------  ----------------------------  -----------------------------  ---------------------------  -----------------------------------  ------------------  ------------------------------------  ----------------------------------------  -------------------------------  ------------------------------------  --------------------------  ------------------------------------  -------------------------------------------  -------------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  ----------------------------------------------  --------------------------------------------  --------------------------------------------  --------------------------------  ---------------------------------------  ------------------------------------  -------------------------------------  -------------------------------------  -----------------------------------------  ------------------------------------  -------------------------------------------  ------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  -----------------------------  ----------------------------------------------  ---------------------------------  -------------------------------  --------------------------------------------  -----------------------------------------------  -------------------------------  --------------------------------------  ----------------  ------------------  ------------------  ------------------------------  --------------------  --------------------------------  --------------------  --------------------------  ----------------  --------------  --------------  -------------------
		sample                                 0.265                        0.066                       0.021                         0.047                    0.022                   0.084                    0.03                             0.03                     0.037                     0.228                    0.042                    0.019                       0.029                         0.035                          0.033                        0.021                                0.042               0.093                                 0.041                                     0.024                            0.019                                 0.095                       0.053                                 0.09                                             0                                        0.018                                         0.02                                          0.02                                         0.018                                           0.021                                         0.12                                          0.024                             0.176                                    0.018                                 0.043                                  0.022                                  0.039                                      0.027                                 0.036                                        0.049                                 0.197                                         0.067                                         0.037                                        0.05                           0.04                                            0.054                              0.035                            0.051                                         0.063                                            0.074                            0.064                                   0.057             0.045               0.021               0.032                           0.027                 0.036                             0.018                 0.018                       0.028             0.019           0.262           0.022                0.059
		population                             0.123                        0.015                       0.002                         0.004                    0.007                   0.016                    0.004                            0.004                    0.011                     0.059                    0.024                    0.002                       0.001                         0.009                          0.003                        0.003                                0.011               0.071                                 0.011                                     0.002                            0.001                                 0.018                       0.024                                 0.008                                            0                                        0                                             0.001                                         0.001                                        0.001                                           0.003                                         0.064                                         0.006                             0.046                                    0.001                                 0.011                                  0.001                                  0.015                                      0.006                                 0.011                                        0.013                                 0.076                                         0.031                                         0.013                                        0.019                          0.015                                           0.01                               0.007                            0.011                                         0.014                                            0.028                            0.013                                   0.015             0.034               0.002               0.003                           0.005                 0.005                             0.001                 0                           0.006             0.001           0.069           0.006                0.005
	match_rate (micro=0.052, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.086
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
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.914
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
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.688, macro=0.61):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.816
		Culture.Biography.Women                      0.36
		Culture.Food and drink                       0.71
		Culture.Internet culture                     0.745
		Culture.Linguistics                          0.673
		Culture.Literature                           0.691
		Culture.Media.Books                          0.626
		Culture.Media.Entertainment                  0.314
		Culture.Media.Films                          0.763
		Culture.Media.Media*                         0.82
		Culture.Media.Music                          0.793
		Culture.Media.Radio                          0.791
		Culture.Media.Software                       0.532
		Culture.Media.Television                     0.634
		Culture.Media.Video games                    0.861
		Culture.Performing arts                      0.597
		Culture.Philosophy and religion              0.507
		Culture.Sports                               0.888
		Culture.Visual arts.Architecture             0.669
		Culture.Visual arts.Comics and Anime         0.655
		Culture.Visual arts.Fashion                  0.662
		Culture.Visual arts.Visual arts*             0.649
		Geography.Geographical                       0.573
		Geography.Regions.Africa.Africa*             0.758
		Geography.Regions.Africa.Central Africa      0.036
		Geography.Regions.Africa.Eastern Africa      0.606
		Geography.Regions.Africa.Northern Africa     0.554
		Geography.Regions.Africa.Southern Africa     0.653
		Geography.Regions.Africa.Western Africa      0.726
		Geography.Regions.Americas.Central America   0.385
		Geography.Regions.Americas.North America     0.611
		Geography.Regions.Americas.South America     0.5
		Geography.Regions.Asia.Asia*                 0.749
		Geography.Regions.Asia.Central Asia          0.529
		Geography.Regions.Asia.East Asia             0.617
		Geography.Regions.Asia.North Asia            0.579
		Geography.Regions.Asia.South Asia            0.787
		Geography.Regions.Asia.Southeast Asia        0.529
		Geography.Regions.Asia.West Asia             0.634
		Geography.Regions.Europe.Eastern Europe      0.597
		Geography.Regions.Europe.Europe*             0.668
		Geography.Regions.Europe.Northern Europe     0.479
		Geography.Regions.Europe.Southern Europe     0.447
		Geography.Regions.Europe.Western Europe      0.553
		Geography.Regions.Oceania                    0.658
		History and Society.Business and economics   0.439
		History and Society.Education                0.471
		History and Society.History                  0.277
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.474
		History and Society.Society                  0.232
		History and Society.Transportation           0.814
		STEM.Biology                                 0.761
		STEM.Chemistry                               0.66
		STEM.Computing                               0.598
		STEM.Earth and environment                   0.57
		STEM.Engineering                             0.633
		STEM.Libraries & Information                 0.514
		STEM.Mathematics                             0.572
		STEM.Medicine & Health                       0.605
		STEM.Physics                                 0.58
		STEM.STEM*                                   0.827
		STEM.Space                                   0.835
		STEM.Technology                              0.534
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
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
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.982
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
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.66, macro=0.511):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.767
		Culture.Biography.Women                      0.392
		Culture.Food and drink                       0.563
		Culture.Internet culture                     0.44
		Culture.Linguistics                          0.791
		Culture.Literature                           0.523
		Culture.Media.Books                          0.43
		Culture.Media.Entertainment                  0.323
		Culture.Media.Films                          0.728
		Culture.Media.Media*                         0.561
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.679
		Culture.Media.Software                       0.099
		Culture.Media.Television                     0.593
		Culture.Media.Video games                    0.718
		Culture.Performing arts                      0.529
		Culture.Philosophy and religion              0.456
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.602
		Culture.Visual arts.Comics and Anime         0.442
		Culture.Visual arts.Fashion                  0.293
		Culture.Visual arts.Visual arts*             0.542
		Geography.Geographical                       0.731
		Geography.Regions.Africa.Africa*             0.562
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.234
		Geography.Regions.Africa.Northern Africa     0.278
		Geography.Regions.Africa.Southern Africa     0.407
		Geography.Regions.Africa.Western Africa      0.363
		Geography.Regions.Americas.Central America   0.408
		Geography.Regions.Americas.North America     0.675
		Geography.Regions.Americas.South America     0.522
		Geography.Regions.Asia.Asia*                 0.66
		Geography.Regions.Asia.Central Asia          0.269
		Geography.Regions.Asia.East Asia             0.596
		Geography.Regions.Asia.North Asia            0.148
		Geography.Regions.Asia.South Asia            0.847
		Geography.Regions.Asia.Southeast Asia        0.649
		Geography.Regions.Asia.West Asia             0.757
		Geography.Regions.Europe.Eastern Europe      0.573
		Geography.Regions.Europe.Europe*             0.595
		Geography.Regions.Europe.Northern Europe     0.619
		Geography.Regions.Europe.Southern Europe     0.581
		Geography.Regions.Europe.Western Europe      0.603
		Geography.Regions.Oceania                    0.843
		History and Society.Business and economics   0.329
		History and Society.Education                0.475
		History and Society.History                  0.349
		History and Society.Military and warfare     0.58
		History and Society.Politics and government  0.604
		History and Society.Society                  0.341
		History and Society.Transportation           0.742
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.254
		STEM.Computing                               0.177
		STEM.Earth and environment                   0.573
		STEM.Engineering                             0.516
		STEM.Libraries & Information                 0.194
		STEM.Mathematics                             0.106
		STEM.Medicine & Health                       0.548
		STEM.Physics                                 0.144
		STEM.STEM*                                   0.691
		STEM.Space                                   0.855
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
		Culture.Media.Books                          0.998
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
		Culture.Visual arts.Architecture             0.996
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
		Geography.Regions.Asia.East Asia             0.996
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
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.667, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.79
		Culture.Biography.Women                      0.375
		Culture.Food and drink                       0.628
		Culture.Internet culture                     0.553
		Culture.Linguistics                          0.727
		Culture.Literature                           0.595
		Culture.Media.Books                          0.51
		Culture.Media.Entertainment                  0.319
		Culture.Media.Films                          0.745
		Culture.Media.Media*                         0.666
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.731
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.613
		Culture.Media.Video games                    0.783
		Culture.Performing arts                      0.561
		Culture.Philosophy and religion              0.48
		Culture.Sports                               0.902
		Culture.Visual arts.Architecture             0.634
		Culture.Visual arts.Comics and Anime         0.528
		Culture.Visual arts.Fashion                  0.406
		Culture.Visual arts.Visual arts*             0.591
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.646
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.337
		Geography.Regions.Africa.Northern Africa     0.37
		Geography.Regions.Africa.Southern Africa     0.502
		Geography.Regions.Africa.Western Africa      0.484
		Geography.Regions.Americas.Central America   0.396
		Geography.Regions.Americas.North America     0.641
		Geography.Regions.Americas.South America     0.511
		Geography.Regions.Asia.Asia*                 0.702
		Geography.Regions.Asia.Central Asia          0.357
		Geography.Regions.Asia.East Asia             0.607
		Geography.Regions.Asia.North Asia            0.236
		Geography.Regions.Asia.South Asia            0.816
		Geography.Regions.Asia.Southeast Asia        0.583
		Geography.Regions.Asia.West Asia             0.69
		Geography.Regions.Europe.Eastern Europe      0.585
		Geography.Regions.Europe.Europe*             0.629
		Geography.Regions.Europe.Northern Europe     0.54
		Geography.Regions.Europe.Southern Europe     0.505
		Geography.Regions.Europe.Western Europe      0.577
		Geography.Regions.Oceania                    0.739
		History and Society.Business and economics   0.376
		History and Society.Education                0.473
		History and Society.History                  0.309
		History and Society.Military and warfare     0.62
		History and Society.Politics and government  0.531
		History and Society.Society                  0.277
		History and Society.Transportation           0.776
		STEM.Biology                                 0.828
		STEM.Chemistry                               0.367
		STEM.Computing                               0.274
		STEM.Earth and environment                   0.572
		STEM.Engineering                             0.569
		STEM.Libraries & Information                 0.282
		STEM.Mathematics                             0.179
		STEM.Medicine & Health                       0.575
		STEM.Physics                                 0.231
		STEM.STEM*                                   0.753
		STEM.Space                                   0.845
		STEM.Technology                              0.282
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.991
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
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
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
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
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
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.952
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.976
		History and Society.Society                  0.985
		History and Society.Transportation           0.993
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
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
		Culture.Biography.Biography*                 0.035
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
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
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.02
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.018
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
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.966, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.952
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.975
		Culture.Literature                           0.974
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.957
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.989
		Culture.Media.Software                       0.979
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.982
		Culture.Philosophy and religion              0.959
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.981
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.963
		Geography.Regions.Africa.Africa*             0.979
		Geography.Regions.Africa.Central Africa      0.587
		Geography.Regions.Africa.Eastern Africa      0.982
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.982
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.973
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.956
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.978
		History and Society.Business and economics   0.951
		History and Society.Education                0.963
		History and Society.History                  0.924
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.948
		History and Society.Society                  0.894
		History and Society.Transportation           0.985
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.985
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.975
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.968
		STEM.Space                                   0.992
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.709, macro=0.545):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.864
		Culture.Biography.Women                      0.313
		Culture.Food and drink                       0.647
		Culture.Internet culture                     0.715
		Culture.Linguistics                          0.721
		Culture.Literature                           0.648
		Culture.Media.Books                          0.481
		Culture.Media.Entertainment                  0.278
		Culture.Media.Films                          0.794
		Culture.Media.Media*                         0.77
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.784
		Culture.Media.Software                       0.103
		Culture.Media.Television                     0.629
		Culture.Media.Video games                    0.885
		Culture.Performing arts                      0.531
		Culture.Philosophy and religion              0.451
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.693
		Culture.Visual arts.Comics and Anime         0.563
		Culture.Visual arts.Fashion                  0.35
		Culture.Visual arts.Visual arts*             0.623
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.662
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.237
		Geography.Regions.Africa.Northern Africa     0.296
		Geography.Regions.Africa.Southern Africa     0.496
		Geography.Regions.Africa.Western Africa      0.381
		Geography.Regions.Americas.Central America   0.347
		Geography.Regions.Americas.North America     0.691
		Geography.Regions.Americas.South America     0.476
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.369
		Geography.Regions.Asia.East Asia             0.607
		Geography.Regions.Asia.North Asia            0.206
		Geography.Regions.Asia.South Asia            0.847
		Geography.Regions.Asia.Southeast Asia        0.602
		Geography.Regions.Asia.West Asia             0.753
		Geography.Regions.Europe.Eastern Europe      0.616
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.571
		Geography.Regions.Europe.Southern Europe     0.517
		Geography.Regions.Europe.Western Europe      0.587
		Geography.Regions.Oceania                    0.806
		History and Society.Business and economics   0.302
		History and Society.Education                0.411
		History and Society.History                  0.25
		History and Society.Military and warfare     0.646
		History and Society.Politics and government  0.574
		History and Society.Society                  0.229
		History and Society.Transportation           0.83
		STEM.Biology                                 0.889
		STEM.Chemistry                               0.383
		STEM.Computing                               0.203
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.598
		STEM.Libraries & Information                 0.269
		STEM.Mathematics                             0.218
		STEM.Medicine & Health                       0.564
		STEM.Physics                                 0.195
		STEM.STEM*                                   0.843
		STEM.Space                                   0.9
		STEM.Technology                              0.236
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'Culture.Literature': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}}

