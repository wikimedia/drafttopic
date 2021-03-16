Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.8'
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
	counts (n=62795):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 26992  -->  25506  1486  1007  34796
			'Culture.Biography.Women'                       6281  -->   4702  1579   954  55560
			'Culture.Food and drink'                        1344  -->    733   611   132  61319
			'Culture.Internet culture'                      3343  -->   2518   825   230  59222
			'Culture.Linguistics'                           1383  -->    751   632   107  61305
			'Culture.Literature'                            5742  -->   3804  1938   627  56426
			'Culture.Media.Books'                           1533  -->   1002   531   140  61122
			'Culture.Media.Entertainment'                   2093  -->    808  1285   214  60488
			'Culture.Media.Films'                           2108  -->   1563   545   142  60545
			'Culture.Media.Media*'                         13935  -->  11072  2863  1683  47177
			'Culture.Media.Music'                           2781  -->   1951   830   360  59654
			'Culture.Media.Radio'                           1131  -->    422   709    98  61566
			'Culture.Media.Software'                        2065  -->   1390   675   337  60393
			'Culture.Media.Television'                      2239  -->   1131  1108   220  60336
			'Culture.Media.Video games'                     2171  -->   1815   356    72  60552
			'Culture.Performing arts'                       1478  -->    589   889   139  61178
			'Culture.Philosophy and religion'               3372  -->   1324  2048   318  59105
			'Culture.Sports'                                8592  -->   7728   864   417  53786
			'Culture.Visual arts.Architecture'              1842  -->   1109   733   195  60758
			'Culture.Visual arts.Comics and Anime'          1830  -->   1265   565   139  60826
			'Culture.Visual arts.Fashion'                   1307  -->    807   500   104  61384
			'Culture.Visual arts.Visual arts*'              5819  -->   3754  2065   538  56438
			'Geography.Geographical'                        3599  -->   2444  1155   364  58832
			'Geography.Regions.Africa.Africa*'              6398  -->   4657  1741   517  55880
			'Geography.Regions.Africa.Central Africa'       1108  -->    699   409    66  61621
			'Geography.Regions.Africa.Eastern Africa'        959  -->    557   402    73  61763
			'Geography.Regions.Africa.Northern Africa'      2066  -->   1330   736   242  60487
			'Geography.Regions.Africa.Southern Africa'      1186  -->    836   350    74  61535
			'Geography.Regions.Africa.Western Africa'        752  -->    509   243    49  61994
			'Geography.Regions.Americas.Central America'    1364  -->    728   636    81  61350
			'Geography.Regions.Americas.North America'      8316  -->   5113  3203  2156  52323
			'Geography.Regions.Americas.South America'      1694  -->   1132   562   134  60967
			'Geography.Regions.Asia.Asia*'                 11871  -->   9264  2607  1055  49869
			'Geography.Regions.Asia.Central Asia'           1163  -->    751   412    91  61541
			'Geography.Regions.Asia.East Asia'              2887  -->   1931   956   264  59644
			'Geography.Regions.Asia.North Asia'             1493  -->    905   588   227  61075
			'Geography.Regions.Asia.South Asia'             1919  -->   1308   611    92  60784
			'Geography.Regions.Asia.Southeast Asia'         1539  -->    975   564    72  61184
			'Geography.Regions.Asia.West Asia'              4041  -->   3020  1021   335  58419
			'Geography.Regions.Europe.Eastern Europe'       2828  -->   1867   961   289  59678
			'Geography.Regions.Europe.Europe*'             13010  -->   9561  3449  2051  47734
			'Geography.Regions.Europe.Northern Europe'      4018  -->   2346  1672   626  58151
			'Geography.Regions.Europe.Southern Europe'      2834  -->   1788  1046   304  59657
			'Geography.Regions.Europe.Western Europe'       4060  -->   2751  1309   528  58207
			'Geography.Regions.Oceania'                     2280  -->   1706   574    83  60432
			'History and Society.Business and economics'    3538  -->   1718  1820   465  58792
			'History and Society.Education'                 2034  -->    698  1336   153  60608
			'History and Society.History'                   4654  -->   1762  2892   686  57455
			'History and Society.Military and warfare'      4697  -->   2914  1783   530  57568
			'History and Society.Politics and government'   5419  -->   2924  2495   651  56725
			'History and Society.Society'                   5993  -->   2120  3873   552  56250
			'History and Society.Transportation'            3223  -->   2601   622   192  59380
			'STEM.Biology'                                  2978  -->   2147   831   240  59577
			'STEM.Chemistry'                                1476  -->    961   515   172  61147
			'STEM.Computing'                                2392  -->   1612   780   385  60018
			'STEM.Earth and environment'                    1682  -->    874   808   174  60939
			'STEM.Engineering'                              2828  -->   1853   975   252  59715
			'STEM.Libraries & Information'                  1175  -->    739   436    86  61534
			'STEM.Mathematics'                              1163  -->    688   475    77  61555
			'STEM.Medicine & Health'                        2224  -->   1362   862   217  60354
			'STEM.Physics'                                  1432  -->    807   625   203  61160
			'STEM.STEM*'                                   17757  -->  14996  2761  1342  43696
			'STEM.Space'                                    1742  -->   1423   319    77  60976
			'STEM.Technology'                               4421  -->   2710  1711   674  57700
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.43          0.123
		Culture.Biography.Women                         0.1           0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.091         0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.034         0.011
		Culture.Media.Media*                            0.222         0.058
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.033         0.001
		Culture.Media.Television                        0.036         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.137         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.029         0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.102         0.008
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0
		Geography.Regions.Africa.Northern Africa        0.033         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.132         0.064
		Geography.Regions.Americas.South America        0.027         0.006
		Geography.Regions.Asia.Asia*                    0.189         0.045
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.046         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.064         0.011
		Geography.Regions.Europe.Eastern Europe         0.045         0.013
		Geography.Regions.Europe.Europe*                0.207         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.065         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.075         0.014
		History and Society.Politics and government     0.086         0.028
		History and Society.Society                     0.095         0.013
		History and Society.Transportation              0.051         0.015
		STEM.Biology                                    0.047         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.038         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.283         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.07          0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.141
		Culture.Biography.Women                      0.028
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.009
		Culture.Sports                               0.071
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.077
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.013
		History and Society.Education                0.005
		History and Society.History                  0.016
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.026
		History and Society.Society                  0.014
		History and Society.Transportation           0.015
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.086
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.859
		Culture.Biography.Women                      0.972
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.991
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.923
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.987
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.974
		History and Society.Society                  0.986
		History and Society.Transportation           0.985
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.914
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.726, macro=0.637):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.945
		Culture.Biography.Women                      0.749
		Culture.Food and drink                       0.545
		Culture.Internet culture                     0.753
		Culture.Linguistics                          0.543
		Culture.Literature                           0.662
		Culture.Media.Books                          0.654
		Culture.Media.Entertainment                  0.386
		Culture.Media.Films                          0.741
		Culture.Media.Media*                         0.795
		Culture.Media.Music                          0.702
		Culture.Media.Radio                          0.373
		Culture.Media.Software                       0.673
		Culture.Media.Television                     0.505
		Culture.Media.Video games                    0.836
		Culture.Performing arts                      0.399
		Culture.Philosophy and religion              0.393
		Culture.Sports                               0.899
		Culture.Visual arts.Architecture             0.602
		Culture.Visual arts.Comics and Anime         0.691
		Culture.Visual arts.Fashion                  0.617
		Culture.Visual arts.Visual arts*             0.645
		Geography.Geographical                       0.679
		Geography.Regions.Africa.Africa*             0.728
		Geography.Regions.Africa.Central Africa      0.631
		Geography.Regions.Africa.Eastern Africa      0.581
		Geography.Regions.Africa.Northern Africa     0.644
		Geography.Regions.Africa.Southern Africa     0.705
		Geography.Regions.Africa.Western Africa      0.677
		Geography.Regions.Americas.Central America   0.534
		Geography.Regions.Americas.North America     0.615
		Geography.Regions.Americas.South America     0.668
		Geography.Regions.Asia.Asia*                 0.78
		Geography.Regions.Asia.Central Asia          0.646
		Geography.Regions.Asia.East Asia             0.669
		Geography.Regions.Asia.North Asia            0.606
		Geography.Regions.Asia.South Asia            0.682
		Geography.Regions.Asia.Southeast Asia        0.634
		Geography.Regions.Asia.West Asia             0.747
		Geography.Regions.Europe.Eastern Europe      0.66
		Geography.Regions.Europe.Europe*             0.735
		Geography.Regions.Europe.Northern Europe     0.584
		Geography.Regions.Europe.Southern Europe     0.631
		Geography.Regions.Europe.Western Europe      0.678
		Geography.Regions.Oceania                    0.748
		History and Society.Business and economics   0.486
		History and Society.Education                0.343
		History and Society.History                  0.379
		History and Society.Military and warfare     0.62
		History and Society.Politics and government  0.54
		History and Society.Society                  0.354
		History and Society.Transportation           0.807
		STEM.Biology                                 0.721
		STEM.Chemistry                               0.651
		STEM.Computing                               0.674
		STEM.Earth and environment                   0.52
		STEM.Engineering                             0.655
		STEM.Libraries & Information                 0.629
		STEM.Mathematics                             0.592
		STEM.Medicine & Health                       0.612
		STEM.Physics                                 0.564
		STEM.STEM*                                   0.845
		STEM.Space                                   0.817
		STEM.Technology                              0.613
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.966
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.988
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
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
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.65, macro=0.497):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.825
		Culture.Biography.Women                      0.396
		Culture.Food and drink                       0.385
		Culture.Internet culture                     0.406
		Culture.Linguistics                          0.697
		Culture.Literature                           0.487
		Culture.Media.Books                          0.536
		Culture.Media.Entertainment                  0.282
		Culture.Media.Films                          0.771
		Culture.Media.Media*                         0.589
		Culture.Media.Music                          0.741
		Culture.Media.Radio                          0.336
		Culture.Media.Software                       0.139
		Culture.Media.Television                     0.553
		Culture.Media.Video games                    0.648
		Culture.Performing arts                      0.337
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.4
		Culture.Visual arts.Fashion                  0.228
		Culture.Visual arts.Visual arts*             0.56
		Geography.Geographical                       0.727
		Geography.Regions.Africa.Africa*             0.384
		Geography.Regions.Africa.Central Africa      0.271
		Geography.Regions.Africa.Eastern Africa      0.183
		Geography.Regions.Africa.Northern Africa     0.166
		Geography.Regions.Africa.Southern Africa     0.408
		Geography.Regions.Africa.Western Africa      0.369
		Geography.Regions.Americas.Central America   0.573
		Geography.Regions.Americas.North America     0.516
		Geography.Regions.Americas.South America     0.659
		Geography.Regions.Asia.Asia*                 0.642
		Geography.Regions.Asia.Central Asia          0.275
		Geography.Regions.Asia.East Asia             0.637
		Geography.Regions.Asia.North Asia            0.131
		Geography.Regions.Asia.South Asia            0.874
		Geography.Regions.Asia.Southeast Asia        0.765
		Geography.Regions.Asia.West Asia             0.591
		Geography.Regions.Europe.Eastern Europe      0.64
		Geography.Regions.Europe.Europe*             0.595
		Geography.Regions.Europe.Northern Europe     0.634
		Geography.Regions.Europe.Southern Europe     0.622
		Geography.Regions.Europe.Western Europe      0.596
		Geography.Regions.Oceania                    0.893
		History and Society.Business and economics   0.387
		History and Society.Education                0.502
		History and Society.History                  0.26
		History and Society.Military and warfare     0.492
		History and Society.Politics and government  0.58
		History and Society.Society                  0.317
		History and Society.Transportation           0.793
		STEM.Biology                                 0.862
		STEM.Chemistry                               0.266
		STEM.Computing                               0.222
		STEM.Earth and environment                   0.454
		STEM.Engineering                             0.451
		STEM.Libraries & Information                 0.219
		STEM.Mathematics                             0.165
		STEM.Medicine & Health                       0.524
		STEM.Physics                                 0.126
		STEM.STEM*                                   0.678
		STEM.Space                                   0.797
		STEM.Technology                              0.215
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.992
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.987
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.978
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.99
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
	f1 (micro=0.679, macro=0.536):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.881
		Culture.Biography.Women                      0.518
		Culture.Food and drink                       0.452
		Culture.Internet culture                     0.528
		Culture.Linguistics                          0.61
		Culture.Literature                           0.561
		Culture.Media.Books                          0.589
		Culture.Media.Entertainment                  0.326
		Culture.Media.Films                          0.756
		Culture.Media.Media*                         0.676
		Culture.Media.Music                          0.721
		Culture.Media.Radio                          0.354
		Culture.Media.Software                       0.23
		Culture.Media.Television                     0.528
		Culture.Media.Video games                    0.73
		Culture.Performing arts                      0.365
		Culture.Philosophy and religion              0.416
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.633
		Culture.Visual arts.Comics and Anime         0.507
		Culture.Visual arts.Fashion                  0.333
		Culture.Visual arts.Visual arts*             0.6
		Geography.Geographical                       0.702
		Geography.Regions.Africa.Africa*             0.503
		Geography.Regions.Africa.Central Africa      0.38
		Geography.Regions.Africa.Eastern Africa      0.278
		Geography.Regions.Africa.Northern Africa     0.263
		Geography.Regions.Africa.Southern Africa     0.517
		Geography.Regions.Africa.Western Africa      0.478
		Geography.Regions.Americas.Central America   0.552
		Geography.Regions.Americas.North America     0.561
		Geography.Regions.Americas.South America     0.664
		Geography.Regions.Asia.Asia*                 0.705
		Geography.Regions.Asia.Central Asia          0.386
		Geography.Regions.Asia.East Asia             0.652
		Geography.Regions.Asia.North Asia            0.216
		Geography.Regions.Asia.South Asia            0.766
		Geography.Regions.Asia.Southeast Asia        0.693
		Geography.Regions.Asia.West Asia             0.66
		Geography.Regions.Europe.Eastern Europe      0.65
		Geography.Regions.Europe.Europe*             0.658
		Geography.Regions.Europe.Northern Europe     0.608
		Geography.Regions.Europe.Southern Europe     0.626
		Geography.Regions.Europe.Western Europe      0.634
		Geography.Regions.Oceania                    0.814
		History and Society.Business and economics   0.431
		History and Society.Education                0.408
		History and Society.History                  0.308
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.559
		History and Society.Society                  0.335
		History and Society.Transportation           0.8
		STEM.Biology                                 0.785
		STEM.Chemistry                               0.378
		STEM.Computing                               0.334
		STEM.Earth and environment                   0.485
		STEM.Engineering                             0.534
		STEM.Libraries & Information                 0.325
		STEM.Mathematics                             0.258
		STEM.Medicine & Health                       0.565
		STEM.Physics                                 0.207
		STEM.STEM*                                   0.752
		STEM.Space                                   0.807
		STEM.Technology                              0.318
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.974, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.984
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.956
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.994
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.028
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.034
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.008
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.04
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.021
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.006
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.041
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.012
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.011
		History and Society.Society                  0.01
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
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.963, macro=0.963):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.962
		Culture.Internet culture                     0.978
		Culture.Linguistics                          0.951
		Culture.Literature                           0.962
		Culture.Media.Books                          0.971
		Culture.Media.Entertainment                  0.949
		Culture.Media.Films                          0.975
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.957
		Culture.Media.Software                       0.98
		Culture.Media.Television                     0.964
		Culture.Media.Video games                    0.987
		Culture.Performing arts                      0.954
		Culture.Philosophy and religion              0.917
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.976
		Culture.Visual arts.Fashion                  0.97
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.975
		Geography.Regions.Africa.Eastern Africa      0.964
		Geography.Regions.Africa.Northern Africa     0.97
		Geography.Regions.Africa.Southern Africa     0.969
		Geography.Regions.Africa.Western Africa      0.972
		Geography.Regions.Americas.Central America   0.955
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.971
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.97
		Geography.Regions.Asia.East Asia             0.969
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.965
		Geography.Regions.Asia.Southeast Asia        0.966
		Geography.Regions.Asia.West Asia             0.971
		Geography.Regions.Europe.Eastern Europe      0.969
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.955
		Geography.Regions.Europe.Southern Europe     0.964
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.968
		History and Society.Business and economics   0.941
		History and Society.Education                0.934
		History and Society.History                  0.923
		History and Society.Military and warfare     0.957
		History and Society.Politics and government  0.933
		History and Society.Society                  0.884
		History and Society.Transportation           0.976
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.981
		STEM.Computing                               0.979
		STEM.Earth and environment                   0.955
		STEM.Engineering                             0.967
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.966
		STEM.Medicine & Health                       0.963
		STEM.Physics                                 0.976
		STEM.STEM*                                   0.967
		STEM.Space                                   0.985
		STEM.Technology                              0.961
		-------------------------------------------  -----
	pr_auc (micro=0.705, macro=0.515):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.93
		Culture.Biography.Women                      0.489
		Culture.Food and drink                       0.354
		Culture.Internet culture                     0.631
		Culture.Linguistics                          0.548
		Culture.Literature                           0.629
		Culture.Media.Books                          0.58
		Culture.Media.Entertainment                  0.262
		Culture.Media.Films                          0.771
		Culture.Media.Media*                         0.771
		Culture.Media.Music                          0.74
		Culture.Media.Radio                          0.22
		Culture.Media.Software                       0.194
		Culture.Media.Television                     0.524
		Culture.Media.Video games                    0.814
		Culture.Performing arts                      0.288
		Culture.Philosophy and religion              0.329
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.635
		Culture.Visual arts.Comics and Anime         0.447
		Culture.Visual arts.Fashion                  0.231
		Culture.Visual arts.Visual arts*             0.606
		Geography.Geographical                       0.744
		Geography.Regions.Africa.Africa*             0.46
		Geography.Regions.Africa.Central Africa      0.284
		Geography.Regions.Africa.Eastern Africa      0.208
		Geography.Regions.Africa.Northern Africa     0.187
		Geography.Regions.Africa.Southern Africa     0.402
		Geography.Regions.Africa.Western Africa      0.314
		Geography.Regions.Americas.Central America   0.46
		Geography.Regions.Americas.North America     0.584
		Geography.Regions.Americas.South America     0.584
		Geography.Regions.Asia.Asia*                 0.779
		Geography.Regions.Asia.Central Asia          0.246
		Geography.Regions.Asia.East Asia             0.608
		Geography.Regions.Asia.North Asia            0.175
		Geography.Regions.Asia.South Asia            0.787
		Geography.Regions.Asia.Southeast Asia        0.676
		Geography.Regions.Asia.West Asia             0.697
		Geography.Regions.Europe.Eastern Europe      0.657
		Geography.Regions.Europe.Europe*             0.701
		Geography.Regions.Europe.Northern Europe     0.632
		Geography.Regions.Europe.Southern Europe     0.605
		Geography.Regions.Europe.Western Europe      0.632
		Geography.Regions.Oceania                    0.835
		History and Society.Business and economics   0.357
		History and Society.Education                0.36
		History and Society.History                  0.231
		History and Society.Military and warfare     0.577
		History and Society.Politics and government  0.583
		History and Society.Society                  0.267
		History and Society.Transportation           0.806
		STEM.Biology                                 0.81
		STEM.Chemistry                               0.404
		STEM.Computing                               0.267
		STEM.Earth and environment                   0.411
		STEM.Engineering                             0.516
		STEM.Libraries & Information                 0.319
		STEM.Mathematics                             0.235
		STEM.Medicine & Health                       0.532
		STEM.Physics                                 0.158
		STEM.STEM*                                   0.855
		STEM.Space                                   0.837
		STEM.Technology                              0.297
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

