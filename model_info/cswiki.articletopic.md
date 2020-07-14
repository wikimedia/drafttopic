Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'init': None, 'population_rates': None, 'max_depth': 5, 'verbose': 0, 'ccp_alpha': 0.0, 'validation_fraction': 0.1, 'warm_start': False, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'max_leaf_nodes': None, 'subsample': 1.0, 'tol': 0.0001, 'presort': 'deprecated', 'min_samples_split': 2, 'random_state': None, 'min_samples_leaf': 1, 'center': False, 'multilabel': True, 'max_features': 'log2', 'learning_rate': 0.1, 'n_estimators': 150, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'label_weights': {}, 'criterion': 'friedman_mse', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'scale': False}
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
	counts (n=60197):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16411  -->  15081  1330   830  42956
			'Culture.Biography.Women'                       4309  -->   3613   696   285  55603
			'Culture.Food and drink'                        1598  -->   1140   458   116  58483
			'Culture.Internet culture'                      3175  -->   2600   575   242  56780
			'Culture.Linguistics'                           1610  -->   1149   461    86  58501
			'Culture.Literature'                            4968  -->   3573  1395   516  54713
			'Culture.Media.Books'                           1697  -->   1332   365   136  58364
			'Culture.Media.Entertainment'                   2268  -->   1029  1239   307  57622
			'Culture.Media.Films'                           2531  -->   2078   453   115  57551
			'Culture.Media.Media*'                         14349  -->  12485  1864  1361  44487
			'Culture.Media.Music'                           3307  -->   2782   525   261  56629
			'Culture.Media.Radio'                            425  -->    198   227    41  59731
			'Culture.Media.Software'                        2392  -->   1841   551   352  57453
			'Culture.Media.Television'                      2548  -->   2167   381   121  57528
			'Culture.Media.Video games'                     1896  -->   1727   169    49  58252
			'Culture.Performing arts'                       1520  -->    960   560   134  58543
			'Culture.Philosophy and religion'               4401  -->   2479  1922   454  55342
			'Culture.Sports'                                5891  -->   5267   624   191  54115
			'Culture.Visual arts.Architecture'              2309  -->   1650   659   240  57648
			'Culture.Visual arts.Comics and Anime'          1679  -->   1436   243    43  58475
			'Culture.Visual arts.Fashion'                   1059  -->    702   357    83  59055
			'Culture.Visual arts.Visual arts*'              5915  -->   4343  1572   432  53850
			'Geography.Geographical'                        4652  -->   3358  1294   725  54820
			'Geography.Regions.Africa.Africa*'              4090  -->   2581  1509   309  55798
			'Geography.Regions.Africa.Central Africa'        732  -->    332   400    74  59391
			'Geography.Regions.Africa.Eastern Africa'        474  -->    259   215    37  59686
			'Geography.Regions.Africa.Northern Africa'      1558  -->    938   620   122  58517
			'Geography.Regions.Africa.Southern Africa'       675  -->    312   363    59  59463
			'Geography.Regions.Africa.Western Africa'        187  -->     82   105    32  59978
			'Geography.Regions.Americas.Central America'    1354  -->    637   717    77  58766
			'Geography.Regions.Americas.North America'      6020  -->   3695  2325   981  53196
			'Geography.Regions.Americas.South America'      1478  -->    997   481   104  58615
			'Geography.Regions.Asia.Asia*'                 10847  -->   8568  2279   888  48462
			'Geography.Regions.Asia.Central Asia'           1311  -->    813   498   117  58769
			'Geography.Regions.Asia.East Asia'              2966  -->   2257   709   188  57043
			'Geography.Regions.Asia.North Asia'             1944  -->   1268   676   292  57961
			'Geography.Regions.Asia.South Asia'             1814  -->   1327   487    96  58287
			'Geography.Regions.Asia.Southeast Asia'         1603  -->    925   678    88  58506
			'Geography.Regions.Asia.West Asia'              2874  -->   2191   683   175  57148
			'Geography.Regions.Europe.Eastern Europe'       5252  -->   3745  1507   665  54280
			'Geography.Regions.Europe.Europe*'             16883  -->  13054  3829  2544  40770
			'Geography.Regions.Europe.Northern Europe'      4019  -->   2435  1584   447  55731
			'Geography.Regions.Europe.Southern Europe'      3488  -->   2254  1234   338  56371
			'Geography.Regions.Europe.Western Europe'       5209  -->   3621  1588   641  54347
			'Geography.Regions.Oceania'                     1774  -->   1198   576    87  58336
			'History and Society.Business and economics'    3567  -->   2068  1499   361  56269
			'History and Society.Education'                 1821  -->    872   949   154  58222
			'History and Society.History'                   5592  -->   3331  2261   695  53910
			'History and Society.Military and warfare'      5797  -->   4112  1685   591  53809
			'History and Society.Politics and government'   4709  -->   2502  2207   519  54969
			'History and Society.Society'                   6861  -->   3083  3778   693  52643
			'History and Society.Transportation'            4282  -->   3865   417   165  55750
			'STEM.Biology'                                  3828  -->   3077   751   187  56182
			'STEM.Chemistry'                                1607  -->   1290   317   147  58443
			'STEM.Computing'                                2851  -->   2322   529   429  56917
			'STEM.Earth and environment'                    2224  -->   1458   766   159  57814
			'STEM.Engineering'                              2978  -->   2273   705   228  56991
			'STEM.Libraries & Information'                   717  -->    467   250    57  59423
			'STEM.Mathematics'                              1208  -->    937   271    77  58912
			'STEM.Medicine & Health'                        2098  -->   1387   711   215  57884
			'STEM.Physics'                                  1466  -->    960   506   158  58573
			'STEM.STEM*'                                   19061  -->  16828  2233  1061  40075
			'STEM.Space'                                    2057  -->   1868   189    48  58092
			'STEM.Technology'                               5209  -->   3765  1444   711  54277
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.273         0.123
		Culture.Biography.Women                         0.072         0.015
		Culture.Food and drink                          0.027         0.002
		Culture.Internet culture                        0.053         0.003
		Culture.Linguistics                             0.027         0.007
		Culture.Literature                              0.083         0.015
		Culture.Media.Books                             0.028         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.042         0.011
		Culture.Media.Media*                            0.238         0.058
		Culture.Media.Music                             0.055         0.024
		Culture.Media.Radio                             0.007         0.002
		Culture.Media.Software                          0.04          0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.031         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.098         0.071
		Culture.Visual arts.Architecture                0.038         0.011
		Culture.Visual arts.Comics and Anime            0.028         0.002
		Culture.Visual arts.Fashion                     0.018         0.001
		Culture.Visual arts.Visual arts*                0.098         0.018
		Geography.Geographical                          0.077         0.024
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.012         0.001
		Geography.Regions.Africa.Eastern Africa         0.008         0
		Geography.Regions.Africa.Northern Africa        0.026         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.003         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.1           0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.18          0.045
		Geography.Regions.Asia.Central Asia             0.022         0.001
		Geography.Regions.Asia.East Asia                0.049         0.011
		Geography.Regions.Asia.North Asia               0.032         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.048         0.011
		Geography.Regions.Europe.Eastern Europe         0.087         0.013
		Geography.Regions.Europe.Europe*                0.28          0.076
		Geography.Regions.Europe.Northern Europe        0.067         0.031
		Geography.Regions.Europe.Southern Europe        0.058         0.013
		Geography.Regions.Europe.Western Europe         0.087         0.019
		Geography.Regions.Oceania                       0.029         0.015
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.03          0.007
		History and Society.History                     0.093         0.011
		History and Society.Military and warfare        0.096         0.014
		History and Society.Politics and government     0.078         0.028
		History and Society.Society                     0.114         0.013
		History and Society.Transportation              0.071         0.015
		STEM.Biology                                    0.064         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.047         0.003
		STEM.Earth and environment                      0.037         0.005
		STEM.Engineering                                0.049         0.005
		STEM.Libraries & Information                    0.012         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.035         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.317         0.069
		STEM.Space                                      0.034         0.006
		STEM.Technology                                 0.087         0.005
	match_rate (micro=0.054, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.13
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.007
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.079
		Culture.Media.Music                          0.025
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.014
		Culture.Sports                               0.067
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.03
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.056
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.053
		Geography.Regions.Asia.Central Asia          0.003
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.006
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.021
		Geography.Regions.Europe.Europe*             0.113
		Geography.Regions.Europe.Northern Europe     0.026
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.025
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.019
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.024
		History and Society.Society                  0.018
		History and Society.Transportation           0.017
		STEM.Biology                                 0.03
		STEM.Chemistry                               0.004
		STEM.Computing                               0.01
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.085
		STEM.Space                                   0.006
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.946, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.87
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.921
		Culture.Media.Music                          0.975
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.986
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.947
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.979
		Geography.Regions.Europe.Europe*             0.887
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.975
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.983
		STEM.Biology                                 0.97
		STEM.Chemistry                               0.996
		STEM.Computing                               0.99
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.915
		STEM.Space                                   0.994
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.767, macro=0.695):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.919
		Culture.Biography.Women                      0.838
		Culture.Food and drink                       0.713
		Culture.Internet culture                     0.819
		Culture.Linguistics                          0.714
		Culture.Literature                           0.719
		Culture.Media.Books                          0.785
		Culture.Media.Entertainment                  0.454
		Culture.Media.Films                          0.821
		Culture.Media.Media*                         0.87
		Culture.Media.Music                          0.841
		Culture.Media.Radio                          0.466
		Culture.Media.Software                       0.77
		Culture.Media.Television                     0.85
		Culture.Media.Video games                    0.911
		Culture.Performing arts                      0.632
		Culture.Philosophy and religion              0.563
		Culture.Sports                               0.894
		Culture.Visual arts.Architecture             0.715
		Culture.Visual arts.Comics and Anime         0.855
		Culture.Visual arts.Fashion                  0.663
		Culture.Visual arts.Visual arts*             0.734
		Geography.Geographical                       0.722
		Geography.Regions.Africa.Africa*             0.631
		Geography.Regions.Africa.Central Africa      0.454
		Geography.Regions.Africa.Eastern Africa      0.546
		Geography.Regions.Africa.Northern Africa     0.602
		Geography.Regions.Africa.Southern Africa     0.462
		Geography.Regions.Africa.Western Africa      0.439
		Geography.Regions.Americas.Central America   0.47
		Geography.Regions.Americas.North America     0.614
		Geography.Regions.Americas.South America     0.675
		Geography.Regions.Asia.Asia*                 0.79
		Geography.Regions.Asia.Central Asia          0.62
		Geography.Regions.Asia.East Asia             0.761
		Geography.Regions.Asia.North Asia            0.652
		Geography.Regions.Asia.South Asia            0.732
		Geography.Regions.Asia.Southeast Asia        0.577
		Geography.Regions.Asia.West Asia             0.762
		Geography.Regions.Europe.Eastern Europe      0.713
		Geography.Regions.Europe.Europe*             0.773
		Geography.Regions.Europe.Northern Europe     0.606
		Geography.Regions.Europe.Southern Europe     0.646
		Geography.Regions.Europe.Western Europe      0.695
		Geography.Regions.Oceania                    0.675
		History and Society.Business and economics   0.58
		History and Society.Education                0.479
		History and Society.History                  0.596
		History and Society.Military and warfare     0.709
		History and Society.Politics and government  0.531
		History and Society.Society                  0.449
		History and Society.Transportation           0.903
		STEM.Biology                                 0.804
		STEM.Chemistry                               0.803
		STEM.Computing                               0.814
		STEM.Earth and environment                   0.656
		STEM.Engineering                             0.763
		STEM.Libraries & Information                 0.651
		STEM.Mathematics                             0.776
		STEM.Medicine & Health                       0.661
		STEM.Physics                                 0.655
		STEM.STEM*                                   0.883
		STEM.Space                                   0.908
		STEM.Technology                              0.723
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.941
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.991
		History and Society.Society                  0.987
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.689, macro=0.539):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.872
		Culture.Biography.Women                      0.708
		Culture.Food and drink                       0.471
		Culture.Internet culture                     0.404
		Culture.Linguistics                          0.782
		Culture.Literature                           0.548
		Culture.Media.Books                          0.577
		Culture.Media.Entertainment                  0.235
		Culture.Media.Films                          0.814
		Culture.Media.Media*                         0.645
		Culture.Media.Music                          0.818
		Culture.Media.Radio                          0.595
		Culture.Media.Software                       0.144
		Culture.Media.Television                     0.783
		Culture.Media.Video games                    0.739
		Culture.Performing arts                      0.445
		Culture.Philosophy and religion              0.427
		Culture.Sports                               0.951
		Culture.Visual arts.Architecture             0.648
		Culture.Visual arts.Comics and Anime         0.719
		Culture.Visual arts.Fashion                  0.277
		Culture.Visual arts.Visual arts*             0.632
		Geography.Geographical                       0.572
		Geography.Regions.Africa.Africa*             0.474
		Geography.Regions.Africa.Central Africa      0.187
		Geography.Regions.Africa.Eastern Africa      0.286
		Geography.Regions.Africa.Northern Africa     0.262
		Geography.Regions.Africa.Southern Africa     0.354
		Geography.Regions.Africa.Western Africa      0.36
		Geography.Regions.Americas.Central America   0.543
		Geography.Regions.Americas.North America     0.7
		Geography.Regions.Americas.South America     0.707
		Geography.Regions.Asia.Asia*                 0.677
		Geography.Regions.Asia.Central Asia          0.213
		Geography.Regions.Asia.East Asia             0.728
		Geography.Regions.Asia.North Asia            0.107
		Geography.Regions.Asia.South Asia            0.873
		Geography.Regions.Asia.Southeast Asia        0.699
		Geography.Regions.Asia.West Asia             0.734
		Geography.Regions.Europe.Eastern Europe      0.434
		Geography.Regions.Europe.Europe*             0.52
		Geography.Regions.Europe.Northern Europe     0.706
		Geography.Regions.Europe.Southern Europe     0.589
		Geography.Regions.Europe.Western Europe      0.538
		Geography.Regions.Oceania                    0.874
		History and Society.Business and economics   0.481
		History and Society.Education                0.574
		History and Society.History                  0.339
		History and Society.Military and warfare     0.482
		History and Society.Politics and government  0.622
		History and Society.Society                  0.306
		History and Society.Transportation           0.824
		STEM.Biology                                 0.894
		STEM.Chemistry                               0.333
		STEM.Computing                               0.227
		STEM.Earth and environment                   0.521
		STEM.Engineering                             0.502
		STEM.Libraries & Information                 0.297
		STEM.Mathematics                             0.199
		STEM.Medicine & Health                       0.535
		STEM.Physics                                 0.171
		STEM.STEM*                                   0.718
		STEM.Space                                   0.869
		STEM.Technology                              0.224
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.989
		Culture.Biography.Women                      0.998
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.999
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
		History and Society.Transportation           0.999
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.991
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.718, macro=0.585):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.768
		Culture.Food and drink                       0.567
		Culture.Internet culture                     0.541
		Culture.Linguistics                          0.746
		Culture.Literature                           0.622
		Culture.Media.Books                          0.665
		Culture.Media.Entertainment                  0.31
		Culture.Media.Films                          0.817
		Culture.Media.Media*                         0.741
		Culture.Media.Music                          0.829
		Culture.Media.Radio                          0.522
		Culture.Media.Software                       0.242
		Culture.Media.Television                     0.815
		Culture.Media.Video games                    0.816
		Culture.Performing arts                      0.522
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.922
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.781
		Culture.Visual arts.Fashion                  0.39
		Culture.Visual arts.Visual arts*             0.679
		Geography.Geographical                       0.638
		Geography.Regions.Africa.Africa*             0.541
		Geography.Regions.Africa.Central Africa      0.265
		Geography.Regions.Africa.Eastern Africa      0.376
		Geography.Regions.Africa.Northern Africa     0.365
		Geography.Regions.Africa.Southern Africa     0.401
		Geography.Regions.Africa.Western Africa      0.395
		Geography.Regions.Americas.Central America   0.504
		Geography.Regions.Americas.North America     0.654
		Geography.Regions.Americas.South America     0.691
		Geography.Regions.Asia.Asia*                 0.729
		Geography.Regions.Asia.Central Asia          0.317
		Geography.Regions.Asia.East Asia             0.744
		Geography.Regions.Asia.North Asia            0.184
		Geography.Regions.Asia.South Asia            0.796
		Geography.Regions.Asia.Southeast Asia        0.632
		Geography.Regions.Asia.West Asia             0.748
		Geography.Regions.Europe.Eastern Europe      0.539
		Geography.Regions.Europe.Europe*             0.622
		Geography.Regions.Europe.Northern Europe     0.652
		Geography.Regions.Europe.Southern Europe     0.616
		Geography.Regions.Europe.Western Europe      0.607
		Geography.Regions.Oceania                    0.762
		History and Society.Business and economics   0.526
		History and Society.Education                0.522
		History and Society.History                  0.432
		History and Society.Military and warfare     0.574
		History and Society.Politics and government  0.573
		History and Society.Society                  0.364
		History and Society.Transportation           0.862
		STEM.Biology                                 0.846
		STEM.Chemistry                               0.471
		STEM.Computing                               0.355
		STEM.Earth and environment                   0.581
		STEM.Engineering                             0.606
		STEM.Libraries & Information                 0.408
		STEM.Mathematics                             0.316
		STEM.Medicine & Health                       0.591
		STEM.Physics                                 0.272
		STEM.STEM*                                   0.792
		STEM.Space                                   0.888
		STEM.Technology                              0.342
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.973
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.986
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.992
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.989
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.928
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.978
		History and Society.Society                  0.98
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.019
		Culture.Biography.Women                      0.005
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.059
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.012
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.006
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.009
		History and Society.Society                  0.013
		History and Society.Transportation           0.003
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.004
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.971, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.979
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.976
		Culture.Literature                           0.974
		Culture.Media.Books                          0.982
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.984
		Culture.Media.Radio                          0.947
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.985
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.973
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.973
		Geography.Regions.Africa.Eastern Africa      0.961
		Geography.Regions.Africa.Northern Africa     0.974
		Geography.Regions.Africa.Southern Africa     0.948
		Geography.Regions.Africa.Western Africa      0.909
		Geography.Regions.Americas.Central America   0.963
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.973
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.973
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.97
		Geography.Regions.Asia.Southeast Asia        0.968
		Geography.Regions.Asia.West Asia             0.979
		Geography.Regions.Europe.Eastern Europe      0.971
		Geography.Regions.Europe.Europe*             0.946
		Geography.Regions.Europe.Northern Europe     0.963
		Geography.Regions.Europe.Southern Europe     0.97
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.962
		History and Society.Education                0.963
		History and Society.History                  0.956
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.95
		History and Society.Society                  0.917
		History and Society.Transportation           0.987
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.987
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.983
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.975
		STEM.Space                                   0.993
		STEM.Technology                              0.974
		-------------------------------------------  -----
	pr_auc (micro=0.766, macro=0.599):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.953
		Culture.Biography.Women                      0.781
		Culture.Food and drink                       0.603
		Culture.Internet culture                     0.726
		Culture.Linguistics                          0.74
		Culture.Literature                           0.667
		Culture.Media.Books                          0.689
		Culture.Media.Entertainment                  0.244
		Culture.Media.Films                          0.825
		Culture.Media.Media*                         0.854
		Culture.Media.Music                          0.849
		Culture.Media.Radio                          0.334
		Culture.Media.Software                       0.337
		Culture.Media.Television                     0.873
		Culture.Media.Video games                    0.904
		Culture.Performing arts                      0.516
		Culture.Philosophy and religion              0.471
		Culture.Sports                               0.955
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.793
		Culture.Visual arts.Fashion                  0.4
		Culture.Visual arts.Visual arts*             0.74
		Geography.Geographical                       0.651
		Geography.Regions.Africa.Africa*             0.537
		Geography.Regions.Africa.Central Africa      0.15
		Geography.Regions.Africa.Eastern Africa      0.219
		Geography.Regions.Africa.Northern Africa     0.321
		Geography.Regions.Africa.Southern Africa     0.215
		Geography.Regions.Africa.Western Africa      0.194
		Geography.Regions.Americas.Central America   0.473
		Geography.Regions.Americas.North America     0.712
		Geography.Regions.Americas.South America     0.693
		Geography.Regions.Asia.Asia*                 0.809
		Geography.Regions.Asia.Central Asia          0.232
		Geography.Regions.Asia.East Asia             0.791
		Geography.Regions.Asia.North Asia            0.214
		Geography.Regions.Asia.South Asia            0.816
		Geography.Regions.Asia.Southeast Asia        0.587
		Geography.Regions.Asia.West Asia             0.8
		Geography.Regions.Europe.Eastern Europe      0.573
		Geography.Regions.Europe.Europe*             0.687
		Geography.Regions.Europe.Northern Europe     0.711
		Geography.Regions.Europe.Southern Europe     0.643
		Geography.Regions.Europe.Western Europe      0.63
		Geography.Regions.Oceania                    0.806
		History and Society.Business and economics   0.507
		History and Society.Education                0.494
		History and Society.History                  0.446
		History and Society.Military and warfare     0.654
		History and Society.Politics and government  0.596
		History and Society.Society                  0.325
		History and Society.Transportation           0.912
		STEM.Biology                                 0.898
		STEM.Chemistry                               0.418
		STEM.Computing                               0.367
		STEM.Earth and environment                   0.596
		STEM.Engineering                             0.71
		STEM.Libraries & Information                 0.385
		STEM.Mathematics                             0.494
		STEM.Medicine & Health                       0.599
		STEM.Physics                                 0.24
		STEM.STEM*                                   0.883
		STEM.Space                                   0.951
		STEM.Technology                              0.479
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object'}

