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
	counts (n=59996):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14008  -->  12231  1777   907  45081
			'Culture.Biography.Women'                       5105  -->   3961  1144   782  54109
			'Culture.Food and drink'                        1372  -->    900   472   132  58492
			'Culture.Internet culture'                      3477  -->   2782   695   256  56263
			'Culture.Linguistics'                           1472  -->   1125   347   102  58422
			'Culture.Literature'                            5540  -->   4096  1444   485  53971
			'Culture.Media.Books'                           1416  -->    976   440   138  58442
			'Culture.Media.Entertainment'                   1937  -->    883  1054   188  57871
			'Culture.Media.Films'                           2566  -->   1929   637   191  57239
			'Culture.Media.Media*'                         13028  -->  11131  1897  1349  45619
			'Culture.Media.Music'                           2872  -->   2386   486   182  56942
			'Culture.Media.Radio'                            274  -->    163   111    22  59700
			'Culture.Media.Software'                        2246  -->   1784   462   326  57424
			'Culture.Media.Television'                      1943  -->   1275   668   169  57884
			'Culture.Media.Video games'                     2118  -->   1897   221    68  57810
			'Culture.Performing arts'                       1354  -->    868   486   105  58537
			'Culture.Philosophy and religion'               2966  -->   1520  1446   251  56779
			'Culture.Sports'                                3832  -->   3309   523    97  56067
			'Culture.Visual arts.Architecture'              1814  -->   1258   556   156  58026
			'Culture.Visual arts.Comics and Anime'          2201  -->   1897   304   100  57695
			'Culture.Visual arts.Fashion'                   1483  -->   1161   322   110  58403
			'Culture.Visual arts.Visual arts*'              6013  -->   4376  1637   419  53564
			'Geography.Geographical'                        3953  -->   2526  1427   521  55522
			'Geography.Regions.Africa.Africa*'              5715  -->   4173  1542   512  53769
			'Geography.Regions.Africa.Central Africa'       1211  -->    704   507   144  58641
			'Geography.Regions.Africa.Eastern Africa'        450  -->    225   225    52  59494
			'Geography.Regions.Africa.Northern Africa'      1467  -->    974   493   109  58420
			'Geography.Regions.Africa.Southern Africa'      1168  -->    785   383    84  58744
			'Geography.Regions.Africa.Western Africa'        670  -->    516   154    61  59265
			'Geography.Regions.Americas.Central America'    1578  -->    896   682   128  58290
			'Geography.Regions.Americas.North America'      5362  -->   3380  1982   590  54044
			'Geography.Regions.Americas.South America'      2198  -->   1565   633   179  57619
			'Geography.Regions.Asia.Asia*'                 13666  -->  11012  2654  1251  45079
			'Geography.Regions.Asia.Central Asia'           1196  -->    884   312    96  58704
			'Geography.Regions.Asia.East Asia'              5485  -->   4194  1291   516  53995
			'Geography.Regions.Asia.North Asia'             1651  -->   1136   515   215  58130
			'Geography.Regions.Asia.South Asia'             2015  -->   1521   494   115  57866
			'Geography.Regions.Asia.Southeast Asia'         2582  -->   1696   886   186  57228
			'Geography.Regions.Asia.West Asia'              2161  -->   1671   490   121  57714
			'Geography.Regions.Europe.Eastern Europe'       3540  -->   2695   845   302  56154
			'Geography.Regions.Europe.Europe*'             12516  -->   9703  2813  1225  46255
			'Geography.Regions.Europe.Northern Europe'      2860  -->   1653  1207   257  56879
			'Geography.Regions.Europe.Southern Europe'      2800  -->   2039   761   187  57009
			'Geography.Regions.Europe.Western Europe'       4004  -->   2981  1023   242  55750
			'Geography.Regions.Oceania'                     2232  -->   1559   673   167  57597
			'History and Society.Business and economics'    3348  -->   1862  1486   339  56309
			'History and Society.Education'                 1568  -->    854   714   119  58309
			'History and Society.History'                   4494  -->   2225  2269   559  54943
			'History and Society.Military and warfare'      4968  -->   3711  1257   450  54578
			'History and Society.Politics and government'   4525  -->   2255  2270   475  54996
			'History and Society.Society'                   6042  -->   2657  3385   503  53451
			'History and Society.Transportation'            3547  -->   3193   354    88  56361
			'STEM.Biology'                                  7090  -->   6464   626   176  52730
			'STEM.Chemistry'                                1476  -->   1119   357   181  58339
			'STEM.Computing'                                2392  -->   1884   508   325  57279
			'STEM.Earth and environment'                    1628  -->   1013   615   146  58222
			'STEM.Engineering'                              2989  -->   2450   539   138  56869
			'STEM.Libraries & Information'                   479  -->    340   139    37  59480
			'STEM.Mathematics'                               932  -->    744   188    52  59012
			'STEM.Medicine & Health'                        1745  -->   1160   585   146  58105
			'STEM.Physics'                                  1338  -->    913   425   139  58519
			'STEM.STEM*'                                   20343  -->  18423  1920  1010  38643
			'STEM.Space'                                    1615  -->   1428   187    55  58326
			'STEM.Technology'                               4144  -->   2906  1238   579  55273
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.123
		Culture.Biography.Women                         0.085         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.058         0.003
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.092         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.217         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.049         0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.066         0.024
		Geography.Regions.Africa.Africa*                0.095         0.008
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.037         0.006
		Geography.Regions.Asia.Asia*                    0.228         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.091         0.011
		Geography.Regions.Asia.North Asia               0.028         0.001
		Geography.Regions.Asia.South Asia               0.034         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.059         0.013
		Geography.Regions.Europe.Europe*                0.209         0.076
		Geography.Regions.Europe.Northern Europe        0.048         0.031
		Geography.Regions.Europe.Southern Europe        0.047         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.026         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.083         0.014
		History and Society.Politics and government     0.075         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.118         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.029         0.006
		STEM.Physics                                    0.022         0.001
		STEM.STEM*                                      0.339         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.051, macro=0.017):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.063
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.003
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.083
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.015
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.022
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.983):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.997
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.917
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.978
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.763, macro=0.712):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.776
		Culture.Food and drink                       0.656
		Culture.Internet culture                     0.8
		Culture.Linguistics                          0.764
		Culture.Literature                           0.739
		Culture.Media.Books                          0.689
		Culture.Media.Entertainment                  0.456
		Culture.Media.Films                          0.752
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.595
		Culture.Media.Software                       0.794
		Culture.Media.Television                     0.656
		Culture.Media.Video games                    0.896
		Culture.Performing arts                      0.641
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.864
		Culture.Visual arts.Architecture             0.693
		Culture.Visual arts.Comics and Anime         0.862
		Culture.Visual arts.Fashion                  0.783
		Culture.Visual arts.Visual arts*             0.728
		Geography.Geographical                       0.639
		Geography.Regions.Africa.Africa*             0.73
		Geography.Regions.Africa.Central Africa      0.581
		Geography.Regions.Africa.Eastern Africa      0.5
		Geography.Regions.Africa.Northern Africa     0.664
		Geography.Regions.Africa.Southern Africa     0.672
		Geography.Regions.Africa.Western Africa      0.77
		Geography.Regions.Americas.Central America   0.568
		Geography.Regions.Americas.North America     0.63
		Geography.Regions.Americas.South America     0.712
		Geography.Regions.Asia.Asia*                 0.806
		Geography.Regions.Asia.Central Asia          0.739
		Geography.Regions.Asia.East Asia             0.765
		Geography.Regions.Asia.North Asia            0.688
		Geography.Regions.Asia.South Asia            0.755
		Geography.Regions.Asia.Southeast Asia        0.657
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.761
		Geography.Regions.Europe.Europe*             0.775
		Geography.Regions.Europe.Northern Europe     0.578
		Geography.Regions.Europe.Southern Europe     0.728
		Geography.Regions.Europe.Western Europe      0.745
		Geography.Regions.Oceania                    0.698
		History and Society.Business and economics   0.556
		History and Society.Education                0.545
		History and Society.History                  0.495
		History and Society.Military and warfare     0.747
		History and Society.Politics and government  0.498
		History and Society.Society                  0.44
		History and Society.Transportation           0.9
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.758
		STEM.Computing                               0.788
		STEM.Earth and environment                   0.622
		STEM.Engineering                             0.82
		STEM.Libraries & Information                 0.71
		STEM.Mathematics                             0.798
		STEM.Medicine & Health                       0.665
		STEM.Physics                                 0.682
		STEM.STEM*                                   0.906
		STEM.Space                                   0.884
		STEM.Technology                              0.701
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.719, macro=0.552):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.861
		Culture.Biography.Women                      0.446
		Culture.Food and drink                       0.418
		Culture.Internet culture                     0.383
		Culture.Linguistics                          0.764
		Culture.Literature                           0.566
		Culture.Media.Books                          0.542
		Culture.Media.Entertainment                  0.336
		Culture.Media.Films                          0.706
		Culture.Media.Media*                         0.649
		Culture.Media.Music                          0.865
		Culture.Media.Radio                          0.777
		Culture.Media.Software                       0.158
		Culture.Media.Television                     0.667
		Culture.Media.Video games                    0.666
		Culture.Performing arts                      0.509
		Culture.Philosophy and religion              0.556
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.734
		Culture.Visual arts.Comics and Anime         0.523
		Culture.Visual arts.Fashion                  0.252
		Culture.Visual arts.Visual arts*             0.636
		Geography.Geographical                       0.624
		Geography.Regions.Africa.Africa*             0.378
		Geography.Regions.Africa.Central Africa      0.13
		Geography.Regions.Africa.Eastern Africa      0.207
		Geography.Regions.Africa.Northern Africa     0.305
		Geography.Regions.Africa.Southern Africa     0.356
		Geography.Regions.Africa.Western Africa      0.339
		Geography.Regions.Americas.Central America   0.462
		Geography.Regions.Americas.North America     0.8
		Geography.Regions.Americas.South America     0.593
		Geography.Regions.Asia.Asia*                 0.587
		Geography.Regions.Asia.Central Asia          0.282
		Geography.Regions.Asia.East Asia             0.482
		Geography.Regions.Asia.North Asia            0.147
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.551
		Geography.Regions.Asia.West Asia             0.803
		Geography.Regions.Europe.Eastern Europe      0.649
		Geography.Regions.Europe.Europe*             0.712
		Geography.Regions.Europe.Northern Europe     0.802
		Geography.Regions.Europe.Southern Europe     0.746
		Geography.Regions.Europe.Western Europe      0.771
		Geography.Regions.Oceania                    0.788
		History and Society.Business and economics   0.486
		History and Society.Education                0.665
		History and Society.History                  0.35
		History and Society.Military and warfare     0.566
		History and Society.Politics and government  0.628
		History and Society.Society                  0.376
		History and Society.Transportation           0.898
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.277
		STEM.Computing                               0.273
		STEM.Earth and environment                   0.531
		STEM.Engineering                             0.64
		STEM.Libraries & Information                 0.415
		STEM.Mathematics                             0.274
		STEM.Medicine & Health                       0.631
		STEM.Physics                                 0.197
		STEM.STEM*                                   0.725
		STEM.Space                                   0.85
		STEM.Technology                              0.259
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.732, macro=0.598):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.566
		Culture.Food and drink                       0.511
		Culture.Internet culture                     0.518
		Culture.Linguistics                          0.764
		Culture.Literature                           0.641
		Culture.Media.Books                          0.607
		Culture.Media.Entertainment                  0.387
		Culture.Media.Films                          0.728
		Culture.Media.Media*                         0.738
		Culture.Media.Music                          0.847
		Culture.Media.Radio                          0.674
		Culture.Media.Software                       0.263
		Culture.Media.Television                     0.662
		Culture.Media.Video games                    0.764
		Culture.Performing arts                      0.567
		Culture.Philosophy and religion              0.533
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.713
		Culture.Visual arts.Comics and Anime         0.651
		Culture.Visual arts.Fashion                  0.381
		Culture.Visual arts.Visual arts*             0.679
		Geography.Geographical                       0.631
		Geography.Regions.Africa.Africa*             0.498
		Geography.Regions.Africa.Central Africa      0.213
		Geography.Regions.Africa.Eastern Africa      0.292
		Geography.Regions.Africa.Northern Africa     0.418
		Geography.Regions.Africa.Southern Africa     0.466
		Geography.Regions.Africa.Western Africa      0.47
		Geography.Regions.Americas.Central America   0.509
		Geography.Regions.Americas.North America     0.705
		Geography.Regions.Americas.South America     0.647
		Geography.Regions.Asia.Asia*                 0.679
		Geography.Regions.Asia.Central Asia          0.408
		Geography.Regions.Asia.East Asia             0.592
		Geography.Regions.Asia.North Asia            0.243
		Geography.Regions.Asia.South Asia            0.802
		Geography.Regions.Asia.Southeast Asia        0.599
		Geography.Regions.Asia.West Asia             0.788
		Geography.Regions.Europe.Eastern Europe      0.701
		Geography.Regions.Europe.Europe*             0.743
		Geography.Regions.Europe.Northern Europe     0.672
		Geography.Regions.Europe.Southern Europe     0.737
		Geography.Regions.Europe.Western Europe      0.758
		Geography.Regions.Oceania                    0.74
		History and Society.Business and economics   0.519
		History and Society.Education                0.599
		History and Society.History                  0.41
		History and Society.Military and warfare     0.644
		History and Society.Politics and government  0.556
		History and Society.Society                  0.405
		History and Society.Transportation           0.899
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.405
		STEM.Computing                               0.406
		STEM.Earth and environment                   0.573
		STEM.Engineering                             0.719
		STEM.Libraries & Information                 0.524
		STEM.Mathematics                             0.408
		STEM.Medicine & Health                       0.647
		STEM.Physics                                 0.305
		STEM.STEM*                                   0.805
		STEM.Space                                   0.867
		STEM.Technology                              0.378
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.987
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.978
		History and Society.Society                  0.984
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.02
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.029
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.027
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.009
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.026
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.972, macro=0.973):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.971
		Culture.Literature                           0.975
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.98
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.937
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.975
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.951
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.985
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.973
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.948
		Geography.Regions.Africa.Northern Africa     0.977
		Geography.Regions.Africa.Southern Africa     0.971
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.979
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.972
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.964
		Geography.Regions.Europe.Southern Europe     0.973
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.962
		History and Society.Education                0.968
		History and Society.History                  0.949
		History and Society.Military and warfare     0.975
		History and Society.Politics and government  0.943
		History and Society.Society                  0.926
		History and Society.Transportation           0.985
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.982
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.985
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.978
		STEM.Space                                   0.989
		STEM.Technology                              0.973
		-------------------------------------------  -----
	pr_auc (micro=0.78, macro=0.609):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.919
		Culture.Biography.Women                      0.543
		Culture.Food and drink                       0.521
		Culture.Internet culture                     0.598
		Culture.Linguistics                          0.765
		Culture.Literature                           0.7
		Culture.Media.Books                          0.565
		Culture.Media.Entertainment                  0.335
		Culture.Media.Films                          0.777
		Culture.Media.Media*                         0.836
		Culture.Media.Music                          0.889
		Culture.Media.Radio                          0.533
		Culture.Media.Software                       0.35
		Culture.Media.Television                     0.651
		Culture.Media.Video games                    0.873
		Culture.Performing arts                      0.539
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.951
		Culture.Visual arts.Architecture             0.737
		Culture.Visual arts.Comics and Anime         0.734
		Culture.Visual arts.Fashion                  0.254
		Culture.Visual arts.Visual arts*             0.715
		Geography.Geographical                       0.646
		Geography.Regions.Africa.Africa*             0.506
		Geography.Regions.Africa.Central Africa      0.26
		Geography.Regions.Africa.Eastern Africa      0.122
		Geography.Regions.Africa.Northern Africa     0.378
		Geography.Regions.Africa.Southern Africa     0.39
		Geography.Regions.Africa.Western Africa      0.357
		Geography.Regions.Americas.Central America   0.446
		Geography.Regions.Americas.North America     0.791
		Geography.Regions.Americas.South America     0.639
		Geography.Regions.Asia.Asia*                 0.757
		Geography.Regions.Asia.Central Asia          0.493
		Geography.Regions.Asia.East Asia             0.604
		Geography.Regions.Asia.North Asia            0.255
		Geography.Regions.Asia.South Asia            0.838
		Geography.Regions.Asia.Southeast Asia        0.59
		Geography.Regions.Asia.West Asia             0.817
		Geography.Regions.Europe.Eastern Europe      0.76
		Geography.Regions.Europe.Europe*             0.817
		Geography.Regions.Europe.Northern Europe     0.74
		Geography.Regions.Europe.Southern Europe     0.762
		Geography.Regions.Europe.Western Europe      0.812
		Geography.Regions.Oceania                    0.777
		History and Society.Business and economics   0.498
		History and Society.Education                0.594
		History and Society.History                  0.373
		History and Society.Military and warfare     0.727
		History and Society.Politics and government  0.59
		History and Society.Society                  0.398
		History and Society.Transportation           0.92
		STEM.Biology                                 0.954
		STEM.Chemistry                               0.406
		STEM.Computing                               0.38
		STEM.Earth and environment                   0.541
		STEM.Engineering                             0.749
		STEM.Libraries & Information                 0.382
		STEM.Mathematics                             0.508
		STEM.Medicine & Health                       0.66
		STEM.Physics                                 0.268
		STEM.STEM*                                   0.903
		STEM.Space                                   0.922
		STEM.Technology                              0.382
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

