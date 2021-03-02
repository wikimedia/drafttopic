Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'tol': 0.0001, 'multilabel': True, 'verbose': 0, 'max_features': 'log2', 'warm_start': False, 'n_estimators': 150, 'validation_fraction': 0.1, 'center': False, 'loss': 'deviance', 'scale': False, 'ccp_alpha': 0.0, 'n_iter_no_change': None, 'min_samples_leaf': 1, 'label_weights': {}, 'presort': 'deprecated', 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'max_depth': 5, 'max_leaf_nodes': None, 'population_rates': None, 'min_samples_split': 2, 'learning_rate': 0.1, 'subsample': 1.0, 'init': None}
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
	counts (n=58530):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15435  -->  13660  1775   904  42191
			'Culture.Biography.Women'                       4173  -->   2651  1522   613  53744
			'Culture.Food and drink'                        1639  -->   1192   447    79  56812
			'Culture.Internet culture'                      3296  -->   2413   883   249  54985
			'Culture.Linguistics'                           1556  -->    930   626   106  56868
			'Culture.Literature'                            5590  -->   3827  1763   566  52374
			'Culture.Media.Books'                           1515  -->   1044   471   147  56868
			'Culture.Media.Entertainment'                   2210  -->    953  1257   216  56104
			'Culture.Media.Films'                           2963  -->   2381   582   136  55431
			'Culture.Media.Media*'                         14625  -->  12056  2569  1636  42269
			'Culture.Media.Music'                           3033  -->   2245   788   299  55198
			'Culture.Media.Radio'                            623  -->    332   291    60  57847
			'Culture.Media.Software'                        2176  -->   1526   650   344  56010
			'Culture.Media.Television'                      2480  -->   1592   888   181  55869
			'Culture.Media.Video games'                     2285  -->   1874   411   124  56121
			'Culture.Performing arts'                       1491  -->    811   680   165  56874
			'Culture.Philosophy and religion'               3635  -->   1790  1845   358  54537
			'Culture.Sports'                                5090  -->   4326   764   228  53212
			'Culture.Visual arts.Architecture'              1999  -->   1260   739   208  56323
			'Culture.Visual arts.Comics and Anime'          2390  -->   1865   525   191  55949
			'Culture.Visual arts.Fashion'                   1291  -->    851   440    98  57141
			'Culture.Visual arts.Visual arts*'              6149  -->   4118  2031   566  51815
			'Geography.Geographical'                        3729  -->   2375  1354   545  54256
			'Geography.Regions.Africa.Africa*'              4106  -->   2935  1171   264  54160
			'Geography.Regions.Africa.Central Africa'        784  -->    495   289    58  57688
			'Geography.Regions.Africa.Eastern Africa'        446  -->    292   154    31  58053
			'Geography.Regions.Africa.Northern Africa'      1410  -->    987   423    92  57028
			'Geography.Regions.Africa.Southern Africa'       673  -->    446   227    56  57801
			'Geography.Regions.Africa.Western Africa'        254  -->    149   105    38  58238
			'Geography.Regions.Americas.Central America'    1325  -->    822   503    59  57146
			'Geography.Regions.Americas.North America'      6296  -->   4026  2270  1154  51080
			'Geography.Regions.Americas.South America'      1458  -->   1005   453    89  56983
			'Geography.Regions.Asia.Asia*'                 15664  -->  12510  3154  1635  41231
			'Geography.Regions.Asia.Central Asia'           1231  -->    853   378   107  57192
			'Geography.Regions.Asia.East Asia'              7462  -->   5760  1702   960  50108
			'Geography.Regions.Asia.North Asia'             2946  -->   1935  1011   266  55318
			'Geography.Regions.Asia.South Asia'             1715  -->   1207   508    76  56739
			'Geography.Regions.Asia.Southeast Asia'         1882  -->   1288   594    98  56550
			'Geography.Regions.Asia.West Asia'              2163  -->   1461   702   180  56187
			'Geography.Regions.Europe.Eastern Europe'       3968  -->   2757  1211   282  54280
			'Geography.Regions.Europe.Europe*'             13625  -->  10593  3032  1679  43226
			'Geography.Regions.Europe.Northern Europe'      3639  -->   2508  1131   412  54479
			'Geography.Regions.Europe.Southern Europe'      3106  -->   2165   941   294  55130
			'Geography.Regions.Europe.Western Europe'       3832  -->   2731  1101   438  54260
			'Geography.Regions.Oceania'                     1664  -->   1078   586    88  56778
			'History and Society.Business and economics'    3691  -->   2013  1678   462  54377
			'History and Society.Education'                 1852  -->   1037   815   173  56505
			'History and Society.History'                   4831  -->   2452  2379   611  53088
			'History and Society.Military and warfare'      4223  -->   2536  1687   461  53846
			'History and Society.Politics and government'   3869  -->   1849  2020   470  54191
			'History and Society.Society'                   4291  -->   1154  3137   298  53941
			'History and Society.Transportation'            3736  -->   3150   586   194  54600
			'STEM.Biology'                                  3346  -->   2538   808   196  54988
			'STEM.Chemistry'                                1417  -->   1030   387   141  56972
			'STEM.Computing'                                2614  -->   1967   647   434  55482
			'STEM.Earth and environment'                    1798  -->   1130   668   171  56561
			'STEM.Engineering'                              2584  -->   1760   824   189  55757
			'STEM.Libraries & Information'                   723  -->    489   234    57  57750
			'STEM.Mathematics'                              1116  -->    823   293    70  57344
			'STEM.Medicine & Health'                        1866  -->   1132   734   170  56494
			'STEM.Physics'                                  1428  -->    899   529   177  56925
			'STEM.STEM*'                                   17051  -->  14672  2379  1103  40376
			'STEM.Space'                                    1626  -->   1374   252    69  56835
			'STEM.Technology'                               4359  -->   2851  1508   682  53489
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.264         0.121
		Culture.Biography.Women                         0.071         0.015
		Culture.Food and drink                          0.028         0.003
		Culture.Internet culture                        0.056         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.051         0.012
		Culture.Media.Media*                            0.25          0.055
		Culture.Media.Music                             0.052         0.021
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.039         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.062         0.01
		Culture.Sports                                  0.087         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.041         0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.105         0.018
		Geography.Geographical                          0.064         0.021
		Geography.Regions.Africa.Africa*                0.07          0.009
		Geography.Regions.Africa.Central Africa         0.013         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.004         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.108         0.064
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.268         0.053
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.127         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.029         0.017
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.037         0.012
		Geography.Regions.Europe.Eastern Europe         0.068         0.018
		Geography.Regions.Europe.Europe*                0.233         0.082
		Geography.Regions.Europe.Northern Europe        0.062         0.029
		Geography.Regions.Europe.Southern Europe        0.053         0.014
		Geography.Regions.Europe.Western Europe         0.065         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.083         0.011
		History and Society.Military and warfare        0.072         0.015
		History and Society.Politics and government     0.066         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.064         0.016
		STEM.Biology                                    0.057         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.044         0.006
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.291         0.066
		STEM.Space                                      0.028         0.004
		STEM.Technology                                 0.074         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.021
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.005
		Culture.Performing arts                      0.005
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.078
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.028
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.098
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.017
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.016
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.081
		STEM.Space                                   0.005
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.995
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.922
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.902
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.983
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.984
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.919
		STEM.Space                                   0.995
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.739, macro=0.675):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.885
		Culture.Biography.Women                      0.635
		Culture.Food and drink                       0.727
		Culture.Internet culture                     0.732
		Culture.Linguistics                          0.598
		Culture.Literature                           0.685
		Culture.Media.Books                          0.689
		Culture.Media.Entertainment                  0.431
		Culture.Media.Films                          0.804
		Culture.Media.Media*                         0.824
		Culture.Media.Music                          0.74
		Culture.Media.Radio                          0.533
		Culture.Media.Software                       0.701
		Culture.Media.Television                     0.642
		Culture.Media.Video games                    0.82
		Culture.Performing arts                      0.544
		Culture.Philosophy and religion              0.492
		Culture.Sports                               0.85
		Culture.Visual arts.Architecture             0.63
		Culture.Visual arts.Comics and Anime         0.78
		Culture.Visual arts.Fashion                  0.659
		Culture.Visual arts.Visual arts*             0.67
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.715
		Geography.Regions.Africa.Central Africa      0.631
		Geography.Regions.Africa.Eastern Africa      0.655
		Geography.Regions.Africa.Northern Africa     0.7
		Geography.Regions.Africa.Southern Africa     0.663
		Geography.Regions.Africa.Western Africa      0.587
		Geography.Regions.Americas.Central America   0.62
		Geography.Regions.Americas.North America     0.639
		Geography.Regions.Americas.South America     0.689
		Geography.Regions.Asia.Asia*                 0.799
		Geography.Regions.Asia.Central Asia          0.693
		Geography.Regions.Asia.East Asia             0.772
		Geography.Regions.Asia.North Asia            0.657
		Geography.Regions.Asia.South Asia            0.704
		Geography.Regions.Asia.Southeast Asia        0.684
		Geography.Regions.Asia.West Asia             0.675
		Geography.Regions.Europe.Eastern Europe      0.695
		Geography.Regions.Europe.Europe*             0.777
		Geography.Regions.Europe.Northern Europe     0.689
		Geography.Regions.Europe.Southern Europe     0.697
		Geography.Regions.Europe.Western Europe      0.713
		Geography.Regions.Oceania                    0.648
		History and Society.Business and economics   0.545
		History and Society.Education                0.56
		History and Society.History                  0.508
		History and Society.Military and warfare     0.601
		History and Society.Politics and government  0.478
		History and Society.Society                  0.269
		History and Society.Transportation           0.843
		STEM.Biology                                 0.759
		STEM.Chemistry                               0.727
		STEM.Computing                               0.752
		STEM.Earth and environment                   0.628
		STEM.Engineering                             0.681
		STEM.Libraries & Information                 0.676
		STEM.Mathematics                             0.737
		STEM.Medicine & Health                       0.607
		STEM.Physics                                 0.63
		STEM.STEM*                                   0.86
		STEM.Space                                   0.845
		STEM.Technology                              0.654
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.962
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.996
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.668, macro=0.531):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.464
		Culture.Food and drink                       0.575
		Culture.Internet culture                     0.38
		Culture.Linguistics                          0.724
		Culture.Literature                           0.494
		Culture.Media.Books                          0.539
		Culture.Media.Entertainment                  0.31
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.565
		Culture.Media.Music                          0.748
		Culture.Media.Radio                          0.547
		Culture.Media.Software                       0.132
		Culture.Media.Television                     0.643
		Culture.Media.Video games                    0.523
		Culture.Performing arts                      0.368
		Culture.Philosophy and religion              0.444
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.654
		Culture.Visual arts.Comics and Anime         0.357
		Culture.Visual arts.Fashion                  0.259
		Culture.Visual arts.Visual arts*             0.535
		Geography.Geographical                       0.583
		Geography.Regions.Africa.Africa*             0.56
		Geography.Regions.Africa.Central Africa      0.309
		Geography.Regions.Africa.Eastern Africa      0.384
		Geography.Regions.Africa.Northern Africa     0.372
		Geography.Regions.Africa.Southern Africa     0.475
		Geography.Regions.Africa.Western Africa      0.404
		Geography.Regions.Americas.Central America   0.678
		Geography.Regions.Americas.North America     0.663
		Geography.Regions.Americas.South America     0.755
		Geography.Regions.Asia.Asia*                 0.54
		Geography.Regions.Asia.Central Asia          0.23
		Geography.Regions.Asia.East Asia             0.338
		Geography.Regions.Asia.North Asia            0.439
		Geography.Regions.Asia.South Asia            0.899
		Geography.Regions.Asia.Southeast Asia        0.715
		Geography.Regions.Asia.West Asia             0.717
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.649
		Geography.Regions.Europe.Northern Europe     0.735
		Geography.Regions.Europe.Southern Europe     0.651
		Geography.Regions.Europe.Western Europe      0.653
		Geography.Regions.Oceania                    0.876
		History and Society.Business and economics   0.391
		History and Society.Education                0.597
		History and Society.History                  0.331
		History and Society.Military and warfare     0.526
		History and Society.Politics and government  0.482
		History and Society.Society                  0.292
		History and Society.Transportation           0.799
		STEM.Biology                                 0.885
		STEM.Chemistry                               0.335
		STEM.Computing                               0.217
		STEM.Earth and environment                   0.5
		STEM.Engineering                             0.54
		STEM.Libraries & Information                 0.322
		STEM.Mathematics                             0.22
		STEM.Medicine & Health                       0.569
		STEM.Physics                                 0.161
		STEM.STEM*                                   0.694
		STEM.Space                                   0.751
		STEM.Technology                              0.213
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
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
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.694, macro=0.575):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.536
		Culture.Food and drink                       0.642
		Culture.Internet culture                     0.501
		Culture.Linguistics                          0.655
		Culture.Literature                           0.574
		Culture.Media.Books                          0.605
		Culture.Media.Entertainment                  0.361
		Culture.Media.Films                          0.799
		Culture.Media.Media*                         0.67
		Culture.Media.Music                          0.744
		Culture.Media.Radio                          0.54
		Culture.Media.Software                       0.222
		Culture.Media.Television                     0.642
		Culture.Media.Video games                    0.638
		Culture.Performing arts                      0.439
		Culture.Philosophy and religion              0.467
		Culture.Sports                               0.887
		Culture.Visual arts.Architecture             0.642
		Culture.Visual arts.Comics and Anime         0.49
		Culture.Visual arts.Fashion                  0.371
		Culture.Visual arts.Visual arts*             0.595
		Geography.Geographical                       0.609
		Geography.Regions.Africa.Africa*             0.628
		Geography.Regions.Africa.Central Africa      0.415
		Geography.Regions.Africa.Eastern Africa      0.484
		Geography.Regions.Africa.Northern Africa     0.486
		Geography.Regions.Africa.Southern Africa     0.553
		Geography.Regions.Africa.Western Africa      0.478
		Geography.Regions.Americas.Central America   0.648
		Geography.Regions.Americas.North America     0.651
		Geography.Regions.Americas.South America     0.721
		Geography.Regions.Asia.Asia*                 0.644
		Geography.Regions.Asia.Central Asia          0.345
		Geography.Regions.Asia.East Asia             0.47
		Geography.Regions.Asia.North Asia            0.526
		Geography.Regions.Asia.South Asia            0.79
		Geography.Regions.Asia.Southeast Asia        0.699
		Geography.Regions.Asia.West Asia             0.695
		Geography.Regions.Europe.Eastern Europe      0.706
		Geography.Regions.Europe.Europe*             0.707
		Geography.Regions.Europe.Northern Europe     0.711
		Geography.Regions.Europe.Southern Europe     0.673
		Geography.Regions.Europe.Western Europe      0.681
		Geography.Regions.Oceania                    0.745
		History and Society.Business and economics   0.455
		History and Society.Education                0.578
		History and Society.History                  0.4
		History and Society.Military and warfare     0.561
		History and Society.Politics and government  0.48
		History and Society.Society                  0.28
		History and Society.Transportation           0.821
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.459
		STEM.Computing                               0.337
		STEM.Earth and environment                   0.557
		STEM.Engineering                             0.603
		STEM.Libraries & Information                 0.436
		STEM.Mathematics                             0.339
		STEM.Medicine & Health                       0.587
		STEM.Physics                                 0.257
		STEM.STEM*                                   0.769
		STEM.Space                                   0.795
		STEM.Technology                              0.322
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.971
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.968
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.955
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.953
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.947
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.983
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.994
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.011
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.037
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.038
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.019
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.004
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.966, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.967
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.976
		Culture.Linguistics                          0.967
		Culture.Literature                           0.964
		Culture.Media.Books                          0.978
		Culture.Media.Entertainment                  0.953
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.955
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.972
		Culture.Media.Video games                    0.983
		Culture.Performing arts                      0.963
		Culture.Philosophy and religion              0.939
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.97
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.973
		Culture.Visual arts.Visual arts*             0.956
		Geography.Geographical                       0.966
		Geography.Regions.Africa.Africa*             0.97
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.961
		Geography.Regions.Africa.Northern Africa     0.974
		Geography.Regions.Africa.Southern Africa     0.96
		Geography.Regions.Africa.Western Africa      0.948
		Geography.Regions.Americas.Central America   0.967
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.956
		Geography.Regions.Asia.Central Asia          0.977
		Geography.Regions.Asia.East Asia             0.97
		Geography.Regions.Asia.North Asia            0.965
		Geography.Regions.Asia.South Asia            0.975
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.969
		Geography.Regions.Europe.Eastern Europe      0.962
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.968
		Geography.Regions.Europe.Western Europe      0.969
		Geography.Regions.Oceania                    0.962
		History and Society.Business and economics   0.951
		History and Society.Education                0.961
		History and Society.History                  0.941
		History and Society.Military and warfare     0.963
		History and Society.Politics and government  0.94
		History and Society.Society                  0.884
		History and Society.Transportation           0.982
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.981
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.969
		STEM.Engineering                             0.971
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.984
		STEM.Medicine & Health                       0.967
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.97
		STEM.Space                                   0.983
		STEM.Technology                              0.968
		-------------------------------------------  -----
	pr_auc (micro=0.73, macro=0.572):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.933
		Culture.Biography.Women                      0.522
		Culture.Food and drink                       0.646
		Culture.Internet culture                     0.59
		Culture.Linguistics                          0.619
		Culture.Literature                           0.636
		Culture.Media.Books                          0.569
		Culture.Media.Entertainment                  0.283
		Culture.Media.Films                          0.84
		Culture.Media.Media*                         0.782
		Culture.Media.Music                          0.739
		Culture.Media.Radio                          0.404
		Culture.Media.Software                       0.228
		Culture.Media.Television                     0.645
		Culture.Media.Video games                    0.724
		Culture.Performing arts                      0.358
		Culture.Philosophy and religion              0.412
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.574
		Culture.Visual arts.Fashion                  0.341
		Culture.Visual arts.Visual arts*             0.63
		Geography.Geographical                       0.596
		Geography.Regions.Africa.Africa*             0.645
		Geography.Regions.Africa.Central Africa      0.396
		Geography.Regions.Africa.Eastern Africa      0.31
		Geography.Regions.Africa.Northern Africa     0.352
		Geography.Regions.Africa.Southern Africa     0.442
		Geography.Regions.Africa.Western Africa      0.247
		Geography.Regions.Americas.Central America   0.604
		Geography.Regions.Americas.North America     0.688
		Geography.Regions.Americas.South America     0.72
		Geography.Regions.Asia.Asia*                 0.71
		Geography.Regions.Asia.Central Asia          0.276
		Geography.Regions.Asia.East Asia             0.51
		Geography.Regions.Asia.North Asia            0.491
		Geography.Regions.Asia.South Asia            0.844
		Geography.Regions.Asia.Southeast Asia        0.68
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.698
		Geography.Regions.Europe.Europe*             0.76
		Geography.Regions.Europe.Northern Europe     0.744
		Geography.Regions.Europe.Southern Europe     0.682
		Geography.Regions.Europe.Western Europe      0.685
		Geography.Regions.Oceania                    0.779
		History and Society.Business and economics   0.424
		History and Society.Education                0.57
		History and Society.History                  0.347
		History and Society.Military and warfare     0.58
		History and Society.Politics and government  0.443
		History and Society.Society                  0.205
		History and Society.Transportation           0.869
		STEM.Biology                                 0.868
		STEM.Chemistry                               0.445
		STEM.Computing                               0.299
		STEM.Earth and environment                   0.513
		STEM.Engineering                             0.619
		STEM.Libraries & Information                 0.421
		STEM.Mathematics                             0.558
		STEM.Medicine & Health                       0.576
		STEM.Physics                                 0.191
		STEM.STEM*                                   0.856
		STEM.Space                                   0.859
		STEM.Technology                              0.368
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'type': 'object'}

