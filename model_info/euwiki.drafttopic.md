Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'init': None, 'max_depth': 5, 'n_estimators': 150, 'center': False, 'scale': False, 'max_features': 'log2', 'warm_start': False, 'multilabel': True, 'population_rates': None, 'verbose': 0, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'n_iter_no_change': None, 'min_samples_leaf': 1, 'label_weights': {}, 'tol': 0.0001, 'ccp_alpha': 0.0, 'min_impurity_split': None, 'min_samples_split': 2, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'presort': 'deprecated', 'validation_fraction': 0.1, 'subsample': 1.0, 'learning_rate': 0.1, 'random_state': None, 'loss': 'deviance', 'criterion': 'friedman_mse', 'min_impurity_decrease': 0.0}
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
	counts (n=55032):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13966  -->  12326  1640   924  40142
			'Culture.Biography.Women'                       3325  -->   2170  1155   408  51299
			'Culture.Food and drink'                        1435  -->    997   438   139  53458
			'Culture.Internet culture'                      1993  -->   1657   336   184  52855
			'Culture.Linguistics'                           2092  -->   1375   717   179  52761
			'Culture.Literature'                            4605  -->   3267  1338   470  49957
			'Culture.Media.Books'                           1213  -->    927   286    84  53735
			'Culture.Media.Entertainment'                   1971  -->    905  1066   236  52825
			'Culture.Media.Films'                           3091  -->   2800   291    96  51845
			'Culture.Media.Media*'                         11162  -->   9535  1627  1085  42785
			'Culture.Media.Music'                           2662  -->   2168   494   153  52217
			'Culture.Media.Radio'                            207  -->    139    68    32  54793
			'Culture.Media.Software'                        1788  -->   1564   224   206  53038
			'Culture.Media.Television'                      1676  -->   1249   427    81  53275
			'Culture.Media.Video games'                      637  -->    603    34    27  54368
			'Culture.Performing arts'                       1548  -->    852   696   118  53366
			'Culture.Philosophy and religion'               3899  -->   2027  1872   364  50769
			'Culture.Sports'                                3696  -->   2935   761   118  51218
			'Culture.Visual arts.Architecture'              2448  -->   1775   673   256  52328
			'Culture.Visual arts.Comics and Anime'          1129  -->    944   185    59  53844
			'Culture.Visual arts.Fashion'                    596  -->    366   230    37  54399
			'Culture.Visual arts.Visual arts*'              4845  -->   3338  1507   448  49739
			'Geography.Geographical'                        4296  -->   2675  1621   723  50013
			'Geography.Regions.Africa.Africa*'              3722  -->   2288  1434   373  50937
			'Geography.Regions.Africa.Central Africa'        814  -->    504   310   109  54109
			'Geography.Regions.Africa.Eastern Africa'        330  -->    183   147    47  54655
			'Geography.Regions.Africa.Northern Africa'      1354  -->    815   539   118  53560
			'Geography.Regions.Africa.Southern Africa'       555  -->    329   226    53  54424
			'Geography.Regions.Africa.Western Africa'         61  -->     26    35    47  54924
			'Geography.Regions.Americas.Central America'    1403  -->    655   748   147  53482
			'Geography.Regions.Americas.North America'      6322  -->   4546  1776   717  47993
			'Geography.Regions.Americas.South America'      1751  -->   1269   482   109  53172
			'Geography.Regions.Asia.Asia*'                 10095  -->   7779  2316   892  44045
			'Geography.Regions.Asia.Central Asia'            683  -->    431   252    79  54270
			'Geography.Regions.Asia.East Asia'              3266  -->   2700   566   227  51539
			'Geography.Regions.Asia.North Asia'             2173  -->   1556   617   117  52742
			'Geography.Regions.Asia.South Asia'             1632  -->   1058   574   108  53292
			'Geography.Regions.Asia.Southeast Asia'         1645  -->    859   786   201  53186
			'Geography.Regions.Asia.West Asia'              2136  -->   1443   693   166  52730
			'Geography.Regions.Europe.Eastern Europe'       3672  -->   2832   840   162  51198
			'Geography.Regions.Europe.Europe*'             17266  -->  14329  2937  1976  35790
			'Geography.Regions.Europe.Northern Europe'      3987  -->   2989   998   300  50745
			'Geography.Regions.Europe.Southern Europe'      5480  -->   3997  1483   639  48913
			'Geography.Regions.Europe.Western Europe'       5036  -->   3881  1155   403  49593
			'Geography.Regions.Oceania'                     1945  -->   1143   802   189  52898
			'History and Society.Business and economics'    2938  -->   1657  1281   270  51824
			'History and Society.Education'                 1684  -->    764   920   128  53220
			'History and Society.History'                   5630  -->   3404  2226   676  48726
			'History and Society.Military and warfare'      3680  -->   2145  1535   403  50949
			'History and Society.Politics and government'   4501  -->   2272  2229   540  49991
			'History and Society.Society'                   5093  -->   1742  3351   435  49504
			'History and Society.Transportation'            2522  -->   2006   516   122  52388
			'STEM.Biology'                                  6818  -->   6191   627   143  48071
			'STEM.Chemistry'                                1507  -->   1139   368   126  53399
			'STEM.Computing'                                2282  -->   1885   397   203  52547
			'STEM.Earth and environment'                    1819  -->   1166   653   135  53078
			'STEM.Engineering'                              2443  -->   1659   784   167  52422
			'STEM.Libraries & Information'                   455  -->    345   110    32  54545
			'STEM.Mathematics'                              1017  -->    857   160    48  53967
			'STEM.Medicine & Health'                        1838  -->   1187   651   169  53025
			'STEM.Physics'                                  1500  -->   1013   487   164  53368
			'STEM.STEM*'                                   19466  -->  17587  1879   998  34568
			'STEM.Space'                                    1805  -->   1635   170    53  53174
			'STEM.Technology'                               4100  -->   2987  1113   563  50369
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.254         0.12
		Culture.Biography.Women                         0.06          0.015
		Culture.Food and drink                          0.026         0.003
		Culture.Internet culture                        0.036         0.004
		Culture.Linguistics                             0.038         0.008
		Culture.Literature                              0.084         0.015
		Culture.Media.Books                             0.022         0.004
		Culture.Media.Entertainment                     0.036         0.004
		Culture.Media.Films                             0.056         0.012
		Culture.Media.Media*                            0.203         0.055
		Culture.Media.Music                             0.048         0.021
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.03          0.009
		Culture.Media.Video games                       0.012         0.003
		Culture.Performing arts                         0.028         0.003
		Culture.Philosophy and religion                 0.071         0.01
		Culture.Sports                                  0.067         0.06
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.088         0.018
		Geography.Geographical                          0.078         0.021
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.01          0.001
		Geography.Regions.Africa.Western Africa         0.001         0.001
		Geography.Regions.Americas.Central America      0.025         0.003
		Geography.Regions.Americas.North America        0.115         0.063
		Geography.Regions.Americas.South America        0.032         0.007
		Geography.Regions.Asia.Asia*                    0.183         0.052
		Geography.Regions.Asia.Central Asia             0.012         0.001
		Geography.Regions.Asia.East Asia                0.059         0.012
		Geography.Regions.Asia.North Asia               0.039         0.006
		Geography.Regions.Asia.South Asia               0.03          0.016
		Geography.Regions.Asia.Southeast Asia           0.03          0.006
		Geography.Regions.Asia.West Asia                0.039         0.012
		Geography.Regions.Europe.Eastern Europe         0.067         0.018
		Geography.Regions.Europe.Europe*                0.314         0.081
		Geography.Regions.Europe.Northern Europe        0.072         0.029
		Geography.Regions.Europe.Southern Europe        0.1           0.014
		Geography.Regions.Europe.Western Europe         0.092         0.02
		Geography.Regions.Oceania                       0.035         0.016
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.031         0.008
		History and Society.History                     0.102         0.011
		History and Society.Military and warfare        0.067         0.015
		History and Society.Politics and government     0.082         0.028
		History and Society.Society                     0.093         0.008
		History and Society.Transportation              0.046         0.016
		STEM.Biology                                    0.124         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.033         0.005
		STEM.Engineering                                0.044         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.027         0.001
		STEM.STEM*                                      0.354         0.065
		STEM.Space                                      0.033         0.004
		STEM.Technology                                 0.075         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.009
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.07
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.05
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.027
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.059
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.059
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.115
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.02
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.024
		History and Society.Society                  0.011
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.085
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.991
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.93
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.941
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.885
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.98
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.989
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.915
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.761, macro=0.695):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.653
		Culture.Food and drink                       0.695
		Culture.Internet culture                     0.831
		Culture.Linguistics                          0.657
		Culture.Literature                           0.709
		Culture.Media.Books                          0.764
		Culture.Media.Entertainment                  0.459
		Culture.Media.Films                          0.906
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.814
		Culture.Media.Radio                          0.671
		Culture.Media.Software                       0.875
		Culture.Media.Television                     0.745
		Culture.Media.Video games                    0.947
		Culture.Performing arts                      0.55
		Culture.Philosophy and religion              0.52
		Culture.Sports                               0.794
		Culture.Visual arts.Architecture             0.725
		Culture.Visual arts.Comics and Anime         0.836
		Culture.Visual arts.Fashion                  0.614
		Culture.Visual arts.Visual arts*             0.689
		Geography.Geographical                       0.623
		Geography.Regions.Africa.Africa*             0.615
		Geography.Regions.Africa.Central Africa      0.619
		Geography.Regions.Africa.Eastern Africa      0.555
		Geography.Regions.Africa.Northern Africa     0.602
		Geography.Regions.Africa.Southern Africa     0.593
		Geography.Regions.Africa.Western Africa      0.426
		Geography.Regions.Americas.Central America   0.467
		Geography.Regions.Americas.North America     0.719
		Geography.Regions.Americas.South America     0.725
		Geography.Regions.Asia.Asia*                 0.771
		Geography.Regions.Asia.Central Asia          0.631
		Geography.Regions.Asia.East Asia             0.827
		Geography.Regions.Asia.North Asia            0.716
		Geography.Regions.Asia.South Asia            0.648
		Geography.Regions.Asia.Southeast Asia        0.522
		Geography.Regions.Asia.West Asia             0.676
		Geography.Regions.Europe.Eastern Europe      0.771
		Geography.Regions.Europe.Europe*             0.83
		Geography.Regions.Europe.Northern Europe     0.75
		Geography.Regions.Europe.Southern Europe     0.729
		Geography.Regions.Europe.Western Europe      0.771
		Geography.Regions.Oceania                    0.588
		History and Society.Business and economics   0.564
		History and Society.Education                0.454
		History and Society.History                  0.605
		History and Society.Military and warfare     0.583
		History and Society.Politics and government  0.505
		History and Society.Society                  0.342
		History and Society.Transportation           0.795
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.756
		STEM.Computing                               0.826
		STEM.Earth and environment                   0.641
		STEM.Engineering                             0.679
		STEM.Libraries & Information                 0.758
		STEM.Mathematics                             0.843
		STEM.Medicine & Health                       0.646
		STEM.Physics                                 0.675
		STEM.STEM*                                   0.903
		STEM.Space                                   0.906
		STEM.Technology                              0.729
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.693, macro=0.557):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.843
		Culture.Biography.Women                      0.556
		Culture.Food and drink                       0.406
		Culture.Internet culture                     0.472
		Culture.Linguistics                          0.611
		Culture.Literature                           0.534
		Culture.Media.Books                          0.679
		Culture.Media.Entertainment                  0.29
		Culture.Media.Films                          0.851
		Culture.Media.Media*                         0.667
		Culture.Media.Music                          0.856
		Culture.Media.Radio                          0.728
		Culture.Media.Software                       0.228
		Culture.Media.Television                     0.814
		Culture.Media.Video games                    0.847
		Culture.Performing arts                      0.433
		Culture.Philosophy and religion              0.433
		Culture.Sports                               0.957
		Culture.Visual arts.Architecture             0.619
		Culture.Visual arts.Comics and Anime         0.646
		Culture.Visual arts.Fashion                  0.447
		Culture.Visual arts.Visual arts*             0.586
		Geography.Geographical                       0.485
		Geography.Regions.Africa.Africa*             0.419
		Geography.Regions.Africa.Central Africa      0.178
		Geography.Regions.Africa.Eastern Africa      0.245
		Geography.Regions.Africa.Northern Africa     0.27
		Geography.Regions.Africa.Southern Africa     0.443
		Geography.Regions.Africa.Western Africa      0.271
		Geography.Regions.Americas.Central America   0.371
		Geography.Regions.Americas.North America     0.766
		Geography.Regions.Americas.South America     0.709
		Geography.Regions.Asia.Asia*                 0.682
		Geography.Regions.Asia.Central Asia          0.257
		Geography.Regions.Asia.East Asia             0.698
		Geography.Regions.Asia.North Asia            0.645
		Geography.Regions.Asia.South Asia            0.843
		Geography.Regions.Asia.Southeast Asia        0.465
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.82
		Geography.Regions.Europe.Europe*             0.582
		Geography.Regions.Europe.Northern Europe     0.792
		Geography.Regions.Europe.Southern Europe     0.441
		Geography.Regions.Europe.Western Europe      0.666
		Geography.Regions.Oceania                    0.733
		History and Society.Business and economics   0.516
		History and Society.Education                0.601
		History and Society.History                  0.327
		History and Society.Military and warfare     0.535
		History and Society.Politics and government  0.576
		History and Society.Society                  0.246
		History and Society.Transportation           0.85
		STEM.Biology                                 0.916
		STEM.Chemistry                               0.352
		STEM.Computing                               0.377
		STEM.Earth and environment                   0.545
		STEM.Engineering                             0.552
		STEM.Libraries & Information                 0.469
		STEM.Mathematics                             0.304
		STEM.Medicine & Health                       0.568
		STEM.Physics                                 0.171
		STEM.STEM*                                   0.691
		STEM.Space                                   0.795
		STEM.Technology                              0.254
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.986
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.718, macro=0.602):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.862
		Culture.Biography.Women                      0.601
		Culture.Food and drink                       0.512
		Culture.Internet culture                     0.602
		Culture.Linguistics                          0.633
		Culture.Literature                           0.609
		Culture.Media.Books                          0.719
		Culture.Media.Entertainment                  0.355
		Culture.Media.Films                          0.878
		Culture.Media.Media*                         0.749
		Culture.Media.Music                          0.835
		Culture.Media.Radio                          0.699
		Culture.Media.Software                       0.362
		Culture.Media.Television                     0.778
		Culture.Media.Video games                    0.894
		Culture.Performing arts                      0.484
		Culture.Philosophy and religion              0.472
		Culture.Sports                               0.868
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.729
		Culture.Visual arts.Fashion                  0.518
		Culture.Visual arts.Visual arts*             0.634
		Geography.Geographical                       0.545
		Geography.Regions.Africa.Africa*             0.499
		Geography.Regions.Africa.Central Africa      0.276
		Geography.Regions.Africa.Eastern Africa      0.339
		Geography.Regions.Africa.Northern Africa     0.373
		Geography.Regions.Africa.Southern Africa     0.507
		Geography.Regions.Africa.Western Africa      0.331
		Geography.Regions.Americas.Central America   0.413
		Geography.Regions.Americas.North America     0.742
		Geography.Regions.Americas.South America     0.717
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.365
		Geography.Regions.Asia.East Asia             0.757
		Geography.Regions.Asia.North Asia            0.679
		Geography.Regions.Asia.South Asia            0.733
		Geography.Regions.Asia.Southeast Asia        0.492
		Geography.Regions.Asia.West Asia             0.696
		Geography.Regions.Europe.Eastern Europe      0.795
		Geography.Regions.Europe.Europe*             0.684
		Geography.Regions.Europe.Northern Europe     0.77
		Geography.Regions.Europe.Southern Europe     0.55
		Geography.Regions.Europe.Western Europe      0.715
		Geography.Regions.Oceania                    0.652
		History and Society.Business and economics   0.539
		History and Society.Education                0.517
		History and Society.History                  0.424
		History and Society.Military and warfare     0.558
		History and Society.Politics and government  0.538
		History and Society.Society                  0.286
		History and Society.Transportation           0.822
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.48
		STEM.Computing                               0.518
		STEM.Earth and environment                   0.589
		STEM.Engineering                             0.609
		STEM.Libraries & Information                 0.58
		STEM.Mathematics                             0.447
		STEM.Medicine & Health                       0.604
		STEM.Physics                                 0.273
		STEM.STEM*                                   0.783
		STEM.Space                                   0.847
		STEM.Technology                              0.376
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.994
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.991
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.976
		History and Society.Society                  0.986
		History and Society.Transportation           0.994
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.023
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.003
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.025
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.014
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.052
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.011
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.004
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.971, macro=0.968):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.971
		Culture.Literature                           0.974
		Culture.Media.Books                          0.982
		Culture.Media.Entertainment                  0.966
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.933
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.985
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.947
		Culture.Sports                               0.973
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.975
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.962
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.939
		Geography.Regions.Africa.Northern Africa     0.973
		Geography.Regions.Africa.Southern Africa     0.96
		Geography.Regions.Africa.Western Africa      0.756
		Geography.Regions.Americas.Central America   0.962
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.977
		Geography.Regions.Asia.Asia*                 0.966
		Geography.Regions.Asia.Central Asia          0.975
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.971
		Geography.Regions.Asia.South Asia            0.972
		Geography.Regions.Asia.Southeast Asia        0.972
		Geography.Regions.Asia.West Asia             0.971
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.973
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.962
		History and Society.Education                0.962
		History and Society.History                  0.954
		History and Society.Military and warfare     0.967
		History and Society.Politics and government  0.943
		History and Society.Society                  0.913
		History and Society.Transportation           0.981
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.983
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.965
		STEM.Engineering                             0.974
		STEM.Libraries & Information                 0.963
		STEM.Mathematics                             0.986
		STEM.Medicine & Health                       0.971
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.977
		STEM.Space                                   0.99
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.766, macro=0.599):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.612
		Culture.Food and drink                       0.49
		Culture.Internet culture                     0.613
		Culture.Linguistics                          0.681
		Culture.Literature                           0.638
		Culture.Media.Books                          0.719
		Culture.Media.Entertainment                  0.297
		Culture.Media.Films                          0.903
		Culture.Media.Media*                         0.849
		Culture.Media.Music                          0.864
		Culture.Media.Radio                          0.461
		Culture.Media.Software                       0.367
		Culture.Media.Television                     0.8
		Culture.Media.Video games                    0.914
		Culture.Performing arts                      0.411
		Culture.Philosophy and religion              0.434
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.662
		Culture.Visual arts.Comics and Anime         0.772
		Culture.Visual arts.Fashion                  0.468
		Culture.Visual arts.Visual arts*             0.665
		Geography.Geographical                       0.548
		Geography.Regions.Africa.Africa*             0.479
		Geography.Regions.Africa.Central Africa      0.231
		Geography.Regions.Africa.Eastern Africa      0.156
		Geography.Regions.Africa.Northern Africa     0.272
		Geography.Regions.Africa.Southern Africa     0.34
		Geography.Regions.Africa.Western Africa      0.106
		Geography.Regions.Americas.Central America   0.345
		Geography.Regions.Americas.North America     0.823
		Geography.Regions.Americas.South America     0.764
		Geography.Regions.Asia.Asia*                 0.783
		Geography.Regions.Asia.Central Asia          0.256
		Geography.Regions.Asia.East Asia             0.771
		Geography.Regions.Asia.North Asia            0.65
		Geography.Regions.Asia.South Asia            0.761
		Geography.Regions.Asia.Southeast Asia        0.478
		Geography.Regions.Asia.West Asia             0.68
		Geography.Regions.Europe.Eastern Europe      0.818
		Geography.Regions.Europe.Europe*             0.796
		Geography.Regions.Europe.Northern Europe     0.829
		Geography.Regions.Europe.Southern Europe     0.604
		Geography.Regions.Europe.Western Europe      0.763
		Geography.Regions.Oceania                    0.706
		History and Society.Business and economics   0.499
		History and Society.Education                0.461
		History and Society.History                  0.428
		History and Society.Military and warfare     0.555
		History and Society.Politics and government  0.564
		History and Society.Society                  0.256
		History and Society.Transportation           0.871
		STEM.Biology                                 0.94
		STEM.Chemistry                               0.548
		STEM.Computing                               0.545
		STEM.Earth and environment                   0.559
		STEM.Engineering                             0.619
		STEM.Libraries & Information                 0.471
		STEM.Mathematics                             0.552
		STEM.Medicine & Health                       0.622
		STEM.Physics                                 0.208
		STEM.STEM*                                   0.89
		STEM.Space                                   0.9
		STEM.Technology                              0.39
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'properties': {'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

