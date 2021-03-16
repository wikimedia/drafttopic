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
	counts (n=58736):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16082  -->  14093  1989  1152  41502
			'Culture.Biography.Women'                       4134  -->   3276   858   325  54277
			'Culture.Food and drink'                        1541  -->    987   554   131  57064
			'Culture.Internet culture'                      3075  -->   2328   747   265  55396
			'Culture.Linguistics'                           1548  -->   1000   548    88  57100
			'Culture.Literature'                            4853  -->   3243  1610   496  53387
			'Culture.Media.Books'                           1658  -->   1199   459   174  56904
			'Culture.Media.Entertainment'                   2214  -->    889  1325   261  56261
			'Culture.Media.Films'                           2464  -->   1917   547   146  56126
			'Culture.Media.Media*'                         14000  -->  11817  2183  1456  43280
			'Culture.Media.Music'                           3257  -->   2613   644   287  55192
			'Culture.Media.Radio'                            417  -->    193   224    53  58266
			'Culture.Media.Software'                        2301  -->   1689   612   385  56050
			'Culture.Media.Television'                      2495  -->   1929   566   146  56095
			'Culture.Media.Video games'                     1832  -->   1601   231    70  56834
			'Culture.Performing arts'                       1480  -->    856   624   136  57120
			'Culture.Philosophy and religion'               4308  -->   2177  2131   456  53972
			'Culture.Sports'                                5661  -->   4949   712   210  52865
			'Culture.Visual arts.Architecture'              2272  -->   1503   769   217  56247
			'Culture.Visual arts.Comics and Anime'          1653  -->   1352   301    46  57037
			'Culture.Visual arts.Fashion'                   1010  -->    580   430    77  57649
			'Culture.Visual arts.Visual arts*'              5793  -->   3945  1848   459  52484
			'Geography.Geographical'                        4552  -->   3085  1467   686  53498
			'Geography.Regions.Africa.Africa*'              4005  -->   2406  1599   328  54403
			'Geography.Regions.Africa.Central Africa'        719  -->    328   391    75  57942
			'Geography.Regions.Africa.Eastern Africa'        470  -->    236   234    39  58227
			'Geography.Regions.Africa.Northern Africa'      1517  -->    841   676   135  57084
			'Geography.Regions.Africa.Southern Africa'       660  -->    269   391    61  58015
			'Geography.Regions.Africa.Western Africa'        182  -->     86    96    26  58528
			'Geography.Regions.Americas.Central America'    1324  -->    582   742    84  57328
			'Geography.Regions.Americas.North America'      5900  -->   3234  2666   962  51874
			'Geography.Regions.Americas.South America'      1453  -->    912   541    93  57190
			'Geography.Regions.Asia.Asia*'                 10657  -->   8015  2642   921  47158
			'Geography.Regions.Asia.Central Asia'           1288  -->    755   533   117  57331
			'Geography.Regions.Asia.East Asia'              2908  -->   2108   800   213  55615
			'Geography.Regions.Asia.North Asia'             1912  -->   1197   715   307  56517
			'Geography.Regions.Asia.South Asia'             1779  -->   1201   578    78  56879
			'Geography.Regions.Asia.Southeast Asia'         1582  -->    845   737   105  57049
			'Geography.Regions.Asia.West Asia'              2824  -->   2109   715   153  55759
			'Geography.Regions.Europe.Eastern Europe'       5143  -->   3460  1683   688  52905
			'Geography.Regions.Europe.Europe*'             16514  -->  12280  4234  2614  39608
			'Geography.Regions.Europe.Northern Europe'      3933  -->   2260  1673   456  54347
			'Geography.Regions.Europe.Southern Europe'      3385  -->   2066  1319   343  55008
			'Geography.Regions.Europe.Western Europe'       5102  -->   3294  1808   676  52958
			'Geography.Regions.Oceania'                     1711  -->   1050   661   103  56922
			'History and Society.Business and economics'    3464  -->   1798  1666   363  54909
			'History and Society.Education'                 1793  -->    768  1025   148  56795
			'History and Society.History'                   5442  -->   2911  2531   720  52574
			'History and Society.Military and warfare'      5679  -->   3804  1875   595  52462
			'History and Society.Politics and government'   4572  -->   2087  2485   492  53672
			'History and Society.Society'                   6690  -->   2753  3937   627  51419
			'History and Society.Transportation'            4217  -->   3680   537   191  54328
			'STEM.Biology'                                  3716  -->   2829   887   212  54808
			'STEM.Chemistry'                                1567  -->   1151   416   164  57005
			'STEM.Computing'                                2762  -->   2143   619   400  55574
			'STEM.Earth and environment'                    2186  -->   1302   884   150  56400
			'STEM.Engineering'                              2908  -->   2065   843   222  55606
			'STEM.Libraries & Information'                   706  -->    447   259    52  57978
			'STEM.Mathematics'                              1186  -->    854   332    80  57470
			'STEM.Medicine & Health'                        2029  -->   1174   855   202  56505
			'STEM.Physics'                                  1433  -->    837   596   180  57123
			'STEM.STEM*'                                   18575  -->  16117  2458  1298  38863
			'STEM.Space'                                    2040  -->   1791   249    70  56626
			'STEM.Technology'                               5041  -->   3458  1583   677  53018
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.274         0.123
		Culture.Biography.Women                         0.07          0.015
		Culture.Food and drink                          0.026         0.002
		Culture.Internet culture                        0.052         0.003
		Culture.Linguistics                             0.026         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.055         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.096         0.071
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.017         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.181         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.05          0.011
		Geography.Regions.Asia.North Asia               0.033         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.088         0.013
		Geography.Regions.Europe.Europe*                0.281         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.058         0.013
		Geography.Regions.Europe.Western Europe         0.087         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.097         0.014
		History and Society.Politics and government     0.078         0.028
		History and Society.Society                     0.114         0.013
		History and Society.Transportation              0.072         0.015
		STEM.Biology                                    0.063         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.316         0.069
		STEM.Space                                      0.035         0.006
		STEM.Technology                                 0.086         0.005
	match_rate (micro=0.055, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.028
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.052
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.003
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.114
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.011
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.022
		History and Society.Society                  0.017
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.09
		STEM.Space                                   0.007
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.945, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.948
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.886
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.989
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.978
		History and Society.Society                  0.983
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.91
		STEM.Space                                   0.993
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.727, macro=0.651):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.792
		Culture.Food and drink                       0.64
		Culture.Internet culture                     0.757
		Culture.Linguistics                          0.646
		Culture.Literature                           0.668
		Culture.Media.Books                          0.723
		Culture.Media.Entertainment                  0.402
		Culture.Media.Films                          0.778
		Culture.Media.Media*                         0.844
		Culture.Media.Music                          0.802
		Culture.Media.Radio                          0.463
		Culture.Media.Software                       0.734
		Culture.Media.Television                     0.773
		Culture.Media.Video games                    0.874
		Culture.Performing arts                      0.578
		Culture.Philosophy and religion              0.505
		Culture.Sports                               0.874
		Culture.Visual arts.Architecture             0.662
		Culture.Visual arts.Comics and Anime         0.818
		Culture.Visual arts.Fashion                  0.574
		Culture.Visual arts.Visual arts*             0.681
		Geography.Geographical                       0.678
		Geography.Regions.Africa.Africa*             0.601
		Geography.Regions.Africa.Central Africa      0.456
		Geography.Regions.Africa.Eastern Africa      0.502
		Geography.Regions.Africa.Northern Africa     0.554
		Geography.Regions.Africa.Southern Africa     0.408
		Geography.Regions.Africa.Western Africa      0.473
		Geography.Regions.Americas.Central America   0.44
		Geography.Regions.Americas.North America     0.548
		Geography.Regions.Americas.South America     0.628
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.586
		Geography.Regions.Asia.East Asia             0.725
		Geography.Regions.Asia.North Asia            0.626
		Geography.Regions.Asia.South Asia            0.675
		Geography.Regions.Asia.Southeast Asia        0.534
		Geography.Regions.Asia.West Asia             0.747
		Geography.Regions.Europe.Eastern Europe      0.673
		Geography.Regions.Europe.Europe*             0.744
		Geography.Regions.Europe.Northern Europe     0.575
		Geography.Regions.Europe.Southern Europe     0.61
		Geography.Regions.Europe.Western Europe      0.646
		Geography.Regions.Oceania                    0.614
		History and Society.Business and economics   0.519
		History and Society.Education                0.428
		History and Society.History                  0.535
		History and Society.Military and warfare     0.67
		History and Society.Politics and government  0.456
		History and Society.Society                  0.412
		History and Society.Transportation           0.873
		STEM.Biology                                 0.761
		STEM.Chemistry                               0.735
		STEM.Computing                               0.776
		STEM.Earth and environment                   0.596
		STEM.Engineering                             0.71
		STEM.Libraries & Information                 0.633
		STEM.Mathematics                             0.72
		STEM.Medicine & Health                       0.579
		STEM.Physics                                 0.584
		STEM.STEM*                                   0.868
		STEM.Space                                   0.878
		STEM.Technology                              0.686
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.991
		History and Society.Society                  0.988
		History and Society.Transportation           0.996
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.66, macro=0.511):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.82
		Culture.Biography.Women                      0.663
		Culture.Food and drink                       0.408
		Culture.Internet culture                     0.358
		Culture.Linguistics                          0.756
		Culture.Literature                           0.533
		Culture.Media.Books                          0.489
		Culture.Media.Entertainment                  0.238
		Culture.Media.Films                          0.761
		Culture.Media.Media*                         0.617
		Culture.Media.Music                          0.792
		Culture.Media.Radio                          0.524
		Culture.Media.Software                       0.125
		Culture.Media.Television                     0.726
		Culture.Media.Video games                    0.65
		Culture.Performing arts                      0.413
		Culture.Philosophy and religion              0.394
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.648
		Culture.Visual arts.Comics and Anime         0.691
		Culture.Visual arts.Fashion                  0.258
		Culture.Visual arts.Visual arts*             0.594
		Geography.Geographical                       0.564
		Geography.Regions.Africa.Africa*             0.441
		Geography.Regions.Africa.Central Africa      0.182
		Geography.Regions.Africa.Eastern Africa      0.254
		Geography.Regions.Africa.Northern Africa     0.224
		Geography.Regions.Africa.Southern Africa     0.313
		Geography.Regions.Africa.Western Africa      0.421
		Geography.Regions.Americas.Central America   0.499
		Geography.Regions.Americas.North America     0.674
		Geography.Regions.Americas.South America     0.71
		Geography.Regions.Asia.Asia*                 0.652
		Geography.Regions.Asia.Central Asia          0.2
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.097
		Geography.Regions.Asia.South Asia            0.884
		Geography.Regions.Asia.Southeast Asia        0.637
		Geography.Regions.Asia.West Asia             0.751
		Geography.Regions.Europe.Eastern Europe      0.405
		Geography.Regions.Europe.Europe*             0.498
		Geography.Regions.Europe.Northern Europe     0.685
		Geography.Regions.Europe.Southern Europe     0.565
		Geography.Regions.Europe.Western Europe      0.5
		Geography.Regions.Oceania                    0.839
		History and Society.Business and economics   0.446
		History and Society.Education                0.55
		History and Society.History                  0.303
		History and Society.Military and warfare     0.46
		History and Society.Politics and government  0.593
		History and Society.Society                  0.304
		History and Society.Transportation           0.792
		STEM.Biology                                 0.873
		STEM.Chemistry                               0.286
		STEM.Computing                               0.226
		STEM.Earth and environment                   0.506
		STEM.Engineering                             0.484
		STEM.Libraries & Information                 0.305
		STEM.Mathematics                             0.178
		STEM.Medicine & Health                       0.511
		STEM.Physics                                 0.136
		STEM.STEM*                                   0.666
		STEM.Space                                   0.811
		STEM.Technology                              0.219
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.683, macro=0.551):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.847
		Culture.Biography.Women                      0.722
		Culture.Food and drink                       0.499
		Culture.Internet culture                     0.486
		Culture.Linguistics                          0.697
		Culture.Literature                           0.593
		Culture.Media.Books                          0.584
		Culture.Media.Entertainment                  0.299
		Culture.Media.Films                          0.769
		Culture.Media.Media*                         0.713
		Culture.Media.Music                          0.797
		Culture.Media.Radio                          0.491
		Culture.Media.Software                       0.214
		Culture.Media.Television                     0.749
		Culture.Media.Video games                    0.746
		Culture.Performing arts                      0.482
		Culture.Philosophy and religion              0.443
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.655
		Culture.Visual arts.Comics and Anime         0.749
		Culture.Visual arts.Fashion                  0.356
		Culture.Visual arts.Visual arts*             0.635
		Geography.Geographical                       0.616
		Geography.Regions.Africa.Africa*             0.508
		Geography.Regions.Africa.Central Africa      0.261
		Geography.Regions.Africa.Eastern Africa      0.338
		Geography.Regions.Africa.Northern Africa     0.319
		Geography.Regions.Africa.Southern Africa     0.354
		Geography.Regions.Africa.Western Africa      0.445
		Geography.Regions.Americas.Central America   0.467
		Geography.Regions.Americas.North America     0.605
		Geography.Regions.Americas.South America     0.667
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.298
		Geography.Regions.Asia.East Asia             0.705
		Geography.Regions.Asia.North Asia            0.168
		Geography.Regions.Asia.South Asia            0.765
		Geography.Regions.Asia.Southeast Asia        0.581
		Geography.Regions.Asia.West Asia             0.749
		Geography.Regions.Europe.Eastern Europe      0.506
		Geography.Regions.Europe.Europe*             0.596
		Geography.Regions.Europe.Northern Europe     0.625
		Geography.Regions.Europe.Southern Europe     0.587
		Geography.Regions.Europe.Western Europe      0.564
		Geography.Regions.Oceania                    0.709
		History and Society.Business and economics   0.48
		History and Society.Education                0.482
		History and Society.History                  0.386
		History and Society.Military and warfare     0.545
		History and Society.Politics and government  0.516
		History and Society.Society                  0.35
		History and Society.Transportation           0.831
		STEM.Biology                                 0.813
		STEM.Chemistry                               0.411
		STEM.Computing                               0.351
		STEM.Earth and environment                   0.547
		STEM.Engineering                             0.576
		STEM.Libraries & Information                 0.412
		STEM.Mathematics                             0.285
		STEM.Medicine & Health                       0.543
		STEM.Physics                                 0.221
		STEM.STEM*                                   0.754
		STEM.Space                                   0.843
		STEM.Technology                              0.332
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.988
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
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
		Culture.Biography.Biography*                 0.961
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.923
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.976
		History and Society.Society                  0.981
		History and Society.Transportation           0.995
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.027
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.062
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.013
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.014
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.009
		History and Society.Society                  0.012
		History and Society.Transportation           0.004
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.964):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.974
		Culture.Internet culture                     0.979
		Culture.Linguistics                          0.965
		Culture.Literature                           0.966
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.956
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.936
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.937
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.972
		Culture.Visual arts.Visual arts*             0.962
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.959
		Geography.Regions.Africa.Central Africa      0.964
		Geography.Regions.Africa.Eastern Africa      0.959
		Geography.Regions.Africa.Northern Africa     0.967
		Geography.Regions.Africa.Southern Africa     0.945
		Geography.Regions.Africa.Western Africa      0.888
		Geography.Regions.Americas.Central America   0.952
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.965
		Geography.Regions.Asia.Asia*                 0.962
		Geography.Regions.Asia.Central Asia          0.968
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.977
		Geography.Regions.Asia.South Asia            0.968
		Geography.Regions.Asia.Southeast Asia        0.961
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.965
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.955
		Geography.Regions.Europe.Southern Europe     0.962
		Geography.Regions.Europe.Western Europe      0.961
		Geography.Regions.Oceania                    0.969
		History and Society.Business and economics   0.952
		History and Society.Education                0.95
		History and Society.History                  0.943
		History and Society.Military and warfare     0.965
		History and Society.Politics and government  0.932
		History and Society.Society                  0.9
		History and Society.Transportation           0.985
		STEM.Biology                                 0.975
		STEM.Chemistry                               0.982
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.973
		STEM.Libraries & Information                 0.963
		STEM.Mathematics                             0.976
		STEM.Medicine & Health                       0.969
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.971
		STEM.Space                                   0.988
		STEM.Technology                              0.969
		-------------------------------------------  -----
	pr_auc (micro=0.724, macro=0.545):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.915
		Culture.Biography.Women                      0.702
		Culture.Food and drink                       0.507
		Culture.Internet culture                     0.634
		Culture.Linguistics                          0.697
		Culture.Literature                           0.624
		Culture.Media.Books                          0.597
		Culture.Media.Entertainment                  0.202
		Culture.Media.Films                          0.779
		Culture.Media.Media*                         0.824
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.278
		Culture.Media.Software                       0.226
		Culture.Media.Television                     0.823
		Culture.Media.Video games                    0.81
		Culture.Performing arts                      0.448
		Culture.Philosophy and religion              0.383
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.678
		Culture.Visual arts.Comics and Anime         0.773
		Culture.Visual arts.Fashion                  0.323
		Culture.Visual arts.Visual arts*             0.679
		Geography.Geographical                       0.625
		Geography.Regions.Africa.Africa*             0.476
		Geography.Regions.Africa.Central Africa      0.11
		Geography.Regions.Africa.Eastern Africa      0.121
		Geography.Regions.Africa.Northern Africa     0.288
		Geography.Regions.Africa.Southern Africa     0.188
		Geography.Regions.Africa.Western Africa      0.225
		Geography.Regions.Americas.Central America   0.39
		Geography.Regions.Americas.North America     0.656
		Geography.Regions.Americas.South America     0.669
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.199
		Geography.Regions.Asia.East Asia             0.731
		Geography.Regions.Asia.North Asia            0.133
		Geography.Regions.Asia.South Asia            0.796
		Geography.Regions.Asia.Southeast Asia        0.557
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.509
		Geography.Regions.Europe.Europe*             0.648
		Geography.Regions.Europe.Northern Europe     0.661
		Geography.Regions.Europe.Southern Europe     0.582
		Geography.Regions.Europe.Western Europe      0.55
		Geography.Regions.Oceania                    0.744
		History and Society.Business and economics   0.439
		History and Society.Education                0.445
		History and Society.History                  0.371
		History and Society.Military and warfare     0.605
		History and Society.Politics and government  0.533
		History and Society.Society                  0.305
		History and Society.Transportation           0.885
		STEM.Biology                                 0.871
		STEM.Chemistry                               0.391
		STEM.Computing                               0.315
		STEM.Earth and environment                   0.512
		STEM.Engineering                             0.675
		STEM.Libraries & Information                 0.315
		STEM.Mathematics                             0.295
		STEM.Medicine & Health                       0.52
		STEM.Physics                                 0.181
		STEM.STEM*                                   0.871
		STEM.Space                                   0.882
		STEM.Technology                              0.415
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

