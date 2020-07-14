Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'random_state': None, 'presort': 'deprecated', 'min_impurity_decrease': 0.0, 'multilabel': True, 'ccp_alpha': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_leaf': 1, 'tol': 0.0001, 'center': False, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'scale': False, 'population_rates': None, 'criterion': 'friedman_mse', 'learning_rate': 0.1, 'validation_fraction': 0.1, 'max_depth': 5, 'n_estimators': 150, 'verbose': 0, 'subsample': 1.0, 'label_weights': {}, 'warm_start': False, 'max_leaf_nodes': None, 'init': None, 'min_impurity_split': None, 'max_features': 'log2', 'n_iter_no_change': None, 'min_samples_split': 2}
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
	counts (n=63509):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 27100  -->  26001  1099   877  35532
			'Culture.Biography.Women'                       6315  -->   4620  1695   904  56290
			'Culture.Food and drink'                        1386  -->    877   509   122  62001
			'Culture.Internet culture'                      3384  -->   2756   628   211  59914
			'Culture.Linguistics'                           1445  -->    939   506   101  61963
			'Culture.Literature'                            5803  -->   4181  1622   552  57154
			'Culture.Media.Books'                           1554  -->   1150   404   114  61841
			'Culture.Media.Entertainment'                   2113  -->   1002  1111   259  61137
			'Culture.Media.Films'                           2128  -->   1700   428    94  61287
			'Culture.Media.Media*'                         14066  -->  11731  2335  1565  47878
			'Culture.Media.Music'                           2797  -->   2089   708   303  60409
			'Culture.Media.Radio'                           1137  -->    498   639   108  62264
			'Culture.Media.Software'                        2101  -->   1523   578   320  61088
			'Culture.Media.Television'                      2253  -->   1268   985   215  61041
			'Culture.Media.Video games'                     2193  -->   1960   233    50  61266
			'Culture.Performing arts'                       1484  -->    760   724   146  61879
			'Culture.Philosophy and religion'               3448  -->   1666  1782   350  59711
			'Culture.Sports'                                8610  -->   7867   743   352  54547
			'Culture.Visual arts.Architecture'              1861  -->   1214   647   188  61460
			'Culture.Visual arts.Comics and Anime'          1848  -->   1449   399    93  61568
			'Culture.Visual arts.Fashion'                   1317  -->    926   391    83  62109
			'Culture.Visual arts.Visual arts*'              5874  -->   4186  1688   434  57201
			'Geography.Geographical'                        3642  -->   2591  1051   377  59490
			'Geography.Regions.Africa.Africa*'              6510  -->   5208  1302   435  56564
			'Geography.Regions.Africa.Central Africa'       1122  -->    795   327    66  62321
			'Geography.Regions.Africa.Eastern Africa'        973  -->    647   326    53  62483
			'Geography.Regions.Africa.Northern Africa'      2129  -->   1536   593   225  61155
			'Geography.Regions.Africa.Southern Africa'      1197  -->    897   300    69  62243
			'Geography.Regions.Africa.Western Africa'        756  -->    556   200    43  62710
			'Geography.Regions.Americas.Central America'    1367  -->    841   526    78  62064
			'Geography.Regions.Americas.North America'      8359  -->   5633  2726  2158  52992
			'Geography.Regions.Americas.South America'      1696  -->   1246   450   121  61692
			'Geography.Regions.Asia.Asia*'                 12021  -->  10021  2000   917  50571
			'Geography.Regions.Asia.Central Asia'           1198  -->    857   341    63  62248
			'Geography.Regions.Asia.East Asia'              2922  -->   2090   832   256  60331
			'Geography.Regions.Asia.North Asia'             1515  -->   1025   490   192  61802
			'Geography.Regions.Asia.South Asia'             1955  -->   1489   466    70  61484
			'Geography.Regions.Asia.Southeast Asia'         1549  -->   1122   427    64  61896
			'Geography.Regions.Asia.West Asia'              4115  -->   3347   768   293  59101
			'Geography.Regions.Europe.Eastern Europe'       2860  -->   2104   756   237  60412
			'Geography.Regions.Europe.Europe*'             13100  -->  10242  2858  1993  48416
			'Geography.Regions.Europe.Northern Europe'      4039  -->   2604  1435   647  58823
			'Geography.Regions.Europe.Southern Europe'      2863  -->   2006   857   289  60357
			'Geography.Regions.Europe.Western Europe'       4084  -->   3070  1014   569  58856
			'Geography.Regions.Oceania'                     2283  -->   1847   436    60  61166
			'History and Society.Business and economics'    3611  -->   1966  1645   458  59440
			'History and Society.Education'                 2059  -->    901  1158   174  61276
			'History and Society.History'                   4740  -->   2063  2677   698  58071
			'History and Society.Military and warfare'      4742  -->   3239  1503   434  58333
			'History and Society.Politics and government'   5471  -->   3251  2220   643  57395
			'History and Society.Society'                   6099  -->   2502  3597   549  56861
			'History and Society.Transportation'            3249  -->   2747   502   158  60102
			'STEM.Biology'                                  3025  -->   2267   758   211  60273
			'STEM.Chemistry'                                1516  -->   1096   420   135  61858
			'STEM.Computing'                                2434  -->   1783   651   393  60682
			'STEM.Earth and environment'                    1702  -->   1013   689   206  61601
			'STEM.Engineering'                              2883  -->   2034   849   249  60377
			'STEM.Libraries & Information'                  1186  -->    785   401    61  62262
			'STEM.Mathematics'                              1176  -->    768   408    72  62261
			'STEM.Medicine & Health'                        2280  -->   1544   736   212  61017
			'STEM.Physics'                                  1470  -->    940   530   213  61826
			'STEM.STEM*'                                   18041  -->  15639  2402  1086  44382
			'STEM.Space'                                    1751  -->   1520   231    60  61698
			'STEM.Technology'                               4518  -->   3048  1470   667  58324
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.427         0.123
		Culture.Biography.Women                         0.099         0.015
		Culture.Food and drink                          0.022         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.023         0.007
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.034         0.011
		Culture.Media.Media*                            0.221         0.058
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.033         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.136         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.029         0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.092         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.103         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0
		Geography.Regions.Africa.Northern Africa        0.034         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.132         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.189         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.024         0.006
		Geography.Regions.Asia.West Asia                0.065         0.011
		Geography.Regions.Europe.Eastern Europe         0.045         0.013
		Geography.Regions.Europe.Europe*                0.206         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.064         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.057         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.075         0.014
		History and Society.Politics and government     0.086         0.028
		History and Society.Society                     0.096         0.013
		History and Society.Transportation              0.051         0.015
		STEM.Biology                                    0.048         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.038         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.284         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.071         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.139
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.071
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.014
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.08
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.096
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.028
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.92
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.904
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.972
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.771, macro=0.699):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.959
		Culture.Biography.Women                      0.732
		Culture.Food and drink                       0.633
		Culture.Internet culture                     0.814
		Culture.Linguistics                          0.65
		Culture.Literature                           0.72
		Culture.Media.Books                          0.74
		Culture.Media.Entertainment                  0.474
		Culture.Media.Films                          0.799
		Culture.Media.Media*                         0.834
		Culture.Media.Music                          0.747
		Culture.Media.Radio                          0.438
		Culture.Media.Software                       0.725
		Culture.Media.Television                     0.563
		Culture.Media.Video games                    0.894
		Culture.Performing arts                      0.512
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.652
		Culture.Visual arts.Comics and Anime         0.784
		Culture.Visual arts.Fashion                  0.703
		Culture.Visual arts.Visual arts*             0.713
		Geography.Geographical                       0.711
		Geography.Regions.Africa.Africa*             0.8
		Geography.Regions.Africa.Central Africa      0.709
		Geography.Regions.Africa.Eastern Africa      0.665
		Geography.Regions.Africa.Northern Africa     0.721
		Geography.Regions.Africa.Southern Africa     0.749
		Geography.Regions.Africa.Western Africa      0.735
		Geography.Regions.Americas.Central America   0.615
		Geography.Regions.Americas.North America     0.674
		Geography.Regions.Americas.South America     0.735
		Geography.Regions.Asia.Asia*                 0.834
		Geography.Regions.Asia.Central Asia          0.715
		Geography.Regions.Asia.East Asia             0.715
		Geography.Regions.Asia.North Asia            0.677
		Geography.Regions.Asia.South Asia            0.762
		Geography.Regions.Asia.Southeast Asia        0.724
		Geography.Regions.Asia.West Asia             0.813
		Geography.Regions.Europe.Eastern Europe      0.736
		Geography.Regions.Europe.Europe*             0.782
		Geography.Regions.Europe.Northern Europe     0.645
		Geography.Regions.Europe.Southern Europe     0.701
		Geography.Regions.Europe.Western Europe      0.752
		Geography.Regions.Oceania                    0.809
		History and Society.Business and economics   0.544
		History and Society.Education                0.438
		History and Society.History                  0.435
		History and Society.Military and warfare     0.683
		History and Society.Politics and government  0.594
		History and Society.Society                  0.41
		History and Society.Transportation           0.845
		STEM.Biology                                 0.749
		STEM.Chemistry                               0.723
		STEM.Computing                               0.733
		STEM.Earth and environment                   0.595
		STEM.Engineering                             0.706
		STEM.Libraries & Information                 0.662
		STEM.Mathematics                             0.653
		STEM.Medicine & Health                       0.677
		STEM.Physics                                 0.639
		STEM.STEM*                                   0.867
		STEM.Space                                   0.868
		STEM.Technology                              0.675
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.683, macro=0.538):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.848
		Culture.Biography.Women                      0.406
		Culture.Food and drink                       0.443
		Culture.Internet culture                     0.449
		Culture.Linguistics                          0.747
		Culture.Literature                           0.542
		Culture.Media.Books                          0.619
		Culture.Media.Entertainment                  0.288
		Culture.Media.Films                          0.847
		Culture.Media.Media*                         0.621
		Culture.Media.Music                          0.786
		Culture.Media.Radio                          0.353
		Culture.Media.Software                       0.156
		Culture.Media.Television                     0.588
		Culture.Media.Video games                    0.742
		Culture.Performing arts                      0.386
		Culture.Philosophy and religion              0.472
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.534
		Culture.Visual arts.Fashion                  0.299
		Culture.Visual arts.Visual arts*             0.638
		Geography.Geographical                       0.732
		Geography.Regions.Africa.Africa*             0.452
		Geography.Regions.Africa.Central Africa      0.297
		Geography.Regions.Africa.Eastern Africa      0.263
		Geography.Regions.Africa.Northern Africa     0.195
		Geography.Regions.Africa.Southern Africa     0.443
		Geography.Regions.Africa.Western Africa      0.423
		Geography.Regions.Americas.Central America   0.619
		Geography.Regions.Americas.North America     0.542
		Geography.Regions.Americas.South America     0.704
		Geography.Regions.Asia.Asia*                 0.691
		Geography.Regions.Asia.Central Asia          0.38
		Geography.Regions.Asia.East Asia             0.661
		Geography.Regions.Asia.North Asia            0.168
		Geography.Regions.Asia.South Asia            0.912
		Geography.Regions.Asia.Southeast Asia        0.809
		Geography.Regions.Asia.West Asia             0.645
		Geography.Regions.Europe.Eastern Europe      0.71
		Geography.Regions.Europe.Europe*             0.62
		Geography.Regions.Europe.Northern Europe     0.651
		Geography.Regions.Europe.Southern Europe     0.66
		Geography.Regions.Europe.Western Europe      0.605
		Geography.Regions.Oceania                    0.927
		History and Society.Business and economics   0.42
		History and Society.Education                0.534
		History and Society.History                  0.286
		History and Society.Military and warfare     0.569
		History and Society.Politics and government  0.609
		History and Society.Society                  0.354
		History and Society.Transportation           0.832
		STEM.Biology                                 0.882
		STEM.Chemistry                               0.341
		STEM.Computing                               0.235
		STEM.Earth and environment                   0.449
		STEM.Engineering                             0.475
		STEM.Libraries & Information                 0.296
		STEM.Mathematics                             0.191
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.137
		STEM.STEM*                                   0.729
		STEM.Space                                   0.844
		STEM.Technology                              0.235
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.994
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.991
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
	f1 (micro=0.719, macro=0.588):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.9
		Culture.Biography.Women                      0.522
		Culture.Food and drink                       0.521
		Culture.Internet culture                     0.579
		Culture.Linguistics                          0.695
		Culture.Literature                           0.619
		Culture.Media.Books                          0.674
		Culture.Media.Entertainment                  0.358
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.712
		Culture.Media.Music                          0.766
		Culture.Media.Radio                          0.391
		Culture.Media.Software                       0.257
		Culture.Media.Television                     0.575
		Culture.Media.Video games                    0.811
		Culture.Performing arts                      0.44
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.673
		Culture.Visual arts.Comics and Anime         0.635
		Culture.Visual arts.Fashion                  0.419
		Culture.Visual arts.Visual arts*             0.673
		Geography.Geographical                       0.721
		Geography.Regions.Africa.Africa*             0.577
		Geography.Regions.Africa.Central Africa      0.419
		Geography.Regions.Africa.Eastern Africa      0.377
		Geography.Regions.Africa.Northern Africa     0.307
		Geography.Regions.Africa.Southern Africa     0.557
		Geography.Regions.Africa.Western Africa      0.537
		Geography.Regions.Americas.Central America   0.617
		Geography.Regions.Americas.North America     0.601
		Geography.Regions.Americas.South America     0.719
		Geography.Regions.Asia.Asia*                 0.755
		Geography.Regions.Asia.Central Asia          0.496
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.269
		Geography.Regions.Asia.South Asia            0.83
		Geography.Regions.Asia.Southeast Asia        0.764
		Geography.Regions.Asia.West Asia             0.72
		Geography.Regions.Europe.Eastern Europe      0.723
		Geography.Regions.Europe.Europe*             0.691
		Geography.Regions.Europe.Northern Europe     0.648
		Geography.Regions.Europe.Southern Europe     0.68
		Geography.Regions.Europe.Western Europe      0.671
		Geography.Regions.Oceania                    0.864
		History and Society.Business and economics   0.475
		History and Society.Education                0.481
		History and Society.History                  0.345
		History and Society.Military and warfare     0.621
		History and Society.Politics and government  0.601
		History and Society.Society                  0.38
		History and Society.Transportation           0.838
		STEM.Biology                                 0.81
		STEM.Chemistry                               0.464
		STEM.Computing                               0.356
		STEM.Earth and environment                   0.512
		STEM.Engineering                             0.568
		STEM.Libraries & Information                 0.409
		STEM.Mathematics                             0.295
		STEM.Medicine & Health                       0.611
		STEM.Physics                                 0.225
		STEM.STEM*                                   0.792
		STEM.Space                                   0.856
		STEM.Technology                              0.349
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.978
		History and Society.Society                  0.983
		History and Society.Transportation           0.995
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.969
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.039
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.04
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.011
		History and Society.Society                  0.01
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.968
		Culture.Literature                           0.972
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.962
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.965
		Culture.Media.Software                       0.984
		Culture.Media.Television                     0.973
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.942
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.983
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.969
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.977
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.977
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.977
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.973
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.978
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.979
		Geography.Regions.Asia.Southeast Asia        0.977
		Geography.Regions.Asia.West Asia             0.98
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.958
		History and Society.Education                0.952
		History and Society.History                  0.936
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.95
		History and Society.Society                  0.913
		History and Society.Transportation           0.982
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.986
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.967
		STEM.Engineering                             0.975
		STEM.Libraries & Information                 0.97
		STEM.Mathematics                             0.975
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.98
		STEM.STEM*                                   0.974
		STEM.Space                                   0.989
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.756, macro=0.591):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.946
		Culture.Biography.Women                      0.477
		Culture.Food and drink                       0.524
		Culture.Internet culture                     0.734
		Culture.Linguistics                          0.707
		Culture.Literature                           0.68
		Culture.Media.Books                          0.648
		Culture.Media.Entertainment                  0.304
		Culture.Media.Films                          0.845
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.291
		Culture.Media.Software                       0.257
		Culture.Media.Television                     0.575
		Culture.Media.Video games                    0.873
		Culture.Performing arts                      0.368
		Culture.Philosophy and religion              0.423
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.711
		Culture.Visual arts.Comics and Anime         0.629
		Culture.Visual arts.Fashion                  0.332
		Culture.Visual arts.Visual arts*             0.715
		Geography.Geographical                       0.766
		Geography.Regions.Africa.Africa*             0.555
		Geography.Regions.Africa.Central Africa      0.353
		Geography.Regions.Africa.Eastern Africa      0.309
		Geography.Regions.Africa.Northern Africa     0.316
		Geography.Regions.Africa.Southern Africa     0.389
		Geography.Regions.Africa.Western Africa      0.469
		Geography.Regions.Americas.Central America   0.57
		Geography.Regions.Americas.North America     0.631
		Geography.Regions.Americas.South America     0.675
		Geography.Regions.Asia.Asia*                 0.825
		Geography.Regions.Asia.Central Asia          0.488
		Geography.Regions.Asia.East Asia             0.693
		Geography.Regions.Asia.North Asia            0.221
		Geography.Regions.Asia.South Asia            0.874
		Geography.Regions.Asia.Southeast Asia        0.753
		Geography.Regions.Asia.West Asia             0.746
		Geography.Regions.Europe.Eastern Europe      0.761
		Geography.Regions.Europe.Europe*             0.752
		Geography.Regions.Europe.Northern Europe     0.677
		Geography.Regions.Europe.Southern Europe     0.696
		Geography.Regions.Europe.Western Europe      0.678
		Geography.Regions.Oceania                    0.863
		History and Society.Business and economics   0.434
		History and Society.Education                0.448
		History and Society.History                  0.293
		History and Society.Military and warfare     0.664
		History and Society.Politics and government  0.626
		History and Society.Society                  0.33
		History and Society.Transportation           0.867
		STEM.Biology                                 0.872
		STEM.Chemistry                               0.548
		STEM.Computing                               0.331
		STEM.Earth and environment                   0.443
		STEM.Engineering                             0.649
		STEM.Libraries & Information                 0.358
		STEM.Mathematics                             0.265
		STEM.Medicine & Health                       0.657
		STEM.Physics                                 0.186
		STEM.STEM*                                   0.887
		STEM.Space                                   0.915
		STEM.Technology                              0.379
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

