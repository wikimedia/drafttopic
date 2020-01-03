Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'learning_rate': 0.1, 'n_estimators': 150, 'max_leaf_nodes': None, 'scale': False, 'min_impurity_split': None, 'n_iter_no_change': None, 'criterion': 'friedman_mse', 'init': None, 'label_weights': {}, 'min_impurity_decrease': 0.0, 'random_state': None, 'subsample': 1.0, 'center': False, 'tol': 0.0001, 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'warm_start': False, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'loss': 'deviance', 'max_features': 'log2', 'verbose': 0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'max_depth': 5, 'presort': 'auto', 'population_rates': None}
	Environment:
	 - revscoring_version: '2.6.2-no_zero_vectors'
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
	counts (n=63017):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16717  -->  14347  2370  1197  45103
			'Culture.Biography.Women'                       4173  -->   1303  2870   560  58284
			'Culture.Food and drink'                        1323  -->    935   388    99  61595
			'Culture.Internet culture'                      2946  -->   2069   877   184  59887
			'Culture.Linguistics'                           1384  -->   1002   382   104  61529
			'Culture.Literature'                            5277  -->   3729  1548   609  57131
			'Culture.Media.Books'                           1919  -->   1291   628   208  60890
			'Culture.Media.Entertainment'                   1876  -->    636  1240   121  61020
			'Culture.Media.Films'                           2307  -->   1830   477   130  60580
			'Culture.Media.Media*'                         14363  -->  11840  2523  1857  46797
			'Culture.Media.Music'                           2677  -->   2136   541   323  60017
			'Culture.Media.Radio'                           1174  -->    929   245    58  61785
			'Culture.Media.Software'                        1798  -->    909   889   416  60803
			'Culture.Media.Television'                      2200  -->   1384   816   249  60568
			'Culture.Media.Video games'                     2078  -->   1746   332    51  60888
			'Culture.Performing arts'                       1334  -->    811   523   118  61565
			'Culture.Philosophy and religion'               2638  -->   1197  1441   337  60042
			'Culture.Sports'                                5843  -->   5176   667   399  56775
			'Culture.Visual arts.Architecture'              2565  -->   1784   781   344  60108
			'Culture.Visual arts.Comics and Anime'          1488  -->    931   557   125  61404
			'Culture.Visual arts.Fashion'                   1188  -->    782   406    98  61731
			'Culture.Visual arts.Visual arts*'              5987  -->   3841  2146   672  56358
			'Geography.Geographical'                        3344  -->   1981  1363   320  59353
			'Geography.Regions.Africa.Africa*'              5693  -->    977  4716   330  56994
			'Geography.Regions.Africa.Central Africa'         28  -->      0    28   118  62871
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    171   943    68  61835
			'Geography.Regions.Africa.Northern Africa'      1266  -->    107  1159    86  61665
			'Geography.Regions.Africa.Southern Africa'      1288  -->    219  1069    87  61642
			'Geography.Regions.Africa.Western Africa'       1152  -->    138  1014    73  61792
			'Geography.Regions.Americas.Central America'    1326  -->     49  1277   102  61589
			'Geography.Regions.Americas.North America'      7565  -->   2627  4938   515  54937
			'Geography.Regions.Americas.South America'      1523  -->    223  1300   182  61312
			'Geography.Regions.Asia.Asia*'                 11060  -->   3358  7702   741  51216
			'Geography.Regions.Asia.Central Asia'           1163  -->    165   998    89  61765
			'Geography.Regions.Asia.East Asia'              2721  -->    479  2242   130  60166
			'Geography.Regions.Asia.North Asia'             1361  -->    167  1194    77  61579
			'Geography.Regions.Asia.South Asia'             2438  -->    568  1870    97  60482
			'Geography.Regions.Asia.Southeast Asia'         1688  -->     70  1618    54  61275
			'Geography.Regions.Asia.West Asia'              2264  -->    905  1359    75  60678
			'Geography.Regions.Europe.Eastern Europe'       3083  -->    646  2437   105  59829
			'Geography.Regions.Europe.Europe*'             12415  -->   3786  8629  1185  49417
			'Geography.Regions.Europe.Northern Europe'      4244  -->    542  3702   139  58634
			'Geography.Regions.Europe.Southern Europe'      2320  -->    335  1985   131  60566
			'Geography.Regions.Europe.Western Europe'       3160  -->    706  2454   270  59587
			'Geography.Regions.Oceania'                     2537  -->    287  2250    94  60386
			'History and Society.Business and economics'    3430  -->   1617  1813   593  58994
			'History and Society.Education'                 2178  -->   1042  1136   234  60605
			'History and Society.History'                   3217  -->    794  2423   369  59431
			'History and Society.Military and warfare'      3977  -->   2144  1833   359  58681
			'History and Society.Politics and government'   4647  -->   1320  3327   491  57879
			'History and Society.Society'                   4057  -->    551  3506   181  58779
			'History and Society.Transportation'            3604  -->   2946   658   266  59147
			'STEM.Biology'                                  2834  -->   2240   594   161  60022
			'STEM.Chemistry'                                1344  -->    898   446   191  61482
			'STEM.Computing'                                2011  -->   1241   770   447  60559
			'STEM.Earth and environment'                    1683  -->   1017   666   144  61190
			'STEM.Engineering'                              2272  -->   1448   824   170  60575
			'STEM.Libraries & Information'                  1159  -->    569   590    92  61766
			'STEM.Mathematics'                              1121  -->    689   432   127  61769
			'STEM.Medicine & Health'                        1737  -->   1109   628   206  61074
			'STEM.Physics'                                  1206  -->    756   450   203  61608
			'STEM.STEM*'                                   16499  -->  13712  2787  1293  45225
			'STEM.Space'                                    1398  -->   1122   276    46  61573
			'STEM.Technology'                               3712  -->   1917  1795   759  58546
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.265         0.123
		Culture.Biography.Women                         0.066         0.015
		Culture.Food and drink                          0.021         0.002
		Culture.Internet culture                        0.047         0.004
		Culture.Linguistics                             0.022         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.03          0.004
		Culture.Media.Films                             0.037         0.011
		Culture.Media.Media*                            0.228         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.019         0.002
		Culture.Media.Software                          0.029         0.001
		Culture.Media.Television                        0.035         0.009
		Culture.Media.Video games                       0.033         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.093         0.071
		Culture.Visual arts.Architecture                0.041         0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.053         0.024
		Geography.Regions.Africa.Africa*                0.09          0.008
		Geography.Regions.Africa.Central Africa         0             0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.02          0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.12          0.064
		Geography.Regions.Americas.South America        0.024         0.006
		Geography.Regions.Asia.Asia*                    0.176         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.036         0.011
		Geography.Regions.Europe.Eastern Europe         0.049         0.013
		Geography.Regions.Europe.Europe*                0.197         0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.037         0.013
		Geography.Regions.Europe.Western Europe         0.05          0.019
		Geography.Regions.Oceania                       0.04          0.015
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.035         0.007
		History and Society.History                     0.051         0.011
		History and Society.Military and warfare        0.063         0.014
		History and Society.Politics and government     0.074         0.028
		History and Society.Society                     0.064         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.028         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.262         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.059         0.005
	match_rate (micro=0.044, macro=0.014):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.128
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.084
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.031
		Geography.Regions.Americas.South America     0.004
		Geography.Regions.Asia.Asia*                 0.027
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.005
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.006
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.045
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.015
		History and Society.Education                0.007
		History and Society.History                  0.009
		History and Society.Military and warfare     0.014
		History and Society.Politics and government  0.016
		History and Society.Society                  0.005
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.956, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.916
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.955
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.985
		History and Society.Education                0.993
		History and Society.History                  0.991
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.984
		History and Society.Society                  0.995
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.558, macro=0.468):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.858
		Culture.Biography.Women                      0.312
		Culture.Food and drink                       0.707
		Culture.Internet culture                     0.702
		Culture.Linguistics                          0.724
		Culture.Literature                           0.707
		Culture.Media.Books                          0.673
		Culture.Media.Entertainment                  0.339
		Culture.Media.Films                          0.793
		Culture.Media.Media*                         0.824
		Culture.Media.Music                          0.798
		Culture.Media.Radio                          0.791
		Culture.Media.Software                       0.506
		Culture.Media.Television                     0.629
		Culture.Media.Video games                    0.84
		Culture.Performing arts                      0.608
		Culture.Philosophy and religion              0.454
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.696
		Culture.Visual arts.Comics and Anime         0.626
		Culture.Visual arts.Fashion                  0.658
		Culture.Visual arts.Visual arts*             0.642
		Geography.Geographical                       0.592
		Geography.Regions.Africa.Africa*             0.172
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.154
		Geography.Regions.Africa.Northern Africa     0.085
		Geography.Regions.Africa.Southern Africa     0.17
		Geography.Regions.Africa.Western Africa      0.12
		Geography.Regions.Americas.Central America   0.037
		Geography.Regions.Americas.North America     0.347
		Geography.Regions.Americas.South America     0.146
		Geography.Regions.Asia.Asia*                 0.304
		Geography.Regions.Asia.Central Asia          0.142
		Geography.Regions.Asia.East Asia             0.176
		Geography.Regions.Asia.North Asia            0.123
		Geography.Regions.Asia.South Asia            0.233
		Geography.Regions.Asia.Southeast Asia        0.041
		Geography.Regions.Asia.West Asia             0.4
		Geography.Regions.Europe.Eastern Europe      0.21
		Geography.Regions.Europe.Europe*             0.305
		Geography.Regions.Europe.Northern Europe     0.128
		Geography.Regions.Europe.Southern Europe     0.144
		Geography.Regions.Europe.Western Europe      0.223
		Geography.Regions.Oceania                    0.113
		History and Society.Business and economics   0.471
		History and Society.Education                0.478
		History and Society.History                  0.247
		History and Society.Military and warfare     0.539
		History and Society.Politics and government  0.284
		History and Society.Society                  0.136
		History and Society.Transportation           0.817
		STEM.Biology                                 0.79
		STEM.Chemistry                               0.668
		STEM.Computing                               0.617
		STEM.Earth and environment                   0.604
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.491
		STEM.Mathematics                             0.615
		STEM.Medicine & Health                       0.638
		STEM.Physics                                 0.627
		STEM.STEM*                                   0.831
		STEM.Space                                   0.803
		STEM.Technology                              0.516
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.991
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.999
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.998
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.99
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.997
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.63, macro=0.449):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.823
		Culture.Biography.Women                      0.327
		Culture.Food and drink                       0.521
		Culture.Internet culture                     0.446
		Culture.Linguistics                          0.76
		Culture.Literature                           0.513
		Culture.Media.Books                          0.444
		Culture.Media.Entertainment                  0.381
		Culture.Media.Films                          0.798
		Culture.Media.Media*                         0.573
		Culture.Media.Music                          0.785
		Culture.Media.Radio                          0.646
		Culture.Media.Software                       0.09
		Culture.Media.Television                     0.578
		Culture.Media.Video games                    0.725
		Culture.Performing arts                      0.479
		Culture.Philosophy and religion              0.467
		Culture.Sports                               0.907
		Culture.Visual arts.Architecture             0.566
		Culture.Visual arts.Comics and Anime         0.404
		Culture.Visual arts.Fashion                  0.252
		Culture.Visual arts.Visual arts*             0.504
		Geography.Geographical                       0.727
		Geography.Regions.Africa.Africa*             0.19
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.06
		Geography.Regions.Africa.Northern Africa     0.069
		Geography.Regions.Africa.Southern Africa     0.124
		Geography.Regions.Africa.Western Africa      0.065
		Geography.Regions.Americas.Central America   0.069
		Geography.Regions.Americas.North America     0.72
		Geography.Regions.Americas.South America     0.239
		Geography.Regions.Asia.Asia*                 0.504
		Geography.Regions.Asia.Central Asia          0.079
		Geography.Regions.Asia.East Asia             0.485
		Geography.Regions.Asia.North Asia            0.083
		Geography.Regions.Asia.South Asia            0.692
		Geography.Regions.Asia.Southeast Asia        0.222
		Geography.Regions.Asia.West Asia             0.781
		Geography.Regions.Europe.Eastern Europe      0.609
		Geography.Regions.Europe.Europe*             0.518
		Geography.Regions.Europe.Northern Europe     0.63
		Geography.Regions.Europe.Southern Europe     0.469
		Geography.Regions.Europe.Western Europe      0.492
		Geography.Regions.Oceania                    0.528
		History and Society.Business and economics   0.326
		History and Society.Education                0.48
		History and Society.History                  0.305
		History and Society.Military and warfare     0.559
		History and Society.Politics and government  0.495
		History and Society.Society                  0.361
		History and Society.Transportation           0.737
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.252
		STEM.Computing                               0.185
		STEM.Earth and environment                   0.54
		STEM.Engineering                             0.545
		STEM.Libraries & Information                 0.17
		STEM.Mathematics                             0.111
		STEM.Medicine & Health                       0.55
		STEM.Physics                                 0.14
		STEM.STEM*                                   0.69
		STEM.Space                                   0.867
		STEM.Technology                              0.172
		-------------------------------------------  -----
	!precision (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.945
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.985
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.979
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=None, macro=None):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.84
		Culture.Biography.Women                      0.319
		Culture.Food and drink                       0.6
		Culture.Internet culture                     0.546
		Culture.Linguistics                          0.742
		Culture.Literature                           0.595
		Culture.Media.Books                          0.535
		Culture.Media.Entertainment                  0.359
		Culture.Media.Films                          0.795
		Culture.Media.Media*                         0.676
		Culture.Media.Music                          0.791
		Culture.Media.Radio                          0.711
		Culture.Media.Software                       0.153
		Culture.Media.Television                     0.602
		Culture.Media.Video games                    0.778
		Culture.Performing arts                      0.536
		Culture.Philosophy and religion              0.46
		Culture.Sports                               0.896
		Culture.Visual arts.Architecture             0.624
		Culture.Visual arts.Comics and Anime         0.491
		Culture.Visual arts.Fashion                  0.364
		Culture.Visual arts.Visual arts*             0.564
		Geography.Geographical                       0.653
		Geography.Regions.Africa.Africa*             0.18
		Geography.Regions.Africa.Central Africa
		Geography.Regions.Africa.Eastern Africa      0.086
		Geography.Regions.Africa.Northern Africa     0.076
		Geography.Regions.Africa.Southern Africa     0.144
		Geography.Regions.Africa.Western Africa      0.084
		Geography.Regions.Americas.Central America   0.048
		Geography.Regions.Americas.North America     0.469
		Geography.Regions.Americas.South America     0.182
		Geography.Regions.Asia.Asia*                 0.379
		Geography.Regions.Asia.Central Asia          0.101
		Geography.Regions.Asia.East Asia             0.258
		Geography.Regions.Asia.North Asia            0.099
		Geography.Regions.Asia.South Asia            0.349
		Geography.Regions.Asia.Southeast Asia        0.07
		Geography.Regions.Asia.West Asia             0.529
		Geography.Regions.Europe.Eastern Europe      0.312
		Geography.Regions.Europe.Europe*             0.384
		Geography.Regions.Europe.Northern Europe     0.212
		Geography.Regions.Europe.Southern Europe     0.221
		Geography.Regions.Europe.Western Europe      0.307
		Geography.Regions.Oceania                    0.186
		History and Society.Business and economics   0.385
		History and Society.Education                0.479
		History and Society.History                  0.273
		History and Society.Military and warfare     0.549
		History and Society.Politics and government  0.361
		History and Society.Society                  0.197
		History and Society.Transportation           0.775
		STEM.Biology                                 0.847
		STEM.Chemistry                               0.366
		STEM.Computing                               0.285
		STEM.Earth and environment                   0.57
		STEM.Engineering                             0.588
		STEM.Libraries & Information                 0.253
		STEM.Mathematics                             0.188
		STEM.Medicine & Health                       0.591
		STEM.Physics                                 0.228
		STEM.STEM*                                   0.754
		STEM.Space                                   0.833
		STEM.Technology                              0.258
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.977
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.973
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.985
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.971, macro=0.988):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.954
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.925
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.972
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.026
		Culture.Biography.Women                      0.01
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.038
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.006
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.012
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.001
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.009
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.014
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.001
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.001
		Geography.Regions.Europe.Eastern Europe      0.002
		Geography.Regions.Europe.Europe*             0.023
		Geography.Regions.Europe.Northern Europe     0.002
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.005
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.01
		History and Society.Education                0.004
		History and Society.History                  0.006
		History and Society.Military and warfare     0.006
		History and Society.Politics and government  0.008
		History and Society.Society                  0.003
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.932, macro=0.931):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.94
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.972
		Culture.Literature                           0.973
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.958
		Culture.Media.Films                          0.982
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.986
		Culture.Media.Software                       0.977
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.979
		Culture.Philosophy and religion              0.948
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.981
		Culture.Visual arts.Fashion                  0.981
		Culture.Visual arts.Visual arts*             0.963
		Geography.Geographical                       0.961
		Geography.Regions.Africa.Africa*             0.869
		Geography.Regions.Africa.Central Africa      0.533
		Geography.Regions.Africa.Eastern Africa      0.897
		Geography.Regions.Africa.Northern Africa     0.878
		Geography.Regions.Africa.Southern Africa     0.872
		Geography.Regions.Africa.Western Africa      0.902
		Geography.Regions.Americas.Central America   0.852
		Geography.Regions.Americas.North America     0.89
		Geography.Regions.Americas.South America     0.894
		Geography.Regions.Asia.Asia*                 0.863
		Geography.Regions.Asia.Central Asia          0.897
		Geography.Regions.Asia.East Asia             0.872
		Geography.Regions.Asia.North Asia            0.922
		Geography.Regions.Asia.South Asia            0.9
		Geography.Regions.Asia.Southeast Asia        0.821
		Geography.Regions.Asia.West Asia             0.902
		Geography.Regions.Europe.Eastern Europe      0.895
		Geography.Regions.Europe.Europe*             0.85
		Geography.Regions.Europe.Northern Europe     0.844
		Geography.Regions.Europe.Southern Europe     0.871
		Geography.Regions.Europe.Western Europe      0.891
		Geography.Regions.Oceania                    0.863
		History and Society.Business and economics   0.956
		History and Society.Education                0.957
		History and Society.History                  0.914
		History and Society.Military and warfare     0.95
		History and Society.Politics and government  0.887
		History and Society.Society                  0.839
		History and Society.Transportation           0.984
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.986
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.973
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.968
		STEM.Space                                   0.99
		STEM.Technology                              0.96
		-------------------------------------------  -----
	pr_auc (micro=0.598, macro=0.421):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.247
		Culture.Food and drink                       0.603
		Culture.Internet culture                     0.686
		Culture.Linguistics                          0.722
		Culture.Literature                           0.665
		Culture.Media.Books                          0.524
		Culture.Media.Entertainment                  0.313
		Culture.Media.Films                          0.817
		Culture.Media.Media*                         0.783
		Culture.Media.Music                          0.832
		Culture.Media.Radio                          0.817
		Culture.Media.Software                       0.085
		Culture.Media.Television                     0.607
		Culture.Media.Video games                    0.86
		Culture.Performing arts                      0.524
		Culture.Philosophy and religion              0.37
		Culture.Sports                               0.925
		Culture.Visual arts.Architecture             0.667
		Culture.Visual arts.Comics and Anime         0.48
		Culture.Visual arts.Fashion                  0.262
		Culture.Visual arts.Visual arts*             0.575
		Geography.Geographical                       0.679
		Geography.Regions.Africa.Africa*             0.12
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.049
		Geography.Regions.Africa.Northern Africa     0.021
		Geography.Regions.Africa.Southern Africa     0.057
		Geography.Regions.Africa.Western Africa      0.02
		Geography.Regions.Americas.Central America   0.031
		Geography.Regions.Americas.North America     0.542
		Geography.Regions.Americas.South America     0.118
		Geography.Regions.Asia.Asia*                 0.404
		Geography.Regions.Asia.Central Asia          0.031
		Geography.Regions.Asia.East Asia             0.25
		Geography.Regions.Asia.North Asia            0.031
		Geography.Regions.Asia.South Asia            0.366
		Geography.Regions.Asia.Southeast Asia        0.048
		Geography.Regions.Asia.West Asia             0.497
		Geography.Regions.Europe.Eastern Europe      0.315
		Geography.Regions.Europe.Europe*             0.42
		Geography.Regions.Europe.Northern Europe     0.273
		Geography.Regions.Europe.Southern Europe     0.201
		Geography.Regions.Europe.Western Europe      0.315
		Geography.Regions.Oceania                    0.21
		History and Society.Business and economics   0.306
		History and Society.Education                0.425
		History and Society.History                  0.196
		History and Society.Military and warfare     0.555
		History and Society.Politics and government  0.356
		History and Society.Society                  0.171
		History and Society.Transportation           0.816
		STEM.Biology                                 0.895
		STEM.Chemistry                               0.428
		STEM.Computing                               0.228
		STEM.Earth and environment                   0.553
		STEM.Engineering                             0.596
		STEM.Libraries & Information                 0.273
		STEM.Mathematics                             0.195
		STEM.Medicine & Health                       0.555
		STEM.Physics                                 0.209
		STEM.STEM*                                   0.836
		STEM.Space                                   0.891
		STEM.Technology                              0.218
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'Culture.Internet culture': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}}, 'title': 'Scikit learn-based classifier score with probability'}

