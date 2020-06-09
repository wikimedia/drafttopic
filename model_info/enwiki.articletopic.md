Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'init': None, 'min_samples_split': 2, 'max_depth': 5, 'n_estimators': 150, 'warm_start': False, 'ccp_alpha': 0.0, 'min_samples_leaf': 1, 'multilabel': True, 'tol': 0.0001, 'scale': False, 'label_weights': {}, 'subsample': 1.0, 'population_rates': None, 'min_impurity_decrease': 0.0, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_features': 'log2', 'presort': 'deprecated', 'loss': 'deviance', 'min_impurity_split': None, 'verbose': 0, 'center': False, 'random_state': None, 'n_iter_no_change': None, 'validation_fraction': 0.1, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'criterion': 'friedman_mse'}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.12'
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
	counts (n=63871):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16688  -->  14910  1778  1157  46026
			'Culture.Biography.Women'                       4203  -->   3273   930   777  58891
			'Culture.Food and drink'                        1319  -->    991   328    72  62480
			'Culture.Internet culture'                      2966  -->   2405   561   227  60678
			'Culture.Linguistics'                           1367  -->    999   368    99  62405
			'Culture.Literature'                            5335  -->   4027  1308   503  58033
			'Culture.Media.Books'                           1980  -->   1402   578   174  61717
			'Culture.Media.Entertainment'                   1865  -->    980   885   167  61839
			'Culture.Media.Films'                           2271  -->   1842   429   191  61409
			'Culture.Media.Media*'                         14408  -->  12394  2014  1482  47981
			'Culture.Media.Music'                           2589  -->   2114   475   279  61003
			'Culture.Media.Radio'                           1181  -->    965   216    32  62658
			'Culture.Media.Software'                        1848  -->   1152   696   386  61637
			'Culture.Media.Television'                      2246  -->   1639   607   207  61418
			'Culture.Media.Video games'                     2113  -->   1931   182    49  61709
			'Culture.Performing arts'                       1344  -->    916   428   110  62417
			'Culture.Philosophy and religion'               2760  -->   1541  1219   361  60750
			'Culture.Sports'                                5903  -->   5407   496   296  57672
			'Culture.Visual arts.Architecture'              2502  -->   1846   656   268  61101
			'Culture.Visual arts.Comics and Anime'          1482  -->   1190   292   108  62281
			'Culture.Visual arts.Fashion'                   1163  -->    868   295    60  62648
			'Culture.Visual arts.Visual arts*'              5882  -->   4492  1390   561  57428
			'Geography.Geographical'                        3516  -->   2325  1191   331  60024
			'Geography.Regions.Africa.Africa*'              6411  -->   5538   873   326  57134
			'Geography.Regions.Africa.Central Africa'       1131  -->    560   571   117  62623
			'Geography.Regions.Africa.Eastern Africa'       1102  -->    868   234    28  62741
			'Geography.Regions.Africa.Northern Africa'      1273  -->    939   334    90  62508
			'Geography.Regions.Africa.Southern Africa'      1276  -->    947   329    59  62536
			'Geography.Regions.Africa.Western Africa'       1133  -->    922   211    68  62670
			'Geography.Regions.Americas.Central America'    1313  -->    932   381    62  62496
			'Geography.Regions.Americas.North America'      7583  -->   5263  2320  1222  55066
			'Geography.Regions.Americas.South America'      1545  -->   1162   383   125  62201
			'Geography.Regions.Asia.Asia*'                 11018  -->   9458  1560   903  51950
			'Geography.Regions.Asia.Central Asia'           1136  -->    894   242    41  62694
			'Geography.Regions.Asia.East Asia'              2653  -->   1993   660   281  60937
			'Geography.Regions.Asia.North Asia'             1372  -->    917   455   206  62293
			'Geography.Regions.Asia.South Asia'             2432  -->   2055   377   112  61327
			'Geography.Regions.Asia.Southeast Asia'         1671  -->   1302   369    91  62109
			'Geography.Regions.Asia.West Asia'              2256  -->   1780   476   140  61475
			'Geography.Regions.Europe.Eastern Europe'       3088  -->   2328   760   306  60477
			'Geography.Regions.Europe.Europe*'             12499  -->   9540  2959  1890  49482
			'Geography.Regions.Europe.Northern Europe'      4299  -->   2934  1365   641  58931
			'Geography.Regions.Europe.Southern Europe'      2421  -->   1702   719   276  61174
			'Geography.Regions.Europe.Western Europe'       3102  -->   1993  1109   399  60370
			'Geography.Regions.Oceania'                     2544  -->   2018   526   131  61196
			'History and Society.Business and economics'    3372  -->   1631  1741   534  59965
			'History and Society.Education'                 2152  -->   1145  1007   280  61439
			'History and Society.History'                   3283  -->   1529  1754   513  60075
			'History and Society.Military and warfare'      4108  -->   2934  1174   413  59350
			'History and Society.Politics and government'   4612  -->   2865  1747   512  58747
			'History and Society.Society'                   4043  -->   1486  2557   396  59432
			'History and Society.Transportation'            3628  -->   3162   466   237  60006
			'STEM.Biology'                                  2988  -->   2448   540   172  60711
			'STEM.Chemistry'                                1334  -->    930   404   186  62351
			'STEM.Computing'                                2037  -->   1404   633   406  61428
			'STEM.Earth and environment'                    1648  -->   1182   466   121  62102
			'STEM.Engineering'                              2314  -->   1694   620   174  61383
			'STEM.Libraries & Information'                  1144  -->    679   465    71  62656
			'STEM.Mathematics'                              1107  -->    817   290    89  62675
			'STEM.Medicine & Health'                        1784  -->   1232   552   201  61886
			'STEM.Physics'                                  1206  -->    814   392   153  62512
			'STEM.STEM*'                                   16602  -->  14386  2216   978  46291
			'STEM.Space'                                    1366  -->   1205   161    60  62445
			'STEM.Technology'                               3701  -->   2357  1344   635  59535
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.261         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.046         0.003
		Culture.Linguistics                             0.021         0.007
		Culture.Literature                              0.084         0.015
		Culture.Media.Books                             0.031         0.004
		Culture.Media.Entertainment                     0.029         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.226         0.058
		Culture.Media.Music                             0.041         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.029         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.043         0.011
		Culture.Sports                                  0.092         0.071
		Culture.Visual arts.Architecture                0.039         0.011
		Culture.Visual arts.Comics and Anime            0.023         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.092         0.018
		Geography.Geographical                          0.055         0.024
		Geography.Regions.Africa.Africa*                0.1           0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.017         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.173         0.045
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.042         0.011
		Geography.Regions.Asia.North Asia               0.021         0.001
		Geography.Regions.Asia.South Asia               0.038         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.035         0.011
		Geography.Regions.Europe.Eastern Europe         0.048         0.013
		Geography.Regions.Europe.Europe*                0.196         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.038         0.013
		Geography.Regions.Europe.Western Europe         0.049         0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.072         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.047         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.017         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.26          0.069
		STEM.Space                                      0.021         0.006
		STEM.Technology                                 0.058         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.132
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.065
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.015
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.092
		Geography.Regions.Europe.Northern Europe     0.031
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.014
		History and Society.Education                0.008
		History and Society.History                  0.013
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.011
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.079
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.868
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.935
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.985
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.908
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.989
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.921
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.78, macro=0.728):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.893
		Culture.Biography.Women                      0.779
		Culture.Food and drink                       0.751
		Culture.Internet culture                     0.811
		Culture.Linguistics                          0.731
		Culture.Literature                           0.755
		Culture.Media.Books                          0.708
		Culture.Media.Entertainment                  0.525
		Culture.Media.Films                          0.811
		Culture.Media.Media*                         0.86
		Culture.Media.Music                          0.817
		Culture.Media.Radio                          0.817
		Culture.Media.Software                       0.623
		Culture.Media.Television                     0.73
		Culture.Media.Video games                    0.914
		Culture.Performing arts                      0.682
		Culture.Philosophy and religion              0.558
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.738
		Culture.Visual arts.Comics and Anime         0.803
		Culture.Visual arts.Fashion                  0.746
		Culture.Visual arts.Visual arts*             0.764
		Geography.Geographical                       0.661
		Geography.Regions.Africa.Africa*             0.864
		Geography.Regions.Africa.Central Africa      0.495
		Geography.Regions.Africa.Eastern Africa      0.788
		Geography.Regions.Africa.Northern Africa     0.738
		Geography.Regions.Africa.Southern Africa     0.742
		Geography.Regions.Africa.Western Africa      0.814
		Geography.Regions.Americas.Central America   0.71
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.752
		Geography.Regions.Asia.Asia*                 0.858
		Geography.Regions.Asia.Central Asia          0.787
		Geography.Regions.Asia.East Asia             0.751
		Geography.Regions.Asia.North Asia            0.668
		Geography.Regions.Asia.South Asia            0.845
		Geography.Regions.Asia.Southeast Asia        0.779
		Geography.Regions.Asia.West Asia             0.789
		Geography.Regions.Europe.Eastern Europe      0.754
		Geography.Regions.Europe.Europe*             0.763
		Geography.Regions.Europe.Northern Europe     0.682
		Geography.Regions.Europe.Southern Europe     0.703
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.793
		History and Society.Business and economics   0.484
		History and Society.Education                0.532
		History and Society.History                  0.466
		History and Society.Military and warfare     0.714
		History and Society.Politics and government  0.621
		History and Society.Society                  0.368
		History and Society.Transportation           0.872
		STEM.Biology                                 0.819
		STEM.Chemistry                               0.697
		STEM.Computing                               0.689
		STEM.Earth and environment                   0.717
		STEM.Engineering                             0.732
		STEM.Libraries & Information                 0.594
		STEM.Mathematics                             0.738
		STEM.Medicine & Health                       0.691
		STEM.Physics                                 0.675
		STEM.STEM*                                   0.867
		STEM.Space                                   0.882
		STEM.Technology                              0.637
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
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
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
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
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
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
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.705, macro=0.567):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.836
		Culture.Biography.Women                      0.469
		Culture.Food and drink                       0.617
		Culture.Internet culture                     0.433
		Culture.Linguistics                          0.773
		Culture.Literature                           0.58
		Culture.Media.Books                          0.504
		Culture.Media.Entertainment                  0.412
		Culture.Media.Films                          0.735
		Culture.Media.Media*                         0.641
		Culture.Media.Music                          0.814
		Culture.Media.Radio                          0.776
		Culture.Media.Software                       0.118
		Culture.Media.Television                     0.659
		Culture.Media.Video games                    0.751
		Culture.Performing arts                      0.529
		Culture.Philosophy and religion              0.504
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.643
		Culture.Visual arts.Comics and Anime         0.505
		Culture.Visual arts.Fashion                  0.387
		Culture.Visual arts.Visual arts*             0.595
		Geography.Geographical                       0.744
		Geography.Regions.Africa.Africa*             0.545
		Geography.Regions.Africa.Central Africa      0.144
		Geography.Regions.Africa.Eastern Africa      0.446
		Geography.Regions.Africa.Northern Africa     0.387
		Geography.Regions.Africa.Southern Africa     0.481
		Geography.Regions.Africa.Western Africa      0.339
		Geography.Regions.Americas.Central America   0.703
		Geography.Regions.Americas.North America     0.687
		Geography.Regions.Americas.South America     0.704
		Geography.Regions.Asia.Asia*                 0.705
		Geography.Regions.Asia.Central Asia          0.511
		Geography.Regions.Asia.East Asia             0.654
		Geography.Regions.Asia.North Asia            0.158
		Geography.Regions.Asia.South Asia            0.877
		Geography.Regions.Asia.Southeast Asia        0.763
		Geography.Regions.Asia.West Asia             0.793
		Geography.Regions.Europe.Eastern Europe      0.661
		Geography.Regions.Europe.Europe*             0.631
		Geography.Regions.Europe.Northern Europe     0.667
		Geography.Regions.Europe.Southern Europe     0.674
		Geography.Regions.Europe.Western Europe      0.657
		Geography.Regions.Oceania                    0.851
		History and Society.Business and economics   0.358
		History and Society.Education                0.465
		History and Society.History                  0.376
		History and Society.Military and warfare     0.596
		History and Society.Politics and government  0.676
		History and Society.Society                  0.415
		History and Society.Transportation           0.772
		STEM.Biology                                 0.91
		STEM.Chemistry                               0.268
		STEM.Computing                               0.221
		STEM.Earth and environment                   0.627
		STEM.Engineering                             0.577
		STEM.Libraries & Information                 0.246
		STEM.Mathematics                             0.178
		STEM.Medicine & Health                       0.579
		STEM.Physics                                 0.19
		STEM.STEM*                                   0.757
		STEM.Space                                   0.848
		STEM.Technology                              0.237
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
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
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
		History and Society.Education                0.997
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
	f1 (micro=0.736, macro=0.62):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.864
		Culture.Biography.Women                      0.585
		Culture.Food and drink                       0.678
		Culture.Internet culture                     0.565
		Culture.Linguistics                          0.751
		Culture.Literature                           0.656
		Culture.Media.Books                          0.589
		Culture.Media.Entertainment                  0.462
		Culture.Media.Films                          0.771
		Culture.Media.Media*                         0.734
		Culture.Media.Music                          0.816
		Culture.Media.Radio                          0.796
		Culture.Media.Software                       0.198
		Culture.Media.Television                     0.692
		Culture.Media.Video games                    0.824
		Culture.Performing arts                      0.595
		Culture.Philosophy and religion              0.53
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.687
		Culture.Visual arts.Comics and Anime         0.62
		Culture.Visual arts.Fashion                  0.51
		Culture.Visual arts.Visual arts*             0.669
		Geography.Geographical                       0.7
		Geography.Regions.Africa.Africa*             0.668
		Geography.Regions.Africa.Central Africa      0.223
		Geography.Regions.Africa.Eastern Africa      0.569
		Geography.Regions.Africa.Northern Africa     0.507
		Geography.Regions.Africa.Southern Africa     0.584
		Geography.Regions.Africa.Western Africa      0.479
		Geography.Regions.Americas.Central America   0.707
		Geography.Regions.Americas.North America     0.691
		Geography.Regions.Americas.South America     0.727
		Geography.Regions.Asia.Asia*                 0.774
		Geography.Regions.Asia.Central Asia          0.619
		Geography.Regions.Asia.East Asia             0.699
		Geography.Regions.Asia.North Asia            0.255
		Geography.Regions.Asia.South Asia            0.861
		Geography.Regions.Asia.Southeast Asia        0.771
		Geography.Regions.Asia.West Asia             0.791
		Geography.Regions.Europe.Eastern Europe      0.704
		Geography.Regions.Europe.Europe*             0.691
		Geography.Regions.Europe.Northern Europe     0.675
		Geography.Regions.Europe.Southern Europe     0.688
		Geography.Regions.Europe.Western Europe      0.649
		Geography.Regions.Oceania                    0.821
		History and Society.Business and economics   0.412
		History and Society.Education                0.496
		History and Society.History                  0.416
		History and Society.Military and warfare     0.65
		History and Society.Politics and government  0.647
		History and Society.Society                  0.39
		History and Society.Transportation           0.819
		STEM.Biology                                 0.862
		STEM.Chemistry                               0.387
		STEM.Computing                               0.334
		STEM.Earth and environment                   0.669
		STEM.Engineering                             0.645
		STEM.Libraries & Information                 0.348
		STEM.Mathematics                             0.287
		STEM.Medicine & Health                       0.63
		STEM.Physics                                 0.297
		STEM.STEM*                                   0.808
		STEM.Space                                   0.865
		STEM.Technology                              0.346
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
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
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.988
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.986
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.981
		History and Society.Society                  0.985
		History and Society.Transportation           0.994
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.025
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
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
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.005
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.002
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
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.005
		History and Society.History                  0.008
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.007
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
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
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.979):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.984
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.981
		Culture.Literature                           0.979
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.974
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.989
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.98
		Culture.Philosophy and religion              0.97
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.987
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.986
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.986
		Geography.Regions.Africa.Northern Africa     0.983
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.988
		Geography.Regions.Americas.Central America   0.983
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.985
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.988
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.973
		Geography.Regions.Oceania                    0.982
		History and Society.Business and economics   0.957
		History and Society.Education                0.967
		History and Society.History                  0.951
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.963
		History and Society.Society                  0.929
		History and Society.Transportation           0.986
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.985
		STEM.Computing                               0.983
		STEM.Earth and environment                   0.981
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.977
		STEM.Mathematics                             0.985
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.977
		STEM.Space                                   0.991
		STEM.Technology                              0.972
		-------------------------------------------  -----
	pr_auc (micro=0.787, macro=0.649):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.921
		Culture.Biography.Women                      0.584
		Culture.Food and drink                       0.717
		Culture.Internet culture                     0.758
		Culture.Linguistics                          0.758
		Culture.Literature                           0.71
		Culture.Media.Books                          0.635
		Culture.Media.Entertainment                  0.469
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.839
		Culture.Media.Music                          0.883
		Culture.Media.Radio                          0.849
		Culture.Media.Software                       0.172
		Culture.Media.Television                     0.732
		Culture.Media.Video games                    0.903
		Culture.Performing arts                      0.578
		Culture.Philosophy and religion              0.517
		Culture.Sports                               0.957
		Culture.Visual arts.Architecture             0.753
		Culture.Visual arts.Comics and Anime         0.653
		Culture.Visual arts.Fashion                  0.552
		Culture.Visual arts.Visual arts*             0.74
		Geography.Geographical                       0.745
		Geography.Regions.Africa.Africa*             0.726
		Geography.Regions.Africa.Central Africa      0.166
		Geography.Regions.Africa.Eastern Africa      0.554
		Geography.Regions.Africa.Northern Africa     0.56
		Geography.Regions.Africa.Southern Africa     0.567
		Geography.Regions.Africa.Western Africa      0.512
		Geography.Regions.Americas.Central America   0.721
		Geography.Regions.Americas.North America     0.759
		Geography.Regions.Americas.South America     0.746
		Geography.Regions.Asia.Asia*                 0.83
		Geography.Regions.Asia.Central Asia          0.657
		Geography.Regions.Asia.East Asia             0.711
		Geography.Regions.Asia.North Asia            0.2
		Geography.Regions.Asia.South Asia            0.9
		Geography.Regions.Asia.Southeast Asia        0.786
		Geography.Regions.Asia.West Asia             0.846
		Geography.Regions.Europe.Eastern Europe      0.739
		Geography.Regions.Europe.Europe*             0.764
		Geography.Regions.Europe.Northern Europe     0.726
		Geography.Regions.Europe.Southern Europe     0.73
		Geography.Regions.Europe.Western Europe      0.667
		Geography.Regions.Oceania                    0.861
		History and Society.Business and economics   0.347
		History and Society.Education                0.418
		History and Society.History                  0.36
		History and Society.Military and warfare     0.698
		History and Society.Politics and government  0.705
		History and Society.Society                  0.356
		History and Society.Transportation           0.881
		STEM.Biology                                 0.925
		STEM.Chemistry                               0.421
		STEM.Computing                               0.307
		STEM.Earth and environment                   0.694
		STEM.Engineering                             0.681
		STEM.Libraries & Information                 0.302
		STEM.Mathematics                             0.35
		STEM.Medicine & Health                       0.677
		STEM.Physics                                 0.303
		STEM.STEM*                                   0.895
		STEM.Space                                   0.925
		STEM.Technology                              0.363
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

