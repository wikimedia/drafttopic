Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'criterion': 'friedman_mse', 'multilabel': True, 'init': None, 'center': False, 'scale': False, 'presort': 'auto', 'min_impurity_decrease': 0.0, 'warm_start': False, 'min_samples_split': 2, 'label_weights': {}, 'min_impurity_split': None, 'tol': 0.0001, 'learning_rate': 0.1, 'n_estimators': 150, 'random_state': None, 'max_leaf_nodes': None, 'max_features': 'log2', 'validation_fraction': 0.1, 'verbose': 0, 'subsample': 1.0, 'loss': 'deviance', 'n_iter_no_change': None, 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'population_rates': None}
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
	counts (n=59878):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13840  -->  12510  1330   789  45249
			'Culture.Biography.Women'                       5034  -->   4190   844   697  54147
			'Culture.Food and drink'                        1365  -->   1065   300    90  58423
			'Culture.Internet culture'                      3536  -->   3150   386   173  56169
			'Culture.Linguistics'                           1486  -->   1147   339    75  58317
			'Culture.Literature'                            5569  -->   4487  1082   398  53911
			'Culture.Media.Books'                           1422  -->   1114   308    78  58378
			'Culture.Media.Entertainment'                   2003  -->   1399   604   140  57735
			'Culture.Media.Films'                           2638  -->   2232   406   160  57080
			'Culture.Media.Media*'                         13246  -->  11756  1490  1094  45538
			'Culture.Media.Music'                           2946  -->   2614   332   171  56761
			'Culture.Media.Radio'                            312  -->    232    80    23  59543
			'Culture.Media.Software'                        2345  -->   2051   294   246  57287
			'Culture.Media.Television'                      1979  -->   1558   421   120  57779
			'Culture.Media.Video games'                     2103  -->   2000   103    32  57743
			'Culture.Performing arts'                       1413  -->   1107   306    98  58367
			'Culture.Philosophy and religion'               3030  -->   1847  1183   245  56603
			'Culture.Sports'                                3756  -->   3286   470   121  56001
			'Culture.Visual arts.Architecture'              1817  -->   1402   415   137  57924
			'Culture.Visual arts.Comics and Anime'          2218  -->   2072   146    63  57597
			'Culture.Visual arts.Fashion'                   1512  -->   1310   202    66  58300
			'Culture.Visual arts.Visual arts*'              6060  -->   4932  1128   342  53476
			'Geography.Geographical'                        3880  -->   2529  1351   525  55473
			'Geography.Regions.Africa.Africa*'              4938  -->   3989   949   330  54610
			'Geography.Regions.Africa.Central Africa'         28  -->      9    19    45  59805
			'Geography.Regions.Africa.Eastern Africa'        448  -->    331   117    27  59403
			'Geography.Regions.Africa.Northern Africa'      1462  -->   1159   303    90  58326
			'Geography.Regions.Africa.Southern Africa'      1167  -->    873   294    47  58664
			'Geography.Regions.Africa.Western Africa'        683  -->    593    90    48  59147
			'Geography.Regions.Americas.Central America'    1620  -->   1184   436    98  58160
			'Geography.Regions.Americas.North America'      5475  -->   3855  1620   598  53805
			'Geography.Regions.Americas.South America'      2140  -->   1704   436   153  57585
			'Geography.Regions.Asia.Asia*'                 13825  -->  11889  1936  1096  44957
			'Geography.Regions.Asia.Central Asia'           1239  -->   1045   194    60  58579
			'Geography.Regions.Asia.East Asia'              5508  -->   4620   888   440  53930
			'Geography.Regions.Asia.North Asia'             1727  -->   1388   339   190  57961
			'Geography.Regions.Asia.South Asia'             1998  -->   1667   331    62  57818
			'Geography.Regions.Asia.Southeast Asia'         2596  -->   1962   634   203  57079
			'Geography.Regions.Asia.West Asia'              2251  -->   1892   359   102  57525
			'Geography.Regions.Europe.Eastern Europe'       3586  -->   3003   583   253  56039
			'Geography.Regions.Europe.Europe*'             12616  -->  10502  2114  1100  46162
			'Geography.Regions.Europe.Northern Europe'      2912  -->   2013   899   253  56713
			'Geography.Regions.Europe.Southern Europe'      2780  -->   2186   594   144  56954
			'Geography.Regions.Europe.Western Europe'       4017  -->   3186   831   231  55630
			'Geography.Regions.Oceania'                     2190  -->   1657   533   123  57565
			'History and Society.Business and economics'    3336  -->   2236  1100   307  56235
			'History and Society.Education'                 1647  -->   1085   562   111  58120
			'History and Society.History'                   4423  -->   2535  1888   496  54959
			'History and Society.Military and warfare'      5028  -->   4040   988   432  54418
			'History and Society.Politics and government'   4560  -->   2689  1871   455  54863
			'History and Society.Society'                   6042  -->   3272  2770   551  53285
			'History and Society.Transportation'            3550  -->   3328   222    70  56258
			'STEM.Biology'                                  6608  -->   6122   486   150  53120
			'STEM.Chemistry'                                1464  -->   1173   291   125  58289
			'STEM.Computing'                                2467  -->   2141   326   238  57173
			'STEM.Earth and environment'                    1636  -->   1217   419   118  58124
			'STEM.Engineering'                              3046  -->   2598   448   107  56725
			'STEM.Libraries & Information'                   482  -->    393    89    25  59371
			'STEM.Mathematics'                               950  -->    830   120    38  58890
			'STEM.Medicine & Health'                        1834  -->   1454   380   131  57913
			'STEM.Physics'                                  1406  -->   1148   258   147  58325
			'STEM.STEM*'                                   20185  -->  18646  1539   803  38890
			'STEM.Space'                                    1642  -->   1527   115    33  58203
			'STEM.Technology'                               4343  -->   3387   956   486  55049
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.231         0.123
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.002
		Culture.Internet culture                        0.059         0.004
		Culture.Linguistics                             0.025         0.007
		Culture.Literature                              0.093         0.016
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.044         0.011
		Culture.Media.Media*                            0.221         0.059
		Culture.Media.Music                             0.049         0.024
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.051         0.011
		Culture.Sports                                  0.063         0.071
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.037         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.101         0.018
		Geography.Geographical                          0.065         0.024
		Geography.Regions.Africa.Africa*                0.082         0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.007         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.027         0.003
		Geography.Regions.Americas.North America        0.091         0.064
		Geography.Regions.Americas.South America        0.036         0.006
		Geography.Regions.Asia.Asia*                    0.231         0.046
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.092         0.011
		Geography.Regions.Asia.North Asia               0.029         0.001
		Geography.Regions.Asia.South Asia               0.033         0.015
		Geography.Regions.Asia.Southeast Asia           0.043         0.006
		Geography.Regions.Asia.West Asia                0.038         0.011
		Geography.Regions.Europe.Eastern Europe         0.06          0.013
		Geography.Regions.Europe.Europe*                0.211         0.076
		Geography.Regions.Europe.Northern Europe        0.049         0.031
		Geography.Regions.Europe.Southern Europe        0.046         0.013
		Geography.Regions.Europe.Western Europe         0.067         0.019
		Geography.Regions.Oceania                       0.037         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.028         0.007
		History and Society.History                     0.074         0.011
		History and Society.Military and warfare        0.084         0.014
		History and Society.Politics and government     0.076         0.028
		History and Society.Society                     0.101         0.013
		History and Society.Transportation              0.059         0.015
		STEM.Biology                                    0.11          0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.051         0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.016         0
		STEM.Medicine & Health                          0.031         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.337         0.069
		STEM.Space                                      0.027         0.006
		STEM.Technology                                 0.073         0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.074
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.064
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.018
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.008
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.025
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.015
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.025
		History and Society.Society                  0.017
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.926
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.992
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.985
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.975
		History and Society.Society                  0.983
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.819, macro=0.791):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.904
		Culture.Biography.Women                      0.832
		Culture.Food and drink                       0.78
		Culture.Internet culture                     0.891
		Culture.Linguistics                          0.772
		Culture.Literature                           0.806
		Culture.Media.Books                          0.783
		Culture.Media.Entertainment                  0.698
		Culture.Media.Films                          0.846
		Culture.Media.Media*                         0.888
		Culture.Media.Music                          0.887
		Culture.Media.Radio                          0.744
		Culture.Media.Software                       0.875
		Culture.Media.Television                     0.787
		Culture.Media.Video games                    0.951
		Culture.Performing arts                      0.783
		Culture.Philosophy and religion              0.61
		Culture.Sports                               0.875
		Culture.Visual arts.Architecture             0.772
		Culture.Visual arts.Comics and Anime         0.934
		Culture.Visual arts.Fashion                  0.866
		Culture.Visual arts.Visual arts*             0.814
		Geography.Geographical                       0.652
		Geography.Regions.Africa.Africa*             0.808
		Geography.Regions.Africa.Central Africa      0.321
		Geography.Regions.Africa.Eastern Africa      0.739
		Geography.Regions.Africa.Northern Africa     0.793
		Geography.Regions.Africa.Southern Africa     0.748
		Geography.Regions.Africa.Western Africa      0.868
		Geography.Regions.Americas.Central America   0.731
		Geography.Regions.Americas.North America     0.704
		Geography.Regions.Americas.South America     0.796
		Geography.Regions.Asia.Asia*                 0.86
		Geography.Regions.Asia.Central Asia          0.843
		Geography.Regions.Asia.East Asia             0.839
		Geography.Regions.Asia.North Asia            0.804
		Geography.Regions.Asia.South Asia            0.834
		Geography.Regions.Asia.Southeast Asia        0.756
		Geography.Regions.Asia.West Asia             0.841
		Geography.Regions.Europe.Eastern Europe      0.837
		Geography.Regions.Europe.Europe*             0.832
		Geography.Regions.Europe.Northern Europe     0.691
		Geography.Regions.Europe.Southern Europe     0.786
		Geography.Regions.Europe.Western Europe      0.793
		Geography.Regions.Oceania                    0.757
		History and Society.Business and economics   0.67
		History and Society.Education                0.659
		History and Society.History                  0.573
		History and Society.Military and warfare     0.804
		History and Society.Politics and government  0.59
		History and Society.Society                  0.542
		History and Society.Transportation           0.937
		STEM.Biology                                 0.926
		STEM.Chemistry                               0.801
		STEM.Computing                               0.868
		STEM.Earth and environment                   0.744
		STEM.Engineering                             0.853
		STEM.Libraries & Information                 0.815
		STEM.Mathematics                             0.874
		STEM.Medicine & Health                       0.793
		STEM.Physics                                 0.817
		STEM.STEM*                                   0.924
		STEM.Space                                   0.93
		STEM.Technology                              0.78
		-------------------------------------------  -----
	!recall (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.989
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.996
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.99
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.758, macro=0.619):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.881
		Culture.Biography.Women                      0.492
		Culture.Food and drink                       0.556
		Culture.Internet culture                     0.505
		Culture.Linguistics                          0.816
		Culture.Literature                           0.634
		Culture.Media.Books                          0.704
		Culture.Media.Entertainment                  0.509
		Culture.Media.Films                          0.763
		Culture.Media.Media*                         0.702
		Culture.Media.Music                          0.879
		Culture.Media.Radio                          0.806
		Culture.Media.Software                       0.214
		Culture.Media.Television                     0.772
		Culture.Media.Video games                    0.818
		Culture.Performing arts                      0.575
		Culture.Philosophy and religion              0.604
		Culture.Sports                               0.969
		Culture.Visual arts.Architecture             0.777
		Culture.Visual arts.Comics and Anime         0.653
		Culture.Visual arts.Fashion                  0.383
		Culture.Visual arts.Visual arts*             0.705
		Geography.Geographical                       0.627
		Geography.Regions.Africa.Africa*             0.514
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.425
		Geography.Regions.Africa.Northern Africa     0.387
		Geography.Regions.Africa.Southern Africa     0.524
		Geography.Regions.Africa.Western Africa      0.423
		Geography.Regions.Americas.Central America   0.59
		Geography.Regions.Americas.North America     0.815
		Geography.Regions.Americas.South America     0.656
		Geography.Regions.Asia.Asia*                 0.633
		Geography.Regions.Asia.Central Asia          0.417
		Geography.Regions.Asia.East Asia             0.545
		Geography.Regions.Asia.North Asia            0.185
		Geography.Regions.Asia.South Asia            0.923
		Geography.Regions.Asia.Southeast Asia        0.563
		Geography.Regions.Asia.West Asia             0.84
		Geography.Regions.Europe.Eastern Europe      0.708
		Geography.Regions.Europe.Europe*             0.747
		Geography.Regions.Europe.Northern Europe     0.831
		Geography.Regions.Europe.Southern Europe     0.805
		Geography.Regions.Europe.Western Europe      0.79
		Geography.Regions.Oceania                    0.845
		History and Society.Business and economics   0.557
		History and Society.Education                0.719
		History and Society.History                  0.413
		History and Society.Military and warfare     0.593
		History and Society.Politics and government  0.675
		History and Society.Society                  0.403
		History and Society.Transportation           0.92
		STEM.Biology                                 0.92
		STEM.Chemistry                               0.369
		STEM.Computing                               0.361
		STEM.Earth and environment                   0.626
		STEM.Engineering                             0.705
		STEM.Libraries & Information                 0.546
		STEM.Mathematics                             0.361
		STEM.Medicine & Health                       0.694
		STEM.Physics                                 0.216
		STEM.STEM*                                   0.772
		STEM.Space                                   0.909
		STEM.Technology                              0.315
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.997
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.997
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.986
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.997
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.999
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.781, macro=0.675):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.892
		Culture.Biography.Women                      0.618
		Culture.Food and drink                       0.649
		Culture.Internet culture                     0.644
		Culture.Linguistics                          0.793
		Culture.Literature                           0.71
		Culture.Media.Books                          0.741
		Culture.Media.Entertainment                  0.589
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.784
		Culture.Media.Music                          0.883
		Culture.Media.Radio                          0.774
		Culture.Media.Software                       0.344
		Culture.Media.Television                     0.779
		Culture.Media.Video games                    0.88
		Culture.Performing arts                      0.663
		Culture.Philosophy and religion              0.607
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.775
		Culture.Visual arts.Comics and Anime         0.769
		Culture.Visual arts.Fashion                  0.531
		Culture.Visual arts.Visual arts*             0.755
		Geography.Geographical                       0.639
		Geography.Regions.Africa.Africa*             0.628
		Geography.Regions.Africa.Central Africa      0.004
		Geography.Regions.Africa.Eastern Africa      0.54
		Geography.Regions.Africa.Northern Africa     0.521
		Geography.Regions.Africa.Southern Africa     0.616
		Geography.Regions.Africa.Western Africa      0.569
		Geography.Regions.Americas.Central America   0.653
		Geography.Regions.Americas.North America     0.755
		Geography.Regions.Americas.South America     0.719
		Geography.Regions.Asia.Asia*                 0.729
		Geography.Regions.Asia.Central Asia          0.558
		Geography.Regions.Asia.East Asia             0.661
		Geography.Regions.Asia.North Asia            0.301
		Geography.Regions.Asia.South Asia            0.877
		Geography.Regions.Asia.Southeast Asia        0.645
		Geography.Regions.Asia.West Asia             0.84
		Geography.Regions.Europe.Eastern Europe      0.767
		Geography.Regions.Europe.Europe*             0.787
		Geography.Regions.Europe.Northern Europe     0.755
		Geography.Regions.Europe.Southern Europe     0.795
		Geography.Regions.Europe.Western Europe      0.791
		Geography.Regions.Oceania                    0.798
		History and Society.Business and economics   0.609
		History and Society.Education                0.688
		History and Society.History                  0.48
		History and Society.Military and warfare     0.682
		History and Society.Politics and government  0.63
		History and Society.Society                  0.462
		History and Society.Transportation           0.929
		STEM.Biology                                 0.923
		STEM.Chemistry                               0.505
		STEM.Computing                               0.51
		STEM.Earth and environment                   0.68
		STEM.Engineering                             0.772
		STEM.Libraries & Information                 0.654
		STEM.Mathematics                             0.511
		STEM.Medicine & Health                       0.74
		STEM.Physics                                 0.342
		STEM.STEM*                                   0.841
		STEM.Space                                   0.919
		STEM.Technology                              0.449
		-------------------------------------------  -----
	!f1 (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.985
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.996
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.99
		History and Society.Society                  0.992
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.987
		STEM.Space                                   1
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.983, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.971
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.98
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	fpr (micro=0.011, macro=0.005):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.007
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.023
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.004
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.002
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.006
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.011
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.024
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.023
		Geography.Regions.Europe.Northern Europe     0.004
		Geography.Regions.Europe.Southern Europe     0.003
		Geography.Regions.Europe.Western Europe      0.004
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.009
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.01
		History and Society.Transportation           0.001
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.004
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.02
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.98, macro=0.978):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.986
		Culture.Internet culture                     0.991
		Culture.Linguistics                          0.979
		Culture.Literature                           0.982
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.982
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.987
		Culture.Media.Radio                          0.961
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.995
		Culture.Performing arts                      0.983
		Culture.Philosophy and religion              0.967
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.99
		Culture.Visual arts.Fashion                  0.989
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.983
		Geography.Regions.Africa.Central Africa      0.709
		Geography.Regions.Africa.Eastern Africa      0.979
		Geography.Regions.Africa.Northern Africa     0.984
		Geography.Regions.Africa.Southern Africa     0.985
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.982
		Geography.Regions.Americas.North America     0.972
		Geography.Regions.Americas.South America     0.986
		Geography.Regions.Asia.Asia*                 0.977
		Geography.Regions.Asia.Central Asia          0.989
		Geography.Regions.Asia.East Asia             0.984
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.984
		Geography.Regions.Asia.Southeast Asia        0.981
		Geography.Regions.Asia.West Asia             0.985
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.974
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.981
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.984
		History and Society.Business and economics   0.974
		History and Society.Education                0.978
		History and Society.History                  0.961
		History and Society.Military and warfare     0.98
		History and Society.Politics and government  0.961
		History and Society.Society                  0.953
		History and Society.Transportation           0.99
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.988
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.983
		STEM.Engineering                             0.987
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.988
		STEM.Medicine & Health                       0.983
		STEM.Physics                                 0.988
		STEM.STEM*                                   0.983
		STEM.Space                                   0.995
		STEM.Technology                              0.982
		-------------------------------------------  -----
	pr_auc (micro=0.841, macro=0.721):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.942
		Culture.Biography.Women                      0.632
		Culture.Food and drink                       0.708
		Culture.Internet culture                     0.832
		Culture.Linguistics                          0.802
		Culture.Literature                           0.787
		Culture.Media.Books                          0.775
		Culture.Media.Entertainment                  0.534
		Culture.Media.Films                          0.839
		Culture.Media.Media*                         0.889
		Culture.Media.Music                          0.929
		Culture.Media.Radio                          0.696
		Culture.Media.Software                       0.406
		Culture.Media.Television                     0.804
		Culture.Media.Video games                    0.955
		Culture.Performing arts                      0.677
		Culture.Philosophy and religion              0.613
		Culture.Sports                               0.961
		Culture.Visual arts.Architecture             0.805
		Culture.Visual arts.Comics and Anime         0.862
		Culture.Visual arts.Fashion                  0.616
		Culture.Visual arts.Visual arts*             0.836
		Geography.Geographical                       0.686
		Geography.Regions.Africa.Africa*             0.698
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.519
		Geography.Regions.Africa.Northern Africa     0.523
		Geography.Regions.Africa.Southern Africa     0.655
		Geography.Regions.Africa.Western Africa      0.544
		Geography.Regions.Americas.Central America   0.624
		Geography.Regions.Americas.North America     0.84
		Geography.Regions.Americas.South America     0.766
		Geography.Regions.Asia.Asia*                 0.829
		Geography.Regions.Asia.Central Asia          0.644
		Geography.Regions.Asia.East Asia             0.705
		Geography.Regions.Asia.North Asia            0.292
		Geography.Regions.Asia.South Asia            0.922
		Geography.Regions.Asia.Southeast Asia        0.675
		Geography.Regions.Asia.West Asia             0.879
		Geography.Regions.Europe.Eastern Europe      0.845
		Geography.Regions.Europe.Europe*             0.875
		Geography.Regions.Europe.Northern Europe     0.817
		Geography.Regions.Europe.Southern Europe     0.838
		Geography.Regions.Europe.Western Europe      0.857
		Geography.Regions.Oceania                    0.862
		History and Society.Business and economics   0.628
		History and Society.Education                0.676
		History and Society.History                  0.471
		History and Society.Military and warfare     0.765
		History and Society.Politics and government  0.675
		History and Society.Society                  0.476
		History and Society.Transportation           0.967
		STEM.Biology                                 0.958
		STEM.Chemistry                               0.612
		STEM.Computing                               0.597
		STEM.Earth and environment                   0.715
		STEM.Engineering                             0.87
		STEM.Libraries & Information                 0.654
		STEM.Mathematics                             0.688
		STEM.Medicine & Health                       0.764
		STEM.Physics                                 0.404
		STEM.STEM*                                   0.938
		STEM.Space                                   0.967
		STEM.Technology                              0.517
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

