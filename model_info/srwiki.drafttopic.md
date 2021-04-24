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
	counts (n=56390):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13186  -->  11335  1851   897  42307
			'Culture.Biography.Women'                       3662  -->   2747   915   318  52410
			'Culture.Food and drink'                        1345  -->    735   610   185  54860
			'Culture.Internet culture'                      2898  -->   2322   576   211  53281
			'Culture.Linguistics'                           1515  -->    960   555   105  54770
			'Culture.Literature'                            5010  -->   3497  1513   464  50916
			'Culture.Media.Books'                           1534  -->   1156   378   120  54736
			'Culture.Media.Entertainment'                   2212  -->   1083  1129   199  53979
			'Culture.Media.Films'                           2650  -->   2231   419    96  53644
			'Culture.Media.Media*'                         12435  -->  10669  1766  1241  42714
			'Culture.Media.Music'                           2628  -->   2042   586   204  53558
			'Culture.Media.Radio'                            271  -->    189    82    30  56089
			'Culture.Media.Software'                        2204  -->   1822   382   256  53930
			'Culture.Media.Television'                      2349  -->   1917   432   121  53920
			'Culture.Media.Video games'                     1391  -->   1251   140    43  54956
			'Culture.Performing arts'                       1412  -->    691   721   118  54860
			'Culture.Philosophy and religion'               4071  -->   2034  2037   451  51868
			'Culture.Sports'                                5036  -->   4383   653   167  51187
			'Culture.Visual arts.Architecture'              1947  -->   1119   828   202  54241
			'Culture.Visual arts.Comics and Anime'          1301  -->   1032   269    84  55005
			'Culture.Visual arts.Fashion'                    633  -->    312   321    45  55712
			'Culture.Visual arts.Visual arts*'              4546  -->   2650  1896   402  51442
			'Geography.Geographical'                        4938  -->   3411  1527   766  50686
			'Geography.Regions.Africa.Africa*'              3767  -->   2397  1370   278  52345
			'Geography.Regions.Africa.Central Africa'        533  -->    232   301    42  55815
			'Geography.Regions.Africa.Eastern Africa'        440  -->    279   161    41  55909
			'Geography.Regions.Africa.Northern Africa'      1469  -->    909   560   101  54820
			'Geography.Regions.Africa.Southern Africa'       607  -->    387   220    37  55746
			'Geography.Regions.Africa.Western Africa'        149  -->     97    52    30  56211
			'Geography.Regions.Americas.Central America'    1299  -->    542   757    72  55019
			'Geography.Regions.Americas.North America'      6032  -->   3931  2101   712  49646
			'Geography.Regions.Americas.South America'      1528  -->    926   602    96  54766
			'Geography.Regions.Asia.Asia*'                  9808  -->   7441  2367   832  45750
			'Geography.Regions.Asia.Central Asia'           1089  -->    680   409    65  55236
			'Geography.Regions.Asia.East Asia'              2608  -->   1977   631    96  53686
			'Geography.Regions.Asia.North Asia'             1937  -->   1325   612   240  54213
			'Geography.Regions.Asia.South Asia'             1731  -->   1195   536    71  54588
			'Geography.Regions.Asia.Southeast Asia'         1564  -->   1028   536    98  54728
			'Geography.Regions.Asia.West Asia'              2682  -->   1776   906   240  53468
			'Geography.Regions.Europe.Eastern Europe'       4098  -->   2888  1210   352  51940
			'Geography.Regions.Europe.Europe*'             16372  -->  12618  3754  2139  37879
			'Geography.Regions.Europe.Northern Europe'      3349  -->   1979  1370   257  52784
			'Geography.Regions.Europe.Southern Europe'      5884  -->   4085  1799   696  49810
			'Geography.Regions.Europe.Western Europe'       4248  -->   2990  1258   330  51812
			'Geography.Regions.Oceania'                     1824  -->   1249   575    86  54480
			'History and Society.Business and economics'    3056  -->   1584  1472   290  53044
			'History and Society.Education'                 1623  -->    757   866   107  54660
			'History and Society.History'                   6664  -->   4024  2640   981  48745
			'History and Society.Military and warfare'      5752  -->   3943  1809   640  49998
			'History and Society.Politics and government'   4556  -->   2401  2155   476  51358
			'History and Society.Society'                   6816  -->   3029  3787   583  48991
			'History and Society.Transportation'            3190  -->   2772   418   114  53086
			'STEM.Biology'                                  3744  -->   2976   768   185  52461
			'STEM.Chemistry'                                2119  -->   1579   540   320  53951
			'STEM.Computing'                                2592  -->   2118   474   277  53521
			'STEM.Earth and environment'                    1653  -->    874   779   132  54605
			'STEM.Engineering'                              2759  -->   2032   727   140  53491
			'STEM.Libraries & Information'                   513  -->    386   127    25  55852
			'STEM.Mathematics'                               564  -->    332   232    56  55770
			'STEM.Medicine & Health'                        2416  -->   1617   799   248  53726
			'STEM.Physics'                                  1402  -->    934   468   144  54844
			'STEM.STEM*'                                   18019  -->  15998  2021  1272  37099
			'STEM.Space'                                    2137  -->   1939   198    29  54224
			'STEM.Technology'                               4533  -->   3238  1295   550  51307
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
		Culture.Food and drink                       0.005
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
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
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.055
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.01
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.016
		Geography.Regions.Europe.Europe*             0.108
		Geography.Regions.Europe.Northern Europe     0.023
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.011
		History and Society.Education                0.005
		History and Society.History                  0.026
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.024
		History and Society.Society                  0.017
		History and Society.Transportation           0.015
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.007
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
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
		Culture.Food and drink                       0.995
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
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
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.892
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.989
		History and Society.Education                0.995
		History and Society.History                  0.974
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.976
		History and Society.Society                  0.983
		History and Society.Transportation           0.985
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.993
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.908
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.745, macro=0.679):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.86
		Culture.Biography.Women                      0.75
		Culture.Food and drink                       0.546
		Culture.Internet culture                     0.801
		Culture.Linguistics                          0.634
		Culture.Literature                           0.698
		Culture.Media.Books                          0.754
		Culture.Media.Entertainment                  0.49
		Culture.Media.Films                          0.842
		Culture.Media.Media*                         0.858
		Culture.Media.Music                          0.777
		Culture.Media.Radio                          0.697
		Culture.Media.Software                       0.827
		Culture.Media.Television                     0.816
		Culture.Media.Video games                    0.899
		Culture.Performing arts                      0.489
		Culture.Philosophy and religion              0.5
		Culture.Sports                               0.87
		Culture.Visual arts.Architecture             0.575
		Culture.Visual arts.Comics and Anime         0.793
		Culture.Visual arts.Fashion                  0.493
		Culture.Visual arts.Visual arts*             0.583
		Geography.Geographical                       0.691
		Geography.Regions.Africa.Africa*             0.636
		Geography.Regions.Africa.Central Africa      0.435
		Geography.Regions.Africa.Eastern Africa      0.634
		Geography.Regions.Africa.Northern Africa     0.619
		Geography.Regions.Africa.Southern Africa     0.638
		Geography.Regions.Africa.Western Africa      0.651
		Geography.Regions.Americas.Central America   0.417
		Geography.Regions.Americas.North America     0.652
		Geography.Regions.Americas.South America     0.606
		Geography.Regions.Asia.Asia*                 0.759
		Geography.Regions.Asia.Central Asia          0.624
		Geography.Regions.Asia.East Asia             0.758
		Geography.Regions.Asia.North Asia            0.684
		Geography.Regions.Asia.South Asia            0.69
		Geography.Regions.Asia.Southeast Asia        0.657
		Geography.Regions.Asia.West Asia             0.662
		Geography.Regions.Europe.Eastern Europe      0.705
		Geography.Regions.Europe.Europe*             0.771
		Geography.Regions.Europe.Northern Europe     0.591
		Geography.Regions.Europe.Southern Europe     0.694
		Geography.Regions.Europe.Western Europe      0.704
		Geography.Regions.Oceania                    0.685
		History and Society.Business and economics   0.518
		History and Society.Education                0.466
		History and Society.History                  0.604
		History and Society.Military and warfare     0.686
		History and Society.Politics and government  0.527
		History and Society.Society                  0.444
		History and Society.Transportation           0.869
		STEM.Biology                                 0.795
		STEM.Chemistry                               0.745
		STEM.Computing                               0.817
		STEM.Earth and environment                   0.529
		STEM.Engineering                             0.736
		STEM.Libraries & Information                 0.752
		STEM.Mathematics                             0.589
		STEM.Medicine & Health                       0.669
		STEM.Physics                                 0.666
		STEM.STEM*                                   0.888
		STEM.Space                                   0.907
		STEM.Technology                              0.714
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
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
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
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.98
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.991
		History and Society.Society                  0.988
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.994
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.691, macro=0.547):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.853
		Culture.Biography.Women                      0.648
		Culture.Food and drink                       0.286
		Culture.Internet culture                     0.416
		Culture.Linguistics                          0.71
		Culture.Literature                           0.549
		Culture.Media.Books                          0.582
		Culture.Media.Entertainment                  0.324
		Culture.Media.Films                          0.834
		Culture.Media.Media*                         0.654
		Culture.Media.Music                          0.834
		Culture.Media.Radio                          0.738
		Culture.Media.Software                       0.189
		Culture.Media.Television                     0.764
		Culture.Media.Video games                    0.751
		Culture.Performing arts                      0.398
		Culture.Philosophy and religion              0.384
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.623
		Culture.Visual arts.Comics and Anime         0.534
		Culture.Visual arts.Fashion                  0.331
		Culture.Visual arts.Visual arts*             0.583
		Geography.Geographical                       0.528
		Geography.Regions.Africa.Africa*             0.486
		Geography.Regions.Africa.Central Africa      0.268
		Geography.Regions.Africa.Eastern Africa      0.282
		Geography.Regions.Africa.Northern Africa     0.292
		Geography.Regions.Africa.Southern Africa     0.531
		Geography.Regions.Africa.Western Africa      0.455
		Geography.Regions.Americas.Central America   0.514
		Geography.Regions.Americas.North America     0.76
		Geography.Regions.Americas.South America     0.687
		Geography.Regions.Asia.Asia*                 0.669
		Geography.Regions.Asia.Central Asia          0.315
		Geography.Regions.Asia.East Asia             0.831
		Geography.Regions.Asia.North Asia            0.125
		Geography.Regions.Asia.South Asia            0.891
		Geography.Regions.Asia.Southeast Asia        0.69
		Geography.Regions.Asia.West Asia             0.62
		Geography.Regions.Europe.Eastern Europe      0.576
		Geography.Regions.Europe.Europe*             0.543
		Geography.Regions.Europe.Northern Europe     0.794
		Geography.Regions.Europe.Southern Europe     0.4
		Geography.Regions.Europe.Western Europe      0.685
		Geography.Regions.Oceania                    0.87
		History and Society.Business and economics   0.493
		History and Society.Education                0.639
		History and Society.History                  0.251
		History and Society.Military and warfare     0.436
		History and Society.Politics and government  0.625
		History and Society.Society                  0.325
		History and Society.Transportation           0.861
		STEM.Biology                                 0.887
		STEM.Chemistry                               0.165
		STEM.Computing                               0.3
		STEM.Earth and environment                   0.5
		STEM.Engineering                             0.597
		STEM.Libraries & Information                 0.511
		STEM.Mathematics                             0.197
		STEM.Medicine & Health                       0.484
		STEM.Physics                                 0.178
		STEM.STEM*                                   0.665
		STEM.Space                                   0.911
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
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               1
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
	f1 (micro=0.708, macro=0.585):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.856
		Culture.Biography.Women                      0.695
		Culture.Food and drink                       0.376
		Culture.Internet culture                     0.548
		Culture.Linguistics                          0.67
		Culture.Literature                           0.615
		Culture.Media.Books                          0.657
		Culture.Media.Entertainment                  0.39
		Culture.Media.Films                          0.838
		Culture.Media.Media*                         0.742
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.717
		Culture.Media.Software                       0.307
		Culture.Media.Television                     0.789
		Culture.Media.Video games                    0.818
		Culture.Performing arts                      0.439
		Culture.Philosophy and religion              0.434
		Culture.Sports                               0.91
		Culture.Visual arts.Architecture             0.598
		Culture.Visual arts.Comics and Anime         0.638
		Culture.Visual arts.Fashion                  0.396
		Culture.Visual arts.Visual arts*             0.583
		Geography.Geographical                       0.599
		Geography.Regions.Africa.Africa*             0.551
		Geography.Regions.Africa.Central Africa      0.332
		Geography.Regions.Africa.Eastern Africa      0.391
		Geography.Regions.Africa.Northern Africa     0.397
		Geography.Regions.Africa.Southern Africa     0.579
		Geography.Regions.Africa.Western Africa      0.536
		Geography.Regions.Americas.Central America   0.461
		Geography.Regions.Americas.North America     0.702
		Geography.Regions.Americas.South America     0.644
		Geography.Regions.Asia.Asia*                 0.711
		Geography.Regions.Asia.Central Asia          0.419
		Geography.Regions.Asia.East Asia             0.793
		Geography.Regions.Asia.North Asia            0.212
		Geography.Regions.Asia.South Asia            0.778
		Geography.Regions.Asia.Southeast Asia        0.673
		Geography.Regions.Asia.West Asia             0.641
		Geography.Regions.Europe.Eastern Europe      0.634
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.677
		Geography.Regions.Europe.Southern Europe     0.507
		Geography.Regions.Europe.Western Europe      0.694
		Geography.Regions.Oceania                    0.766
		History and Society.Business and economics   0.505
		History and Society.Education                0.539
		History and Society.History                  0.355
		History and Society.Military and warfare     0.533
		History and Society.Politics and government  0.572
		History and Society.Society                  0.376
		History and Society.Transportation           0.865
		STEM.Biology                                 0.839
		STEM.Chemistry                               0.27
		STEM.Computing                               0.439
		STEM.Earth and environment                   0.514
		STEM.Engineering                             0.66
		STEM.Libraries & Information                 0.609
		STEM.Mathematics                             0.295
		STEM.Medicine & Health                       0.562
		STEM.Physics                                 0.281
		STEM.STEM*                                   0.761
		STEM.Space                                   0.909
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
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
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
		History and Society.Politics and government  0.989
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
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.933
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.982
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.976
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.978
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.994
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
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
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.015
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
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
		Geography.Regions.Europe.Europe*             0.053
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.02
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.009
		History and Society.Society                  0.012
		History and Society.Transportation           0.002
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.006
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.033
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.968, macro=0.968):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.968
		Culture.Internet culture                     0.982
		Culture.Linguistics                          0.969
		Culture.Literature                           0.974
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.947
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.983
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.964
		Culture.Philosophy and religion              0.943
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.961
		Culture.Visual arts.Visual arts*             0.959
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.97
		Geography.Regions.Africa.Eastern Africa      0.975
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.966
		Geography.Regions.Africa.Western Africa      0.874
		Geography.Regions.Americas.Central America   0.952
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.974
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.974
		Geography.Regions.Asia.Southeast Asia        0.967
		Geography.Regions.Asia.West Asia             0.969
		Geography.Regions.Europe.Eastern Europe      0.972
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.962
		Geography.Regions.Europe.Southern Europe     0.966
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.953
		History and Society.Education                0.958
		History and Society.History                  0.949
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.943
		History and Society.Society                  0.917
		History and Society.Transportation           0.984
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.985
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.963
		STEM.Engineering                             0.978
		STEM.Libraries & Information                 0.964
		STEM.Mathematics                             0.957
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.979
		STEM.STEM*                                   0.975
		STEM.Space                                   0.991
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.752, macro=0.57):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.918
		Culture.Biography.Women                      0.718
		Culture.Food and drink                       0.295
		Culture.Internet culture                     0.61
		Culture.Linguistics                          0.639
		Culture.Literature                           0.661
		Culture.Media.Books                          0.65
		Culture.Media.Entertainment                  0.262
		Culture.Media.Films                          0.88
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.819
		Culture.Media.Radio                          0.513
		Culture.Media.Software                       0.32
		Culture.Media.Television                     0.82
		Culture.Media.Video games                    0.846
		Culture.Performing arts                      0.327
		Culture.Philosophy and religion              0.39
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.585
		Culture.Visual arts.Comics and Anime         0.693
		Culture.Visual arts.Fashion                  0.214
		Culture.Visual arts.Visual arts*             0.578
		Geography.Geographical                       0.619
		Geography.Regions.Africa.Africa*             0.547
		Geography.Regions.Africa.Central Africa      0.166
		Geography.Regions.Africa.Eastern Africa      0.203
		Geography.Regions.Africa.Northern Africa     0.313
		Geography.Regions.Africa.Southern Africa     0.452
		Geography.Regions.Africa.Western Africa      0.344
		Geography.Regions.Americas.Central America   0.371
		Geography.Regions.Americas.North America     0.788
		Geography.Regions.Americas.South America     0.634
		Geography.Regions.Asia.Asia*                 0.786
		Geography.Regions.Asia.Central Asia          0.251
		Geography.Regions.Asia.East Asia             0.817
		Geography.Regions.Asia.North Asia            0.191
		Geography.Regions.Asia.South Asia            0.821
		Geography.Regions.Asia.Southeast Asia        0.593
		Geography.Regions.Asia.West Asia             0.649
		Geography.Regions.Europe.Eastern Europe      0.681
		Geography.Regions.Europe.Europe*             0.731
		Geography.Regions.Europe.Northern Europe     0.729
		Geography.Regions.Europe.Southern Europe     0.527
		Geography.Regions.Europe.Western Europe      0.738
		Geography.Regions.Oceania                    0.795
		History and Society.Business and economics   0.487
		History and Society.Education                0.489
		History and Society.History                  0.369
		History and Society.Military and warfare     0.581
		History and Society.Politics and government  0.588
		History and Society.Society                  0.334
		History and Society.Transportation           0.905
		STEM.Biology                                 0.876
		STEM.Chemistry                               0.28
		STEM.Computing                               0.418
		STEM.Earth and environment                   0.46
		STEM.Engineering                             0.689
		STEM.Libraries & Information                 0.487
		STEM.Mathematics                             0.136
		STEM.Medicine & Health                       0.583
		STEM.Physics                                 0.237
		STEM.STEM*                                   0.87
		STEM.Space                                   0.938
		STEM.Technology                              0.485
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

