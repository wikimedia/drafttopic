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
	counts (n=54768):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 15434  -->  13723  1711   778  38556
			'Culture.Biography.Women'                       4442  -->   3025  1417   487  49839
			'Culture.Food and drink'                        1651  -->   1244   407    96  53021
			'Culture.Internet culture'                      2455  -->   2005   450   135  52178
			'Culture.Linguistics'                           1666  -->   1128   538    89  53013
			'Culture.Literature'                            5219  -->   3724  1495   522  49027
			'Culture.Media.Books'                           1730  -->   1400   330   112  52926
			'Culture.Media.Entertainment'                   2126  -->    995  1131   174  52468
			'Culture.Media.Films'                           2978  -->   2551   427   136  51654
			'Culture.Media.Media*'                         13038  -->  11086  1952  1249  40481
			'Culture.Media.Music'                           3385  -->   2729   656   260  51123
			'Culture.Media.Radio'                            231  -->    173    58    25  54512
			'Culture.Media.Software'                        2174  -->   1984   190   169  52425
			'Culture.Media.Television'                      2046  -->   1551   495    92  52630
			'Culture.Media.Video games'                      731  -->    704    27    19  54018
			'Culture.Performing arts'                       1716  -->   1104   612   125  52927
			'Culture.Philosophy and religion'               3830  -->   1887  1943   320  50618
			'Culture.Sports'                                3252  -->   2624   628    92  51424
			'Culture.Visual arts.Architecture'              2428  -->   1829   599   240  52100
			'Culture.Visual arts.Comics and Anime'          1054  -->    872   182    41  53673
			'Culture.Visual arts.Fashion'                    807  -->    595   212    50  53911
			'Culture.Visual arts.Visual arts*'              5374  -->   3756  1618   492  48902
			'Geography.Geographical'                        4807  -->   3314  1493   556  49405
			'Geography.Regions.Africa.Africa*'              3253  -->   1859  1394   210  51305
			'Geography.Regions.Africa.Central Africa'        387  -->    250   137    15  54366
			'Geography.Regions.Africa.Eastern Africa'        244  -->    184    60    23  54501
			'Geography.Regions.Africa.Northern Africa'      1308  -->    813   495    84  53376
			'Geography.Regions.Africa.Southern Africa'       603  -->    443   160    20  54145
			'Geography.Regions.Africa.Western Africa'        140  -->     90    50    34  54594
			'Geography.Regions.Americas.Central America'    1242  -->    488   754    47  53479
			'Geography.Regions.Americas.North America'      5786  -->   3799  1987   713  48269
			'Geography.Regions.Americas.South America'      1659  -->   1251   408    69  53040
			'Geography.Regions.Asia.Asia*'                 11940  -->   9086  2854  1250  41578
			'Geography.Regions.Asia.Central Asia'           1084  -->    667   417    64  53620
			'Geography.Regions.Asia.East Asia'              2617  -->   2030   587   118  52033
			'Geography.Regions.Asia.North Asia'             2544  -->   1728   816   299  51925
			'Geography.Regions.Asia.South Asia'             1903  -->   1218   685    76  52789
			'Geography.Regions.Asia.Southeast Asia'         1445  -->    731   714    35  53288
			'Geography.Regions.Asia.West Asia'              4362  -->   3026  1336   406  50000
			'Geography.Regions.Europe.Eastern Europe'       4452  -->   3134  1318   427  49889
			'Geography.Regions.Europe.Europe*'             16807  -->  13206  3601  2136  35825
			'Geography.Regions.Europe.Northern Europe'      4196  -->   2846  1350   317  50255
			'Geography.Regions.Europe.Southern Europe'      4373  -->   3153  1220   352  50043
			'Geography.Regions.Europe.Western Europe'       4887  -->   3630  1257   387  49494
			'Geography.Regions.Oceania'                     1664  -->    958   706    83  53021
			'History and Society.Business and economics'    3402  -->   2157  1245   256  51110
			'History and Society.Education'                 1839  -->   1069   770   114  52815
			'History and Society.History'                   5751  -->   3026  2725   720  48297
			'History and Society.Military and warfare'      5144  -->   3427  1717   635  48989
			'History and Society.Politics and government'   4609  -->   2261  2348   469  49690
			'History and Society.Society'                   7860  -->   3941  3919   754  46154
			'History and Society.Transportation'            2480  -->   2052   428    91  52197
			'STEM.Biology'                                  3060  -->   2301   759   161  51547
			'STEM.Chemistry'                                1509  -->   1217   292   124  53135
			'STEM.Computing'                                2235  -->   1869   366   167  52366
			'STEM.Earth and environment'                    1837  -->   1209   628   139  52792
			'STEM.Engineering'                              2740  -->   1969   771   206  51822
			'STEM.Libraries & Information'                   497  -->    381   116    19  54252
			'STEM.Mathematics'                               590  -->    474   116    30  54148
			'STEM.Medicine & Health'                        2056  -->   1456   600   133  52579
			'STEM.Physics'                                  1641  -->   1218   423   132  52995
			'STEM.STEM*'                                   16483  -->  14410  2073  1029  37256
			'STEM.Space'                                    2075  -->   1930   145    33  52660
			'STEM.Technology'                               4422  -->   3251  1171   477  49869
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.282         0.123
		Culture.Biography.Women                         0.081         0.015
		Culture.Food and drink                          0.03          0.002
		Culture.Internet culture                        0.045         0.003
		Culture.Linguistics                             0.03          0.007
		Culture.Literature                              0.095         0.015
		Culture.Media.Books                             0.032         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.054         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.062         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.013         0.003
		Culture.Performing arts                         0.031         0.003
		Culture.Philosophy and religion                 0.07          0.011
		Culture.Sports                                  0.059         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.019         0.002
		Culture.Visual arts.Fashion                     0.015         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.088         0.024
		Geography.Regions.Africa.Africa*                0.059         0.008
		Geography.Regions.Africa.Central Africa         0.007         0.001
		Geography.Regions.Africa.Eastern Africa         0.004         0
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.106         0.064
		Geography.Regions.Americas.South America        0.03          0.006
		Geography.Regions.Asia.Asia*                    0.218         0.045
		Geography.Regions.Asia.Central Asia             0.02          0.001
		Geography.Regions.Asia.East Asia                0.048         0.011
		Geography.Regions.Asia.North Asia               0.046         0.001
		Geography.Regions.Asia.South Asia               0.035         0.015
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.08          0.011
		Geography.Regions.Europe.Eastern Europe         0.081         0.013
		Geography.Regions.Europe.Europe*                0.307         0.076
		Geography.Regions.Europe.Northern Europe        0.077         0.031
		Geography.Regions.Europe.Southern Europe        0.08          0.013
		Geography.Regions.Europe.Western Europe         0.089         0.019
		Geography.Regions.Oceania                       0.03          0.015
		History and Society.Business and economics      0.062         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.105         0.011
		History and Society.Military and warfare        0.094         0.014
		History and Society.Politics and government     0.084         0.028
		History and Society.Society                     0.144         0.013
		History and Society.Transportation              0.045         0.015
		STEM.Biology                                    0.056         0.034
		STEM.Chemistry                                  0.028         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.034         0.005
		STEM.Engineering                                0.05          0.005
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.011         0
		STEM.Medicine & Health                          0.038         0.006
		STEM.Physics                                    0.03          0.001
		STEM.STEM*                                      0.301         0.069
		STEM.Space                                      0.038         0.006
		STEM.Technology                                 0.081         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.127
		Culture.Biography.Women                      0.019
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.007
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.027
		Geography.Regions.Africa.Africa*             0.009
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.011
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.016
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.112
		Geography.Regions.Europe.Northern Europe     0.027
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.02
		History and Society.Military and warfare     0.022
		History and Society.Politics and government  0.023
		History and Society.Society                  0.022
		History and Society.Transportation           0.014
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.993
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.888
		Geography.Regions.Europe.Northern Europe     0.973
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.98
		History and Society.Military and warfare     0.978
		History and Society.Politics and government  0.977
		History and Society.Society                  0.978
		History and Society.Transportation           0.986
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.751, macro=0.712):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.889
		Culture.Biography.Women                      0.681
		Culture.Food and drink                       0.753
		Culture.Internet culture                     0.817
		Culture.Linguistics                          0.677
		Culture.Literature                           0.714
		Culture.Media.Books                          0.809
		Culture.Media.Entertainment                  0.468
		Culture.Media.Films                          0.857
		Culture.Media.Media*                         0.85
		Culture.Media.Music                          0.806
		Culture.Media.Radio                          0.749
		Culture.Media.Software                       0.913
		Culture.Media.Television                     0.758
		Culture.Media.Video games                    0.963
		Culture.Performing arts                      0.643
		Culture.Philosophy and religion              0.493
		Culture.Sports                               0.807
		Culture.Visual arts.Architecture             0.753
		Culture.Visual arts.Comics and Anime         0.827
		Culture.Visual arts.Fashion                  0.737
		Culture.Visual arts.Visual arts*             0.699
		Geography.Geographical                       0.689
		Geography.Regions.Africa.Africa*             0.571
		Geography.Regions.Africa.Central Africa      0.646
		Geography.Regions.Africa.Eastern Africa      0.754
		Geography.Regions.Africa.Northern Africa     0.622
		Geography.Regions.Africa.Southern Africa     0.735
		Geography.Regions.Africa.Western Africa      0.643
		Geography.Regions.Americas.Central America   0.393
		Geography.Regions.Americas.North America     0.657
		Geography.Regions.Americas.South America     0.754
		Geography.Regions.Asia.Asia*                 0.761
		Geography.Regions.Asia.Central Asia          0.615
		Geography.Regions.Asia.East Asia             0.776
		Geography.Regions.Asia.North Asia            0.679
		Geography.Regions.Asia.South Asia            0.64
		Geography.Regions.Asia.Southeast Asia        0.506
		Geography.Regions.Asia.West Asia             0.694
		Geography.Regions.Europe.Eastern Europe      0.704
		Geography.Regions.Europe.Europe*             0.786
		Geography.Regions.Europe.Northern Europe     0.678
		Geography.Regions.Europe.Southern Europe     0.721
		Geography.Regions.Europe.Western Europe      0.743
		Geography.Regions.Oceania                    0.576
		History and Society.Business and economics   0.634
		History and Society.Education                0.581
		History and Society.History                  0.526
		History and Society.Military and warfare     0.666
		History and Society.Politics and government  0.491
		History and Society.Society                  0.501
		History and Society.Transportation           0.827
		STEM.Biology                                 0.752
		STEM.Chemistry                               0.806
		STEM.Computing                               0.836
		STEM.Earth and environment                   0.658
		STEM.Engineering                             0.719
		STEM.Libraries & Information                 0.767
		STEM.Mathematics                             0.803
		STEM.Medicine & Health                       0.708
		STEM.Physics                                 0.742
		STEM.STEM*                                   0.874
		STEM.Space                                   0.93
		STEM.Technology                              0.735
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.989
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.985
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.991
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.991
		-------------------------------------------  -----
	precision (micro=0.693, macro=0.584):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.863
		Culture.Biography.Women                      0.51
		Culture.Food and drink                       0.507
		Culture.Internet culture                     0.526
		Culture.Linguistics                          0.749
		Culture.Literature                           0.516
		Culture.Media.Books                          0.608
		Culture.Media.Entertainment                  0.337
		Culture.Media.Films                          0.776
		Culture.Media.Media*                         0.638
		Culture.Media.Music                          0.796
		Culture.Media.Radio                          0.779
		Culture.Media.Software                       0.274
		Culture.Media.Television                     0.794
		Culture.Media.Video games                    0.878
		Culture.Performing arts                      0.441
		Culture.Philosophy and religion              0.458
		Culture.Sports                               0.972
		Culture.Visual arts.Architecture             0.637
		Culture.Visual arts.Comics and Anime         0.705
		Culture.Visual arts.Fashion                  0.392
		Culture.Visual arts.Visual arts*             0.567
		Geography.Geographical                       0.599
		Geography.Regions.Africa.Africa*             0.524
		Geography.Regions.Africa.Central Africa      0.597
		Geography.Regions.Africa.Eastern Africa      0.449
		Geography.Regions.Africa.Northern Africa     0.327
		Geography.Regions.Africa.Southern Africa     0.701
		Geography.Regions.Africa.Western Africa      0.414
		Geography.Regions.Americas.Central America   0.597
		Geography.Regions.Americas.North America     0.756
		Geography.Regions.Americas.South America     0.787
		Geography.Regions.Asia.Asia*                 0.554
		Geography.Regions.Asia.Central Asia          0.309
		Geography.Regions.Asia.East Asia             0.798
		Geography.Regions.Asia.North Asia            0.099
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.823
		Geography.Regions.Asia.West Asia             0.487
		Geography.Regions.Europe.Eastern Europe      0.519
		Geography.Regions.Europe.Europe*             0.535
		Geography.Regions.Europe.Northern Europe     0.773
		Geography.Regions.Europe.Southern Europe     0.577
		Geography.Regions.Europe.Western Europe      0.652
		Geography.Regions.Oceania                    0.85
		History and Society.Business and economics   0.565
		History and Society.Education                0.667
		History and Society.History                  0.282
		History and Society.Military and warfare     0.426
		History and Society.Politics and government  0.603
		History and Society.Society                  0.285
		History and Society.Transportation           0.879
		STEM.Biology                                 0.894
		STEM.Chemistry                               0.351
		STEM.Computing                               0.415
		STEM.Earth and environment                   0.533
		STEM.Engineering                             0.488
		STEM.Libraries & Information                 0.576
		STEM.Mathematics                             0.377
		STEM.Medicine & Health                       0.644
		STEM.Physics                                 0.202
		STEM.STEM*                                   0.707
		STEM.Space                                   0.9
		STEM.Technology                              0.286
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.995
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.985
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.991
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.711, macro=0.623):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.583
		Culture.Food and drink                       0.606
		Culture.Internet culture                     0.64
		Culture.Linguistics                          0.711
		Culture.Literature                           0.599
		Culture.Media.Books                          0.694
		Culture.Media.Entertainment                  0.392
		Culture.Media.Films                          0.814
		Culture.Media.Media*                         0.729
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.764
		Culture.Media.Software                       0.422
		Culture.Media.Television                     0.776
		Culture.Media.Video games                    0.918
		Culture.Performing arts                      0.524
		Culture.Philosophy and religion              0.475
		Culture.Sports                               0.882
		Culture.Visual arts.Architecture             0.69
		Culture.Visual arts.Comics and Anime         0.761
		Culture.Visual arts.Fashion                  0.512
		Culture.Visual arts.Visual arts*             0.626
		Geography.Geographical                       0.641
		Geography.Regions.Africa.Africa*             0.547
		Geography.Regions.Africa.Central Africa      0.62
		Geography.Regions.Africa.Eastern Africa      0.563
		Geography.Regions.Africa.Northern Africa     0.429
		Geography.Regions.Africa.Southern Africa     0.717
		Geography.Regions.Africa.Western Africa      0.504
		Geography.Regions.Americas.Central America   0.474
		Geography.Regions.Americas.North America     0.703
		Geography.Regions.Americas.South America     0.77
		Geography.Regions.Asia.Asia*                 0.641
		Geography.Regions.Asia.Central Asia          0.411
		Geography.Regions.Asia.East Asia             0.787
		Geography.Regions.Asia.North Asia            0.173
		Geography.Regions.Asia.South Asia            0.739
		Geography.Regions.Asia.Southeast Asia        0.627
		Geography.Regions.Asia.West Asia             0.572
		Geography.Regions.Europe.Eastern Europe      0.597
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.723
		Geography.Regions.Europe.Southern Europe     0.641
		Geography.Regions.Europe.Western Europe      0.694
		Geography.Regions.Oceania                    0.686
		History and Society.Business and economics   0.597
		History and Society.Education                0.621
		History and Society.History                  0.367
		History and Society.Military and warfare     0.52
		History and Society.Politics and government  0.541
		History and Society.Society                  0.363
		History and Society.Transportation           0.853
		STEM.Biology                                 0.817
		STEM.Chemistry                               0.489
		STEM.Computing                               0.555
		STEM.Earth and environment                   0.589
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.658
		STEM.Mathematics                             0.513
		STEM.Medicine & Health                       0.674
		STEM.Physics                                 0.318
		STEM.STEM*                                   0.782
		STEM.Space                                   0.915
		STEM.Technology                              0.412
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.995
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
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.988
		History and Society.Society                  0.989
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.995
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.961
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.98
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.977
		History and Society.Society                  0.978
		History and Society.Transportation           0.996
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.966
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.02
		Culture.Biography.Women                      0.01
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.011
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.004
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.029
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.008
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.007
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.015
		History and Society.Military and warfare     0.013
		History and Society.Politics and government  0.009
		History and Society.Society                  0.016
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.002
		STEM.STEM*                                   0.027
		STEM.Space                                   0.001
		STEM.Technology                              0.009
		-------------------------------------------  -----
	roc_auc (micro=0.969, macro=0.97):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.973
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.971
		Culture.Literature                           0.972
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.967
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.946
		Culture.Media.Software                       0.99
		Culture.Media.Television                     0.98
		Culture.Media.Video games                    0.992
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.945
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.981
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.968
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.964
		Geography.Regions.Africa.Central Africa      0.966
		Geography.Regions.Africa.Eastern Africa      0.928
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.976
		Geography.Regions.Africa.Western Africa      0.903
		Geography.Regions.Americas.Central America   0.955
		Geography.Regions.Americas.North America     0.964
		Geography.Regions.Americas.South America     0.978
		Geography.Regions.Asia.Asia*                 0.96
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.981
		Geography.Regions.Asia.North Asia            0.979
		Geography.Regions.Asia.South Asia            0.972
		Geography.Regions.Asia.Southeast Asia        0.963
		Geography.Regions.Asia.West Asia             0.973
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.968
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.961
		History and Society.Business and economics   0.965
		History and Society.Education                0.964
		History and Society.History                  0.941
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.946
		History and Society.Society                  0.919
		History and Society.Transportation           0.983
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.967
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.974
		STEM.Space                                   0.991
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.758, macro=0.613):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.934
		Culture.Biography.Women                      0.551
		Culture.Food and drink                       0.615
		Culture.Internet culture                     0.746
		Culture.Linguistics                          0.694
		Culture.Literature                           0.655
		Culture.Media.Books                          0.705
		Culture.Media.Entertainment                  0.347
		Culture.Media.Films                          0.863
		Culture.Media.Media*                         0.831
		Culture.Media.Music                          0.848
		Culture.Media.Radio                          0.555
		Culture.Media.Software                       0.645
		Culture.Media.Television                     0.765
		Culture.Media.Video games                    0.951
		Culture.Performing arts                      0.486
		Culture.Philosophy and religion              0.445
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.705
		Culture.Visual arts.Comics and Anime         0.75
		Culture.Visual arts.Fashion                  0.344
		Culture.Visual arts.Visual arts*             0.636
		Geography.Geographical                       0.674
		Geography.Regions.Africa.Africa*             0.535
		Geography.Regions.Africa.Central Africa      0.363
		Geography.Regions.Africa.Eastern Africa      0.275
		Geography.Regions.Africa.Northern Africa     0.332
		Geography.Regions.Africa.Southern Africa     0.567
		Geography.Regions.Africa.Western Africa      0.217
		Geography.Regions.Americas.Central America   0.398
		Geography.Regions.Americas.North America     0.764
		Geography.Regions.Americas.South America     0.805
		Geography.Regions.Asia.Asia*                 0.695
		Geography.Regions.Asia.Central Asia          0.308
		Geography.Regions.Asia.East Asia             0.801
		Geography.Regions.Asia.North Asia            0.129
		Geography.Regions.Asia.South Asia            0.789
		Geography.Regions.Asia.Southeast Asia        0.606
		Geography.Regions.Asia.West Asia             0.584
		Geography.Regions.Europe.Eastern Europe      0.599
		Geography.Regions.Europe.Europe*             0.731
		Geography.Regions.Europe.Northern Europe     0.778
		Geography.Regions.Europe.Southern Europe     0.688
		Geography.Regions.Europe.Western Europe      0.723
		Geography.Regions.Oceania                    0.696
		History and Society.Business and economics   0.571
		History and Society.Education                0.612
		History and Society.History                  0.333
		History and Society.Military and warfare     0.536
		History and Society.Politics and government  0.559
		History and Society.Society                  0.344
		History and Society.Transportation           0.89
		STEM.Biology                                 0.886
		STEM.Chemistry                               0.458
		STEM.Computing                               0.589
		STEM.Earth and environment                   0.537
		STEM.Engineering                             0.613
		STEM.Libraries & Information                 0.524
		STEM.Mathematics                             0.462
		STEM.Medicine & Health                       0.674
		STEM.Physics                                 0.273
		STEM.STEM*                                   0.889
		STEM.Space                                   0.943
		STEM.Technology                              0.482
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

