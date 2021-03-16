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
	counts (n=56444):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14111  -->  12799  1312   669  41664
			'Culture.Biography.Women'                       3558  -->   2499  1059   315  52571
			'Culture.Food and drink'                        1464  -->   1073   391   106  54874
			'Culture.Internet culture'                      2157  -->   1885   272   152  54135
			'Culture.Linguistics'                           2171  -->   1632   539   146  54127
			'Culture.Literature'                            4875  -->   3733  1142   428  51141
			'Culture.Media.Books'                           1305  -->   1071   234    86  55053
			'Culture.Media.Entertainment'                   2110  -->   1232   878   227  54107
			'Culture.Media.Films'                           3102  -->   2843   259    82  53260
			'Culture.Media.Media*'                         11523  -->  10155  1368   946  43975
			'Culture.Media.Music'                           2715  -->   2341   374   152  53577
			'Culture.Media.Radio'                            253  -->    189    64    23  56168
			'Culture.Media.Software'                        2005  -->   1869   136   170  54269
			'Culture.Media.Television'                      1733  -->   1384   349    90  54621
			'Culture.Media.Video games'                      651  -->    617    34    28  55765
			'Culture.Performing arts'                       1551  -->    974   577   118  54775
			'Culture.Philosophy and religion'               4242  -->   2414  1828   367  51835
			'Culture.Sports'                                3639  -->   2921   718   132  52673
			'Culture.Visual arts.Architecture'              2502  -->   1957   545   264  53678
			'Culture.Visual arts.Comics and Anime'          1161  -->   1017   144    46  55237
			'Culture.Visual arts.Fashion'                    618  -->    430   188    31  55795
			'Culture.Visual arts.Visual arts*'              4969  -->   3732  1237   384  51091
			'Geography.Geographical'                        4627  -->   3225  1402   661  51156
			'Geography.Regions.Africa.Africa*'              3906  -->   2647  1259   323  52215
			'Geography.Regions.Africa.Central Africa'        808  -->    500   308    89  55547
			'Geography.Regions.Africa.Eastern Africa'        360  -->    236   124    49  56035
			'Geography.Regions.Africa.Northern Africa'      1527  -->   1063   464   122  54795
			'Geography.Regions.Africa.Southern Africa'       590  -->    395   195    25  55829
			'Geography.Regions.Africa.Western Africa'         77  -->     49    28    19  56348
			'Geography.Regions.Americas.Central America'    1406  -->    814   592   136  54902
			'Geography.Regions.Americas.North America'      6544  -->   4965  1579   755  49145
			'Geography.Regions.Americas.South America'      1784  -->   1380   404   122  54538
			'Geography.Regions.Asia.Asia*'                  9866  -->   7956  1910   810  45768
			'Geography.Regions.Asia.Central Asia'            928  -->    698   230    69  55447
			'Geography.Regions.Asia.East Asia'              3315  -->   2772   543   175  52954
			'Geography.Regions.Asia.North Asia'             1410  -->   1191   219   120  54914
			'Geography.Regions.Asia.South Asia'             1800  -->   1291   509   112  54532
			'Geography.Regions.Asia.Southeast Asia'         1750  -->    968   782   213  54481
			'Geography.Regions.Asia.West Asia'              2383  -->   1851   532   141  53920
			'Geography.Regions.Europe.Eastern Europe'       3057  -->   2559   498   163  53224
			'Geography.Regions.Europe.Europe*'             16976  -->  14502  2474  1936  37532
			'Geography.Regions.Europe.Northern Europe'      4149  -->   3265   884   291  52004
			'Geography.Regions.Europe.Southern Europe'      5477  -->   4264  1213   619  50348
			'Geography.Regions.Europe.Western Europe'       5201  -->   4157  1044   394  50849
			'Geography.Regions.Oceania'                     1895  -->   1321   574   148  54401
			'History and Society.Business and economics'    3125  -->   2061  1064   224  53095
			'History and Society.Education'                 1777  -->    956   821   108  54559
			'History and Society.History'                   6150  -->   4069  2081   714  49580
			'History and Society.Military and warfare'      4199  -->   2844  1355   407  51838
			'History and Society.Politics and government'   4713  -->   2741  1972   511  51220
			'History and Society.Society'                   6946  -->   3502  3444   656  48842
			'History and Society.Transportation'            2533  -->   2156   377    92  53819
			'STEM.Biology'                                  6821  -->   6231   590   146  49477
			'STEM.Chemistry'                                1541  -->   1262   279   114  54789
			'STEM.Computing'                                2464  -->   2185   279   148  53832
			'STEM.Earth and environment'                    1875  -->   1377   498   114  54455
			'STEM.Engineering'                              2557  -->   1862   695   191  53696
			'STEM.Libraries & Information'                   476  -->    367   109    36  55932
			'STEM.Mathematics'                              1069  -->    948   121    33  55342
			'STEM.Medicine & Health'                        1942  -->   1411   531   138  54364
			'STEM.Physics'                                  1574  -->   1205   369   140  54730
			'STEM.STEM*'                                   19988  -->  18305  1683   815  35641
			'STEM.Space'                                    1879  -->   1736   143    31  54534
			'STEM.Technology'                               4389  -->   3451   938   526  51529
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.25          0.123
		Culture.Biography.Women                         0.063         0.015
		Culture.Food and drink                          0.026         0.002
		Culture.Internet culture                        0.038         0.003
		Culture.Linguistics                             0.038         0.007
		Culture.Literature                              0.086         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.037         0.004
		Culture.Media.Films                             0.055         0.011
		Culture.Media.Media*                            0.204         0.058
		Culture.Media.Music                             0.048         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.031         0.009
		Culture.Media.Video games                       0.012         0.003
		Culture.Performing arts                         0.027         0.003
		Culture.Philosophy and religion                 0.075         0.011
		Culture.Sports                                  0.064         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.088         0.018
		Geography.Geographical                          0.082         0.024
		Geography.Regions.Africa.Africa*                0.069         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.027         0.001
		Geography.Regions.Africa.Southern Africa        0.01          0.001
		Geography.Regions.Africa.Western Africa         0.001         0.001
		Geography.Regions.Americas.Central America      0.025         0.003
		Geography.Regions.Americas.North America        0.116         0.064
		Geography.Regions.Americas.South America        0.032         0.006
		Geography.Regions.Asia.Asia*                    0.175         0.045
		Geography.Regions.Asia.Central Asia             0.016         0.001
		Geography.Regions.Asia.East Asia                0.059         0.011
		Geography.Regions.Asia.North Asia               0.025         0.001
		Geography.Regions.Asia.South Asia               0.032         0.015
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.042         0.011
		Geography.Regions.Europe.Eastern Europe         0.054         0.013
		Geography.Regions.Europe.Europe*                0.301         0.076
		Geography.Regions.Europe.Northern Europe        0.074         0.031
		Geography.Regions.Europe.Southern Europe        0.097         0.013
		Geography.Regions.Europe.Western Europe         0.092         0.019
		Geography.Regions.Oceania                       0.034         0.015
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.109         0.011
		History and Society.Military and warfare        0.074         0.014
		History and Society.Politics and government     0.083         0.028
		History and Society.Society                     0.123         0.013
		History and Society.Transportation              0.045         0.015
		STEM.Biology                                    0.121         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.044         0.003
		STEM.Earth and environment                      0.033         0.005
		STEM.Engineering                                0.045         0.005
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.028         0.001
		STEM.STEM*                                      0.354         0.069
		STEM.Space                                      0.033         0.006
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.126
		Culture.Biography.Women                      0.016
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.008
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.071
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.063
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.11
		Geography.Regions.Europe.Northern Europe     0.029
		Geography.Regions.Europe.Southern Europe     0.022
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.026
		History and Society.Society                  0.019
		History and Society.Transportation           0.015
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.003
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.984
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.992
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.929
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.937
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.89
		Geography.Regions.Europe.Northern Europe     0.971
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.974
		History and Society.Society                  0.981
		History and Society.Transportation           0.985
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.997
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.803, macro=0.757):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.907
		Culture.Biography.Women                      0.702
		Culture.Food and drink                       0.733
		Culture.Internet culture                     0.874
		Culture.Linguistics                          0.752
		Culture.Literature                           0.766
		Culture.Media.Books                          0.821
		Culture.Media.Entertainment                  0.584
		Culture.Media.Films                          0.917
		Culture.Media.Media*                         0.881
		Culture.Media.Music                          0.862
		Culture.Media.Radio                          0.747
		Culture.Media.Software                       0.932
		Culture.Media.Television                     0.799
		Culture.Media.Video games                    0.948
		Culture.Performing arts                      0.628
		Culture.Philosophy and religion              0.569
		Culture.Sports                               0.803
		Culture.Visual arts.Architecture             0.782
		Culture.Visual arts.Comics and Anime         0.876
		Culture.Visual arts.Fashion                  0.696
		Culture.Visual arts.Visual arts*             0.751
		Geography.Geographical                       0.697
		Geography.Regions.Africa.Africa*             0.678
		Geography.Regions.Africa.Central Africa      0.619
		Geography.Regions.Africa.Eastern Africa      0.656
		Geography.Regions.Africa.Northern Africa     0.696
		Geography.Regions.Africa.Southern Africa     0.669
		Geography.Regions.Africa.Western Africa      0.636
		Geography.Regions.Americas.Central America   0.579
		Geography.Regions.Americas.North America     0.759
		Geography.Regions.Americas.South America     0.774
		Geography.Regions.Asia.Asia*                 0.806
		Geography.Regions.Asia.Central Asia          0.752
		Geography.Regions.Asia.East Asia             0.836
		Geography.Regions.Asia.North Asia            0.845
		Geography.Regions.Asia.South Asia            0.717
		Geography.Regions.Asia.Southeast Asia        0.553
		Geography.Regions.Asia.West Asia             0.777
		Geography.Regions.Europe.Eastern Europe      0.837
		Geography.Regions.Europe.Europe*             0.854
		Geography.Regions.Europe.Northern Europe     0.787
		Geography.Regions.Europe.Southern Europe     0.779
		Geography.Regions.Europe.Western Europe      0.799
		Geography.Regions.Oceania                    0.697
		History and Society.Business and economics   0.66
		History and Society.Education                0.538
		History and Society.History                  0.662
		History and Society.Military and warfare     0.677
		History and Society.Politics and government  0.582
		History and Society.Society                  0.504
		History and Society.Transportation           0.851
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.819
		STEM.Computing                               0.887
		STEM.Earth and environment                   0.734
		STEM.Engineering                             0.728
		STEM.Libraries & Information                 0.771
		STEM.Mathematics                             0.887
		STEM.Medicine & Health                       0.727
		STEM.Physics                                 0.766
		STEM.STEM*                                   0.916
		STEM.Space                                   0.924
		STEM.Technology                              0.786
		-------------------------------------------  -----
	!recall (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.951
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.987
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
		STEM.STEM*                                   0.978
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.728, macro=0.594):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.89
		Culture.Biography.Women                      0.635
		Culture.Food and drink                       0.484
		Culture.Internet culture                     0.523
		Culture.Linguistics                          0.673
		Culture.Literature                           0.592
		Culture.Media.Books                          0.68
		Culture.Media.Entertainment                  0.334
		Culture.Media.Films                          0.864
		Culture.Media.Media*                         0.722
		Culture.Media.Music                          0.882
		Culture.Media.Radio                          0.798
		Culture.Media.Software                       0.284
		Culture.Media.Television                     0.812
		Culture.Media.Video games                    0.832
		Culture.Performing arts                      0.458
		Culture.Philosophy and religion              0.466
		Culture.Sports                               0.961
		Culture.Visual arts.Architecture             0.631
		Culture.Visual arts.Comics and Anime         0.699
		Culture.Visual arts.Fashion                  0.503
		Culture.Visual arts.Visual arts*             0.652
		Geography.Geographical                       0.569
		Geography.Regions.Africa.Africa*             0.464
		Geography.Regions.Africa.Central Africa      0.196
		Geography.Regions.Africa.Eastern Africa      0.255
		Geography.Regions.Africa.Northern Africa     0.278
		Geography.Regions.Africa.Southern Africa     0.638
		Geography.Regions.Africa.Western Africa      0.563
		Geography.Regions.Americas.Central America   0.437
		Geography.Regions.Americas.North America     0.775
		Geography.Regions.Americas.South America     0.687
		Geography.Regions.Asia.Asia*                 0.689
		Geography.Regions.Asia.Central Asia          0.344
		Geography.Regions.Asia.East Asia             0.746
		Geography.Regions.Asia.North Asia            0.264
		Geography.Regions.Asia.South Asia            0.844
		Geography.Regions.Asia.Southeast Asia        0.462
		Geography.Regions.Asia.West Asia             0.767
		Geography.Regions.Europe.Eastern Europe      0.781
		Geography.Regions.Europe.Europe*             0.589
		Geography.Regions.Europe.Northern Europe     0.817
		Geography.Regions.Europe.Southern Europe     0.458
		Geography.Regions.Europe.Western Europe      0.67
		Geography.Regions.Oceania                    0.798
		History and Society.Business and economics   0.615
		History and Society.Education                0.669
		History and Society.History                  0.338
		History and Society.Military and warfare     0.554
		History and Society.Politics and government  0.631
		History and Society.Society                  0.327
		History and Society.Transportation           0.884
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.381
		STEM.Computing                               0.466
		STEM.Earth and environment                   0.616
		STEM.Engineering                             0.519
		STEM.Libraries & Information                 0.427
		STEM.Mathematics                             0.383
		STEM.Medicine & Health                       0.649
		STEM.Physics                                 0.203
		STEM.STEM*                                   0.753
		STEM.Space                                   0.908
		STEM.Technology                              0.286
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.987
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     1
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.999
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.985
		Culture.Visual arts.Architecture             0.998
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.988
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.997
		History and Society.Education                0.997
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.757, macro=0.649):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.898
		Culture.Biography.Women                      0.667
		Culture.Food and drink                       0.583
		Culture.Internet culture                     0.654
		Culture.Linguistics                          0.71
		Culture.Literature                           0.668
		Culture.Media.Books                          0.744
		Culture.Media.Entertainment                  0.425
		Culture.Media.Films                          0.889
		Culture.Media.Media*                         0.794
		Culture.Media.Music                          0.872
		Culture.Media.Radio                          0.771
		Culture.Media.Software                       0.436
		Culture.Media.Television                     0.805
		Culture.Media.Video games                    0.886
		Culture.Performing arts                      0.53
		Culture.Philosophy and religion              0.512
		Culture.Sports                               0.875
		Culture.Visual arts.Architecture             0.698
		Culture.Visual arts.Comics and Anime         0.777
		Culture.Visual arts.Fashion                  0.584
		Culture.Visual arts.Visual arts*             0.698
		Geography.Geographical                       0.626
		Geography.Regions.Africa.Africa*             0.551
		Geography.Regions.Africa.Central Africa      0.298
		Geography.Regions.Africa.Eastern Africa      0.367
		Geography.Regions.Africa.Northern Africa     0.397
		Geography.Regions.Africa.Southern Africa     0.653
		Geography.Regions.Africa.Western Africa      0.598
		Geography.Regions.Americas.Central America   0.498
		Geography.Regions.Americas.North America     0.767
		Geography.Regions.Americas.South America     0.728
		Geography.Regions.Asia.Asia*                 0.743
		Geography.Regions.Asia.Central Asia          0.472
		Geography.Regions.Asia.East Asia             0.788
		Geography.Regions.Asia.North Asia            0.402
		Geography.Regions.Asia.South Asia            0.775
		Geography.Regions.Asia.Southeast Asia        0.503
		Geography.Regions.Asia.West Asia             0.772
		Geography.Regions.Europe.Eastern Europe      0.808
		Geography.Regions.Europe.Europe*             0.698
		Geography.Regions.Europe.Northern Europe     0.802
		Geography.Regions.Europe.Southern Europe     0.577
		Geography.Regions.Europe.Western Europe      0.729
		Geography.Regions.Oceania                    0.744
		History and Society.Business and economics   0.637
		History and Society.Education                0.596
		History and Society.History                  0.447
		History and Society.Military and warfare     0.609
		History and Society.Politics and government  0.605
		History and Society.Society                  0.397
		History and Society.Transportation           0.867
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.52
		STEM.Computing                               0.611
		STEM.Earth and environment                   0.67
		STEM.Engineering                             0.606
		STEM.Libraries & Information                 0.55
		STEM.Mathematics                             0.535
		STEM.Medicine & Health                       0.686
		STEM.Physics                                 0.321
		STEM.STEM*                                   0.826
		STEM.Space                                   0.916
		STEM.Technology                              0.42
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.986
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.986
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.98, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.996
		Culture.Literature                           0.988
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.991
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.992
		History and Society.Education                0.995
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.979
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.973
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.013, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.016
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.003
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.021
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.003
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.049
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.012
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.004
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.013
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
		STEM.STEM*                                   0.022
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.977, macro=0.975):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.984
		Culture.Literature                           0.979
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.982
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.939
		Culture.Media.Software                       0.99
		Culture.Media.Television                     0.986
		Culture.Media.Video games                    0.983
		Culture.Performing arts                      0.974
		Culture.Philosophy and religion              0.959
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.984
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.982
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.974
		Geography.Regions.Africa.Central Africa      0.981
		Geography.Regions.Africa.Eastern Africa      0.963
		Geography.Regions.Africa.Northern Africa     0.977
		Geography.Regions.Africa.Southern Africa     0.968
		Geography.Regions.Africa.Western Africa      0.839
		Geography.Regions.Americas.Central America   0.971
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.983
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.983
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.988
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.969
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.979
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.979
		History and Society.Business and economics   0.972
		History and Society.Education                0.971
		History and Society.History                  0.963
		History and Society.Military and warfare     0.974
		History and Society.Politics and government  0.956
		History and Society.Society                  0.937
		History and Society.Transportation           0.985
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.987
		STEM.Computing                               0.989
		STEM.Earth and environment                   0.981
		STEM.Engineering                             0.977
		STEM.Libraries & Information                 0.956
		STEM.Mathematics                             0.989
		STEM.Medicine & Health                       0.978
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.981
		STEM.Space                                   0.994
		STEM.Technology                              0.979
		-------------------------------------------  -----
	pr_auc (micro=0.813, macro=0.66):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.956
		Culture.Biography.Women                      0.68
		Culture.Food and drink                       0.672
		Culture.Internet culture                     0.721
		Culture.Linguistics                          0.787
		Culture.Literature                           0.712
		Culture.Media.Books                          0.768
		Culture.Media.Entertainment                  0.371
		Culture.Media.Films                          0.919
		Culture.Media.Media*                         0.89
		Culture.Media.Music                          0.869
		Culture.Media.Radio                          0.59
		Culture.Media.Software                       0.575
		Culture.Media.Television                     0.866
		Culture.Media.Video games                    0.891
		Culture.Performing arts                      0.469
		Culture.Philosophy and religion              0.491
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.739
		Culture.Visual arts.Comics and Anime         0.739
		Culture.Visual arts.Fashion                  0.465
		Culture.Visual arts.Visual arts*             0.743
		Geography.Geographical                       0.664
		Geography.Regions.Africa.Africa*             0.579
		Geography.Regions.Africa.Central Africa      0.209
		Geography.Regions.Africa.Eastern Africa      0.184
		Geography.Regions.Africa.Northern Africa     0.319
		Geography.Regions.Africa.Southern Africa     0.531
		Geography.Regions.Africa.Western Africa      0.382
		Geography.Regions.Americas.Central America   0.454
		Geography.Regions.Americas.North America     0.844
		Geography.Regions.Americas.South America     0.793
		Geography.Regions.Asia.Asia*                 0.826
		Geography.Regions.Asia.Central Asia          0.339
		Geography.Regions.Asia.East Asia             0.803
		Geography.Regions.Asia.North Asia            0.424
		Geography.Regions.Asia.South Asia            0.814
		Geography.Regions.Asia.Southeast Asia        0.496
		Geography.Regions.Asia.West Asia             0.792
		Geography.Regions.Europe.Eastern Europe      0.814
		Geography.Regions.Europe.Europe*             0.815
		Geography.Regions.Europe.Northern Europe     0.847
		Geography.Regions.Europe.Southern Europe     0.657
		Geography.Regions.Europe.Western Europe      0.803
		Geography.Regions.Oceania                    0.778
		History and Society.Business and economics   0.657
		History and Society.Education                0.586
		History and Society.History                  0.476
		History and Society.Military and warfare     0.665
		History and Society.Politics and government  0.633
		History and Society.Society                  0.377
		History and Society.Transportation           0.913
		STEM.Biology                                 0.96
		STEM.Chemistry                               0.501
		STEM.Computing                               0.706
		STEM.Earth and environment                   0.672
		STEM.Engineering                             0.67
		STEM.Libraries & Information                 0.413
		STEM.Mathematics                             0.648
		STEM.Medicine & Health                       0.718
		STEM.Physics                                 0.255
		STEM.STEM*                                   0.931
		STEM.Space                                   0.957
		STEM.Technology                              0.49
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

