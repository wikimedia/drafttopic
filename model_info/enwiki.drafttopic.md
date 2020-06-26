Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'min_impurity_decrease': 0.0, 'n_estimators': 150, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'random_state': None, 'min_impurity_split': None, 'loss': 'deviance', 'label_weights': {}, 'warm_start': False, 'presort': 'auto', 'scale': False, 'subsample': 1.0, 'population_rates': None, 'center': False, 'init': None, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'tol': 0.0001, 'min_samples_split': 2, 'validation_fraction': 0.1, 'n_iter_no_change': None, 'max_features': 'log2', 'verbose': 0, 'max_leaf_nodes': None, 'max_depth': 5, 'learning_rate': 0.1, 'multilabel': True}
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
	counts (n=60891):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16301  -->  13569  2732  1429  43161
			'Culture.Biography.Women'                       3904  -->   2649  1255   765  56222
			'Culture.Food and drink'                        1261  -->    768   493    80  59550
			'Culture.Internet culture'                      2689  -->   1876   813   220  57982
			'Culture.Linguistics'                           1225  -->    809   416   111  59555
			'Culture.Literature'                            4966  -->   3340  1626   524  55401
			'Culture.Media.Books'                           1782  -->   1168   614   201  58908
			'Culture.Media.Entertainment'                   1675  -->    699   976   191  59025
			'Culture.Media.Films'                           2282  -->   1731   551   192  58417
			'Culture.Media.Media*'                         13501  -->  10935  2566  1548  45842
			'Culture.Media.Music'                           2502  -->   1824   678   268  58121
			'Culture.Media.Radio'                           1092  -->    822   270    39  59760
			'Culture.Media.Software'                        1624  -->    795   829   324  58943
			'Culture.Media.Television'                      2046  -->   1340   706   209  58636
			'Culture.Media.Video games'                     1909  -->   1559   350    58  58924
			'Culture.Performing arts'                       1307  -->    752   555   106  59478
			'Culture.Philosophy and religion'               2543  -->   1272  1271   327  58021
			'Culture.Sports'                                5760  -->   5034   726   327  54804
			'Culture.Visual arts.Architecture'              2542  -->   1690   852   273  58076
			'Culture.Visual arts.Comics and Anime'          1418  -->   1013   405    97  59376
			'Culture.Visual arts.Fashion'                   1083  -->    635   448    73  59735
			'Culture.Visual arts.Visual arts*'              5684  -->   3818  1866   528  54679
			'Geography.Geographical'                        3318  -->   2095  1223   292  57281
			'Geography.Regions.Africa.Africa*'              6291  -->   5253  1038   367  54233
			'Geography.Regions.Africa.Central Africa'       1105  -->    797   308    50  59736
			'Geography.Regions.Africa.Eastern Africa'       1051  -->    812   239    37  59803
			'Geography.Regions.Africa.Northern Africa'      1241  -->    857   384    92  59558
			'Geography.Regions.Africa.Southern Africa'      1257  -->    911   346    57  59577
			'Geography.Regions.Africa.Western Africa'       1126  -->    862   264    69  59696
			'Geography.Regions.Americas.Central America'    1290  -->    830   460    99  59502
			'Geography.Regions.Americas.North America'      7440  -->   4741  2699  1183  52268
			'Geography.Regions.Americas.South America'      1482  -->   1058   424   136  59273
			'Geography.Regions.Asia.Asia*'                 11296  -->   9263  2033   842  48753
			'Geography.Regions.Asia.Central Asia'           1057  -->    756   301    48  59786
			'Geography.Regions.Asia.East Asia'              2639  -->   1903   736   258  57994
			'Geography.Regions.Asia.North Asia'             2021  -->   1349   672   206  58664
			'Geography.Regions.Asia.South Asia'             2318  -->   1837   481   137  58436
			'Geography.Regions.Asia.Southeast Asia'         1602  -->   1157   445   117  59172
			'Geography.Regions.Asia.West Asia'              2087  -->   1611   476   143  58661
			'Geography.Regions.Europe.Eastern Europe'       3409  -->   2530   879   274  57208
			'Geography.Regions.Europe.Europe*'             12489  -->   9173  3316  1786  46616
			'Geography.Regions.Europe.Northern Europe'      4047  -->   2586  1461   601  56243
			'Geography.Regions.Europe.Southern Europe'      2278  -->   1549   729   300  58313
			'Geography.Regions.Europe.Western Europe'       3042  -->   1968  1074   451  57398
			'Geography.Regions.Oceania'                     2133  -->   1623   510   137  58621
			'History and Society.Business and economics'    3214  -->   1256  1958   478  57199
			'History and Society.Education'                 2142  -->    834  1308   224  58525
			'History and Society.History'                   3008  -->   1036  1972   427  57456
			'History and Society.Military and warfare'      3128  -->   1912  1216   343  57420
			'History and Society.Politics and government'   2915  -->   1163  1752   369  57607
			'History and Society.Society'                   2729  -->    603  2126   212  57950
			'History and Society.Transportation'            3426  -->   2769   657   247  57218
			'STEM.Biology'                                  2746  -->   2168   578   138  58007
			'STEM.Chemistry'                                1196  -->    686   510   155  59540
			'STEM.Computing'                                1923  -->   1085   838   370  58598
			'STEM.Earth and environment'                    1571  -->    983   588   132  59188
			'STEM.Engineering'                              2112  -->   1386   726   172  58607
			'STEM.Libraries & Information'                  1103  -->    538   565    66  59722
			'STEM.Mathematics'                              1036  -->    547   489    70  59785
			'STEM.Medicine & Health'                        1645  -->    888   757   194  59052
			'STEM.Physics'                                  1153  -->    543   610   174  59564
			'STEM.STEM*'                                   15467  -->  12832  2635  1162  44262
			'STEM.Space'                                    1263  -->   1029   234    76  59552
			'STEM.Technology'                               3411  -->   1777  1634   613  56867
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.268         0.121
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.021         0.003
		Culture.Internet culture                        0.044         0.004
		Culture.Linguistics                             0.02          0.008
		Culture.Literature                              0.082         0.015
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.037         0.012
		Culture.Media.Media*                            0.222         0.055
		Culture.Media.Music                             0.041         0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.027         0.001
		Culture.Media.Television                        0.034         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.01
		Culture.Sports                                  0.095         0.061
		Culture.Visual arts.Architecture                0.042         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.054         0.021
		Geography.Regions.Africa.Africa*                0.103         0.009
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0.001
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.122         0.064
		Geography.Regions.Americas.South America        0.024         0.007
		Geography.Regions.Asia.Asia*                    0.186         0.053
		Geography.Regions.Asia.Central Asia             0.017         0.001
		Geography.Regions.Asia.East Asia                0.043         0.012
		Geography.Regions.Asia.North Asia               0.033         0.006
		Geography.Regions.Asia.South Asia               0.038         0.017
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.034         0.012
		Geography.Regions.Europe.Eastern Europe         0.056         0.018
		Geography.Regions.Europe.Europe*                0.205         0.082
		Geography.Regions.Europe.Northern Europe        0.066         0.029
		Geography.Regions.Europe.Southern Europe        0.037         0.014
		Geography.Regions.Europe.Western Europe         0.05          0.021
		Geography.Regions.Oceania                       0.035         0.017
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.035         0.008
		History and Society.History                     0.049         0.011
		History and Society.Military and warfare        0.051         0.015
		History and Society.Politics and government     0.048         0.016
		History and Society.Society                     0.045         0.008
		History and Society.Transportation              0.056         0.016
		STEM.Biology                                    0.045         0.035
		STEM.Chemistry                                  0.02          0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.035         0.006
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.254         0.066
		STEM.Space                                      0.021         0.004
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.051, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.129
		Culture.Biography.Women                      0.023
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.016
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.011
		History and Society.Military and warfare     0.015
		History and Society.Politics and government  0.013
		History and Society.Society                  0.005
		History and Society.Transportation           0.018
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.078
		STEM.Space                                   0.005
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.977
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.989
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.987
		History and Society.Society                  0.995
		History and Society.Transportation           0.982
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.922
		STEM.Space                                   0.995
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.724, macro=0.655):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.832
		Culture.Biography.Women                      0.679
		Culture.Food and drink                       0.609
		Culture.Internet culture                     0.698
		Culture.Linguistics                          0.66
		Culture.Literature                           0.673
		Culture.Media.Books                          0.655
		Culture.Media.Entertainment                  0.417
		Culture.Media.Films                          0.759
		Culture.Media.Media*                         0.81
		Culture.Media.Music                          0.729
		Culture.Media.Radio                          0.753
		Culture.Media.Software                       0.49
		Culture.Media.Television                     0.655
		Culture.Media.Video games                    0.817
		Culture.Performing arts                      0.575
		Culture.Philosophy and religion              0.5
		Culture.Sports                               0.874
		Culture.Visual arts.Architecture             0.665
		Culture.Visual arts.Comics and Anime         0.714
		Culture.Visual arts.Fashion                  0.586
		Culture.Visual arts.Visual arts*             0.672
		Geography.Geographical                       0.631
		Geography.Regions.Africa.Africa*             0.835
		Geography.Regions.Africa.Central Africa      0.721
		Geography.Regions.Africa.Eastern Africa      0.773
		Geography.Regions.Africa.Northern Africa     0.691
		Geography.Regions.Africa.Southern Africa     0.725
		Geography.Regions.Africa.Western Africa      0.766
		Geography.Regions.Americas.Central America   0.643
		Geography.Regions.Americas.North America     0.637
		Geography.Regions.Americas.South America     0.714
		Geography.Regions.Asia.Asia*                 0.82
		Geography.Regions.Asia.Central Asia          0.715
		Geography.Regions.Asia.East Asia             0.721
		Geography.Regions.Asia.North Asia            0.667
		Geography.Regions.Asia.South Asia            0.792
		Geography.Regions.Asia.Southeast Asia        0.722
		Geography.Regions.Asia.West Asia             0.772
		Geography.Regions.Europe.Eastern Europe      0.742
		Geography.Regions.Europe.Europe*             0.734
		Geography.Regions.Europe.Northern Europe     0.639
		Geography.Regions.Europe.Southern Europe     0.68
		Geography.Regions.Europe.Western Europe      0.647
		Geography.Regions.Oceania                    0.761
		History and Society.Business and economics   0.391
		History and Society.Education                0.389
		History and Society.History                  0.344
		History and Society.Military and warfare     0.611
		History and Society.Politics and government  0.399
		History and Society.Society                  0.221
		History and Society.Transportation           0.808
		STEM.Biology                                 0.79
		STEM.Chemistry                               0.574
		STEM.Computing                               0.564
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.656
		STEM.Libraries & Information                 0.488
		STEM.Mathematics                             0.528
		STEM.Medicine & Health                       0.54
		STEM.Physics                                 0.471
		STEM.STEM*                                   0.83
		STEM.Space                                   0.815
		STEM.Technology                              0.521
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
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
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.994
		History and Society.Society                  0.996
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.676, macro=0.546):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.782
		Culture.Biography.Women                      0.437
		Culture.Food and drink                       0.54
		Culture.Internet culture                     0.411
		Culture.Linguistics                          0.744
		Culture.Literature                           0.522
		Culture.Media.Books                          0.458
		Culture.Media.Entertainment                  0.341
		Culture.Media.Films                          0.732
		Culture.Media.Media*                         0.592
		Culture.Media.Music                          0.775
		Culture.Media.Radio                          0.731
		Culture.Media.Software                       0.106
		Culture.Media.Television                     0.625
		Culture.Media.Video games                    0.71
		Culture.Performing arts                      0.5
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.905
		Culture.Visual arts.Architecture             0.61
		Culture.Visual arts.Comics and Anime         0.515
		Culture.Visual arts.Fashion                  0.303
		Culture.Visual arts.Visual arts*             0.566
		Geography.Geographical                       0.731
		Geography.Regions.Africa.Africa*             0.518
		Geography.Regions.Africa.Central Africa      0.38
		Geography.Regions.Africa.Eastern Africa      0.388
		Geography.Regions.Africa.Northern Africa     0.379
		Geography.Regions.Africa.Southern Africa     0.501
		Geography.Regions.Africa.Western Africa      0.333
		Geography.Regions.Americas.Central America   0.575
		Geography.Regions.Americas.North America     0.662
		Geography.Regions.Americas.South America     0.685
		Geography.Regions.Asia.Asia*                 0.73
		Geography.Regions.Asia.Central Asia          0.418
		Geography.Regions.Asia.East Asia             0.669
		Geography.Regions.Asia.North Asia            0.521
		Geography.Regions.Asia.South Asia            0.852
		Geography.Regions.Asia.Southeast Asia        0.699
		Geography.Regions.Asia.West Asia             0.791
		Geography.Regions.Europe.Eastern Europe      0.746
		Geography.Regions.Europe.Europe*             0.639
		Geography.Regions.Europe.Northern Europe     0.646
		Geography.Regions.Europe.Southern Europe     0.653
		Geography.Regions.Europe.Western Europe      0.637
		Geography.Regions.Oceania                    0.846
		History and Society.Business and economics   0.319
		History and Society.Education                0.452
		History and Society.History                  0.342
		History and Society.Military and warfare     0.618
		History and Society.Politics and government  0.512
		History and Society.Society                  0.338
		History and Society.Transportation           0.758
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.274
		STEM.Computing                               0.204
		STEM.Earth and environment                   0.574
		STEM.Engineering                             0.567
		STEM.Libraries & Information                 0.234
		STEM.Mathematics                             0.174
		STEM.Medicine & Health                       0.519
		STEM.Physics                                 0.133
		STEM.STEM*                                   0.695
		STEM.Space                                   0.734
		STEM.Technology                              0.203
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.976
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.695, macro=0.583):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.807
		Culture.Biography.Women                      0.531
		Culture.Food and drink                       0.572
		Culture.Internet culture                     0.517
		Culture.Linguistics                          0.7
		Culture.Literature                           0.588
		Culture.Media.Books                          0.539
		Culture.Media.Entertainment                  0.375
		Culture.Media.Films                          0.745
		Culture.Media.Media*                         0.684
		Culture.Media.Music                          0.751
		Culture.Media.Radio                          0.742
		Culture.Media.Software                       0.174
		Culture.Media.Television                     0.64
		Culture.Media.Video games                    0.759
		Culture.Performing arts                      0.535
		Culture.Philosophy and religion              0.493
		Culture.Sports                               0.889
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.598
		Culture.Visual arts.Fashion                  0.4
		Culture.Visual arts.Visual arts*             0.615
		Geography.Geographical                       0.677
		Geography.Regions.Africa.Africa*             0.639
		Geography.Regions.Africa.Central Africa      0.498
		Geography.Regions.Africa.Eastern Africa      0.517
		Geography.Regions.Africa.Northern Africa     0.49
		Geography.Regions.Africa.Southern Africa     0.592
		Geography.Regions.Africa.Western Africa      0.464
		Geography.Regions.Americas.Central America   0.608
		Geography.Regions.Americas.North America     0.649
		Geography.Regions.Americas.South America     0.699
		Geography.Regions.Asia.Asia*                 0.772
		Geography.Regions.Asia.Central Asia          0.528
		Geography.Regions.Asia.East Asia             0.694
		Geography.Regions.Asia.North Asia            0.585
		Geography.Regions.Asia.South Asia            0.821
		Geography.Regions.Asia.Southeast Asia        0.71
		Geography.Regions.Asia.West Asia             0.782
		Geography.Regions.Europe.Eastern Europe      0.744
		Geography.Regions.Europe.Europe*             0.683
		Geography.Regions.Europe.Northern Europe     0.642
		Geography.Regions.Europe.Southern Europe     0.666
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.801
		History and Society.Business and economics   0.351
		History and Society.Education                0.418
		History and Society.History                  0.343
		History and Society.Military and warfare     0.614
		History and Society.Politics and government  0.449
		History and Society.Society                  0.267
		History and Society.Transportation           0.783
		STEM.Biology                                 0.851
		STEM.Chemistry                               0.371
		STEM.Computing                               0.3
		STEM.Earth and environment                   0.599
		STEM.Engineering                             0.608
		STEM.Libraries & Information                 0.316
		STEM.Mathematics                             0.262
		STEM.Medicine & Health                       0.529
		STEM.Physics                                 0.207
		STEM.STEM*                                   0.756
		STEM.Space                                   0.772
		STEM.Technology                              0.292
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.978
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
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.951
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.986
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.986
		History and Society.Education                0.991
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.984
		History and Society.Society                  0.99
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.965
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.032
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
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
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.007
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.006
		History and Society.Society                  0.004
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.965, macro=0.967):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.969
		Culture.Food and drink                       0.972
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.968
		Culture.Literature                           0.967
		Culture.Media.Books                          0.974
		Culture.Media.Entertainment                  0.959
		Culture.Media.Films                          0.977
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.975
		Culture.Media.Software                       0.973
		Culture.Media.Television                     0.97
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.946
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.974
		Culture.Visual arts.Comics and Anime         0.979
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.959
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.978
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.975
		Geography.Regions.Africa.Northern Africa     0.968
		Geography.Regions.Africa.Southern Africa     0.977
		Geography.Regions.Africa.Western Africa      0.981
		Geography.Regions.Americas.Central America   0.972
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.974
		Geography.Regions.Asia.North Asia            0.965
		Geography.Regions.Asia.South Asia            0.978
		Geography.Regions.Asia.Southeast Asia        0.971
		Geography.Regions.Asia.West Asia             0.978
		Geography.Regions.Europe.Eastern Europe      0.97
		Geography.Regions.Europe.Europe*             0.951
		Geography.Regions.Europe.Northern Europe     0.961
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.966
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.938
		History and Society.Education                0.943
		History and Society.History                  0.93
		History and Society.Military and warfare     0.962
		History and Society.Politics and government  0.934
		History and Society.Society                  0.881
		History and Society.Transportation           0.979
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.975
		STEM.Computing                               0.972
		STEM.Earth and environment                   0.97
		STEM.Engineering                             0.966
		STEM.Libraries & Information                 0.96
		STEM.Mathematics                             0.965
		STEM.Medicine & Health                       0.959
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.967
		STEM.Space                                   0.983
		STEM.Technology                              0.958
		-------------------------------------------  -----
	pr_auc (micro=0.726, macro=0.579):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.495
		Culture.Food and drink                       0.532
		Culture.Internet culture                     0.648
		Culture.Linguistics                          0.7
		Culture.Literature                           0.633
		Culture.Media.Books                          0.54
		Culture.Media.Entertainment                  0.305
		Culture.Media.Films                          0.733
		Culture.Media.Media*                         0.772
		Culture.Media.Music                          0.763
		Culture.Media.Radio                          0.779
		Culture.Media.Software                       0.141
		Culture.Media.Television                     0.617
		Culture.Media.Video games                    0.826
		Culture.Performing arts                      0.458
		Culture.Philosophy and religion              0.431
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.659
		Culture.Visual arts.Comics and Anime         0.614
		Culture.Visual arts.Fashion                  0.31
		Culture.Visual arts.Visual arts*             0.641
		Geography.Geographical                       0.734
		Geography.Regions.Africa.Africa*             0.663
		Geography.Regions.Africa.Central Africa      0.552
		Geography.Regions.Africa.Eastern Africa      0.431
		Geography.Regions.Africa.Northern Africa     0.469
		Geography.Regions.Africa.Southern Africa     0.568
		Geography.Regions.Africa.Western Africa      0.383
		Geography.Regions.Americas.Central America   0.563
		Geography.Regions.Americas.North America     0.71
		Geography.Regions.Americas.South America     0.707
		Geography.Regions.Asia.Asia*                 0.829
		Geography.Regions.Asia.Central Asia          0.572
		Geography.Regions.Asia.East Asia             0.723
		Geography.Regions.Asia.North Asia            0.557
		Geography.Regions.Asia.South Asia            0.837
		Geography.Regions.Asia.Southeast Asia        0.672
		Geography.Regions.Asia.West Asia             0.791
		Geography.Regions.Europe.Eastern Europe      0.766
		Geography.Regions.Europe.Europe*             0.728
		Geography.Regions.Europe.Northern Europe     0.668
		Geography.Regions.Europe.Southern Europe     0.661
		Geography.Regions.Europe.Western Europe      0.643
		Geography.Regions.Oceania                    0.827
		History and Society.Business and economics   0.26
		History and Society.Education                0.349
		History and Society.History                  0.262
		History and Society.Military and warfare     0.622
		History and Society.Politics and government  0.422
		History and Society.Society                  0.205
		History and Society.Transportation           0.817
		STEM.Biology                                 0.893
		STEM.Chemistry                               0.291
		STEM.Computing                               0.205
		STEM.Earth and environment                   0.604
		STEM.Engineering                             0.562
		STEM.Libraries & Information                 0.276
		STEM.Mathematics                             0.286
		STEM.Medicine & Health                       0.481
		STEM.Physics                                 0.137
		STEM.STEM*                                   0.839
		STEM.Space                                   0.809
		STEM.Technology                              0.285
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Media.Books': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

