Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'criterion': 'friedman_mse', 'random_state': None, 'label_weights': {}, 'n_estimators': 150, 'n_iter_no_change': None, 'verbose': 0, 'scale': False, 'min_samples_leaf': 1, 'min_impurity_split': None, 'validation_fraction': 0.1, 'init': None, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'presort': 'auto', 'min_impurity_decrease': 0.0, 'learning_rate': 0.1, 'warm_start': False, 'multilabel': True, 'max_leaf_nodes': None, 'max_depth': 5, 'loss': 'deviance', 'tol': 0.0001, 'max_features': 'log2', 'subsample': 1.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'population_rates': None, 'center': False}
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
	counts (n=63017):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16717  -->  13634  3083  1600  44700
			'Culture.Biography.Women'                       4173  -->   1580  2593   540  58304
			'Culture.Food and drink'                        1323  -->    948   375    81  61613
			'Culture.Internet culture'                      2946  -->   2187   759   227  59844
			'Culture.Linguistics'                           1384  -->    933   451    88  61545
			'Culture.Literature'                            5277  -->   3642  1635   619  57121
			'Culture.Media.Books'                           1919  -->   1197   722   208  60890
			'Culture.Media.Entertainment'                   1876  -->    626  1250   124  61017
			'Culture.Media.Films'                           2307  -->   1766   541   171  60539
			'Culture.Media.Media*'                         14363  -->  11790  2573  1975  46679
			'Culture.Media.Music'                           2677  -->   2130   547   285  60055
			'Culture.Media.Radio'                           1174  -->    943   231    47  61796
			'Culture.Media.Software'                        1798  -->    984   814   374  60845
			'Culture.Media.Television'                      2200  -->   1426   774   230  60587
			'Culture.Media.Video games'                     2078  -->   1780   298    63  60876
			'Culture.Performing arts'                       1334  -->    805   529   121  61562
			'Culture.Philosophy and religion'               2638  -->   1384  1254   382  59997
			'Culture.Sports'                                5843  -->   5177   666   351  56823
			'Culture.Visual arts.Architecture'              2565  -->   1744   821   290  60162
			'Culture.Visual arts.Comics and Anime'          1488  -->    987   501   122  61407
			'Culture.Visual arts.Fashion'                   1188  -->    814   374    76  61753
			'Culture.Visual arts.Visual arts*'              5987  -->   3884  2103   598  56432
			'Geography.Geographical'                        3344  -->   1932  1412   302  59371
			'Geography.Regions.Africa.Africa*'              5693  -->   4364  1329   288  57036
			'Geography.Regions.Africa.Central Africa'         28  -->      3    25    72  62917
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    659   455    56  61847
			'Geography.Regions.Africa.Northern Africa'      1266  -->    697   569   123  61628
			'Geography.Regions.Africa.Southern Africa'      1288  -->    864   424    63  61666
			'Geography.Regions.Africa.Western Africa'       1152  -->    856   296    56  61809
			'Geography.Regions.Americas.Central America'    1326  -->    504   822   103  61588
			'Geography.Regions.Americas.North America'      7565  -->   4611  2954  1121  54331
			'Geography.Regions.Americas.South America'      1523  -->    740   783   206  61288
			'Geography.Regions.Asia.Asia*'                 11060  -->   8321  2739   977  50980
			'Geography.Regions.Asia.Central Asia'           1163  -->    633   530    76  61778
			'Geography.Regions.Asia.East Asia'              2721  -->   1661  1060   307  59989
			'Geography.Regions.Asia.North Asia'             1361  -->    783   578   168  61488
			'Geography.Regions.Asia.South Asia'             2438  -->   1940   498   122  60457
			'Geography.Regions.Asia.Southeast Asia'         1688  -->    899   789   100  61229
			'Geography.Regions.Asia.West Asia'              2264  -->   1448   816   138  60615
			'Geography.Regions.Europe.Eastern Europe'       3083  -->   1832  1251   349  59585
			'Geography.Regions.Europe.Europe*'             12415  -->   8214  4201  1895  48707
			'Geography.Regions.Europe.Northern Europe'      4244  -->   2028  2216   564  58209
			'Geography.Regions.Europe.Southern Europe'      2320  -->   1028  1292   261  60436
			'Geography.Regions.Europe.Western Europe'       3160  -->   1731  1429   451  59406
			'Geography.Regions.Oceania'                     2537  -->   1686   851    96  60384
			'History and Society.Business and economics'    3430  -->   1493  1937   533  59054
			'History and Society.Education'                 2178  -->   1038  1140   261  60578
			'History and Society.History'                   3217  -->    877  2340   337  59463
			'History and Society.Military and warfare'      3977  -->   2629  1348   409  58631
			'History and Society.Politics and government'   4647  -->   2235  2412   538  57832
			'History and Society.Society'                   4057  -->    955  3102   316  58644
			'History and Society.Transportation'            3604  -->   2942   662   267  59146
			'STEM.Biology'                                  2834  -->   2130   704   165  60018
			'STEM.Chemistry'                                1344  -->    893   451   196  61477
			'STEM.Computing'                                2011  -->   1226   785   441  60565
			'STEM.Earth and environment'                    1683  -->    960   723   136  61198
			'STEM.Engineering'                              2272  -->   1422   850   187  60558
			'STEM.Libraries & Information'                  1159  -->    620   539    75  61783
			'STEM.Mathematics'                              1121  -->    638   483   111  61785
			'STEM.Medicine & Health'                        1737  -->   1051   686   199  61081
			'STEM.Physics'                                  1206  -->    699   507   177  61634
			'STEM.STEM*'                                   16499  -->  13656  2843  1275  45243
			'STEM.Space'                                    1398  -->   1178   220    45  61574
			'STEM.Technology'                               3712  -->   1996  1716   686  58619
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
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
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
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
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
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.01
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.008
		History and Society.History                  0.009
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.023
		History and Society.Society                  0.008
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
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
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
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
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
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.991
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.977
		History and Society.Society                  0.992
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
	recall (micro=0.689, macro=0.614):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.816
		Culture.Biography.Women                      0.379
		Culture.Food and drink                       0.717
		Culture.Internet culture                     0.742
		Culture.Linguistics                          0.674
		Culture.Literature                           0.69
		Culture.Media.Books                          0.624
		Culture.Media.Entertainment                  0.334
		Culture.Media.Films                          0.765
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.803
		Culture.Media.Software                       0.547
		Culture.Media.Television                     0.648
		Culture.Media.Video games                    0.857
		Culture.Performing arts                      0.603
		Culture.Philosophy and religion              0.525
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.663
		Culture.Visual arts.Fashion                  0.685
		Culture.Visual arts.Visual arts*             0.649
		Geography.Geographical                       0.578
		Geography.Regions.Africa.Africa*             0.767
		Geography.Regions.Africa.Central Africa      0.107
		Geography.Regions.Africa.Eastern Africa      0.592
		Geography.Regions.Africa.Northern Africa     0.551
		Geography.Regions.Africa.Southern Africa     0.671
		Geography.Regions.Africa.Western Africa      0.743
		Geography.Regions.Americas.Central America   0.38
		Geography.Regions.Americas.North America     0.61
		Geography.Regions.Americas.South America     0.486
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.544
		Geography.Regions.Asia.East Asia             0.61
		Geography.Regions.Asia.North Asia            0.575
		Geography.Regions.Asia.South Asia            0.796
		Geography.Regions.Asia.Southeast Asia        0.533
		Geography.Regions.Asia.West Asia             0.64
		Geography.Regions.Europe.Eastern Europe      0.594
		Geography.Regions.Europe.Europe*             0.662
		Geography.Regions.Europe.Northern Europe     0.478
		Geography.Regions.Europe.Southern Europe     0.443
		Geography.Regions.Europe.Western Europe      0.548
		Geography.Regions.Oceania                    0.665
		History and Society.Business and economics   0.435
		History and Society.Education                0.477
		History and Society.History                  0.273
		History and Society.Military and warfare     0.661
		History and Society.Politics and government  0.481
		History and Society.Society                  0.235
		History and Society.Transportation           0.816
		STEM.Biology                                 0.752
		STEM.Chemistry                               0.664
		STEM.Computing                               0.61
		STEM.Earth and environment                   0.57
		STEM.Engineering                             0.626
		STEM.Libraries & Information                 0.535
		STEM.Mathematics                             0.569
		STEM.Medicine & Health                       0.605
		STEM.Physics                                 0.58
		STEM.STEM*                                   0.828
		STEM.Space                                   0.843
		STEM.Technology                              0.538
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
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
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
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
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.658, macro=0.51):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.768
		Culture.Biography.Women                      0.379
		Culture.Food and drink                       0.574
		Culture.Internet culture                     0.408
		Culture.Linguistics                          0.777
		Culture.Literature                           0.503
		Culture.Media.Books                          0.426
		Culture.Media.Entertainment                  0.372
		Culture.Media.Films                          0.743
		Culture.Media.Media*                         0.557
		Culture.Media.Music                          0.805
		Culture.Media.Radio                          0.695
		Culture.Media.Software                       0.107
		Culture.Media.Television                     0.604
		Culture.Media.Video games                    0.685
		Culture.Performing arts                      0.471
		Culture.Philosophy and religion              0.472
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.602
		Culture.Visual arts.Comics and Anime         0.424
		Culture.Visual arts.Fashion                  0.311
		Culture.Visual arts.Visual arts*             0.536
		Geography.Geographical                       0.734
		Geography.Regions.Africa.Africa*             0.545
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.229
		Geography.Regions.Africa.Northern Africa     0.254
		Geography.Regions.Africa.Southern Africa     0.436
		Geography.Regions.Africa.Western Africa      0.36
		Geography.Regions.Americas.Central America   0.43
		Geography.Regions.Americas.North America     0.674
		Geography.Regions.Americas.South America     0.479
		Geography.Regions.Asia.Asia*                 0.656
		Geography.Regions.Asia.Central Asia          0.278
		Geography.Regions.Asia.East Asia             0.581
		Geography.Regions.Asia.North Asia            0.163
		Geography.Regions.Asia.South Asia            0.859
		Geography.Regions.Asia.Southeast Asia        0.664
		Geography.Regions.Asia.West Asia             0.756
		Geography.Regions.Europe.Eastern Europe      0.57
		Geography.Regions.Europe.Europe*             0.593
		Geography.Regions.Europe.Northern Europe     0.611
		Geography.Regions.Europe.Southern Europe     0.577
		Geography.Regions.Europe.Western Europe      0.587
		Geography.Regions.Oceania                    0.865
		History and Society.Business and economics   0.332
		History and Society.Education                0.452
		History and Society.History                  0.347
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.602
		History and Society.Society                  0.359
		History and Society.Transportation           0.736
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.246
		STEM.Computing                               0.185
		STEM.Earth and environment                   0.54
		STEM.Engineering                             0.517
		STEM.Libraries & Information                 0.215
		STEM.Mathematics                             0.117
		STEM.Medicine & Health                       0.546
		STEM.Physics                                 0.147
		STEM.STEM*                                   0.692
		STEM.Space                                   0.875
		STEM.Technology                              0.193
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
		Culture.Media.Films                          0.998
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
		STEM.Biology                                 0.991
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
	f1 (micro=0.667, macro=0.537):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.791
		Culture.Biography.Women                      0.379
		Culture.Food and drink                       0.638
		Culture.Internet culture                     0.527
		Culture.Linguistics                          0.722
		Culture.Literature                           0.582
		Culture.Media.Books                          0.506
		Culture.Media.Entertainment                  0.352
		Culture.Media.Films                          0.754
		Culture.Media.Media*                         0.664
		Culture.Media.Music                          0.8
		Culture.Media.Radio                          0.745
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.625
		Culture.Media.Video games                    0.761
		Culture.Performing arts                      0.529
		Culture.Philosophy and religion              0.497
		Culture.Sports                               0.901
		Culture.Visual arts.Architecture             0.639
		Culture.Visual arts.Comics and Anime         0.517
		Culture.Visual arts.Fashion                  0.428
		Culture.Visual arts.Visual arts*             0.587
		Geography.Geographical                       0.647
		Geography.Regions.Africa.Africa*             0.637
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.331
		Geography.Regions.Africa.Northern Africa     0.347
		Geography.Regions.Africa.Southern Africa     0.529
		Geography.Regions.Africa.Western Africa      0.485
		Geography.Regions.Americas.Central America   0.403
		Geography.Regions.Americas.North America     0.64
		Geography.Regions.Americas.South America     0.483
		Geography.Regions.Asia.Asia*                 0.701
		Geography.Regions.Asia.Central Asia          0.368
		Geography.Regions.Asia.East Asia             0.595
		Geography.Regions.Asia.North Asia            0.255
		Geography.Regions.Asia.South Asia            0.826
		Geography.Regions.Asia.Southeast Asia        0.591
		Geography.Regions.Asia.West Asia             0.693
		Geography.Regions.Europe.Eastern Europe      0.582
		Geography.Regions.Europe.Europe*             0.625
		Geography.Regions.Europe.Northern Europe     0.536
		Geography.Regions.Europe.Southern Europe     0.501
		Geography.Regions.Europe.Western Europe      0.567
		Geography.Regions.Oceania                    0.752
		History and Society.Business and economics   0.376
		History and Society.Education                0.464
		History and Society.History                  0.305
		History and Society.Military and warfare     0.616
		History and Society.Politics and government  0.535
		History and Society.Society                  0.284
		History and Society.Transportation           0.774
		STEM.Biology                                 0.821
		STEM.Chemistry                               0.359
		STEM.Computing                               0.284
		STEM.Earth and environment                   0.555
		STEM.Engineering                             0.566
		STEM.Libraries & Information                 0.307
		STEM.Mathematics                             0.194
		STEM.Medicine & Health                       0.574
		STEM.Physics                                 0.234
		STEM.STEM*                                   0.754
		STEM.Space                                   0.858
		STEM.Technology                              0.285
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
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
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.995
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
		Geography.Regions.Africa.Northern Africa     0.997
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
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.976
		History and Society.Society                  0.985
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
		STEM.STEM*                                   0.963
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.035
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
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
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
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
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.967, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.953
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.977
		Culture.Literature                           0.973
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.988
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.981
		Culture.Philosophy and religion              0.958
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.979
		Geography.Regions.Africa.Central Africa      0.551
		Geography.Regions.Africa.Eastern Africa      0.981
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.971
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.957
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.969
		Geography.Regions.Oceania                    0.978
		History and Society.Business and economics   0.953
		History and Society.Education                0.964
		History and Society.History                  0.922
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.95
		History and Society.Society                  0.897
		History and Society.Transportation           0.986
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.986
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.975
		STEM.Libraries & Information                 0.971
		STEM.Mathematics                             0.98
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.968
		STEM.Space                                   0.992
		STEM.Technology                              0.963
		-------------------------------------------  -----
	pr_auc (micro=0.707, macro=0.548):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.303
		Culture.Food and drink                       0.649
		Culture.Internet culture                     0.707
		Culture.Linguistics                          0.742
		Culture.Literature                           0.633
		Culture.Media.Books                          0.532
		Culture.Media.Entertainment                  0.278
		Culture.Media.Films                          0.799
		Culture.Media.Media*                         0.769
		Culture.Media.Music                          0.848
		Culture.Media.Radio                          0.813
		Culture.Media.Software                       0.146
		Culture.Media.Television                     0.651
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.432
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.696
		Culture.Visual arts.Comics and Anime         0.539
		Culture.Visual arts.Fashion                  0.348
		Culture.Visual arts.Visual arts*             0.599
		Geography.Geographical                       0.701
		Geography.Regions.Africa.Africa*             0.673
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.261
		Geography.Regions.Africa.Northern Africa     0.337
		Geography.Regions.Africa.Southern Africa     0.514
		Geography.Regions.Africa.Western Africa      0.462
		Geography.Regions.Americas.Central America   0.357
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.443
		Geography.Regions.Asia.Asia*                 0.745
		Geography.Regions.Asia.Central Asia          0.342
		Geography.Regions.Asia.East Asia             0.592
		Geography.Regions.Asia.North Asia            0.197
		Geography.Regions.Asia.South Asia            0.846
		Geography.Regions.Asia.Southeast Asia        0.582
		Geography.Regions.Asia.West Asia             0.754
		Geography.Regions.Europe.Eastern Europe      0.615
		Geography.Regions.Europe.Europe*             0.662
		Geography.Regions.Europe.Northern Europe     0.576
		Geography.Regions.Europe.Southern Europe     0.504
		Geography.Regions.Europe.Western Europe      0.579
		Geography.Regions.Oceania                    0.802
		History and Society.Business and economics   0.32
		History and Society.Education                0.425
		History and Society.History                  0.236
		History and Society.Military and warfare     0.666
		History and Society.Politics and government  0.578
		History and Society.Society                  0.243
		History and Society.Transportation           0.83
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.362
		STEM.Computing                               0.202
		STEM.Earth and environment                   0.527
		STEM.Engineering                             0.57
		STEM.Libraries & Information                 0.291
		STEM.Mathematics                             0.173
		STEM.Medicine & Health                       0.595
		STEM.Physics                                 0.257
		STEM.STEM*                                   0.841
		STEM.Space                                   0.912
		STEM.Technology                              0.246
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.Physics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}}, 'type': 'object'}}}

