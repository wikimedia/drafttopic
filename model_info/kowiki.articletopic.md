Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'max_depth': 5, 'scale': False, 'center': False, 'tol': 0.0001, 'min_impurity_decrease': 0.0, 'ccp_alpha': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'max_features': 'log2', 'subsample': 1.0, 'min_impurity_split': None, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'presort': 'deprecated', 'n_iter_no_change': None, 'init': None, 'validation_fraction': 0.1, 'population_rates': None, 'min_samples_split': 2, 'criterion': 'friedman_mse', 'n_estimators': 150, 'random_state': None, 'learning_rate': 0.1, 'min_samples_leaf': 1, 'verbose': 0, 'max_leaf_nodes': None, 'label_weights': {}, 'warm_start': False}
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
	counts (n=60728):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15814  -->  14156  1658   842  44072
			'Culture.Biography.Women'                       4488  -->   3379  1109   443  55797
			'Culture.Food and drink'                        1771  -->   1433   338    81  58876
			'Culture.Internet culture'                      3426  -->   2802   624   233  57069
			'Culture.Linguistics'                           1697  -->   1270   427    83  58948
			'Culture.Literature'                            5934  -->   4610  1324   429  54365
			'Culture.Media.Books'                           1642  -->   1287   355    96  58990
			'Culture.Media.Entertainment'                   2396  -->   1361  1035   223  58109
			'Culture.Media.Films'                           2946  -->   2497   449   115  57667
			'Culture.Media.Media*'                         15170  -->  13288  1882  1452  44106
			'Culture.Media.Music'                           3287  -->   2675   612   281  57160
			'Culture.Media.Radio'                            675  -->    431   244    45  60008
			'Culture.Media.Software'                        2336  -->   1933   403   309  58083
			'Culture.Media.Television'                      2441  -->   1743   698   122  58165
			'Culture.Media.Video games'                     2290  -->   2051   239    71  58367
			'Culture.Performing arts'                       1528  -->    958   570   146  59054
			'Culture.Philosophy and religion'               3925  -->   2258  1667   286  56517
			'Culture.Sports'                                5172  -->   4538   634   182  55374
			'Culture.Visual arts.Architecture'              2077  -->   1476   601   208  58443
			'Culture.Visual arts.Comics and Anime'          2513  -->   2183   330   132  58083
			'Culture.Visual arts.Fashion'                   1352  -->   1027   325    75  59301
			'Culture.Visual arts.Visual arts*'              6445  -->   4859  1586   491  53792
			'Geography.Geographical'                        3895  -->   2619  1276   565  56268
			'Geography.Regions.Africa.Africa*'              4280  -->   3261  1019   281  56167
			'Geography.Regions.Africa.Central Africa'        831  -->    445   386    88  59809
			'Geography.Regions.Africa.Eastern Africa'        474  -->    346   128    37  60217
			'Geography.Regions.Africa.Northern Africa'      1551  -->   1205   346   103  59074
			'Geography.Regions.Africa.Southern Africa'       686  -->    512   174    44  59998
			'Geography.Regions.Africa.Western Africa'        288  -->    205    83    50  60390
			'Geography.Regions.Americas.Central America'    1360  -->    932   428    69  59299
			'Geography.Regions.Americas.North America'      6654  -->   4368  2286   962  53112
			'Geography.Regions.Americas.South America'      1568  -->   1169   399   106  59054
			'Geography.Regions.Asia.Asia*'                 14925  -->  12485  2440  1399  44404
			'Geography.Regions.Asia.Central Asia'           1369  -->   1076   293    79  59280
			'Geography.Regions.Asia.East Asia'              7365  -->   5944  1421   709  52654
			'Geography.Regions.Asia.North Asia'             1843  -->   1395   448   194  58691
			'Geography.Regions.Asia.South Asia'             1890  -->   1457   433    62  58776
			'Geography.Regions.Asia.Southeast Asia'         1926  -->   1471   455    83  58719
			'Geography.Regions.Asia.West Asia'              2398  -->   1825   573   124  58206
			'Geography.Regions.Europe.Eastern Europe'       3411  -->   2622   789   280  57037
			'Geography.Regions.Europe.Europe*'             13335  -->  10666  2669  1545  45848
			'Geography.Regions.Europe.Northern Europe'      3848  -->   2701  1147   327  56553
			'Geography.Regions.Europe.Southern Europe'      3336  -->   2438   898   274  57118
			'Geography.Regions.Europe.Western Europe'       4003  -->   2990  1013   386  56339
			'Geography.Regions.Oceania'                     1775  -->   1311   464    57  58896
			'History and Society.Business and economics'    3890  -->   2407  1483   365  56473
			'History and Society.Education'                 1966  -->   1256   710   104  58658
			'History and Society.History'                   5586  -->   3422  2164   540  54602
			'History and Society.Military and warfare'      5188  -->   3620  1568   408  55132
			'History and Society.Politics and government'   5154  -->   3059  2095   491  55083
			'History and Society.Society'                   6736  -->   3066  3670   511  53481
			'History and Society.Transportation'            3819  -->   3425   394   175  56734
			'STEM.Biology'                                  3485  -->   2850   635   154  57089
			'STEM.Chemistry'                                1540  -->   1262   278   108  59080
			'STEM.Computing'                                2804  -->   2333   471   364  57560
			'STEM.Earth and environment'                    1920  -->   1368   552   124  58684
			'STEM.Engineering'                              2759  -->   2135   624   190  57779
			'STEM.Libraries & Information'                   766  -->    552   214    41  59921
			'STEM.Mathematics'                              1191  -->    992   199    61  59476
			'STEM.Medicine & Health'                        2006  -->   1465   541   130  58592
			'STEM.Physics'                                  1520  -->   1207   313   159  59049
			'STEM.STEM*'                                   17913  -->  15901  2012   934  41881
			'STEM.Space'                                    1703  -->   1561   142    32  58993
			'STEM.Technology'                               4720  -->   3594  1126   581  55427
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.26          0.123
		Culture.Biography.Women                         0.074         0.015
		Culture.Food and drink                          0.029         0.002
		Culture.Internet culture                        0.056         0.003
		Culture.Linguistics                             0.028         0.007
		Culture.Literature                              0.098         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.25          0.058
		Culture.Media.Music                             0.054         0.024
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.04          0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.065         0.011
		Culture.Sports                                  0.085         0.071
		Culture.Visual arts.Architecture                0.034         0.011
		Culture.Visual arts.Comics and Anime            0.041         0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.106         0.018
		Geography.Geographical                          0.064         0.024
		Geography.Regions.Africa.Africa*                0.07          0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.11          0.064
		Geography.Regions.Americas.South America        0.026         0.006
		Geography.Regions.Asia.Asia*                    0.246         0.045
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.121         0.011
		Geography.Regions.Asia.North Asia               0.03          0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.039         0.011
		Geography.Regions.Europe.Eastern Europe         0.056         0.013
		Geography.Regions.Europe.Europe*                0.22          0.076
		Geography.Regions.Europe.Northern Europe        0.063         0.031
		Geography.Regions.Europe.Southern Europe        0.055         0.013
		Geography.Regions.Europe.Western Europe         0.066         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.092         0.011
		History and Society.Military and warfare        0.085         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.111         0.013
		History and Society.Transportation              0.063         0.015
		STEM.Biology                                    0.057         0.034
		STEM.Chemistry                                  0.025         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.032         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.013         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.033         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.295         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.066
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.026
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.059
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.067
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.022
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.091
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.025
		History and Society.Society                  0.015
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.003
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.934
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.933
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.909
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.975
		History and Society.Society                  0.985
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.787, macro=0.751):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.753
		Culture.Food and drink                       0.809
		Culture.Internet culture                     0.818
		Culture.Linguistics                          0.748
		Culture.Literature                           0.777
		Culture.Media.Books                          0.784
		Culture.Media.Entertainment                  0.568
		Culture.Media.Films                          0.848
		Culture.Media.Media*                         0.876
		Culture.Media.Music                          0.814
		Culture.Media.Radio                          0.639
		Culture.Media.Software                       0.827
		Culture.Media.Television                     0.714
		Culture.Media.Video games                    0.896
		Culture.Performing arts                      0.627
		Culture.Philosophy and religion              0.575
		Culture.Sports                               0.877
		Culture.Visual arts.Architecture             0.711
		Culture.Visual arts.Comics and Anime         0.869
		Culture.Visual arts.Fashion                  0.76
		Culture.Visual arts.Visual arts*             0.754
		Geography.Geographical                       0.672
		Geography.Regions.Africa.Africa*             0.762
		Geography.Regions.Africa.Central Africa      0.535
		Geography.Regions.Africa.Eastern Africa      0.73
		Geography.Regions.Africa.Northern Africa     0.777
		Geography.Regions.Africa.Southern Africa     0.746
		Geography.Regions.Africa.Western Africa      0.712
		Geography.Regions.Americas.Central America   0.685
		Geography.Regions.Americas.North America     0.656
		Geography.Regions.Americas.South America     0.746
		Geography.Regions.Asia.Asia*                 0.837
		Geography.Regions.Asia.Central Asia          0.786
		Geography.Regions.Asia.East Asia             0.807
		Geography.Regions.Asia.North Asia            0.757
		Geography.Regions.Asia.South Asia            0.771
		Geography.Regions.Asia.Southeast Asia        0.764
		Geography.Regions.Asia.West Asia             0.761
		Geography.Regions.Europe.Eastern Europe      0.769
		Geography.Regions.Europe.Europe*             0.8
		Geography.Regions.Europe.Northern Europe     0.702
		Geography.Regions.Europe.Southern Europe     0.731
		Geography.Regions.Europe.Western Europe      0.747
		Geography.Regions.Oceania                    0.739
		History and Society.Business and economics   0.619
		History and Society.Education                0.639
		History and Society.History                  0.613
		History and Society.Military and warfare     0.698
		History and Society.Politics and government  0.594
		History and Society.Society                  0.455
		History and Society.Transportation           0.897
		STEM.Biology                                 0.818
		STEM.Chemistry                               0.819
		STEM.Computing                               0.832
		STEM.Earth and environment                   0.712
		STEM.Engineering                             0.774
		STEM.Libraries & Information                 0.721
		STEM.Mathematics                             0.833
		STEM.Medicine & Health                       0.73
		STEM.Physics                                 0.794
		STEM.STEM*                                   0.888
		STEM.Space                                   0.917
		STEM.Technology                              0.761
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.718, macro=0.58):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.585
		Culture.Food and drink                       0.593
		Culture.Internet culture                     0.414
		Culture.Linguistics                          0.797
		Culture.Literature                           0.61
		Culture.Media.Books                          0.661
		Culture.Media.Entertainment                  0.348
		Culture.Media.Films                          0.819
		Culture.Media.Media*                         0.631
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.648
		Culture.Media.Software                       0.172
		Culture.Media.Television                     0.752
		Culture.Media.Video games                    0.659
		Culture.Performing arts                      0.424
		Culture.Philosophy and religion              0.552
		Culture.Sports                               0.954
		Culture.Visual arts.Architecture             0.681
		Culture.Visual arts.Comics and Anime         0.457
		Culture.Visual arts.Fashion                  0.327
		Culture.Visual arts.Visual arts*             0.608
		Geography.Geographical                       0.62
		Geography.Regions.Africa.Africa*             0.546
		Geography.Regions.Africa.Central Africa      0.187
		Geography.Regions.Africa.Eastern Africa      0.351
		Geography.Regions.Africa.Northern Africa     0.354
		Geography.Regions.Africa.Southern Africa     0.545
		Geography.Regions.Africa.Western Africa      0.37
		Geography.Regions.Americas.Central America   0.661
		Geography.Regions.Americas.North America     0.717
		Geography.Regions.Americas.South America     0.725
		Geography.Regions.Asia.Asia*                 0.566
		Geography.Regions.Asia.Central Asia          0.339
		Geography.Regions.Asia.East Asia             0.412
		Geography.Regions.Asia.North Asia            0.175
		Geography.Regions.Asia.South Asia            0.919
		Geography.Regions.Asia.Southeast Asia        0.766
		Geography.Regions.Asia.West Asia             0.798
		Geography.Regions.Europe.Eastern Europe      0.672
		Geography.Regions.Europe.Europe*             0.669
		Geography.Regions.Europe.Northern Europe     0.794
		Geography.Regions.Europe.Southern Europe     0.669
		Geography.Regions.Europe.Western Europe      0.682
		Geography.Regions.Oceania                    0.921
		History and Society.Business and economics   0.495
		History and Society.Education                0.728
		History and Society.History                  0.407
		History and Society.Military and warfare     0.575
		History and Society.Politics and government  0.661
		History and Society.Society                  0.38
		History and Society.Transportation           0.817
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.412
		STEM.Computing                               0.263
		STEM.Earth and environment                   0.606
		STEM.Engineering                             0.554
		STEM.Libraries & Information                 0.396
		STEM.Mathematics                             0.253
		STEM.Medicine & Health                       0.68
		STEM.Physics                                 0.201
		STEM.STEM*                                   0.751
		STEM.Space                                   0.911
		STEM.Technology                              0.275
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       1
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.744, macro=0.633):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.883
		Culture.Biography.Women                      0.659
		Culture.Food and drink                       0.684
		Culture.Internet culture                     0.55
		Culture.Linguistics                          0.772
		Culture.Literature                           0.683
		Culture.Media.Books                          0.717
		Culture.Media.Entertainment                  0.432
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.733
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.643
		Culture.Media.Software                       0.285
		Culture.Media.Television                     0.733
		Culture.Media.Video games                    0.759
		Culture.Performing arts                      0.506
		Culture.Philosophy and religion              0.563
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.696
		Culture.Visual arts.Comics and Anime         0.599
		Culture.Visual arts.Fashion                  0.458
		Culture.Visual arts.Visual arts*             0.673
		Geography.Geographical                       0.645
		Geography.Regions.Africa.Africa*             0.636
		Geography.Regions.Africa.Central Africa      0.277
		Geography.Regions.Africa.Eastern Africa      0.474
		Geography.Regions.Africa.Northern Africa     0.487
		Geography.Regions.Africa.Southern Africa     0.63
		Geography.Regions.Africa.Western Africa      0.487
		Geography.Regions.Americas.Central America   0.673
		Geography.Regions.Americas.North America     0.685
		Geography.Regions.Americas.South America     0.735
		Geography.Regions.Asia.Asia*                 0.675
		Geography.Regions.Asia.Central Asia          0.473
		Geography.Regions.Asia.East Asia             0.546
		Geography.Regions.Asia.North Asia            0.285
		Geography.Regions.Asia.South Asia            0.838
		Geography.Regions.Asia.Southeast Asia        0.765
		Geography.Regions.Asia.West Asia             0.779
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.729
		Geography.Regions.Europe.Northern Europe     0.745
		Geography.Regions.Europe.Southern Europe     0.699
		Geography.Regions.Europe.Western Europe      0.713
		Geography.Regions.Oceania                    0.82
		History and Society.Business and economics   0.55
		History and Society.Education                0.68
		History and Society.History                  0.489
		History and Society.Military and warfare     0.631
		History and Society.Politics and government  0.625
		History and Society.Society                  0.414
		History and Society.Transportation           0.855
		STEM.Biology                                 0.863
		STEM.Chemistry                               0.548
		STEM.Computing                               0.4
		STEM.Earth and environment                   0.655
		STEM.Engineering                             0.646
		STEM.Libraries & Information                 0.511
		STEM.Mathematics                             0.388
		STEM.Medicine & Health                       0.704
		STEM.Physics                                 0.321
		STEM.STEM*                                   0.814
		STEM.Space                                   0.914
		STEM.Technology                              0.404
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.975
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.985
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.955
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.99
		History and Society.Education                0.996
		History and Society.History                  0.986
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.98
		History and Society.Society                  0.984
		History and Society.Transportation           0.995
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.998
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.031
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.033
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.01
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.009
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.985
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.982
		Culture.Literature                           0.98
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.973
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.973
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.977
		Culture.Philosophy and religion              0.96
		Culture.Sports                               0.98
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.984
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.967
		Geography.Regions.Americas.Central America   0.979
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.986
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.981
		Geography.Regions.Asia.West Asia             0.983
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.976
		History and Society.Business and economics   0.968
		History and Society.Education                0.977
		History and Society.History                  0.96
		History and Society.Military and warfare     0.975
		History and Society.Politics and government  0.962
		History and Society.Society                  0.929
		History and Society.Transportation           0.985
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.987
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.98
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.973
		STEM.Mathematics                             0.987
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.986
		STEM.STEM*                                   0.978
		STEM.Space                                   0.991
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.797, macro=0.66):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.938
		Culture.Biography.Women                      0.653
		Culture.Food and drink                       0.768
		Culture.Internet culture                     0.712
		Culture.Linguistics                          0.793
		Culture.Literature                           0.773
		Culture.Media.Books                          0.774
		Culture.Media.Entertainment                  0.412
		Culture.Media.Films                          0.859
		Culture.Media.Media*                         0.843
		Culture.Media.Music                          0.835
		Culture.Media.Radio                          0.565
		Culture.Media.Software                       0.316
		Culture.Media.Television                     0.759
		Culture.Media.Video games                    0.839
		Culture.Performing arts                      0.471
		Culture.Philosophy and religion              0.559
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.729
		Culture.Visual arts.Comics and Anime         0.718
		Culture.Visual arts.Fashion                  0.427
		Culture.Visual arts.Visual arts*             0.741
		Geography.Geographical                       0.657
		Geography.Regions.Africa.Africa*             0.656
		Geography.Regions.Africa.Central Africa      0.201
		Geography.Regions.Africa.Eastern Africa      0.345
		Geography.Regions.Africa.Northern Africa     0.432
		Geography.Regions.Africa.Southern Africa     0.581
		Geography.Regions.Africa.Western Africa      0.342
		Geography.Regions.Americas.Central America   0.664
		Geography.Regions.Americas.North America     0.753
		Geography.Regions.Americas.South America     0.766
		Geography.Regions.Asia.Asia*                 0.769
		Geography.Regions.Asia.Central Asia          0.557
		Geography.Regions.Asia.East Asia             0.647
		Geography.Regions.Asia.North Asia            0.261
		Geography.Regions.Asia.South Asia            0.878
		Geography.Regions.Asia.Southeast Asia        0.808
		Geography.Regions.Asia.West Asia             0.808
		Geography.Regions.Europe.Eastern Europe      0.758
		Geography.Regions.Europe.Europe*             0.799
		Geography.Regions.Europe.Northern Europe     0.809
		Geography.Regions.Europe.Southern Europe     0.75
		Geography.Regions.Europe.Western Europe      0.738
		Geography.Regions.Oceania                    0.861
		History and Society.Business and economics   0.544
		History and Society.Education                0.679
		History and Society.History                  0.506
		History and Society.Military and warfare     0.706
		History and Society.Politics and government  0.67
		History and Society.Society                  0.373
		History and Society.Transportation           0.87
		STEM.Biology                                 0.922
		STEM.Chemistry                               0.654
		STEM.Computing                               0.473
		STEM.Earth and environment                   0.624
		STEM.Engineering                             0.662
		STEM.Libraries & Information                 0.469
		STEM.Mathematics                             0.456
		STEM.Medicine & Health                       0.76
		STEM.Physics                                 0.271
		STEM.STEM*                                   0.914
		STEM.Space                                   0.948
		STEM.Technology                              0.472
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}}}}}

