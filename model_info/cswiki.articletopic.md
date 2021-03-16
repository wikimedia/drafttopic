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
	counts (n=60197):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16411  -->  15078  1333   829  42957
			'Culture.Biography.Women'                       4309  -->   3614   695   291  55597
			'Culture.Food and drink'                        1598  -->   1153   445   121  58478
			'Culture.Internet culture'                      3175  -->   2581   594   212  56810
			'Culture.Linguistics'                           1610  -->   1171   439    95  58492
			'Culture.Literature'                            4968  -->   3572  1396   498  54731
			'Culture.Media.Books'                           1697  -->   1335   362   137  58363
			'Culture.Media.Entertainment'                   2268  -->   1025  1243   282  57647
			'Culture.Media.Films'                           2531  -->   2087   444   112  57554
			'Culture.Media.Media*'                         14349  -->  12461  1888  1334  44514
			'Culture.Media.Music'                           3307  -->   2791   516   241  56649
			'Culture.Media.Radio'                            425  -->    203   222    41  59731
			'Culture.Media.Software'                        2392  -->   1815   577   353  57452
			'Culture.Media.Television'                      2548  -->   2136   412   106  57543
			'Culture.Media.Video games'                     1896  -->   1725   171    44  58257
			'Culture.Performing arts'                       1520  -->    990   530   109  58568
			'Culture.Philosophy and religion'               4401  -->   2459  1942   464  55332
			'Culture.Sports'                                5891  -->   5270   621   189  54117
			'Culture.Visual arts.Architecture'              2309  -->   1631   678   217  57671
			'Culture.Visual arts.Comics and Anime'          1679  -->   1445   234    49  58469
			'Culture.Visual arts.Fashion'                   1059  -->    692   367    74  59064
			'Culture.Visual arts.Visual arts*'              5915  -->   4335  1580   428  53854
			'Geography.Geographical'                        4652  -->   3331  1321   723  54822
			'Geography.Regions.Africa.Africa*'              4090  -->   2581  1509   322  55785
			'Geography.Regions.Africa.Central Africa'        732  -->    327   405    67  59398
			'Geography.Regions.Africa.Eastern Africa'        474  -->    257   217    47  59676
			'Geography.Regions.Africa.Northern Africa'      1558  -->    909   649   132  58507
			'Geography.Regions.Africa.Southern Africa'       675  -->    303   372    71  59451
			'Geography.Regions.Africa.Western Africa'        187  -->     86   101    48  59962
			'Geography.Regions.Americas.Central America'    1354  -->    636   718    81  58762
			'Geography.Regions.Americas.North America'      6020  -->   3720  2300  1006  53171
			'Geography.Regions.Americas.South America'      1478  -->    991   487   102  58617
			'Geography.Regions.Asia.Asia*'                 10847  -->   8568  2279   874  48476
			'Geography.Regions.Asia.Central Asia'           1311  -->    822   489   104  58782
			'Geography.Regions.Asia.East Asia'              2966  -->   2244   722   191  57040
			'Geography.Regions.Asia.North Asia'             1944  -->   1280   664   312  57941
			'Geography.Regions.Asia.South Asia'             1814  -->   1311   503    75  58308
			'Geography.Regions.Asia.Southeast Asia'         1603  -->    939   664    83  58511
			'Geography.Regions.Asia.West Asia'              2874  -->   2201   673   173  57150
			'Geography.Regions.Europe.Eastern Europe'       5252  -->   3741  1511   642  54303
			'Geography.Regions.Europe.Europe*'             16883  -->  13072  3811  2513  40801
			'Geography.Regions.Europe.Northern Europe'      4019  -->   2456  1563   451  55727
			'Geography.Regions.Europe.Southern Europe'      3488  -->   2263  1225   359  56350
			'Geography.Regions.Europe.Western Europe'       5209  -->   3613  1596   667  54321
			'Geography.Regions.Oceania'                     1774  -->   1208   566    82  58341
			'History and Society.Business and economics'    3567  -->   2076  1491   365  56265
			'History and Society.Education'                 1821  -->    866   955   164  58212
			'History and Society.History'                   5592  -->   3301  2291   718  53887
			'History and Society.Military and warfare'      5797  -->   4111  1686   597  53803
			'History and Society.Politics and government'   4709  -->   2518  2191   511  54977
			'History and Society.Society'                   6861  -->   3103  3758   708  52628
			'History and Society.Transportation'            4282  -->   3872   410   184  55731
			'STEM.Biology'                                  3828  -->   3078   750   171  56198
			'STEM.Chemistry'                                1607  -->   1308   299   145  58445
			'STEM.Computing'                                2851  -->   2335   516   406  56940
			'STEM.Earth and environment'                    2224  -->   1454   770   155  57818
			'STEM.Engineering'                              2978  -->   2283   695   246  56973
			'STEM.Libraries & Information'                   717  -->    463   254    66  59414
			'STEM.Mathematics'                              1208  -->    924   284    70  58919
			'STEM.Medicine & Health'                        2098  -->   1384   714   211  57888
			'STEM.Physics'                                  1466  -->    955   511   153  58578
			'STEM.STEM*'                                   19061  -->  16843  2218  1100  40036
			'STEM.Space'                                    2057  -->   1879   178    46  58094
			'STEM.Technology'                               5209  -->   3770  1439   700  54288
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.273         0.123
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.027         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.055         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.098         0.071
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.18          0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.049         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.087         0.013
		Geography.Regions.Europe.Europe*                0.28          0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.058         0.013
		Geography.Regions.Europe.Western Europe         0.087         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.03          0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.096         0.014
		History and Society.Politics and government     0.078         0.028
		History and Society.Society                     0.114         0.013
		History and Society.Transportation              0.071         0.015
		STEM.Biology                                    0.064         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.317         0.069
		STEM.Space                                      0.034         0.006
		STEM.Technology                                 0.087         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.03
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.113
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.024
		History and Society.Society                  0.019
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.887
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.976
		History and Society.Society                  0.981
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.768, macro=0.696):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.919
		Culture.Biography.Women                      0.839
		Culture.Food and drink                       0.722
		Culture.Internet culture                     0.813
		Culture.Linguistics                          0.727
		Culture.Literature                           0.719
		Culture.Media.Books                          0.787
		Culture.Media.Entertainment                  0.452
		Culture.Media.Films                          0.825
		Culture.Media.Media*                         0.868
		Culture.Media.Music                          0.844
		Culture.Media.Radio                          0.478
		Culture.Media.Software                       0.759
		Culture.Media.Television                     0.838
		Culture.Media.Video games                    0.91
		Culture.Performing arts                      0.651
		Culture.Philosophy and religion              0.559
		Culture.Sports                               0.895
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.861
		Culture.Visual arts.Fashion                  0.653
		Culture.Visual arts.Visual arts*             0.733
		Geography.Geographical                       0.716
		Geography.Regions.Africa.Africa*             0.631
		Geography.Regions.Africa.Central Africa      0.447
		Geography.Regions.Africa.Eastern Africa      0.542
		Geography.Regions.Africa.Northern Africa     0.583
		Geography.Regions.Africa.Southern Africa     0.449
		Geography.Regions.Africa.Western Africa      0.46
		Geography.Regions.Americas.Central America   0.47
		Geography.Regions.Americas.North America     0.618
		Geography.Regions.Americas.South America     0.671
		Geography.Regions.Asia.Asia*                 0.79
		Geography.Regions.Asia.Central Asia          0.627
		Geography.Regions.Asia.East Asia             0.757
		Geography.Regions.Asia.North Asia            0.658
		Geography.Regions.Asia.South Asia            0.723
		Geography.Regions.Asia.Southeast Asia        0.586
		Geography.Regions.Asia.West Asia             0.766
		Geography.Regions.Europe.Eastern Europe      0.712
		Geography.Regions.Europe.Europe*             0.774
		Geography.Regions.Europe.Northern Europe     0.611
		Geography.Regions.Europe.Southern Europe     0.649
		Geography.Regions.Europe.Western Europe      0.694
		Geography.Regions.Oceania                    0.681
		History and Society.Business and economics   0.582
		History and Society.Education                0.476
		History and Society.History                  0.59
		History and Society.Military and warfare     0.709
		History and Society.Politics and government  0.535
		History and Society.Society                  0.452
		History and Society.Transportation           0.904
		STEM.Biology                                 0.804
		STEM.Chemistry                               0.814
		STEM.Computing                               0.819
		STEM.Earth and environment                   0.654
		STEM.Engineering                             0.767
		STEM.Libraries & Information                 0.646
		STEM.Mathematics                             0.765
		STEM.Medicine & Health                       0.66
		STEM.Physics                                 0.651
		STEM.STEM*                                   0.884
		STEM.Space                                   0.913
		STEM.Technology                              0.724
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.991
		History and Society.Society                  0.987
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.69, macro=0.538):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.704
		Culture.Food and drink                       0.463
		Culture.Internet culture                     0.434
		Culture.Linguistics                          0.768
		Culture.Literature                           0.557
		Culture.Media.Books                          0.576
		Culture.Media.Entertainment                  0.25
		Culture.Media.Films                          0.819
		Culture.Media.Media*                         0.65
		Culture.Media.Music                          0.83
		Culture.Media.Radio                          0.601
		Culture.Media.Software                       0.142
		Culture.Media.Television                     0.802
		Culture.Media.Video games                    0.759
		Culture.Performing arts                      0.504
		Culture.Philosophy and religion              0.42
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.693
		Culture.Visual arts.Fashion                  0.297
		Culture.Visual arts.Visual arts*             0.634
		Geography.Geographical                       0.57
		Geography.Regions.Africa.Africa*             0.464
		Geography.Regions.Africa.Central Africa      0.2
		Geography.Regions.Africa.Eastern Africa      0.239
		Geography.Regions.Africa.Northern Africa     0.242
		Geography.Regions.Africa.Southern Africa     0.307
		Geography.Regions.Africa.Western Africa      0.282
		Geography.Regions.Americas.Central America   0.53
		Geography.Regions.Americas.North America     0.696
		Geography.Regions.Americas.South America     0.71
		Geography.Regions.Asia.Asia*                 0.68
		Geography.Regions.Asia.Central Asia          0.235
		Geography.Regions.Asia.East Asia             0.723
		Geography.Regions.Asia.North Asia            0.102
		Geography.Regions.Asia.South Asia            0.897
		Geography.Regions.Asia.Southeast Asia        0.714
		Geography.Regions.Asia.West Asia             0.737
		Geography.Regions.Europe.Eastern Europe      0.442
		Geography.Regions.Europe.Europe*             0.524
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.575
		Geography.Regions.Europe.Western Europe      0.528
		Geography.Regions.Oceania                    0.882
		History and Society.Business and economics   0.479
		History and Society.Education                0.556
		History and Society.History                  0.33
		History and Society.Military and warfare     0.48
		History and Society.Politics and government  0.627
		History and Society.Society                  0.303
		History and Society.Transportation           0.808
		STEM.Biology                                 0.902
		STEM.Chemistry                               0.339
		STEM.Computing                               0.238
		STEM.Earth and environment                   0.527
		STEM.Engineering                             0.484
		STEM.Libraries & Information                 0.266
		STEM.Mathematics                             0.212
		STEM.Medicine & Health                       0.539
		STEM.Physics                                 0.175
		STEM.STEM*                                   0.71
		STEM.Space                                   0.875
		STEM.Technology                              0.227
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.998
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
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.987
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.719, macro=0.585):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.766
		Culture.Food and drink                       0.564
		Culture.Internet culture                     0.566
		Culture.Linguistics                          0.747
		Culture.Literature                           0.627
		Culture.Media.Books                          0.665
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.743
		Culture.Media.Music                          0.837
		Culture.Media.Radio                          0.532
		Culture.Media.Software                       0.239
		Culture.Media.Television                     0.82
		Culture.Media.Video games                    0.828
		Culture.Performing arts                      0.568
		Culture.Philosophy and religion              0.479
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.687
		Culture.Visual arts.Comics and Anime         0.768
		Culture.Visual arts.Fashion                  0.408
		Culture.Visual arts.Visual arts*             0.68
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.534
		Geography.Regions.Africa.Central Africa      0.277
		Geography.Regions.Africa.Eastern Africa      0.331
		Geography.Regions.Africa.Northern Africa     0.342
		Geography.Regions.Africa.Southern Africa     0.365
		Geography.Regions.Africa.Western Africa      0.35
		Geography.Regions.Americas.Central America   0.498
		Geography.Regions.Americas.North America     0.654
		Geography.Regions.Americas.South America     0.69
		Geography.Regions.Asia.Asia*                 0.731
		Geography.Regions.Asia.Central Asia          0.342
		Geography.Regions.Asia.East Asia             0.74
		Geography.Regions.Asia.North Asia            0.177
		Geography.Regions.Asia.South Asia            0.8
		Geography.Regions.Asia.Southeast Asia        0.644
		Geography.Regions.Asia.West Asia             0.751
		Geography.Regions.Europe.Eastern Europe      0.546
		Geography.Regions.Europe.Europe*             0.625
		Geography.Regions.Europe.Northern Europe     0.655
		Geography.Regions.Europe.Southern Europe     0.61
		Geography.Regions.Europe.Western Europe      0.599
		Geography.Regions.Oceania                    0.768
		History and Society.Business and economics   0.526
		History and Society.Education                0.513
		History and Society.History                  0.423
		History and Society.Military and warfare     0.572
		History and Society.Politics and government  0.577
		History and Society.Society                  0.363
		History and Society.Transportation           0.853
		STEM.Biology                                 0.85
		STEM.Chemistry                               0.479
		STEM.Computing                               0.369
		STEM.Earth and environment                   0.584
		STEM.Engineering                             0.593
		STEM.Libraries & Information                 0.376
		STEM.Mathematics                             0.332
		STEM.Medicine & Health                       0.593
		STEM.Physics                                 0.276
		STEM.STEM*                                   0.788
		STEM.Space                                   0.894
		STEM.Technology                              0.345
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.929
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.978
		History and Society.Society                  0.98
		History and Society.Transportation           0.995
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.019
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.058
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.009
		History and Society.Society                  0.013
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.971, macro=0.971):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.974
		Culture.Literature                           0.974
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.953
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.976
		Culture.Visual arts.Visual arts*             0.973
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.96
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.946
		Geography.Regions.Africa.Western Africa      0.895
		Geography.Regions.Americas.Central America   0.96
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.971
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.974
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.982
		Geography.Regions.Asia.South Asia            0.968
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.964
		History and Society.Education                0.962
		History and Society.History                  0.956
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.95
		History and Society.Society                  0.919
		History and Society.Transportation           0.988
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.987
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.965
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.975
		STEM.Space                                   0.992
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.765, macro=0.593):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.95
		Culture.Biography.Women                      0.789
		Culture.Food and drink                       0.584
		Culture.Internet culture                     0.705
		Culture.Linguistics                          0.761
		Culture.Literature                           0.689
		Culture.Media.Books                          0.681
		Culture.Media.Entertainment                  0.277
		Culture.Media.Films                          0.847
		Culture.Media.Media*                         0.852
		Culture.Media.Music                          0.859
		Culture.Media.Radio                          0.351
		Culture.Media.Software                       0.27
		Culture.Media.Television                     0.883
		Culture.Media.Video games                    0.905
		Culture.Performing arts                      0.503
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.703
		Culture.Visual arts.Comics and Anime         0.813
		Culture.Visual arts.Fashion                  0.335
		Culture.Visual arts.Visual arts*             0.74
		Geography.Geographical                       0.65
		Geography.Regions.Africa.Africa*             0.527
		Geography.Regions.Africa.Central Africa      0.168
		Geography.Regions.Africa.Eastern Africa      0.147
		Geography.Regions.Africa.Northern Africa     0.276
		Geography.Regions.Africa.Southern Africa     0.202
		Geography.Regions.Africa.Western Africa      0.153
		Geography.Regions.Americas.Central America   0.43
		Geography.Regions.Americas.North America     0.711
		Geography.Regions.Americas.South America     0.705
		Geography.Regions.Asia.Asia*                 0.808
		Geography.Regions.Asia.Central Asia          0.226
		Geography.Regions.Asia.East Asia             0.79
		Geography.Regions.Asia.North Asia            0.154
		Geography.Regions.Asia.South Asia            0.815
		Geography.Regions.Asia.Southeast Asia        0.623
		Geography.Regions.Asia.West Asia             0.798
		Geography.Regions.Europe.Eastern Europe      0.561
		Geography.Regions.Europe.Europe*             0.687
		Geography.Regions.Europe.Northern Europe     0.702
		Geography.Regions.Europe.Southern Europe     0.627
		Geography.Regions.Europe.Western Europe      0.614
		Geography.Regions.Oceania                    0.802
		History and Society.Business and economics   0.501
		History and Society.Education                0.492
		History and Society.History                  0.433
		History and Society.Military and warfare     0.648
		History and Society.Politics and government  0.601
		History and Society.Society                  0.319
		History and Society.Transportation           0.885
		STEM.Biology                                 0.903
		STEM.Chemistry                               0.487
		STEM.Computing                               0.358
		STEM.Earth and environment                   0.576
		STEM.Engineering                             0.693
		STEM.Libraries & Information                 0.359
		STEM.Mathematics                             0.439
		STEM.Medicine & Health                       0.599
		STEM.Physics                                 0.278
		STEM.STEM*                                   0.884
		STEM.Space                                   0.95
		STEM.Technology                              0.471
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

