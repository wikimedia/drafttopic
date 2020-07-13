Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'verbose': 0, 'max_leaf_nodes': None, 'subsample': 1.0, 'n_estimators': 150, 'scale': False, 'presort': 'auto', 'n_iter_no_change': None, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'warm_start': False, 'criterion': 'friedman_mse', 'tol': 0.0001, 'random_state': None, 'multilabel': True, 'min_samples_leaf': 1, 'label_weights': {}, 'learning_rate': 0.1, 'max_features': 'log2', 'init': None, 'min_weight_fraction_leaf': 0.0, 'center': False, 'min_samples_split': 2, 'min_impurity_split': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'validation_fraction': 0.1, 'population_rates': None}
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
	counts (n=59985):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13994  -->  12310  1684   891  45100
			'Culture.Biography.Women'                       5166  -->   4040  1126   800  54019
			'Culture.Food and drink'                        1365  -->    930   435   124  58496
			'Culture.Internet culture'                      3540  -->   2850   690   253  56192
			'Culture.Linguistics'                           1495  -->   1115   380    60  58430
			'Culture.Literature'                            5456  -->   4046  1410   512  54017
			'Culture.Media.Books'                           1402  -->    921   481   147  58436
			'Culture.Media.Entertainment'                   1931  -->    940   991   188  57866
			'Culture.Media.Films'                           2584  -->   1975   609   174  57227
			'Culture.Media.Media*'                         13074  -->  11123  1951  1322  45589
			'Culture.Media.Music'                           2914  -->   2409   505   180  56891
			'Culture.Media.Radio'                            299  -->    193   106    40  59646
			'Culture.Media.Software'                        2295  -->   1863   432   284  57406
			'Culture.Media.Television'                      1955  -->   1348   607   155  57875
			'Culture.Media.Video games'                     2120  -->   1918   202    57  57808
			'Culture.Performing arts'                       1357  -->    847   510   120  58508
			'Culture.Philosophy and religion'               2997  -->   1547  1450   268  56720
			'Culture.Sports'                                3884  -->   3382   502   120  55981
			'Culture.Visual arts.Architecture'              1827  -->   1279   548   179  57979
			'Culture.Visual arts.Comics and Anime'          2132  -->   1844   288   105  57748
			'Culture.Visual arts.Fashion'                   1484  -->   1203   281   104  58397
			'Culture.Visual arts.Visual arts*'              5932  -->   4393  1539   446  53607
			'Geography.Geographical'                        3989  -->   2499  1490   539  55457
			'Geography.Regions.Africa.Africa*'              5657  -->   4296  1361   475  53853
			'Geography.Regions.Africa.Central Africa'       1194  -->    737   457   127  58664
			'Geography.Regions.Africa.Eastern Africa'        449  -->    198   251    41  59495
			'Geography.Regions.Africa.Northern Africa'      1495  -->   1028   467   105  58385
			'Geography.Regions.Africa.Southern Africa'      1148  -->    755   393    81  58756
			'Geography.Regions.Africa.Western Africa'        707  -->    563   144    61  59217
			'Geography.Regions.Americas.Central America'    1586  -->    955   631   138  58261
			'Geography.Regions.Americas.North America'      5322  -->   3427  1895   569  54094
			'Geography.Regions.Americas.South America'      2216  -->   1630   586   201  57568
			'Geography.Regions.Asia.Asia*'                 13592  -->  11002  2590  1143  45250
			'Geography.Regions.Asia.Central Asia'           1193  -->    846   347    85  58707
			'Geography.Regions.Asia.East Asia'              5451  -->   4214  1237   448  54086
			'Geography.Regions.Asia.North Asia'             1641  -->   1134   507   208  58136
			'Geography.Regions.Asia.South Asia'             1968  -->   1508   460    80  57937
			'Geography.Regions.Asia.Southeast Asia'         2590  -->   1732   858   196  57199
			'Geography.Regions.Asia.West Asia'              2197  -->   1715   482    96  57692
			'Geography.Regions.Europe.Eastern Europe'       3543  -->   2752   791   283  56159
			'Geography.Regions.Europe.Europe*'             12445  -->   9743  2702  1224  46316
			'Geography.Regions.Europe.Northern Europe'      2797  -->   1707  1090   273  56915
			'Geography.Regions.Europe.Southern Europe'      2811  -->   2110   701   170  57004
			'Geography.Regions.Europe.Western Europe'       3952  -->   2966   986   263  55770
			'Geography.Regions.Oceania'                     2206  -->   1631   575   105  57674
			'History and Society.Business and economics'    3326  -->   1908  1418   333  56326
			'History and Society.Education'                 1615  -->    879   736   133  58237
			'History and Society.History'                   4419  -->   2268  2151   580  54986
			'History and Society.Military and warfare'      4968  -->   3745  1223   426  54591
			'History and Society.Politics and government'   4477  -->   2268  2209   472  55036
			'History and Society.Society'                   6007  -->   2694  3313   496  53482
			'History and Society.Transportation'            3523  -->   3175   348    95  56367
			'STEM.Biology'                                  7040  -->   6401   639   150  52795
			'STEM.Chemistry'                                1416  -->   1016   400   191  58378
			'STEM.Computing'                                2448  -->   1918   530   319  57218
			'STEM.Earth and environment'                    1681  -->   1101   580   125  58179
			'STEM.Engineering'                              2950  -->   2395   555   115  56920
			'STEM.Libraries & Information'                   485  -->    361   124    49  59451
			'STEM.Mathematics'                               923  -->    705   218    62  59000
			'STEM.Medicine & Health'                        1746  -->   1203   543   129  58110
			'STEM.Physics'                                  1338  -->    900   438   156  58491
			'STEM.STEM*'                                   20356  -->  18461  1895   984  38645
			'STEM.Space'                                    1585  -->   1388   197    41  58359
			'STEM.Technology'                               4218  -->   3027  1191   552  55215
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.121
		Culture.Biography.Women                         0.086         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.218         0.055
		Culture.Media.Music                             0.049         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.033         0.009
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
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.037         0.007
		Geography.Regions.Asia.Asia*                    0.227         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.091         0.012
		Geography.Regions.Asia.North Asia               0.027         0.006
		Geography.Regions.Asia.South Asia               0.033         0.017
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.059         0.018
		Geography.Regions.Europe.Europe*                0.207         0.082
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.047         0.014
		Geography.Regions.Europe.Western Europe         0.066         0.021
		Geography.Regions.Oceania                       0.037         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.083         0.015
		History and Society.Politics and government     0.075         0.016
		History and Society.Society                     0.1           0.008
		History and Society.Transportation              0.059         0.016
		STEM.Biology                                    0.117         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.339         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.05, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.124
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.074
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.009
		Geography.Regions.Asia.Asia*                 0.066
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.019
		Geography.Regions.Europe.Europe*             0.088
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.011
		History and Society.Education                0.007
		History and Society.History                  0.016
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.017
		History and Society.Society                  0.013
		History and Society.Transportation           0.016
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.004
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.95, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.926
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.991
		Geography.Regions.Asia.Asia*                 0.934
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.912
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.983
		History and Society.Society                  0.987
		History and Society.Transportation           0.984
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.996
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.773, macro=0.72):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.88
		Culture.Biography.Women                      0.782
		Culture.Food and drink                       0.681
		Culture.Internet culture                     0.805
		Culture.Linguistics                          0.746
		Culture.Literature                           0.742
		Culture.Media.Books                          0.657
		Culture.Media.Entertainment                  0.487
		Culture.Media.Films                          0.764
		Culture.Media.Media*                         0.851
		Culture.Media.Music                          0.827
		Culture.Media.Radio                          0.645
		Culture.Media.Software                       0.812
		Culture.Media.Television                     0.69
		Culture.Media.Video games                    0.905
		Culture.Performing arts                      0.624
		Culture.Philosophy and religion              0.516
		Culture.Sports                               0.871
		Culture.Visual arts.Architecture             0.7
		Culture.Visual arts.Comics and Anime         0.865
		Culture.Visual arts.Fashion                  0.811
		Culture.Visual arts.Visual arts*             0.741
		Geography.Geographical                       0.626
		Geography.Regions.Africa.Africa*             0.759
		Geography.Regions.Africa.Central Africa      0.617
		Geography.Regions.Africa.Eastern Africa      0.441
		Geography.Regions.Africa.Northern Africa     0.688
		Geography.Regions.Africa.Southern Africa     0.658
		Geography.Regions.Africa.Western Africa      0.796
		Geography.Regions.Americas.Central America   0.602
		Geography.Regions.Americas.North America     0.644
		Geography.Regions.Americas.South America     0.736
		Geography.Regions.Asia.Asia*                 0.809
		Geography.Regions.Asia.Central Asia          0.709
		Geography.Regions.Asia.East Asia             0.773
		Geography.Regions.Asia.North Asia            0.691
		Geography.Regions.Asia.South Asia            0.766
		Geography.Regions.Asia.Southeast Asia        0.669
		Geography.Regions.Asia.West Asia             0.781
		Geography.Regions.Europe.Eastern Europe      0.777
		Geography.Regions.Europe.Europe*             0.783
		Geography.Regions.Europe.Northern Europe     0.61
		Geography.Regions.Europe.Southern Europe     0.751
		Geography.Regions.Europe.Western Europe      0.751
		Geography.Regions.Oceania                    0.739
		History and Society.Business and economics   0.574
		History and Society.Education                0.544
		History and Society.History                  0.513
		History and Society.Military and warfare     0.754
		History and Society.Politics and government  0.507
		History and Society.Society                  0.448
		History and Society.Transportation           0.901
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.718
		STEM.Computing                               0.783
		STEM.Earth and environment                   0.655
		STEM.Engineering                             0.812
		STEM.Libraries & Information                 0.744
		STEM.Mathematics                             0.764
		STEM.Medicine & Health                       0.689
		STEM.Physics                                 0.673
		STEM.STEM*                                   0.907
		STEM.Space                                   0.876
		STEM.Technology                              0.718
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.99
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.724, macro=0.57):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.863
		Culture.Biography.Women                      0.451
		Culture.Food and drink                       0.454
		Culture.Internet culture                     0.404
		Culture.Linguistics                          0.856
		Culture.Literature                           0.546
		Culture.Media.Books                          0.534
		Culture.Media.Entertainment                  0.376
		Culture.Media.Films                          0.748
		Culture.Media.Media*                         0.639
		Culture.Media.Music                          0.85
		Culture.Media.Radio                          0.694
		Culture.Media.Software                       0.179
		Culture.Media.Television                     0.7
		Culture.Media.Video games                    0.73
		Culture.Performing arts                      0.485
		Culture.Philosophy and religion              0.537
		Culture.Sports                               0.964
		Culture.Visual arts.Architecture             0.715
		Culture.Visual arts.Comics and Anime         0.536
		Culture.Visual arts.Fashion                  0.292
		Culture.Visual arts.Visual arts*             0.625
		Geography.Geographical                       0.587
		Geography.Regions.Africa.Africa*             0.429
		Geography.Regions.Africa.Central Africa      0.169
		Geography.Regions.Africa.Eastern Africa      0.245
		Geography.Regions.Africa.Northern Africa     0.343
		Geography.Regions.Africa.Southern Africa     0.387
		Geography.Regions.Africa.Western Africa      0.368
		Geography.Regions.Americas.Central America   0.471
		Geography.Regions.Americas.North America     0.808
		Geography.Regions.Americas.South America     0.595
		Geography.Regions.Asia.Asia*                 0.648
		Geography.Regions.Asia.Central Asia          0.283
		Geography.Regions.Asia.East Asia             0.539
		Geography.Regions.Asia.North Asia            0.525
		Geography.Regions.Asia.South Asia            0.904
		Geography.Regions.Asia.Southeast Asia        0.554
		Geography.Regions.Asia.West Asia             0.849
		Geography.Regions.Europe.Eastern Europe      0.745
		Geography.Regions.Europe.Europe*             0.73
		Geography.Regions.Europe.Northern Europe     0.794
		Geography.Regions.Europe.Southern Europe     0.781
		Geography.Regions.Europe.Western Europe      0.772
		Geography.Regions.Oceania                    0.873
		History and Society.Business and economics   0.492
		History and Society.Education                0.658
		History and Society.History                  0.354
		History and Society.Military and warfare     0.604
		History and Society.Politics and government  0.499
		History and Society.Society                  0.291
		History and Society.Transportation           0.899
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.273
		STEM.Computing                               0.288
		STEM.Earth and environment                   0.594
		STEM.Engineering                             0.701
		STEM.Libraries & Information                 0.385
		STEM.Mathematics                             0.253
		STEM.Medicine & Health                       0.67
		STEM.Physics                                 0.193
		STEM.STEM*                                   0.72
		STEM.Space                                   0.843
		STEM.Technology                              0.275
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
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
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.74, macro=0.616):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.572
		Culture.Food and drink                       0.545
		Culture.Internet culture                     0.538
		Culture.Linguistics                          0.797
		Culture.Literature                           0.629
		Culture.Media.Books                          0.589
		Culture.Media.Entertainment                  0.424
		Culture.Media.Films                          0.756
		Culture.Media.Media*                         0.73
		Culture.Media.Music                          0.838
		Culture.Media.Radio                          0.669
		Culture.Media.Software                       0.293
		Culture.Media.Television                     0.695
		Culture.Media.Video games                    0.808
		Culture.Performing arts                      0.546
		Culture.Philosophy and religion              0.527
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.707
		Culture.Visual arts.Comics and Anime         0.662
		Culture.Visual arts.Fashion                  0.43
		Culture.Visual arts.Visual arts*             0.678
		Geography.Geographical                       0.606
		Geography.Regions.Africa.Africa*             0.548
		Geography.Regions.Africa.Central Africa      0.265
		Geography.Regions.Africa.Eastern Africa      0.315
		Geography.Regions.Africa.Northern Africa     0.458
		Geography.Regions.Africa.Southern Africa     0.487
		Geography.Regions.Africa.Western Africa      0.504
		Geography.Regions.Americas.Central America   0.529
		Geography.Regions.Americas.North America     0.717
		Geography.Regions.Americas.South America     0.658
		Geography.Regions.Asia.Asia*                 0.72
		Geography.Regions.Asia.Central Asia          0.405
		Geography.Regions.Asia.East Asia             0.635
		Geography.Regions.Asia.North Asia            0.596
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.606
		Geography.Regions.Asia.West Asia             0.813
		Geography.Regions.Europe.Eastern Europe      0.76
		Geography.Regions.Europe.Europe*             0.755
		Geography.Regions.Europe.Northern Europe     0.69
		Geography.Regions.Europe.Southern Europe     0.766
		Geography.Regions.Europe.Western Europe      0.761
		Geography.Regions.Oceania                    0.801
		History and Society.Business and economics   0.53
		History and Society.Education                0.596
		History and Society.History                  0.419
		History and Society.Military and warfare     0.671
		History and Society.Politics and government  0.503
		History and Society.Society                  0.353
		History and Society.Transportation           0.9
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.396
		STEM.Computing                               0.421
		STEM.Earth and environment                   0.623
		STEM.Engineering                             0.753
		STEM.Libraries & Information                 0.507
		STEM.Mathematics                             0.381
		STEM.Medicine & Health                       0.68
		STEM.Physics                                 0.3
		STEM.STEM*                                   0.802
		STEM.Space                                   0.859
		STEM.Technology                              0.397
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
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
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
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
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.98, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.984
		History and Society.Society                  0.986
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.01
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.025
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.026
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.005
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.974, macro=0.975):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.974
		Culture.Literature                           0.975
		Culture.Media.Books                          0.977
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.963
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.978
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.947
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.975
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.953
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.972
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.972
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.977
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.973
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.967
		History and Society.Education                0.967
		History and Society.History                  0.947
		History and Society.Military and warfare     0.975
		History and Society.Politics and government  0.949
		History and Society.Society                  0.925
		History and Society.Transportation           0.987
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.984
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.983
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.979
		STEM.Space                                   0.99
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.787, macro=0.622):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.587
		Culture.Food and drink                       0.572
		Culture.Internet culture                     0.609
		Culture.Linguistics                          0.827
		Culture.Literature                           0.685
		Culture.Media.Books                          0.542
		Culture.Media.Entertainment                  0.362
		Culture.Media.Films                          0.788
		Culture.Media.Media*                         0.818
		Culture.Media.Music                          0.879
		Culture.Media.Radio                          0.451
		Culture.Media.Software                       0.289
		Culture.Media.Television                     0.711
		Culture.Media.Video games                    0.847
		Culture.Performing arts                      0.494
		Culture.Philosophy and religion              0.494
		Culture.Sports                               0.948
		Culture.Visual arts.Architecture             0.735
		Culture.Visual arts.Comics and Anime         0.788
		Culture.Visual arts.Fashion                  0.37
		Culture.Visual arts.Visual arts*             0.724
		Geography.Geographical                       0.635
		Geography.Regions.Africa.Africa*             0.568
		Geography.Regions.Africa.Central Africa      0.206
		Geography.Regions.Africa.Eastern Africa      0.133
		Geography.Regions.Africa.Northern Africa     0.395
		Geography.Regions.Africa.Southern Africa     0.391
		Geography.Regions.Africa.Western Africa      0.458
		Geography.Regions.Americas.Central America   0.451
		Geography.Regions.Americas.North America     0.806
		Geography.Regions.Americas.South America     0.626
		Geography.Regions.Asia.Asia*                 0.786
		Geography.Regions.Asia.Central Asia          0.458
		Geography.Regions.Asia.East Asia             0.619
		Geography.Regions.Asia.North Asia            0.536
		Geography.Regions.Asia.South Asia            0.884
		Geography.Regions.Asia.Southeast Asia        0.598
		Geography.Regions.Asia.West Asia             0.852
		Geography.Regions.Europe.Eastern Europe      0.785
		Geography.Regions.Europe.Europe*             0.836
		Geography.Regions.Europe.Northern Europe     0.735
		Geography.Regions.Europe.Southern Europe     0.812
		Geography.Regions.Europe.Western Europe      0.803
		Geography.Regions.Oceania                    0.841
		History and Society.Business and economics   0.539
		History and Society.Education                0.59
		History and Society.History                  0.37
		History and Society.Military and warfare     0.723
		History and Society.Politics and government  0.531
		History and Society.Society                  0.334
		History and Society.Transportation           0.938
		STEM.Biology                                 0.959
		STEM.Chemistry                               0.374
		STEM.Computing                               0.372
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.835
		STEM.Libraries & Information                 0.329
		STEM.Mathematics                             0.423
		STEM.Medicine & Health                       0.708
		STEM.Physics                                 0.239
		STEM.STEM*                                   0.896
		STEM.Space                                   0.906
		STEM.Technology                              0.454
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}}

