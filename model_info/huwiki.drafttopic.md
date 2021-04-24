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
	counts (n=58260):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15310  -->  13192  2118  1129  41821
			'Culture.Biography.Women'                       3531  -->   2178  1353   383  54346
			'Culture.Food and drink'                        1437  -->    808   629   133  56690
			'Culture.Internet culture'                      3201  -->   2520   681   233  54826
			'Culture.Linguistics'                           1596  -->    969   627    96  56568
			'Culture.Literature'                            5484  -->   3741  1743   535  52241
			'Culture.Media.Books'                           1715  -->   1286   429   117  56428
			'Culture.Media.Entertainment'                   2307  -->    867  1440   239  55714
			'Culture.Media.Films'                           2816  -->   2209   607   182  55262
			'Culture.Media.Media*'                         14125  -->  12073  2052  1409  42726
			'Culture.Media.Music'                           3252  -->   2570   682   254  54754
			'Culture.Media.Radio'                            323  -->    170   153    31  57906
			'Culture.Media.Software'                        2128  -->   1623   505   284  55848
			'Culture.Media.Television'                      2434  -->   1826   608   146  55680
			'Culture.Media.Video games'                     2038  -->   1787   251    67  56155
			'Culture.Performing arts'                       1459  -->    810   649   145  56656
			'Culture.Philosophy and religion'               3909  -->   2003  1906   388  53963
			'Culture.Sports'                                6193  -->   5459   734   193  51874
			'Culture.Visual arts.Architecture'              1992  -->   1221   771   244  56024
			'Culture.Visual arts.Comics and Anime'          1824  -->   1384   440   100  56336
			'Culture.Visual arts.Fashion'                    776  -->    415   361    53  57431
			'Culture.Visual arts.Visual arts*'              5280  -->   3195  2085   481  52499
			'Geography.Geographical'                        3799  -->   2313  1486   528  53933
			'Geography.Regions.Africa.Africa*'              3983  -->   2415  1568   370  53907
			'Geography.Regions.Africa.Central Africa'        874  -->    509   365    61  57325
			'Geography.Regions.Africa.Eastern Africa'        361  -->    219   142    35  57864
			'Geography.Regions.Africa.Northern Africa'      1468  -->    821   647   111  56681
			'Geography.Regions.Africa.Southern Africa'       683  -->    456   227    49  57528
			'Geography.Regions.Africa.Western Africa'        155  -->     67    88    50  58055
			'Geography.Regions.Americas.Central America'    1354  -->    702   652   101  56805
			'Geography.Regions.Americas.North America'      5506  -->   3136  2370   815  51939
			'Geography.Regions.Americas.South America'      1602  -->   1038   564   136  56522
			'Geography.Regions.Asia.Asia*'                 10551  -->   7858  2693  1075  46634
			'Geography.Regions.Asia.Central Asia'           1318  -->    841   477    84  56858
			'Geography.Regions.Asia.East Asia'              3361  -->   2453   908   219  54680
			'Geography.Regions.Asia.North Asia'             1840  -->   1227   613   243  56177
			'Geography.Regions.Asia.South Asia'             1780  -->   1175   605   119  56361
			'Geography.Regions.Asia.Southeast Asia'         1584  -->    846   738    88  56588
			'Geography.Regions.Asia.West Asia'              2439  -->   1606   833   220  55601
			'Geography.Regions.Europe.Eastern Europe'       4845  -->   3300  1545   598  52817
			'Geography.Regions.Europe.Europe*'             16576  -->  12804  3772  2339  39345
			'Geography.Regions.Europe.Northern Europe'      3563  -->   2160  1403   393  54304
			'Geography.Regions.Europe.Southern Europe'      4000  -->   2755  1245   371  53889
			'Geography.Regions.Europe.Western Europe'       5143  -->   3665  1478   566  52551
			'Geography.Regions.Oceania'                     1821  -->   1191   630   126  56313
			'History and Society.Business and economics'    3106  -->   1510  1596   331  54823
			'History and Society.Education'                 1568  -->    654   914   143  56549
			'History and Society.History'                   6030  -->   3421  2609   683  51547
			'History and Society.Military and warfare'      4947  -->   3209  1738   487  52826
			'History and Society.Politics and government'   4355  -->   2263  2092   404  53501
			'History and Society.Society'                   6075  -->   2535  3540   515  51670
			'History and Society.Transportation'            4015  -->   3468   547   200  54045
			'STEM.Biology'                                  4621  -->   3907   714   165  53474
			'STEM.Chemistry'                                1581  -->   1173   408   187  56492
			'STEM.Computing'                                2399  -->   1834   565   322  55539
			'STEM.Earth and environment'                    1842  -->   1160   682   144  56274
			'STEM.Engineering'                              2439  -->   1588   851   229  55592
			'STEM.Libraries & Information'                   498  -->    266   232    42  57720
			'STEM.Mathematics'                               979  -->    726   253    42  57239
			'STEM.Medicine & Health'                        1865  -->   1206   659   180  56215
			'STEM.Physics'                                  1378  -->    767   611   180  56702
			'STEM.STEM*'                                   18114  -->  15808  2306  1131  39015
			'STEM.Space'                                    2331  -->   2120   211    61  55868
			'STEM.Technology'                               4782  -->   3388  1394   583  52895
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.263         0.123
		Culture.Biography.Women                         0.061         0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.055         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.04          0.004
		Culture.Media.Films                             0.048         0.011
		Culture.Media.Media*                            0.242         0.058
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.006         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.067         0.011
		Culture.Sports                                  0.106         0.071
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.031         0.002
		Culture.Visual arts.Fashion                     0.013         0.001
		Culture.Visual arts.Visual arts*                0.091         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.012         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.095         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.181         0.045
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.058         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.042         0.011
		Geography.Regions.Europe.Eastern Europe         0.083         0.013
		Geography.Regions.Europe.Europe*                0.285         0.076
		Geography.Regions.Europe.Northern Europe        0.061         0.031
		Geography.Regions.Europe.Southern Europe        0.069         0.013
		Geography.Regions.Europe.Western Europe         0.088         0.019
		Geography.Regions.Oceania                       0.031         0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.027         0.007
		History and Society.History                     0.104         0.011
		History and Society.Military and warfare        0.085         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.104         0.013
		History and Society.Transportation              0.069         0.015
		STEM.Biology                                    0.079         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.042         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.311         0.069
		STEM.Space                                      0.04          0.006
		STEM.Technology                                 0.082         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.022
		History and Society.Society                  0.015
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.087
		STEM.Space                                   0.007
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.978
		History and Society.Society                  0.985
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.913
		STEM.Space                                   0.993
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.731, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.862
		Culture.Biography.Women                      0.617
		Culture.Food and drink                       0.562
		Culture.Internet culture                     0.787
		Culture.Linguistics                          0.607
		Culture.Literature                           0.682
		Culture.Media.Books                          0.75
		Culture.Media.Entertainment                  0.376
		Culture.Media.Films                          0.784
		Culture.Media.Media*                         0.855
		Culture.Media.Music                          0.79
		Culture.Media.Radio                          0.526
		Culture.Media.Software                       0.763
		Culture.Media.Television                     0.75
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.555
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.613
		Culture.Visual arts.Comics and Anime         0.759
		Culture.Visual arts.Fashion                  0.535
		Culture.Visual arts.Visual arts*             0.605
		Geography.Geographical                       0.609
		Geography.Regions.Africa.Africa*             0.606
		Geography.Regions.Africa.Central Africa      0.582
		Geography.Regions.Africa.Eastern Africa      0.607
		Geography.Regions.Africa.Northern Africa     0.559
		Geography.Regions.Africa.Southern Africa     0.668
		Geography.Regions.Africa.Western Africa      0.432
		Geography.Regions.Americas.Central America   0.518
		Geography.Regions.Americas.North America     0.57
		Geography.Regions.Americas.South America     0.648
		Geography.Regions.Asia.Asia*                 0.745
		Geography.Regions.Asia.Central Asia          0.638
		Geography.Regions.Asia.East Asia             0.73
		Geography.Regions.Asia.North Asia            0.667
		Geography.Regions.Asia.South Asia            0.66
		Geography.Regions.Asia.Southeast Asia        0.534
		Geography.Regions.Asia.West Asia             0.658
		Geography.Regions.Europe.Eastern Europe      0.681
		Geography.Regions.Europe.Europe*             0.772
		Geography.Regions.Europe.Northern Europe     0.606
		Geography.Regions.Europe.Southern Europe     0.689
		Geography.Regions.Europe.Western Europe      0.713
		Geography.Regions.Oceania                    0.654
		History and Society.Business and economics   0.486
		History and Society.Education                0.417
		History and Society.History                  0.567
		History and Society.Military and warfare     0.649
		History and Society.Politics and government  0.52
		History and Society.Society                  0.417
		History and Society.Transportation           0.864
		STEM.Biology                                 0.845
		STEM.Chemistry                               0.742
		STEM.Computing                               0.764
		STEM.Earth and environment                   0.63
		STEM.Engineering                             0.651
		STEM.Libraries & Information                 0.534
		STEM.Mathematics                             0.742
		STEM.Medicine & Health                       0.647
		STEM.Physics                                 0.557
		STEM.STEM*                                   0.873
		STEM.Space                                   0.909
		STEM.Technology                              0.708
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.993
		History and Society.Society                  0.99
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.671, macro=0.522):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.822
		Culture.Biography.Women                      0.566
		Culture.Food and drink                       0.372
		Culture.Internet culture                     0.395
		Culture.Linguistics                          0.726
		Culture.Literature                           0.514
		Culture.Media.Books                          0.594
		Culture.Media.Entertainment                  0.24
		Culture.Media.Films                          0.717
		Culture.Media.Media*                         0.624
		Culture.Media.Music                          0.807
		Culture.Media.Radio                          0.68
		Culture.Media.Software                       0.167
		Culture.Media.Television                     0.718
		Culture.Media.Video games                    0.658
		Culture.Performing arts                      0.386
		Culture.Philosophy and religion              0.436
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.601
		Culture.Visual arts.Comics and Anime         0.485
		Culture.Visual arts.Fashion                  0.319
		Culture.Visual arts.Visual arts*             0.554
		Geography.Geographical                       0.603
		Geography.Regions.Africa.Africa*             0.411
		Geography.Regions.Africa.Central Africa      0.257
		Geography.Regions.Africa.Eastern Africa      0.313
		Geography.Regions.Africa.Northern Africa     0.26
		Geography.Regions.Africa.Southern Africa     0.48
		Geography.Regions.Africa.Western Africa      0.256
		Geography.Regions.Americas.Central America   0.492
		Geography.Regions.Americas.North America     0.717
		Geography.Regions.Americas.South America     0.631
		Geography.Regions.Asia.Asia*                 0.612
		Geography.Regions.Asia.Central Asia          0.273
		Geography.Regions.Asia.East Asia             0.679
		Geography.Regions.Asia.North Asia            0.125
		Geography.Regions.Asia.South Asia            0.828
		Geography.Regions.Asia.Southeast Asia        0.675
		Geography.Regions.Asia.West Asia             0.648
		Geography.Regions.Europe.Eastern Europe      0.442
		Geography.Regions.Europe.Europe*             0.532
		Geography.Regions.Europe.Northern Europe     0.727
		Geography.Regions.Europe.Southern Europe     0.571
		Geography.Regions.Europe.Western Europe      0.567
		Geography.Regions.Oceania                    0.818
		History and Society.Business and economics   0.452
		History and Society.Education                0.551
		History and Society.History                  0.322
		History and Society.Military and warfare     0.503
		History and Society.Politics and government  0.668
		History and Society.Society                  0.351
		History and Society.Transportation           0.782
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.26
		STEM.Computing                               0.263
		STEM.Earth and environment                   0.529
		STEM.Engineering                             0.455
		STEM.Libraries & Information                 0.313
		STEM.Mathematics                             0.297
		STEM.Medicine & Health                       0.566
		STEM.Physics                                 0.13
		STEM.STEM*                                   0.697
		STEM.Space                                   0.835
		STEM.Technology                              0.251
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.692, macro=0.563):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.841
		Culture.Biography.Women                      0.59
		Culture.Food and drink                       0.448
		Culture.Internet culture                     0.526
		Culture.Linguistics                          0.661
		Culture.Literature                           0.587
		Culture.Media.Books                          0.663
		Culture.Media.Entertainment                  0.293
		Culture.Media.Films                          0.749
		Culture.Media.Media*                         0.722
		Culture.Media.Music                          0.799
		Culture.Media.Radio                          0.593
		Culture.Media.Software                       0.274
		Culture.Media.Television                     0.734
		Culture.Media.Video games                    0.752
		Culture.Performing arts                      0.456
		Culture.Philosophy and religion              0.471
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.607
		Culture.Visual arts.Comics and Anime         0.592
		Culture.Visual arts.Fashion                  0.4
		Culture.Visual arts.Visual arts*             0.578
		Geography.Geographical                       0.606
		Geography.Regions.Africa.Africa*             0.49
		Geography.Regions.Africa.Central Africa      0.357
		Geography.Regions.Africa.Eastern Africa      0.413
		Geography.Regions.Africa.Northern Africa     0.355
		Geography.Regions.Africa.Southern Africa     0.558
		Geography.Regions.Africa.Western Africa      0.321
		Geography.Regions.Americas.Central America   0.505
		Geography.Regions.Americas.North America     0.635
		Geography.Regions.Americas.South America     0.64
		Geography.Regions.Asia.Asia*                 0.672
		Geography.Regions.Asia.Central Asia          0.382
		Geography.Regions.Asia.East Asia             0.703
		Geography.Regions.Asia.North Asia            0.211
		Geography.Regions.Asia.South Asia            0.735
		Geography.Regions.Asia.Southeast Asia        0.596
		Geography.Regions.Asia.West Asia             0.653
		Geography.Regions.Europe.Eastern Europe      0.536
		Geography.Regions.Europe.Europe*             0.63
		Geography.Regions.Europe.Northern Europe     0.661
		Geography.Regions.Europe.Southern Europe     0.624
		Geography.Regions.Europe.Western Europe      0.631
		Geography.Regions.Oceania                    0.727
		History and Society.Business and economics   0.469
		History and Society.Education                0.475
		History and Society.History                  0.411
		History and Society.Military and warfare     0.567
		History and Society.Politics and government  0.585
		History and Society.Society                  0.381
		History and Society.Transportation           0.821
		STEM.Biology                                 0.874
		STEM.Chemistry                               0.385
		STEM.Computing                               0.392
		STEM.Earth and environment                   0.575
		STEM.Engineering                             0.536
		STEM.Libraries & Information                 0.395
		STEM.Mathematics                             0.424
		STEM.Medicine & Health                       0.604
		STEM.Physics                                 0.211
		STEM.STEM*                                   0.775
		STEM.Space                                   0.87
		STEM.Technology                              0.371
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
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
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.931
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.983
		History and Society.Transportation           0.994
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.965
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.023
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.007
		History and Society.Society                  0.01
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.965, macro=0.965):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.968
		Culture.Food and drink                       0.966
		Culture.Internet culture                     0.982
		Culture.Linguistics                          0.963
		Culture.Literature                           0.967
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.981
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.921
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.941
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.958
		Culture.Visual arts.Visual arts*             0.956
		Geography.Geographical                       0.963
		Geography.Regions.Africa.Africa*             0.96
		Geography.Regions.Africa.Central Africa      0.979
		Geography.Regions.Africa.Eastern Africa      0.938
		Geography.Regions.Africa.Northern Africa     0.963
		Geography.Regions.Africa.Southern Africa     0.968
		Geography.Regions.Africa.Western Africa      0.888
		Geography.Regions.Americas.Central America   0.965
		Geography.Regions.Americas.North America     0.95
		Geography.Regions.Americas.South America     0.968
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.973
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.971
		Geography.Regions.Asia.Southeast Asia        0.963
		Geography.Regions.Asia.West Asia             0.968
		Geography.Regions.Europe.Eastern Europe      0.968
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.959
		Geography.Regions.Europe.Southern Europe     0.968
		Geography.Regions.Europe.Western Europe      0.973
		Geography.Regions.Oceania                    0.966
		History and Society.Business and economics   0.945
		History and Society.Education                0.954
		History and Society.History                  0.948
		History and Society.Military and warfare     0.964
		History and Society.Politics and government  0.938
		History and Society.Society                  0.907
		History and Society.Transportation           0.983
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.981
		STEM.Computing                               0.983
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.97
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.974
		STEM.Medicine & Health                       0.97
		STEM.Physics                                 0.971
		STEM.STEM*                                   0.971
		STEM.Space                                   0.991
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.733, macro=0.549):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.911
		Culture.Biography.Women                      0.566
		Culture.Food and drink                       0.362
		Culture.Internet culture                     0.669
		Culture.Linguistics                          0.659
		Culture.Literature                           0.603
		Culture.Media.Books                          0.724
		Culture.Media.Entertainment                  0.192
		Culture.Media.Films                          0.786
		Culture.Media.Media*                         0.825
		Culture.Media.Music                          0.821
		Culture.Media.Radio                          0.361
		Culture.Media.Software                       0.324
		Culture.Media.Television                     0.753
		Culture.Media.Video games                    0.778
		Culture.Performing arts                      0.378
		Culture.Philosophy and religion              0.417
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.586
		Culture.Visual arts.Comics and Anime         0.645
		Culture.Visual arts.Fashion                  0.254
		Culture.Visual arts.Visual arts*             0.585
		Geography.Geographical                       0.617
		Geography.Regions.Africa.Africa*             0.44
		Geography.Regions.Africa.Central Africa      0.257
		Geography.Regions.Africa.Eastern Africa      0.21
		Geography.Regions.Africa.Northern Africa     0.266
		Geography.Regions.Africa.Southern Africa     0.44
		Geography.Regions.Africa.Western Africa      0.134
		Geography.Regions.Americas.Central America   0.412
		Geography.Regions.Americas.North America     0.709
		Geography.Regions.Americas.South America     0.593
		Geography.Regions.Asia.Asia*                 0.728
		Geography.Regions.Asia.Central Asia          0.265
		Geography.Regions.Asia.East Asia             0.699
		Geography.Regions.Asia.North Asia            0.175
		Geography.Regions.Asia.South Asia            0.777
		Geography.Regions.Asia.Southeast Asia        0.567
		Geography.Regions.Asia.West Asia             0.637
		Geography.Regions.Europe.Eastern Europe      0.544
		Geography.Regions.Europe.Europe*             0.725
		Geography.Regions.Europe.Northern Europe     0.711
		Geography.Regions.Europe.Southern Europe     0.644
		Geography.Regions.Europe.Western Europe      0.718
		Geography.Regions.Oceania                    0.745
		History and Society.Business and economics   0.422
		History and Society.Education                0.39
		History and Society.History                  0.432
		History and Society.Military and warfare     0.591
		History and Society.Politics and government  0.596
		History and Society.Society                  0.324
		History and Society.Transportation           0.868
		STEM.Biology                                 0.895
		STEM.Chemistry                               0.374
		STEM.Computing                               0.41
		STEM.Earth and environment                   0.539
		STEM.Engineering                             0.56
		STEM.Libraries & Information                 0.187
		STEM.Mathematics                             0.413
		STEM.Medicine & Health                       0.597
		STEM.Physics                                 0.122
		STEM.STEM*                                   0.866
		STEM.Space                                   0.927
		STEM.Technology                              0.486
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

