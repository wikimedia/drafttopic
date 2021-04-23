Model Information:
	 - type: GradientBoosting
	 - version: 1.4.0
	 - params: {'scale': False, 'center': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'multilabel': True, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': {}}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.9'
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
			'Culture.Biography.Biography*'                 15434  -->  13765  1669   767  38567
			'Culture.Biography.Women'                       4442  -->   3011  1431   482  49844
			'Culture.Food and drink'                        1651  -->   1240   411   109  53008
			'Culture.Internet culture'                      2455  -->   2017   438   147  52166
			'Culture.Linguistics'                           1666  -->   1139   527    62  53040
			'Culture.Literature'                            5219  -->   3675  1544   515  49034
			'Culture.Media.Books'                           1730  -->   1392   338   104  52934
			'Culture.Media.Entertainment'                   2126  -->   1000  1126   188  52454
			'Culture.Media.Films'                           2978  -->   2534   444   130  51660
			'Culture.Media.Media*'                         13038  -->  11126  1912  1318  40412
			'Culture.Media.Music'                           3385  -->   2746   639   264  51119
			'Culture.Media.Radio'                            231  -->    173    58    20  54517
			'Culture.Media.Software'                        2174  -->   1981   193   176  52418
			'Culture.Media.Television'                      2046  -->   1550   496    97  52625
			'Culture.Media.Video games'                      731  -->    711    20    16  54021
			'Culture.Performing arts'                       1716  -->   1094   622   119  52933
			'Culture.Philosophy and religion'               3830  -->   1895  1935   327  50611
			'Culture.Sports'                                3252  -->   2648   604   105  51411
			'Culture.Visual arts.Architecture'              2428  -->   1824   604   258  52082
			'Culture.Visual arts.Comics and Anime'          1054  -->    858   196    48  53666
			'Culture.Visual arts.Fashion'                    807  -->    598   209    46  53915
			'Culture.Visual arts.Visual arts*'              5374  -->   3740  1634   498  48896
			'Geography.Geographical'                        4807  -->   3301  1506   558  49403
			'Geography.Regions.Africa.Africa*'              3253  -->   1886  1367   206  51309
			'Geography.Regions.Africa.Central Africa'        387  -->    242   145    40  54341
			'Geography.Regions.Africa.Eastern Africa'        244  -->    185    59    27  54497
			'Geography.Regions.Africa.Northern Africa'      1308  -->    832   476    93  53367
			'Geography.Regions.Africa.Southern Africa'       603  -->    441   162    19  54146
			'Geography.Regions.Africa.Western Africa'        140  -->     64    76    42  54586
			'Geography.Regions.Americas.Central America'    1242  -->    501   741    54  53472
			'Geography.Regions.Americas.North America'      5786  -->   3813  1973   717  48265
			'Geography.Regions.Americas.South America'      1659  -->   1251   408    70  53039
			'Geography.Regions.Asia.Asia*'                 11940  -->   9075  2865  1251  41577
			'Geography.Regions.Asia.Central Asia'           1084  -->    670   414    63  53621
			'Geography.Regions.Asia.East Asia'              2617  -->   2035   582   131  52020
			'Geography.Regions.Asia.North Asia'             2544  -->   1742   802   323  51901
			'Geography.Regions.Asia.South Asia'             1903  -->   1207   696    71  52794
			'Geography.Regions.Asia.Southeast Asia'         1445  -->    705   740    37  53286
			'Geography.Regions.Asia.West Asia'              4362  -->   3051  1311   410  49996
			'Geography.Regions.Europe.Eastern Europe'       4452  -->   3170  1282   426  49890
			'Geography.Regions.Europe.Europe*'             16807  -->  13202  3605  2152  35809
			'Geography.Regions.Europe.Northern Europe'      4196  -->   2835  1361   298  50274
			'Geography.Regions.Europe.Southern Europe'      4373  -->   3142  1231   320  50075
			'Geography.Regions.Europe.Western Europe'       4887  -->   3635  1252   405  49476
			'Geography.Regions.Oceania'                     1664  -->    924   740    81  53023
			'History and Society.Business and economics'    3402  -->   2151  1251   264  51102
			'History and Society.Education'                 1839  -->   1063   776   109  52820
			'History and Society.History'                   5751  -->   2990  2761   699  48318
			'History and Society.Military and warfare'      5144  -->   3425  1719   600  49024
			'History and Society.Politics and government'   4609  -->   2234  2375   471  49688
			'History and Society.Society'                   7860  -->   3929  3931   736  46172
			'History and Society.Transportation'            2480  -->   2041   439    89  52199
			'STEM.Biology'                                  3060  -->   2304   756   157  51551
			'STEM.Chemistry'                                1509  -->   1212   297   118  53141
			'STEM.Computing'                                2235  -->   1872   363   167  52366
			'STEM.Earth and environment'                    1837  -->   1238   599   123  52808
			'STEM.Engineering'                              2740  -->   1968   772   212  51816
			'STEM.Libraries & Information'                   497  -->    383   114    36  54235
			'STEM.Mathematics'                               590  -->    465   125    28  54150
			'STEM.Medicine & Health'                        2056  -->   1478   578   138  52574
			'STEM.Physics'                                  1641  -->   1228   413   150  52977
			'STEM.STEM*'                                   16483  -->  14428  2055  1004  37281
			'STEM.Space'                                    2075  -->   1922   153    33  52660
			'STEM.Technology'                               4422  -->   3264  1158   505  49841
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
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.08
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.008
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.06
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.027
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.062
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.011
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.016
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.112
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.016
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.02
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.023
		History and Society.Society                  0.022
		History and Society.Transportation           0.014
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.873
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.92
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.938
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.984
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.888
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.98
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.977
		History and Society.Society                  0.978
		History and Society.Transportation           0.986
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.752, macro=0.709):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.892
		Culture.Biography.Women                      0.678
		Culture.Food and drink                       0.751
		Culture.Internet culture                     0.822
		Culture.Linguistics                          0.684
		Culture.Literature                           0.704
		Culture.Media.Books                          0.805
		Culture.Media.Entertainment                  0.47
		Culture.Media.Films                          0.851
		Culture.Media.Media*                         0.853
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.749
		Culture.Media.Software                       0.911
		Culture.Media.Television                     0.758
		Culture.Media.Video games                    0.973
		Culture.Performing arts                      0.638
		Culture.Philosophy and religion              0.495
		Culture.Sports                               0.814
		Culture.Visual arts.Architecture             0.751
		Culture.Visual arts.Comics and Anime         0.814
		Culture.Visual arts.Fashion                  0.741
		Culture.Visual arts.Visual arts*             0.696
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.58
		Geography.Regions.Africa.Central Africa      0.625
		Geography.Regions.Africa.Eastern Africa      0.758
		Geography.Regions.Africa.Northern Africa     0.636
		Geography.Regions.Africa.Southern Africa     0.731
		Geography.Regions.Africa.Western Africa      0.457
		Geography.Regions.Americas.Central America   0.403
		Geography.Regions.Americas.North America     0.659
		Geography.Regions.Americas.South America     0.754
		Geography.Regions.Asia.Asia*                 0.76
		Geography.Regions.Asia.Central Asia          0.618
		Geography.Regions.Asia.East Asia             0.778
		Geography.Regions.Asia.North Asia            0.685
		Geography.Regions.Asia.South Asia            0.634
		Geography.Regions.Asia.Southeast Asia        0.488
		Geography.Regions.Asia.West Asia             0.699
		Geography.Regions.Europe.Eastern Europe      0.712
		Geography.Regions.Europe.Europe*             0.786
		Geography.Regions.Europe.Northern Europe     0.676
		Geography.Regions.Europe.Southern Europe     0.718
		Geography.Regions.Europe.Western Europe      0.744
		Geography.Regions.Oceania                    0.555
		History and Society.Business and economics   0.632
		History and Society.Education                0.578
		History and Society.History                  0.52
		History and Society.Military and warfare     0.666
		History and Society.Politics and government  0.485
		History and Society.Society                  0.5
		History and Society.Transportation           0.823
		STEM.Biology                                 0.753
		STEM.Chemistry                               0.803
		STEM.Computing                               0.838
		STEM.Earth and environment                   0.674
		STEM.Engineering                             0.718
		STEM.Libraries & Information                 0.771
		STEM.Mathematics                             0.788
		STEM.Medicine & Health                       0.719
		STEM.Physics                                 0.748
		STEM.STEM*                                   0.875
		STEM.Space                                   0.926
		STEM.Technology                              0.738
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.99
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.968
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
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.943
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.991
		History and Society.Society                  0.984
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.692, macro=0.576):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.511
		Culture.Food and drink                       0.475
		Culture.Internet culture                     0.507
		Culture.Linguistics                          0.812
		Culture.Literature                           0.516
		Culture.Media.Books                          0.624
		Culture.Media.Entertainment                  0.321
		Culture.Media.Films                          0.783
		Culture.Media.Media*                         0.627
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.815
		Culture.Media.Software                       0.266
		Culture.Media.Television                     0.785
		Culture.Media.Video games                    0.896
		Culture.Performing arts                      0.451
		Culture.Philosophy and religion              0.453
		Culture.Sports                               0.968
		Culture.Visual arts.Architecture             0.619
		Culture.Visual arts.Comics and Anime         0.667
		Culture.Visual arts.Fashion                  0.413
		Culture.Visual arts.Visual arts*             0.563
		Geography.Geographical                       0.598
		Geography.Regions.Africa.Africa*             0.533
		Geography.Regions.Africa.Central Africa      0.349
		Geography.Regions.Africa.Eastern Africa      0.411
		Geography.Regions.Africa.Northern Africa     0.31
		Geography.Regions.Africa.Southern Africa     0.71
		Geography.Regions.Africa.Western Africa      0.289
		Geography.Regions.Americas.Central America   0.57
		Geography.Regions.Americas.North America     0.756
		Geography.Regions.Americas.South America     0.784
		Geography.Regions.Asia.Asia*                 0.554
		Geography.Regions.Asia.Central Asia          0.313
		Geography.Regions.Asia.East Asia             0.781
		Geography.Regions.Asia.North Asia            0.093
		Geography.Regions.Asia.South Asia            0.879
		Geography.Regions.Asia.Southeast Asia        0.809
		Geography.Regions.Asia.West Asia             0.487
		Geography.Regions.Europe.Eastern Europe      0.522
		Geography.Regions.Europe.Europe*             0.533
		Geography.Regions.Europe.Northern Europe     0.783
		Geography.Regions.Europe.Southern Europe     0.599
		Geography.Regions.Europe.Western Europe      0.642
		Geography.Regions.Oceania                    0.848
		History and Society.Business and economics   0.556
		History and Society.Education                0.675
		History and Society.History                  0.285
		History and Society.Military and warfare     0.44
		History and Society.Politics and government  0.6
		History and Society.Society                  0.289
		History and Society.Transportation           0.881
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.361
		STEM.Computing                               0.415
		STEM.Earth and environment                   0.569
		STEM.Engineering                             0.481
		STEM.Libraries & Information                 0.419
		STEM.Mathematics                             0.389
		STEM.Medicine & Health                       0.639
		STEM.Physics                                 0.184
		STEM.STEM*                                   0.713
		STEM.Space                                   0.9
		STEM.Technology                              0.275
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
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
		Culture.Sports                               0.986
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
		Geography.Regions.Oceania                    0.993
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
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.711, macro=0.615):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.583
		Culture.Food and drink                       0.582
		Culture.Internet culture                     0.627
		Culture.Linguistics                          0.742
		Culture.Literature                           0.596
		Culture.Media.Books                          0.703
		Culture.Media.Entertainment                  0.382
		Culture.Media.Films                          0.815
		Culture.Media.Media*                         0.723
		Culture.Media.Music                          0.803
		Culture.Media.Radio                          0.781
		Culture.Media.Software                       0.412
		Culture.Media.Television                     0.771
		Culture.Media.Video games                    0.933
		Culture.Performing arts                      0.529
		Culture.Philosophy and religion              0.473
		Culture.Sports                               0.885
		Culture.Visual arts.Architecture             0.679
		Culture.Visual arts.Comics and Anime         0.733
		Culture.Visual arts.Fashion                  0.53
		Culture.Visual arts.Visual arts*             0.622
		Geography.Geographical                       0.639
		Geography.Regions.Africa.Africa*             0.555
		Geography.Regions.Africa.Central Africa      0.448
		Geography.Regions.Africa.Eastern Africa      0.533
		Geography.Regions.Africa.Northern Africa     0.417
		Geography.Regions.Africa.Southern Africa     0.721
		Geography.Regions.Africa.Western Africa      0.354
		Geography.Regions.Americas.Central America   0.472
		Geography.Regions.Americas.North America     0.704
		Geography.Regions.Americas.South America     0.769
		Geography.Regions.Asia.Asia*                 0.641
		Geography.Regions.Asia.Central Asia          0.416
		Geography.Regions.Asia.East Asia             0.779
		Geography.Regions.Asia.North Asia            0.164
		Geography.Regions.Asia.South Asia            0.737
		Geography.Regions.Asia.Southeast Asia        0.609
		Geography.Regions.Asia.West Asia             0.574
		Geography.Regions.Europe.Eastern Europe      0.603
		Geography.Regions.Europe.Europe*             0.635
		Geography.Regions.Europe.Northern Europe     0.726
		Geography.Regions.Europe.Southern Europe     0.653
		Geography.Regions.Europe.Western Europe      0.689
		Geography.Regions.Oceania                    0.671
		History and Society.Business and economics   0.592
		History and Society.Education                0.623
		History and Society.History                  0.368
		History and Society.Military and warfare     0.53
		History and Society.Politics and government  0.536
		History and Society.Society                  0.366
		History and Society.Transportation           0.851
		STEM.Biology                                 0.818
		STEM.Chemistry                               0.498
		STEM.Computing                               0.555
		STEM.Earth and environment                   0.617
		STEM.Engineering                             0.576
		STEM.Libraries & Information                 0.543
		STEM.Mathematics                             0.521
		STEM.Medicine & Health                       0.676
		STEM.Physics                                 0.295
		STEM.STEM*                                   0.786
		STEM.Space                                   0.913
		STEM.Technology                              0.401
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
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
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.979
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.992
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
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.985
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
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
		Geography.Regions.Europe.Europe*             0.931
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.981
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.978
		History and Society.Transportation           0.996
		STEM.Biology                                 0.989
		STEM.Chemistry                               0.997
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.967
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.01
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.01
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.032
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
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.029
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.008
		Geography.Regions.Europe.Europe*             0.057
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.012
		History and Society.Politics and government  0.009
		History and Society.Society                  0.016
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.969, macro=0.969):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.972
		Culture.Food and drink                       0.981
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.969
		Culture.Literature                           0.972
		Culture.Media.Books                          0.983
		Culture.Media.Entertainment                  0.967
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.975
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.94
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.944
		Culture.Sports                               0.975
		Culture.Visual arts.Architecture             0.981
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.976
		Culture.Visual arts.Visual arts*             0.97
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.965
		Geography.Regions.Africa.Central Africa      0.962
		Geography.Regions.Africa.Eastern Africa      0.933
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.973
		Geography.Regions.Africa.Western Africa      0.901
		Geography.Regions.Americas.Central America   0.958
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.959
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.979
		Geography.Regions.Asia.South Asia            0.972
		Geography.Regions.Asia.Southeast Asia        0.961
		Geography.Regions.Asia.West Asia             0.973
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.972
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.96
		History and Society.Business and economics   0.964
		History and Society.Education                0.965
		History and Society.History                  0.941
		History and Society.Military and warfare     0.965
		History and Society.Politics and government  0.945
		History and Society.Society                  0.919
		History and Society.Transportation           0.984
		STEM.Biology                                 0.976
		STEM.Chemistry                               0.986
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.966
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.984
		STEM.STEM*                                   0.975
		STEM.Space                                   0.991
		STEM.Technology                              0.977
		-------------------------------------------  -----
	pr_auc (micro=0.757, macro=0.607):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.938
		Culture.Biography.Women                      0.567
		Culture.Food and drink                       0.601
		Culture.Internet culture                     0.718
		Culture.Linguistics                          0.751
		Culture.Literature                           0.657
		Culture.Media.Books                          0.729
		Culture.Media.Entertainment                  0.295
		Culture.Media.Films                          0.849
		Culture.Media.Media*                         0.82
		Culture.Media.Music                          0.86
		Culture.Media.Radio                          0.557
		Culture.Media.Software                       0.465
		Culture.Media.Television                     0.739
		Culture.Media.Video games                    0.947
		Culture.Performing arts                      0.505
		Culture.Philosophy and religion              0.454
		Culture.Sports                               0.935
		Culture.Visual arts.Architecture             0.721
		Culture.Visual arts.Comics and Anime         0.752
		Culture.Visual arts.Fashion                  0.394
		Culture.Visual arts.Visual arts*             0.629
		Geography.Geographical                       0.666
		Geography.Regions.Africa.Africa*             0.554
		Geography.Regions.Africa.Central Africa      0.225
		Geography.Regions.Africa.Eastern Africa      0.303
		Geography.Regions.Africa.Northern Africa     0.325
		Geography.Regions.Africa.Southern Africa     0.618
		Geography.Regions.Africa.Western Africa      0.149
		Geography.Regions.Americas.Central America   0.38
		Geography.Regions.Americas.North America     0.762
		Geography.Regions.Americas.South America     0.813
		Geography.Regions.Asia.Asia*                 0.686
		Geography.Regions.Asia.Central Asia          0.294
		Geography.Regions.Asia.East Asia             0.81
		Geography.Regions.Asia.North Asia            0.13
		Geography.Regions.Asia.South Asia            0.797
		Geography.Regions.Asia.Southeast Asia        0.579
		Geography.Regions.Asia.West Asia             0.585
		Geography.Regions.Europe.Eastern Europe      0.606
		Geography.Regions.Europe.Europe*             0.723
		Geography.Regions.Europe.Northern Europe     0.779
		Geography.Regions.Europe.Southern Europe     0.683
		Geography.Regions.Europe.Western Europe      0.744
		Geography.Regions.Oceania                    0.707
		History and Society.Business and economics   0.59
		History and Society.Education                0.606
		History and Society.History                  0.354
		History and Society.Military and warfare     0.526
		History and Society.Politics and government  0.56
		History and Society.Society                  0.328
		History and Society.Transportation           0.902
		STEM.Biology                                 0.877
		STEM.Chemistry                               0.436
		STEM.Computing                               0.635
		STEM.Earth and environment                   0.574
		STEM.Engineering                             0.655
		STEM.Libraries & Information                 0.369
		STEM.Mathematics                             0.453
		STEM.Medicine & Health                       0.644
		STEM.Physics                                 0.248
		STEM.STEM*                                   0.892
		STEM.Space                                   0.949
		STEM.Technology                              0.454
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

