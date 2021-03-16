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
	counts (n=57416):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13381  -->  11942  1439   744  43291
			'Culture.Biography.Women'                       3703  -->   2952   751   281  53432
			'Culture.Food and drink'                        1377  -->    830   547   168  55871
			'Culture.Internet culture'                      2959  -->   2506   453   211  54246
			'Culture.Linguistics'                           1601  -->   1150   451   105  55710
			'Culture.Literature'                            5115  -->   3847  1268   405  51896
			'Culture.Media.Books'                           1560  -->   1255   305    97  55759
			'Culture.Media.Entertainment'                   2246  -->   1203  1043   214  54956
			'Culture.Media.Films'                           2674  -->   2342   332   102  54640
			'Culture.Media.Media*'                         12684  -->  11207  1477  1096  43636
			'Culture.Media.Music'                           2694  -->   2248   446   163  54559
			'Culture.Media.Radio'                            284  -->    201    83    19  57113
			'Culture.Media.Software'                        2267  -->   1961   306   239  54910
			'Culture.Media.Television'                      2400  -->   2049   351   110  54906
			'Culture.Media.Video games'                     1405  -->   1320    85    39  55972
			'Culture.Performing arts'                       1449  -->    801   648   120  55847
			'Culture.Philosophy and religion'               4226  -->   2430  1796   455  52735
			'Culture.Sports'                                5082  -->   4504   578   133  52201
			'Culture.Visual arts.Architecture'              1985  -->   1264   721   200  55231
			'Culture.Visual arts.Comics and Anime'          1324  -->   1126   198    64  56028
			'Culture.Visual arts.Fashion'                    646  -->    330   316    50  56720
			'Culture.Visual arts.Visual arts*'              4640  -->   2941  1699   377  52399
			'Geography.Geographical'                        5060  -->   3708  1352   795  51561
			'Geography.Regions.Africa.Africa*'              3847  -->   2594  1253   295  53274
			'Geography.Regions.Africa.Central Africa'        537  -->    297   240    75  56804
			'Geography.Regions.Africa.Eastern Africa'        449  -->    291   158    51  56916
			'Geography.Regions.Africa.Northern Africa'      1505  -->   1024   481   107  55804
			'Geography.Regions.Africa.Southern Africa'       625  -->    370   255    38  56753
			'Geography.Regions.Africa.Western Africa'        150  -->    102    48    36  57230
			'Geography.Regions.Americas.Central America'    1314  -->    597   717    90  56012
			'Geography.Regions.Americas.North America'      6102  -->   4246  1856   754  50560
			'Geography.Regions.Americas.South America'      1547  -->   1019   528   104  55765
			'Geography.Regions.Asia.Asia*'                 10008  -->   8003  2005   805  46603
			'Geography.Regions.Asia.Central Asia'           1120  -->    746   374    65  56231
			'Geography.Regions.Asia.East Asia'              2638  -->   2068   570    92  54686
			'Geography.Regions.Asia.North Asia'             1984  -->   1456   528   262  55170
			'Geography.Regions.Asia.South Asia'             1784  -->   1283   501    78  55554
			'Geography.Regions.Asia.Southeast Asia'         1588  -->   1072   516    85  55743
			'Geography.Regions.Asia.West Asia'              2753  -->   1978   775   236  54427
			'Geography.Regions.Europe.Eastern Europe'       4176  -->   3084  1092   388  52852
			'Geography.Regions.Europe.Europe*'             16664  -->  13536  3128  2077  38675
			'Geography.Regions.Europe.Northern Europe'      3404  -->   2252  1152   244  53768
			'Geography.Regions.Europe.Southern Europe'      6030  -->   4545  1485   673  50713
			'Geography.Regions.Europe.Western Europe'       4302  -->   3287  1015   338  52776
			'Geography.Regions.Oceania'                     1836  -->   1280   556    99  55481
			'History and Society.Business and economics'    3143  -->   1824  1319   323  53950
			'History and Society.Education'                 1669  -->    840   829   115  55632
			'History and Society.History'                   6814  -->   4427  2387   907  49695
			'History and Society.Military and warfare'      5875  -->   4321  1554   635  50906
			'History and Society.Politics and government'   4679  -->   2730  1949   486  52251
			'History and Society.Society'                   6974  -->   3406  3568   646  49796
			'History and Society.Transportation'            3236  -->   2907   329    89  54091
			'STEM.Biology'                                  3787  -->   3120   667   158  53471
			'STEM.Chemistry'                                2144  -->   1627   517   370  54902
			'STEM.Computing'                                2657  -->   2271   386   260  54499
			'STEM.Earth and environment'                    1681  -->   1038   643   154  55581
			'STEM.Engineering'                              2820  -->   2197   623   157  54439
			'STEM.Libraries & Information'                   516  -->    387   129    28  56872
			'STEM.Mathematics'                               573  -->    358   215    51  56792
			'STEM.Medicine & Health'                        2450  -->   1722   728   252  54714
			'STEM.Physics'                                  1431  -->   1042   389   158  55827
			'STEM.STEM*'                                   18323  -->  16600  1723   963  38130
			'STEM.Space'                                    2151  -->   2017   134    37  55228
			'STEM.Technology'                               4652  -->   3565  1087   523  52241
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
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.015
		Culture.Sports                               0.065
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.019
		Geography.Geographical                       0.032
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.109
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.025
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.025
		History and Society.Society                  0.019
		History and Society.Transportation           0.015
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.008
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.009
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.985
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.891
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.975
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.975
		History and Society.Society                  0.981
		History and Society.Transportation           0.985
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.992
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.784, macro=0.721):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.892
		Culture.Biography.Women                      0.797
		Culture.Food and drink                       0.603
		Culture.Internet culture                     0.847
		Culture.Linguistics                          0.718
		Culture.Literature                           0.752
		Culture.Media.Books                          0.804
		Culture.Media.Entertainment                  0.536
		Culture.Media.Films                          0.876
		Culture.Media.Media*                         0.884
		Culture.Media.Music                          0.834
		Culture.Media.Radio                          0.708
		Culture.Media.Software                       0.865
		Culture.Media.Television                     0.854
		Culture.Media.Video games                    0.94
		Culture.Performing arts                      0.553
		Culture.Philosophy and religion              0.575
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.637
		Culture.Visual arts.Comics and Anime         0.85
		Culture.Visual arts.Fashion                  0.511
		Culture.Visual arts.Visual arts*             0.634
		Geography.Geographical                       0.733
		Geography.Regions.Africa.Africa*             0.674
		Geography.Regions.Africa.Central Africa      0.553
		Geography.Regions.Africa.Eastern Africa      0.648
		Geography.Regions.Africa.Northern Africa     0.68
		Geography.Regions.Africa.Southern Africa     0.592
		Geography.Regions.Africa.Western Africa      0.68
		Geography.Regions.Americas.Central America   0.454
		Geography.Regions.Americas.North America     0.696
		Geography.Regions.Americas.South America     0.659
		Geography.Regions.Asia.Asia*                 0.8
		Geography.Regions.Asia.Central Asia          0.666
		Geography.Regions.Asia.East Asia             0.784
		Geography.Regions.Asia.North Asia            0.734
		Geography.Regions.Asia.South Asia            0.719
		Geography.Regions.Asia.Southeast Asia        0.675
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.739
		Geography.Regions.Europe.Europe*             0.812
		Geography.Regions.Europe.Northern Europe     0.662
		Geography.Regions.Europe.Southern Europe     0.754
		Geography.Regions.Europe.Western Europe      0.764
		Geography.Regions.Oceania                    0.697
		History and Society.Business and economics   0.58
		History and Society.Education                0.503
		History and Society.History                  0.65
		History and Society.Military and warfare     0.735
		History and Society.Politics and government  0.583
		History and Society.Society                  0.488
		History and Society.Transportation           0.898
		STEM.Biology                                 0.824
		STEM.Chemistry                               0.759
		STEM.Computing                               0.855
		STEM.Earth and environment                   0.617
		STEM.Engineering                             0.779
		STEM.Libraries & Information                 0.75
		STEM.Mathematics                             0.625
		STEM.Medicine & Health                       0.703
		STEM.Physics                                 0.728
		STEM.STEM*                                   0.906
		STEM.Space                                   0.938
		STEM.Technology                              0.766
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
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
		Culture.Media.Software                       0.996
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
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
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
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.991
		History and Society.Society                  0.987
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.993
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.715, macro=0.564):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.881
		Culture.Biography.Women                      0.692
		Culture.Food and drink                       0.332
		Culture.Internet culture                     0.434
		Culture.Linguistics                          0.738
		Culture.Literature                           0.605
		Culture.Media.Books                          0.652
		Culture.Media.Entertainment                  0.332
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.691
		Culture.Media.Music                          0.873
		Culture.Media.Radio                          0.821
		Culture.Media.Software                       0.21
		Culture.Media.Television                     0.792
		Culture.Media.Video games                    0.779
		Culture.Performing arts                      0.427
		Culture.Philosophy and religion              0.42
		Culture.Sports                               0.964
		Culture.Visual arts.Architecture             0.653
		Culture.Visual arts.Comics and Anime         0.621
		Culture.Visual arts.Fashion                  0.319
		Culture.Visual arts.Visual arts*             0.623
		Geography.Geographical                       0.538
		Geography.Regions.Africa.Africa*             0.49
		Geography.Regions.Africa.Central Africa      0.21
		Geography.Regions.Africa.Eastern Africa      0.248
		Geography.Regions.Africa.Northern Africa     0.304
		Geography.Regions.Africa.Southern Africa     0.51
		Geography.Regions.Africa.Western Africa      0.425
		Geography.Regions.Americas.Central America   0.484
		Geography.Regions.Americas.North America     0.765
		Geography.Regions.Americas.South America     0.692
		Geography.Regions.Asia.Asia*                 0.692
		Geography.Regions.Asia.Central Asia          0.333
		Geography.Regions.Asia.East Asia             0.843
		Geography.Regions.Asia.North Asia            0.126
		Geography.Regions.Asia.South Asia            0.888
		Geography.Regions.Asia.Southeast Asia        0.728
		Geography.Regions.Asia.West Asia             0.647
		Geography.Regions.Europe.Eastern Europe      0.568
		Geography.Regions.Europe.Europe*             0.568
		Geography.Regions.Europe.Northern Europe     0.822
		Geography.Regions.Europe.Southern Europe     0.432
		Geography.Regions.Europe.Western Europe      0.701
		Geography.Regions.Oceania                    0.857
		History and Society.Business and economics   0.498
		History and Society.Education                0.644
		History and Society.History                  0.284
		History and Society.Military and warfare     0.46
		History and Society.Politics and government  0.647
		History and Society.Society                  0.328
		History and Society.Transportation           0.893
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.15
		STEM.Computing                               0.327
		STEM.Earth and environment                   0.505
		STEM.Engineering                             0.588
		STEM.Libraries & Information                 0.487
		STEM.Mathematics                             0.225
		STEM.Medicine & Health                       0.497
		STEM.Physics                                 0.18
		STEM.STEM*                                   0.732
		STEM.Space                                   0.895
		STEM.Technology                              0.285
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
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
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
		History and Society.Transportation           0.998
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
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.741
		Culture.Food and drink                       0.428
		Culture.Internet culture                     0.574
		Culture.Linguistics                          0.728
		Culture.Literature                           0.67
		Culture.Media.Books                          0.72
		Culture.Media.Entertainment                  0.41
		Culture.Media.Films                          0.854
		Culture.Media.Media*                         0.776
		Culture.Media.Music                          0.853
		Culture.Media.Radio                          0.76
		Culture.Media.Software                       0.338
		Culture.Media.Television                     0.821
		Culture.Media.Video games                    0.852
		Culture.Performing arts                      0.482
		Culture.Philosophy and religion              0.485
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.645
		Culture.Visual arts.Comics and Anime         0.718
		Culture.Visual arts.Fashion                  0.393
		Culture.Visual arts.Visual arts*             0.628
		Geography.Geographical                       0.621
		Geography.Regions.Africa.Africa*             0.568
		Geography.Regions.Africa.Central Africa      0.304
		Geography.Regions.Africa.Eastern Africa      0.359
		Geography.Regions.Africa.Northern Africa     0.42
		Geography.Regions.Africa.Southern Africa     0.548
		Geography.Regions.Africa.Western Africa      0.523
		Geography.Regions.Americas.Central America   0.469
		Geography.Regions.Americas.North America     0.729
		Geography.Regions.Americas.South America     0.675
		Geography.Regions.Asia.Asia*                 0.742
		Geography.Regions.Asia.Central Asia          0.444
		Geography.Regions.Asia.East Asia             0.813
		Geography.Regions.Asia.North Asia            0.214
		Geography.Regions.Asia.South Asia            0.795
		Geography.Regions.Asia.Southeast Asia        0.701
		Geography.Regions.Asia.West Asia             0.681
		Geography.Regions.Europe.Eastern Europe      0.642
		Geography.Regions.Europe.Europe*             0.668
		Geography.Regions.Europe.Northern Europe     0.733
		Geography.Regions.Europe.Southern Europe     0.549
		Geography.Regions.Europe.Western Europe      0.731
		Geography.Regions.Oceania                    0.769
		History and Society.Business and economics   0.536
		History and Society.Education                0.565
		History and Society.History                  0.395
		History and Society.Military and warfare     0.566
		History and Society.Politics and government  0.614
		History and Society.Society                  0.392
		History and Society.Transportation           0.896
		STEM.Biology                                 0.863
		STEM.Chemistry                               0.251
		STEM.Computing                               0.473
		STEM.Earth and environment                   0.555
		STEM.Engineering                             0.67
		STEM.Libraries & Information                 0.59
		STEM.Mathematics                             0.331
		STEM.Medicine & Health                       0.582
		STEM.Physics                                 0.288
		STEM.STEM*                                   0.81
		STEM.Space                                   0.916
		STEM.Technology                              0.415
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
		Culture.Media.Radio                          1
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
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
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
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.996
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.989
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
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.978
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.979
		History and Society.Society                  0.981
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.993
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
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
		Culture.Media.Software                       0.004
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
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
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
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.018
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.009
		History and Society.Society                  0.013
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.007
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.975, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.977
		Culture.Literature                           0.979
		Culture.Media.Books                          0.987
		Culture.Media.Entertainment                  0.973
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.943
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.97
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.968
		Culture.Visual arts.Visual arts*             0.967
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.974
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.968
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.968
		Geography.Regions.Africa.Western Africa      0.915
		Geography.Regions.Americas.Central America   0.962
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.979
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.979
		Geography.Regions.Asia.Southeast Asia        0.977
		Geography.Regions.Asia.West Asia             0.975
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.96
		History and Society.Education                0.96
		History and Society.History                  0.959
		History and Society.Military and warfare     0.973
		History and Society.Politics and government  0.955
		History and Society.Society                  0.929
		History and Society.Transportation           0.987
		STEM.Biology                                 0.98
		STEM.Chemistry                               0.986
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.971
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.969
		STEM.Medicine & Health                       0.98
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.981
		STEM.Space                                   0.99
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.787, macro=0.608):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.939
		Culture.Biography.Women                      0.753
		Culture.Food and drink                       0.421
		Culture.Internet culture                     0.679
		Culture.Linguistics                          0.732
		Culture.Literature                           0.733
		Culture.Media.Books                          0.778
		Culture.Media.Entertainment                  0.31
		Culture.Media.Films                          0.851
		Culture.Media.Media*                         0.875
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.586
		Culture.Media.Software                       0.408
		Culture.Media.Television                     0.858
		Culture.Media.Video games                    0.92
		Culture.Performing arts                      0.382
		Culture.Philosophy and religion              0.466
		Culture.Sports                               0.951
		Culture.Visual arts.Architecture             0.649
		Culture.Visual arts.Comics and Anime         0.76
		Culture.Visual arts.Fashion                  0.196
		Culture.Visual arts.Visual arts*             0.654
		Geography.Geographical                       0.643
		Geography.Regions.Africa.Africa*             0.558
		Geography.Regions.Africa.Central Africa      0.143
		Geography.Regions.Africa.Eastern Africa      0.218
		Geography.Regions.Africa.Northern Africa     0.314
		Geography.Regions.Africa.Southern Africa     0.419
		Geography.Regions.Africa.Western Africa      0.296
		Geography.Regions.Americas.Central America   0.389
		Geography.Regions.Americas.North America     0.801
		Geography.Regions.Americas.South America     0.688
		Geography.Regions.Asia.Asia*                 0.821
		Geography.Regions.Asia.Central Asia          0.38
		Geography.Regions.Asia.East Asia             0.853
		Geography.Regions.Asia.North Asia            0.221
		Geography.Regions.Asia.South Asia            0.844
		Geography.Regions.Asia.Southeast Asia        0.679
		Geography.Regions.Asia.West Asia             0.682
		Geography.Regions.Europe.Eastern Europe      0.718
		Geography.Regions.Europe.Europe*             0.762
		Geography.Regions.Europe.Northern Europe     0.783
		Geography.Regions.Europe.Southern Europe     0.612
		Geography.Regions.Europe.Western Europe      0.771
		Geography.Regions.Oceania                    0.799
		History and Society.Business and economics   0.491
		History and Society.Education                0.537
		History and Society.History                  0.443
		History and Society.Military and warfare     0.619
		History and Society.Politics and government  0.642
		History and Society.Society                  0.367
		History and Society.Transportation           0.938
		STEM.Biology                                 0.91
		STEM.Chemistry                               0.248
		STEM.Computing                               0.562
		STEM.Earth and environment                   0.48
		STEM.Engineering                             0.699
		STEM.Libraries & Information                 0.382
		STEM.Mathematics                             0.219
		STEM.Medicine & Health                       0.617
		STEM.Physics                                 0.266
		STEM.STEM*                                   0.914
		STEM.Space                                   0.924
		STEM.Technology                              0.511
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

