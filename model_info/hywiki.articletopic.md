Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'ccp_alpha': 0.0, 'tol': 0.0001, 'max_features': 'log2', 'min_impurity_split': None, 'center': False, 'random_state': None, 'n_iter_no_change': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'label_weights': {}, 'loss': 'deviance', 'max_leaf_nodes': None, 'n_estimators': 150, 'min_samples_leaf': 1, 'max_depth': 5, 'min_weight_fraction_leaf': 0.0, 'presort': 'deprecated', 'criterion': 'friedman_mse', 'population_rates': None, 'multilabel': True, 'learning_rate': 0.1, 'verbose': 0, 'subsample': 1.0, 'warm_start': False, 'scale': False, 'validation_fraction': 0.1, 'init': None, 'min_samples_split': 2, 'min_impurity_decrease': 0.0}
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
	counts (n=54263):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15412  -->  13875  1537   727  38124
			'Culture.Biography.Women'                       4335  -->   3145  1190   454  49474
			'Culture.Food and drink'                        1602  -->   1216   386   108  52553
			'Culture.Internet culture'                      2263  -->   1864   399   157  51843
			'Culture.Linguistics'                           1590  -->   1133   457    70  52603
			'Culture.Literature'                            5079  -->   3756  1323   483  48701
			'Culture.Media.Books'                           1754  -->   1445   309   112  52397
			'Culture.Media.Entertainment'                   2043  -->    935  1108   170  52050
			'Culture.Media.Films'                           2911  -->   2566   345   139  51213
			'Culture.Media.Media*'                         12625  -->  11067  1558  1161  40477
			'Culture.Media.Music'                           3277  -->   2744   533   224  50762
			'Culture.Media.Radio'                            219  -->    166    53    36  54008
			'Culture.Media.Software'                        1909  -->   1759   150   175  52179
			'Culture.Media.Television'                      2131  -->   1749   382    80  52052
			'Culture.Media.Video games'                      733  -->    710    23    20  53510
			'Culture.Performing arts'                       1702  -->   1150   552   120  52441
			'Culture.Philosophy and religion'               3764  -->   2002  1762   348  50151
			'Culture.Sports'                                3196  -->   2668   528   107  50960
			'Culture.Visual arts.Architecture'              2441  -->   1886   555   254  51568
			'Culture.Visual arts.Comics and Anime'          1047  -->    884   163    48  53168
			'Culture.Visual arts.Fashion'                    848  -->    666   182    34  53381
			'Culture.Visual arts.Visual arts*'              5369  -->   4048  1321   501  48393
			'Geography.Geographical'                        4379  -->   3009  1370   539  49345
			'Geography.Regions.Africa.Africa*'              3183  -->   1896  1287   207  50873
			'Geography.Regions.Africa.Central Africa'        395  -->    265   130    28  53840
			'Geography.Regions.Africa.Eastern Africa'        216  -->    143    73    49  53998
			'Geography.Regions.Africa.Northern Africa'      1227  -->    762   465   101  52935
			'Geography.Regions.Africa.Southern Africa'       589  -->    463   126    28  53646
			'Geography.Regions.Africa.Western Africa'        140  -->     95    45    40  54083
			'Geography.Regions.Americas.Central America'    1089  -->    408   681    52  53122
			'Geography.Regions.Americas.North America'      5641  -->   4003  1638   824  47798
			'Geography.Regions.Americas.South America'      1614  -->   1269   345    73  52576
			'Geography.Regions.Asia.Asia*'                 13787  -->  11327  2460  1311  39165
			'Geography.Regions.Asia.Central Asia'            875  -->    503   372    58  53330
			'Geography.Regions.Asia.East Asia'              2463  -->   1951   512   130  51670
			'Geography.Regions.Asia.North Asia'             5098  -->   4038  1060   427  48738
			'Geography.Regions.Asia.South Asia'             1731  -->   1159   572    88  52444
			'Geography.Regions.Asia.Southeast Asia'         1109  -->    432   677    59  53095
			'Geography.Regions.Asia.West Asia'              4142  -->   3178   964   367  49754
			'Geography.Regions.Europe.Eastern Europe'       6506  -->   5086  1420   494  47263
			'Geography.Regions.Europe.Europe*'             18893  -->  15806  3087  1966  33404
			'Geography.Regions.Europe.Northern Europe'      4100  -->   3017  1083   312  49851
			'Geography.Regions.Europe.Southern Europe'      4333  -->   3349   984   292  49638
			'Geography.Regions.Europe.Western Europe'       4866  -->   3750  1116   394  49003
			'Geography.Regions.Oceania'                      719  -->    373   346    73  53471
			'History and Society.Business and economics'    3397  -->   2119  1278   283  50583
			'History and Society.Education'                 1855  -->   1162   693   133  52275
			'History and Society.History'                   5474  -->   3126  2348   708  48081
			'History and Society.Military and warfare'      3979  -->   2599  1380   473  49811
			'History and Society.Politics and government'   3682  -->   1948  1734   492  50089
			'History and Society.Society'                   4758  -->   1504  3254   315  49190
			'History and Society.Transportation'            2450  -->   2062   388   108  51705
			'STEM.Biology'                                  3017  -->   2354   663   195  51051
			'STEM.Chemistry'                                1678  -->   1415   263   109  52476
			'STEM.Computing'                                2112  -->   1778   334   152  51999
			'STEM.Earth and environment'                    1868  -->   1228   640   149  52246
			'STEM.Engineering'                              2661  -->   1970   691   214  51388
			'STEM.Libraries & Information'                   481  -->    372   109    23  53759
			'STEM.Mathematics'                               564  -->    459   105    24  53675
			'STEM.Medicine & Health'                        2061  -->   1501   560   152  52050
			'STEM.Physics'                                  1644  -->   1269   375   162  52457
			'STEM.STEM*'                                   16225  -->  14410  1815   914  37124
			'STEM.Space'                                    1943  -->   1824   119    34  52286
			'STEM.Technology'                               4192  -->   3149  1043   539  49532
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.284         0.13
		Culture.Biography.Women                         0.08          0.015
		Culture.Food and drink                          0.03          0.003
		Culture.Internet culture                        0.042         0.004
		Culture.Linguistics                             0.029         0.008
		Culture.Literature                              0.094         0.015
		Culture.Media.Books                             0.032         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.054         0.012
		Culture.Media.Media*                            0.233         0.056
		Culture.Media.Music                             0.06          0.021
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.039         0.009
		Culture.Media.Video games                       0.014         0.003
		Culture.Performing arts                         0.031         0.003
		Culture.Philosophy and religion                 0.069         0.011
		Culture.Sports                                  0.059         0.061
		Culture.Visual arts.Architecture                0.045         0.011
		Culture.Visual arts.Comics and Anime            0.019         0.002
		Culture.Visual arts.Fashion                     0.016         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.081         0.021
		Geography.Regions.Africa.Africa*                0.059         0.009
		Geography.Regions.Africa.Central Africa         0.007         0.001
		Geography.Regions.Africa.Eastern Africa         0.004         0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.02          0.004
		Geography.Regions.Americas.North America        0.104         0.064
		Geography.Regions.Americas.South America        0.03          0.007
		Geography.Regions.Asia.Asia*                    0.254         0.053
		Geography.Regions.Asia.Central Asia             0.016         0.001
		Geography.Regions.Asia.East Asia                0.045         0.012
		Geography.Regions.Asia.North Asia               0.094         0.006
		Geography.Regions.Asia.South Asia               0.032         0.017
		Geography.Regions.Asia.Southeast Asia           0.02          0.006
		Geography.Regions.Asia.West Asia                0.076         0.012
		Geography.Regions.Europe.Eastern Europe         0.12          0.019
		Geography.Regions.Europe.Europe*                0.348         0.082
		Geography.Regions.Europe.Northern Europe        0.076         0.029
		Geography.Regions.Europe.Southern Europe        0.08          0.014
		Geography.Regions.Europe.Western Europe         0.09          0.021
		Geography.Regions.Oceania                       0.013         0.005
		History and Society.Business and economics      0.063         0.01
		History and Society.Education                   0.034         0.008
		History and Society.History                     0.101         0.011
		History and Society.Military and warfare        0.073         0.016
		History and Society.Politics and government     0.068         0.017
		History and Society.Society                     0.088         0.008
		History and Society.Transportation              0.045         0.016
		STEM.Biology                                    0.056         0.035
		STEM.Chemistry                                  0.031         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.034         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.01          0
		STEM.Medicine & Health                          0.038         0.007
		STEM.Physics                                    0.03          0.001
		STEM.STEM*                                      0.299         0.066
		STEM.Space                                      0.036         0.004
		STEM.Technology                                 0.077         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.133
		Culture.Biography.Women                      0.02
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.013
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.053
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.025
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.074
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.013
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.016
		Geography.Regions.Europe.Eastern Europe      0.025
		Geography.Regions.Europe.Europe*             0.12
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.017
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.012
		History and Society.Education                0.008
		History and Society.History                  0.021
		History and Society.Military and warfare     0.019
		History and Society.Politics and government  0.018
		History and Society.Society                  0.009
		History and Society.Transportation           0.016
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.081
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.947
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.926
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.88
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.979
		History and Society.Military and warfare     0.981
		History and Society.Politics and government  0.982
		History and Society.Society                  0.991
		History and Society.Transportation           0.984
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.919
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.784, macro=0.73):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.9
		Culture.Biography.Women                      0.725
		Culture.Food and drink                       0.759
		Culture.Internet culture                     0.824
		Culture.Linguistics                          0.713
		Culture.Literature                           0.74
		Culture.Media.Books                          0.824
		Culture.Media.Entertainment                  0.458
		Culture.Media.Films                          0.881
		Culture.Media.Media*                         0.877
		Culture.Media.Music                          0.837
		Culture.Media.Radio                          0.758
		Culture.Media.Software                       0.921
		Culture.Media.Television                     0.821
		Culture.Media.Video games                    0.969
		Culture.Performing arts                      0.676
		Culture.Philosophy and religion              0.532
		Culture.Sports                               0.835
		Culture.Visual arts.Architecture             0.773
		Culture.Visual arts.Comics and Anime         0.844
		Culture.Visual arts.Fashion                  0.785
		Culture.Visual arts.Visual arts*             0.754
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.596
		Geography.Regions.Africa.Central Africa      0.671
		Geography.Regions.Africa.Eastern Africa      0.662
		Geography.Regions.Africa.Northern Africa     0.621
		Geography.Regions.Africa.Southern Africa     0.786
		Geography.Regions.Africa.Western Africa      0.679
		Geography.Regions.Americas.Central America   0.375
		Geography.Regions.Americas.North America     0.71
		Geography.Regions.Americas.South America     0.786
		Geography.Regions.Asia.Asia*                 0.822
		Geography.Regions.Asia.Central Asia          0.575
		Geography.Regions.Asia.East Asia             0.792
		Geography.Regions.Asia.North Asia            0.792
		Geography.Regions.Asia.South Asia            0.67
		Geography.Regions.Asia.Southeast Asia        0.39
		Geography.Regions.Asia.West Asia             0.767
		Geography.Regions.Europe.Eastern Europe      0.782
		Geography.Regions.Europe.Europe*             0.837
		Geography.Regions.Europe.Northern Europe     0.736
		Geography.Regions.Europe.Southern Europe     0.773
		Geography.Regions.Europe.Western Europe      0.771
		Geography.Regions.Oceania                    0.519
		History and Society.Business and economics   0.624
		History and Society.Education                0.626
		History and Society.History                  0.571
		History and Society.Military and warfare     0.653
		History and Society.Politics and government  0.529
		History and Society.Society                  0.316
		History and Society.Transportation           0.842
		STEM.Biology                                 0.78
		STEM.Chemistry                               0.843
		STEM.Computing                               0.842
		STEM.Earth and environment                   0.657
		STEM.Engineering                             0.74
		STEM.Libraries & Information                 0.773
		STEM.Mathematics                             0.814
		STEM.Medicine & Health                       0.728
		STEM.Physics                                 0.772
		STEM.STEM*                                   0.888
		STEM.Space                                   0.939
		STEM.Technology                              0.751
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.968
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.985
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.99
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.697, macro=0.588):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.551
		Culture.Food and drink                       0.49
		Culture.Internet culture                     0.509
		Culture.Linguistics                          0.815
		Culture.Literature                           0.535
		Culture.Media.Books                          0.629
		Culture.Media.Entertainment                  0.361
		Culture.Media.Films                          0.794
		Culture.Media.Media*                         0.649
		Culture.Media.Music                          0.806
		Culture.Media.Radio                          0.729
		Culture.Media.Software                       0.268
		Culture.Media.Television                     0.829
		Culture.Media.Video games                    0.885
		Culture.Performing arts                      0.479
		Culture.Philosophy and religion              0.451
		Culture.Sports                               0.963
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.695
		Culture.Visual arts.Fashion                  0.529
		Culture.Visual arts.Visual arts*             0.579
		Geography.Geographical                       0.582
		Geography.Regions.Africa.Africa*             0.561
		Geography.Regions.Africa.Central Africa      0.479
		Geography.Regions.Africa.Eastern Africa      0.271
		Geography.Regions.Africa.Northern Africa     0.309
		Geography.Regions.Africa.Southern Africa     0.667
		Geography.Regions.Africa.Western Africa      0.41
		Geography.Regions.Americas.Central America   0.574
		Geography.Regions.Americas.North America     0.741
		Geography.Regions.Americas.South America     0.799
		Geography.Regions.Asia.Asia*                 0.588
		Geography.Regions.Asia.Central Asia          0.3
		Geography.Regions.Asia.East Asia             0.798
		Geography.Regions.Asia.North Asia            0.343
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.691
		Geography.Regions.Asia.West Asia             0.557
		Geography.Regions.Europe.Eastern Europe      0.588
		Geography.Regions.Europe.Europe*             0.574
		Geography.Regions.Europe.Northern Europe     0.782
		Geography.Regions.Europe.Southern Europe     0.653
		Geography.Regions.Europe.Western Europe      0.672
		Geography.Regions.Oceania                    0.638
		History and Society.Business and economics   0.528
		History and Society.Education                0.667
		History and Society.History                  0.304
		History and Society.Military and warfare     0.523
		History and Society.Politics and government  0.478
		History and Society.Society                  0.296
		History and Society.Transportation           0.871
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.411
		STEM.Computing                               0.453
		STEM.Earth and environment                   0.527
		STEM.Engineering                             0.511
		STEM.Libraries & Information                 0.557
		STEM.Mathematics                             0.46
		STEM.Medicine & Health                       0.622
		STEM.Physics                                 0.192
		STEM.STEM*                                   0.723
		STEM.Space                                   0.862
		STEM.Technology                              0.268
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.73, macro=0.636):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.889
		Culture.Biography.Women                      0.627
		Culture.Food and drink                       0.595
		Culture.Internet culture                     0.629
		Culture.Linguistics                          0.76
		Culture.Literature                           0.621
		Culture.Media.Books                          0.714
		Culture.Media.Entertainment                  0.404
		Culture.Media.Films                          0.835
		Culture.Media.Media*                         0.746
		Culture.Media.Music                          0.821
		Culture.Media.Radio                          0.743
		Culture.Media.Software                       0.415
		Culture.Media.Television                     0.825
		Culture.Media.Video games                    0.925
		Culture.Performing arts                      0.561
		Culture.Philosophy and religion              0.488
		Culture.Sports                               0.894
		Culture.Visual arts.Architecture             0.697
		Culture.Visual arts.Comics and Anime         0.762
		Culture.Visual arts.Fashion                  0.632
		Culture.Visual arts.Visual arts*             0.655
		Geography.Geographical                       0.63
		Geography.Regions.Africa.Africa*             0.578
		Geography.Regions.Africa.Central Africa      0.559
		Geography.Regions.Africa.Eastern Africa      0.385
		Geography.Regions.Africa.Northern Africa     0.413
		Geography.Regions.Africa.Southern Africa     0.721
		Geography.Regions.Africa.Western Africa      0.511
		Geography.Regions.Americas.Central America   0.453
		Geography.Regions.Americas.North America     0.725
		Geography.Regions.Americas.South America     0.792
		Geography.Regions.Asia.Asia*                 0.685
		Geography.Regions.Asia.Central Asia          0.394
		Geography.Regions.Asia.East Asia             0.795
		Geography.Regions.Asia.North Asia            0.478
		Geography.Regions.Asia.South Asia            0.757
		Geography.Regions.Asia.Southeast Asia        0.498
		Geography.Regions.Asia.West Asia             0.646
		Geography.Regions.Europe.Eastern Europe      0.671
		Geography.Regions.Europe.Europe*             0.681
		Geography.Regions.Europe.Northern Europe     0.758
		Geography.Regions.Europe.Southern Europe     0.708
		Geography.Regions.Europe.Western Europe      0.718
		Geography.Regions.Oceania                    0.572
		History and Society.Business and economics   0.572
		History and Society.Education                0.646
		History and Society.History                  0.397
		History and Society.Military and warfare     0.581
		History and Society.Politics and government  0.502
		History and Society.Society                  0.306
		History and Society.Transportation           0.856
		STEM.Biology                                 0.828
		STEM.Chemistry                               0.553
		STEM.Computing                               0.589
		STEM.Earth and environment                   0.585
		STEM.Engineering                             0.605
		STEM.Libraries & Information                 0.647
		STEM.Mathematics                             0.588
		STEM.Medicine & Health                       0.671
		STEM.Physics                                 0.308
		STEM.STEM*                                   0.797
		STEM.Space                                   0.899
		STEM.Technology                              0.395
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.964
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.984
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.967
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.966
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.99
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.986
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.991
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.983
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.017
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.032
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.007
		Geography.Regions.Europe.Eastern Europe      0.01
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.015
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.01
		History and Society.Society                  0.006
		History and Society.Transportation           0.002
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.977
		Culture.Literature                           0.975
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.97
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.929
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.954
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.978
		Culture.Visual arts.Visual arts*             0.975
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.966
		Geography.Regions.Africa.Central Africa      0.967
		Geography.Regions.Africa.Eastern Africa      0.936
		Geography.Regions.Africa.Northern Africa     0.977
		Geography.Regions.Africa.Southern Africa     0.969
		Geography.Regions.Africa.Western Africa      0.895
		Geography.Regions.Americas.Central America   0.955
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.97
		Geography.Regions.Asia.East Asia             0.983
		Geography.Regions.Asia.North Asia            0.978
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.953
		Geography.Regions.Asia.West Asia             0.98
		Geography.Regions.Europe.Eastern Europe      0.975
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.965
		History and Society.Business and economics   0.969
		History and Society.Education                0.975
		History and Society.History                  0.951
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.955
		History and Society.Society                  0.908
		History and Society.Transportation           0.982
		STEM.Biology                                 0.98
		STEM.Chemistry                               0.988
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.965
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.979
		STEM.Space                                   0.992
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.78, macro=0.629):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.944
		Culture.Biography.Women                      0.628
		Culture.Food and drink                       0.619
		Culture.Internet culture                     0.624
		Culture.Linguistics                          0.787
		Culture.Literature                           0.688
		Culture.Media.Books                          0.76
		Culture.Media.Entertainment                  0.333
		Culture.Media.Films                          0.893
		Culture.Media.Media*                         0.862
		Culture.Media.Music                          0.876
		Culture.Media.Radio                          0.481
		Culture.Media.Software                       0.519
		Culture.Media.Television                     0.828
		Culture.Media.Video games                    0.916
		Culture.Performing arts                      0.55
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.722
		Culture.Visual arts.Fashion                  0.52
		Culture.Visual arts.Visual arts*             0.676
		Geography.Geographical                       0.648
		Geography.Regions.Africa.Africa*             0.556
		Geography.Regions.Africa.Central Africa      0.3
		Geography.Regions.Africa.Eastern Africa      0.154
		Geography.Regions.Africa.Northern Africa     0.298
		Geography.Regions.Africa.Southern Africa     0.59
		Geography.Regions.Africa.Western Africa      0.243
		Geography.Regions.Americas.Central America   0.369
		Geography.Regions.Americas.North America     0.774
		Geography.Regions.Americas.South America     0.836
		Geography.Regions.Asia.Asia*                 0.783
		Geography.Regions.Asia.Central Asia          0.262
		Geography.Regions.Asia.East Asia             0.837
		Geography.Regions.Asia.North Asia            0.567
		Geography.Regions.Asia.South Asia            0.809
		Geography.Regions.Asia.Southeast Asia        0.462
		Geography.Regions.Asia.West Asia             0.657
		Geography.Regions.Europe.Eastern Europe      0.747
		Geography.Regions.Europe.Europe*             0.789
		Geography.Regions.Europe.Northern Europe     0.812
		Geography.Regions.Europe.Southern Europe     0.766
		Geography.Regions.Europe.Western Europe      0.771
		Geography.Regions.Oceania                    0.502
		History and Society.Business and economics   0.549
		History and Society.Education                0.669
		History and Society.History                  0.394
		History and Society.Military and warfare     0.591
		History and Society.Politics and government  0.451
		History and Society.Society                  0.237
		History and Society.Transportation           0.9
		STEM.Biology                                 0.897
		STEM.Chemistry                               0.595
		STEM.Computing                               0.62
		STEM.Earth and environment                   0.584
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.508
		STEM.Mathematics                             0.575
		STEM.Medicine & Health                       0.689
		STEM.Physics                                 0.239
		STEM.STEM*                                   0.902
		STEM.Space                                   0.928
		STEM.Technology                              0.426
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}}}}}

