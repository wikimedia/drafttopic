Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'population_rates': None, 'subsample': 1.0, 'n_iter_no_change': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'center': False, 'max_features': 'log2', 'multilabel': True, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'validation_fraction': 0.1, 'presort': 'auto', 'tol': 0.0001, 'max_depth': 5, 'min_samples_split': 2, 'init': None, 'warm_start': False, 'min_impurity_split': None, 'max_leaf_nodes': None, 'loss': 'deviance', 'n_estimators': 150, 'min_samples_leaf': 1, 'criterion': 'friedman_mse', 'min_impurity_decrease': 0.0, 'label_weights': {}, 'learning_rate': 0.1, 'scale': False}
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
			'Culture.Biography.Biography*'                 16717  -->  15035  1682  1141  45159
			'Culture.Biography.Women'                       4173  -->   3191   982   765  58079
			'Culture.Food and drink'                        1323  -->    995   328    77  61617
			'Culture.Internet culture'                      2946  -->   2374   572   191  59880
			'Culture.Linguistics'                           1384  -->   1054   330    77  61556
			'Culture.Literature'                            5277  -->   4037  1240   503  57237
			'Culture.Media.Books'                           1919  -->   1383   536   153  60945
			'Culture.Media.Entertainment'                   1876  -->   1020   856   165  60976
			'Culture.Media.Films'                           2307  -->   1909   398   141  60569
			'Culture.Media.Media*'                         14363  -->  12431  1932  1443  47211
			'Culture.Media.Music'                           2677  -->   2238   439   255  60085
			'Culture.Media.Radio'                           1174  -->    957   217    27  61816
			'Culture.Media.Software'                        1798  -->   1140   658   345  60874
			'Culture.Media.Television'                      2200  -->   1607   593   184  60633
			'Culture.Media.Video games'                     2078  -->   1881   197    39  60900
			'Culture.Performing arts'                       1334  -->    940   394   104  61579
			'Culture.Philosophy and religion'               2638  -->   1567  1071   299  60080
			'Culture.Sports'                                5843  -->   5334   509   278  56896
			'Culture.Visual arts.Architecture'              2565  -->   1931   634   291  60161
			'Culture.Visual arts.Comics and Anime'          1488  -->   1222   266   103  61426
			'Culture.Visual arts.Fashion'                   1188  -->    933   255    68  61761
			'Culture.Visual arts.Visual arts*'              5987  -->   4713  1274   585  56445
			'Geography.Geographical'                        3344  -->   2244  1100   278  59395
			'Geography.Regions.Africa.Africa*'              5693  -->   4994   699   195  57129
			'Geography.Regions.Africa.Central Africa'         28  -->      0    28    37  62952
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    925   189    30  61873
			'Geography.Regions.Africa.Northern Africa'      1266  -->    949   317    73  61678
			'Geography.Regions.Africa.Southern Africa'      1288  -->   1026   262    41  61688
			'Geography.Regions.Africa.Western Africa'       1152  -->    971   181    60  61805
			'Geography.Regions.Americas.Central America'    1326  -->    954   372    73  61618
			'Geography.Regions.Americas.North America'      7565  -->   5273  2292  1221  54231
			'Geography.Regions.Americas.South America'      1523  -->   1145   378   128  61366
			'Geography.Regions.Asia.Asia*'                 11060  -->   9583  1477   796  51161
			'Geography.Regions.Asia.Central Asia'           1163  -->    921   242    58  61796
			'Geography.Regions.Asia.East Asia'              2721  -->   2155   566   247  60049
			'Geography.Regions.Asia.North Asia'             1361  -->    934   427   187  61469
			'Geography.Regions.Asia.South Asia'             2438  -->   2107   331   111  60468
			'Geography.Regions.Asia.Southeast Asia'         1688  -->   1336   352    98  61231
			'Geography.Regions.Asia.West Asia'              2264  -->   1808   456   133  60620
			'Geography.Regions.Europe.Eastern Europe'       3083  -->   2422   661   300  59634
			'Geography.Regions.Europe.Europe*'             12415  -->   9688  2727  1834  48768
			'Geography.Regions.Europe.Northern Europe'      4244  -->   2929  1315   616  58157
			'Geography.Regions.Europe.Southern Europe'      2320  -->   1641   679   254  60443
			'Geography.Regions.Europe.Western Europe'       3160  -->   2105  1055   392  59465
			'Geography.Regions.Oceania'                     2537  -->   2084   453   125  60355
			'History and Society.Business and economics'    3430  -->   1762  1668   519  59068
			'History and Society.Education'                 2178  -->   1185   993   249  60590
			'History and Society.History'                   3217  -->   1466  1751   450  59350
			'History and Society.Military and warfare'      3977  -->   2902  1075   400  58640
			'History and Society.Politics and government'   4647  -->   2928  1719   530  57840
			'History and Society.Society'                   4057  -->   1690  2367   394  58566
			'History and Society.Transportation'            3604  -->   3131   473   239  59174
			'STEM.Biology'                                  2834  -->   2312   522   155  60028
			'STEM.Chemistry'                                1344  -->   1012   332   150  61523
			'STEM.Computing'                                2011  -->   1416   595   432  60574
			'STEM.Earth and environment'                    1683  -->   1202   481   110  61224
			'STEM.Engineering'                              2272  -->   1637   635   187  60558
			'STEM.Libraries & Information'                  1159  -->    714   445    53  61805
			'STEM.Mathematics'                              1121  -->    882   239    76  61820
			'STEM.Medicine & Health'                        1737  -->   1206   531   167  61113
			'STEM.Physics'                                  1206  -->    844   362   131  61680
			'STEM.STEM*'                                   16499  -->  14385  2114  1027  45491
			'STEM.Space'                                    1398  -->   1237   161    40  61579
			'STEM.Technology'                               3712  -->   2402  1310   584  58721
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
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.02
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.065
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.093
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.012
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.027
		History and Society.Society                  0.012
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.935
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.907
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.973
		History and Society.Society                  0.988
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.79, macro=0.735):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.765
		Culture.Food and drink                       0.752
		Culture.Internet culture                     0.806
		Culture.Linguistics                          0.762
		Culture.Literature                           0.765
		Culture.Media.Books                          0.721
		Culture.Media.Entertainment                  0.544
		Culture.Media.Films                          0.827
		Culture.Media.Media*                         0.865
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.815
		Culture.Media.Software                       0.634
		Culture.Media.Television                     0.73
		Culture.Media.Video games                    0.905
		Culture.Performing arts                      0.705
		Culture.Philosophy and religion              0.594
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.753
		Culture.Visual arts.Comics and Anime         0.821
		Culture.Visual arts.Fashion                  0.785
		Culture.Visual arts.Visual arts*             0.787
		Geography.Geographical                       0.671
		Geography.Regions.Africa.Africa*             0.877
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.83
		Geography.Regions.Africa.Northern Africa     0.75
		Geography.Regions.Africa.Southern Africa     0.797
		Geography.Regions.Africa.Western Africa      0.843
		Geography.Regions.Americas.Central America   0.719
		Geography.Regions.Americas.North America     0.697
		Geography.Regions.Americas.South America     0.752
		Geography.Regions.Asia.Asia*                 0.866
		Geography.Regions.Asia.Central Asia          0.792
		Geography.Regions.Asia.East Asia             0.792
		Geography.Regions.Asia.North Asia            0.686
		Geography.Regions.Asia.South Asia            0.864
		Geography.Regions.Asia.Southeast Asia        0.791
		Geography.Regions.Asia.West Asia             0.799
		Geography.Regions.Europe.Eastern Europe      0.786
		Geography.Regions.Europe.Europe*             0.78
		Geography.Regions.Europe.Northern Europe     0.69
		Geography.Regions.Europe.Southern Europe     0.707
		Geography.Regions.Europe.Western Europe      0.666
		Geography.Regions.Oceania                    0.821
		History and Society.Business and economics   0.514
		History and Society.Education                0.544
		History and Society.History                  0.456
		History and Society.Military and warfare     0.73
		History and Society.Politics and government  0.63
		History and Society.Society                  0.417
		History and Society.Transportation           0.869
		STEM.Biology                                 0.816
		STEM.Chemistry                               0.753
		STEM.Computing                               0.704
		STEM.Earth and environment                   0.714
		STEM.Engineering                             0.721
		STEM.Libraries & Information                 0.616
		STEM.Mathematics                             0.787
		STEM.Medicine & Health                       0.694
		STEM.Physics                                 0.7
		STEM.STEM*                                   0.872
		STEM.Space                                   0.885
		STEM.Technology                              0.647
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.714, macro=0.581):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.837
		Culture.Biography.Women                      0.465
		Culture.Food and drink                       0.598
		Culture.Internet culture                     0.471
		Culture.Linguistics                          0.818
		Culture.Literature                           0.58
		Culture.Media.Books                          0.538
		Culture.Media.Entertainment                  0.42
		Culture.Media.Films                          0.791
		Culture.Media.Media*                         0.645
		Culture.Media.Music                          0.829
		Culture.Media.Radio                          0.801
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.682
		Culture.Media.Video games                    0.787
		Culture.Performing arts                      0.548
		Culture.Philosophy and religion              0.564
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.626
		Culture.Visual arts.Comics and Anime         0.519
		Culture.Visual arts.Fashion                  0.366
		Culture.Visual arts.Visual arts*             0.589
		Geography.Geographical                       0.777
		Geography.Regions.Africa.Africa*             0.67
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.438
		Geography.Regions.Africa.Northern Africa     0.438
		Geography.Regions.Africa.Southern Africa     0.585
		Geography.Regions.Africa.Western Africa      0.373
		Geography.Regions.Americas.Central America   0.668
		Geography.Regions.Americas.North America     0.685
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.73
		Geography.Regions.Asia.Central Asia          0.423
		Geography.Regions.Asia.East Asia             0.691
		Geography.Regions.Asia.North Asia            0.173
		Geography.Regions.Asia.South Asia            0.879
		Geography.Regions.Asia.Southeast Asia        0.75
		Geography.Regions.Asia.West Asia             0.801
		Geography.Regions.Europe.Eastern Europe      0.671
		Geography.Regions.Europe.Europe*             0.64
		Geography.Regions.Europe.Northern Europe     0.675
		Geography.Regions.Europe.Southern Europe     0.691
		Geography.Regions.Europe.Western Europe      0.665
		Geography.Regions.Oceania                    0.859
		History and Society.Business and economics   0.376
		History and Society.Education                0.496
		History and Society.History                  0.399
		History and Society.Military and warfare     0.606
		History and Society.Politics and government  0.668
		History and Society.Society                  0.443
		History and Society.Transportation           0.768
		STEM.Biology                                 0.917
		STEM.Chemistry                               0.326
		STEM.Computing                               0.212
		STEM.Earth and environment                   0.645
		STEM.Engineering                             0.552
		STEM.Libraries & Information                 0.309
		STEM.Mathematics                             0.211
		STEM.Medicine & Health                       0.621
		STEM.Physics                                 0.219
		STEM.STEM*                                   0.746
		STEM.Space                                   0.892
		STEM.Technology                              0.253
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.994
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.578
		Culture.Food and drink                       0.666
		Culture.Internet culture                     0.595
		Culture.Linguistics                          0.789
		Culture.Literature                           0.66
		Culture.Media.Books                          0.616
		Culture.Media.Entertainment                  0.474
		Culture.Media.Films                          0.809
		Culture.Media.Media*                         0.739
		Culture.Media.Music                          0.832
		Culture.Media.Radio                          0.808
		Culture.Media.Software                       0.216
		Culture.Media.Television                     0.706
		Culture.Media.Video games                    0.842
		Culture.Performing arts                      0.616
		Culture.Philosophy and religion              0.578
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.636
		Culture.Visual arts.Fashion                  0.5
		Culture.Visual arts.Visual arts*             0.674
		Geography.Geographical                       0.72
		Geography.Regions.Africa.Africa*             0.76
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.574
		Geography.Regions.Africa.Northern Africa     0.553
		Geography.Regions.Africa.Southern Africa     0.675
		Geography.Regions.Africa.Western Africa      0.517
		Geography.Regions.Americas.Central America   0.693
		Geography.Regions.Americas.North America     0.691
		Geography.Regions.Americas.South America     0.723
		Geography.Regions.Asia.Asia*                 0.792
		Geography.Regions.Asia.Central Asia          0.551
		Geography.Regions.Asia.East Asia             0.738
		Geography.Regions.Asia.North Asia            0.276
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.77
		Geography.Regions.Asia.West Asia             0.8
		Geography.Regions.Europe.Eastern Europe      0.724
		Geography.Regions.Europe.Europe*             0.703
		Geography.Regions.Europe.Northern Europe     0.683
		Geography.Regions.Europe.Southern Europe     0.699
		Geography.Regions.Europe.Western Europe      0.666
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.434
		History and Society.Education                0.519
		History and Society.History                  0.425
		History and Society.Military and warfare     0.662
		History and Society.Politics and government  0.649
		History and Society.Society                  0.43
		History and Society.Transportation           0.815
		STEM.Biology                                 0.863
		STEM.Chemistry                               0.455
		STEM.Computing                               0.325
		STEM.Earth and environment                   0.678
		STEM.Engineering                             0.625
		STEM.Libraries & Information                 0.412
		STEM.Mathematics                             0.333
		STEM.Medicine & Health                       0.656
		STEM.Physics                                 0.334
		STEM.STEM*                                   0.804
		STEM.Space                                   0.888
		STEM.Technology                              0.364
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.973
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
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
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.987
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.981
		History and Society.Society                  0.986
		History and Society.Transportation           0.994
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.025
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.003
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.015
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.036
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.007
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.978, macro=0.975):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.984
		Culture.Literature                           0.98
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.977
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.99
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.984
		Culture.Philosophy and religion              0.97
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.986
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.988
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.569
		Geography.Regions.Africa.Eastern Africa      0.99
		Geography.Regions.Africa.Northern Africa     0.987
		Geography.Regions.Africa.Southern Africa     0.989
		Geography.Regions.Africa.Western Africa      0.987
		Geography.Regions.Americas.Central America   0.986
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.985
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.987
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.985
		Geography.Regions.Asia.West Asia             0.987
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.981
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.961
		History and Society.Education                0.97
		History and Society.History                  0.951
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.967
		History and Society.Society                  0.939
		History and Society.Transportation           0.987
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.989
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.982
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.98
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.977
		STEM.Space                                   0.993
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.8, macro=0.672):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.924
		Culture.Biography.Women                      0.589
		Culture.Food and drink                       0.69
		Culture.Internet culture                     0.778
		Culture.Linguistics                          0.811
		Culture.Literature                           0.725
		Culture.Media.Books                          0.661
		Culture.Media.Entertainment                  0.514
		Culture.Media.Films                          0.85
		Culture.Media.Media*                         0.852
		Culture.Media.Music                          0.897
		Culture.Media.Radio                          0.849
		Culture.Media.Software                       0.209
		Culture.Media.Television                     0.746
		Culture.Media.Video games                    0.929
		Culture.Performing arts                      0.649
		Culture.Philosophy and religion              0.55
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.769
		Culture.Visual arts.Comics and Anime         0.704
		Culture.Visual arts.Fashion                  0.518
		Culture.Visual arts.Visual arts*             0.752
		Geography.Geographical                       0.776
		Geography.Regions.Africa.Africa*             0.821
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.571
		Geography.Regions.Africa.Northern Africa     0.586
		Geography.Regions.Africa.Southern Africa     0.69
		Geography.Regions.Africa.Western Africa      0.48
		Geography.Regions.Americas.Central America   0.691
		Geography.Regions.Americas.North America     0.75
		Geography.Regions.Americas.South America     0.733
		Geography.Regions.Asia.Asia*                 0.856
		Geography.Regions.Asia.Central Asia          0.519
		Geography.Regions.Asia.East Asia             0.747
		Geography.Regions.Asia.North Asia            0.273
		Geography.Regions.Asia.South Asia            0.894
		Geography.Regions.Asia.Southeast Asia        0.761
		Geography.Regions.Asia.West Asia             0.858
		Geography.Regions.Europe.Eastern Europe      0.756
		Geography.Regions.Europe.Europe*             0.774
		Geography.Regions.Europe.Northern Europe     0.74
		Geography.Regions.Europe.Southern Europe     0.742
		Geography.Regions.Europe.Western Europe      0.706
		Geography.Regions.Oceania                    0.878
		History and Society.Business and economics   0.388
		History and Society.Education                0.471
		History and Society.History                  0.383
		History and Society.Military and warfare     0.728
		History and Society.Politics and government  0.708
		History and Society.Society                  0.402
		History and Society.Transportation           0.881
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.562
		STEM.Computing                               0.359
		STEM.Earth and environment                   0.717
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.411
		STEM.Mathematics                             0.582
		STEM.Medicine & Health                       0.687
		STEM.Physics                                 0.41
		STEM.STEM*                                   0.899
		STEM.Space                                   0.943
		STEM.Technology                              0.398
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}}, 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability'}

