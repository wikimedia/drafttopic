Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'verbose': 0, 'init': None, 'criterion': 'friedman_mse', 'n_estimators': 150, 'label_weights': {}, 'presort': 'deprecated', 'loss': 'deviance', 'random_state': None, 'max_leaf_nodes': None, 'warm_start': False, 'tol': 0.0001, 'center': False, 'min_weight_fraction_leaf': 0.0, 'max_features': 'log2', 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'min_impurity_split': None, 'validation_fraction': 0.1, 'max_depth': 5, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'subsample': 1.0, 'learning_rate': 0.1, 'scale': False, 'ccp_alpha': 0.0, 'min_impurity_decrease': 0.0}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=58644):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15490  -->  13588  1902   907  42247
			'Culture.Biography.Women'                       4332  -->   2827  1505   627  53685
			'Culture.Food and drink'                        1669  -->   1183   486    97  56878
			'Culture.Internet culture'                      3323  -->   2389   934   264  55057
			'Culture.Linguistics'                           1556  -->    908   648   123  56965
			'Culture.Literature'                            5612  -->   3782  1830   540  52492
			'Culture.Media.Books'                           1527  -->   1027   500   127  56990
			'Culture.Media.Entertainment'                   2282  -->   1038  1244   225  56137
			'Culture.Media.Films'                           2888  -->   2316   572   107  55649
			'Culture.Media.Media*'                         14695  -->  12061  2634  1627  42322
			'Culture.Media.Music'                           3178  -->   2394   784   303  55163
			'Culture.Media.Radio'                            673  -->    393   280    45  57926
			'Culture.Media.Software'                        2238  -->   1592   646   366  56040
			'Culture.Media.Television'                      2423  -->   1547   876   160  56061
			'Culture.Media.Video games'                     2223  -->   1832   391    89  56332
			'Culture.Performing arts'                       1473  -->    730   743   143  57028
			'Culture.Philosophy and religion'               3662  -->   1701  1961   305  54677
			'Culture.Sports'                                5114  -->   4302   812   195  53335
			'Culture.Visual arts.Architecture'              2085  -->   1260   825   207  56352
			'Culture.Visual arts.Comics and Anime'          2327  -->   1843   484   183  56134
			'Culture.Visual arts.Fashion'                   1308  -->    820   488    84  57252
			'Culture.Visual arts.Visual arts*'              6199  -->   4009  2190   547  51898
			'Geography.Geographical'                        3757  -->   2228  1529   454  54433
			'Geography.Regions.Africa.Africa*'              4200  -->   2892  1308   291  54153
			'Geography.Regions.Africa.Central Africa'        821  -->    549   272    62  57761
			'Geography.Regions.Africa.Eastern Africa'        463  -->    312   151    47  58134
			'Geography.Regions.Africa.Northern Africa'      1473  -->   1009   464   111  57060
			'Geography.Regions.Africa.Southern Africa'       674  -->    419   255    71  57899
			'Geography.Regions.Africa.Western Africa'        277  -->    184    93    32  58335
			'Geography.Regions.Americas.Central America'    1313  -->    791   522    56  57275
			'Geography.Regions.Americas.North America'      6457  -->   4225  2232  1159  51028
			'Geography.Regions.Americas.South America'      1489  -->   1058   431    86  57069
			'Geography.Regions.Asia.Asia*'                 14600  -->  11525  3075  1633  42411
			'Geography.Regions.Asia.Central Asia'           1266  -->    837   429    89  57289
			'Geography.Regions.Asia.East Asia'              7283  -->   5500  1783   884  50477
			'Geography.Regions.Asia.North Asia'             1773  -->   1253   520   218  56653
			'Geography.Regions.Asia.South Asia'             1810  -->   1281   529    78  56756
			'Geography.Regions.Asia.Southeast Asia'         1855  -->   1179   676    96  56693
			'Geography.Regions.Asia.West Asia'              2301  -->   1579   722   175  56168
			'Geography.Regions.Europe.Eastern Europe'       3327  -->   2399   928   307  55010
			'Geography.Regions.Europe.Europe*'             13076  -->  10244  2832  1712  43856
			'Geography.Regions.Europe.Northern Europe'      3855  -->   2602  1253   408  54381
			'Geography.Regions.Europe.Southern Europe'      3204  -->   2174  1030   324  55116
			'Geography.Regions.Europe.Western Europe'       3979  -->   2831  1148   432  54233
			'Geography.Regions.Oceania'                     1787  -->   1237   550    76  56781
			'History and Society.Business and economics'    3759  -->   1780  1979   374  54511
			'History and Society.Education'                 1849  -->    945   904   124  56671
			'History and Society.History'                   5284  -->   2714  2570   676  52684
			'History and Society.Military and warfare'      5136  -->   3195  1941   486  53022
			'History and Society.Politics and government'   5011  -->   2421  2590   470  53163
			'History and Society.Society'                   6391  -->   2544  3847   564  51689
			'History and Society.Transportation'            3675  -->   2987   688   189  54780
			'STEM.Biology'                                  3308  -->   2397   911   153  55183
			'STEM.Chemistry'                                1395  -->    906   489   130  57119
			'STEM.Computing'                                2630  -->   1858   772   440  55574
			'STEM.Earth and environment'                    1795  -->   1059   736   169  56680
			'STEM.Engineering'                              2596  -->   1653   943   181  55867
			'STEM.Libraries & Information'                   730  -->    456   274    34  57880
			'STEM.Mathematics'                              1143  -->    765   378    90  57411
			'STEM.Medicine & Health'                        1884  -->    997   887   194  56566
			'STEM.Physics'                                  1376  -->    730   646   173  57095
			'STEM.STEM*'                                   17094  -->  14541  2553  1288  40262
			'STEM.Space'                                    1657  -->   1380   277    71  56916
			'STEM.Technology'                               4504  -->   2851  1653   688  53452
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
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.021
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.083
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.063
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.005
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.022
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.063
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.071
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.026
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.015
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.022
		History and Society.Society                  0.016
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.003
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.088
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.917
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.995
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.929
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.974
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.978
		History and Society.Society                  0.984
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.997
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.912
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.732, macro=0.664):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.653
		Culture.Food and drink                       0.709
		Culture.Internet culture                     0.719
		Culture.Linguistics                          0.584
		Culture.Literature                           0.674
		Culture.Media.Books                          0.673
		Culture.Media.Entertainment                  0.455
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.753
		Culture.Media.Radio                          0.584
		Culture.Media.Software                       0.711
		Culture.Media.Television                     0.638
		Culture.Media.Video games                    0.824
		Culture.Performing arts                      0.496
		Culture.Philosophy and religion              0.465
		Culture.Sports                               0.841
		Culture.Visual arts.Architecture             0.604
		Culture.Visual arts.Comics and Anime         0.792
		Culture.Visual arts.Fashion                  0.627
		Culture.Visual arts.Visual arts*             0.647
		Geography.Geographical                       0.593
		Geography.Regions.Africa.Africa*             0.689
		Geography.Regions.Africa.Central Africa      0.669
		Geography.Regions.Africa.Eastern Africa      0.674
		Geography.Regions.Africa.Northern Africa     0.685
		Geography.Regions.Africa.Southern Africa     0.622
		Geography.Regions.Africa.Western Africa      0.664
		Geography.Regions.Americas.Central America   0.602
		Geography.Regions.Americas.North America     0.654
		Geography.Regions.Americas.South America     0.711
		Geography.Regions.Asia.Asia*                 0.789
		Geography.Regions.Asia.Central Asia          0.661
		Geography.Regions.Asia.East Asia             0.755
		Geography.Regions.Asia.North Asia            0.707
		Geography.Regions.Asia.South Asia            0.708
		Geography.Regions.Asia.Southeast Asia        0.636
		Geography.Regions.Asia.West Asia             0.686
		Geography.Regions.Europe.Eastern Europe      0.721
		Geography.Regions.Europe.Europe*             0.783
		Geography.Regions.Europe.Northern Europe     0.675
		Geography.Regions.Europe.Southern Europe     0.679
		Geography.Regions.Europe.Western Europe      0.711
		Geography.Regions.Oceania                    0.692
		History and Society.Business and economics   0.474
		History and Society.Education                0.511
		History and Society.History                  0.514
		History and Society.Military and warfare     0.622
		History and Society.Politics and government  0.483
		History and Society.Society                  0.398
		History and Society.Transportation           0.813
		STEM.Biology                                 0.725
		STEM.Chemistry                               0.649
		STEM.Computing                               0.706
		STEM.Earth and environment                   0.59
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.625
		STEM.Mathematics                             0.669
		STEM.Medicine & Health                       0.529
		STEM.Physics                                 0.531
		STEM.STEM*                                   0.851
		STEM.Space                                   0.833
		STEM.Technology                              0.633
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.992
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
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.991
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.671, macro=0.52):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.455
		Culture.Food and drink                       0.507
		Culture.Internet culture                     0.346
		Culture.Linguistics                          0.667
		Culture.Literature                           0.51
		Culture.Media.Books                          0.55
		Culture.Media.Entertainment                  0.29
		Culture.Media.Films                          0.816
		Culture.Media.Media*                         0.579
		Culture.Media.Music                          0.771
		Culture.Media.Radio                          0.619
		Culture.Media.Software                       0.127
		Culture.Media.Television                     0.666
		Culture.Media.Video games                    0.578
		Culture.Performing arts                      0.364
		Culture.Philosophy and religion              0.474
		Culture.Sports                               0.947
		Culture.Visual arts.Architecture             0.638
		Culture.Visual arts.Comics and Anime         0.349
		Culture.Visual arts.Fashion                  0.257
		Culture.Visual arts.Visual arts*             0.536
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.503
		Geography.Regions.Africa.Central Africa      0.283
		Geography.Regions.Africa.Eastern Africa      0.275
		Geography.Regions.Africa.Northern Africa     0.302
		Geography.Regions.Africa.Southern Africa     0.374
		Geography.Regions.Africa.Western Africa      0.453
		Geography.Regions.Americas.Central America   0.671
		Geography.Regions.Americas.North America     0.669
		Geography.Regions.Americas.South America     0.75
		Geography.Regions.Asia.Asia*                 0.504
		Geography.Regions.Asia.Central Asia          0.27
		Geography.Regions.Asia.East Asia             0.336
		Geography.Regions.Asia.North Asia            0.146
		Geography.Regions.Asia.South Asia            0.888
		Geography.Regions.Asia.Southeast Asia        0.694
		Geography.Regions.Asia.West Asia             0.709
		Geography.Regions.Europe.Eastern Europe      0.628
		Geography.Regions.Europe.Europe*             0.632
		Geography.Regions.Europe.Northern Europe     0.741
		Geography.Regions.Europe.Southern Europe     0.605
		Geography.Regions.Europe.Western Europe      0.638
		Geography.Regions.Oceania                    0.888
		History and Society.Business and economics   0.415
		History and Society.Education                0.634
		History and Society.History                  0.308
		History and Society.Military and warfare     0.494
		History and Society.Politics and government  0.615
		History and Society.Society                  0.32
		History and Society.Transportation           0.784
		STEM.Biology                                 0.901
		STEM.Chemistry                               0.309
		STEM.Computing                               0.195
		STEM.Earth and environment                   0.475
		STEM.Engineering                             0.509
		STEM.Libraries & Information                 0.398
		STEM.Mathematics                             0.151
		STEM.Medicine & Health                       0.499
		STEM.Physics                                 0.13
		STEM.STEM*                                   0.671
		STEM.Space                                   0.802
		STEM.Technology                              0.204
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
		Geography.Regions.Asia.South Asia            0.996
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
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.985
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.99
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
	f1 (micro=0.691, macro=0.561):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.536
		Culture.Food and drink                       0.591
		Culture.Internet culture                     0.467
		Culture.Linguistics                          0.622
		Culture.Literature                           0.581
		Culture.Media.Books                          0.605
		Culture.Media.Entertainment                  0.355
		Culture.Media.Films                          0.809
		Culture.Media.Media*                         0.679
		Culture.Media.Music                          0.762
		Culture.Media.Radio                          0.601
		Culture.Media.Software                       0.216
		Culture.Media.Television                     0.652
		Culture.Media.Video games                    0.679
		Culture.Performing arts                      0.42
		Culture.Philosophy and religion              0.469
		Culture.Sports                               0.891
		Culture.Visual arts.Architecture             0.621
		Culture.Visual arts.Comics and Anime         0.485
		Culture.Visual arts.Fashion                  0.365
		Culture.Visual arts.Visual arts*             0.586
		Geography.Geographical                       0.613
		Geography.Regions.Africa.Africa*             0.581
		Geography.Regions.Africa.Central Africa      0.397
		Geography.Regions.Africa.Eastern Africa      0.391
		Geography.Regions.Africa.Northern Africa     0.42
		Geography.Regions.Africa.Southern Africa     0.467
		Geography.Regions.Africa.Western Africa      0.539
		Geography.Regions.Americas.Central America   0.635
		Geography.Regions.Americas.North America     0.662
		Geography.Regions.Americas.South America     0.73
		Geography.Regions.Asia.Asia*                 0.615
		Geography.Regions.Asia.Central Asia          0.383
		Geography.Regions.Asia.East Asia             0.465
		Geography.Regions.Asia.North Asia            0.242
		Geography.Regions.Asia.South Asia            0.788
		Geography.Regions.Asia.Southeast Asia        0.664
		Geography.Regions.Asia.West Asia             0.697
		Geography.Regions.Europe.Eastern Europe      0.671
		Geography.Regions.Europe.Europe*             0.7
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.64
		Geography.Regions.Europe.Western Europe      0.673
		Geography.Regions.Oceania                    0.778
		History and Society.Business and economics   0.442
		History and Society.Education                0.566
		History and Society.History                  0.385
		History and Society.Military and warfare     0.551
		History and Society.Politics and government  0.541
		History and Society.Society                  0.355
		History and Society.Transportation           0.798
		STEM.Biology                                 0.803
		STEM.Chemistry                               0.418
		STEM.Computing                               0.306
		STEM.Earth and environment                   0.526
		STEM.Engineering                             0.566
		STEM.Libraries & Information                 0.486
		STEM.Mathematics                             0.247
		STEM.Medicine & Health                       0.514
		STEM.Physics                                 0.209
		STEM.STEM*                                   0.75
		STEM.Space                                   0.817
		STEM.Technology                              0.309
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
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
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
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
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.985
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.955
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.994
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.983
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
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.991
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.983
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
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
		Culture.Biography.Women                      0.012
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.037
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.002
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.008
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
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.009
		History and Society.Society                  0.011
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.965, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.968
		Culture.Food and drink                       0.978
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.962
		Culture.Literature                           0.963
		Culture.Media.Books                          0.975
		Culture.Media.Entertainment                  0.957
		Culture.Media.Films                          0.979
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.956
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.972
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.959
		Culture.Philosophy and religion              0.932
		Culture.Sports                               0.974
		Culture.Visual arts.Architecture             0.97
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.969
		Culture.Visual arts.Visual arts*             0.955
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.966
		Geography.Regions.Africa.Central Africa      0.978
		Geography.Regions.Africa.Eastern Africa      0.965
		Geography.Regions.Africa.Northern Africa     0.972
		Geography.Regions.Africa.Southern Africa     0.947
		Geography.Regions.Africa.Western Africa      0.953
		Geography.Regions.Americas.Central America   0.964
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.975
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.971
		Geography.Regions.Asia.East Asia             0.968
		Geography.Regions.Asia.North Asia            0.981
		Geography.Regions.Asia.South Asia            0.97
		Geography.Regions.Asia.Southeast Asia        0.965
		Geography.Regions.Asia.West Asia             0.97
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.965
		Geography.Regions.Europe.Southern Europe     0.97
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.97
		History and Society.Business and economics   0.95
		History and Society.Education                0.961
		History and Society.History                  0.94
		History and Society.Military and warfare     0.959
		History and Society.Politics and government  0.932
		History and Society.Society                  0.902
		History and Society.Transportation           0.979
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.979
		STEM.Computing                               0.982
		STEM.Earth and environment                   0.962
		STEM.Engineering                             0.968
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.977
		STEM.Medicine & Health                       0.956
		STEM.Physics                                 0.971
		STEM.STEM*                                   0.968
		STEM.Space                                   0.983
		STEM.Technology                              0.964
		-------------------------------------------  -----
	pr_auc (micro=0.726, macro=0.547):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.928
		Culture.Biography.Women                      0.512
		Culture.Food and drink                       0.583
		Culture.Internet culture                     0.505
		Culture.Linguistics                          0.616
		Culture.Literature                           0.624
		Culture.Media.Books                          0.592
		Culture.Media.Entertainment                  0.264
		Culture.Media.Films                          0.791
		Culture.Media.Media*                         0.789
		Culture.Media.Music                          0.775
		Culture.Media.Radio                          0.455
		Culture.Media.Software                       0.217
		Culture.Media.Television                     0.672
		Culture.Media.Video games                    0.734
		Culture.Performing arts                      0.33
		Culture.Philosophy and religion              0.415
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.622
		Culture.Visual arts.Comics and Anime         0.525
		Culture.Visual arts.Fashion                  0.307
		Culture.Visual arts.Visual arts*             0.619
		Geography.Geographical                       0.626
		Geography.Regions.Africa.Africa*             0.579
		Geography.Regions.Africa.Central Africa      0.298
		Geography.Regions.Africa.Eastern Africa      0.205
		Geography.Regions.Africa.Northern Africa     0.323
		Geography.Regions.Africa.Southern Africa     0.335
		Geography.Regions.Africa.Western Africa      0.339
		Geography.Regions.Americas.Central America   0.592
		Geography.Regions.Americas.North America     0.692
		Geography.Regions.Americas.South America     0.741
		Geography.Regions.Asia.Asia*                 0.681
		Geography.Regions.Asia.Central Asia          0.309
		Geography.Regions.Asia.East Asia             0.506
		Geography.Regions.Asia.North Asia            0.189
		Geography.Regions.Asia.South Asia            0.815
		Geography.Regions.Asia.Southeast Asia        0.636
		Geography.Regions.Asia.West Asia             0.68
		Geography.Regions.Europe.Eastern Europe      0.687
		Geography.Regions.Europe.Europe*             0.763
		Geography.Regions.Europe.Northern Europe     0.747
		Geography.Regions.Europe.Southern Europe     0.67
		Geography.Regions.Europe.Western Europe      0.67
		Geography.Regions.Oceania                    0.807
		History and Society.Business and economics   0.389
		History and Society.Education                0.532
		History and Society.History                  0.347
		History and Society.Military and warfare     0.545
		History and Society.Politics and government  0.559
		History and Society.Society                  0.311
		History and Society.Transportation           0.818
		STEM.Biology                                 0.852
		STEM.Chemistry                               0.444
		STEM.Computing                               0.309
		STEM.Earth and environment                   0.468
		STEM.Engineering                             0.576
		STEM.Libraries & Information                 0.346
		STEM.Mathematics                             0.266
		STEM.Medicine & Health                       0.47
		STEM.Physics                                 0.142
		STEM.STEM*                                   0.841
		STEM.Space                                   0.802
		STEM.Technology                              0.307
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

