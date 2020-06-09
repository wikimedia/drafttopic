Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'max_features': 'log2', 'validation_fraction': 0.1, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'verbose': 0, 'min_samples_leaf': 1, 'min_impurity_split': None, 'population_rates': None, 'label_weights': {}, 'init': None, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'n_iter_no_change': None, 'subsample': 1.0, 'min_impurity_decrease': 0.0, 'max_depth': 5, 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'loss': 'deviance', 'presort': 'deprecated', 'tol': 0.0001, 'max_leaf_nodes': None, 'ccp_alpha': 0.0, 'multilabel': True, 'center': False, 'n_estimators': 150, 'learning_rate': 0.1}
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
	counts (n=60196):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16632  -->  15348  1284   807  42757
			'Culture.Biography.Women'                       4316  -->   3709   607   317  55563
			'Culture.Food and drink'                        1626  -->   1356   270    84  58486
			'Culture.Internet culture'                      3193  -->   2785   408   174  56829
			'Culture.Linguistics'                           1619  -->   1276   343    86  58491
			'Culture.Literature'                            5022  -->   3878  1144   446  54728
			'Culture.Media.Books'                           1689  -->   1405   284    96  58411
			'Culture.Media.Entertainment'                   2324  -->   1392   932   219  57653
			'Culture.Media.Films'                           2572  -->   2138   434   103  57521
			'Culture.Media.Media*'                         14411  -->  12910  1501  1221  44564
			'Culture.Media.Music'                           3408  -->   3011   397   282  56506
			'Culture.Media.Radio'                            434  -->    255   179    42  59720
			'Culture.Media.Software'                        2325  -->   1931   394   274  57597
			'Culture.Media.Television'                      2526  -->   2139   387   115  57555
			'Culture.Media.Video games'                     1915  -->   1787   128    39  58242
			'Culture.Performing arts'                       1529  -->   1119   410   112  58555
			'Culture.Philosophy and religion'               4392  -->   2700  1692   433  55371
			'Culture.Sports'                                5921  -->   5322   599   215  54060
			'Culture.Visual arts.Architecture'              2290  -->   1813   477   215  57691
			'Culture.Visual arts.Comics and Anime'          1636  -->   1458   178    38  58522
			'Culture.Visual arts.Fashion'                   1066  -->    834   232    54  59076
			'Culture.Visual arts.Visual arts*'              5861  -->   4674  1187   388  53947
			'Geography.Geographical'                        4531  -->   3354  1177   688  54977
			'Geography.Regions.Africa.Africa*'              4135  -->   2972  1163   289  55772
			'Geography.Regions.Africa.Central Africa'        741  -->    352   389    81  59374
			'Geography.Regions.Africa.Eastern Africa'        472  -->    331   141    56  59668
			'Geography.Regions.Africa.Northern Africa'      1564  -->   1071   493    98  58534
			'Geography.Regions.Africa.Southern Africa'       690  -->    428   262    36  59470
			'Geography.Regions.Africa.Western Africa'        196  -->    102    94    52  59948
			'Geography.Regions.Americas.Central America'    1341  -->    884   457    58  58797
			'Geography.Regions.Americas.North America'      6188  -->   3949  2239   910  53098
			'Geography.Regions.Americas.South America'      1503  -->   1061   442    76  58617
			'Geography.Regions.Asia.Asia*'                 10746  -->   8679  2067   818  48632
			'Geography.Regions.Asia.Central Asia'           1312  -->    962   350    89  58795
			'Geography.Regions.Asia.East Asia'              2951  -->   2289   662   161  57084
			'Geography.Regions.Asia.North Asia'             1928  -->   1368   560   250  58018
			'Geography.Regions.Asia.South Asia'             1822  -->   1393   429    72  58302
			'Geography.Regions.Asia.Southeast Asia'         1639  -->   1164   475    66  58491
			'Geography.Regions.Asia.West Asia'              2828  -->   2220   608   189  57179
			'Geography.Regions.Europe.Eastern Europe'       5236  -->   3866  1370   646  54314
			'Geography.Regions.Europe.Europe*'             16902  -->  13499  3403  2474  40820
			'Geography.Regions.Europe.Northern Europe'      3994  -->   2596  1398   430  55772
			'Geography.Regions.Europe.Southern Europe'      3547  -->   2465  1082   287  56362
			'Geography.Regions.Europe.Western Europe'       5139  -->   3661  1478   611  54446
			'Geography.Regions.Oceania'                     1825  -->   1263   562    69  58302
			'History and Society.Business and economics'    3620  -->   2293  1327   355  56221
			'History and Society.Education'                 1763  -->   1074   689   115  58318
			'History and Society.History'                   5548  -->   3603  1945   655  53993
			'History and Society.Military and warfare'      5782  -->   4282  1500   545  53869
			'History and Society.Politics and government'   4677  -->   2700  1977   499  55020
			'History and Society.Society'                   6769  -->   3468  3301   670  52757
			'History and Society.Transportation'            4305  -->   3964   341   158  55733
			'STEM.Biology'                                  3876  -->   3276   600   171  56149
			'STEM.Chemistry'                                1571  -->   1351   220   106  58519
			'STEM.Computing'                                2761  -->   2397   364   310  57125
			'STEM.Earth and environment'                    2179  -->   1655   524   147  57870
			'STEM.Engineering'                              2932  -->   2380   552   203  57061
			'STEM.Libraries & Information'                   759  -->    551   208    55  59382
			'STEM.Mathematics'                              1197  -->   1046   151    43  58956
			'STEM.Medicine & Health'                        2020  -->   1525   495   166  58010
			'STEM.Physics'                                  1502  -->   1178   324   144  58550
			'STEM.STEM*'                                   18964  -->  17045  1919   924  40308
			'STEM.Space'                                    2095  -->   1982   113    50  58051
			'STEM.Technology'                               5167  -->   4022  1145   612  54417
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.276         0.123
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.027         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.043         0.011
		Culture.Media.Media*                            0.239         0.058
		Culture.Media.Music                             0.057         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.098         0.071
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.097         0.018
		Geography.Geographical                          0.075         0.024
		Geography.Regions.Africa.Africa*                0.069         0.008
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.103         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.179         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.049         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.047         0.011
		Geography.Regions.Europe.Eastern Europe         0.087         0.013
		Geography.Regions.Europe.Europe*                0.281         0.076
		Geography.Regions.Europe.Northern Europe        0.066         0.031
		Geography.Regions.Europe.Southern Europe        0.059         0.013
		Geography.Regions.Europe.Western Europe         0.085         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.06          0.01
		History and Society.Education                   0.029         0.007
		History and Society.History                     0.092         0.011
		History and Society.Military and warfare        0.096         0.014
		History and Society.Politics and government     0.078         0.028
		History and Society.Society                     0.112         0.013
		History and Society.Transportation              0.072         0.015
		STEM.Biology                                    0.064         0.034
		STEM.Chemistry                                  0.026         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.036         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.013         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.315         0.069
		STEM.Space                                      0.035         0.006
		STEM.Technology                                 0.086         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.026
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.03
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.057
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.114
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.02
		History and Society.Politics and government  0.025
		History and Society.Society                  0.019
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.007
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.943
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.886
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.975
		History and Society.Society                  0.981
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.993
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.798, macro=0.756):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.923
		Culture.Biography.Women                      0.859
		Culture.Food and drink                       0.834
		Culture.Internet culture                     0.872
		Culture.Linguistics                          0.788
		Culture.Literature                           0.772
		Culture.Media.Books                          0.832
		Culture.Media.Entertainment                  0.599
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.896
		Culture.Media.Music                          0.884
		Culture.Media.Radio                          0.588
		Culture.Media.Software                       0.831
		Culture.Media.Television                     0.847
		Culture.Media.Video games                    0.933
		Culture.Performing arts                      0.732
		Culture.Philosophy and religion              0.615
		Culture.Sports                               0.899
		Culture.Visual arts.Architecture             0.792
		Culture.Visual arts.Comics and Anime         0.891
		Culture.Visual arts.Fashion                  0.782
		Culture.Visual arts.Visual arts*             0.797
		Geography.Geographical                       0.74
		Geography.Regions.Africa.Africa*             0.719
		Geography.Regions.Africa.Central Africa      0.475
		Geography.Regions.Africa.Eastern Africa      0.701
		Geography.Regions.Africa.Northern Africa     0.685
		Geography.Regions.Africa.Southern Africa     0.62
		Geography.Regions.Africa.Western Africa      0.52
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.638
		Geography.Regions.Americas.South America     0.706
		Geography.Regions.Asia.Asia*                 0.808
		Geography.Regions.Asia.Central Asia          0.733
		Geography.Regions.Asia.East Asia             0.776
		Geography.Regions.Asia.North Asia            0.71
		Geography.Regions.Asia.South Asia            0.765
		Geography.Regions.Asia.Southeast Asia        0.71
		Geography.Regions.Asia.West Asia             0.785
		Geography.Regions.Europe.Eastern Europe      0.738
		Geography.Regions.Europe.Europe*             0.799
		Geography.Regions.Europe.Northern Europe     0.65
		Geography.Regions.Europe.Southern Europe     0.695
		Geography.Regions.Europe.Western Europe      0.712
		Geography.Regions.Oceania                    0.692
		History and Society.Business and economics   0.633
		History and Society.Education                0.609
		History and Society.History                  0.649
		History and Society.Military and warfare     0.741
		History and Society.Politics and government  0.577
		History and Society.Society                  0.512
		History and Society.Transportation           0.921
		STEM.Biology                                 0.845
		STEM.Chemistry                               0.86
		STEM.Computing                               0.868
		STEM.Earth and environment                   0.76
		STEM.Engineering                             0.812
		STEM.Libraries & Information                 0.726
		STEM.Mathematics                             0.874
		STEM.Medicine & Health                       0.755
		STEM.Physics                                 0.784
		STEM.STEM*                                   0.899
		STEM.Space                                   0.946
		STEM.Technology                              0.778
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.943
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.991
		History and Society.Society                  0.987
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.713, macro=0.584):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.691
		Culture.Food and drink                       0.589
		Culture.Internet culture                     0.501
		Culture.Linguistics                          0.798
		Culture.Literature                           0.601
		Culture.Media.Books                          0.672
		Culture.Media.Entertainment                  0.363
		Culture.Media.Films                          0.832
		Culture.Media.Media*                         0.676
		Culture.Media.Music                          0.813
		Culture.Media.Radio                          0.644
		Culture.Media.Software                       0.189
		Culture.Media.Television                     0.791
		Culture.Media.Video games                    0.785
		Culture.Performing arts                      0.526
		Culture.Philosophy and religion              0.46
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.751
		Culture.Visual arts.Fashion                  0.409
		Culture.Visual arts.Visual arts*             0.675
		Geography.Geographical                       0.591
		Geography.Regions.Africa.Africa*             0.523
		Geography.Regions.Africa.Central Africa      0.181
		Geography.Regions.Africa.Eastern Africa      0.254
		Geography.Regions.Africa.Northern Africa     0.335
		Geography.Regions.Africa.Southern Africa     0.547
		Geography.Regions.Africa.Western Africa      0.291
		Geography.Regions.Americas.Central America   0.689
		Geography.Regions.Americas.North America     0.722
		Geography.Regions.Americas.South America     0.776
		Geography.Regions.Asia.Asia*                 0.699
		Geography.Regions.Asia.Central Asia          0.296
		Geography.Regions.Asia.East Asia             0.761
		Geography.Regions.Asia.North Asia            0.133
		Geography.Regions.Asia.South Asia            0.905
		Geography.Regions.Asia.Southeast Asia        0.792
		Geography.Regions.Asia.West Asia             0.724
		Geography.Regions.Europe.Eastern Europe      0.449
		Geography.Regions.Europe.Europe*             0.535
		Geography.Regions.Europe.Northern Europe     0.728
		Geography.Regions.Europe.Southern Europe     0.644
		Geography.Regions.Europe.Western Europe      0.556
		Geography.Regions.Oceania                    0.9
		History and Society.Business and economics   0.507
		History and Society.Education                0.696
		History and Society.History                  0.372
		History and Society.Military and warfare     0.513
		History and Society.Politics and government  0.651
		History and Society.Society                  0.343
		History and Society.Transportation           0.833
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.426
		STEM.Computing                               0.303
		STEM.Earth and environment                   0.577
		STEM.Engineering                             0.546
		STEM.Libraries & Information                 0.328
		STEM.Mathematics                             0.333
		STEM.Medicine & Health                       0.63
		STEM.Physics                                 0.214
		STEM.STEM*                                   0.749
		STEM.Space                                   0.869
		STEM.Technology                              0.265
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.998
		Culture.Food and drink                       1
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.994
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
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.995
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
	f1 (micro=0.746, macro=0.639):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.766
		Culture.Food and drink                       0.691
		Culture.Internet culture                     0.636
		Culture.Linguistics                          0.793
		Culture.Literature                           0.676
		Culture.Media.Books                          0.743
		Culture.Media.Entertainment                  0.452
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.771
		Culture.Media.Music                          0.847
		Culture.Media.Radio                          0.614
		Culture.Media.Software                       0.308
		Culture.Media.Television                     0.818
		Culture.Media.Video games                    0.853
		Culture.Performing arts                      0.612
		Culture.Philosophy and religion              0.526
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.74
		Culture.Visual arts.Comics and Anime         0.815
		Culture.Visual arts.Fashion                  0.538
		Culture.Visual arts.Visual arts*             0.731
		Geography.Geographical                       0.657
		Geography.Regions.Africa.Africa*             0.605
		Geography.Regions.Africa.Central Africa      0.262
		Geography.Regions.Africa.Eastern Africa      0.373
		Geography.Regions.Africa.Northern Africa     0.45
		Geography.Regions.Africa.Southern Africa     0.581
		Geography.Regions.Africa.Western Africa      0.373
		Geography.Regions.Americas.Central America   0.674
		Geography.Regions.Americas.North America     0.678
		Geography.Regions.Americas.South America     0.739
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.422
		Geography.Regions.Asia.East Asia             0.768
		Geography.Regions.Asia.North Asia            0.223
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.749
		Geography.Regions.Asia.West Asia             0.753
		Geography.Regions.Europe.Eastern Europe      0.559
		Geography.Regions.Europe.Europe*             0.641
		Geography.Regions.Europe.Northern Europe     0.687
		Geography.Regions.Europe.Southern Europe     0.669
		Geography.Regions.Europe.Western Europe      0.625
		Geography.Regions.Oceania                    0.782
		History and Society.Business and economics   0.563
		History and Society.Education                0.65
		History and Society.History                  0.473
		History and Society.Military and warfare     0.606
		History and Society.Politics and government  0.612
		History and Society.Society                  0.411
		History and Society.Transportation           0.875
		STEM.Biology                                 0.875
		STEM.Chemistry                               0.57
		STEM.Computing                               0.449
		STEM.Earth and environment                   0.656
		STEM.Engineering                             0.653
		STEM.Libraries & Information                 0.452
		STEM.Mathematics                             0.483
		STEM.Medicine & Health                       0.687
		STEM.Physics                                 0.336
		STEM.STEM*                                   0.817
		STEM.Space                                   0.906
		STEM.Technology                              0.396
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.012
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.057
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.009
		History and Society.Society                  0.013
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.988
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.981
		Culture.Literature                           0.978
		Culture.Media.Books                          0.987
		Culture.Media.Entertainment                  0.978
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.962
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.988
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.986
		Culture.Philosophy and religion              0.964
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.989
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.98
		Geography.Regions.Africa.Central Africa      0.976
		Geography.Regions.Africa.Eastern Africa      0.975
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.974
		Geography.Regions.Africa.Western Africa      0.912
		Geography.Regions.Americas.Central America   0.98
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.984
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.982
		Geography.Regions.Asia.Southeast Asia        0.979
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.953
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.972
		History and Society.Education                0.975
		History and Society.History                  0.964
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.96
		History and Society.Society                  0.938
		History and Society.Transportation           0.988
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.986
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.983
		STEM.Engineering                             0.984
		STEM.Libraries & Information                 0.971
		STEM.Mathematics                             0.989
		STEM.Medicine & Health                       0.982
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.979
		STEM.Space                                   0.994
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.798, macro=0.663):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.948
		Culture.Biography.Women                      0.799
		Culture.Food and drink                       0.733
		Culture.Internet culture                     0.778
		Culture.Linguistics                          0.798
		Culture.Literature                           0.738
		Culture.Media.Books                          0.813
		Culture.Media.Entertainment                  0.425
		Culture.Media.Films                          0.867
		Culture.Media.Media*                         0.878
		Culture.Media.Music                          0.89
		Culture.Media.Radio                          0.461
		Culture.Media.Software                       0.301
		Culture.Media.Television                     0.869
		Culture.Media.Video games                    0.93
		Culture.Performing arts                      0.695
		Culture.Philosophy and religion              0.565
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.774
		Culture.Visual arts.Comics and Anime         0.882
		Culture.Visual arts.Fashion                  0.587
		Culture.Visual arts.Visual arts*             0.798
		Geography.Geographical                       0.675
		Geography.Regions.Africa.Africa*             0.615
		Geography.Regions.Africa.Central Africa      0.162
		Geography.Regions.Africa.Eastern Africa      0.246
		Geography.Regions.Africa.Northern Africa     0.368
		Geography.Regions.Africa.Southern Africa     0.538
		Geography.Regions.Africa.Western Africa      0.185
		Geography.Regions.Americas.Central America   0.676
		Geography.Regions.Americas.North America     0.73
		Geography.Regions.Americas.South America     0.777
		Geography.Regions.Asia.Asia*                 0.824
		Geography.Regions.Asia.Central Asia          0.343
		Geography.Regions.Asia.East Asia             0.802
		Geography.Regions.Asia.North Asia            0.166
		Geography.Regions.Asia.South Asia            0.878
		Geography.Regions.Asia.Southeast Asia        0.772
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.612
		Geography.Regions.Europe.Europe*             0.713
		Geography.Regions.Europe.Northern Europe     0.739
		Geography.Regions.Europe.Southern Europe     0.674
		Geography.Regions.Europe.Western Europe      0.639
		Geography.Regions.Oceania                    0.838
		History and Society.Business and economics   0.591
		History and Society.Education                0.643
		History and Society.History                  0.48
		History and Society.Military and warfare     0.686
		History and Society.Politics and government  0.638
		History and Society.Society                  0.384
		History and Society.Transportation           0.943
		STEM.Biology                                 0.933
		STEM.Chemistry                               0.6
		STEM.Computing                               0.533
		STEM.Earth and environment                   0.697
		STEM.Engineering                             0.685
		STEM.Libraries & Information                 0.304
		STEM.Mathematics                             0.573
		STEM.Medicine & Health                       0.749
		STEM.Physics                                 0.319
		STEM.STEM*                                   0.917
		STEM.Space                                   0.947
		STEM.Technology                              0.561
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'properties': {'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

