Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'subsample': 1.0, 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'population_rates': None, 'multilabel': True, 'warm_start': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'init': None, 'label_weights': {}, 'scale': False, 'verbose': 0, 'max_features': 'log2', 'center': False, 'presort': 'deprecated', 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'criterion': 'friedman_mse', 'loss': 'deviance', 'ccp_alpha': 0.0, 'random_state': None, 'tol': 0.0001, 'validation_fraction': 0.1, 'max_depth': 5, 'min_impurity_split': None, 'min_samples_leaf': 1, 'learning_rate': 0.1, 'n_iter_no_change': None}
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
	counts (n=56241):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14263  -->  12989  1274   713  41265
			'Culture.Biography.Women'                       3376  -->   2354  1022   354  52511
			'Culture.Food and drink'                        1494  -->   1126   368   130  54617
			'Culture.Internet culture'                      2012  -->   1713   299   207  54022
			'Culture.Linguistics'                           2166  -->   1541   625   202  53873
			'Culture.Literature'                            4709  -->   3572  1137   475  51057
			'Culture.Media.Books'                           1241  -->    984   257    96  54904
			'Culture.Media.Entertainment'                   1978  -->   1020   958   233  54030
			'Culture.Media.Films'                           3105  -->   2834   271    85  53051
			'Culture.Media.Media*'                         11287  -->   9890  1397   992  43962
			'Culture.Media.Music'                           2686  -->   2293   393   145  53410
			'Culture.Media.Radio'                            220  -->    143    77    31  55990
			'Culture.Media.Software'                        1807  -->   1646   161   198  54236
			'Culture.Media.Television'                      1699  -->   1317   382    95  54447
			'Culture.Media.Video games'                      646  -->    623    23    22  55573
			'Culture.Performing arts'                       1566  -->    912   654   122  54553
			'Culture.Philosophy and religion'               4079  -->   2227  1852   378  51784
			'Culture.Sports'                                3726  -->   3022   704   136  52379
			'Culture.Visual arts.Architecture'              2491  -->   1921   570   255  53495
			'Culture.Visual arts.Comics and Anime'          1144  -->    985   159    46  55051
			'Culture.Visual arts.Fashion'                    614  -->    422   192    50  55577
			'Culture.Visual arts.Visual arts*'              4938  -->   3695  1243   385  50918
			'Geography.Geographical'                        4567  -->   3092  1475   682  50992
			'Geography.Regions.Africa.Africa*'              3817  -->   2443  1374   348  52076
			'Geography.Regions.Africa.Central Africa'        831  -->    540   291    86  55324
			'Geography.Regions.Africa.Eastern Africa'        333  -->    187   146    40  55868
			'Geography.Regions.Africa.Northern Africa'      1402  -->    892   510   124  54715
			'Geography.Regions.Africa.Southern Africa'       570  -->    341   229    42  55629
			'Geography.Regions.Africa.Western Africa'         65  -->     30    35    33  56143
			'Geography.Regions.Americas.Central America'    1433  -->    774   659   156  54652
			'Geography.Regions.Americas.North America'      6392  -->   4813  1579   755  49094
			'Geography.Regions.Americas.South America'      1765  -->   1362   403   142  54334
			'Geography.Regions.Asia.Asia*'                 10451  -->   8415  2036   862  44928
			'Geography.Regions.Asia.Central Asia'            722  -->    487   235   105  55414
			'Geography.Regions.Asia.East Asia'              3333  -->   2845   488   214  52694
			'Geography.Regions.Asia.North Asia'             2294  -->   1798   496   120  53827
			'Geography.Regions.Asia.South Asia'             1684  -->   1152   532   117  54440
			'Geography.Regions.Asia.Southeast Asia'         1669  -->    903   766   209  54363
			'Geography.Regions.Asia.West Asia'              2263  -->   1628   635   160  53818
			'Geography.Regions.Europe.Eastern Europe'       3811  -->   3033   778   148  52282
			'Geography.Regions.Europe.Europe*'             17711  -->  15168  2543  1945  36585
			'Geography.Regions.Europe.Northern Europe'      4040  -->   3170   870   310  51891
			'Geography.Regions.Europe.Southern Europe'      5627  -->   4331  1296   632  49982
			'Geography.Regions.Europe.Western Europe'       5184  -->   4152  1032   411  50646
			'Geography.Regions.Oceania'                     1966  -->   1329   637   135  54140
			'History and Society.Business and economics'    3030  -->   1868  1162   255  52956
			'History and Society.Education'                 1729  -->    893   836   131  54381
			'History and Society.History'                   5865  -->   3815  2050   678  49698
			'History and Society.Military and warfare'      3813  -->   2476  1337   407  52021
			'History and Society.Politics and government'   4611  -->   2579  2032   500  51130
			'History and Society.Society'                   5292  -->   2021  3271   528  50421
			'History and Society.Transportation'            2607  -->   2198   409    85  53549
			'STEM.Biology'                                  6922  -->   6306   616   176  49143
			'STEM.Chemistry'                                1534  -->   1236   298   109  54598
			'STEM.Computing'                                2311  -->   2007   304   184  53746
			'STEM.Earth and environment'                    1877  -->   1334   543   121  54243
			'STEM.Engineering'                              2528  -->   1826   702   180  53533
			'STEM.Libraries & Information'                   472  -->    341   131    32  55737
			'STEM.Mathematics'                              1030  -->    915   115    40  55171
			'STEM.Medicine & Health'                        1894  -->   1341   553   156  54191
			'STEM.Physics'                                  1545  -->   1150   395   170  54526
			'STEM.STEM*'                                   19866  -->  18157  1709   875  35500
			'STEM.Space'                                    1855  -->   1697   158    42  54344
			'STEM.Technology'                               4185  -->   3115  1070   550  51506
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.254         0.12
		Culture.Biography.Women                         0.06          0.015
		Culture.Food and drink                          0.027         0.003
		Culture.Internet culture                        0.036         0.004
		Culture.Linguistics                             0.039         0.008
		Culture.Literature                              0.084         0.015
		Culture.Media.Books                             0.022         0.004
		Culture.Media.Entertainment                     0.035         0.004
		Culture.Media.Films                             0.055         0.012
		Culture.Media.Media*                            0.201         0.055
		Culture.Media.Music                             0.048         0.021
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.032         0.001
		Culture.Media.Television                        0.03          0.009
		Culture.Media.Video games                       0.011         0.003
		Culture.Performing arts                         0.028         0.003
		Culture.Philosophy and religion                 0.073         0.01
		Culture.Sports                                  0.066         0.06
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.02          0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.088         0.018
		Geography.Geographical                          0.081         0.021
		Geography.Regions.Africa.Africa*                0.068         0.008
		Geography.Regions.Africa.Central Africa         0.015         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.01          0.001
		Geography.Regions.Africa.Western Africa         0.001         0.001
		Geography.Regions.Americas.Central America      0.025         0.003
		Geography.Regions.Americas.North America        0.114         0.063
		Geography.Regions.Americas.South America        0.031         0.007
		Geography.Regions.Asia.Asia*                    0.186         0.052
		Geography.Regions.Asia.Central Asia             0.013         0.001
		Geography.Regions.Asia.East Asia                0.059         0.012
		Geography.Regions.Asia.North Asia               0.041         0.006
		Geography.Regions.Asia.South Asia               0.03          0.016
		Geography.Regions.Asia.Southeast Asia           0.03          0.006
		Geography.Regions.Asia.West Asia                0.04          0.012
		Geography.Regions.Europe.Eastern Europe         0.068         0.018
		Geography.Regions.Europe.Europe*                0.315         0.081
		Geography.Regions.Europe.Northern Europe        0.072         0.029
		Geography.Regions.Europe.Southern Europe        0.1           0.014
		Geography.Regions.Europe.Western Europe         0.092         0.02
		Geography.Regions.Oceania                       0.035         0.016
		History and Society.Business and economics      0.054         0.01
		History and Society.Education                   0.031         0.008
		History and Society.History                     0.104         0.011
		History and Society.Military and warfare        0.068         0.015
		History and Society.Politics and government     0.082         0.028
		History and Society.Society                     0.094         0.008
		History and Society.Transportation              0.046         0.016
		STEM.Biology                                    0.123         0.034
		STEM.Chemistry                                  0.027         0.002
		STEM.Computing                                  0.041         0.003
		STEM.Earth and environment                      0.033         0.005
		STEM.Engineering                                0.045         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.034         0.006
		STEM.Physics                                    0.027         0.001
		STEM.STEM*                                      0.353         0.065
		STEM.Space                                      0.033         0.004
		STEM.Technology                                 0.074         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.124
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.009
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.069
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.051
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.027
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.005
		Geography.Regions.Americas.North America     0.062
		Geography.Regions.Americas.South America     0.008
		Geography.Regions.Asia.Asia*                 0.06
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.007
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.017
		Geography.Regions.Europe.Europe*             0.115
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.023
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.02
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.025
		History and Society.Society                  0.013
		History and Society.Transportation           0.015
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.082
		STEM.Space                                   0.005
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.876
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.991
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.931
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.949
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.973
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.995
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.992
		Geography.Regions.Asia.Asia*                 0.94
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.983
		Geography.Regions.Europe.Europe*             0.885
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.977
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.98
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.975
		History and Society.Society                  0.987
		History and Society.Transportation           0.985
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.918
		STEM.Space                                   0.995
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.794, macro=0.732):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.911
		Culture.Biography.Women                      0.697
		Culture.Food and drink                       0.754
		Culture.Internet culture                     0.851
		Culture.Linguistics                          0.711
		Culture.Literature                           0.759
		Culture.Media.Books                          0.793
		Culture.Media.Entertainment                  0.516
		Culture.Media.Films                          0.913
		Culture.Media.Media*                         0.876
		Culture.Media.Music                          0.854
		Culture.Media.Radio                          0.65
		Culture.Media.Software                       0.911
		Culture.Media.Television                     0.775
		Culture.Media.Video games                    0.964
		Culture.Performing arts                      0.582
		Culture.Philosophy and religion              0.546
		Culture.Sports                               0.811
		Culture.Visual arts.Architecture             0.771
		Culture.Visual arts.Comics and Anime         0.861
		Culture.Visual arts.Fashion                  0.687
		Culture.Visual arts.Visual arts*             0.748
		Geography.Geographical                       0.677
		Geography.Regions.Africa.Africa*             0.64
		Geography.Regions.Africa.Central Africa      0.65
		Geography.Regions.Africa.Eastern Africa      0.562
		Geography.Regions.Africa.Northern Africa     0.636
		Geography.Regions.Africa.Southern Africa     0.598
		Geography.Regions.Africa.Western Africa      0.462
		Geography.Regions.Americas.Central America   0.54
		Geography.Regions.Americas.North America     0.753
		Geography.Regions.Americas.South America     0.772
		Geography.Regions.Asia.Asia*                 0.805
		Geography.Regions.Asia.Central Asia          0.675
		Geography.Regions.Asia.East Asia             0.854
		Geography.Regions.Asia.North Asia            0.784
		Geography.Regions.Asia.South Asia            0.684
		Geography.Regions.Asia.Southeast Asia        0.541
		Geography.Regions.Asia.West Asia             0.719
		Geography.Regions.Europe.Eastern Europe      0.796
		Geography.Regions.Europe.Europe*             0.856
		Geography.Regions.Europe.Northern Europe     0.785
		Geography.Regions.Europe.Southern Europe     0.77
		Geography.Regions.Europe.Western Europe      0.801
		Geography.Regions.Oceania                    0.676
		History and Society.Business and economics   0.617
		History and Society.Education                0.516
		History and Society.History                  0.65
		History and Society.Military and warfare     0.649
		History and Society.Politics and government  0.559
		History and Society.Society                  0.382
		History and Society.Transportation           0.843
		STEM.Biology                                 0.911
		STEM.Chemistry                               0.806
		STEM.Computing                               0.868
		STEM.Earth and environment                   0.711
		STEM.Engineering                             0.722
		STEM.Libraries & Information                 0.722
		STEM.Mathematics                             0.888
		STEM.Medicine & Health                       0.708
		STEM.Physics                                 0.744
		STEM.STEM*                                   0.914
		STEM.Space                                   0.915
		STEM.Technology                              0.744
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.95
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.715, macro=0.579):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.88
		Culture.Biography.Women                      0.612
		Culture.Food and drink                       0.447
		Culture.Internet culture                     0.455
		Culture.Linguistics                          0.606
		Culture.Literature                           0.553
		Culture.Media.Books                          0.663
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.869
		Culture.Media.Media*                         0.697
		Culture.Media.Music                          0.871
		Culture.Media.Radio                          0.732
		Culture.Media.Software                       0.247
		Culture.Media.Television                     0.799
		Culture.Media.Video games                    0.876
		Culture.Performing arts                      0.444
		Culture.Philosophy and religion              0.441
		Culture.Sports                               0.953
		Culture.Visual arts.Architecture             0.639
		Culture.Visual arts.Comics and Anime         0.712
		Culture.Visual arts.Fashion                  0.406
		Culture.Visual arts.Visual arts*             0.647
		Geography.Geographical                       0.525
		Geography.Regions.Africa.Africa*             0.452
		Geography.Regions.Africa.Central Africa      0.227
		Geography.Regions.Africa.Eastern Africa      0.283
		Geography.Regions.Africa.Northern Africa     0.275
		Geography.Regions.Africa.Southern Africa     0.509
		Geography.Regions.Africa.Western Africa      0.369
		Geography.Regions.Americas.Central America   0.396
		Geography.Regions.Americas.North America     0.769
		Geography.Regions.Americas.South America     0.671
		Geography.Regions.Asia.Asia*                 0.703
		Geography.Regions.Asia.Central Asia          0.221
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.665
		Geography.Regions.Asia.South Asia            0.842
		Geography.Regions.Asia.Southeast Asia        0.469
		Geography.Regions.Asia.West Asia             0.741
		Geography.Regions.Europe.Eastern Europe      0.84
		Geography.Regions.Europe.Europe*             0.598
		Geography.Regions.Europe.Northern Europe     0.797
		Geography.Regions.Europe.Southern Europe     0.463
		Geography.Regions.Europe.Western Europe      0.675
		Geography.Regions.Oceania                    0.819
		History and Society.Business and economics   0.558
		History and Society.Education                0.631
		History and Society.History                  0.347
		History and Society.Military and warfare     0.565
		History and Society.Politics and government  0.624
		History and Society.Society                  0.235
		History and Society.Transportation           0.898
		STEM.Biology                                 0.901
		STEM.Chemistry                               0.406
		STEM.Computing                               0.418
		STEM.Earth and environment                   0.602
		STEM.Engineering                             0.554
		STEM.Libraries & Information                 0.463
		STEM.Mathematics                             0.361
		STEM.Medicine & Health                       0.614
		STEM.Physics                                 0.183
		STEM.STEM*                                   0.725
		STEM.Space                                   0.835
		STEM.Technology                              0.267
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.988
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.993
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.998
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
		Geography.Regions.Americas.North America     0.983
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.987
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.996
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.987
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               1
		STEM.Earth and environment                   0.999
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.746, macro=0.631):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.895
		Culture.Biography.Women                      0.652
		Culture.Food and drink                       0.562
		Culture.Internet culture                     0.593
		Culture.Linguistics                          0.655
		Culture.Literature                           0.64
		Culture.Media.Books                          0.722
		Culture.Media.Entertainment                  0.396
		Culture.Media.Films                          0.89
		Culture.Media.Media*                         0.776
		Culture.Media.Music                          0.862
		Culture.Media.Radio                          0.689
		Culture.Media.Software                       0.388
		Culture.Media.Television                     0.787
		Culture.Media.Video games                    0.918
		Culture.Performing arts                      0.504
		Culture.Philosophy and religion              0.488
		Culture.Sports                               0.876
		Culture.Visual arts.Architecture             0.699
		Culture.Visual arts.Comics and Anime         0.779
		Culture.Visual arts.Fashion                  0.511
		Culture.Visual arts.Visual arts*             0.694
		Geography.Geographical                       0.591
		Geography.Regions.Africa.Africa*             0.53
		Geography.Regions.Africa.Central Africa      0.337
		Geography.Regions.Africa.Eastern Africa      0.376
		Geography.Regions.Africa.Northern Africa     0.384
		Geography.Regions.Africa.Southern Africa     0.55
		Geography.Regions.Africa.Western Africa      0.41
		Geography.Regions.Americas.Central America   0.457
		Geography.Regions.Americas.North America     0.761
		Geography.Regions.Americas.South America     0.718
		Geography.Regions.Asia.Asia*                 0.751
		Geography.Regions.Asia.Central Asia          0.333
		Geography.Regions.Asia.East Asia             0.782
		Geography.Regions.Asia.North Asia            0.719
		Geography.Regions.Asia.South Asia            0.755
		Geography.Regions.Asia.Southeast Asia        0.503
		Geography.Regions.Asia.West Asia             0.73
		Geography.Regions.Europe.Eastern Europe      0.817
		Geography.Regions.Europe.Europe*             0.704
		Geography.Regions.Europe.Northern Europe     0.791
		Geography.Regions.Europe.Southern Europe     0.578
		Geography.Regions.Europe.Western Europe      0.733
		Geography.Regions.Oceania                    0.741
		History and Society.Business and economics   0.586
		History and Society.Education                0.568
		History and Society.History                  0.453
		History and Society.Military and warfare     0.604
		History and Society.Politics and government  0.59
		History and Society.Society                  0.291
		History and Society.Transportation           0.87
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.54
		STEM.Computing                               0.565
		STEM.Earth and environment                   0.652
		STEM.Engineering                             0.627
		STEM.Libraries & Information                 0.564
		STEM.Mathematics                             0.514
		STEM.Medicine & Health                       0.658
		STEM.Physics                                 0.294
		STEM.STEM*                                   0.809
		STEM.Space                                   0.873
		STEM.Technology                              0.393
		-------------------------------------------  -----
	!f1 (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.997
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.985
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.984
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.968
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.98, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.994
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.98
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.972
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.992
		History and Society.Education                0.994
		History and Society.History                  0.983
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.978
		History and Society.Society                  0.985
		History and Society.Transportation           0.996
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.017
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.004
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.022
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.013
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.05
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.012
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.01
		History and Society.Transportation           0.002
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.976, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.979
		Culture.Literature                           0.979
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.971
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.985
		Culture.Media.Radio                          0.925
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.984
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.972
		Culture.Philosophy and religion              0.956
		Culture.Sports                               0.976
		Culture.Visual arts.Architecture             0.983
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.976
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.972
		Geography.Regions.Africa.Central Africa      0.98
		Geography.Regions.Africa.Eastern Africa      0.966
		Geography.Regions.Africa.Northern Africa     0.976
		Geography.Regions.Africa.Southern Africa     0.967
		Geography.Regions.Africa.Western Africa      0.764
		Geography.Regions.Americas.Central America   0.972
		Geography.Regions.Americas.North America     0.976
		Geography.Regions.Americas.South America     0.98
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.975
		Geography.Regions.Asia.East Asia             0.982
		Geography.Regions.Asia.North Asia            0.977
		Geography.Regions.Asia.South Asia            0.973
		Geography.Regions.Asia.Southeast Asia        0.977
		Geography.Regions.Asia.West Asia             0.977
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.978
		History and Society.Business and economics   0.968
		History and Society.Education                0.965
		History and Society.History                  0.961
		History and Society.Military and warfare     0.971
		History and Society.Politics and government  0.954
		History and Society.Society                  0.926
		History and Society.Transportation           0.984
		STEM.Biology                                 0.986
		STEM.Chemistry                               0.987
		STEM.Computing                               0.988
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.979
		STEM.Libraries & Information                 0.966
		STEM.Mathematics                             0.988
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.983
		STEM.STEM*                                   0.98
		STEM.Space                                   0.989
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.798, macro=0.634):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.952
		Culture.Biography.Women                      0.656
		Culture.Food and drink                       0.551
		Culture.Internet culture                     0.652
		Culture.Linguistics                          0.698
		Culture.Literature                           0.677
		Culture.Media.Books                          0.706
		Culture.Media.Entertainment                  0.339
		Culture.Media.Films                          0.941
		Culture.Media.Media*                         0.864
		Culture.Media.Music                          0.873
		Culture.Media.Radio                          0.463
		Culture.Media.Software                       0.47
		Culture.Media.Television                     0.832
		Culture.Media.Video games                    0.911
		Culture.Performing arts                      0.453
		Culture.Philosophy and religion              0.49
		Culture.Sports                               0.923
		Culture.Visual arts.Architecture             0.721
		Culture.Visual arts.Comics and Anime         0.829
		Culture.Visual arts.Fashion                  0.385
		Culture.Visual arts.Visual arts*             0.726
		Geography.Geographical                       0.625
		Geography.Regions.Africa.Africa*             0.548
		Geography.Regions.Africa.Central Africa      0.221
		Geography.Regions.Africa.Eastern Africa      0.175
		Geography.Regions.Africa.Northern Africa     0.228
		Geography.Regions.Africa.Southern Africa     0.369
		Geography.Regions.Africa.Western Africa      0.156
		Geography.Regions.Americas.Central America   0.436
		Geography.Regions.Americas.North America     0.842
		Geography.Regions.Americas.South America     0.758
		Geography.Regions.Asia.Asia*                 0.826
		Geography.Regions.Asia.Central Asia          0.209
		Geography.Regions.Asia.East Asia             0.794
		Geography.Regions.Asia.North Asia            0.722
		Geography.Regions.Asia.South Asia            0.782
		Geography.Regions.Asia.Southeast Asia        0.476
		Geography.Regions.Asia.West Asia             0.734
		Geography.Regions.Europe.Eastern Europe      0.845
		Geography.Regions.Europe.Europe*             0.82
		Geography.Regions.Europe.Northern Europe     0.852
		Geography.Regions.Europe.Southern Europe     0.668
		Geography.Regions.Europe.Western Europe      0.786
		Geography.Regions.Oceania                    0.778
		History and Society.Business and economics   0.568
		History and Society.Education                0.504
		History and Society.History                  0.491
		History and Society.Military and warfare     0.609
		History and Society.Politics and government  0.624
		History and Society.Society                  0.252
		History and Society.Transportation           0.914
		STEM.Biology                                 0.959
		STEM.Chemistry                               0.581
		STEM.Computing                               0.614
		STEM.Earth and environment                   0.664
		STEM.Engineering                             0.679
		STEM.Libraries & Information                 0.428
		STEM.Mathematics                             0.67
		STEM.Medicine & Health                       0.682
		STEM.Physics                                 0.265
		STEM.STEM*                                   0.922
		STEM.Space                                   0.921
		STEM.Technology                              0.451
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

