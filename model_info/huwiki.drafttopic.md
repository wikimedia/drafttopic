Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'label_weights': {}, 'multilabel': True, 'n_iter_no_change': None, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_samples_leaf': 1, 'max_depth': 5, 'loss': 'deviance', 'subsample': 1.0, 'population_rates': None, 'presort': 'deprecated', 'scale': False, 'tol': 0.0001, 'center': False, 'learning_rate': 0.1, 'min_samples_split': 2, 'min_impurity_split': None, 'ccp_alpha': 0.0, 'n_estimators': 150, 'verbose': 0, 'validation_fraction': 0.1, 'min_weight_fraction_leaf': 0.0, 'init': None, 'warm_start': False, 'criterion': 'friedman_mse', 'random_state': None, 'min_impurity_decrease': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology']}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=58091):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15858  -->  13485  2373  1219  41014
			'Culture.Biography.Women'                       3430  -->   2034  1396   412  54249
			'Culture.Food and drink'                        1437  -->    810   627   162  56492
			'Culture.Internet culture'                      3186  -->   2507   679   220  54685
			'Culture.Linguistics'                           1547  -->    910   637   122  56422
			'Culture.Literature'                            5411  -->   3644  1767   585  52095
			'Culture.Media.Books'                           1616  -->   1183   433   114  56361
			'Culture.Media.Entertainment'                   2234  -->    752  1482   220  55637
			'Culture.Media.Films'                           2873  -->   2228   645   178  55040
			'Culture.Media.Media*'                         13982  -->  11961  2021  1382  42727
			'Culture.Media.Music'                           3151  -->   2500   651   294  54646
			'Culture.Media.Radio'                            303  -->    141   162    35  57753
			'Culture.Media.Software'                        2106  -->   1590   516   307  55678
			'Culture.Media.Television'                      2497  -->   1871   626   165  55429
			'Culture.Media.Video games'                     2093  -->   1815   278    57  55941
			'Culture.Performing arts'                       1431  -->    736   695   150  56510
			'Culture.Philosophy and religion'               3836  -->   1919  1917   402  53853
			'Culture.Sports'                                6321  -->   5547   774   228  51542
			'Culture.Visual arts.Architecture'              1971  -->   1222   749   270  55850
			'Culture.Visual arts.Comics and Anime'          1850  -->   1389   461   115  56126
			'Culture.Visual arts.Fashion'                    766  -->    399   367    71  57254
			'Culture.Visual arts.Visual arts*'              5221  -->   3282  1939   513  52357
			'Geography.Geographical'                        3706  -->   2219  1487   599  53786
			'Geography.Regions.Africa.Africa*'              3932  -->   2343  1589   395  53764
			'Geography.Regions.Africa.Central Africa'        844  -->    474   370    75  57172
			'Geography.Regions.Africa.Eastern Africa'        322  -->    162   160    37  57732
			'Geography.Regions.Africa.Northern Africa'      1466  -->    826   640   143  56482
			'Geography.Regions.Africa.Southern Africa'       651  -->    407   244    49  57391
			'Geography.Regions.Africa.Western Africa'        158  -->     80    78    29  57904
			'Geography.Regions.Americas.Central America'    1326  -->    628   698   100  56665
			'Geography.Regions.Americas.North America'      5580  -->   3126  2454   860  51651
			'Geography.Regions.Americas.South America'      1564  -->    913   651   150  56377
			'Geography.Regions.Asia.Asia*'                 11124  -->   8335  2789  1071  45896
			'Geography.Regions.Asia.Central Asia'           1019  -->    516   503    69  57003
			'Geography.Regions.Asia.East Asia'              3278  -->   2399   879   259  54554
			'Geography.Regions.Asia.North Asia'             2919  -->   1970   949   240  54932
			'Geography.Regions.Asia.South Asia'             1645  -->   1003   642   115  56331
			'Geography.Regions.Asia.Southeast Asia'         1562  -->    727   835   111  56418
			'Geography.Regions.Asia.West Asia'              2224  -->   1412   812   194  55673
			'Geography.Regions.Europe.Eastern Europe'       5703  -->   4053  1650   585  51803
			'Geography.Regions.Europe.Europe*'             17669  -->  13988  3681  2493  37929
			'Geography.Regions.Europe.Northern Europe'      3556  -->   2179  1377   426  54109
			'Geography.Regions.Europe.Southern Europe'      4000  -->   2798  1202   387  53704
			'Geography.Regions.Europe.Western Europe'       5222  -->   3847  1375   616  52253
			'Geography.Regions.Oceania'                     1283  -->    634   649   140  56668
			'History and Society.Business and economics'    2975  -->   1372  1603   323  54793
			'History and Society.Education'                 1523  -->    520  1003   126  56442
			'History and Society.History'                   5599  -->   3098  2501   752  51740
			'History and Society.Military and warfare'      4234  -->   2546  1688   466  53391
			'History and Society.Politics and government'   3121  -->   1405  1716   309  54661
			'History and Society.Society'                   3943  -->    937  3006   217  53931
			'History and Society.Transportation'            4131  -->   3597   534   188  53772
			'STEM.Biology'                                  4567  -->   3812   755   188  53336
			'STEM.Chemistry'                                1555  -->   1135   420   176  56360
			'STEM.Computing'                                2379  -->   1815   564   320  55392
			'STEM.Earth and environment'                    1797  -->   1124   673   160  56134
			'STEM.Engineering'                              2362  -->   1564   798   210  55519
			'STEM.Libraries & Information'                   478  -->    241   237    50  57563
			'STEM.Mathematics'                               943  -->    690   253    46  57102
			'STEM.Medicine & Health'                        1870  -->   1141   729   214  56007
			'STEM.Physics'                                  1381  -->    775   606   179  56531
			'STEM.STEM*'                                   17908  -->  15643  2265  1127  39056
			'STEM.Space'                                    2233  -->   2026   207    58  55800
			'STEM.Technology'                               4706  -->   3311  1395   590  52795
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.273         0.13
		Culture.Biography.Women                         0.059         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.055         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.093         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.049         0.012
		Culture.Media.Media*                            0.241         0.056
		Culture.Media.Music                             0.054         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.043         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.066         0.011
		Culture.Sports                                  0.109         0.061
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.032         0.002
		Culture.Visual arts.Fashion                     0.013         0.001
		Culture.Visual arts.Visual arts*                0.09          0.018
		Geography.Geographical                          0.064         0.021
		Geography.Regions.Africa.Africa*                0.068         0.009
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.004
		Geography.Regions.Americas.North America        0.096         0.064
		Geography.Regions.Americas.South America        0.027         0.007
		Geography.Regions.Asia.Asia*                    0.191         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.056         0.012
		Geography.Regions.Asia.North Asia               0.05          0.006
		Geography.Regions.Asia.South Asia               0.028         0.017
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.038         0.012
		Geography.Regions.Europe.Eastern Europe         0.098         0.019
		Geography.Regions.Europe.Europe*                0.304         0.082
		Geography.Regions.Europe.Northern Europe        0.061         0.029
		Geography.Regions.Europe.Southern Europe        0.069         0.014
		Geography.Regions.Europe.Western Europe         0.09          0.021
		Geography.Regions.Oceania                       0.022         0.005
		History and Society.Business and economics      0.051         0.01
		History and Society.Education                   0.026         0.008
		History and Society.History                     0.096         0.011
		History and Society.Military and warfare        0.073         0.016
		History and Society.Politics and government     0.054         0.017
		History and Society.Society                     0.068         0.008
		History and Society.Transportation              0.071         0.016
		STEM.Biology                                    0.079         0.035
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.041         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.032         0.007
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.308         0.066
		STEM.Space                                      0.038         0.004
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.055, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.135
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.058
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.008
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.024
		Geography.Regions.Europe.Europe*             0.122
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.017
		Geography.Regions.Europe.Western Europe      0.027
		Geography.Regions.Oceania                    0.005
		History and Society.Business and economics   0.01
		History and Society.Education                0.005
		History and Society.History                  0.02
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.013
		History and Society.Society                  0.006
		History and Society.Transportation           0.018
		STEM.Biology                                 0.033
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.084
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.945, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.992
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.878
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.973
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.98
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.987
		History and Society.Society                  0.994
		History and Society.Transportation           0.982
		STEM.Biology                                 0.967
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.916
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.725, macro=0.638):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.85
		Culture.Biography.Women                      0.593
		Culture.Food and drink                       0.564
		Culture.Internet culture                     0.787
		Culture.Linguistics                          0.588
		Culture.Literature                           0.673
		Culture.Media.Books                          0.732
		Culture.Media.Entertainment                  0.337
		Culture.Media.Films                          0.775
		Culture.Media.Media*                         0.855
		Culture.Media.Music                          0.793
		Culture.Media.Radio                          0.465
		Culture.Media.Software                       0.755
		Culture.Media.Television                     0.749
		Culture.Media.Video games                    0.867
		Culture.Performing arts                      0.514
		Culture.Philosophy and religion              0.5
		Culture.Sports                               0.878
		Culture.Visual arts.Architecture             0.62
		Culture.Visual arts.Comics and Anime         0.751
		Culture.Visual arts.Fashion                  0.521
		Culture.Visual arts.Visual arts*             0.629
		Geography.Geographical                       0.599
		Geography.Regions.Africa.Africa*             0.596
		Geography.Regions.Africa.Central Africa      0.562
		Geography.Regions.Africa.Eastern Africa      0.503
		Geography.Regions.Africa.Northern Africa     0.563
		Geography.Regions.Africa.Southern Africa     0.625
		Geography.Regions.Africa.Western Africa      0.506
		Geography.Regions.Americas.Central America   0.474
		Geography.Regions.Americas.North America     0.56
		Geography.Regions.Americas.South America     0.584
		Geography.Regions.Asia.Asia*                 0.749
		Geography.Regions.Asia.Central Asia          0.506
		Geography.Regions.Asia.East Asia             0.732
		Geography.Regions.Asia.North Asia            0.675
		Geography.Regions.Asia.South Asia            0.61
		Geography.Regions.Asia.Southeast Asia        0.465
		Geography.Regions.Asia.West Asia             0.635
		Geography.Regions.Europe.Eastern Europe      0.711
		Geography.Regions.Europe.Europe*             0.792
		Geography.Regions.Europe.Northern Europe     0.613
		Geography.Regions.Europe.Southern Europe     0.7
		Geography.Regions.Europe.Western Europe      0.737
		Geography.Regions.Oceania                    0.494
		History and Society.Business and economics   0.461
		History and Society.Education                0.341
		History and Society.History                  0.553
		History and Society.Military and warfare     0.601
		History and Society.Politics and government  0.45
		History and Society.Society                  0.238
		History and Society.Transportation           0.871
		STEM.Biology                                 0.835
		STEM.Chemistry                               0.73
		STEM.Computing                               0.763
		STEM.Earth and environment                   0.625
		STEM.Engineering                             0.662
		STEM.Libraries & Information                 0.504
		STEM.Mathematics                             0.732
		STEM.Medicine & Health                       0.61
		STEM.Physics                                 0.561
		STEM.STEM*                                   0.874
		STEM.Space                                   0.907
		STEM.Technology                              0.704
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.994
		History and Society.Society                  0.996
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.656, macro=0.517):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.815
		Culture.Biography.Women                      0.548
		Culture.Food and drink                       0.338
		Culture.Internet culture                     0.427
		Culture.Linguistics                          0.691
		Culture.Literature                           0.481
		Culture.Media.Books                          0.615
		Culture.Media.Entertainment                  0.256
		Culture.Media.Films                          0.74
		Culture.Media.Media*                         0.617
		Culture.Media.Music                          0.763
		Culture.Media.Radio                          0.645
		Culture.Media.Software                       0.155
		Culture.Media.Television                     0.696
		Culture.Media.Video games                    0.716
		Culture.Performing arts                      0.376
		Culture.Philosophy and religion              0.418
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.588
		Culture.Visual arts.Comics and Anime         0.472
		Culture.Visual arts.Fashion                  0.277
		Culture.Visual arts.Visual arts*             0.547
		Geography.Geographical                       0.543
		Geography.Regions.Africa.Africa*             0.415
		Geography.Regions.Africa.Central Africa      0.234
		Geography.Regions.Africa.Eastern Africa      0.286
		Geography.Regions.Africa.Northern Africa     0.234
		Geography.Regions.Africa.Southern Africa     0.493
		Geography.Regions.Africa.Western Africa      0.434
		Geography.Regions.Americas.Central America   0.486
		Geography.Regions.Americas.North America     0.7
		Geography.Regions.Americas.South America     0.606
		Geography.Regions.Asia.Asia*                 0.649
		Geography.Regions.Asia.Central Asia          0.253
		Geography.Regions.Asia.East Asia             0.659
		Geography.Regions.Asia.North Asia            0.47
		Geography.Regions.Asia.South Asia            0.836
		Geography.Regions.Asia.Southeast Asia        0.601
		Geography.Regions.Asia.West Asia             0.687
		Geography.Regions.Europe.Eastern Europe      0.546
		Geography.Regions.Europe.Europe*             0.534
		Geography.Regions.Europe.Northern Europe     0.704
		Geography.Regions.Europe.Southern Europe     0.582
		Geography.Regions.Europe.Western Europe      0.573
		Geography.Regions.Oceania                    0.481
		History and Society.Business and economics   0.439
		History and Society.Education                0.554
		History and Society.History                  0.3
		History and Society.Military and warfare     0.523
		History and Society.Politics and government  0.574
		History and Society.Society                  0.334
		History and Society.Transportation           0.807
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.287
		STEM.Computing                               0.276
		STEM.Earth and environment                   0.515
		STEM.Engineering                             0.507
		STEM.Libraries & Information                 0.287
		STEM.Mathematics                             0.299
		STEM.Medicine & Health                       0.513
		STEM.Physics                                 0.145
		STEM.STEM*                                   0.687
		STEM.Space                                   0.791
		STEM.Technology                              0.25
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.681, macro=0.554):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.832
		Culture.Biography.Women                      0.57
		Culture.Food and drink                       0.423
		Culture.Internet culture                     0.554
		Culture.Linguistics                          0.636
		Culture.Literature                           0.561
		Culture.Media.Books                          0.668
		Culture.Media.Entertainment                  0.291
		Culture.Media.Films                          0.757
		Culture.Media.Media*                         0.717
		Culture.Media.Music                          0.778
		Culture.Media.Radio                          0.541
		Culture.Media.Software                       0.257
		Culture.Media.Television                     0.722
		Culture.Media.Video games                    0.784
		Culture.Performing arts                      0.435
		Culture.Philosophy and religion              0.455
		Culture.Sports                               0.902
		Culture.Visual arts.Architecture             0.603
		Culture.Visual arts.Comics and Anime         0.579
		Culture.Visual arts.Fashion                  0.361
		Culture.Visual arts.Visual arts*             0.585
		Geography.Geographical                       0.57
		Geography.Regions.Africa.Africa*             0.489
		Geography.Regions.Africa.Central Africa      0.331
		Geography.Regions.Africa.Eastern Africa      0.365
		Geography.Regions.Africa.Northern Africa     0.331
		Geography.Regions.Africa.Southern Africa     0.551
		Geography.Regions.Africa.Western Africa      0.467
		Geography.Regions.Americas.Central America   0.48
		Geography.Regions.Americas.North America     0.622
		Geography.Regions.Americas.South America     0.595
		Geography.Regions.Asia.Asia*                 0.696
		Geography.Regions.Asia.Central Asia          0.337
		Geography.Regions.Asia.East Asia             0.694
		Geography.Regions.Asia.North Asia            0.554
		Geography.Regions.Asia.South Asia            0.705
		Geography.Regions.Asia.Southeast Asia        0.525
		Geography.Regions.Asia.West Asia             0.66
		Geography.Regions.Europe.Eastern Europe      0.618
		Geography.Regions.Europe.Europe*             0.638
		Geography.Regions.Europe.Northern Europe     0.655
		Geography.Regions.Europe.Southern Europe     0.636
		Geography.Regions.Europe.Western Europe      0.645
		Geography.Regions.Oceania                    0.488
		History and Society.Business and economics   0.45
		History and Society.Education                0.422
		History and Society.History                  0.389
		History and Society.Military and warfare     0.559
		History and Society.Politics and government  0.505
		History and Society.Society                  0.278
		History and Society.Transportation           0.838
		STEM.Biology                                 0.864
		STEM.Chemistry                               0.412
		STEM.Computing                               0.405
		STEM.Earth and environment                   0.565
		STEM.Engineering                             0.574
		STEM.Libraries & Information                 0.366
		STEM.Mathematics                             0.424
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.23
		STEM.STEM*                                   0.769
		STEM.Space                                   0.845
		STEM.Technology                              0.369
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.993
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.981
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.984
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.965
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.926
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.989
		History and Society.Education                0.992
		History and Society.History                  0.981
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.985
		History and Society.Society                  0.99
		History and Society.Transportation           0.994
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.965
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.029
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.016
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.023
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.011
		Geography.Regions.Europe.Europe*             0.062
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.006
		History and Society.Society                  0.004
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.963, macro=0.962):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.964
		Culture.Food and drink                       0.966
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.959
		Culture.Literature                           0.967
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.953
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.911
		Culture.Media.Software                       0.983
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.963
		Culture.Philosophy and religion              0.943
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.983
		Culture.Visual arts.Fashion                  0.961
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.96
		Geography.Regions.Africa.Africa*             0.958
		Geography.Regions.Africa.Central Africa      0.98
		Geography.Regions.Africa.Eastern Africa      0.939
		Geography.Regions.Africa.Northern Africa     0.963
		Geography.Regions.Africa.Southern Africa     0.961
		Geography.Regions.Africa.Western Africa      0.886
		Geography.Regions.Americas.Central America   0.961
		Geography.Regions.Americas.North America     0.947
		Geography.Regions.Americas.South America     0.967
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.963
		Geography.Regions.Asia.East Asia             0.972
		Geography.Regions.Asia.North Asia            0.968
		Geography.Regions.Asia.South Asia            0.967
		Geography.Regions.Asia.Southeast Asia        0.957
		Geography.Regions.Asia.West Asia             0.965
		Geography.Regions.Europe.Eastern Europe      0.962
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.96
		Geography.Regions.Europe.Southern Europe     0.966
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.959
		History and Society.Business and economics   0.941
		History and Society.Education                0.947
		History and Society.History                  0.94
		History and Society.Military and warfare     0.96
		History and Society.Politics and government  0.938
		History and Society.Society                  0.885
		History and Society.Transportation           0.983
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.981
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.97
		STEM.Libraries & Information                 0.959
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.967
		STEM.Physics                                 0.974
		STEM.STEM*                                   0.972
		STEM.Space                                   0.991
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.719, macro=0.535):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.543
		Culture.Food and drink                       0.349
		Culture.Internet culture                     0.662
		Culture.Linguistics                          0.593
		Culture.Literature                           0.597
		Culture.Media.Books                          0.662
		Culture.Media.Entertainment                  0.199
		Culture.Media.Films                          0.773
		Culture.Media.Media*                         0.832
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.296
		Culture.Media.Software                       0.247
		Culture.Media.Television                     0.724
		Culture.Media.Video games                    0.862
		Culture.Performing arts                      0.382
		Culture.Philosophy and religion              0.406
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.59
		Culture.Visual arts.Comics and Anime         0.616
		Culture.Visual arts.Fashion                  0.26
		Culture.Visual arts.Visual arts*             0.601
		Geography.Geographical                       0.548
		Geography.Regions.Africa.Africa*             0.467
		Geography.Regions.Africa.Central Africa      0.217
		Geography.Regions.Africa.Eastern Africa      0.141
		Geography.Regions.Africa.Northern Africa     0.225
		Geography.Regions.Africa.Southern Africa     0.421
		Geography.Regions.Africa.Western Africa      0.238
		Geography.Regions.Americas.Central America   0.423
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.533
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.169
		Geography.Regions.Asia.East Asia             0.721
		Geography.Regions.Asia.North Asia            0.565
		Geography.Regions.Asia.South Asia            0.754
		Geography.Regions.Asia.Southeast Asia        0.479
		Geography.Regions.Asia.West Asia             0.657
		Geography.Regions.Europe.Eastern Europe      0.649
		Geography.Regions.Europe.Europe*             0.739
		Geography.Regions.Europe.Northern Europe     0.679
		Geography.Regions.Europe.Southern Europe     0.679
		Geography.Regions.Europe.Western Europe      0.697
		Geography.Regions.Oceania                    0.431
		History and Society.Business and economics   0.382
		History and Society.Education                0.38
		History and Society.History                  0.4
		History and Society.Military and warfare     0.584
		History and Society.Politics and government  0.5
		History and Society.Society                  0.211
		History and Society.Transportation           0.854
		STEM.Biology                                 0.883
		STEM.Chemistry                               0.379
		STEM.Computing                               0.37
		STEM.Earth and environment                   0.551
		STEM.Engineering                             0.563
		STEM.Libraries & Information                 0.167
		STEM.Mathematics                             0.487
		STEM.Medicine & Health                       0.509
		STEM.Physics                                 0.131
		STEM.STEM*                                   0.872
		STEM.Space                                   0.883
		STEM.Technology                              0.473
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}}}}}

