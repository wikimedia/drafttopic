Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'label_weights': {}, 'learning_rate': 0.1, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'max_leaf_nodes': None, 'tol': 0.0001, 'presort': 'auto', 'loss': 'deviance', 'verbose': 0, 'criterion': 'friedman_mse', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_split': 2, 'multilabel': True, 'min_impurity_split': None, 'max_features': 'log2', 'scale': False, 'validation_fraction': 0.1, 'init': None, 'warm_start': False, 'population_rates': None, 'max_depth': 5, 'random_state': None, 'center': False, 'subsample': 1.0, 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150}
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
	counts (n=63014):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16614  -->  14881  1733  1130  45270
			'Culture.Biography.Women'                       4129  -->   3237   892   844  58041
			'Culture.Food and drink'                        1318  -->    989   329    70  61626
			'Culture.Internet culture'                      2936  -->   2350   586   197  59881
			'Culture.Linguistics'                           1345  -->    972   373    68  61601
			'Culture.Literature'                            5321  -->   3945  1376   544  57149
			'Culture.Media.Books'                           1864  -->   1315   549   161  60989
			'Culture.Media.Entertainment'                   1804  -->    946   858   188  61022
			'Culture.Media.Films'                           2276  -->   1892   384   171  60567
			'Culture.Media.Media*'                         14363  -->  12365  1998  1535  47116
			'Culture.Media.Music'                           2669  -->   2219   450   303  60042
			'Culture.Media.Radio'                           1177  -->    941   236    39  61798
			'Culture.Media.Software'                        1810  -->   1138   672   369  60835
			'Culture.Media.Television'                      2229  -->   1652   577   210  60575
			'Culture.Media.Video games'                     2073  -->   1886   187    39  60902
			'Culture.Performing arts'                       1328  -->    907   421   112  61574
			'Culture.Philosophy and religion'               2619  -->   1438  1181   355  60040
			'Culture.Sports'                                5868  -->   5316   552   352  56794
			'Culture.Visual arts.Architecture'              2526  -->   1858   668   270  60218
			'Culture.Visual arts.Comics and Anime'          1543  -->   1231   312   118  61353
			'Culture.Visual arts.Fashion'                   1184  -->    880   304    60  61770
			'Culture.Visual arts.Visual arts*'              5986  -->   4577  1409   571  56457
			'Geography.Geographical'                        3512  -->   2355  1157   318  59184
			'Geography.Regions.Africa.Africa*'              5645  -->   4849   796   242  57127
			'Geography.Regions.Africa.Central Africa'         66  -->     11    55    29  62919
			'Geography.Regions.Africa.Eastern Africa'       1117  -->    902   215    33  61864
			'Geography.Regions.Africa.Northern Africa'      1300  -->    963   337   102  61612
			'Geography.Regions.Africa.Southern Africa'      1241  -->    944   297    46  61727
			'Geography.Regions.Africa.Western Africa'       1134  -->    914   220    70  61810
			'Geography.Regions.Americas.Central America'    1294  -->    881   413    92  61628
			'Geography.Regions.Americas.North America'      7483  -->   5191  2292  1224  54307
			'Geography.Regions.Americas.South America'      1548  -->   1146   402   140  61326
			'Geography.Regions.Asia.Asia*'                 11087  -->   9528  1559   858  51069
			'Geography.Regions.Asia.Central Asia'           1117  -->    873   244    55  61842
			'Geography.Regions.Asia.East Asia'              2693  -->   2088   605   246  60075
			'Geography.Regions.Asia.North Asia'             1391  -->    916   475   195  61428
			'Geography.Regions.Asia.South Asia'             2402  -->   2051   351   135  60477
			'Geography.Regions.Asia.Southeast Asia'         1684  -->   1337   347   100  61230
			'Geography.Regions.Asia.West Asia'              2297  -->   1825   472   164  60553
			'Geography.Regions.Europe.Eastern Europe'       3086  -->   2333   753   275  59653
			'Geography.Regions.Europe.Europe*'             12498  -->   9586  2912  1851  48665
			'Geography.Regions.Europe.Northern Europe'      4230  -->   2893  1337   655  58129
			'Geography.Regions.Europe.Southern Europe'      2412  -->   1672   740   278  60324
			'Geography.Regions.Europe.Western Europe'       3171  -->   2062  1109   434  59409
			'Geography.Regions.Oceania'                     2560  -->   2110   450   128  60326
			'History and Society.Business and economics'    3536  -->   1737  1799   571  58907
			'History and Society.Education'                 2148  -->   1096  1052   266  60600
			'History and Society.History'                   3316  -->   1541  1775   511  59187
			'History and Society.Military and warfare'      3992  -->   2840  1152   399  58623
			'History and Society.Politics and government'   4564  -->   2892  1672   482  57968
			'History and Society.Society'                   4022  -->   1591  2431   378  58614
			'History and Society.Transportation'            3621  -->   3145   476   240  59153
			'STEM.Biology'                                  2816  -->   2307   509   149  60049
			'STEM.Chemistry'                                1336  -->    944   392   177  61501
			'STEM.Computing'                                2045  -->   1466   579   439  60530
			'STEM.Earth and environment'                    1615  -->   1142   473   117  61282
			'STEM.Engineering'                              2281  -->   1682   599   174  60559
			'STEM.Libraries & Information'                  1160  -->    694   466    72  61782
			'STEM.Mathematics'                              1143  -->    858   285    83  61788
			'STEM.Medicine & Health'                        1746  -->   1219   527   193  61075
			'STEM.Physics'                                  1222  -->    814   408   155  61637
			'STEM.STEM*'                                   16404  -->  14307  2097   932  45678
			'STEM.Space'                                    1395  -->   1233   162    49  61570
			'STEM.Technology'                               3670  -->   2433  1237   630  58714
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
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.025
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.065
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.092
		Geography.Regions.Europe.Northern Europe     0.032
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.02
		Geography.Regions.Oceania                    0.015
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.014
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.011
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.079
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.935
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.908
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.98
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.989
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.921
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.783, macro=0.725):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.784
		Culture.Food and drink                       0.75
		Culture.Internet culture                     0.8
		Culture.Linguistics                          0.723
		Culture.Literature                           0.741
		Culture.Media.Books                          0.705
		Culture.Media.Entertainment                  0.524
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.861
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.799
		Culture.Media.Software                       0.629
		Culture.Media.Television                     0.741
		Culture.Media.Video games                    0.91
		Culture.Performing arts                      0.683
		Culture.Philosophy and religion              0.549
		Culture.Sports                               0.906
		Culture.Visual arts.Architecture             0.736
		Culture.Visual arts.Comics and Anime         0.798
		Culture.Visual arts.Fashion                  0.743
		Culture.Visual arts.Visual arts*             0.765
		Geography.Geographical                       0.671
		Geography.Regions.Africa.Africa*             0.859
		Geography.Regions.Africa.Central Africa      0.167
		Geography.Regions.Africa.Eastern Africa      0.808
		Geography.Regions.Africa.Northern Africa     0.741
		Geography.Regions.Africa.Southern Africa     0.761
		Geography.Regions.Africa.Western Africa      0.806
		Geography.Regions.Americas.Central America   0.681
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.74
		Geography.Regions.Asia.Asia*                 0.859
		Geography.Regions.Asia.Central Asia          0.782
		Geography.Regions.Asia.East Asia             0.775
		Geography.Regions.Asia.North Asia            0.659
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.794
		Geography.Regions.Asia.West Asia             0.795
		Geography.Regions.Europe.Eastern Europe      0.756
		Geography.Regions.Europe.Europe*             0.767
		Geography.Regions.Europe.Northern Europe     0.684
		Geography.Regions.Europe.Southern Europe     0.693
		Geography.Regions.Europe.Western Europe      0.65
		Geography.Regions.Oceania                    0.824
		History and Society.Business and economics   0.491
		History and Society.Education                0.51
		History and Society.History                  0.465
		History and Society.Military and warfare     0.711
		History and Society.Politics and government  0.634
		History and Society.Society                  0.396
		History and Society.Transportation           0.869
		STEM.Biology                                 0.819
		STEM.Chemistry                               0.707
		STEM.Computing                               0.717
		STEM.Earth and environment                   0.707
		STEM.Engineering                             0.737
		STEM.Libraries & Information                 0.598
		STEM.Mathematics                             0.751
		STEM.Medicine & Health                       0.698
		STEM.Physics                                 0.666
		STEM.STEM*                                   0.872
		STEM.Space                                   0.884
		STEM.Technology                              0.663
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.99
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.705, macro=0.563):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.838
		Culture.Biography.Women                      0.447
		Culture.Food and drink                       0.62
		Culture.Internet culture                     0.462
		Culture.Linguistics                          0.829
		Culture.Literature                           0.553
		Culture.Media.Books                          0.52
		Culture.Media.Entertainment                  0.38
		Culture.Media.Films                          0.758
		Culture.Media.Media*                         0.629
		Culture.Media.Music                          0.802
		Culture.Media.Radio                          0.733
		Culture.Media.Software                       0.122
		Culture.Media.Television                     0.656
		Culture.Media.Video games                    0.788
		Culture.Performing arts                      0.521
		Culture.Philosophy and religion              0.502
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.638
		Culture.Visual arts.Comics and Anime         0.478
		Culture.Visual arts.Fashion                  0.383
		Culture.Visual arts.Visual arts*             0.587
		Geography.Geographical                       0.752
		Geography.Regions.Africa.Africa*             0.616
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.408
		Geography.Regions.Africa.Northern Africa     0.355
		Geography.Regions.Africa.Southern Africa     0.546
		Geography.Regions.Africa.Western Africa      0.328
		Geography.Regions.Americas.Central America   0.602
		Geography.Regions.Americas.North America     0.684
		Geography.Regions.Americas.South America     0.674
		Geography.Regions.Asia.Asia*                 0.713
		Geography.Regions.Asia.Central Asia          0.433
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.161
		Geography.Regions.Asia.South Asia            0.855
		Geography.Regions.Asia.Southeast Asia        0.746
		Geography.Regions.Asia.West Asia             0.764
		Geography.Regions.Europe.Eastern Europe      0.682
		Geography.Regions.Europe.Europe*             0.633
		Geography.Regions.Europe.Northern Europe     0.66
		Geography.Regions.Europe.Southern Europe     0.666
		Geography.Regions.Europe.Western Europe      0.637
		Geography.Regions.Oceania                    0.857
		History and Society.Business and economics   0.343
		History and Society.Education                0.464
		History and Society.History                  0.373
		History and Society.Military and warfare     0.6
		History and Society.Politics and government  0.69
		History and Society.Society                  0.441
		History and Society.Transportation           0.767
		STEM.Biology                                 0.92
		STEM.Chemistry                               0.278
		STEM.Computing                               0.212
		STEM.Earth and environment                   0.629
		STEM.Engineering                             0.575
		STEM.Libraries & Information                 0.242
		STEM.Mathematics                             0.189
		STEM.Medicine & Health                       0.588
		STEM.Physics                                 0.184
		STEM.STEM*                                   0.764
		STEM.Space                                   0.871
		STEM.Technology                              0.244
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
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
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
	f1 (micro=0.737, macro=0.616):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.569
		Culture.Food and drink                       0.679
		Culture.Internet culture                     0.586
		Culture.Linguistics                          0.772
		Culture.Literature                           0.634
		Culture.Media.Books                          0.599
		Culture.Media.Entertainment                  0.441
		Culture.Media.Films                          0.793
		Culture.Media.Media*                         0.727
		Culture.Media.Music                          0.817
		Culture.Media.Radio                          0.765
		Culture.Media.Software                       0.204
		Culture.Media.Television                     0.696
		Culture.Media.Video games                    0.845
		Culture.Performing arts                      0.591
		Culture.Philosophy and religion              0.524
		Culture.Sports                               0.912
		Culture.Visual arts.Architecture             0.683
		Culture.Visual arts.Comics and Anime         0.598
		Culture.Visual arts.Fashion                  0.505
		Culture.Visual arts.Visual arts*             0.664
		Geography.Geographical                       0.709
		Geography.Regions.Africa.Africa*             0.717
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.542
		Geography.Regions.Africa.Northern Africa     0.48
		Geography.Regions.Africa.Southern Africa     0.636
		Geography.Regions.Africa.Western Africa      0.466
		Geography.Regions.Americas.Central America   0.639
		Geography.Regions.Americas.North America     0.689
		Geography.Regions.Americas.South America     0.705
		Geography.Regions.Asia.Asia*                 0.779
		Geography.Regions.Asia.Central Asia          0.557
		Geography.Regions.Asia.East Asia             0.729
		Geography.Regions.Asia.North Asia            0.259
		Geography.Regions.Asia.South Asia            0.855
		Geography.Regions.Asia.Southeast Asia        0.769
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.694
		Geography.Regions.Europe.Northern Europe     0.672
		Geography.Regions.Europe.Southern Europe     0.679
		Geography.Regions.Europe.Western Europe      0.643
		Geography.Regions.Oceania                    0.84
		History and Society.Business and economics   0.404
		History and Society.Education                0.486
		History and Society.History                  0.414
		History and Society.Military and warfare     0.651
		History and Society.Politics and government  0.661
		History and Society.Society                  0.417
		History and Society.Transportation           0.815
		STEM.Biology                                 0.867
		STEM.Chemistry                               0.399
		STEM.Computing                               0.327
		STEM.Earth and environment                   0.665
		STEM.Engineering                             0.646
		STEM.Libraries & Information                 0.345
		STEM.Mathematics                             0.302
		STEM.Medicine & Health                       0.638
		STEM.Physics                                 0.289
		STEM.STEM*                                   0.815
		STEM.Space                                   0.877
		STEM.Technology                              0.356
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.989
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
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.978
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.982
		History and Society.Society                  0.986
		History and Society.Transportation           0.994
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.01
		History and Society.Education                0.004
		History and Society.History                  0.009
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.008
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.02
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.976):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.982
		Culture.Literature                           0.978
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.974
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.989
		Culture.Media.Software                       0.982
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.982
		Culture.Philosophy and religion              0.966
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.982
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.744
		Geography.Regions.Africa.Eastern Africa      0.988
		Geography.Regions.Africa.Northern Africa     0.983
		Geography.Regions.Africa.Southern Africa     0.985
		Geography.Regions.Africa.Western Africa      0.99
		Geography.Regions.Americas.Central America   0.983
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.985
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.988
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.956
		History and Society.Education                0.965
		History and Society.History                  0.951
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.966
		History and Society.Society                  0.936
		History and Society.Transportation           0.986
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.987
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.982
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.979
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.977
		STEM.Space                                   0.991
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.789, macro=0.646):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.923
		Culture.Biography.Women                      0.579
		Culture.Food and drink                       0.681
		Culture.Internet culture                     0.753
		Culture.Linguistics                          0.815
		Culture.Literature                           0.712
		Culture.Media.Books                          0.64
		Culture.Media.Entertainment                  0.434
		Culture.Media.Films                          0.769
		Culture.Media.Media*                         0.841
		Culture.Media.Music                          0.861
		Culture.Media.Radio                          0.818
		Culture.Media.Software                       0.165
		Culture.Media.Television                     0.735
		Culture.Media.Video games                    0.926
		Culture.Performing arts                      0.6
		Culture.Philosophy and religion              0.495
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.732
		Culture.Visual arts.Comics and Anime         0.624
		Culture.Visual arts.Fashion                  0.529
		Culture.Visual arts.Visual arts*             0.717
		Geography.Geographical                       0.774
		Geography.Regions.Africa.Africa*             0.786
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.649
		Geography.Regions.Africa.Northern Africa     0.541
		Geography.Regions.Africa.Southern Africa     0.602
		Geography.Regions.Africa.Western Africa      0.391
		Geography.Regions.Americas.Central America   0.643
		Geography.Regions.Americas.North America     0.757
		Geography.Regions.Americas.South America     0.715
		Geography.Regions.Asia.Asia*                 0.845
		Geography.Regions.Asia.Central Asia          0.646
		Geography.Regions.Asia.East Asia             0.767
		Geography.Regions.Asia.North Asia            0.21
		Geography.Regions.Asia.South Asia            0.876
		Geography.Regions.Asia.Southeast Asia        0.774
		Geography.Regions.Asia.West Asia             0.846
		Geography.Regions.Europe.Eastern Europe      0.76
		Geography.Regions.Europe.Europe*             0.767
		Geography.Regions.Europe.Northern Europe     0.727
		Geography.Regions.Europe.Southern Europe     0.702
		Geography.Regions.Europe.Western Europe      0.677
		Geography.Regions.Oceania                    0.888
		History and Society.Business and economics   0.354
		History and Society.Education                0.445
		History and Society.History                  0.366
		History and Society.Military and warfare     0.705
		History and Society.Politics and government  0.718
		History and Society.Society                  0.395
		History and Society.Transportation           0.852
		STEM.Biology                                 0.926
		STEM.Chemistry                               0.5
		STEM.Computing                               0.307
		STEM.Earth and environment                   0.723
		STEM.Engineering                             0.683
		STEM.Libraries & Information                 0.282
		STEM.Mathematics                             0.266
		STEM.Medicine & Health                       0.668
		STEM.Physics                                 0.34
		STEM.STEM*                                   0.894
		STEM.Space                                   0.935
		STEM.Technology                              0.366
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}}

