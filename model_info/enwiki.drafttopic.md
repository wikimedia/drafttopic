Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'presort': 'deprecated', 'min_weight_fraction_leaf': 0.0, 'center': False, 'validation_fraction': 0.1, 'max_depth': 5, 'max_features': 'log2', 'learning_rate': 0.1, 'label_weights': {}, 'subsample': 1.0, 'criterion': 'friedman_mse', 'warm_start': False, 'random_state': None, 'loss': 'deviance', 'init': None, 'n_iter_no_change': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'ccp_alpha': 0.0, 'tol': 0.0001, 'scale': False, 'verbose': 0, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'population_rates': None, 'max_leaf_nodes': None, 'n_estimators': 150, 'min_impurity_split': None, 'min_samples_split': 2, 'multilabel': True}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=60905):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16147  -->  13404  2743  1463  43295
			'Culture.Biography.Women'                       4041  -->   2755  1286   808  56056
			'Culture.Food and drink'                        1222  -->    726   496    93  59590
			'Culture.Internet culture'                      2732  -->   1895   837   230  57943
			'Culture.Linguistics'                           1169  -->    773   396   126  59610
			'Culture.Literature'                            5001  -->   3302  1699   530  55374
			'Culture.Media.Books'                           1792  -->   1121   671   260  58853
			'Culture.Media.Entertainment'                   1691  -->    664  1027   189  59025
			'Culture.Media.Films'                           2259  -->   1729   530   187  58459
			'Culture.Media.Media*'                         13536  -->  10947  2589  1589  45780
			'Culture.Media.Music'                           2502  -->   1849   653   267  58136
			'Culture.Media.Radio'                           1126  -->    845   281    46  59733
			'Culture.Media.Software'                        1652  -->    775   877   324  58929
			'Culture.Media.Television'                      2029  -->   1332   697   202  58674
			'Culture.Media.Video games'                     1940  -->   1597   343    66  58899
			'Culture.Performing arts'                       1257  -->    705   552   126  59522
			'Culture.Philosophy and religion'               2583  -->   1258  1325   316  58006
			'Culture.Sports'                                5799  -->   5094   705   310  54796
			'Culture.Visual arts.Architecture'              2497  -->   1700   797   278  58130
			'Culture.Visual arts.Comics and Anime'          1399  -->   1011   388   108  59398
			'Culture.Visual arts.Fashion'                   1110  -->    651   459    72  59723
			'Culture.Visual arts.Visual arts*'              5713  -->   3909  1804   563  54629
			'Geography.Geographical'                        3399  -->   2133  1266   271  57235
			'Geography.Regions.Africa.Africa*'              6314  -->   5249  1065   359  54232
			'Geography.Regions.Africa.Central Africa'       1134  -->    821   313    52  59719
			'Geography.Regions.Africa.Eastern Africa'       1074  -->    818   256    41  59790
			'Geography.Regions.Africa.Northern Africa'      1259  -->    895   364    89  59557
			'Geography.Regions.Africa.Southern Africa'      1237  -->    893   344    62  59606
			'Geography.Regions.Africa.Western Africa'       1120  -->    882   238    70  59715
			'Geography.Regions.Americas.Central America'    1269  -->    815   454    83  59553
			'Geography.Regions.Americas.North America'      7174  -->   4512  2662  1121  52610
			'Geography.Regions.Americas.South America'      1531  -->   1073   458   113  59261
			'Geography.Regions.Asia.Asia*'                 10799  -->   8771  2028   857  49249
			'Geography.Regions.Asia.Central Asia'           1097  -->    785   312    59  59749
			'Geography.Regions.Asia.East Asia'              2642  -->   1816   826   275  57988
			'Geography.Regions.Asia.North Asia'             1321  -->    826   495   182  59402
			'Geography.Regions.Asia.South Asia'             2354  -->   1880   474   114  58437
			'Geography.Regions.Asia.Southeast Asia'         1653  -->   1173   480   114  59138
			'Geography.Regions.Asia.West Asia'              2204  -->   1702   502   142  58559
			'Geography.Regions.Europe.Eastern Europe'       3005  -->   2225   780   269  57631
			'Geography.Regions.Europe.Europe*'             11882  -->   8687  3195  1680  47343
			'Geography.Regions.Europe.Northern Europe'      3947  -->   2493  1454   578  56380
			'Geography.Regions.Europe.Southern Europe'      2321  -->   1571   750   299  58285
			'Geography.Regions.Europe.Western Europe'       2971  -->   1893  1078   462  57472
			'Geography.Regions.Oceania'                     2463  -->   1876   587   150  58292
			'History and Society.Business and economics'    3254  -->   1286  1968   503  57148
			'History and Society.Education'                 2112  -->    852  1260   226  58567
			'History and Society.History'                   3155  -->   1063  2092   457  57293
			'History and Society.Military and warfare'      3889  -->   2540  1349   390  56626
			'History and Society.Politics and government'   4429  -->   2474  1955   433  56043
			'History and Society.Society'                   3807  -->   1300  2507   336  56762
			'History and Society.Transportation'            3425  -->   2783   642   241  57239
			'STEM.Biology'                                  2829  -->   2216   613   138  57938
			'STEM.Chemistry'                                1222  -->    733   489   147  59536
			'STEM.Computing'                                1966  -->   1126   840   381  58558
			'STEM.Earth and environment'                    1552  -->   1005   547   114  59239
			'STEM.Engineering'                              2242  -->   1500   742   182  58481
			'STEM.Libraries & Information'                  1120  -->    534   586   105  59680
			'STEM.Mathematics'                              1057  -->    569   488    87  59761
			'STEM.Medicine & Health'                        1640  -->    917   723   176  59089
			'STEM.Physics'                                  1112  -->    556   556   138  59655
			'STEM.STEM*'                                   15719  -->  13115  2604  1224  43962
			'STEM.Space'                                    1343  -->   1111   232    62  59500
			'STEM.Technology'                               3435  -->   1816  1619   596  56874
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.265         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.045         0.003
		Culture.Linguistics                             0.019         0.007
		Culture.Literature                              0.082         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.222         0.058
		Culture.Media.Music                             0.041         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.094         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.104         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.118         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.177         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.195         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.049         0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.025         0.005
		STEM.Engineering                                0.037         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.018         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.052, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.06
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.087
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.011
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.023
		History and Society.Society                  0.01
		History and Society.Transportation           0.016
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
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
	filter_rate (micro=0.948, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.94
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.913
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.977
		History and Society.Society                  0.99
		History and Society.Transportation           0.984
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
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
	recall (micro=0.726, macro=0.66):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.83
		Culture.Biography.Women                      0.682
		Culture.Food and drink                       0.594
		Culture.Internet culture                     0.694
		Culture.Linguistics                          0.661
		Culture.Literature                           0.66
		Culture.Media.Books                          0.626
		Culture.Media.Entertainment                  0.393
		Culture.Media.Films                          0.765
		Culture.Media.Media*                         0.809
		Culture.Media.Music                          0.739
		Culture.Media.Radio                          0.75
		Culture.Media.Software                       0.469
		Culture.Media.Television                     0.656
		Culture.Media.Video games                    0.823
		Culture.Performing arts                      0.561
		Culture.Philosophy and religion              0.487
		Culture.Sports                               0.878
		Culture.Visual arts.Architecture             0.681
		Culture.Visual arts.Comics and Anime         0.723
		Culture.Visual arts.Fashion                  0.586
		Culture.Visual arts.Visual arts*             0.684
		Geography.Geographical                       0.628
		Geography.Regions.Africa.Africa*             0.831
		Geography.Regions.Africa.Central Africa      0.724
		Geography.Regions.Africa.Eastern Africa      0.762
		Geography.Regions.Africa.Northern Africa     0.711
		Geography.Regions.Africa.Southern Africa     0.722
		Geography.Regions.Africa.Western Africa      0.787
		Geography.Regions.Americas.Central America   0.642
		Geography.Regions.Americas.North America     0.629
		Geography.Regions.Americas.South America     0.701
		Geography.Regions.Asia.Asia*                 0.812
		Geography.Regions.Asia.Central Asia          0.716
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.625
		Geography.Regions.Asia.South Asia            0.799
		Geography.Regions.Asia.Southeast Asia        0.71
		Geography.Regions.Asia.West Asia             0.772
		Geography.Regions.Europe.Eastern Europe      0.74
		Geography.Regions.Europe.Europe*             0.731
		Geography.Regions.Europe.Northern Europe     0.632
		Geography.Regions.Europe.Southern Europe     0.677
		Geography.Regions.Europe.Western Europe      0.637
		Geography.Regions.Oceania                    0.762
		History and Society.Business and economics   0.395
		History and Society.Education                0.403
		History and Society.History                  0.337
		History and Society.Military and warfare     0.653
		History and Society.Politics and government  0.559
		History and Society.Society                  0.341
		History and Society.Transportation           0.813
		STEM.Biology                                 0.783
		STEM.Chemistry                               0.6
		STEM.Computing                               0.573
		STEM.Earth and environment                   0.648
		STEM.Engineering                             0.669
		STEM.Libraries & Information                 0.477
		STEM.Mathematics                             0.538
		STEM.Medicine & Health                       0.559
		STEM.Physics                                 0.5
		STEM.STEM*                                   0.834
		STEM.Space                                   0.827
		STEM.Technology                              0.529
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.678, macro=0.53):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.781
		Culture.Biography.Women                      0.415
		Culture.Food and drink                       0.485
		Culture.Internet culture                     0.381
		Culture.Linguistics                          0.698
		Culture.Literature                           0.523
		Culture.Media.Books                          0.365
		Culture.Media.Entertainment                  0.307
		Culture.Media.Films                          0.718
		Culture.Media.Media*                         0.6
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.678
		Culture.Media.Software                       0.102
		Culture.Media.Television                     0.63
		Culture.Media.Video games                    0.658
		Culture.Performing arts                      0.435
		Culture.Philosophy and religion              0.492
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.604
		Culture.Visual arts.Comics and Anime         0.467
		Culture.Visual arts.Fashion                  0.283
		Culture.Visual arts.Visual arts*             0.556
		Geography.Geographical                       0.763
		Geography.Regions.Africa.Africa*             0.498
		Geography.Regions.Africa.Central Africa      0.345
		Geography.Regions.Africa.Eastern Africa      0.336
		Geography.Regions.Africa.Northern Africa     0.369
		Geography.Regions.Africa.Southern Africa     0.45
		Geography.Regions.Africa.Western Africa      0.315
		Geography.Regions.Americas.Central America   0.604
		Geography.Regions.Americas.North America     0.674
		Geography.Regions.Americas.South America     0.7
		Geography.Regions.Asia.Asia*                 0.694
		Geography.Regions.Asia.Central Asia          0.386
		Geography.Regions.Asia.East Asia             0.627
		Geography.Regions.Asia.North Asia            0.159
		Geography.Regions.Asia.South Asia            0.863
		Geography.Regions.Asia.Southeast Asia        0.69
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.674
		Geography.Regions.Europe.Europe*             0.638
		Geography.Regions.Europe.Northern Europe     0.663
		Geography.Regions.Europe.Southern Europe     0.637
		Geography.Regions.Europe.Western Europe      0.61
		Geography.Regions.Oceania                    0.82
		History and Society.Business and economics   0.316
		History and Society.Education                0.437
		History and Society.History                  0.318
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.679
		History and Society.Society                  0.426
		History and Society.Transportation           0.748
		STEM.Biology                                 0.92
		STEM.Chemistry                               0.275
		STEM.Computing                               0.193
		STEM.Earth and environment                   0.606
		STEM.Engineering                             0.532
		STEM.Libraries & Information                 0.144
		STEM.Mathematics                             0.134
		STEM.Medicine & Health                       0.548
		STEM.Physics                                 0.155
		STEM.STEM*                                   0.696
		STEM.Space                                   0.828
		STEM.Technology                              0.208
		-------------------------------------------  -----
	!precision (micro=0.988, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.988
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.696, macro=0.571):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.805
		Culture.Biography.Women                      0.516
		Culture.Food and drink                       0.534
		Culture.Internet culture                     0.492
		Culture.Linguistics                          0.679
		Culture.Literature                           0.584
		Culture.Media.Books                          0.461
		Culture.Media.Entertainment                  0.344
		Culture.Media.Films                          0.741
		Culture.Media.Media*                         0.689
		Culture.Media.Music                          0.767
		Culture.Media.Radio                          0.712
		Culture.Media.Software                       0.168
		Culture.Media.Television                     0.643
		Culture.Media.Video games                    0.731
		Culture.Performing arts                      0.49
		Culture.Philosophy and religion              0.489
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.64
		Culture.Visual arts.Comics and Anime         0.567
		Culture.Visual arts.Fashion                  0.382
		Culture.Visual arts.Visual arts*             0.613
		Geography.Geographical                       0.689
		Geography.Regions.Africa.Africa*             0.623
		Geography.Regions.Africa.Central Africa      0.467
		Geography.Regions.Africa.Eastern Africa      0.466
		Geography.Regions.Africa.Northern Africa     0.486
		Geography.Regions.Africa.Southern Africa     0.554
		Geography.Regions.Africa.Western Africa      0.45
		Geography.Regions.Americas.Central America   0.623
		Geography.Regions.Americas.North America     0.651
		Geography.Regions.Americas.South America     0.701
		Geography.Regions.Asia.Asia*                 0.748
		Geography.Regions.Asia.Central Asia          0.501
		Geography.Regions.Asia.East Asia             0.656
		Geography.Regions.Asia.North Asia            0.254
		Geography.Regions.Asia.South Asia            0.83
		Geography.Regions.Asia.Southeast Asia        0.7
		Geography.Regions.Asia.West Asia             0.775
		Geography.Regions.Europe.Eastern Europe      0.706
		Geography.Regions.Europe.Europe*             0.681
		Geography.Regions.Europe.Northern Europe     0.647
		Geography.Regions.Europe.Southern Europe     0.656
		Geography.Regions.Europe.Western Europe      0.623
		Geography.Regions.Oceania                    0.79
		History and Society.Business and economics   0.351
		History and Society.Education                0.42
		History and Society.History                  0.327
		History and Society.Military and warfare     0.613
		History and Society.Politics and government  0.613
		History and Society.Society                  0.379
		History and Society.Transportation           0.779
		STEM.Biology                                 0.846
		STEM.Chemistry                               0.378
		STEM.Computing                               0.289
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.592
		STEM.Libraries & Information                 0.222
		STEM.Mathematics                             0.214
		STEM.Medicine & Health                       0.554
		STEM.Physics                                 0.237
		STEM.STEM*                                   0.759
		STEM.Space                                   0.828
		STEM.Technology                              0.299
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.95
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.98
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.033
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.034
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.964, macro=0.967):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.967
		Culture.Food and drink                       0.971
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.957
		Culture.Literature                           0.965
		Culture.Media.Books                          0.974
		Culture.Media.Entertainment                  0.952
		Culture.Media.Films                          0.975
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.976
		Culture.Media.Software                       0.971
		Culture.Media.Television                     0.97
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.94
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.979
		Culture.Visual arts.Fashion                  0.973
		Culture.Visual arts.Visual arts*             0.961
		Geography.Geographical                       0.962
		Geography.Regions.Africa.Africa*             0.977
		Geography.Regions.Africa.Central Africa      0.977
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.97
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.98
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.97
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.974
		Geography.Regions.Asia.South Asia            0.977
		Geography.Regions.Asia.Southeast Asia        0.971
		Geography.Regions.Asia.West Asia             0.975
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.959
		Geography.Regions.Europe.Southern Europe     0.968
		Geography.Regions.Europe.Western Europe      0.963
		Geography.Regions.Oceania                    0.974
		History and Society.Business and economics   0.941
		History and Society.Education                0.941
		History and Society.History                  0.925
		History and Society.Military and warfare     0.965
		History and Society.Politics and government  0.944
		History and Society.Society                  0.898
		History and Society.Transportation           0.981
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.975
		STEM.Computing                               0.974
		STEM.Earth and environment                   0.966
		STEM.Engineering                             0.97
		STEM.Libraries & Information                 0.959
		STEM.Mathematics                             0.968
		STEM.Medicine & Health                       0.967
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.968
		STEM.Space                                   0.983
		STEM.Technology                              0.958
		-------------------------------------------  -----
	pr_auc (micro=0.729, macro=0.566):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.856
		Culture.Biography.Women                      0.469
		Culture.Food and drink                       0.45
		Culture.Internet culture                     0.595
		Culture.Linguistics                          0.625
		Culture.Literature                           0.593
		Culture.Media.Books                          0.388
		Culture.Media.Entertainment                  0.284
		Culture.Media.Films                          0.726
		Culture.Media.Media*                         0.784
		Culture.Media.Music                          0.793
		Culture.Media.Radio                          0.758
		Culture.Media.Software                       0.105
		Culture.Media.Television                     0.635
		Culture.Media.Video games                    0.78
		Culture.Performing arts                      0.425
		Culture.Philosophy and religion              0.423
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.554
		Culture.Visual arts.Fashion                  0.316
		Culture.Visual arts.Visual arts*             0.656
		Geography.Geographical                       0.74
		Geography.Regions.Africa.Africa*             0.654
		Geography.Regions.Africa.Central Africa      0.578
		Geography.Regions.Africa.Eastern Africa      0.378
		Geography.Regions.Africa.Northern Africa     0.428
		Geography.Regions.Africa.Southern Africa     0.526
		Geography.Regions.Africa.Western Africa      0.371
		Geography.Regions.Americas.Central America   0.566
		Geography.Regions.Americas.North America     0.703
		Geography.Regions.Americas.South America     0.711
		Geography.Regions.Asia.Asia*                 0.792
		Geography.Regions.Asia.Central Asia          0.495
		Geography.Regions.Asia.East Asia             0.654
		Geography.Regions.Asia.North Asia            0.203
		Geography.Regions.Asia.South Asia            0.828
		Geography.Regions.Asia.Southeast Asia        0.685
		Geography.Regions.Asia.West Asia             0.767
		Geography.Regions.Europe.Eastern Europe      0.747
		Geography.Regions.Europe.Europe*             0.738
		Geography.Regions.Europe.Northern Europe     0.689
		Geography.Regions.Europe.Southern Europe     0.639
		Geography.Regions.Europe.Western Europe      0.624
		Geography.Regions.Oceania                    0.802
		History and Society.Business and economics   0.289
		History and Society.Education                0.365
		History and Society.History                  0.248
		History and Society.Military and warfare     0.64
		History and Society.Politics and government  0.644
		History and Society.Society                  0.318
		History and Society.Transportation           0.803
		STEM.Biology                                 0.887
		STEM.Chemistry                               0.276
		STEM.Computing                               0.222
		STEM.Earth and environment                   0.632
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.242
		STEM.Mathematics                             0.214
		STEM.Medicine & Health                       0.534
		STEM.Physics                                 0.228
		STEM.STEM*                                   0.854
		STEM.Space                                   0.847
		STEM.Technology                              0.27
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}}, 'type': 'object'}

