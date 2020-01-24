Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'max_depth': 5, 'multilabel': True, 'random_state': None, 'min_samples_split': 2, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'warm_start': False, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'max_features': 'log2', 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'min_impurity_split': None, 'subsample': 1.0, 'presort': 'auto', 'population_rates': None, 'label_weights': {}, 'verbose': 0, 'min_samples_leaf': 1, 'learning_rate': 0.1, 'validation_fraction': 0.1, 'init': None, 'n_estimators': 150, 'max_leaf_nodes': None, 'scale': False, 'tol': 0.0001, 'center': False}
	Environment:
	 - revscoring_version: '2.6.4-mmap'
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
	counts (n=60150):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15672  -->  14032  1640   871  43607
			'Culture.Biography.Women'                       4475  -->   3413  1062   436  55239
			'Culture.Food and drink'                        1819  -->   1471   348    86  58245
			'Culture.Internet culture'                      3397  -->   2789   608   237  56516
			'Culture.Linguistics'                           1625  -->   1194   431    77  58448
			'Culture.Literature'                            5881  -->   4544  1337   444  53825
			'Culture.Media.Books'                           1634  -->   1274   360    87  58429
			'Culture.Media.Entertainment'                   2333  -->   1324  1009   194  57623
			'Culture.Media.Films'                           2960  -->   2499   461   127  57063
			'Culture.Media.Media*'                         15008  -->  13056  1952  1486  43656
			'Culture.Media.Music'                           3173  -->   2591   582   274  56703
			'Culture.Media.Radio'                            699  -->    461   238    53  59398
			'Culture.Media.Software'                        2364  -->   1918   446   346  57440
			'Culture.Media.Television'                      2484  -->   1792   692   143  57523
			'Culture.Media.Video games'                     2223  -->   2002   221    48  57879
			'Culture.Performing arts'                       1501  -->    959   542   120  58529
			'Culture.Philosophy and religion'               3876  -->   2194  1682   295  55979
			'Culture.Sports'                                4964  -->   4327   637   188  54998
			'Culture.Visual arts.Architecture'              2131  -->   1546   585   198  57821
			'Culture.Visual arts.Comics and Anime'          2410  -->   2121   289   131  57609
			'Culture.Visual arts.Fashion'                   1336  -->   1018   318    74  58740
			'Culture.Visual arts.Visual arts*'              6373  -->   4818  1555   414  53363
			'Geography.Geographical'                        3933  -->   2690  1243   546  55671
			'Geography.Regions.Africa.Africa*'              3848  -->   2920   928   220  56082
			'Geography.Regions.Africa.Central Africa'         31  -->      8    23    14  60105
			'Geography.Regions.Africa.Eastern Africa'        482  -->    377   105    59  59609
			'Geography.Regions.Africa.Northern Africa'      1522  -->   1156   366    94  58534
			'Geography.Regions.Africa.Southern Africa'       685  -->    524   161    41  59424
			'Geography.Regions.Africa.Western Africa'        281  -->    190    91    40  59829
			'Geography.Regions.Americas.Central America'    1372  -->    977   395    58  58720
			'Geography.Regions.Americas.North America'      6575  -->   4254  2321   907  52668
			'Geography.Regions.Americas.South America'      1548  -->   1161   387   101  58501
			'Geography.Regions.Asia.Asia*'                 14972  -->  12548  2424  1396  43782
			'Geography.Regions.Asia.Central Asia'           1337  -->   1049   288    73  58740
			'Geography.Regions.Asia.East Asia'              7339  -->   5957  1382   689  52122
			'Geography.Regions.Asia.North Asia'             1895  -->   1461   434   196  58059
			'Geography.Regions.Asia.South Asia'             1895  -->   1469   426    47  58208
			'Geography.Regions.Asia.Southeast Asia'         1955  -->   1436   519   100  58095
			'Geography.Regions.Asia.West Asia'              2422  -->   1803   619   151  57577
			'Geography.Regions.Europe.Eastern Europe'       3438  -->   2684   754   271  56441
			'Geography.Regions.Europe.Europe*'             13539  -->  10934  2605  1546  45065
			'Geography.Regions.Europe.Northern Europe'      3935  -->   2797  1138   330  55885
			'Geography.Regions.Europe.Southern Europe'      3358  -->   2492   866   254  56538
			'Geography.Regions.Europe.Western Europe'       4055  -->   2998  1057   374  55721
			'Geography.Regions.Oceania'                     1799  -->   1297   502    83  58268
			'History and Society.Business and economics'    3922  -->   2441  1481   364  55864
			'History and Society.Education'                 1913  -->   1259   654   104  58133
			'History and Society.History'                   5571  -->   3403  2168   529  54050
			'History and Society.Military and warfare'      5194  -->   3684  1510   413  54543
			'History and Society.Politics and government'   5121  -->   3044  2077   503  54526
			'History and Society.Society'                   6681  -->   3218  3463   494  52975
			'History and Society.Transportation'            3741  -->   3369   372   141  56268
			'STEM.Biology'                                  3435  -->   2813   622   159  56556
			'STEM.Chemistry'                                1504  -->   1244   260   114  58532
			'STEM.Computing'                                2806  -->   2335   471   373  56971
			'STEM.Earth and environment'                    1895  -->   1333   562   113  58142
			'STEM.Engineering'                              2650  -->   2010   640   157  57343
			'STEM.Libraries & Information'                   781  -->    565   216    38  59331
			'STEM.Mathematics'                              1168  -->    962   206    55  58927
			'STEM.Medicine & Health'                        2004  -->   1451   553   129  58017
			'STEM.Physics'                                  1520  -->   1204   316   149  58481
			'STEM.STEM*'                                   17833  -->  15823  2010   918  41399
			'STEM.Space'                                    1710  -->   1584   126    28  58412
			'STEM.Technology'                               4761  -->   3576  1185   613  54776
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.261         0.123
		Culture.Biography.Women                         0.074         0.015
		Culture.Food and drink                          0.03          0.002
		Culture.Internet culture                        0.056         0.004
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.098         0.016
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.25          0.059
		Culture.Media.Music                             0.053         0.024
		Culture.Media.Radio                             0.012         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.037         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.064         0.011
		Culture.Sports                                  0.083         0.071
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.106         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.064         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.109         0.064
		Geography.Regions.Americas.South America        0.026         0.006
		Geography.Regions.Asia.Asia*                    0.249         0.046
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.122         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.032         0.015
		Geography.Regions.Asia.Southeast Asia           0.033         0.006
		Geography.Regions.Asia.West Asia                0.04          0.011
		Geography.Regions.Europe.Eastern Europe         0.057         0.013
		Geography.Regions.Europe.Europe*                0.225         0.076
		Geography.Regions.Europe.Northern Europe        0.065         0.031
		Geography.Regions.Europe.Southern Europe        0.056         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.065         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.086         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.111         0.013
		History and Society.Transportation              0.062         0.015
		STEM.Biology                                    0.057         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.044         0.005
		STEM.Libraries & Information                    0.013         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.296         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.079         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.082
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.065
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.068
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.022
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.092
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.015
		History and Society.Transportation           0.016
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.003
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.918
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.932
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.908
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.985
		History and Society.Transportation           0.984
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.787, macro=0.748):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.763
		Culture.Food and drink                       0.809
		Culture.Internet culture                     0.821
		Culture.Linguistics                          0.735
		Culture.Literature                           0.773
		Culture.Media.Books                          0.78
		Culture.Media.Entertainment                  0.568
		Culture.Media.Films                          0.844
		Culture.Media.Media*                         0.87
		Culture.Media.Music                          0.817
		Culture.Media.Radio                          0.66
		Culture.Media.Software                       0.811
		Culture.Media.Television                     0.721
		Culture.Media.Video games                    0.901
		Culture.Performing arts                      0.639
		Culture.Philosophy and religion              0.566
		Culture.Sports                               0.872
		Culture.Visual arts.Architecture             0.725
		Culture.Visual arts.Comics and Anime         0.88
		Culture.Visual arts.Fashion                  0.762
		Culture.Visual arts.Visual arts*             0.756
		Geography.Geographical                       0.684
		Geography.Regions.Africa.Africa*             0.759
		Geography.Regions.Africa.Central Africa      0.258
		Geography.Regions.Africa.Eastern Africa      0.782
		Geography.Regions.Africa.Northern Africa     0.76
		Geography.Regions.Africa.Southern Africa     0.765
		Geography.Regions.Africa.Western Africa      0.676
		Geography.Regions.Americas.Central America   0.712
		Geography.Regions.Americas.North America     0.647
		Geography.Regions.Americas.South America     0.75
		Geography.Regions.Asia.Asia*                 0.838
		Geography.Regions.Asia.Central Asia          0.785
		Geography.Regions.Asia.East Asia             0.812
		Geography.Regions.Asia.North Asia            0.771
		Geography.Regions.Asia.South Asia            0.775
		Geography.Regions.Asia.Southeast Asia        0.735
		Geography.Regions.Asia.West Asia             0.744
		Geography.Regions.Europe.Eastern Europe      0.781
		Geography.Regions.Europe.Europe*             0.808
		Geography.Regions.Europe.Northern Europe     0.711
		Geography.Regions.Europe.Southern Europe     0.742
		Geography.Regions.Europe.Western Europe      0.739
		Geography.Regions.Oceania                    0.721
		History and Society.Business and economics   0.622
		History and Society.Education                0.658
		History and Society.History                  0.611
		History and Society.Military and warfare     0.709
		History and Society.Politics and government  0.594
		History and Society.Society                  0.482
		History and Society.Transportation           0.901
		STEM.Biology                                 0.819
		STEM.Chemistry                               0.827
		STEM.Computing                               0.832
		STEM.Earth and environment                   0.703
		STEM.Engineering                             0.758
		STEM.Libraries & Information                 0.723
		STEM.Mathematics                             0.824
		STEM.Medicine & Health                       0.724
		STEM.Physics                                 0.792
		STEM.STEM*                                   0.887
		STEM.Space                                   0.926
		STEM.Technology                              0.751
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   1
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.719, macro=0.581):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.59
		Culture.Food and drink                       0.575
		Culture.Internet culture                     0.409
		Culture.Linguistics                          0.805
		Culture.Literature                           0.598
		Culture.Media.Books                          0.68
		Culture.Media.Entertainment                  0.378
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.622
		Culture.Media.Music                          0.806
		Culture.Media.Radio                          0.615
		Culture.Media.Software                       0.153
		Culture.Media.Television                     0.721
		Culture.Media.Video games                    0.74
		Culture.Performing arts                      0.475
		Culture.Philosophy and religion              0.538
		Culture.Sports                               0.952
		Culture.Visual arts.Architecture             0.694
		Culture.Visual arts.Comics and Anime         0.461
		Culture.Visual arts.Fashion                  0.329
		Culture.Visual arts.Visual arts*             0.647
		Geography.Geographical                       0.63
		Geography.Regions.Africa.Africa*             0.604
		Geography.Regions.Africa.Central Africa      0.005
		Geography.Regions.Africa.Eastern Africa      0.265
		Geography.Regions.Africa.Northern Africa     0.368
		Geography.Regions.Africa.Southern Africa     0.566
		Geography.Regions.Africa.Western Africa      0.409
		Geography.Regions.Americas.Central America   0.705
		Geography.Regions.Americas.North America     0.724
		Geography.Regions.Americas.South America     0.734
		Geography.Regions.Asia.Asia*                 0.564
		Geography.Regions.Asia.Central Asia          0.354
		Geography.Regions.Asia.East Asia             0.418
		Geography.Regions.Asia.North Asia            0.175
		Geography.Regions.Asia.South Asia            0.937
		Geography.Regions.Asia.Southeast Asia        0.721
		Geography.Regions.Asia.West Asia             0.758
		Geography.Regions.Europe.Eastern Europe      0.68
		Geography.Regions.Europe.Europe*             0.668
		Geography.Regions.Europe.Northern Europe     0.793
		Geography.Regions.Europe.Southern Europe     0.687
		Geography.Regions.Europe.Western Europe      0.684
		Geography.Regions.Oceania                    0.886
		History and Society.Business and economics   0.495
		History and Society.Education                0.732
		History and Society.History                  0.409
		History and Society.Military and warfare     0.574
		History and Society.Politics and government  0.654
		History and Society.Society                  0.4
		History and Society.Transportation           0.847
		STEM.Biology                                 0.91
		STEM.Chemistry                               0.399
		STEM.Computing                               0.257
		STEM.Earth and environment                   0.623
		STEM.Engineering                             0.594
		STEM.Libraries & Information                 0.413
		STEM.Mathematics                             0.269
		STEM.Medicine & Health                       0.678
		STEM.Physics                                 0.209
		STEM.STEM*                                   0.752
		STEM.Space                                   0.921
		STEM.Technology                              0.259
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       1
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
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
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.745, macro=0.632):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.88
		Culture.Biography.Women                      0.665
		Culture.Food and drink                       0.672
		Culture.Internet culture                     0.546
		Culture.Linguistics                          0.768
		Culture.Literature                           0.674
		Culture.Media.Books                          0.726
		Culture.Media.Entertainment                  0.454
		Culture.Media.Films                          0.822
		Culture.Media.Media*                         0.725
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.637
		Culture.Media.Software                       0.257
		Culture.Media.Television                     0.721
		Culture.Media.Video games                    0.812
		Culture.Performing arts                      0.545
		Culture.Philosophy and religion              0.551
		Culture.Sports                               0.91
		Culture.Visual arts.Architecture             0.71
		Culture.Visual arts.Comics and Anime         0.605
		Culture.Visual arts.Fashion                  0.46
		Culture.Visual arts.Visual arts*             0.697
		Geography.Geographical                       0.656
		Geography.Regions.Africa.Africa*             0.673
		Geography.Regions.Africa.Central Africa      0.009
		Geography.Regions.Africa.Eastern Africa      0.396
		Geography.Regions.Africa.Northern Africa     0.496
		Geography.Regions.Africa.Southern Africa     0.651
		Geography.Regions.Africa.Western Africa      0.51
		Geography.Regions.Americas.Central America   0.709
		Geography.Regions.Americas.North America     0.683
		Geography.Regions.Americas.South America     0.742
		Geography.Regions.Asia.Asia*                 0.674
		Geography.Regions.Asia.Central Asia          0.488
		Geography.Regions.Asia.East Asia             0.552
		Geography.Regions.Asia.North Asia            0.285
		Geography.Regions.Asia.South Asia            0.848
		Geography.Regions.Asia.Southeast Asia        0.728
		Geography.Regions.Asia.West Asia             0.751
		Geography.Regions.Europe.Eastern Europe      0.727
		Geography.Regions.Europe.Europe*             0.731
		Geography.Regions.Europe.Northern Europe     0.749
		Geography.Regions.Europe.Southern Europe     0.713
		Geography.Regions.Europe.Western Europe      0.711
		Geography.Regions.Oceania                    0.795
		History and Society.Business and economics   0.551
		History and Society.Education                0.693
		History and Society.History                  0.49
		History and Society.Military and warfare     0.635
		History and Society.Politics and government  0.623
		History and Society.Society                  0.437
		History and Society.Transportation           0.873
		STEM.Biology                                 0.862
		STEM.Chemistry                               0.539
		STEM.Computing                               0.392
		STEM.Earth and environment                   0.661
		STEM.Engineering                             0.666
		STEM.Libraries & Information                 0.526
		STEM.Mathematics                             0.406
		STEM.Medicine & Health                       0.7
		STEM.Physics                                 0.331
		STEM.STEM*                                   0.814
		STEM.Space                                   0.924
		STEM.Technology                              0.386
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.955
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.996
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.98
		History and Society.Society                  0.984
		History and Society.Transportation           0.996
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.02
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.033
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.031
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.033
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.987
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.982
		Culture.Literature                           0.98
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.973
		Culture.Media.Films                          0.984
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.975
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.962
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.705
		Geography.Regions.Africa.Eastern Africa      0.975
		Geography.Regions.Africa.Northern Africa     0.982
		Geography.Regions.Africa.Southern Africa     0.979
		Geography.Regions.Africa.Western Africa      0.962
		Geography.Regions.Americas.Central America   0.98
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.984
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.985
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.981
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.98
		History and Society.Business and economics   0.968
		History and Society.Education                0.978
		History and Society.History                  0.96
		History and Society.Military and warfare     0.973
		History and Society.Politics and government  0.962
		History and Society.Society                  0.932
		History and Society.Transportation           0.985
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.987
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.98
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.982
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.978
		STEM.Space                                   0.991
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.8, macro=0.664):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.668
		Culture.Food and drink                       0.764
		Culture.Internet culture                     0.654
		Culture.Linguistics                          0.8
		Culture.Literature                           0.76
		Culture.Media.Books                          0.775
		Culture.Media.Entertainment                  0.447
		Culture.Media.Films                          0.873
		Culture.Media.Media*                         0.851
		Culture.Media.Music                          0.843
		Culture.Media.Radio                          0.542
		Culture.Media.Software                       0.355
		Culture.Media.Television                     0.738
		Culture.Media.Video games                    0.87
		Culture.Performing arts                      0.551
		Culture.Philosophy and religion              0.572
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.729
		Culture.Visual arts.Comics and Anime         0.734
		Culture.Visual arts.Fashion                  0.412
		Culture.Visual arts.Visual arts*             0.762
		Geography.Geographical                       0.676
		Geography.Regions.Africa.Africa*             0.73
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.257
		Geography.Regions.Africa.Northern Africa     0.45
		Geography.Regions.Africa.Southern Africa     0.603
		Geography.Regions.Africa.Western Africa      0.319
		Geography.Regions.Americas.Central America   0.707
		Geography.Regions.Americas.North America     0.742
		Geography.Regions.Americas.South America     0.77
		Geography.Regions.Asia.Asia*                 0.775
		Geography.Regions.Asia.Central Asia          0.513
		Geography.Regions.Asia.East Asia             0.622
		Geography.Regions.Asia.North Asia            0.331
		Geography.Regions.Asia.South Asia            0.898
		Geography.Regions.Asia.Southeast Asia        0.775
		Geography.Regions.Asia.West Asia             0.797
		Geography.Regions.Europe.Eastern Europe      0.783
		Geography.Regions.Europe.Europe*             0.786
		Geography.Regions.Europe.Northern Europe     0.811
		Geography.Regions.Europe.Southern Europe     0.745
		Geography.Regions.Europe.Western Europe      0.739
		Geography.Regions.Oceania                    0.846
		History and Society.Business and economics   0.522
		History and Society.Education                0.706
		History and Society.History                  0.522
		History and Society.Military and warfare     0.689
		History and Society.Politics and government  0.654
		History and Society.Society                  0.401
		History and Society.Transportation           0.891
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.573
		STEM.Computing                               0.547
		STEM.Earth and environment                   0.699
		STEM.Engineering                             0.722
		STEM.Libraries & Information                 0.416
		STEM.Mathematics                             0.526
		STEM.Medicine & Health                       0.718
		STEM.Physics                                 0.376
		STEM.STEM*                                   0.913
		STEM.Space                                   0.954
		STEM.Technology                              0.513
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'Culture.Media.Radio': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability'}

