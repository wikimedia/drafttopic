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
	counts (n=58644):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15490  -->  13596  1894   903  42251
			'Culture.Biography.Women'                       4332  -->   2836  1496   600  53712
			'Culture.Food and drink'                        1669  -->   1194   475    93  56882
			'Culture.Internet culture'                      3323  -->   2374   949   268  55053
			'Culture.Linguistics'                           1556  -->    881   675    99  56989
			'Culture.Literature'                            5612  -->   3795  1817   529  52503
			'Culture.Media.Books'                           1527  -->   1022   505   135  56982
			'Culture.Media.Entertainment'                   2282  -->   1043  1239   209  56153
			'Culture.Media.Films'                           2888  -->   2341   547   109  55647
			'Culture.Media.Media*'                         14695  -->  12074  2621  1637  42312
			'Culture.Media.Music'                           3178  -->   2406   772   306  55160
			'Culture.Media.Radio'                            673  -->    379   294    48  57923
			'Culture.Media.Software'                        2238  -->   1601   637   359  56047
			'Culture.Media.Television'                      2423  -->   1552   871   165  56056
			'Culture.Media.Video games'                     2223  -->   1826   397   110  56311
			'Culture.Performing arts'                       1473  -->    740   733   154  57017
			'Culture.Philosophy and religion'               3662  -->   1675  1987   315  54667
			'Culture.Sports'                                5114  -->   4314   800   188  53342
			'Culture.Visual arts.Architecture'              2085  -->   1276   809   189  56370
			'Culture.Visual arts.Comics and Anime'          2327  -->   1835   492   174  56143
			'Culture.Visual arts.Fashion'                   1308  -->    797   511    94  57242
			'Culture.Visual arts.Visual arts*'              6199  -->   3981  2218   525  51920
			'Geography.Geographical'                        3757  -->   2211  1546   478  54409
			'Geography.Regions.Africa.Africa*'              4200  -->   2904  1296   285  54159
			'Geography.Regions.Africa.Central Africa'        821  -->    554   267    63  57760
			'Geography.Regions.Africa.Eastern Africa'        463  -->    296   167    70  58111
			'Geography.Regions.Africa.Northern Africa'      1473  -->   1015   458   118  57053
			'Geography.Regions.Africa.Southern Africa'       674  -->    423   251    77  57893
			'Geography.Regions.Africa.Western Africa'        277  -->    186    91    52  58315
			'Geography.Regions.Americas.Central America'    1313  -->    799   514    51  57280
			'Geography.Regions.Americas.North America'      6457  -->   4203  2254  1149  51038
			'Geography.Regions.Americas.South America'      1489  -->   1057   432    86  57069
			'Geography.Regions.Asia.Asia*'                 14600  -->  11508  3092  1635  42409
			'Geography.Regions.Asia.Central Asia'           1266  -->    835   431    93  57285
			'Geography.Regions.Asia.East Asia'              7283  -->   5499  1784   876  50485
			'Geography.Regions.Asia.North Asia'             1773  -->   1263   510   236  56635
			'Geography.Regions.Asia.South Asia'             1810  -->   1266   544    64  56770
			'Geography.Regions.Asia.Southeast Asia'         1855  -->   1175   680    75  56714
			'Geography.Regions.Asia.West Asia'              2301  -->   1574   727   179  56164
			'Geography.Regions.Europe.Eastern Europe'       3327  -->   2385   942   305  55012
			'Geography.Regions.Europe.Europe*'             13076  -->  10249  2827  1724  43844
			'Geography.Regions.Europe.Northern Europe'      3855  -->   2599  1256   412  54377
			'Geography.Regions.Europe.Southern Europe'      3204  -->   2187  1017   300  55140
			'Geography.Regions.Europe.Western Europe'       3979  -->   2813  1166   448  54217
			'Geography.Regions.Oceania'                     1787  -->   1230   557    71  56786
			'History and Society.Business and economics'    3759  -->   1776  1983   378  54507
			'History and Society.Education'                 1849  -->    926   923   120  56675
			'History and Society.History'                   5284  -->   2751  2533   681  52679
			'History and Society.Military and warfare'      5136  -->   3150  1986   477  53031
			'History and Society.Politics and government'   5011  -->   2406  2605   469  53164
			'History and Society.Society'                   6391  -->   2579  3812   551  51702
			'History and Society.Transportation'            3675  -->   2981   694   203  54766
			'STEM.Biology'                                  3308  -->   2399   909   165  55171
			'STEM.Chemistry'                                1395  -->    918   477   132  57117
			'STEM.Computing'                                2630  -->   1862   768   471  55543
			'STEM.Earth and environment'                    1795  -->   1053   742   156  56693
			'STEM.Engineering'                              2596  -->   1644   952   187  55861
			'STEM.Libraries & Information'                   730  -->    476   254    49  57865
			'STEM.Mathematics'                              1143  -->    780   363    84  57417
			'STEM.Medicine & Health'                        1884  -->   1016   868   185  56575
			'STEM.Physics'                                  1376  -->    737   639   167  57101
			'STEM.STEM*'                                   17094  -->  14524  2570  1262  40288
			'STEM.Space'                                    1657  -->   1374   283    58  56929
			'STEM.Technology'                               4504  -->   2845  1659   695  53445
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.264         0.123
		Culture.Biography.Women                         0.074         0.015
		Culture.Food and drink                          0.028         0.002
		Culture.Internet culture                        0.057         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.096         0.015
		Culture.Media.Books                             0.026         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.049         0.011
		Culture.Media.Media*                            0.251         0.058
		Culture.Media.Music                             0.054         0.024
		Culture.Media.Radio                             0.011         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.041         0.009
		Culture.Media.Video games                       0.038         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.062         0.011
		Culture.Sports                                  0.087         0.071
		Culture.Visual arts.Architecture                0.036         0.011
		Culture.Visual arts.Comics and Anime            0.04          0.002
		Culture.Visual arts.Fashion                     0.022         0.001
		Culture.Visual arts.Visual arts*                0.106         0.018
		Geography.Geographical                          0.064         0.024
		Geography.Regions.Africa.Africa*                0.072         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.005         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.11          0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.249         0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.124         0.011
		Geography.Regions.Asia.North Asia               0.03          0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.032         0.006
		Geography.Regions.Asia.West Asia                0.039         0.011
		Geography.Regions.Europe.Eastern Europe         0.057         0.013
		Geography.Regions.Europe.Europe*                0.223         0.076
		Geography.Regions.Europe.Northern Europe        0.066         0.031
		Geography.Regions.Europe.Southern Europe        0.055         0.013
		Geography.Regions.Europe.Western Europe         0.068         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.064         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.09          0.011
		History and Society.Military and warfare        0.088         0.014
		History and Society.Politics and government     0.085         0.028
		History and Society.Society                     0.109         0.013
		History and Society.Transportation              0.063         0.015
		STEM.Biology                                    0.056         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.045         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.044         0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.032         0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.291         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.077         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.083
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.063
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.062
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.071
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.025
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.095
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.022
		History and Society.Society                  0.016
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.087
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.917
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.929
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.905
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.978
		History and Society.Society                  0.984
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.913
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.731, macro=0.664):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.655
		Culture.Food and drink                       0.715
		Culture.Internet culture                     0.714
		Culture.Linguistics                          0.566
		Culture.Literature                           0.676
		Culture.Media.Books                          0.669
		Culture.Media.Entertainment                  0.457
		Culture.Media.Films                          0.811
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.757
		Culture.Media.Radio                          0.563
		Culture.Media.Software                       0.715
		Culture.Media.Television                     0.641
		Culture.Media.Video games                    0.821
		Culture.Performing arts                      0.502
		Culture.Philosophy and religion              0.457
		Culture.Sports                               0.844
		Culture.Visual arts.Architecture             0.612
		Culture.Visual arts.Comics and Anime         0.789
		Culture.Visual arts.Fashion                  0.609
		Culture.Visual arts.Visual arts*             0.642
		Geography.Geographical                       0.589
		Geography.Regions.Africa.Africa*             0.691
		Geography.Regions.Africa.Central Africa      0.675
		Geography.Regions.Africa.Eastern Africa      0.639
		Geography.Regions.Africa.Northern Africa     0.689
		Geography.Regions.Africa.Southern Africa     0.628
		Geography.Regions.Africa.Western Africa      0.671
		Geography.Regions.Americas.Central America   0.609
		Geography.Regions.Americas.North America     0.651
		Geography.Regions.Americas.South America     0.71
		Geography.Regions.Asia.Asia*                 0.788
		Geography.Regions.Asia.Central Asia          0.66
		Geography.Regions.Asia.East Asia             0.755
		Geography.Regions.Asia.North Asia            0.712
		Geography.Regions.Asia.South Asia            0.699
		Geography.Regions.Asia.Southeast Asia        0.633
		Geography.Regions.Asia.West Asia             0.684
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.784
		Geography.Regions.Europe.Northern Europe     0.674
		Geography.Regions.Europe.Southern Europe     0.683
		Geography.Regions.Europe.Western Europe      0.707
		Geography.Regions.Oceania                    0.688
		History and Society.Business and economics   0.472
		History and Society.Education                0.501
		History and Society.History                  0.521
		History and Society.Military and warfare     0.613
		History and Society.Politics and government  0.48
		History and Society.Society                  0.404
		History and Society.Transportation           0.811
		STEM.Biology                                 0.725
		STEM.Chemistry                               0.658
		STEM.Computing                               0.708
		STEM.Earth and environment                   0.587
		STEM.Engineering                             0.633
		STEM.Libraries & Information                 0.652
		STEM.Mathematics                             0.682
		STEM.Medicine & Health                       0.539
		STEM.Physics                                 0.536
		STEM.STEM*                                   0.85
		STEM.Space                                   0.829
		STEM.Technology                              0.632
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.991
		History and Society.Society                  0.989
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.672, macro=0.517):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.855
		Culture.Biography.Women                      0.467
		Culture.Food and drink                       0.52
		Culture.Internet culture                     0.341
		Culture.Linguistics                          0.707
		Culture.Literature                           0.516
		Culture.Media.Books                          0.534
		Culture.Media.Entertainment                  0.307
		Culture.Media.Films                          0.815
		Culture.Media.Media*                         0.578
		Culture.Media.Music                          0.771
		Culture.Media.Radio                          0.595
		Culture.Media.Software                       0.13
		Culture.Media.Television                     0.66
		Culture.Media.Video games                    0.525
		Culture.Performing arts                      0.351
		Culture.Philosophy and religion              0.462
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.662
		Culture.Visual arts.Comics and Anime         0.36
		Culture.Visual arts.Fashion                  0.231
		Culture.Visual arts.Visual arts*             0.544
		Geography.Geographical                       0.62
		Geography.Regions.Africa.Africa*             0.509
		Geography.Regions.Africa.Central Africa      0.281
		Geography.Regions.Africa.Eastern Africa      0.195
		Geography.Regions.Africa.Northern Africa     0.291
		Geography.Regions.Africa.Southern Africa     0.357
		Geography.Regions.Africa.Western Africa      0.34
		Geography.Regions.Americas.Central America   0.694
		Geography.Regions.Americas.North America     0.67
		Geography.Regions.Americas.South America     0.75
		Geography.Regions.Asia.Asia*                 0.503
		Geography.Regions.Asia.Central Asia          0.261
		Geography.Regions.Asia.East Asia             0.338
		Geography.Regions.Asia.North Asia            0.137
		Geography.Regions.Asia.South Asia            0.905
		Geography.Regions.Asia.Southeast Asia        0.743
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.628
		Geography.Regions.Europe.Europe*             0.631
		Geography.Regions.Europe.Northern Europe     0.739
		Geography.Regions.Europe.Southern Europe     0.625
		Geography.Regions.Europe.Western Europe      0.628
		Geography.Regions.Oceania                    0.894
		History and Society.Business and economics   0.411
		History and Society.Education                0.637
		History and Society.History                  0.309
		History and Society.Military and warfare     0.495
		History and Society.Politics and government  0.614
		History and Society.Society                  0.328
		History and Society.Transportation           0.771
		STEM.Biology                                 0.894
		STEM.Chemistry                               0.308
		STEM.Computing                               0.185
		STEM.Earth and environment                   0.493
		STEM.Engineering                             0.5
		STEM.Libraries & Information                 0.324
		STEM.Mathematics                             0.163
		STEM.Medicine & Health                       0.516
		STEM.Physics                                 0.135
		STEM.STEM*                                   0.675
		STEM.Space                                   0.831
		STEM.Technology                              0.202
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.995
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
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.985
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.989
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.691, macro=0.557):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.545
		Culture.Food and drink                       0.602
		Culture.Internet culture                     0.462
		Culture.Linguistics                          0.629
		Culture.Literature                           0.585
		Culture.Media.Books                          0.594
		Culture.Media.Entertainment                  0.367
		Culture.Media.Films                          0.813
		Culture.Media.Media*                         0.679
		Culture.Media.Music                          0.764
		Culture.Media.Radio                          0.579
		Culture.Media.Software                       0.22
		Culture.Media.Television                     0.65
		Culture.Media.Video games                    0.64
		Culture.Performing arts                      0.413
		Culture.Philosophy and religion              0.46
		Culture.Sports                               0.893
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.494
		Culture.Visual arts.Fashion                  0.335
		Culture.Visual arts.Visual arts*             0.589
		Geography.Geographical                       0.604
		Geography.Regions.Africa.Africa*             0.587
		Geography.Regions.Africa.Central Africa      0.397
		Geography.Regions.Africa.Eastern Africa      0.298
		Geography.Regions.Africa.Northern Africa     0.409
		Geography.Regions.Africa.Southern Africa     0.455
		Geography.Regions.Africa.Western Africa      0.451
		Geography.Regions.Americas.Central America   0.648
		Geography.Regions.Americas.North America     0.66
		Geography.Regions.Americas.South America     0.729
		Geography.Regions.Asia.Asia*                 0.614
		Geography.Regions.Asia.Central Asia          0.374
		Geography.Regions.Asia.East Asia             0.467
		Geography.Regions.Asia.North Asia            0.23
		Geography.Regions.Asia.South Asia            0.789
		Geography.Regions.Asia.Southeast Asia        0.684
		Geography.Regions.Asia.West Asia             0.694
		Geography.Regions.Europe.Eastern Europe      0.67
		Geography.Regions.Europe.Europe*             0.699
		Geography.Regions.Europe.Northern Europe     0.705
		Geography.Regions.Europe.Southern Europe     0.652
		Geography.Regions.Europe.Western Europe      0.665
		Geography.Regions.Oceania                    0.778
		History and Society.Business and economics   0.44
		History and Society.Education                0.561
		History and Society.History                  0.388
		History and Society.Military and warfare     0.548
		History and Society.Politics and government  0.539
		History and Society.Society                  0.362
		History and Society.Transportation           0.79
		STEM.Biology                                 0.801
		STEM.Chemistry                               0.42
		STEM.Computing                               0.293
		STEM.Earth and environment                   0.536
		STEM.Engineering                             0.559
		STEM.Libraries & Information                 0.433
		STEM.Mathematics                             0.263
		STEM.Medicine & Health                       0.527
		STEM.Physics                                 0.216
		STEM.STEM*                                   0.752
		STEM.Space                                   0.83
		STEM.Technology                              0.307
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
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
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
		History and Society.Society                  0.991
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.954
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.977
		History and Society.Society                  0.982
		History and Society.Transportation           0.994
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.997
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.961
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.011
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.037
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.009
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.022
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.037
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.017
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.009
		History and Society.Society                  0.011
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.03
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.965, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.968
		Culture.Food and drink                       0.977
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.963
		Culture.Literature                           0.963
		Culture.Media.Books                          0.974
		Culture.Media.Entertainment                  0.956
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.955
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.971
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.959
		Culture.Philosophy and religion              0.933
		Culture.Sports                               0.974
		Culture.Visual arts.Architecture             0.97
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.969
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.967
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.973
		Geography.Regions.Africa.Northern Africa     0.971
		Geography.Regions.Africa.Southern Africa     0.945
		Geography.Regions.Africa.Western Africa      0.942
		Geography.Regions.Americas.Central America   0.963
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.967
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.97
		Geography.Regions.Asia.Southeast Asia        0.965
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.969
		Geography.Regions.Europe.Western Europe      0.971
		Geography.Regions.Oceania                    0.971
		History and Society.Business and economics   0.949
		History and Society.Education                0.96
		History and Society.History                  0.941
		History and Society.Military and warfare     0.959
		History and Society.Politics and government  0.932
		History and Society.Society                  0.902
		History and Society.Transportation           0.979
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.978
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.961
		STEM.Engineering                             0.968
		STEM.Libraries & Information                 0.962
		STEM.Mathematics                             0.978
		STEM.Medicine & Health                       0.958
		STEM.Physics                                 0.972
		STEM.STEM*                                   0.968
		STEM.Space                                   0.983
		STEM.Technology                              0.964
		-------------------------------------------  -----
	pr_auc (micro=0.727, macro=0.546):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.929
		Culture.Biography.Women                      0.508
		Culture.Food and drink                       0.634
		Culture.Internet culture                     0.589
		Culture.Linguistics                          0.621
		Culture.Literature                           0.652
		Culture.Media.Books                          0.587
		Culture.Media.Entertainment                  0.29
		Culture.Media.Films                          0.768
		Culture.Media.Media*                         0.791
		Culture.Media.Music                          0.795
		Culture.Media.Radio                          0.432
		Culture.Media.Software                       0.197
		Culture.Media.Television                     0.61
		Culture.Media.Video games                    0.697
		Culture.Performing arts                      0.378
		Culture.Philosophy and religion              0.411
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.634
		Culture.Visual arts.Comics and Anime         0.524
		Culture.Visual arts.Fashion                  0.248
		Culture.Visual arts.Visual arts*             0.609
		Geography.Geographical                       0.625
		Geography.Regions.Africa.Africa*             0.578
		Geography.Regions.Africa.Central Africa      0.31
		Geography.Regions.Africa.Eastern Africa      0.143
		Geography.Regions.Africa.Northern Africa     0.291
		Geography.Regions.Africa.Southern Africa     0.323
		Geography.Regions.Africa.Western Africa      0.29
		Geography.Regions.Americas.Central America   0.593
		Geography.Regions.Americas.North America     0.694
		Geography.Regions.Americas.South America     0.724
		Geography.Regions.Asia.Asia*                 0.688
		Geography.Regions.Asia.Central Asia          0.323
		Geography.Regions.Asia.East Asia             0.508
		Geography.Regions.Asia.North Asia            0.193
		Geography.Regions.Asia.South Asia            0.829
		Geography.Regions.Asia.Southeast Asia        0.674
		Geography.Regions.Asia.West Asia             0.666
		Geography.Regions.Europe.Eastern Europe      0.696
		Geography.Regions.Europe.Europe*             0.753
		Geography.Regions.Europe.Northern Europe     0.744
		Geography.Regions.Europe.Southern Europe     0.677
		Geography.Regions.Europe.Western Europe      0.676
		Geography.Regions.Oceania                    0.81
		History and Society.Business and economics   0.379
		History and Society.Education                0.553
		History and Society.History                  0.339
		History and Society.Military and warfare     0.563
		History and Society.Politics and government  0.553
		History and Society.Society                  0.314
		History and Society.Transportation           0.829
		STEM.Biology                                 0.853
		STEM.Chemistry                               0.449
		STEM.Computing                               0.273
		STEM.Earth and environment                   0.449
		STEM.Engineering                             0.581
		STEM.Libraries & Information                 0.332
		STEM.Mathematics                             0.276
		STEM.Medicine & Health                       0.463
		STEM.Physics                                 0.13
		STEM.STEM*                                   0.845
		STEM.Space                                   0.848
		STEM.Technology                              0.303
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

