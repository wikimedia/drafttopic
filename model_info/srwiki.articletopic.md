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
	counts (n=57416):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13381  -->  11913  1468   713  43322
			'Culture.Biography.Women'                       3703  -->   2961   742   284  53429
			'Culture.Food and drink'                        1377  -->    824   553   164  55875
			'Culture.Internet culture'                      2959  -->   2514   445   228  54229
			'Culture.Linguistics'                           1601  -->   1150   451   129  55686
			'Culture.Literature'                            5115  -->   3833  1282   421  51880
			'Culture.Media.Books'                           1560  -->   1238   322    97  55759
			'Culture.Media.Entertainment'                   2246  -->   1192  1054   218  54952
			'Culture.Media.Films'                           2674  -->   2333   341   106  54636
			'Culture.Media.Media*'                         12684  -->  11238  1446  1123  43609
			'Culture.Media.Music'                           2694  -->   2253   441   165  54557
			'Culture.Media.Radio'                            284  -->    200    84    26  57106
			'Culture.Media.Software'                        2267  -->   1929   338   250  54899
			'Culture.Media.Television'                      2400  -->   2048   352   103  54913
			'Culture.Media.Video games'                     1405  -->   1327    78    37  55974
			'Culture.Performing arts'                       1449  -->    807   642   120  55847
			'Culture.Philosophy and religion'               4226  -->   2410  1816   453  52737
			'Culture.Sports'                                5082  -->   4504   578   140  52194
			'Culture.Visual arts.Architecture'              1985  -->   1246   739   204  55227
			'Culture.Visual arts.Comics and Anime'          1324  -->   1122   202    72  56020
			'Culture.Visual arts.Fashion'                    646  -->    341   305    50  56720
			'Culture.Visual arts.Visual arts*'              4640  -->   2945  1695   387  52389
			'Geography.Geographical'                        5060  -->   3705  1355   796  51560
			'Geography.Regions.Africa.Africa*'              3847  -->   2602  1245   291  53278
			'Geography.Regions.Africa.Central Africa'        537  -->    274   263    58  56821
			'Geography.Regions.Africa.Eastern Africa'        449  -->    282   167    44  56923
			'Geography.Regions.Africa.Northern Africa'      1505  -->   1015   490   125  55786
			'Geography.Regions.Africa.Southern Africa'       625  -->    380   245    45  56746
			'Geography.Regions.Africa.Western Africa'        150  -->    102    48    24  57242
			'Geography.Regions.Americas.Central America'    1314  -->    602   712    86  56016
			'Geography.Regions.Americas.North America'      6102  -->   4272  1830   738  50576
			'Geography.Regions.Americas.South America'      1547  -->   1020   527   101  55768
			'Geography.Regions.Asia.Asia*'                 10008  -->   7945  2063   777  46631
			'Geography.Regions.Asia.Central Asia'           1120  -->    756   364    70  56226
			'Geography.Regions.Asia.East Asia'              2638  -->   2062   576   103  54675
			'Geography.Regions.Asia.North Asia'             1984  -->   1456   528   274  55158
			'Geography.Regions.Asia.South Asia'             1784  -->   1277   507    64  55568
			'Geography.Regions.Asia.Southeast Asia'         1588  -->   1078   510   102  55726
			'Geography.Regions.Asia.West Asia'              2753  -->   1950   803   221  54442
			'Geography.Regions.Europe.Eastern Europe'       4176  -->   3084  1092   369  52871
			'Geography.Regions.Europe.Europe*'             16664  -->  13521  3143  2059  38693
			'Geography.Regions.Europe.Northern Europe'      3404  -->   2231  1173   244  53768
			'Geography.Regions.Europe.Southern Europe'      6030  -->   4566  1464   668  50718
			'Geography.Regions.Europe.Western Europe'       4302  -->   3277  1025   320  52794
			'Geography.Regions.Oceania'                     1836  -->   1260   576    88  55492
			'History and Society.Business and economics'    3143  -->   1856  1287   280  53993
			'History and Society.Education'                 1669  -->    857   812   113  55634
			'History and Society.History'                   6814  -->   4435  2379   904  49698
			'History and Society.Military and warfare'      5875  -->   4303  1572   638  50903
			'History and Society.Politics and government'   4679  -->   2720  1959   462  52275
			'History and Society.Society'                   6974  -->   3425  3549   613  49829
			'History and Society.Transportation'            3236  -->   2923   313    95  54085
			'STEM.Biology'                                  3787  -->   3111   676   159  53470
			'STEM.Chemistry'                                2144  -->   1639   505   342  54930
			'STEM.Computing'                                2657  -->   2252   405   255  54504
			'STEM.Earth and environment'                    1681  -->   1018   663   155  55580
			'STEM.Engineering'                              2820  -->   2183   637   147  54449
			'STEM.Libraries & Information'                   516  -->    382   134    26  56874
			'STEM.Mathematics'                               573  -->    351   222    53  56790
			'STEM.Medicine & Health'                        2450  -->   1738   712   258  54708
			'STEM.Physics'                                  1431  -->   1039   392   160  55825
			'STEM.STEM*'                                   18323  -->  16602  1721   950  38143
			'STEM.Space'                                    2151  -->   2029   122    25  55240
			'STEM.Technology'                               4652  -->   3536  1116   522  52242
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.024         0.002
		Culture.Internet culture                        0.052         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.089         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.047         0.011
		Culture.Media.Media*                            0.221         0.058
		Culture.Media.Music                             0.047         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.024         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.074         0.011
		Culture.Sports                                  0.089         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.081         0.018
		Geography.Geographical                          0.088         0.024
		Geography.Regions.Africa.Africa*                0.067         0.008
		Geography.Regions.Africa.Central Africa         0.009         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.174         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.035         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.073         0.013
		Geography.Regions.Europe.Europe*                0.29          0.076
		Geography.Regions.Europe.Northern Europe        0.059         0.031
		Geography.Regions.Europe.Southern Europe        0.105         0.013
		Geography.Regions.Europe.Western Europe         0.075         0.019
		Geography.Regions.Oceania                       0.032         0.015
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.029         0.007
		History and Society.History                     0.119         0.011
		History and Society.Military and warfare        0.102         0.014
		History and Society.Politics and government     0.081         0.028
		History and Society.Society                     0.121         0.013
		History and Society.Transportation              0.056         0.015
		STEM.Biology                                    0.066         0.034
		STEM.Chemistry                                  0.037         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.029         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.01          0
		STEM.Medicine & Health                          0.043         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.319         0.069
		STEM.Space                                      0.037         0.006
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.124
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.008
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.019
		Geography.Geographical                       0.032
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
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.108
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.025
		History and Society.Military and warfare     0.023
		History and Society.Politics and government  0.025
		History and Society.Society                  0.018
		History and Society.Transportation           0.015
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.007
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.009
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.992
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.968
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
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.892
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.975
		History and Society.Military and warfare     0.977
		History and Society.Politics and government  0.975
		History and Society.Society                  0.982
		History and Society.Transportation           0.985
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.993
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.783, macro=0.719):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.8
		Culture.Food and drink                       0.598
		Culture.Internet culture                     0.85
		Culture.Linguistics                          0.718
		Culture.Literature                           0.749
		Culture.Media.Books                          0.794
		Culture.Media.Entertainment                  0.531
		Culture.Media.Films                          0.872
		Culture.Media.Media*                         0.886
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.704
		Culture.Media.Software                       0.851
		Culture.Media.Television                     0.853
		Culture.Media.Video games                    0.944
		Culture.Performing arts                      0.557
		Culture.Philosophy and religion              0.57
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.628
		Culture.Visual arts.Comics and Anime         0.847
		Culture.Visual arts.Fashion                  0.528
		Culture.Visual arts.Visual arts*             0.635
		Geography.Geographical                       0.732
		Geography.Regions.Africa.Africa*             0.676
		Geography.Regions.Africa.Central Africa      0.51
		Geography.Regions.Africa.Eastern Africa      0.628
		Geography.Regions.Africa.Northern Africa     0.674
		Geography.Regions.Africa.Southern Africa     0.608
		Geography.Regions.Africa.Western Africa      0.68
		Geography.Regions.Americas.Central America   0.458
		Geography.Regions.Americas.North America     0.7
		Geography.Regions.Americas.South America     0.659
		Geography.Regions.Asia.Asia*                 0.794
		Geography.Regions.Asia.Central Asia          0.675
		Geography.Regions.Asia.East Asia             0.782
		Geography.Regions.Asia.North Asia            0.734
		Geography.Regions.Asia.South Asia            0.716
		Geography.Regions.Asia.Southeast Asia        0.679
		Geography.Regions.Asia.West Asia             0.708
		Geography.Regions.Europe.Eastern Europe      0.739
		Geography.Regions.Europe.Europe*             0.811
		Geography.Regions.Europe.Northern Europe     0.655
		Geography.Regions.Europe.Southern Europe     0.757
		Geography.Regions.Europe.Western Europe      0.762
		Geography.Regions.Oceania                    0.686
		History and Society.Business and economics   0.591
		History and Society.Education                0.513
		History and Society.History                  0.651
		History and Society.Military and warfare     0.732
		History and Society.Politics and government  0.581
		History and Society.Society                  0.491
		History and Society.Transportation           0.903
		STEM.Biology                                 0.821
		STEM.Chemistry                               0.764
		STEM.Computing                               0.848
		STEM.Earth and environment                   0.606
		STEM.Engineering                             0.774
		STEM.Libraries & Information                 0.74
		STEM.Mathematics                             0.613
		STEM.Medicine & Health                       0.709
		STEM.Physics                                 0.726
		STEM.STEM*                                   0.906
		STEM.Space                                   0.943
		STEM.Technology                              0.76
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.991
		History and Society.Society                  0.988
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.994
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   1
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.717, macro=0.565):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.885
		Culture.Biography.Women                      0.691
		Culture.Food and drink                       0.335
		Culture.Internet culture                     0.416
		Culture.Linguistics                          0.696
		Culture.Literature                           0.594
		Culture.Media.Books                          0.649
		Culture.Media.Entertainment                  0.326
		Culture.Media.Films                          0.827
		Culture.Media.Media*                         0.687
		Culture.Media.Music                          0.872
		Culture.Media.Radio                          0.77
		Culture.Media.Software                       0.2
		Culture.Media.Television                     0.802
		Culture.Media.Video games                    0.789
		Culture.Performing arts                      0.429
		Culture.Philosophy and religion              0.419
		Culture.Sports                               0.962
		Culture.Visual arts.Architecture             0.646
		Culture.Visual arts.Comics and Anime         0.592
		Culture.Visual arts.Fashion                  0.327
		Culture.Visual arts.Visual arts*             0.617
		Geography.Geographical                       0.538
		Geography.Regions.Africa.Africa*             0.495
		Geography.Regions.Africa.Central Africa      0.24
		Geography.Regions.Africa.Eastern Africa      0.27
		Geography.Regions.Africa.Northern Africa     0.27
		Geography.Regions.Africa.Southern Africa     0.474
		Geography.Regions.Africa.Western Africa      0.526
		Geography.Regions.Americas.Central America   0.497
		Geography.Regions.Americas.North America     0.77
		Geography.Regions.Americas.South America     0.698
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.32
		Geography.Regions.Asia.East Asia             0.828
		Geography.Regions.Asia.North Asia            0.121
		Geography.Regions.Asia.South Asia            0.906
		Geography.Regions.Asia.Southeast Asia        0.692
		Geography.Regions.Asia.West Asia             0.659
		Geography.Regions.Europe.Eastern Europe      0.581
		Geography.Regions.Europe.Europe*             0.57
		Geography.Regions.Europe.Northern Europe     0.821
		Geography.Regions.Europe.Southern Europe     0.435
		Geography.Regions.Europe.Western Europe      0.712
		Geography.Regions.Oceania                    0.869
		History and Society.Business and economics   0.538
		History and Society.Education                0.652
		History and Society.History                  0.285
		History and Society.Military and warfare     0.458
		History and Society.Politics and government  0.658
		History and Society.Society                  0.34
		History and Society.Transportation           0.887
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.162
		STEM.Computing                               0.329
		STEM.Earth and environment                   0.498
		STEM.Engineering                             0.602
		STEM.Libraries & Information                 0.502
		STEM.Mathematics                             0.215
		STEM.Medicine & Health                       0.493
		STEM.Physics                                 0.178
		STEM.STEM*                                   0.735
		STEM.Space                                   0.927
		STEM.Technology                              0.284
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.74, macro=0.611):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.888
		Culture.Biography.Women                      0.741
		Culture.Food and drink                       0.43
		Culture.Internet culture                     0.559
		Culture.Linguistics                          0.707
		Culture.Literature                           0.663
		Culture.Media.Books                          0.714
		Culture.Media.Entertainment                  0.404
		Culture.Media.Films                          0.849
		Culture.Media.Media*                         0.774
		Culture.Media.Music                          0.854
		Culture.Media.Radio                          0.735
		Culture.Media.Software                       0.324
		Culture.Media.Television                     0.827
		Culture.Media.Video games                    0.86
		Culture.Performing arts                      0.485
		Culture.Philosophy and religion              0.483
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.697
		Culture.Visual arts.Fashion                  0.404
		Culture.Visual arts.Visual arts*             0.626
		Geography.Geographical                       0.62
		Geography.Regions.Africa.Africa*             0.571
		Geography.Regions.Africa.Central Africa      0.327
		Geography.Regions.Africa.Eastern Africa      0.378
		Geography.Regions.Africa.Northern Africa     0.386
		Geography.Regions.Africa.Southern Africa     0.533
		Geography.Regions.Africa.Western Africa      0.593
		Geography.Regions.Americas.Central America   0.477
		Geography.Regions.Americas.North America     0.733
		Geography.Regions.Americas.South America     0.678
		Geography.Regions.Asia.Asia*                 0.743
		Geography.Regions.Asia.Central Asia          0.434
		Geography.Regions.Asia.East Asia             0.804
		Geography.Regions.Asia.North Asia            0.207
		Geography.Regions.Asia.South Asia            0.8
		Geography.Regions.Asia.Southeast Asia        0.685
		Geography.Regions.Asia.West Asia             0.683
		Geography.Regions.Europe.Eastern Europe      0.65
		Geography.Regions.Europe.Europe*             0.669
		Geography.Regions.Europe.Northern Europe     0.729
		Geography.Regions.Europe.Southern Europe     0.552
		Geography.Regions.Europe.Western Europe      0.736
		Geography.Regions.Oceania                    0.767
		History and Society.Business and economics   0.563
		History and Society.Education                0.575
		History and Society.History                  0.397
		History and Society.Military and warfare     0.563
		History and Society.Politics and government  0.617
		History and Society.Society                  0.402
		History and Society.Transportation           0.895
		STEM.Biology                                 0.862
		STEM.Chemistry                               0.267
		STEM.Computing                               0.474
		STEM.Earth and environment                   0.547
		STEM.Engineering                             0.677
		STEM.Libraries & Information                 0.598
		STEM.Mathematics                             0.318
		STEM.Medicine & Health                       0.582
		STEM.Physics                                 0.285
		STEM.STEM*                                   0.811
		STEM.Space                                   0.935
		STEM.Technology                              0.413
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.984
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.991
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.98
		History and Society.Society                  0.982
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.993
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.025
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.015
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.051
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.018
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.009
		History and Society.Society                  0.012
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.006
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.975, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.973
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.976
		Culture.Literature                           0.979
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.945
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.97
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.966
		Culture.Visual arts.Visual arts*             0.967
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.973
		Geography.Regions.Africa.Central Africa      0.972
		Geography.Regions.Africa.Eastern Africa      0.971
		Geography.Regions.Africa.Northern Africa     0.976
		Geography.Regions.Africa.Southern Africa     0.969
		Geography.Regions.Africa.Western Africa      0.908
		Geography.Regions.Americas.Central America   0.963
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.977
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.979
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.974
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.961
		History and Society.Education                0.963
		History and Society.History                  0.96
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.957
		History and Society.Society                  0.929
		History and Society.Transportation           0.987
		STEM.Biology                                 0.98
		STEM.Chemistry                               0.987
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.971
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.967
		STEM.Medicine & Health                       0.98
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.98
		STEM.Space                                   0.99
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.79, macro=0.61):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.94
		Culture.Biography.Women                      0.762
		Culture.Food and drink                       0.419
		Culture.Internet culture                     0.673
		Culture.Linguistics                          0.672
		Culture.Literature                           0.723
		Culture.Media.Books                          0.718
		Culture.Media.Entertainment                  0.331
		Culture.Media.Films                          0.887
		Culture.Media.Media*                         0.872
		Culture.Media.Music                          0.888
		Culture.Media.Radio                          0.563
		Culture.Media.Software                       0.382
		Culture.Media.Television                     0.851
		Culture.Media.Video games                    0.914
		Culture.Performing arts                      0.38
		Culture.Philosophy and religion              0.464
		Culture.Sports                               0.953
		Culture.Visual arts.Architecture             0.626
		Culture.Visual arts.Comics and Anime         0.767
		Culture.Visual arts.Fashion                  0.243
		Culture.Visual arts.Visual arts*             0.651
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.564
		Geography.Regions.Africa.Central Africa      0.171
		Geography.Regions.Africa.Eastern Africa      0.167
		Geography.Regions.Africa.Northern Africa     0.337
		Geography.Regions.Africa.Southern Africa     0.42
		Geography.Regions.Africa.Western Africa      0.414
		Geography.Regions.Americas.Central America   0.385
		Geography.Regions.Americas.North America     0.803
		Geography.Regions.Americas.South America     0.671
		Geography.Regions.Asia.Asia*                 0.827
		Geography.Regions.Asia.Central Asia          0.333
		Geography.Regions.Asia.East Asia             0.853
		Geography.Regions.Asia.North Asia            0.174
		Geography.Regions.Asia.South Asia            0.84
		Geography.Regions.Asia.Southeast Asia        0.659
		Geography.Regions.Asia.West Asia             0.679
		Geography.Regions.Europe.Eastern Europe      0.697
		Geography.Regions.Europe.Europe*             0.771
		Geography.Regions.Europe.Northern Europe     0.787
		Geography.Regions.Europe.Southern Europe     0.621
		Geography.Regions.Europe.Western Europe      0.804
		Geography.Regions.Oceania                    0.814
		History and Society.Business and economics   0.517
		History and Society.Education                0.551
		History and Society.History                  0.439
		History and Society.Military and warfare     0.629
		History and Society.Politics and government  0.657
		History and Society.Society                  0.365
		History and Society.Transportation           0.935
		STEM.Biology                                 0.9
		STEM.Chemistry                               0.244
		STEM.Computing                               0.577
		STEM.Earth and environment                   0.526
		STEM.Engineering                             0.723
		STEM.Libraries & Information                 0.466
		STEM.Mathematics                             0.148
		STEM.Medicine & Health                       0.657
		STEM.Physics                                 0.293
		STEM.STEM*                                   0.914
		STEM.Space                                   0.957
		STEM.Technology                              0.467
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

