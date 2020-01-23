Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'population_rates': None, 'max_depth': 5, 'max_leaf_nodes': None, 'n_estimators': 150, 'min_samples_leaf': 1, 'init': None, 'tol': 0.0001, 'loss': 'deviance', 'random_state': None, 'warm_start': False, 'center': False, 'max_features': 'log2', 'subsample': 1.0, 'verbose': 0, 'validation_fraction': 0.1, 'min_samples_split': 2, 'n_iter_no_change': None, 'min_impurity_decrease': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'learning_rate': 0.1, 'scale': False, 'min_impurity_split': None, 'min_weight_fraction_leaf': 0.0, 'multilabel': True, 'criterion': 'friedman_mse', 'presort': 'auto', 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.6.4-mmap'
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
	counts (n=59658):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16433  -->  15136  1297   826  42399
			'Culture.Biography.Women'                       4279  -->   3697   582   299  55080
			'Culture.Food and drink'                        1599  -->   1317   282    89  57970
			'Culture.Internet culture'                      3200  -->   2814   386   191  56267
			'Culture.Linguistics'                           1607  -->   1282   325    82  57969
			'Culture.Literature'                            5032  -->   3895  1137   414  54212
			'Culture.Media.Books'                           1699  -->   1441   258    89  57870
			'Culture.Media.Entertainment'                   2282  -->   1387   895   214  57162
			'Culture.Media.Films'                           2531  -->   2146   385    94  57033
			'Culture.Media.Media*'                         14310  -->  12794  1516  1205  44143
			'Culture.Media.Music'                           3319  -->   2890   429   322  56017
			'Culture.Media.Radio'                            424  -->    266   158    44  59190
			'Culture.Media.Software'                        2394  -->   2007   387   334  56930
			'Culture.Media.Television'                      2521  -->   2166   355   105  57032
			'Culture.Media.Video games'                     1891  -->   1783   108    31  57736
			'Culture.Performing arts'                       1489  -->   1074   415   116  58053
			'Culture.Philosophy and religion'               4421  -->   2750  1671   440  54797
			'Culture.Sports'                                5663  -->   5065   598   213  53782
			'Culture.Visual arts.Architecture'              2283  -->   1759   524   216  57159
			'Culture.Visual arts.Comics and Anime'          1695  -->   1525   170    28  57935
			'Culture.Visual arts.Fashion'                   1063  -->    845   218    51  58544
			'Culture.Visual arts.Visual arts*'              5896  -->   4677  1219   398  53364
			'Geography.Geographical'                        4621  -->   3420  1201   701  54336
			'Geography.Regions.Africa.Africa*'              3696  -->   2679  1017   220  55742
			'Geography.Regions.Africa.Central Africa'         31  -->      8    23    15  59612
			'Geography.Regions.Africa.Eastern Africa'        471  -->    335   136    41  59146
			'Geography.Regions.Africa.Northern Africa'      1548  -->   1072   476    97  58013
			'Geography.Regions.Africa.Southern Africa'       677  -->    422   255    34  58947
			'Geography.Regions.Africa.Western Africa'        194  -->     99    95    38  59426
			'Geography.Regions.Americas.Central America'    1360  -->    933   427    53  58245
			'Geography.Regions.Americas.North America'      6003  -->   3823  2180   874  52781
			'Geography.Regions.Americas.South America'      1502  -->   1052   450    75  58081
			'Geography.Regions.Asia.Asia*'                 10850  -->   8822  2028   824  47984
			'Geography.Regions.Asia.Central Asia'           1352  -->    985   367    69  58237
			'Geography.Regions.Asia.East Asia'              2943  -->   2269   674   172  56543
			'Geography.Regions.Asia.North Asia'             1967  -->   1400   567   263  57428
			'Geography.Regions.Asia.South Asia'             1843  -->   1404   439    78  57737
			'Geography.Regions.Asia.Southeast Asia'         1643  -->   1183   460    65  57950
			'Geography.Regions.Asia.West Asia'              2881  -->   2281   600   185  56592
			'Geography.Regions.Europe.Eastern Europe'       5297  -->   3902  1395   631  53730
			'Geography.Regions.Europe.Europe*'             16868  -->  13483  3385  2410  40380
			'Geography.Regions.Europe.Northern Europe'      4065  -->   2661  1404   406  55187
			'Geography.Regions.Europe.Southern Europe'      3540  -->   2410  1130   312  55806
			'Geography.Regions.Europe.Western Europe'       5074  -->   3692  1382   575  54009
			'Geography.Regions.Oceania'                     1769  -->   1197   572    85  57804
			'History and Society.Business and economics'    3605  -->   2300  1305   333  55720
			'History and Society.Education'                 1828  -->   1081   747   127  57703
			'History and Society.History'                   5571  -->   3641  1930   663  53424
			'History and Society.Military and warfare'      5707  -->   4173  1534   564  53387
			'History and Society.Politics and government'   4760  -->   2792  1968   519  54379
			'History and Society.Society'                   6846  -->   3561  3285   642  52170
			'History and Society.Transportation'            4252  -->   3906   346   182  55224
			'STEM.Biology'                                  3739  -->   3178   561   175  55744
			'STEM.Chemistry'                                1549  -->   1327   222   118  57991
			'STEM.Computing'                                2872  -->   2511   361   338  56448
			'STEM.Earth and environment'                    2183  -->   1669   514   141  57334
			'STEM.Engineering'                              2974  -->   2379   595   208  56476
			'STEM.Libraries & Information'                   720  -->    511   209    41  58897
			'STEM.Mathematics'                              1210  -->   1052   158    56  58392
			'STEM.Medicine & Health'                        2017  -->   1523   494   169  57472
			'STEM.Physics'                                  1499  -->   1195   304   130  58029
			'STEM.STEM*'                                   18910  -->  17008  1902   909  39839
			'STEM.Space'                                    2041  -->   1932   109    43  57574
			'STEM.Technology'                               5221  -->   4137  1084   651  53786
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.275         0.123
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.027         0.002
		Culture.Internet culture                        0.054         0.004
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.24          0.059
		Culture.Media.Music                             0.056         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.074         0.011
		Culture.Sports                                  0.095         0.071
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.099         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.062         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.101         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.182         0.046
		Geography.Regions.Asia.Central Asia             0.023         0.001
		Geography.Regions.Asia.East Asia                0.049         0.011
		Geography.Regions.Asia.North Asia               0.033         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.028         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.089         0.013
		Geography.Regions.Europe.Europe*                0.283         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.059         0.013
		Geography.Regions.Europe.Western Europe         0.085         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.06          0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.096         0.014
		History and Society.Politics and government     0.08          0.028
		History and Society.Society                     0.115         0.013
		History and Society.Transportation              0.071         0.015
		STEM.Biology                                    0.063         0.034
		STEM.Chemistry                                  0.026         0.002
		STEM.Computing                                  0.048         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.317         0.069
		STEM.Space                                      0.034         0.006
		STEM.Technology                                 0.088         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.018
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.077
		Culture.Media.Music                          0.026
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.015
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.03
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.113
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.007
		History and Society.History                  0.019
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.026
		History and Society.Society                  0.019
		History and Society.Transportation           0.017
		STEM.Biology                                 0.032
		STEM.Chemistry                               0.003
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.016
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.923
		Culture.Media.Music                          0.974
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.985
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.887
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.981
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.974
		History and Society.Society                  0.981
		History and Society.Transportation           0.983
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.984
		-------------------------------------------  -----
	recall (micro=0.798, macro=0.755):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.921
		Culture.Biography.Women                      0.864
		Culture.Food and drink                       0.824
		Culture.Internet culture                     0.879
		Culture.Linguistics                          0.798
		Culture.Literature                           0.774
		Culture.Media.Books                          0.848
		Culture.Media.Entertainment                  0.608
		Culture.Media.Films                          0.848
		Culture.Media.Media*                         0.894
		Culture.Media.Music                          0.871
		Culture.Media.Radio                          0.627
		Culture.Media.Software                       0.838
		Culture.Media.Television                     0.859
		Culture.Media.Video games                    0.943
		Culture.Performing arts                      0.721
		Culture.Philosophy and religion              0.622
		Culture.Sports                               0.894
		Culture.Visual arts.Architecture             0.77
		Culture.Visual arts.Comics and Anime         0.9
		Culture.Visual arts.Fashion                  0.795
		Culture.Visual arts.Visual arts*             0.793
		Geography.Geographical                       0.74
		Geography.Regions.Africa.Africa*             0.725
		Geography.Regions.Africa.Central Africa      0.258
		Geography.Regions.Africa.Eastern Africa      0.711
		Geography.Regions.Africa.Northern Africa     0.693
		Geography.Regions.Africa.Southern Africa     0.623
		Geography.Regions.Africa.Western Africa      0.51
		Geography.Regions.Americas.Central America   0.686
		Geography.Regions.Americas.North America     0.637
		Geography.Regions.Americas.South America     0.7
		Geography.Regions.Asia.Asia*                 0.813
		Geography.Regions.Asia.Central Asia          0.729
		Geography.Regions.Asia.East Asia             0.771
		Geography.Regions.Asia.North Asia            0.712
		Geography.Regions.Asia.South Asia            0.762
		Geography.Regions.Asia.Southeast Asia        0.72
		Geography.Regions.Asia.West Asia             0.792
		Geography.Regions.Europe.Eastern Europe      0.737
		Geography.Regions.Europe.Europe*             0.799
		Geography.Regions.Europe.Northern Europe     0.655
		Geography.Regions.Europe.Southern Europe     0.681
		Geography.Regions.Europe.Western Europe      0.728
		Geography.Regions.Oceania                    0.677
		History and Society.Business and economics   0.638
		History and Society.Education                0.591
		History and Society.History                  0.654
		History and Society.Military and warfare     0.731
		History and Society.Politics and government  0.587
		History and Society.Society                  0.52
		History and Society.Transportation           0.919
		STEM.Biology                                 0.85
		STEM.Chemistry                               0.857
		STEM.Computing                               0.874
		STEM.Earth and environment                   0.765
		STEM.Engineering                             0.8
		STEM.Libraries & Information                 0.71
		STEM.Mathematics                             0.869
		STEM.Medicine & Health                       0.755
		STEM.Physics                                 0.797
		STEM.STEM*                                   0.899
		STEM.Space                                   0.947
		STEM.Technology                              0.792
		-------------------------------------------  -----
	!recall (micro=0.985, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.988
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.991
		History and Society.Society                  0.988
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.713, macro=0.585):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.703
		Culture.Food and drink                       0.57
		Culture.Internet culture                     0.477
		Culture.Linguistics                          0.807
		Culture.Literature                           0.617
		Culture.Media.Books                          0.691
		Culture.Media.Entertainment                  0.369
		Culture.Media.Films                          0.846
		Culture.Media.Media*                         0.677
		Culture.Media.Music                          0.789
		Culture.Media.Radio                          0.646
		Culture.Media.Software                       0.161
		Culture.Media.Television                     0.806
		Culture.Media.Video games                    0.822
		Culture.Performing arts                      0.512
		Culture.Philosophy and religion              0.457
		Culture.Sports                               0.946
		Culture.Visual arts.Architecture             0.686
		Culture.Visual arts.Comics and Anime         0.804
		Culture.Visual arts.Fashion                  0.425
		Culture.Visual arts.Visual arts*             0.666
		Geography.Geographical                       0.584
		Geography.Regions.Africa.Africa*             0.592
		Geography.Regions.Africa.Central Africa      0.004
		Geography.Regions.Africa.Eastern Africa      0.319
		Geography.Regions.Africa.Northern Africa     0.338
		Geography.Regions.Africa.Southern Africa     0.56
		Geography.Regions.Africa.Western Africa      0.353
		Geography.Regions.Americas.Central America   0.714
		Geography.Regions.Americas.North America     0.729
		Geography.Regions.Americas.South America     0.775
		Geography.Regions.Asia.Asia*                 0.697
		Geography.Regions.Asia.Central Asia          0.348
		Geography.Regions.Asia.East Asia             0.746
		Geography.Regions.Asia.North Asia            0.126
		Geography.Regions.Asia.South Asia            0.897
		Geography.Regions.Asia.Southeast Asia        0.795
		Geography.Regions.Asia.West Asia             0.728
		Geography.Regions.Europe.Eastern Europe      0.452
		Geography.Regions.Europe.Europe*             0.539
		Geography.Regions.Europe.Northern Europe     0.739
		Geography.Regions.Europe.Southern Europe     0.618
		Geography.Regions.Europe.Western Europe      0.575
		Geography.Regions.Oceania                    0.876
		History and Society.Business and economics   0.523
		History and Society.Education                0.666
		History and Society.History                  0.369
		History and Society.Military and warfare     0.5
		History and Society.Politics and government  0.643
		History and Society.Society                  0.354
		History and Society.Transportation           0.811
		STEM.Biology                                 0.904
		STEM.Chemistry                               0.397
		STEM.Computing                               0.284
		STEM.Earth and environment                   0.587
		STEM.Engineering                             0.534
		STEM.Libraries & Information                 0.388
		STEM.Mathematics                             0.275
		STEM.Medicine & Health                       0.624
		STEM.Physics                                 0.233
		STEM.STEM*                                   0.75
		STEM.Space                                   0.885
		STEM.Technology                              0.255
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.998
		Culture.Food and drink                       1
		Culture.Internet culture                     1
		Culture.Linguistics                          0.999
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
		Geography.Regions.Europe.Western Europe      0.995
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
	f1 (micro=0.746, macro=0.638):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.775
		Culture.Food and drink                       0.674
		Culture.Internet culture                     0.619
		Culture.Linguistics                          0.802
		Culture.Literature                           0.686
		Culture.Media.Books                          0.761
		Culture.Media.Entertainment                  0.46
		Culture.Media.Films                          0.847
		Culture.Media.Media*                         0.77
		Culture.Media.Music                          0.828
		Culture.Media.Radio                          0.637
		Culture.Media.Software                       0.27
		Culture.Media.Television                     0.832
		Culture.Media.Video games                    0.878
		Culture.Performing arts                      0.599
		Culture.Philosophy and religion              0.527
		Culture.Sports                               0.919
		Culture.Visual arts.Architecture             0.726
		Culture.Visual arts.Comics and Anime         0.849
		Culture.Visual arts.Fashion                  0.554
		Culture.Visual arts.Visual arts*             0.724
		Geography.Geographical                       0.653
		Geography.Regions.Africa.Africa*             0.652
		Geography.Regions.Africa.Central Africa      0.008
		Geography.Regions.Africa.Eastern Africa      0.44
		Geography.Regions.Africa.Northern Africa     0.454
		Geography.Regions.Africa.Southern Africa     0.59
		Geography.Regions.Africa.Western Africa      0.418
		Geography.Regions.Americas.Central America   0.7
		Geography.Regions.Americas.North America     0.68
		Geography.Regions.Americas.South America     0.736
		Geography.Regions.Asia.Asia*                 0.75
		Geography.Regions.Asia.Central Asia          0.471
		Geography.Regions.Asia.East Asia             0.758
		Geography.Regions.Asia.North Asia            0.214
		Geography.Regions.Asia.South Asia            0.824
		Geography.Regions.Asia.Southeast Asia        0.756
		Geography.Regions.Asia.West Asia             0.759
		Geography.Regions.Europe.Eastern Europe      0.56
		Geography.Regions.Europe.Europe*             0.644
		Geography.Regions.Europe.Northern Europe     0.694
		Geography.Regions.Europe.Southern Europe     0.648
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.764
		History and Society.Business and economics   0.575
		History and Society.Education                0.627
		History and Society.History                  0.472
		History and Society.Military and warfare     0.594
		History and Society.Politics and government  0.613
		History and Society.Society                  0.421
		History and Society.Transportation           0.861
		STEM.Biology                                 0.876
		STEM.Chemistry                               0.543
		STEM.Computing                               0.429
		STEM.Earth and environment                   0.664
		STEM.Engineering                             0.641
		STEM.Libraries & Information                 0.502
		STEM.Mathematics                             0.417
		STEM.Medicine & Health                       0.683
		STEM.Physics                                 0.36
		STEM.STEM*                                   0.818
		STEM.Space                                   0.915
		STEM.Technology                              0.386
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.999
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.983
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
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
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.997
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.985
		Geography.Regions.Europe.Europe*             0.933
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.99
		History and Society.Education                0.995
		History and Society.History                  0.984
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.982
		History and Society.Transportation           0.996
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.015, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.027
		Culture.Media.Music                          0.006
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.016
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.007
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.012
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.009
		History and Society.Society                  0.012
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.975):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.987
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.983
		Culture.Literature                           0.979
		Culture.Media.Books                          0.986
		Culture.Media.Entertainment                  0.978
		Culture.Media.Films                          0.987
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.958
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.989
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.982
		Culture.Philosophy and religion              0.964
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.992
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.769
		Geography.Regions.Africa.Eastern Africa      0.978
		Geography.Regions.Africa.Northern Africa     0.981
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.936
		Geography.Regions.Americas.Central America   0.981
		Geography.Regions.Americas.North America     0.963
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.984
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.985
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.979
		Geography.Regions.Asia.West Asia             0.983
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.954
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.971
		History and Society.Education                0.974
		History and Society.History                  0.964
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.962
		History and Society.Society                  0.938
		History and Society.Transportation           0.988
		STEM.Biology                                 0.983
		STEM.Chemistry                               0.989
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.982
		STEM.Engineering                             0.983
		STEM.Libraries & Information                 0.97
		STEM.Mathematics                             0.989
		STEM.Medicine & Health                       0.981
		STEM.Physics                                 0.988
		STEM.STEM*                                   0.979
		STEM.Space                                   0.993
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.801, macro=0.67):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.8
		Culture.Food and drink                       0.782
		Culture.Internet culture                     0.789
		Culture.Linguistics                          0.807
		Culture.Literature                           0.75
		Culture.Media.Books                          0.799
		Culture.Media.Entertainment                  0.457
		Culture.Media.Films                          0.897
		Culture.Media.Media*                         0.868
		Culture.Media.Music                          0.854
		Culture.Media.Radio                          0.491
		Culture.Media.Software                       0.315
		Culture.Media.Television                     0.862
		Culture.Media.Video games                    0.926
		Culture.Performing arts                      0.626
		Culture.Philosophy and religion              0.535
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.763
		Culture.Visual arts.Comics and Anime         0.915
		Culture.Visual arts.Fashion                  0.5
		Culture.Visual arts.Visual arts*             0.793
		Geography.Geographical                       0.679
		Geography.Regions.Africa.Africa*             0.68
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.308
		Geography.Regions.Africa.Northern Africa     0.42
		Geography.Regions.Africa.Southern Africa     0.568
		Geography.Regions.Africa.Western Africa      0.232
		Geography.Regions.Americas.Central America   0.689
		Geography.Regions.Americas.North America     0.747
		Geography.Regions.Americas.South America     0.772
		Geography.Regions.Asia.Asia*                 0.829
		Geography.Regions.Asia.Central Asia          0.414
		Geography.Regions.Asia.East Asia             0.808
		Geography.Regions.Asia.North Asia            0.184
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.79
		Geography.Regions.Asia.West Asia             0.806
		Geography.Regions.Europe.Eastern Europe      0.598
		Geography.Regions.Europe.Europe*             0.73
		Geography.Regions.Europe.Northern Europe     0.75
		Geography.Regions.Europe.Southern Europe     0.686
		Geography.Regions.Europe.Western Europe      0.664
		Geography.Regions.Oceania                    0.818
		History and Society.Business and economics   0.568
		History and Society.Education                0.646
		History and Society.History                  0.489
		History and Society.Military and warfare     0.674
		History and Society.Politics and government  0.636
		History and Society.Society                  0.401
		History and Society.Transportation           0.904
		STEM.Biology                                 0.921
		STEM.Chemistry                               0.627
		STEM.Computing                               0.506
		STEM.Earth and environment                   0.677
		STEM.Engineering                             0.713
		STEM.Libraries & Information                 0.547
		STEM.Mathematics                             0.608
		STEM.Medicine & Health                       0.727
		STEM.Physics                                 0.412
		STEM.STEM*                                   0.918
		STEM.Space                                   0.962
		STEM.Technology                              0.474
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}}}}}

