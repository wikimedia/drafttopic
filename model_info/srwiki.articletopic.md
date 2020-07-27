Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'presort': 'deprecated', 'multilabel': True, 'tol': 0.0001, 'learning_rate': 0.1, 'min_samples_split': 2, 'loss': 'deviance', 'random_state': None, 'n_estimators': 150, 'n_iter_no_change': None, 'max_features': 'log2', 'validation_fraction': 0.1, 'ccp_alpha': 0.0, 'subsample': 1.0, 'max_leaf_nodes': None, 'center': False, 'min_weight_fraction_leaf': 0.0, 'min_impurity_decrease': 0.0, 'criterion': 'friedman_mse', 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_samples_leaf': 1, 'max_depth': 5, 'warm_start': False, 'label_weights': {}, 'population_rates': None, 'verbose': 0, 'min_impurity_split': None, 'init': None}
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
	counts (n=57232):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13351  -->  11963  1388   749  43132
			'Culture.Biography.Women'                       3639  -->   2863   776   282  53311
			'Culture.Food and drink'                        1413  -->    842   571   170  55649
			'Culture.Internet culture'                      3014  -->   2542   472   271  53947
			'Culture.Linguistics'                           1565  -->   1055   510   121  55546
			'Culture.Literature'                            4944  -->   3669  1275   423  51865
			'Culture.Media.Books'                           1547  -->   1215   332   105  55580
			'Culture.Media.Entertainment'                   2216  -->   1170  1046   213  54803
			'Culture.Media.Films'                           2704  -->   2349   355   112  54416
			'Culture.Media.Media*'                         12711  -->  11268  1443  1228  43293
			'Culture.Media.Music'                           2650  -->   2149   501   190  54392
			'Culture.Media.Radio'                            267  -->    187    80    29  56936
			'Culture.Media.Software'                        2229  -->   1939   290   289  54714
			'Culture.Media.Television'                      2426  -->   2051   375   122  54684
			'Culture.Media.Video games'                     1475  -->   1398    77    34  55723
			'Culture.Performing arts'                       1448  -->    763   685   131  55653
			'Culture.Philosophy and religion'               4058  -->   2202  1856   446  52728
			'Culture.Sports'                                5247  -->   4624   623   172  51813
			'Culture.Visual arts.Architecture'              2049  -->   1276   773   239  54944
			'Culture.Visual arts.Comics and Anime'          1202  -->   1006   196    57  55973
			'Culture.Visual arts.Fashion'                    654  -->    333   321    41  56537
			'Culture.Visual arts.Visual arts*'              4544  -->   2872  1672   385  52303
			'Geography.Geographical'                        4977  -->   3604  1373   846  51409
			'Geography.Regions.Africa.Africa*'              3799  -->   2586  1213   258  53175
			'Geography.Regions.Africa.Central Africa'        543  -->    274   269    62  56627
			'Geography.Regions.Africa.Eastern Africa'        408  -->    240   168    38  56786
			'Geography.Regions.Africa.Northern Africa'      1444  -->    986   458   117  55671
			'Geography.Regions.Africa.Southern Africa'       622  -->    376   246    36  56574
			'Geography.Regions.Africa.Western Africa'        139  -->     96    43    23  57070
			'Geography.Regions.Americas.Central America'    1301  -->    521   780    89  55842
			'Geography.Regions.Americas.North America'      6159  -->   4288  1871   748  50325
			'Geography.Regions.Americas.South America'      1530  -->    971   559    94  55608
			'Geography.Regions.Asia.Asia*'                 10831  -->   8595  2236   795  45606
			'Geography.Regions.Asia.Central Asia'            884  -->    510   374    85  56263
			'Geography.Regions.Asia.East Asia'              2441  -->   1865   576   131  54660
			'Geography.Regions.Asia.North Asia'             3464  -->   2601   863   264  53504
			'Geography.Regions.Asia.South Asia'             1648  -->   1075   573    90  55494
			'Geography.Regions.Asia.Southeast Asia'         1475  -->    887   588    93  55664
			'Geography.Regions.Asia.West Asia'              2529  -->   1750   779   201  54502
			'Geography.Regions.Europe.Eastern Europe'       5416  -->   4111  1305   369  51447
			'Geography.Regions.Europe.Europe*'             17865  -->  14706  3159  2025  37342
			'Geography.Regions.Europe.Northern Europe'      3218  -->   2082  1136   276  53738
			'Geography.Regions.Europe.Southern Europe'      6108  -->   4689  1419   699  50425
			'Geography.Regions.Europe.Western Europe'       4361  -->   3267  1094   331  52540
			'Geography.Regions.Oceania'                     1865  -->   1285   580    97  55270
			'History and Society.Business and economics'    3012  -->   1664  1348   295  53925
			'History and Society.Education'                 1645  -->    752   893   129  55458
			'History and Society.History'                   6442  -->   4148  2294   920  49870
			'History and Society.Military and warfare'      4946  -->   3533  1413   531  51755
			'History and Society.Politics and government'   4421  -->   2494  1927   500  52311
			'History and Society.Society'                   4449  -->   1266  3183   381  52402
			'History and Society.Transportation'            3186  -->   2855   331   108  53938
			'STEM.Biology'                                  3821  -->   3173   648   190  53221
			'STEM.Chemistry'                                2073  -->   1542   531   304  54855
			'STEM.Computing'                                2684  -->   2336   348   286  54262
			'STEM.Earth and environment'                    1709  -->   1011   698   187  55336
			'STEM.Engineering'                              2697  -->   2095   602   159  54376
			'STEM.Libraries & Information'                   503  -->    385   118    34  56695
			'STEM.Mathematics'                               549  -->    321   228    36  56647
			'STEM.Medicine & Health'                        2394  -->   1695   699   273  54565
			'STEM.Physics'                                  1403  -->   1009   394   152  55677
			'STEM.STEM*'                                   18244  -->  16459  1785   993  37995
			'STEM.Space'                                    2129  -->   1970   159    24  55079
			'STEM.Technology'                               4564  -->   3452  1112   597  52071
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.233         0.12
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.053         0.004
		Culture.Linguistics                             0.027         0.008
		Culture.Literature                              0.086         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.047         0.012
		Culture.Media.Media*                            0.222         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.039         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.026         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.071         0.01
		Culture.Sports                                  0.092         0.06
		Culture.Visual arts.Architecture                0.036         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.079         0.018
		Geography.Geographical                          0.087         0.021
		Geography.Regions.Africa.Africa*                0.066         0.008
		Geography.Regions.Africa.Central Africa         0.009         0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.002         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.108         0.063
		Geography.Regions.Americas.South America        0.027         0.007
		Geography.Regions.Asia.Asia*                    0.189         0.052
		Geography.Regions.Asia.Central Asia             0.015         0.001
		Geography.Regions.Asia.East Asia                0.043         0.012
		Geography.Regions.Asia.North Asia               0.061         0.006
		Geography.Regions.Asia.South Asia               0.029         0.016
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.044         0.012
		Geography.Regions.Europe.Eastern Europe         0.095         0.018
		Geography.Regions.Europe.Europe*                0.312         0.081
		Geography.Regions.Europe.Northern Europe        0.056         0.029
		Geography.Regions.Europe.Southern Europe        0.107         0.014
		Geography.Regions.Europe.Western Europe         0.076         0.02
		Geography.Regions.Oceania                       0.033         0.016
		History and Society.Business and economics      0.053         0.01
		History and Society.Education                   0.029         0.008
		History and Society.History                     0.113         0.011
		History and Society.Military and warfare        0.086         0.015
		History and Society.Politics and government     0.077         0.028
		History and Society.Society                     0.078         0.008
		History and Society.Transportation              0.056         0.016
		STEM.Biology                                    0.067         0.034
		STEM.Chemistry                                  0.036         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.047         0.006
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.01          0
		STEM.Medicine & Health                          0.042         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.319         0.065
		STEM.Space                                      0.037         0.004
		STEM.Technology                                 0.08          0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.123
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.005
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.008
		Culture.Literature                           0.019
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.075
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.019
		Geography.Geographical                       0.031
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.058
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.012
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.114
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.024
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.025
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.025
		History and Society.Society                  0.01
		History and Society.Transportation           0.017
		STEM.Biology                                 0.032
		STEM.Chemistry                               0.007
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.009
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.004
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.995
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.992
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.925
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.981
		Geography.Geographical                       0.969
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.942
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.988
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.886
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.976
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.975
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.975
		History and Society.Society                  0.99
		History and Society.Transportation           0.983
		STEM.Biology                                 0.968
		STEM.Chemistry                               0.993
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.996
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.774, macro=0.705):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.896
		Culture.Biography.Women                      0.787
		Culture.Food and drink                       0.596
		Culture.Internet culture                     0.843
		Culture.Linguistics                          0.674
		Culture.Literature                           0.742
		Culture.Media.Books                          0.785
		Culture.Media.Entertainment                  0.528
		Culture.Media.Films                          0.869
		Culture.Media.Media*                         0.886
		Culture.Media.Music                          0.811
		Culture.Media.Radio                          0.7
		Culture.Media.Software                       0.87
		Culture.Media.Television                     0.845
		Culture.Media.Video games                    0.948
		Culture.Performing arts                      0.527
		Culture.Philosophy and religion              0.543
		Culture.Sports                               0.881
		Culture.Visual arts.Architecture             0.623
		Culture.Visual arts.Comics and Anime         0.837
		Culture.Visual arts.Fashion                  0.509
		Culture.Visual arts.Visual arts*             0.632
		Geography.Geographical                       0.724
		Geography.Regions.Africa.Africa*             0.681
		Geography.Regions.Africa.Central Africa      0.505
		Geography.Regions.Africa.Eastern Africa      0.588
		Geography.Regions.Africa.Northern Africa     0.683
		Geography.Regions.Africa.Southern Africa     0.605
		Geography.Regions.Africa.Western Africa      0.691
		Geography.Regions.Americas.Central America   0.4
		Geography.Regions.Americas.North America     0.696
		Geography.Regions.Americas.South America     0.635
		Geography.Regions.Asia.Asia*                 0.794
		Geography.Regions.Asia.Central Asia          0.577
		Geography.Regions.Asia.East Asia             0.764
		Geography.Regions.Asia.North Asia            0.751
		Geography.Regions.Asia.South Asia            0.652
		Geography.Regions.Asia.Southeast Asia        0.601
		Geography.Regions.Asia.West Asia             0.692
		Geography.Regions.Europe.Eastern Europe      0.759
		Geography.Regions.Europe.Europe*             0.823
		Geography.Regions.Europe.Northern Europe     0.647
		Geography.Regions.Europe.Southern Europe     0.768
		Geography.Regions.Europe.Western Europe      0.749
		Geography.Regions.Oceania                    0.689
		History and Society.Business and economics   0.552
		History and Society.Education                0.457
		History and Society.History                  0.644
		History and Society.Military and warfare     0.714
		History and Society.Politics and government  0.564
		History and Society.Society                  0.285
		History and Society.Transportation           0.896
		STEM.Biology                                 0.83
		STEM.Chemistry                               0.744
		STEM.Computing                               0.87
		STEM.Earth and environment                   0.592
		STEM.Engineering                             0.777
		STEM.Libraries & Information                 0.765
		STEM.Mathematics                             0.585
		STEM.Medicine & Health                       0.708
		STEM.Physics                                 0.719
		STEM.STEM*                                   0.902
		STEM.Space                                   0.925
		STEM.Technology                              0.756
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.982
		History and Society.Military and warfare     0.99
		History and Society.Politics and government  0.991
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.994
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   1
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.704, macro=0.568):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.694
		Culture.Food and drink                       0.333
		Culture.Internet culture                     0.387
		Culture.Linguistics                          0.715
		Culture.Literature                           0.58
		Culture.Media.Books                          0.643
		Culture.Media.Entertainment                  0.35
		Culture.Media.Films                          0.831
		Culture.Media.Media*                         0.65
		Culture.Media.Music                          0.833
		Culture.Media.Radio                          0.762
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.773
		Culture.Media.Video games                    0.819
		Culture.Performing arts                      0.407
		Culture.Philosophy and religion              0.403
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.61
		Culture.Visual arts.Comics and Anime         0.663
		Culture.Visual arts.Fashion                  0.386
		Culture.Visual arts.Visual arts*             0.614
		Geography.Geographical                       0.491
		Geography.Regions.Africa.Africa*             0.546
		Geography.Regions.Africa.Central Africa      0.245
		Geography.Regions.Africa.Eastern Africa      0.306
		Geography.Regions.Africa.Northern Africa     0.305
		Geography.Regions.Africa.Southern Africa     0.554
		Geography.Regions.Africa.Western Africa      0.561
		Geography.Regions.Americas.Central America   0.465
		Geography.Regions.Americas.North America     0.761
		Geography.Regions.Americas.South America     0.721
		Geography.Regions.Asia.Asia*                 0.719
		Geography.Regions.Asia.Central Asia          0.233
		Geography.Regions.Asia.East Asia             0.797
		Geography.Regions.Asia.North Asia            0.462
		Geography.Regions.Asia.South Asia            0.871
		Geography.Regions.Asia.Southeast Asia        0.693
		Geography.Regions.Asia.West Asia             0.69
		Geography.Regions.Europe.Eastern Europe      0.665
		Geography.Regions.Europe.Europe*             0.584
		Geography.Regions.Europe.Northern Europe     0.79
		Geography.Regions.Europe.Southern Europe     0.44
		Geography.Regions.Europe.Western Europe      0.714
		Geography.Regions.Oceania                    0.868
		History and Society.Business and economics   0.499
		History and Society.Education                0.611
		History and Society.History                  0.281
		History and Society.Military and warfare     0.522
		History and Society.Politics and government  0.631
		History and Society.Society                  0.247
		History and Society.Transportation           0.881
		STEM.Biology                                 0.893
		STEM.Chemistry                               0.186
		STEM.Computing                               0.319
		STEM.Earth and environment                   0.454
		STEM.Engineering                             0.606
		STEM.Libraries & Information                 0.466
		STEM.Mathematics                             0.298
		STEM.Medicine & Health                       0.479
		STEM.Physics                                 0.198
		STEM.STEM*                                   0.711
		STEM.Space                                   0.901
		STEM.Technology                              0.256
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.984
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.988
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.994
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.993
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.729, macro=0.61):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.887
		Culture.Biography.Women                      0.737
		Culture.Food and drink                       0.427
		Culture.Internet culture                     0.53
		Culture.Linguistics                          0.694
		Culture.Literature                           0.651
		Culture.Media.Books                          0.707
		Culture.Media.Entertainment                  0.421
		Culture.Media.Films                          0.85
		Culture.Media.Media*                         0.75
		Culture.Media.Music                          0.822
		Culture.Media.Radio                          0.73
		Culture.Media.Software                       0.295
		Culture.Media.Television                     0.807
		Culture.Media.Video games                    0.879
		Culture.Performing arts                      0.459
		Culture.Philosophy and religion              0.463
		Culture.Sports                               0.912
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.74
		Culture.Visual arts.Fashion                  0.439
		Culture.Visual arts.Visual arts*             0.623
		Geography.Geographical                       0.585
		Geography.Regions.Africa.Africa*             0.606
		Geography.Regions.Africa.Central Africa      0.33
		Geography.Regions.Africa.Eastern Africa      0.403
		Geography.Regions.Africa.Northern Africa     0.422
		Geography.Regions.Africa.Southern Africa     0.578
		Geography.Regions.Africa.Western Africa      0.619
		Geography.Regions.Americas.Central America   0.43
		Geography.Regions.Americas.North America     0.727
		Geography.Regions.Americas.South America     0.675
		Geography.Regions.Asia.Asia*                 0.755
		Geography.Regions.Asia.Central Asia          0.332
		Geography.Regions.Asia.East Asia             0.78
		Geography.Regions.Asia.North Asia            0.572
		Geography.Regions.Asia.South Asia            0.746
		Geography.Regions.Asia.Southeast Asia        0.644
		Geography.Regions.Asia.West Asia             0.691
		Geography.Regions.Europe.Eastern Europe      0.709
		Geography.Regions.Europe.Europe*             0.683
		Geography.Regions.Europe.Northern Europe     0.712
		Geography.Regions.Europe.Southern Europe     0.559
		Geography.Regions.Europe.Western Europe      0.731
		Geography.Regions.Oceania                    0.768
		History and Society.Business and economics   0.524
		History and Society.Education                0.523
		History and Society.History                  0.391
		History and Society.Military and warfare     0.603
		History and Society.Politics and government  0.596
		History and Society.Society                  0.264
		History and Society.Transportation           0.888
		STEM.Biology                                 0.86
		STEM.Chemistry                               0.297
		STEM.Computing                               0.467
		STEM.Earth and environment                   0.514
		STEM.Engineering                             0.681
		STEM.Libraries & Information                 0.579
		STEM.Mathematics                             0.395
		STEM.Medicine & Health                       0.571
		STEM.Physics                                 0.311
		STEM.STEM*                                   0.795
		STEM.Space                                   0.913
		STEM.Technology                              0.383
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.984
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
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
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   1
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.979, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.995
		Culture.Literature                           0.988
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.985
		Geography.Regions.Europe.Southern Europe     0.983
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.99
		History and Society.Education                0.993
		History and Society.History                  0.978
		History and Society.Military and warfare     0.986
		History and Society.Politics and government  0.979
		History and Society.Society                  0.987
		History and Society.Transportation           0.996
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.994
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.008
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.028
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.016
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.051
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.006
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.018
		History and Society.Military and warfare     0.01
		History and Society.Politics and government  0.009
		History and Society.Society                  0.007
		History and Society.Transportation           0.002
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.006
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.988
		Culture.Linguistics                          0.974
		Culture.Literature                           0.977
		Culture.Media.Books                          0.985
		Culture.Media.Entertainment                  0.971
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.935
		Culture.Media.Software                       0.988
		Culture.Media.Television                     0.986
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.968
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.962
		Culture.Visual arts.Visual arts*             0.964
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.973
		Geography.Regions.Africa.Central Africa      0.979
		Geography.Regions.Africa.Eastern Africa      0.956
		Geography.Regions.Africa.Northern Africa     0.977
		Geography.Regions.Africa.Southern Africa     0.97
		Geography.Regions.Africa.Western Africa      0.908
		Geography.Regions.Americas.Central America   0.96
		Geography.Regions.Americas.North America     0.967
		Geography.Regions.Americas.South America     0.974
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.971
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.976
		Geography.Regions.Asia.South Asia            0.974
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.974
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.959
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.976
		Geography.Regions.Europe.Western Europe      0.974
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.958
		History and Society.Education                0.961
		History and Society.History                  0.959
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.955
		History and Society.Society                  0.905
		History and Society.Transportation           0.985
		STEM.Biology                                 0.981
		STEM.Chemistry                               0.987
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.973
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.961
		STEM.Mathematics                             0.97
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.979
		STEM.Space                                   0.995
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.775, macro=0.601):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.946
		Culture.Biography.Women                      0.743
		Culture.Food and drink                       0.364
		Culture.Internet culture                     0.706
		Culture.Linguistics                          0.693
		Culture.Literature                           0.709
		Culture.Media.Books                          0.714
		Culture.Media.Entertainment                  0.324
		Culture.Media.Films                          0.877
		Culture.Media.Media*                         0.848
		Culture.Media.Music                          0.852
		Culture.Media.Radio                          0.503
		Culture.Media.Software                       0.352
		Culture.Media.Television                     0.825
		Culture.Media.Video games                    0.906
		Culture.Performing arts                      0.358
		Culture.Philosophy and religion              0.471
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.606
		Culture.Visual arts.Comics and Anime         0.765
		Culture.Visual arts.Fashion                  0.247
		Culture.Visual arts.Visual arts*             0.629
		Geography.Geographical                       0.603
		Geography.Regions.Africa.Africa*             0.588
		Geography.Regions.Africa.Central Africa      0.178
		Geography.Regions.Africa.Eastern Africa      0.191
		Geography.Regions.Africa.Northern Africa     0.322
		Geography.Regions.Africa.Southern Africa     0.435
		Geography.Regions.Africa.Western Africa      0.379
		Geography.Regions.Americas.Central America   0.384
		Geography.Regions.Americas.North America     0.798
		Geography.Regions.Americas.South America     0.689
		Geography.Regions.Asia.Asia*                 0.817
		Geography.Regions.Asia.Central Asia          0.195
		Geography.Regions.Asia.East Asia             0.808
		Geography.Regions.Asia.North Asia            0.572
		Geography.Regions.Asia.South Asia            0.807
		Geography.Regions.Asia.Southeast Asia        0.615
		Geography.Regions.Asia.West Asia             0.711
		Geography.Regions.Europe.Eastern Europe      0.776
		Geography.Regions.Europe.Europe*             0.788
		Geography.Regions.Europe.Northern Europe     0.758
		Geography.Regions.Europe.Southern Europe     0.615
		Geography.Regions.Europe.Western Europe      0.778
		Geography.Regions.Oceania                    0.817
		History and Society.Business and economics   0.462
		History and Society.Education                0.476
		History and Society.History                  0.417
		History and Society.Military and warfare     0.643
		History and Society.Politics and government  0.615
		History and Society.Society                  0.18
		History and Society.Transportation           0.911
		STEM.Biology                                 0.883
		STEM.Chemistry                               0.294
		STEM.Computing                               0.476
		STEM.Earth and environment                   0.478
		STEM.Engineering                             0.74
		STEM.Libraries & Information                 0.429
		STEM.Mathematics                             0.182
		STEM.Medicine & Health                       0.581
		STEM.Physics                                 0.329
		STEM.STEM*                                   0.893
		STEM.Space                                   0.954
		STEM.Technology                              0.484
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

