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
	counts (n=60764):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14139  -->  12651  1488   789  45836
			'Culture.Biography.Women'                       5153  -->   4127  1026   774  54837
			'Culture.Food and drink'                        1399  -->   1015   384   122  59243
			'Culture.Internet culture'                      3531  -->   2917   614   233  57000
			'Culture.Linguistics'                           1509  -->   1165   344    69  59186
			'Culture.Literature'                            5659  -->   4444  1215   505  54600
			'Culture.Media.Books'                           1467  -->   1089   378   111  59186
			'Culture.Media.Entertainment'                   1984  -->   1041   943   194  58586
			'Culture.Media.Films'                           2612  -->   2073   539   173  57979
			'Culture.Media.Media*'                         13270  -->  11633  1637  1282  46212
			'Culture.Media.Music'                           2908  -->   2509   399   163  57693
			'Culture.Media.Radio'                            285  -->    178   107    32  60447
			'Culture.Media.Software'                        2291  -->   1910   381   288  58185
			'Culture.Media.Television'                      1983  -->   1438   545   133  58648
			'Culture.Media.Video games'                     2139  -->   1969   170    54  58571
			'Culture.Performing arts'                       1374  -->    960   414   105  59285
			'Culture.Philosophy and religion'               3040  -->   1731  1309   295  57429
			'Culture.Sports'                                3871  -->   3411   460   104  56789
			'Culture.Visual arts.Architecture'              1854  -->   1334   520   167  58743
			'Culture.Visual arts.Comics and Anime'          2239  -->   2029   210    78  58447
			'Culture.Visual arts.Fashion'                   1501  -->   1213   288   105  59158
			'Culture.Visual arts.Visual arts*'              6119  -->   4741  1378   400  54245
			'Geography.Geographical'                        3991  -->   2584  1407   552  56221
			'Geography.Regions.Africa.Africa*'              5744  -->   4467  1277   485  54535
			'Geography.Regions.Africa.Central Africa'       1214  -->    811   403   123  59427
			'Geography.Regions.Africa.Eastern Africa'        451  -->    216   235    40  60273
			'Geography.Regions.Africa.Northern Africa'      1474  -->   1036   438    95  59195
			'Geography.Regions.Africa.Southern Africa'      1178  -->    798   380    78  59508
			'Geography.Regions.Africa.Western Africa'        672  -->    537   135    41  60051
			'Geography.Regions.Americas.Central America'    1588  -->    992   596   116  59060
			'Geography.Regions.Americas.North America'      5438  -->   3677  1761   651  54675
			'Geography.Regions.Americas.South America'      2210  -->   1706   504   183  58371
			'Geography.Regions.Asia.Asia*'                 13867  -->  11650  2217  1216  45681
			'Geography.Regions.Asia.Central Asia'           1211  -->    914   297    84  59469
			'Geography.Regions.Asia.East Asia'              5571  -->   4489  1082   445  54748
			'Geography.Regions.Asia.North Asia'             1693  -->   1283   410   235  58836
			'Geography.Regions.Asia.South Asia'             2038  -->   1624   414   108  58618
			'Geography.Regions.Asia.Southeast Asia'         2632  -->   1945   687   190  57942
			'Geography.Regions.Asia.West Asia'              2178  -->   1753   425   105  58481
			'Geography.Regions.Europe.Eastern Europe'       3590  -->   2868   722   277  56897
			'Geography.Regions.Europe.Europe*'             12682  -->  10215  2467  1220  46862
			'Geography.Regions.Europe.Northern Europe'      2896  -->   1842  1054   227  57641
			'Geography.Regions.Europe.Southern Europe'      2854  -->   2126   728   203  57707
			'Geography.Regions.Europe.Western Europe'       4043  -->   3153   890   237  56484
			'Geography.Regions.Oceania'                     2238  -->   1660   578   126  58400
			'History and Society.Business and economics'    3404  -->   2099  1305   350  57010
			'History and Society.Education'                 1589  -->    926   663   132  59043
			'History and Society.History'                   4595  -->   2468  2127   569  55600
			'History and Society.Military and warfare'      5048  -->   3942  1106   446  55270
			'History and Society.Politics and government'   4595  -->   2624  1971   485  55684
			'History and Society.Society'                   6148  -->   2979  3169   513  54103
			'History and Society.Transportation'            3573  -->   3290   283    82  57109
			'STEM.Biology'                                  7137  -->   6573   564   165  53462
			'STEM.Chemistry'                                1506  -->   1175   331   170  59088
			'STEM.Computing'                                2452  -->   2053   399   305  58007
			'STEM.Earth and environment'                    1649  -->   1118   531   123  58992
			'STEM.Engineering'                              3027  -->   2529   498   129  57608
			'STEM.Libraries & Information'                   489  -->    359   130    32  60243
			'STEM.Mathematics'                               942  -->    782   160    56  59766
			'STEM.Medicine & Health'                        1774  -->   1261   513   144  58846
			'STEM.Physics'                                  1374  -->   1025   349   139  59251
			'STEM.STEM*'                                   20595  -->  18875  1720   892  39277
			'STEM.Space'                                    1637  -->   1485   152    39  59088
			'STEM.Technology'                               4233  -->   3133  1100   585  55946
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.218         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.05          0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.031         0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.095         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.228         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
		Geography.Regions.Asia.North Asia               0.028         0.001
		Geography.Regions.Asia.South Asia               0.034         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.059         0.013
		Geography.Regions.Europe.Europe*                0.209         0.076
		Geography.Regions.Europe.Northern Europe        0.048         0.031
		Geography.Regions.Europe.Southern Europe        0.047         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.026         0.007
		History and Society.History                     0.076         0.011
		History and Society.Military and warfare        0.083         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.117         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.339         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.054
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.063
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.017
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.023
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.016
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.024
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.946
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.937
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.976
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.795, macro=0.75):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.801
		Culture.Food and drink                       0.726
		Culture.Internet culture                     0.826
		Culture.Linguistics                          0.772
		Culture.Literature                           0.785
		Culture.Media.Books                          0.742
		Culture.Media.Entertainment                  0.525
		Culture.Media.Films                          0.794
		Culture.Media.Media*                         0.877
		Culture.Media.Music                          0.863
		Culture.Media.Radio                          0.625
		Culture.Media.Software                       0.834
		Culture.Media.Television                     0.725
		Culture.Media.Video games                    0.921
		Culture.Performing arts                      0.699
		Culture.Philosophy and religion              0.569
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.72
		Culture.Visual arts.Comics and Anime         0.906
		Culture.Visual arts.Fashion                  0.808
		Culture.Visual arts.Visual arts*             0.775
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.778
		Geography.Regions.Africa.Central Africa      0.668
		Geography.Regions.Africa.Eastern Africa      0.479
		Geography.Regions.Africa.Northern Africa     0.703
		Geography.Regions.Africa.Southern Africa     0.677
		Geography.Regions.Africa.Western Africa      0.799
		Geography.Regions.Americas.Central America   0.625
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.772
		Geography.Regions.Asia.Asia*                 0.84
		Geography.Regions.Asia.Central Asia          0.755
		Geography.Regions.Asia.East Asia             0.806
		Geography.Regions.Asia.North Asia            0.758
		Geography.Regions.Asia.South Asia            0.797
		Geography.Regions.Asia.Southeast Asia        0.739
		Geography.Regions.Asia.West Asia             0.805
		Geography.Regions.Europe.Eastern Europe      0.799
		Geography.Regions.Europe.Europe*             0.805
		Geography.Regions.Europe.Northern Europe     0.636
		Geography.Regions.Europe.Southern Europe     0.745
		Geography.Regions.Europe.Western Europe      0.78
		Geography.Regions.Oceania                    0.742
		History and Society.Business and economics   0.617
		History and Society.Education                0.583
		History and Society.History                  0.537
		History and Society.Military and warfare     0.781
		History and Society.Politics and government  0.571
		History and Society.Society                  0.485
		History and Society.Transportation           0.921
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.78
		STEM.Computing                               0.837
		STEM.Earth and environment                   0.678
		STEM.Engineering                             0.835
		STEM.Libraries & Information                 0.734
		STEM.Mathematics                             0.83
		STEM.Medicine & Health                       0.711
		STEM.Physics                                 0.746
		STEM.STEM*                                   0.916
		STEM.Space                                   0.907
		STEM.Technology                              0.74
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.988
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
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
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.737, macro=0.578):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.881
		Culture.Biography.Women                      0.459
		Culture.Food and drink                       0.466
		Culture.Internet culture                     0.416
		Culture.Linguistics                          0.83
		Culture.Literature                           0.574
		Culture.Media.Books                          0.616
		Culture.Media.Entertainment                  0.364
		Culture.Media.Films                          0.739
		Culture.Media.Media*                         0.669
		Culture.Media.Music                          0.882
		Culture.Media.Radio                          0.718
		Culture.Media.Software                       0.184
		Culture.Media.Television                     0.74
		Culture.Media.Video games                    0.723
		Culture.Performing arts                      0.534
		Culture.Philosophy and religion              0.545
		Culture.Sports                               0.974
		Culture.Visual arts.Architecture             0.73
		Culture.Visual arts.Comics and Anime         0.599
		Culture.Visual arts.Fashion                  0.27
		Culture.Visual arts.Visual arts*             0.664
		Geography.Geographical                       0.617
		Geography.Regions.Africa.Africa*             0.409
		Geography.Regions.Africa.Central Africa      0.17
		Geography.Regions.Africa.Eastern Africa      0.247
		Geography.Regions.Africa.Northern Africa     0.35
		Geography.Regions.Africa.Southern Africa     0.378
		Geography.Regions.Africa.Western Africa      0.445
		Geography.Regions.Americas.Central America   0.513
		Geography.Regions.Americas.North America     0.798
		Geography.Regions.Americas.South America     0.611
		Geography.Regions.Asia.Asia*                 0.607
		Geography.Regions.Asia.Central Asia          0.317
		Geography.Regions.Asia.East Asia             0.536
		Geography.Regions.Asia.North Asia            0.15
		Geography.Regions.Asia.South Asia            0.87
		Geography.Regions.Asia.Southeast Asia        0.577
		Geography.Regions.Asia.West Asia             0.832
		Geography.Regions.Europe.Eastern Europe      0.682
		Geography.Regions.Europe.Europe*             0.724
		Geography.Regions.Europe.Northern Europe     0.836
		Geography.Regions.Europe.Southern Europe     0.737
		Geography.Regions.Europe.Western Europe      0.785
		Geography.Regions.Oceania                    0.841
		History and Society.Business and economics   0.507
		History and Society.Education                0.659
		History and Society.History                  0.367
		History and Society.Military and warfare     0.582
		History and Society.Politics and government  0.657
		History and Society.Society                  0.397
		History and Society.Transportation           0.908
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.298
		STEM.Computing                               0.302
		STEM.Earth and environment                   0.598
		STEM.Engineering                             0.663
		STEM.Libraries & Information                 0.462
		STEM.Mathematics                             0.27
		STEM.Medicine & Health                       0.652
		STEM.Physics                                 0.213
		STEM.STEM*                                   0.754
		STEM.Space                                   0.893
		STEM.Technology                              0.269
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
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
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
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
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.757, macro=0.631):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.888
		Culture.Biography.Women                      0.584
		Culture.Food and drink                       0.567
		Culture.Internet culture                     0.553
		Culture.Linguistics                          0.8
		Culture.Literature                           0.663
		Culture.Media.Books                          0.673
		Culture.Media.Entertainment                  0.43
		Culture.Media.Films                          0.765
		Culture.Media.Media*                         0.759
		Culture.Media.Music                          0.872
		Culture.Media.Radio                          0.668
		Culture.Media.Software                       0.301
		Culture.Media.Television                     0.733
		Culture.Media.Video games                    0.81
		Culture.Performing arts                      0.605
		Culture.Philosophy and religion              0.557
		Culture.Sports                               0.925
		Culture.Visual arts.Architecture             0.725
		Culture.Visual arts.Comics and Anime         0.722
		Culture.Visual arts.Fashion                  0.404
		Culture.Visual arts.Visual arts*             0.715
		Geography.Geographical                       0.632
		Geography.Regions.Africa.Africa*             0.536
		Geography.Regions.Africa.Central Africa      0.271
		Geography.Regions.Africa.Eastern Africa      0.326
		Geography.Regions.Africa.Northern Africa     0.467
		Geography.Regions.Africa.Southern Africa     0.486
		Geography.Regions.Africa.Western Africa      0.571
		Geography.Regions.Americas.Central America   0.564
		Geography.Regions.Americas.North America     0.732
		Geography.Regions.Americas.South America     0.682
		Geography.Regions.Asia.Asia*                 0.705
		Geography.Regions.Asia.Central Asia          0.446
		Geography.Regions.Asia.East Asia             0.644
		Geography.Regions.Asia.North Asia            0.25
		Geography.Regions.Asia.South Asia            0.832
		Geography.Regions.Asia.Southeast Asia        0.648
		Geography.Regions.Asia.West Asia             0.818
		Geography.Regions.Europe.Eastern Europe      0.736
		Geography.Regions.Europe.Europe*             0.762
		Geography.Regions.Europe.Northern Europe     0.723
		Geography.Regions.Europe.Southern Europe     0.741
		Geography.Regions.Europe.Western Europe      0.782
		Geography.Regions.Oceania                    0.788
		History and Society.Business and economics   0.557
		History and Society.Education                0.619
		History and Society.History                  0.436
		History and Society.Military and warfare     0.667
		History and Society.Politics and government  0.611
		History and Society.Society                  0.437
		History and Society.Transportation           0.914
		STEM.Biology                                 0.917
		STEM.Chemistry                               0.431
		STEM.Computing                               0.443
		STEM.Earth and environment                   0.635
		STEM.Engineering                             0.739
		STEM.Libraries & Information                 0.567
		STEM.Mathematics                             0.407
		STEM.Medicine & Health                       0.68
		STEM.Physics                                 0.332
		STEM.STEM*                                   0.827
		STEM.Space                                   0.9
		STEM.Technology                              0.395
		-------------------------------------------  -----
	!f1 (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.979
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.986
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.981, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.985
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.98
		History and Society.Society                  0.984
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
	fpr (micro=0.012, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.012
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.026
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.025
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
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
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.978
		Culture.Literature                           0.98
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.97
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.946
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.98
		Culture.Philosophy and religion              0.962
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.981
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.983
		Geography.Regions.Africa.Eastern Africa      0.966
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.982
		Geography.Regions.Americas.Central America   0.975
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.985
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.979
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.98
		History and Society.Business and economics   0.971
		History and Society.Education                0.973
		History and Society.History                  0.957
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.956
		History and Society.Society                  0.94
		History and Society.Transportation           0.989
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.987
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.985
		STEM.Libraries & Information                 0.972
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.981
		STEM.Space                                   0.994
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.808, macro=0.652):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.57
		Culture.Food and drink                       0.594
		Culture.Internet culture                     0.736
		Culture.Linguistics                          0.821
		Culture.Literature                           0.727
		Culture.Media.Books                          0.708
		Culture.Media.Entertainment                  0.415
		Culture.Media.Films                          0.812
		Culture.Media.Media*                         0.85
		Culture.Media.Music                          0.913
		Culture.Media.Radio                          0.506
		Culture.Media.Software                       0.359
		Culture.Media.Television                     0.737
		Culture.Media.Video games                    0.913
		Culture.Performing arts                      0.594
		Culture.Philosophy and religion              0.561
		Culture.Sports                               0.959
		Culture.Visual arts.Architecture             0.717
		Culture.Visual arts.Comics and Anime         0.805
		Culture.Visual arts.Fashion                  0.346
		Culture.Visual arts.Visual arts*             0.764
		Geography.Geographical                       0.679
		Geography.Regions.Africa.Africa*             0.611
		Geography.Regions.Africa.Central Africa      0.243
		Geography.Regions.Africa.Eastern Africa      0.139
		Geography.Regions.Africa.Northern Africa     0.37
		Geography.Regions.Africa.Southern Africa     0.354
		Geography.Regions.Africa.Western Africa      0.49
		Geography.Regions.Americas.Central America   0.549
		Geography.Regions.Americas.North America     0.807
		Geography.Regions.Americas.South America     0.64
		Geography.Regions.Asia.Asia*                 0.79
		Geography.Regions.Asia.Central Asia          0.405
		Geography.Regions.Asia.East Asia             0.668
		Geography.Regions.Asia.North Asia            0.23
		Geography.Regions.Asia.South Asia            0.869
		Geography.Regions.Asia.Southeast Asia        0.688
		Geography.Regions.Asia.West Asia             0.839
		Geography.Regions.Europe.Eastern Europe      0.815
		Geography.Regions.Europe.Europe*             0.832
		Geography.Regions.Europe.Northern Europe     0.782
		Geography.Regions.Europe.Southern Europe     0.801
		Geography.Regions.Europe.Western Europe      0.817
		Geography.Regions.Oceania                    0.826
		History and Society.Business and economics   0.56
		History and Society.Education                0.613
		History and Society.History                  0.443
		History and Society.Military and warfare     0.759
		History and Society.Politics and government  0.647
		History and Society.Society                  0.408
		History and Society.Transportation           0.943
		STEM.Biology                                 0.959
		STEM.Chemistry                               0.48
		STEM.Computing                               0.475
		STEM.Earth and environment                   0.623
		STEM.Engineering                             0.847
		STEM.Libraries & Information                 0.53
		STEM.Mathematics                             0.51
		STEM.Medicine & Health                       0.718
		STEM.Physics                                 0.322
		STEM.STEM*                                   0.908
		STEM.Space                                   0.952
		STEM.Technology                              0.446
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

