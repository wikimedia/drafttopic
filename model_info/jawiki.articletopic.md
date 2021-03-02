Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'center': False, 'subsample': 1.0, 'multilabel': True, 'label_weights': {}, 'loss': 'deviance', 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'max_depth': 5, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'tol': 0.0001, 'verbose': 0, 'min_samples_leaf': 1, 'random_state': None, 'presort': 'deprecated', 'init': None, 'min_impurity_decrease': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'validation_fraction': 0.1, 'max_features': 'log2', 'warm_start': False, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'scale': False, 'min_impurity_split': None, 'min_samples_split': 2}
	Environment:
	 - revscoring_version: '2.9.2'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=62161):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 17996  -->  16111  1885  1205  42960
			'Culture.Biography.Women'                       3990  -->   2487  1503   546  57625
			'Culture.Food and drink'                        1602  -->   1179   423   118  60441
			'Culture.Internet culture'                      3249  -->   2428   821   282  58630
			'Culture.Linguistics'                           1726  -->   1143   583   155  60280
			'Culture.Literature'                            5947  -->   4306  1641   719  55495
			'Culture.Media.Books'                           1625  -->    953   672   250  60286
			'Culture.Media.Entertainment'                   2288  -->   1147  1141   183  59690
			'Culture.Media.Films'                           2752  -->   2046   706   242  59167
			'Culture.Media.Media*'                         14723  -->  12282  2441  1930  45508
			'Culture.Media.Music'                           3280  -->   2610   670   346  58535
			'Culture.Media.Radio'                            836  -->    462   374    83  61242
			'Culture.Media.Software'                        2002  -->   1338   664   431  59728
			'Culture.Media.Television'                      2131  -->   1356   775   175  59855
			'Culture.Media.Video games'                     2339  -->   1964   375   116  59706
			'Culture.Performing arts'                       1481  -->    834   647   161  60519
			'Culture.Philosophy and religion'               3399  -->   1741  1658   396  58366
			'Culture.Sports'                                6660  -->   5889   771   262  55239
			'Culture.Visual arts.Architecture'              2074  -->   1184   890   275  59812
			'Culture.Visual arts.Comics and Anime'          2611  -->   2118   493   238  59312
			'Culture.Visual arts.Fashion'                   1262  -->    887   375    98  60801
			'Culture.Visual arts.Visual arts*'              6538  -->   4562  1976   727  54896
			'Geography.Geographical'                        3548  -->   2167  1381   596  58017
			'Geography.Regions.Africa.Africa*'              5002  -->   3559  1443   370  56789
			'Geography.Regions.Africa.Central Africa'       1192  -->    764   428    70  60899
			'Geography.Regions.Africa.Eastern Africa'        592  -->    312   280    62  61507
			'Geography.Regions.Africa.Northern Africa'      1406  -->    882   524   114  60641
			'Geography.Regions.Africa.Southern Africa'      1058  -->    578   480    69  61034
			'Geography.Regions.Africa.Western Africa'        348  -->    148   200    53  61760
			'Geography.Regions.Americas.Central America'    1344  -->    780   564    82  60735
			'Geography.Regions.Americas.North America'      6128  -->   3404  2724  1013  55020
			'Geography.Regions.Americas.South America'      1524  -->    908   616   110  60527
			'Geography.Regions.Asia.Asia*'                 15849  -->  12478  3371  1800  44512
			'Geography.Regions.Asia.Central Asia'           1248  -->    813   435    79  60834
			'Geography.Regions.Asia.East Asia'              7676  -->   5866  1810   985  53500
			'Geography.Regions.Asia.North Asia'             2935  -->   1816  1119   310  58916
			'Geography.Regions.Asia.South Asia'             1726  -->   1198   528   114  60321
			'Geography.Regions.Asia.Southeast Asia'         1739  -->   1121   618   104  60318
			'Geography.Regions.Asia.West Asia'              1981  -->   1248   733   187  59993
			'Geography.Regions.Europe.Eastern Europe'       3995  -->   2569  1426   391  57775
			'Geography.Regions.Europe.Europe*'             13925  -->  10071  3854  1976  46260
			'Geography.Regions.Europe.Northern Europe'      3447  -->   1845  1602   446  58268
			'Geography.Regions.Europe.Southern Europe'      3085  -->   2004  1081   355  58721
			'Geography.Regions.Europe.Western Europe'       4253  -->   2661  1592   579  57329
			'Geography.Regions.Oceania'                     1627  -->   1007   620    91  60443
			'History and Society.Business and economics'    3965  -->   2165  1800   571  57625
			'History and Society.Education'                 1982  -->    986   996   170  60009
			'History and Society.History'                   4839  -->   2329  2510   660  56662
			'History and Society.Military and warfare'      4820  -->   3219  1601   540  56801
			'History and Society.Politics and government'   3564  -->   1725  1839   580  58017
			'History and Society.Society'                   4230  -->   1162  3068   326  57605
			'History and Society.Transportation'            4960  -->   4360   600   290  56911
			'STEM.Biology'                                  2985  -->   2198   787   249  58927
			'STEM.Chemistry'                                1522  -->   1069   453   219  60420
			'STEM.Computing'                                2573  -->   1974   599   464  59124
			'STEM.Earth and environment'                    1893  -->   1229   664   158  60110
			'STEM.Engineering'                              3017  -->   2222   795   254  58890
			'STEM.Libraries & Information'                   997  -->    582   415    96  61068
			'STEM.Mathematics'                              1173  -->    890   283    76  60912
			'STEM.Medicine & Health'                        1995  -->   1281   714   227  59939
			'STEM.Physics'                                  1421  -->    884   537   199  60541
			'STEM.STEM*'                                   18067  -->  15711  2356  1303  42791
			'STEM.Space'                                    1918  -->   1688   230    80  60163
			'STEM.Technology'                               4518  -->   3000  1518   805  56838
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.29          0.121
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.026         0.003
		Culture.Internet culture                        0.052         0.004
		Culture.Linguistics                             0.028         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.044         0.012
		Culture.Media.Media*                            0.237         0.055
		Culture.Media.Music                             0.053         0.021
		Culture.Media.Radio                             0.013         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.034         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.055         0.01
		Culture.Sports                                  0.107         0.061
		Culture.Visual arts.Architecture                0.033         0.011
		Culture.Visual arts.Comics and Anime            0.042         0.002
		Culture.Visual arts.Fashion                     0.02          0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.057         0.021
		Geography.Regions.Africa.Africa*                0.08          0.009
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.01          0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.017         0.001
		Geography.Regions.Africa.Western Africa         0.006         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.099         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.255         0.053
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.123         0.012
		Geography.Regions.Asia.North Asia               0.047         0.006
		Geography.Regions.Asia.South Asia               0.028         0.017
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.032         0.012
		Geography.Regions.Europe.Eastern Europe         0.064         0.018
		Geography.Regions.Europe.Europe*                0.224         0.082
		Geography.Regions.Europe.Northern Europe        0.055         0.029
		Geography.Regions.Europe.Southern Europe        0.05          0.014
		Geography.Regions.Europe.Western Europe         0.068         0.021
		Geography.Regions.Oceania                       0.026         0.017
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.078         0.011
		History and Society.Military and warfare        0.078         0.015
		History and Society.Politics and government     0.057         0.016
		History and Society.Society                     0.068         0.008
		History and Society.Transportation              0.08          0.016
		STEM.Biology                                    0.048         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.016         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.291         0.066
		STEM.Space                                      0.031         0.004
		STEM.Technology                                 0.073         0.005
	match_rate (micro=0.054, macro=0.019):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.133
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.008
		Culture.Literature                           0.023
		Culture.Media.Books                          0.007
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.013
		Culture.Media.Media*                         0.085
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.058
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.006
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.026
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.052
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.079
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.027
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.097
		Geography.Regions.Europe.Northern Europe     0.023
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.015
		History and Society.Education                0.007
		History and Society.History                  0.017
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.018
		History and Society.Society                  0.008
		History and Society.Transportation           0.019
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.005
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.009
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.085
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.981):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.992
		Culture.Literature                           0.977
		Culture.Media.Books                          0.993
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.915
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.994
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.974
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.948
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.921
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.973
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.903
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.985
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.982
		History and Society.Society                  0.992
		History and Society.Transportation           0.981
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.995
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.991
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.915
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.724, macro=0.658):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.623
		Culture.Food and drink                       0.736
		Culture.Internet culture                     0.747
		Culture.Linguistics                          0.662
		Culture.Literature                           0.724
		Culture.Media.Books                          0.586
		Culture.Media.Entertainment                  0.501
		Culture.Media.Films                          0.743
		Culture.Media.Media*                         0.834
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.553
		Culture.Media.Software                       0.668
		Culture.Media.Television                     0.636
		Culture.Media.Video games                    0.84
		Culture.Performing arts                      0.563
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.884
		Culture.Visual arts.Architecture             0.571
		Culture.Visual arts.Comics and Anime         0.811
		Culture.Visual arts.Fashion                  0.703
		Culture.Visual arts.Visual arts*             0.698
		Geography.Geographical                       0.611
		Geography.Regions.Africa.Africa*             0.712
		Geography.Regions.Africa.Central Africa      0.641
		Geography.Regions.Africa.Eastern Africa      0.527
		Geography.Regions.Africa.Northern Africa     0.627
		Geography.Regions.Africa.Southern Africa     0.546
		Geography.Regions.Africa.Western Africa      0.425
		Geography.Regions.Americas.Central America   0.58
		Geography.Regions.Americas.North America     0.555
		Geography.Regions.Americas.South America     0.596
		Geography.Regions.Asia.Asia*                 0.787
		Geography.Regions.Asia.Central Asia          0.651
		Geography.Regions.Asia.East Asia             0.764
		Geography.Regions.Asia.North Asia            0.619
		Geography.Regions.Asia.South Asia            0.694
		Geography.Regions.Asia.Southeast Asia        0.645
		Geography.Regions.Asia.West Asia             0.63
		Geography.Regions.Europe.Eastern Europe      0.643
		Geography.Regions.Europe.Europe*             0.723
		Geography.Regions.Europe.Northern Europe     0.535
		Geography.Regions.Europe.Southern Europe     0.65
		Geography.Regions.Europe.Western Europe      0.626
		Geography.Regions.Oceania                    0.619
		History and Society.Business and economics   0.546
		History and Society.Education                0.497
		History and Society.History                  0.481
		History and Society.Military and warfare     0.668
		History and Society.Politics and government  0.484
		History and Society.Society                  0.275
		History and Society.Transportation           0.879
		STEM.Biology                                 0.736
		STEM.Chemistry                               0.702
		STEM.Computing                               0.767
		STEM.Earth and environment                   0.649
		STEM.Engineering                             0.736
		STEM.Libraries & Information                 0.584
		STEM.Mathematics                             0.759
		STEM.Medicine & Health                       0.642
		STEM.Physics                                 0.622
		STEM.STEM*                                   0.87
		STEM.Space                                   0.88
		STEM.Technology                              0.664
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.99
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.995
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	precision (micro=0.644, macro=0.501):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.819
		Culture.Biography.Women                      0.505
		Culture.Food and drink                       0.494
		Culture.Internet culture                     0.371
		Culture.Linguistics                          0.678
		Culture.Literature                           0.463
		Culture.Media.Books                          0.383
		Culture.Media.Entertainment                  0.396
		Culture.Media.Films                          0.683
		Culture.Media.Media*                         0.546
		Culture.Media.Music                          0.746
		Culture.Media.Radio                          0.49
		Culture.Media.Software                       0.11
		Culture.Media.Television                     0.664
		Culture.Media.Video games                    0.56
		Culture.Performing arts                      0.396
		Culture.Philosophy and religion              0.446
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.579
		Culture.Visual arts.Comics and Anime         0.329
		Culture.Visual arts.Fashion                  0.283
		Culture.Visual arts.Visual arts*             0.498
		Geography.Geographical                       0.567
		Geography.Regions.Africa.Africa*             0.487
		Geography.Regions.Africa.Central Africa      0.284
		Geography.Regions.Africa.Eastern Africa      0.21
		Geography.Regions.Africa.Northern Africa     0.313
		Geography.Regions.Africa.Southern Africa     0.39
		Geography.Regions.Africa.Western Africa      0.272
		Geography.Regions.Americas.Central America   0.601
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.532
		Geography.Regions.Asia.Central Asia          0.288
		Geography.Regions.Asia.East Asia             0.344
		Geography.Regions.Asia.North Asia            0.402
		Geography.Regions.Asia.South Asia            0.862
		Geography.Regions.Asia.Southeast Asia        0.704
		Geography.Regions.Asia.West Asia             0.708
		Geography.Regions.Europe.Eastern Europe      0.643
		Geography.Regions.Europe.Europe*             0.611
		Geography.Regions.Europe.Northern Europe     0.68
		Geography.Regions.Europe.Southern Europe     0.606
		Geography.Regions.Europe.Western Europe      0.569
		Geography.Regions.Oceania                    0.874
		History and Society.Business and economics   0.356
		History and Society.Education                0.587
		History and Society.History                  0.316
		History and Society.Military and warfare     0.527
		History and Society.Politics and government  0.45
		History and Society.Society                  0.291
		History and Society.Transportation           0.743
		STEM.Biology                                 0.863
		STEM.Chemistry                               0.25
		STEM.Computing                               0.22
		STEM.Earth and environment                   0.543
		STEM.Engineering                             0.5
		STEM.Libraries & Information                 0.205
		STEM.Mathematics                             0.221
		STEM.Medicine & Health                       0.527
		STEM.Physics                                 0.152
		STEM.STEM*                                   0.674
		STEM.Space                                   0.741
		STEM.Technology                              0.199
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.672, macro=0.548):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.856
		Culture.Biography.Women                      0.558
		Culture.Food and drink                       0.591
		Culture.Internet culture                     0.496
		Culture.Linguistics                          0.67
		Culture.Literature                           0.565
		Culture.Media.Books                          0.464
		Culture.Media.Entertainment                  0.443
		Culture.Media.Films                          0.712
		Culture.Media.Media*                         0.66
		Culture.Media.Music                          0.77
		Culture.Media.Radio                          0.519
		Culture.Media.Software                       0.189
		Culture.Media.Television                     0.65
		Culture.Media.Video games                    0.672
		Culture.Performing arts                      0.465
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.904
		Culture.Visual arts.Architecture             0.575
		Culture.Visual arts.Comics and Anime         0.469
		Culture.Visual arts.Fashion                  0.404
		Culture.Visual arts.Visual arts*             0.581
		Geography.Geographical                       0.588
		Geography.Regions.Africa.Africa*             0.578
		Geography.Regions.Africa.Central Africa      0.394
		Geography.Regions.Africa.Eastern Africa      0.3
		Geography.Regions.Africa.Northern Africa     0.418
		Geography.Regions.Africa.Southern Africa     0.455
		Geography.Regions.Africa.Western Africa      0.332
		Geography.Regions.Americas.Central America   0.59
		Geography.Regions.Americas.North America     0.61
		Geography.Regions.Americas.South America     0.642
		Geography.Regions.Asia.Asia*                 0.635
		Geography.Regions.Asia.Central Asia          0.399
		Geography.Regions.Asia.East Asia             0.475
		Geography.Regions.Asia.North Asia            0.488
		Geography.Regions.Asia.South Asia            0.769
		Geography.Regions.Asia.Southeast Asia        0.673
		Geography.Regions.Asia.West Asia             0.667
		Geography.Regions.Europe.Eastern Europe      0.643
		Geography.Regions.Europe.Europe*             0.662
		Geography.Regions.Europe.Northern Europe     0.599
		Geography.Regions.Europe.Southern Europe     0.627
		Geography.Regions.Europe.Western Europe      0.596
		Geography.Regions.Oceania                    0.725
		History and Society.Business and economics   0.431
		History and Society.Education                0.538
		History and Society.History                  0.382
		History and Society.Military and warfare     0.589
		History and Society.Politics and government  0.466
		History and Society.Society                  0.283
		History and Society.Transportation           0.805
		STEM.Biology                                 0.795
		STEM.Chemistry                               0.368
		STEM.Computing                               0.342
		STEM.Earth and environment                   0.591
		STEM.Engineering                             0.596
		STEM.Libraries & Information                 0.303
		STEM.Mathematics                             0.343
		STEM.Medicine & Health                       0.579
		STEM.Physics                                 0.245
		STEM.STEM*                                   0.759
		STEM.Space                                   0.805
		STEM.Technology                              0.306
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
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
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.963
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.983
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.952
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.955
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.952
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.982
		History and Society.Society                  0.988
		History and Society.Transportation           0.993
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.964
		STEM.Space                                   0.998
		STEM.Technology                              0.984
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.008):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.027
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.003
		Culture.Literature                           0.013
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.004
		Culture.Media.Media*                         0.041
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.013
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.039
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.041
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.01
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.01
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.01
		History and Society.Society                  0.006
		History and Society.Transportation           0.005
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.014
		-------------------------------------------  -----
	roc_auc (micro=0.967, macro=0.97):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.97
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.976
		Culture.Literature                           0.972
		Culture.Media.Books                          0.976
		Culture.Media.Entertainment                  0.964
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.967
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.947
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.963
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.97
		Geography.Regions.Africa.Central Africa      0.982
		Geography.Regions.Africa.Eastern Africa      0.967
		Geography.Regions.Africa.Northern Africa     0.971
		Geography.Regions.Africa.Southern Africa     0.966
		Geography.Regions.Africa.Western Africa      0.946
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.948
		Geography.Regions.Americas.South America     0.969
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.971
		Geography.Regions.Asia.North Asia            0.967
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.974
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.964
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.958
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.968
		History and Society.Business and economics   0.957
		History and Society.Education                0.964
		History and Society.History                  0.942
		History and Society.Military and warfare     0.97
		History and Society.Politics and government  0.951
		History and Society.Society                  0.897
		History and Society.Transportation           0.986
		STEM.Biology                                 0.975
		STEM.Chemistry                               0.984
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.978
		STEM.Libraries & Information                 0.97
		STEM.Mathematics                             0.983
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.972
		STEM.Space                                   0.989
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.712, macro=0.549):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.926
		Culture.Biography.Women                      0.542
		Culture.Food and drink                       0.622
		Culture.Internet culture                     0.584
		Culture.Linguistics                          0.674
		Culture.Literature                           0.609
		Culture.Media.Books                          0.415
		Culture.Media.Entertainment                  0.432
		Culture.Media.Films                          0.747
		Culture.Media.Media*                         0.759
		Culture.Media.Music                          0.776
		Culture.Media.Radio                          0.385
		Culture.Media.Software                       0.146
		Culture.Media.Television                     0.666
		Culture.Media.Video games                    0.767
		Culture.Performing arts                      0.398
		Culture.Philosophy and religion              0.418
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.544
		Culture.Visual arts.Comics and Anime         0.595
		Culture.Visual arts.Fashion                  0.503
		Culture.Visual arts.Visual arts*             0.637
		Geography.Geographical                       0.583
		Geography.Regions.Africa.Africa*             0.56
		Geography.Regions.Africa.Central Africa      0.38
		Geography.Regions.Africa.Eastern Africa      0.164
		Geography.Regions.Africa.Northern Africa     0.382
		Geography.Regions.Africa.Southern Africa     0.341
		Geography.Regions.Africa.Western Africa      0.123
		Geography.Regions.Americas.Central America   0.498
		Geography.Regions.Americas.North America     0.671
		Geography.Regions.Americas.South America     0.609
		Geography.Regions.Asia.Asia*                 0.694
		Geography.Regions.Asia.Central Asia          0.382
		Geography.Regions.Asia.East Asia             0.482
		Geography.Regions.Asia.North Asia            0.433
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.667
		Geography.Regions.Asia.West Asia             0.669
		Geography.Regions.Europe.Eastern Europe      0.635
		Geography.Regions.Europe.Europe*             0.712
		Geography.Regions.Europe.Northern Europe     0.65
		Geography.Regions.Europe.Southern Europe     0.668
		Geography.Regions.Europe.Western Europe      0.588
		Geography.Regions.Oceania                    0.776
		History and Society.Business and economics   0.38
		History and Society.Education                0.501
		History and Society.History                  0.347
		History and Society.Military and warfare     0.634
		History and Society.Politics and government  0.431
		History and Society.Society                  0.205
		History and Society.Transportation           0.87
		STEM.Biology                                 0.839
		STEM.Chemistry                               0.333
		STEM.Computing                               0.328
		STEM.Earth and environment                   0.573
		STEM.Engineering                             0.64
		STEM.Libraries & Information                 0.207
		STEM.Mathematics                             0.358
		STEM.Medicine & Health                       0.576
		STEM.Physics                                 0.225
		STEM.STEM*                                   0.865
		STEM.Space                                   0.889
		STEM.Technology                              0.363
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Americas.North America': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

