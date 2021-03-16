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
	counts (n=56390):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13186  -->  11348  1838   893  42311
			'Culture.Biography.Women'                       3662  -->   2729   933   331  52397
			'Culture.Food and drink'                        1345  -->    734   611   167  54878
			'Culture.Internet culture'                      2898  -->   2326   572   223  53269
			'Culture.Linguistics'                           1515  -->    956   559   116  54759
			'Culture.Literature'                            5010  -->   3516  1494   455  50925
			'Culture.Media.Books'                           1534  -->   1146   388   118  54738
			'Culture.Media.Entertainment'                   2212  -->   1082  1130   204  53974
			'Culture.Media.Films'                           2650  -->   2228   422   117  53623
			'Culture.Media.Media*'                         12435  -->  10617  1818  1252  42703
			'Culture.Media.Music'                           2628  -->   2054   574   189  53573
			'Culture.Media.Radio'                            271  -->    189    82    32  56087
			'Culture.Media.Software'                        2204  -->   1818   386   258  53928
			'Culture.Media.Television'                      2349  -->   1909   440   116  53925
			'Culture.Media.Video games'                     1391  -->   1267   124    43  54956
			'Culture.Performing arts'                       1412  -->    683   729   109  54869
			'Culture.Philosophy and religion'               4071  -->   2023  2048   452  51867
			'Culture.Sports'                                5036  -->   4395   641   144  51210
			'Culture.Visual arts.Architecture'              1947  -->   1115   832   199  54244
			'Culture.Visual arts.Comics and Anime'          1301  -->   1048   253    62  55027
			'Culture.Visual arts.Fashion'                    633  -->    312   321    24  55733
			'Culture.Visual arts.Visual arts*'              4546  -->   2660  1886   398  51446
			'Geography.Geographical'                        4938  -->   3406  1532   770  50682
			'Geography.Regions.Africa.Africa*'              3767  -->   2436  1331   283  52340
			'Geography.Regions.Africa.Central Africa'        533  -->    241   292    66  55791
			'Geography.Regions.Africa.Eastern Africa'        440  -->    284   156    36  55914
			'Geography.Regions.Africa.Northern Africa'      1469  -->    911   558   107  54814
			'Geography.Regions.Africa.Southern Africa'       607  -->    391   216    53  55730
			'Geography.Regions.Africa.Western Africa'        149  -->     99    50    27  56214
			'Geography.Regions.Americas.Central America'    1299  -->    553   746    82  55009
			'Geography.Regions.Americas.North America'      6032  -->   3920  2112   687  49671
			'Geography.Regions.Americas.South America'      1528  -->    942   586    93  54769
			'Geography.Regions.Asia.Asia*'                  9808  -->   7475  2333   824  45758
			'Geography.Regions.Asia.Central Asia'           1089  -->    679   410    78  55223
			'Geography.Regions.Asia.East Asia'              2608  -->   1977   631   103  53679
			'Geography.Regions.Asia.North Asia'             1937  -->   1330   607   241  54212
			'Geography.Regions.Asia.South Asia'             1731  -->   1169   562    80  54579
			'Geography.Regions.Asia.Southeast Asia'         1564  -->   1032   532    88  54738
			'Geography.Regions.Asia.West Asia'              2682  -->   1775   907   228  53480
			'Geography.Regions.Europe.Eastern Europe'       4098  -->   2903  1195   341  51951
			'Geography.Regions.Europe.Europe*'             16372  -->  12678  3694  2162  37856
			'Geography.Regions.Europe.Northern Europe'      3349  -->   1987  1362   260  52781
			'Geography.Regions.Europe.Southern Europe'      5884  -->   4096  1788   687  49819
			'Geography.Regions.Europe.Western Europe'       4248  -->   2981  1267   318  51824
			'Geography.Regions.Oceania'                     1824  -->   1223   601    86  54480
			'History and Society.Business and economics'    3056  -->   1603  1453   308  53026
			'History and Society.Education'                 1623  -->    778   845   110  54657
			'History and Society.History'                   6664  -->   4024  2640   976  48750
			'History and Society.Military and warfare'      5752  -->   3969  1783   646  49992
			'History and Society.Politics and government'   4556  -->   2398  2158   497  51337
			'History and Society.Society'                   6816  -->   3020  3796   607  48967
			'History and Society.Transportation'            3190  -->   2759   431   114  53086
			'STEM.Biology'                                  3744  -->   2946   798   181  52465
			'STEM.Chemistry'                                2119  -->   1575   544   349  53922
			'STEM.Computing'                                2592  -->   2096   496   261  53537
			'STEM.Earth and environment'                    1653  -->    898   755   156  54581
			'STEM.Engineering'                              2759  -->   2012   747   152  53479
			'STEM.Libraries & Information'                   513  -->    378   135    36  55841
			'STEM.Mathematics'                               564  -->    343   221    56  55770
			'STEM.Medicine & Health'                        2416  -->   1621   795   257  53717
			'STEM.Physics'                                  1402  -->    918   484   147  54841
			'STEM.STEM*'                                   18019  -->  16000  2019  1245  37126
			'STEM.Space'                                    2137  -->   1947   190    30  54223
			'STEM.Technology'                               4533  -->   3251  1282   552  51305
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.234         0.123
		Culture.Biography.Women                         0.065         0.015
		Culture.Food and drink                          0.024         0.002
		Culture.Internet culture                        0.051         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.089         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.047         0.011
		Culture.Media.Media*                            0.221         0.058
		Culture.Media.Music                             0.047         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.025         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.072         0.011
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
		Geography.Regions.Americas.North America        0.107         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.174         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.034         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.073         0.013
		Geography.Regions.Europe.Europe*                0.29          0.076
		Geography.Regions.Europe.Northern Europe        0.059         0.031
		Geography.Regions.Europe.Southern Europe        0.104         0.013
		Geography.Regions.Europe.Western Europe         0.075         0.019
		Geography.Regions.Oceania                       0.032         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.029         0.007
		History and Society.History                     0.118         0.011
		History and Society.Military and warfare        0.102         0.014
		History and Society.Politics and government     0.081         0.028
		History and Society.Society                     0.121         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.066         0.034
		STEM.Chemistry                                  0.038         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.029         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.01          0
		STEM.Medicine & Health                          0.043         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.32          0.069
		STEM.Space                                      0.038         0.006
		STEM.Technology                                 0.08          0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.124
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.065
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.018
		Geography.Geographical                       0.031
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.055
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.109
		Geography.Regions.Europe.Northern Europe     0.023
		Geography.Regions.Europe.Southern Europe     0.022
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.026
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.024
		History and Society.Society                  0.018
		History and Society.Transportation           0.015
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.008
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.009
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.092
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.891
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.974
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.985
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.992
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.908
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.745, macro=0.68):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.745
		Culture.Food and drink                       0.546
		Culture.Internet culture                     0.803
		Culture.Linguistics                          0.631
		Culture.Literature                           0.702
		Culture.Media.Books                          0.747
		Culture.Media.Entertainment                  0.489
		Culture.Media.Films                          0.841
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.782
		Culture.Media.Radio                          0.697
		Culture.Media.Software                       0.825
		Culture.Media.Television                     0.813
		Culture.Media.Video games                    0.911
		Culture.Performing arts                      0.484
		Culture.Philosophy and religion              0.497
		Culture.Sports                               0.873
		Culture.Visual arts.Architecture             0.573
		Culture.Visual arts.Comics and Anime         0.806
		Culture.Visual arts.Fashion                  0.493
		Culture.Visual arts.Visual arts*             0.585
		Geography.Geographical                       0.69
		Geography.Regions.Africa.Africa*             0.647
		Geography.Regions.Africa.Central Africa      0.452
		Geography.Regions.Africa.Eastern Africa      0.645
		Geography.Regions.Africa.Northern Africa     0.62
		Geography.Regions.Africa.Southern Africa     0.644
		Geography.Regions.Africa.Western Africa      0.664
		Geography.Regions.Americas.Central America   0.426
		Geography.Regions.Americas.North America     0.65
		Geography.Regions.Americas.South America     0.616
		Geography.Regions.Asia.Asia*                 0.762
		Geography.Regions.Asia.Central Asia          0.624
		Geography.Regions.Asia.East Asia             0.758
		Geography.Regions.Asia.North Asia            0.687
		Geography.Regions.Asia.South Asia            0.675
		Geography.Regions.Asia.Southeast Asia        0.66
		Geography.Regions.Asia.West Asia             0.662
		Geography.Regions.Europe.Eastern Europe      0.708
		Geography.Regions.Europe.Europe*             0.774
		Geography.Regions.Europe.Northern Europe     0.593
		Geography.Regions.Europe.Southern Europe     0.696
		Geography.Regions.Europe.Western Europe      0.702
		Geography.Regions.Oceania                    0.671
		History and Society.Business and economics   0.525
		History and Society.Education                0.479
		History and Society.History                  0.604
		History and Society.Military and warfare     0.69
		History and Society.Politics and government  0.526
		History and Society.Society                  0.443
		History and Society.Transportation           0.865
		STEM.Biology                                 0.787
		STEM.Chemistry                               0.743
		STEM.Computing                               0.809
		STEM.Earth and environment                   0.543
		STEM.Engineering                             0.729
		STEM.Libraries & Information                 0.737
		STEM.Mathematics                             0.608
		STEM.Medicine & Health                       0.671
		STEM.Physics                                 0.655
		STEM.STEM*                                   0.888
		STEM.Space                                   0.911
		STEM.Technology                              0.717
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.986
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.98
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.99
		History and Society.Society                  0.988
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.994
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.691, macro=0.546):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.637
		Culture.Food and drink                       0.308
		Culture.Internet culture                     0.403
		Culture.Linguistics                          0.688
		Culture.Literature                           0.555
		Culture.Media.Books                          0.584
		Culture.Media.Entertainment                  0.318
		Culture.Media.Films                          0.804
		Culture.Media.Media*                         0.651
		Culture.Media.Music                          0.845
		Culture.Media.Radio                          0.725
		Culture.Media.Software                       0.187
		Culture.Media.Television                     0.771
		Culture.Media.Video games                    0.753
		Culture.Performing arts                      0.414
		Culture.Philosophy and religion              0.382
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.626
		Culture.Visual arts.Comics and Anime         0.612
		Culture.Visual arts.Fashion                  0.481
		Culture.Visual arts.Visual arts*             0.587
		Geography.Geographical                       0.527
		Geography.Regions.Africa.Africa*             0.486
		Geography.Regions.Africa.Central Africa      0.195
		Geography.Regions.Africa.Eastern Africa      0.313
		Geography.Regions.Africa.Northern Africa     0.281
		Geography.Regions.Africa.Southern Africa     0.444
		Geography.Regions.Africa.Western Africa      0.486
		Geography.Regions.Americas.Central America   0.486
		Geography.Regions.Americas.North America     0.766
		Geography.Regions.Americas.South America     0.698
		Geography.Regions.Asia.Asia*                 0.673
		Geography.Regions.Asia.Central Asia          0.277
		Geography.Regions.Asia.East Asia             0.82
		Geography.Regions.Asia.North Asia            0.125
		Geography.Regions.Asia.South Asia            0.877
		Geography.Regions.Asia.Southeast Asia        0.713
		Geography.Regions.Asia.West Asia             0.632
		Geography.Regions.Europe.Eastern Europe      0.585
		Geography.Regions.Europe.Europe*             0.542
		Geography.Regions.Europe.Northern Europe     0.792
		Geography.Regions.Europe.Southern Europe     0.403
		Geography.Regions.Europe.Western Europe      0.692
		Geography.Regions.Oceania                    0.867
		History and Society.Business and economics   0.481
		History and Society.Education                0.639
		History and Society.History                  0.252
		History and Society.Military and warfare     0.436
		History and Society.Politics and government  0.614
		History and Society.Society                  0.316
		History and Society.Transportation           0.861
		STEM.Biology                                 0.888
		STEM.Chemistry                               0.153
		STEM.Computing                               0.31
		STEM.Earth and environment                   0.465
		STEM.Engineering                             0.575
		STEM.Libraries & Information                 0.416
		STEM.Mathematics                             0.202
		STEM.Medicine & Health                       0.476
		STEM.Physics                                 0.172
		STEM.STEM*                                   0.67
		STEM.Space                                   0.909
		STEM.Technology                              0.258
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.996
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
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.708, macro=0.583):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.857
		Culture.Biography.Women                      0.687
		Culture.Food and drink                       0.393
		Culture.Internet culture                     0.537
		Culture.Linguistics                          0.658
		Culture.Literature                           0.62
		Culture.Media.Books                          0.656
		Culture.Media.Entertainment                  0.386
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.738
		Culture.Media.Music                          0.812
		Culture.Media.Radio                          0.711
		Culture.Media.Software                       0.305
		Culture.Media.Television                     0.791
		Culture.Media.Video games                    0.824
		Culture.Performing arts                      0.446
		Culture.Philosophy and religion              0.432
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.598
		Culture.Visual arts.Comics and Anime         0.695
		Culture.Visual arts.Fashion                  0.487
		Culture.Visual arts.Visual arts*             0.586
		Geography.Geographical                       0.597
		Geography.Regions.Africa.Africa*             0.555
		Geography.Regions.Africa.Central Africa      0.272
		Geography.Regions.Africa.Eastern Africa      0.422
		Geography.Regions.Africa.Northern Africa     0.387
		Geography.Regions.Africa.Southern Africa     0.525
		Geography.Regions.Africa.Western Africa      0.562
		Geography.Regions.Americas.Central America   0.454
		Geography.Regions.Americas.North America     0.703
		Geography.Regions.Americas.South America     0.655
		Geography.Regions.Asia.Asia*                 0.715
		Geography.Regions.Asia.Central Asia          0.384
		Geography.Regions.Asia.East Asia             0.788
		Geography.Regions.Asia.North Asia            0.212
		Geography.Regions.Asia.South Asia            0.763
		Geography.Regions.Asia.Southeast Asia        0.685
		Geography.Regions.Asia.West Asia             0.647
		Geography.Regions.Europe.Eastern Europe      0.641
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.679
		Geography.Regions.Europe.Southern Europe     0.511
		Geography.Regions.Europe.Western Europe      0.697
		Geography.Regions.Oceania                    0.756
		History and Society.Business and economics   0.502
		History and Society.Education                0.548
		History and Society.History                  0.356
		History and Society.Military and warfare     0.534
		History and Society.Politics and government  0.567
		History and Society.Society                  0.369
		History and Society.Transportation           0.863
		STEM.Biology                                 0.835
		STEM.Chemistry                               0.254
		STEM.Computing                               0.448
		STEM.Earth and environment                   0.501
		STEM.Engineering                             0.643
		STEM.Libraries & Information                 0.531
		STEM.Mathematics                             0.303
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.273
		STEM.STEM*                                   0.764
		STEM.Space                                   0.91
		STEM.Technology                              0.379
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.988
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.933
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.976
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.977
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.993
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.962
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.015
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.014
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.054
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.02
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.01
		History and Society.Society                  0.012
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.006
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.968, macro=0.968):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.966
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.97
		Culture.Literature                           0.973
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.94
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.965
		Culture.Philosophy and religion              0.943
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.973
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.96
		Culture.Visual arts.Visual arts*             0.959
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.967
		Geography.Regions.Africa.Central Africa      0.971
		Geography.Regions.Africa.Eastern Africa      0.973
		Geography.Regions.Africa.Northern Africa     0.972
		Geography.Regions.Africa.Southern Africa     0.966
		Geography.Regions.Africa.Western Africa      0.92
		Geography.Regions.Americas.Central America   0.949
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.97
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.974
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.968
		Geography.Regions.Asia.West Asia             0.969
		Geography.Regions.Europe.Eastern Europe      0.972
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.961
		Geography.Regions.Europe.Southern Europe     0.965
		Geography.Regions.Europe.Western Europe      0.971
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.953
		History and Society.Education                0.958
		History and Society.History                  0.949
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.942
		History and Society.Society                  0.916
		History and Society.Transportation           0.984
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.963
		STEM.Engineering                             0.978
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.958
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.979
		STEM.STEM*                                   0.975
		STEM.Space                                   0.99
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.748, macro=0.563):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.914
		Culture.Biography.Women                      0.694
		Culture.Food and drink                       0.35
		Culture.Internet culture                     0.551
		Culture.Linguistics                          0.634
		Culture.Literature                           0.62
		Culture.Media.Books                          0.672
		Culture.Media.Entertainment                  0.282
		Culture.Media.Films                          0.829
		Culture.Media.Media*                         0.817
		Culture.Media.Music                          0.838
		Culture.Media.Radio                          0.455
		Culture.Media.Software                       0.274
		Culture.Media.Television                     0.824
		Culture.Media.Video games                    0.776
		Culture.Performing arts                      0.412
		Culture.Philosophy and religion              0.375
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.578
		Culture.Visual arts.Comics and Anime         0.733
		Culture.Visual arts.Fashion                  0.303
		Culture.Visual arts.Visual arts*             0.582
		Geography.Geographical                       0.618
		Geography.Regions.Africa.Africa*             0.55
		Geography.Regions.Africa.Central Africa      0.112
		Geography.Regions.Africa.Eastern Africa      0.205
		Geography.Regions.Africa.Northern Africa     0.286
		Geography.Regions.Africa.Southern Africa     0.344
		Geography.Regions.Africa.Western Africa      0.344
		Geography.Regions.Americas.Central America   0.355
		Geography.Regions.Americas.North America     0.777
		Geography.Regions.Americas.South America     0.614
		Geography.Regions.Asia.Asia*                 0.78
		Geography.Regions.Asia.Central Asia          0.226
		Geography.Regions.Asia.East Asia             0.822
		Geography.Regions.Asia.North Asia            0.191
		Geography.Regions.Asia.South Asia            0.807
		Geography.Regions.Asia.Southeast Asia        0.614
		Geography.Regions.Asia.West Asia             0.631
		Geography.Regions.Europe.Eastern Europe      0.686
		Geography.Regions.Europe.Europe*             0.728
		Geography.Regions.Europe.Northern Europe     0.722
		Geography.Regions.Europe.Southern Europe     0.529
		Geography.Regions.Europe.Western Europe      0.733
		Geography.Regions.Oceania                    0.802
		History and Society.Business and economics   0.441
		History and Society.Education                0.495
		History and Society.History                  0.37
		History and Society.Military and warfare     0.572
		History and Society.Politics and government  0.589
		History and Society.Society                  0.332
		History and Society.Transportation           0.905
		STEM.Biology                                 0.874
		STEM.Chemistry                               0.269
		STEM.Computing                               0.41
		STEM.Earth and environment                   0.443
		STEM.Engineering                             0.725
		STEM.Libraries & Information                 0.362
		STEM.Mathematics                             0.159
		STEM.Medicine & Health                       0.56
		STEM.Physics                                 0.267
		STEM.STEM*                                   0.871
		STEM.Space                                   0.949
		STEM.Technology                              0.488
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

