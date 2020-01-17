Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'min_samples_split': 2, 'tol': 0.0001, 'init': None, 'population_rates': None, 'max_leaf_nodes': None, 'n_iter_no_change': None, 'subsample': 1.0, 'criterion': 'friedman_mse', 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'presort': 'auto', 'random_state': None, 'loss': 'deviance', 'min_impurity_split': None, 'max_depth': 5, 'scale': False, 'verbose': 0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'validation_fraction': 0.1, 'center': False, 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'label_weights': {}, 'warm_start': False, 'multilabel': True, 'learning_rate': 0.1}
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
	counts (n=60052):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16350  -->  13907  2443  1346  42356
			'Culture.Biography.Women'                       4056  -->   2834  1222   778  55218
			'Culture.Food and drink'                        1245  -->    831   414    88  58719
			'Culture.Internet culture'                      2681  -->   1996   685   208  57163
			'Culture.Linguistics'                           1210  -->    792   418    68  58774
			'Culture.Literature'                            4977  -->   3432  1545   545  54530
			'Culture.Media.Books'                           1810  -->   1158   652   196  58046
			'Culture.Media.Entertainment'                   1737  -->    785   952   171  58144
			'Culture.Media.Films'                           2225  -->   1693   532   173  57654
			'Culture.Media.Media*'                         13453  -->  11084  2369  1576  45023
			'Culture.Media.Music'                           2532  -->   1945   587   265  57255
			'Culture.Media.Radio'                           1116  -->    856   260    44  58892
			'Culture.Media.Software'                        1667  -->    941   726   341  58044
			'Culture.Media.Television'                      2008  -->   1278   730   196  57848
			'Culture.Media.Video games'                     1881  -->   1615   266    61  58110
			'Culture.Performing arts'                       1273  -->    794   479   117  58662
			'Culture.Philosophy and religion'               2505  -->   1296  1209   299  57248
			'Culture.Sports'                                5720  -->   5148   572   312  54020
			'Culture.Visual arts.Architecture'              2468  -->   1729   739   269  57315
			'Culture.Visual arts.Comics and Anime'          1384  -->   1064   320   112  58556
			'Culture.Visual arts.Fashion'                   1118  -->    789   329    84  58850
			'Culture.Visual arts.Visual arts*'              5691  -->   4120  1571   588  53773
			'Geography.Geographical'                        3224  -->   2068  1156   303  56525
			'Geography.Regions.Africa.Africa*'              5529  -->   4610   919   216  54307
			'Geography.Regions.Africa.Central Africa'         27  -->      0    27    33  59992
			'Geography.Regions.Africa.Eastern Africa'       1079  -->    857   222    26  58947
			'Geography.Regions.Africa.Northern Africa'      1228  -->    865   363    75  58749
			'Geography.Regions.Africa.Southern Africa'      1244  -->    932   312    49  58759
			'Geography.Regions.Africa.Western Africa'       1131  -->    902   229    61  58860
			'Geography.Regions.Americas.Central America'    1282  -->    856   426    70  58700
			'Geography.Regions.Americas.North America'      7247  -->   4573  2674  1168  51637
			'Geography.Regions.Americas.South America'      1480  -->   1040   440   135  58437
			'Geography.Regions.Asia.Asia*'                 10642  -->   8808  1834   841  48569
			'Geography.Regions.Asia.Central Asia'           1125  -->    822   303    41  58886
			'Geography.Regions.Asia.East Asia'              2594  -->   1870   724   269  57189
			'Geography.Regions.Asia.North Asia'             1317  -->    829   488   177  58558
			'Geography.Regions.Asia.South Asia'             2361  -->   1923   438   127  57564
			'Geography.Regions.Asia.Southeast Asia'         1623  -->   1189   434   103  58326
			'Geography.Regions.Asia.West Asia'              2154  -->   1647   507   132  57766
			'Geography.Regions.Europe.Eastern Europe'       2996  -->   2220   776   325  56731
			'Geography.Regions.Europe.Europe*'             11970  -->   8926  3044  1740  46342
			'Geography.Regions.Europe.Northern Europe'      4083  -->   2576  1507   585  55384
			'Geography.Regions.Europe.Southern Europe'      2233  -->   1474   759   250  57569
			'Geography.Regions.Europe.Western Europe'       3035  -->   1877  1158   386  56631
			'Geography.Regions.Oceania'                     2466  -->   1861   605   151  57435
			'History and Society.Business and economics'    3248  -->   1402  1846   458  56346
			'History and Society.Education'                 2097  -->    990  1107   240  57715
			'History and Society.History'                   3062  -->   1194  1868   438  56552
			'History and Society.Military and warfare'      3819  -->   2577  1242   403  55830
			'History and Society.Politics and government'   4473  -->   2490  1983   516  55063
			'History and Society.Society'                   3850  -->   1371  2479   356  55846
			'History and Society.Transportation'            3424  -->   2849   575   239  56389
			'STEM.Biology'                                  2735  -->   2168   567   144  57173
			'STEM.Chemistry'                                1251  -->    833   418   142  58659
			'STEM.Computing'                                1902  -->   1171   731   403  57747
			'STEM.Earth and environment'                    1590  -->   1046   544   109  58353
			'STEM.Engineering'                              2145  -->   1468   677   197  57710
			'STEM.Libraries & Information'                  1110  -->    592   518    66  58876
			'STEM.Mathematics'                              1026  -->    709   317    72  58954
			'STEM.Medicine & Health'                        1613  -->   1004   609   181  58258
			'STEM.Physics'                                  1135  -->    710   425   121  58796
			'STEM.STEM*'                                   15592  -->  13110  2482  1154  43306
			'STEM.Space'                                    1330  -->   1129   201    57  58665
			'STEM.Technology'                               3436  -->   2016  1420   585  56031
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.272         0.123
		Culture.Biography.Women                         0.068         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.02          0.007
		Culture.Literature                              0.083         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.224         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.054         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.021         0.001
		Geography.Regions.Africa.Western Africa         0.019         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.121         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.177         0.046
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.199         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.057         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.02
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.09
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.008
		History and Society.History                  0.012
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.025
		History and Society.Society                  0.011
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.91
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.975
		History and Society.Society                  0.989
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.741, macro=0.676):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.851
		Culture.Biography.Women                      0.699
		Culture.Food and drink                       0.667
		Culture.Internet culture                     0.744
		Culture.Linguistics                          0.655
		Culture.Literature                           0.69
		Culture.Media.Books                          0.64
		Culture.Media.Entertainment                  0.452
		Culture.Media.Films                          0.761
		Culture.Media.Media*                         0.824
		Culture.Media.Music                          0.768
		Culture.Media.Radio                          0.767
		Culture.Media.Software                       0.564
		Culture.Media.Television                     0.636
		Culture.Media.Video games                    0.859
		Culture.Performing arts                      0.624
		Culture.Philosophy and religion              0.517
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.701
		Culture.Visual arts.Comics and Anime         0.769
		Culture.Visual arts.Fashion                  0.706
		Culture.Visual arts.Visual arts*             0.724
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.834
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.794
		Geography.Regions.Africa.Northern Africa     0.704
		Geography.Regions.Africa.Southern Africa     0.749
		Geography.Regions.Africa.Western Africa      0.798
		Geography.Regions.Americas.Central America   0.668
		Geography.Regions.Americas.North America     0.631
		Geography.Regions.Americas.South America     0.703
		Geography.Regions.Asia.Asia*                 0.828
		Geography.Regions.Asia.Central Asia          0.731
		Geography.Regions.Asia.East Asia             0.721
		Geography.Regions.Asia.North Asia            0.629
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.733
		Geography.Regions.Asia.West Asia             0.765
		Geography.Regions.Europe.Eastern Europe      0.741
		Geography.Regions.Europe.Europe*             0.746
		Geography.Regions.Europe.Northern Europe     0.631
		Geography.Regions.Europe.Southern Europe     0.66
		Geography.Regions.Europe.Western Europe      0.618
		Geography.Regions.Oceania                    0.755
		History and Society.Business and economics   0.432
		History and Society.Education                0.472
		History and Society.History                  0.39
		History and Society.Military and warfare     0.675
		History and Society.Politics and government  0.557
		History and Society.Society                  0.356
		History and Society.Transportation           0.832
		STEM.Biology                                 0.793
		STEM.Chemistry                               0.666
		STEM.Computing                               0.616
		STEM.Earth and environment                   0.658
		STEM.Engineering                             0.684
		STEM.Libraries & Information                 0.533
		STEM.Mathematics                             0.691
		STEM.Medicine & Health                       0.622
		STEM.Physics                                 0.626
		STEM.STEM*                                   0.841
		STEM.Space                                   0.849
		STEM.Technology                              0.587
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.966
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
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
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
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.683, macro=0.545):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.795
		Culture.Biography.Women                      0.426
		Culture.Food and drink                       0.524
		Culture.Internet culture                     0.419
		Culture.Linguistics                          0.807
		Culture.Literature                           0.523
		Culture.Media.Books                          0.435
		Culture.Media.Entertainment                  0.357
		Culture.Media.Films                          0.73
		Culture.Media.Media*                         0.602
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.689
		Culture.Media.Software                       0.114
		Culture.Media.Television                     0.626
		Culture.Media.Video games                    0.682
		Culture.Performing arts                      0.476
		Culture.Philosophy and religion              0.517
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.47
		Culture.Visual arts.Fashion                  0.286
		Culture.Visual arts.Visual arts*             0.555
		Geography.Geographical                       0.744
		Geography.Regions.Africa.Africa*             0.623
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.451
		Geography.Regions.Africa.Northern Africa     0.404
		Geography.Regions.Africa.Southern Africa     0.514
		Geography.Regions.Africa.Western Africa      0.345
		Geography.Regions.Americas.Central America   0.65
		Geography.Regions.Americas.North America     0.662
		Geography.Regions.Americas.South America     0.659
		Geography.Regions.Asia.Asia*                 0.699
		Geography.Regions.Asia.Central Asia          0.477
		Geography.Regions.Asia.East Asia             0.64
		Geography.Regions.Asia.North Asia            0.162
		Geography.Regions.Asia.South Asia            0.851
		Geography.Regions.Asia.Southeast Asia        0.715
		Geography.Regions.Asia.West Asia             0.787
		Geography.Regions.Europe.Eastern Europe      0.628
		Geography.Regions.Europe.Europe*             0.63
		Geography.Regions.Europe.Northern Europe     0.656
		Geography.Regions.Europe.Southern Europe     0.669
		Geography.Regions.Europe.Western Europe      0.641
		Geography.Regions.Oceania                    0.816
		History and Society.Business and economics   0.353
		History and Society.Education                0.458
		History and Society.History                  0.357
		History and Society.Military and warfare     0.573
		History and Society.Politics and government  0.635
		History and Society.Society                  0.418
		History and Society.Transportation           0.751
		STEM.Biology                                 0.917
		STEM.Chemistry                               0.301
		STEM.Computing                               0.193
		STEM.Earth and environment                   0.617
		STEM.Engineering                             0.514
		STEM.Libraries & Information                 0.229
		STEM.Mathematics                             0.191
		STEM.Medicine & Health                       0.564
		STEM.Physics                                 0.206
		STEM.STEM*                                   0.707
		STEM.Space                                   0.841
		STEM.Technology                              0.227
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.979
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.822
		Culture.Biography.Women                      0.53
		Culture.Food and drink                       0.587
		Culture.Internet culture                     0.536
		Culture.Linguistics                          0.723
		Culture.Literature                           0.595
		Culture.Media.Books                          0.518
		Culture.Media.Entertainment                  0.399
		Culture.Media.Films                          0.745
		Culture.Media.Media*                         0.696
		Culture.Media.Music                          0.785
		Culture.Media.Radio                          0.726
		Culture.Media.Software                       0.19
		Culture.Media.Television                     0.631
		Culture.Media.Video games                    0.76
		Culture.Performing arts                      0.54
		Culture.Philosophy and religion              0.517
		Culture.Sports                               0.911
		Culture.Visual arts.Architecture             0.655
		Culture.Visual arts.Comics and Anime         0.583
		Culture.Visual arts.Fashion                  0.407
		Culture.Visual arts.Visual arts*             0.628
		Geography.Geographical                       0.689
		Geography.Regions.Africa.Africa*             0.713
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.575
		Geography.Regions.Africa.Northern Africa     0.514
		Geography.Regions.Africa.Southern Africa     0.61
		Geography.Regions.Africa.Western Africa      0.482
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.646
		Geography.Regions.Americas.South America     0.68
		Geography.Regions.Asia.Asia*                 0.758
		Geography.Regions.Asia.Central Asia          0.577
		Geography.Regions.Asia.East Asia             0.678
		Geography.Regions.Asia.North Asia            0.258
		Geography.Regions.Asia.South Asia            0.832
		Geography.Regions.Asia.Southeast Asia        0.724
		Geography.Regions.Asia.West Asia             0.776
		Geography.Regions.Europe.Eastern Europe      0.68
		Geography.Regions.Europe.Europe*             0.683
		Geography.Regions.Europe.Northern Europe     0.643
		Geography.Regions.Europe.Southern Europe     0.664
		Geography.Regions.Europe.Western Europe      0.63
		Geography.Regions.Oceania                    0.784
		History and Society.Business and economics   0.388
		History and Society.Education                0.465
		History and Society.History                  0.373
		History and Society.Military and warfare     0.62
		History and Society.Politics and government  0.593
		History and Society.Society                  0.385
		History and Society.Transportation           0.79
		STEM.Biology                                 0.85
		STEM.Chemistry                               0.415
		STEM.Computing                               0.294
		STEM.Earth and environment                   0.637
		STEM.Engineering                             0.587
		STEM.Libraries & Information                 0.32
		STEM.Mathematics                             0.3
		STEM.Medicine & Health                       0.592
		STEM.Physics                                 0.31
		STEM.STEM*                                   0.768
		STEM.Space                                   0.845
		STEM.Technology                              0.327
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.978
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.965
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.031
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.034
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
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.036
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.008
		History and Society.Education                0.004
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.006
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
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.97, macro=0.969):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.975
		Culture.Literature                           0.972
		Culture.Media.Books                          0.975
		Culture.Media.Entertainment                  0.964
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.983
		Culture.Media.Software                       0.979
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.956
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.982
		Culture.Visual arts.Visual arts*             0.969
		Geography.Geographical                       0.966
		Geography.Regions.Africa.Africa*             0.982
		Geography.Regions.Africa.Central Africa      0.626
		Geography.Regions.Africa.Eastern Africa      0.987
		Geography.Regions.Africa.Northern Africa     0.984
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.979
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.98
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.979
		Geography.Regions.Asia.West Asia             0.982
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.967
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.971
		Geography.Regions.Oceania                    0.977
		History and Society.Business and economics   0.946
		History and Society.Education                0.959
		History and Society.History                  0.936
		History and Society.Military and warfare     0.97
		History and Society.Politics and government  0.953
		History and Society.Society                  0.917
		History and Society.Transportation           0.983
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.985
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.969
		STEM.Mathematics                             0.981
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.971
		STEM.Space                                   0.986
		STEM.Technology                              0.967
		-------------------------------------------  -----
	pr_auc (micro=0.752, macro=0.605):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.506
		Culture.Food and drink                       0.603
		Culture.Internet culture                     0.664
		Culture.Linguistics                          0.749
		Culture.Literature                           0.643
		Culture.Media.Books                          0.542
		Culture.Media.Entertainment                  0.376
		Culture.Media.Films                          0.779
		Culture.Media.Media*                         0.789
		Culture.Media.Music                          0.84
		Culture.Media.Radio                          0.795
		Culture.Media.Software                       0.148
		Culture.Media.Television                     0.652
		Culture.Media.Video games                    0.814
		Culture.Performing arts                      0.507
		Culture.Philosophy and religion              0.451
		Culture.Sports                               0.926
		Culture.Visual arts.Architecture             0.727
		Culture.Visual arts.Comics and Anime         0.585
		Culture.Visual arts.Fashion                  0.365
		Culture.Visual arts.Visual arts*             0.693
		Geography.Geographical                       0.735
		Geography.Regions.Africa.Africa*             0.76
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.501
		Geography.Regions.Africa.Northern Africa     0.537
		Geography.Regions.Africa.Southern Africa     0.577
		Geography.Regions.Africa.Western Africa      0.41
		Geography.Regions.Americas.Central America   0.631
		Geography.Regions.Americas.North America     0.71
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.824
		Geography.Regions.Asia.Central Asia          0.569
		Geography.Regions.Asia.East Asia             0.696
		Geography.Regions.Asia.North Asia            0.217
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.733
		Geography.Regions.Asia.West Asia             0.826
		Geography.Regions.Europe.Eastern Europe      0.69
		Geography.Regions.Europe.Europe*             0.744
		Geography.Regions.Europe.Northern Europe     0.693
		Geography.Regions.Europe.Southern Europe     0.678
		Geography.Regions.Europe.Western Europe      0.647
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.328
		History and Society.Education                0.417
		History and Society.History                  0.294
		History and Society.Military and warfare     0.636
		History and Society.Politics and government  0.644
		History and Society.Society                  0.348
		History and Society.Transportation           0.857
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.428
		STEM.Computing                               0.258
		STEM.Earth and environment                   0.677
		STEM.Engineering                             0.59
		STEM.Libraries & Information                 0.314
		STEM.Mathematics                             0.421
		STEM.Medicine & Health                       0.586
		STEM.Physics                                 0.312
		STEM.STEM*                                   0.868
		STEM.Space                                   0.906
		STEM.Technology                              0.324
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'properties': {'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

