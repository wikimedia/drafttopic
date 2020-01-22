Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'min_impurity_split': None, 'random_state': None, 'n_estimators': 150, 'criterion': 'friedman_mse', 'label_weights': {}, 'warm_start': False, 'min_samples_split': 2, 'learning_rate': 0.1, 'max_depth': 5, 'n_iter_no_change': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_weight_fraction_leaf': 0.0, 'validation_fraction': 0.1, 'max_features': 'log2', 'center': False, 'max_leaf_nodes': None, 'tol': 0.0001, 'multilabel': True, 'presort': 'auto', 'scale': False, 'loss': 'deviance', 'subsample': 1.0, 'verbose': 0, 'init': None, 'min_samples_leaf': 1, 'population_rates': None, 'min_impurity_decrease': 0.0}
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
	counts (n=63014):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16614  -->  14943  1671  1099  45301
			'Culture.Biography.Women'                       4129  -->   3223   906   775  58110
			'Culture.Food and drink'                        1318  -->    991   327    62  61634
			'Culture.Internet culture'                      2936  -->   2388   548   185  59893
			'Culture.Linguistics'                           1345  -->   1035   310    77  61592
			'Culture.Literature'                            5321  -->   4011  1310   526  57167
			'Culture.Media.Books'                           1864  -->   1331   533   178  60972
			'Culture.Media.Entertainment'                   1804  -->    993   811   189  61021
			'Culture.Media.Films'                           2276  -->   1891   385   152  60586
			'Culture.Media.Media*'                         14363  -->  12393  1970  1481  47170
			'Culture.Media.Music'                           2669  -->   2203   466   290  60055
			'Culture.Media.Radio'                           1177  -->    965   212    32  61805
			'Culture.Media.Software'                        1810  -->   1149   661   346  60858
			'Culture.Media.Television'                      2229  -->   1615   614   190  60595
			'Culture.Media.Video games'                     2073  -->   1897   176    36  60905
			'Culture.Performing arts'                       1328  -->    943   385   105  61581
			'Culture.Philosophy and religion'               2619  -->   1484  1135   328  60067
			'Culture.Sports'                                5868  -->   5324   544   324  56822
			'Culture.Visual arts.Architecture'              2526  -->   1879   647   280  60208
			'Culture.Visual arts.Comics and Anime'          1543  -->   1259   284   104  61367
			'Culture.Visual arts.Fashion'                   1184  -->    958   226    47  61783
			'Culture.Visual arts.Visual arts*'              5986  -->   4696  1290   545  56483
			'Geography.Geographical'                        3512  -->   2414  1098   285  59217
			'Geography.Regions.Africa.Africa*'              5645  -->   4899   746   226  57143
			'Geography.Regions.Africa.Central Africa'         66  -->     12    54    27  62921
			'Geography.Regions.Africa.Eastern Africa'       1117  -->    919   198    32  61865
			'Geography.Regions.Africa.Northern Africa'      1300  -->    969   331    77  61637
			'Geography.Regions.Africa.Southern Africa'      1241  -->    979   262    43  61730
			'Geography.Regions.Africa.Western Africa'       1134  -->    944   190    69  61811
			'Geography.Regions.Americas.Central America'    1294  -->    925   369    76  61644
			'Geography.Regions.Americas.North America'      7483  -->   5240  2243  1232  54299
			'Geography.Regions.Americas.South America'      1548  -->   1184   364   132  61334
			'Geography.Regions.Asia.Asia*'                 11087  -->   9622  1465   843  51084
			'Geography.Regions.Asia.Central Asia'           1117  -->    881   236    52  61845
			'Geography.Regions.Asia.East Asia'              2693  -->   2162   531   252  60069
			'Geography.Regions.Asia.North Asia'             1391  -->    965   426   189  61434
			'Geography.Regions.Asia.South Asia'             2402  -->   2088   314   118  60494
			'Geography.Regions.Asia.Southeast Asia'         1684  -->   1340   344    84  61246
			'Geography.Regions.Asia.West Asia'              2297  -->   1812   485   138  60579
			'Geography.Regions.Europe.Eastern Europe'       3086  -->   2427   659   270  59658
			'Geography.Regions.Europe.Europe*'             12498  -->   9741  2757  1870  48646
			'Geography.Regions.Europe.Northern Europe'      4230  -->   2897  1333   629  58155
			'Geography.Regions.Europe.Southern Europe'      2412  -->   1706   706   265  60337
			'Geography.Regions.Europe.Western Europe'       3171  -->   2110  1061   408  59435
			'Geography.Regions.Oceania'                     2560  -->   2131   429   113  60341
			'History and Society.Business and economics'    3536  -->   1781  1755   536  58942
			'History and Society.Education'                 2148  -->   1138  1010   260  60606
			'History and Society.History'                   3316  -->   1581  1735   486  59212
			'History and Society.Military and warfare'      3992  -->   2902  1090   385  58637
			'History and Society.Politics and government'   4564  -->   2946  1618   483  57967
			'History and Society.Society'                   4022  -->   1669  2353   388  58604
			'History and Society.Transportation'            3621  -->   3161   460   230  59163
			'STEM.Biology'                                  2816  -->   2330   486   133  60065
			'STEM.Chemistry'                                1336  -->    978   358   169  61509
			'STEM.Computing'                                2045  -->   1463   582   399  60570
			'STEM.Earth and environment'                    1615  -->   1170   445   101  61298
			'STEM.Engineering'                              2281  -->   1710   571   176  60557
			'STEM.Libraries & Information'                  1160  -->    734   426    58  61796
			'STEM.Mathematics'                              1143  -->    896   247    59  61812
			'STEM.Medicine & Health'                        1746  -->   1203   543   166  61102
			'STEM.Physics'                                  1222  -->    856   366   131  61661
			'STEM.STEM*'                                   16404  -->  14353  2051   968  45642
			'STEM.Space'                                    1395  -->   1250   145    54  61565
			'STEM.Technology'                               3670  -->   2435  1235   562  58782
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.264         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.047         0.004
		Culture.Linguistics                             0.021         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.228         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.029         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.093         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.056         0.024
		Geography.Regions.Africa.Africa*                0.09          0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.176         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.198         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.05          0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.053         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
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
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.066
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.013
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.012
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.08
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
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
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
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.934
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.988
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.92
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.791, macro=0.739):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.781
		Culture.Food and drink                       0.752
		Culture.Internet culture                     0.813
		Culture.Linguistics                          0.77
		Culture.Literature                           0.754
		Culture.Media.Books                          0.714
		Culture.Media.Entertainment                  0.55
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.863
		Culture.Media.Music                          0.825
		Culture.Media.Radio                          0.82
		Culture.Media.Software                       0.635
		Culture.Media.Television                     0.725
		Culture.Media.Video games                    0.915
		Culture.Performing arts                      0.71
		Culture.Philosophy and religion              0.567
		Culture.Sports                               0.907
		Culture.Visual arts.Architecture             0.744
		Culture.Visual arts.Comics and Anime         0.816
		Culture.Visual arts.Fashion                  0.809
		Culture.Visual arts.Visual arts*             0.784
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.868
		Geography.Regions.Africa.Central Africa      0.182
		Geography.Regions.Africa.Eastern Africa      0.823
		Geography.Regions.Africa.Northern Africa     0.745
		Geography.Regions.Africa.Southern Africa     0.789
		Geography.Regions.Africa.Western Africa      0.832
		Geography.Regions.Americas.Central America   0.715
		Geography.Regions.Americas.North America     0.7
		Geography.Regions.Americas.South America     0.765
		Geography.Regions.Asia.Asia*                 0.868
		Geography.Regions.Asia.Central Asia          0.789
		Geography.Regions.Asia.East Asia             0.803
		Geography.Regions.Asia.North Asia            0.694
		Geography.Regions.Asia.South Asia            0.869
		Geography.Regions.Asia.Southeast Asia        0.796
		Geography.Regions.Asia.West Asia             0.789
		Geography.Regions.Europe.Eastern Europe      0.786
		Geography.Regions.Europe.Europe*             0.779
		Geography.Regions.Europe.Northern Europe     0.685
		Geography.Regions.Europe.Southern Europe     0.707
		Geography.Regions.Europe.Western Europe      0.665
		Geography.Regions.Oceania                    0.832
		History and Society.Business and economics   0.504
		History and Society.Education                0.53
		History and Society.History                  0.477
		History and Society.Military and warfare     0.727
		History and Society.Politics and government  0.645
		History and Society.Society                  0.415
		History and Society.Transportation           0.873
		STEM.Biology                                 0.827
		STEM.Chemistry                               0.732
		STEM.Computing                               0.715
		STEM.Earth and environment                   0.724
		STEM.Engineering                             0.75
		STEM.Libraries & Information                 0.633
		STEM.Mathematics                             0.784
		STEM.Medicine & Health                       0.689
		STEM.Physics                                 0.7
		STEM.STEM*                                   0.875
		STEM.Space                                   0.896
		STEM.Technology                              0.663
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.713, macro=0.58):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.842
		Culture.Biography.Women                      0.467
		Culture.Food and drink                       0.649
		Culture.Internet culture                     0.481
		Culture.Linguistics                          0.82
		Culture.Literature                           0.566
		Culture.Media.Books                          0.498
		Culture.Media.Entertainment                  0.391
		Culture.Media.Films                          0.779
		Culture.Media.Media*                         0.638
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.774
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.673
		Culture.Media.Video games                    0.802
		Culture.Performing arts                      0.547
		Culture.Philosophy and religion              0.529
		Culture.Sports                               0.925
		Culture.Visual arts.Architecture             0.632
		Culture.Visual arts.Comics and Anime         0.515
		Culture.Visual arts.Fashion                  0.463
		Culture.Visual arts.Visual arts*             0.605
		Geography.Geographical                       0.776
		Geography.Regions.Africa.Africa*             0.634
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.42
		Geography.Regions.Africa.Northern Africa     0.423
		Geography.Regions.Africa.Southern Africa     0.572
		Geography.Regions.Africa.Western Africa      0.338
		Geography.Regions.Americas.Central America   0.658
		Geography.Regions.Americas.North America     0.684
		Geography.Regions.Americas.South America     0.693
		Geography.Regions.Asia.Asia*                 0.718
		Geography.Regions.Asia.Central Asia          0.449
		Geography.Regions.Asia.East Asia             0.689
		Geography.Regions.Asia.North Asia            0.173
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.778
		Geography.Regions.Asia.West Asia             0.793
		Geography.Regions.Europe.Eastern Europe      0.694
		Geography.Regions.Europe.Europe*             0.635
		Geography.Regions.Europe.Northern Europe     0.669
		Geography.Regions.Europe.Southern Europe     0.681
		Geography.Regions.Europe.Western Europe      0.656
		Geography.Regions.Oceania                    0.872
		History and Society.Business and economics   0.363
		History and Society.Education                0.479
		History and Society.History                  0.391
		History and Society.Military and warfare     0.614
		History and Society.Politics and government  0.694
		History and Society.Society                  0.446
		History and Society.Transportation           0.775
		STEM.Biology                                 0.929
		STEM.Chemistry                               0.294
		STEM.Computing                               0.228
		STEM.Earth and environment                   0.668
		STEM.Engineering                             0.577
		STEM.Libraries & Information                 0.296
		STEM.Mathematics                             0.255
		STEM.Medicine & Health                       0.621
		STEM.Physics                                 0.219
		STEM.STEM*                                   0.758
		STEM.Space                                   0.861
		STEM.Technology                              0.265
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
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
		Culture.Philosophy and religion              0.995
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
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.994
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.99
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
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.746, macro=0.634):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.585
		Culture.Food and drink                       0.697
		Culture.Internet culture                     0.605
		Culture.Linguistics                          0.794
		Culture.Literature                           0.646
		Culture.Media.Books                          0.587
		Culture.Media.Entertainment                  0.457
		Culture.Media.Films                          0.804
		Culture.Media.Media*                         0.734
		Culture.Media.Music                          0.817
		Culture.Media.Radio                          0.796
		Culture.Media.Software                       0.216
		Culture.Media.Television                     0.698
		Culture.Media.Video games                    0.855
		Culture.Performing arts                      0.618
		Culture.Philosophy and religion              0.547
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.631
		Culture.Visual arts.Fashion                  0.589
		Culture.Visual arts.Visual arts*             0.683
		Geography.Geographical                       0.729
		Geography.Regions.Africa.Africa*             0.733
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.556
		Geography.Regions.Africa.Northern Africa     0.54
		Geography.Regions.Africa.Southern Africa     0.663
		Geography.Regions.Africa.Western Africa      0.481
		Geography.Regions.Americas.Central America   0.685
		Geography.Regions.Americas.North America     0.692
		Geography.Regions.Americas.South America     0.727
		Geography.Regions.Asia.Asia*                 0.786
		Geography.Regions.Asia.Central Asia          0.572
		Geography.Regions.Asia.East Asia             0.742
		Geography.Regions.Asia.North Asia            0.277
		Geography.Regions.Asia.South Asia            0.871
		Geography.Regions.Asia.Southeast Asia        0.787
		Geography.Regions.Asia.West Asia             0.791
		Geography.Regions.Europe.Eastern Europe      0.737
		Geography.Regions.Europe.Europe*             0.7
		Geography.Regions.Europe.Northern Europe     0.677
		Geography.Regions.Europe.Southern Europe     0.694
		Geography.Regions.Europe.Western Europe      0.661
		Geography.Regions.Oceania                    0.852
		History and Society.Business and economics   0.422
		History and Society.Education                0.503
		History and Society.History                  0.43
		History and Society.Military and warfare     0.666
		History and Society.Politics and government  0.669
		History and Society.Society                  0.43
		History and Society.Transportation           0.821
		STEM.Biology                                 0.875
		STEM.Chemistry                               0.42
		STEM.Computing                               0.346
		STEM.Earth and environment                   0.695
		STEM.Engineering                             0.652
		STEM.Libraries & Information                 0.403
		STEM.Mathematics                             0.385
		STEM.Medicine & Health                       0.653
		STEM.Physics                                 0.334
		STEM.STEM*                                   0.812
		STEM.Space                                   0.878
		STEM.Technology                              0.379
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
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
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.978
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.982
		History and Society.Society                  0.986
		History and Society.Transportation           0.994
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.007
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.021
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.978, macro=0.979):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.985
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.983
		Culture.Literature                           0.979
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.978
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.992
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.985
		Culture.Philosophy and religion              0.97
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.987
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.819
		Geography.Regions.Africa.Eastern Africa      0.99
		Geography.Regions.Africa.Northern Africa     0.986
		Geography.Regions.Africa.Southern Africa     0.988
		Geography.Regions.Africa.Western Africa      0.99
		Geography.Regions.Americas.Central America   0.985
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.985
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.991
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.984
		Geography.Regions.Asia.West Asia             0.987
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.958
		History and Society.Education                0.967
		History and Society.History                  0.952
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.968
		History and Society.Society                  0.939
		History and Society.Transportation           0.987
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.988
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.984
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.982
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.98
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.978
		STEM.Space                                   0.993
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.801, macro=0.676):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.587
		Culture.Food and drink                       0.704
		Culture.Internet culture                     0.782
		Culture.Linguistics                          0.834
		Culture.Literature                           0.712
		Culture.Media.Books                          0.615
		Culture.Media.Entertainment                  0.486
		Culture.Media.Films                          0.837
		Culture.Media.Media*                         0.847
		Culture.Media.Music                          0.863
		Culture.Media.Radio                          0.872
		Culture.Media.Software                       0.256
		Culture.Media.Television                     0.71
		Culture.Media.Video games                    0.93
		Culture.Performing arts                      0.678
		Culture.Philosophy and religion              0.528
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.761
		Culture.Visual arts.Comics and Anime         0.706
		Culture.Visual arts.Fashion                  0.568
		Culture.Visual arts.Visual arts*             0.747
		Geography.Geographical                       0.792
		Geography.Regions.Africa.Africa*             0.789
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.607
		Geography.Regions.Africa.Northern Africa     0.605
		Geography.Regions.Africa.Southern Africa     0.674
		Geography.Regions.Africa.Western Africa      0.481
		Geography.Regions.Americas.Central America   0.684
		Geography.Regions.Americas.North America     0.754
		Geography.Regions.Americas.South America     0.754
		Geography.Regions.Asia.Asia*                 0.838
		Geography.Regions.Asia.Central Asia          0.724
		Geography.Regions.Asia.East Asia             0.775
		Geography.Regions.Asia.North Asia            0.247
		Geography.Regions.Asia.South Asia            0.893
		Geography.Regions.Asia.Southeast Asia        0.804
		Geography.Regions.Asia.West Asia             0.866
		Geography.Regions.Europe.Eastern Europe      0.776
		Geography.Regions.Europe.Europe*             0.781
		Geography.Regions.Europe.Northern Europe     0.737
		Geography.Regions.Europe.Southern Europe     0.731
		Geography.Regions.Europe.Western Europe      0.701
		Geography.Regions.Oceania                    0.898
		History and Society.Business and economics   0.364
		History and Society.Education                0.456
		History and Society.History                  0.395
		History and Society.Military and warfare     0.725
		History and Society.Politics and government  0.731
		History and Society.Society                  0.398
		History and Society.Transportation           0.872
		STEM.Biology                                 0.933
		STEM.Chemistry                               0.535
		STEM.Computing                               0.345
		STEM.Earth and environment                   0.755
		STEM.Engineering                             0.732
		STEM.Libraries & Information                 0.384
		STEM.Mathematics                             0.455
		STEM.Medicine & Health                       0.666
		STEM.Physics                                 0.427
		STEM.STEM*                                   0.906
		STEM.Space                                   0.927
		STEM.Technology                              0.425
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability'}

