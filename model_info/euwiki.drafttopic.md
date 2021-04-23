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
	counts (n=55230):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13830  -->  12127  1703   852  40548
			'Culture.Biography.Women'                       3519  -->   2326  1193   393  51318
			'Culture.Food and drink'                        1408  -->    991   417   114  53708
			'Culture.Internet culture'                      2130  -->   1797   333   157  52943
			'Culture.Linguistics'                           2107  -->   1492   615   142  52981
			'Culture.Literature'                            4764  -->   3381  1383   474  49992
			'Culture.Media.Books'                           1275  -->   1005   270    81  53874
			'Culture.Media.Entertainment'                   2102  -->   1129   973   228  52900
			'Culture.Media.Films'                           3089  -->   2771   318    85  52056
			'Culture.Media.Media*'                         11397  -->   9834  1563  1033  42800
			'Culture.Media.Music'                           2693  -->   2207   486   134  52403
			'Culture.Media.Radio'                            239  -->    164    75    44  54947
			'Culture.Media.Software'                        1983  -->   1814   169   201  53046
			'Culture.Media.Television'                      1712  -->   1342   370    88  53430
			'Culture.Media.Video games'                      643  -->    611    32    31  54556
			'Culture.Performing arts'                       1527  -->    914   613   128  53575
			'Culture.Philosophy and religion'               4046  -->   2108  1938   342  50842
			'Culture.Sports'                                3611  -->   2876   735   125  51494
			'Culture.Visual arts.Architecture'              2455  -->   1851   604   236  52539
			'Culture.Visual arts.Comics and Anime'          1147  -->    952   195    47  54036
			'Culture.Visual arts.Fashion'                    601  -->    387   214    33  54596
			'Culture.Visual arts.Visual arts*'              4876  -->   3429  1447   431  49923
			'Geography.Geographical'                        4334  -->   2773  1561   714  50182
			'Geography.Regions.Africa.Africa*'              3798  -->   2411  1387   360  51072
			'Geography.Regions.Africa.Central Africa'        791  -->    483   308    99  54340
			'Geography.Regions.Africa.Eastern Africa'        354  -->    217   137    18  54858
			'Geography.Regions.Africa.Northern Africa'      1474  -->   1000   474   124  53632
			'Geography.Regions.Africa.Southern Africa'       578  -->    363   215    38  54614
			'Geography.Regions.Africa.Western Africa'         71  -->     35    36    30  55129
			'Geography.Regions.Americas.Central America'    1367  -->    684   683   130  53733
			'Geography.Regions.Americas.North America'      6463  -->   4647  1816   739  48028
			'Geography.Regions.Americas.South America'      1771  -->   1232   539   107  53352
			'Geography.Regions.Asia.Asia*'                  9516  -->   7311  2205   772  44942
			'Geography.Regions.Asia.Central Asia'            875  -->    642   233    75  54280
			'Geography.Regions.Asia.East Asia'              3238  -->   2645   593   175  51817
			'Geography.Regions.Asia.North Asia'             1326  -->   1084   242   126  53778
			'Geography.Regions.Asia.South Asia'             1733  -->   1180   553    78  53419
			'Geography.Regions.Asia.Southeast Asia'         1716  -->    829   887   183  53331
			'Geography.Regions.Asia.West Asia'              2253  -->   1605   648   127  52850
			'Geography.Regions.Europe.Eastern Europe'       2948  -->   2382   566   153  52129
			'Geography.Regions.Europe.Europe*'             16574  -->  13665  2909  2011  36645
			'Geography.Regions.Europe.Northern Europe'      4108  -->   3055  1053   286  50836
			'Geography.Regions.Europe.Southern Europe'      5331  -->   3826  1505   628  49271
			'Geography.Regions.Europe.Western Europe'       5063  -->   3853  1210   402  49765
			'Geography.Regions.Oceania'                     1871  -->   1095   776   201  53158
			'History and Society.Business and economics'    3041  -->   1801  1240   236  51953
			'History and Society.Education'                 1722  -->    863   859   107  53401
			'History and Society.History'                   5917  -->   3681  2236   731  48582
			'History and Society.Military and warfare'      4042  -->   2468  1574   409  50779
			'History and Society.Politics and government'   4581  -->   2317  2264   497  50152
			'History and Society.Society'                   6679  -->   3084  3595   615  47936
			'History and Society.Transportation'            2451  -->   2004   447    91  52688
			'STEM.Biology'                                  6701  -->   6066   635   156  48373
			'STEM.Chemistry'                                1508  -->   1183   325   129  53593
			'STEM.Computing'                                2429  -->   2094   335   146  52655
			'STEM.Earth and environment'                    1808  -->   1248   560   118  53304
			'STEM.Engineering'                              2475  -->   1721   754   181  52574
			'STEM.Libraries & Information'                   460  -->    346   114    35  54735
			'STEM.Mathematics'                              1057  -->    924   133    34  54139
			'STEM.Medicine & Health'                        1892  -->   1279   613   134  53204
			'STEM.Physics'                                  1525  -->   1078   447   138  53567
			'STEM.STEM*'                                   19559  -->  17745  1814   937  34734
			'STEM.Space'                                    1819  -->   1655   164    47  53364
			'STEM.Technology'                               4295  -->   3271  1024   535  50400
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.25          0.123
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.025         0.002
		Culture.Internet culture                        0.039         0.003
		Culture.Linguistics                             0.038         0.007
		Culture.Literature                              0.086         0.015
		Culture.Media.Books                             0.023         0.004
		Culture.Media.Entertainment                     0.038         0.004
		Culture.Media.Films                             0.056         0.011
		Culture.Media.Media*                            0.206         0.058
		Culture.Media.Music                             0.049         0.024
		Culture.Media.Radio                             0.004         0.002
		Culture.Media.Software                          0.036         0.001
		Culture.Media.Television                        0.031         0.009
		Culture.Media.Video games                       0.012         0.003
		Culture.Performing arts                         0.028         0.003
		Culture.Philosophy and religion                 0.073         0.011
		Culture.Sports                                  0.065         0.071
		Culture.Visual arts.Architecture                0.044         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.088         0.018
		Geography.Geographical                          0.078         0.024
		Geography.Regions.Africa.Africa*                0.069         0.008
		Geography.Regions.Africa.Central Africa         0.014         0.001
		Geography.Regions.Africa.Eastern Africa         0.006         0
		Geography.Regions.Africa.Northern Africa        0.027         0.001
		Geography.Regions.Africa.Southern Africa        0.01          0.001
		Geography.Regions.Africa.Western Africa         0.001         0.001
		Geography.Regions.Americas.Central America      0.025         0.003
		Geography.Regions.Americas.North America        0.117         0.064
		Geography.Regions.Americas.South America        0.032         0.006
		Geography.Regions.Asia.Asia*                    0.172         0.045
		Geography.Regions.Asia.Central Asia             0.016         0.001
		Geography.Regions.Asia.East Asia                0.059         0.011
		Geography.Regions.Asia.North Asia               0.024         0.001
		Geography.Regions.Asia.South Asia               0.031         0.015
		Geography.Regions.Asia.Southeast Asia           0.031         0.006
		Geography.Regions.Asia.West Asia                0.041         0.011
		Geography.Regions.Europe.Eastern Europe         0.053         0.013
		Geography.Regions.Europe.Europe*                0.3           0.076
		Geography.Regions.Europe.Northern Europe        0.074         0.031
		Geography.Regions.Europe.Southern Europe        0.097         0.013
		Geography.Regions.Europe.Western Europe         0.092         0.019
		Geography.Regions.Oceania                       0.034         0.015
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.031         0.007
		History and Society.History                     0.107         0.011
		History and Society.Military and warfare        0.073         0.014
		History and Society.Politics and government     0.083         0.028
		History and Society.Society                     0.121         0.013
		History and Society.Transportation              0.044         0.015
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
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.008
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.073
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.059
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.029
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.06
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.051
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.111
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.022
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.01
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.024
		History and Society.Society                  0.018
		History and Society.Transportation           0.014
		STEM.Biology                                 0.034
		STEM.Chemistry                               0.004
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.087
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.874
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.992
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.927
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.971
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.94
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.949
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.889
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.99
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.986
		STEM.Biology                                 0.966
		STEM.Chemistry                               0.996
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.913
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.768, macro=0.717):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.661
		Culture.Food and drink                       0.704
		Culture.Internet culture                     0.844
		Culture.Linguistics                          0.708
		Culture.Literature                           0.71
		Culture.Media.Books                          0.788
		Culture.Media.Entertainment                  0.537
		Culture.Media.Films                          0.897
		Culture.Media.Media*                         0.863
		Culture.Media.Music                          0.82
		Culture.Media.Radio                          0.686
		Culture.Media.Software                       0.915
		Culture.Media.Television                     0.784
		Culture.Media.Video games                    0.95
		Culture.Performing arts                      0.599
		Culture.Philosophy and religion              0.521
		Culture.Sports                               0.796
		Culture.Visual arts.Architecture             0.754
		Culture.Visual arts.Comics and Anime         0.83
		Culture.Visual arts.Fashion                  0.644
		Culture.Visual arts.Visual arts*             0.703
		Geography.Geographical                       0.64
		Geography.Regions.Africa.Africa*             0.635
		Geography.Regions.Africa.Central Africa      0.611
		Geography.Regions.Africa.Eastern Africa      0.613
		Geography.Regions.Africa.Northern Africa     0.678
		Geography.Regions.Africa.Southern Africa     0.628
		Geography.Regions.Africa.Western Africa      0.493
		Geography.Regions.Americas.Central America   0.5
		Geography.Regions.Americas.North America     0.719
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.768
		Geography.Regions.Asia.Central Asia          0.734
		Geography.Regions.Asia.East Asia             0.817
		Geography.Regions.Asia.North Asia            0.817
		Geography.Regions.Asia.South Asia            0.681
		Geography.Regions.Asia.Southeast Asia        0.483
		Geography.Regions.Asia.West Asia             0.712
		Geography.Regions.Europe.Eastern Europe      0.808
		Geography.Regions.Europe.Europe*             0.824
		Geography.Regions.Europe.Northern Europe     0.744
		Geography.Regions.Europe.Southern Europe     0.718
		Geography.Regions.Europe.Western Europe      0.761
		Geography.Regions.Oceania                    0.585
		History and Society.Business and economics   0.592
		History and Society.Education                0.501
		History and Society.History                  0.622
		History and Society.Military and warfare     0.611
		History and Society.Politics and government  0.506
		History and Society.Society                  0.462
		History and Society.Transportation           0.818
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.784
		STEM.Computing                               0.862
		STEM.Earth and environment                   0.69
		STEM.Engineering                             0.695
		STEM.Libraries & Information                 0.752
		STEM.Mathematics                             0.874
		STEM.Medicine & Health                       0.676
		STEM.Physics                                 0.707
		STEM.STEM*                                   0.907
		STEM.Space                                   0.91
		STEM.Technology                              0.762
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.992
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.976
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.948
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.985
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.987
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.707, macro=0.57):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.857
		Culture.Biography.Women                      0.562
		Culture.Food and drink                       0.451
		Culture.Internet culture                     0.5
		Culture.Linguistics                          0.662
		Culture.Literature                           0.543
		Culture.Media.Books                          0.68
		Culture.Media.Entertainment                  0.31
		Culture.Media.Films                          0.854
		Culture.Media.Media*                         0.695
		Culture.Media.Music                          0.887
		Culture.Media.Radio                          0.649
		Culture.Media.Software                       0.244
		Culture.Media.Television                     0.809
		Culture.Media.Video games                    0.814
		Culture.Performing arts                      0.421
		Culture.Philosophy and religion              0.456
		Culture.Sports                               0.962
		Culture.Visual arts.Architecture             0.643
		Culture.Visual arts.Comics and Anime         0.678
		Culture.Visual arts.Fashion                  0.463
		Culture.Visual arts.Visual arts*             0.605
		Geography.Geographical                       0.524
		Geography.Regions.Africa.Africa*             0.416
		Geography.Regions.Africa.Central Africa      0.175
		Geography.Regions.Africa.Eastern Africa      0.46
		Geography.Regions.Africa.Northern Africa     0.265
		Geography.Regions.Africa.Southern Africa     0.515
		Geography.Regions.Africa.Western Africa      0.383
		Geography.Regions.Americas.Central America   0.407
		Geography.Regions.Americas.North America     0.765
		Geography.Regions.Americas.South America     0.688
		Geography.Regions.Asia.Asia*                 0.684
		Geography.Regions.Asia.Central Asia          0.315
		Geography.Regions.Asia.East Asia             0.737
		Geography.Regions.Asia.North Asia            0.244
		Geography.Regions.Asia.South Asia            0.878
		Geography.Regions.Asia.Southeast Asia        0.461
		Geography.Regions.Asia.West Asia             0.766
		Geography.Regions.Europe.Eastern Europe      0.782
		Geography.Regions.Europe.Europe*             0.566
		Geography.Regions.Europe.Northern Europe     0.807
		Geography.Regions.Europe.Southern Europe     0.43
		Geography.Regions.Europe.Western Europe      0.65
		Geography.Regions.Oceania                    0.705
		History and Society.Business and economics   0.572
		History and Society.Education                0.65
		History and Society.History                  0.315
		History and Society.Military and warfare     0.522
		History and Society.Politics and government  0.599
		History and Society.Society                  0.318
		History and Society.Transportation           0.879
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.338
		STEM.Computing                               0.457
		STEM.Earth and environment                   0.587
		STEM.Engineering                             0.516
		STEM.Libraries & Information                 0.423
		STEM.Mathematics                             0.367
		STEM.Medicine & Health                       0.634
		STEM.Physics                                 0.189
		STEM.STEM*                                   0.719
		STEM.Space                                   0.862
		STEM.Technology                              0.272
		-------------------------------------------  -----
	!precision (micro=0.991, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.991
		Culture.Media.Music                          0.996
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
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.981
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.989
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.998
		Geography.Regions.Europe.Europe*             0.985
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.996
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.986
		History and Society.Society                  0.993
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
		STEM.STEM*                                   0.993
		STEM.Space                                   0.999
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.729, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.608
		Culture.Food and drink                       0.549
		Culture.Internet culture                     0.628
		Culture.Linguistics                          0.684
		Culture.Literature                           0.615
		Culture.Media.Books                          0.73
		Culture.Media.Entertainment                  0.393
		Culture.Media.Films                          0.875
		Culture.Media.Media*                         0.77
		Culture.Media.Music                          0.852
		Culture.Media.Radio                          0.667
		Culture.Media.Software                       0.385
		Culture.Media.Television                     0.796
		Culture.Media.Video games                    0.877
		Culture.Performing arts                      0.494
		Culture.Philosophy and religion              0.487
		Culture.Sports                               0.871
		Culture.Visual arts.Architecture             0.694
		Culture.Visual arts.Comics and Anime         0.746
		Culture.Visual arts.Fashion                  0.539
		Culture.Visual arts.Visual arts*             0.65
		Geography.Geographical                       0.576
		Geography.Regions.Africa.Africa*             0.503
		Geography.Regions.Africa.Central Africa      0.272
		Geography.Regions.Africa.Eastern Africa      0.525
		Geography.Regions.Africa.Northern Africa     0.382
		Geography.Regions.Africa.Southern Africa     0.566
		Geography.Regions.Africa.Western Africa      0.431
		Geography.Regions.Americas.Central America   0.449
		Geography.Regions.Americas.North America     0.741
		Geography.Regions.Americas.South America     0.692
		Geography.Regions.Asia.Asia*                 0.724
		Geography.Regions.Asia.Central Asia          0.441
		Geography.Regions.Asia.East Asia             0.775
		Geography.Regions.Asia.North Asia            0.376
		Geography.Regions.Asia.South Asia            0.767
		Geography.Regions.Asia.Southeast Asia        0.472
		Geography.Regions.Asia.West Asia             0.738
		Geography.Regions.Europe.Eastern Europe      0.795
		Geography.Regions.Europe.Europe*             0.672
		Geography.Regions.Europe.Northern Europe     0.774
		Geography.Regions.Europe.Southern Europe     0.537
		Geography.Regions.Europe.Western Europe      0.701
		Geography.Regions.Oceania                    0.639
		History and Society.Business and economics   0.582
		History and Society.Education                0.566
		History and Society.History                  0.418
		History and Society.Military and warfare     0.563
		History and Society.Politics and government  0.549
		History and Society.Society                  0.376
		History and Society.Transportation           0.847
		STEM.Biology                                 0.906
		STEM.Chemistry                               0.472
		STEM.Computing                               0.597
		STEM.Earth and environment                   0.635
		STEM.Engineering                             0.592
		STEM.Libraries & Information                 0.541
		STEM.Mathematics                             0.517
		STEM.Medicine & Health                       0.654
		STEM.Physics                                 0.299
		STEM.STEM*                                   0.803
		STEM.Space                                   0.885
		STEM.Technology                              0.401
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.984
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.995
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
		Geography.Regions.Asia.North Asia            0.999
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.993
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.99
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.999
		STEM.Computing                               0.998
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.967
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.995
		Culture.Literature                           0.986
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.991
		History and Society.Education                0.994
		History and Society.History                  0.981
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.977
		History and Society.Society                  0.981
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.008
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.003
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.024
		Culture.Media.Music                          0.003
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.014
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.017
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.003
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.052
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.015
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.013
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.971):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.976
		Culture.Internet culture                     0.986
		Culture.Linguistics                          0.976
		Culture.Literature                           0.975
		Culture.Media.Books                          0.982
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.933
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.97
		Culture.Philosophy and religion              0.95
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.975
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.974
		Geography.Regions.Africa.Eastern Africa      0.955
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.973
		Geography.Regions.Africa.Western Africa      0.81
		Geography.Regions.Americas.Central America   0.965
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.976
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.977
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.975
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.965
		History and Society.Education                0.963
		History and Society.History                  0.956
		History and Society.Military and warfare     0.967
		History and Society.Politics and government  0.947
		History and Society.Society                  0.926
		History and Society.Transportation           0.983
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.984
		STEM.Computing                               0.989
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.974
		STEM.Libraries & Information                 0.953
		STEM.Mathematics                             0.988
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.978
		STEM.Space                                   0.99
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.781, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.931
		Culture.Biography.Women                      0.613
		Culture.Food and drink                       0.54
		Culture.Internet culture                     0.727
		Culture.Linguistics                          0.735
		Culture.Literature                           0.656
		Culture.Media.Books                          0.708
		Culture.Media.Entertainment                  0.32
		Culture.Media.Films                          0.878
		Culture.Media.Media*                         0.865
		Culture.Media.Music                          0.891
		Culture.Media.Radio                          0.456
		Culture.Media.Software                       0.451
		Culture.Media.Television                     0.83
		Culture.Media.Video games                    0.887
		Culture.Performing arts                      0.413
		Culture.Philosophy and religion              0.447
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.697
		Culture.Visual arts.Comics and Anime         0.764
		Culture.Visual arts.Fashion                  0.369
		Culture.Visual arts.Visual arts*             0.661
		Geography.Geographical                       0.599
		Geography.Regions.Africa.Africa*             0.523
		Geography.Regions.Africa.Central Africa      0.181
		Geography.Regions.Africa.Eastern Africa      0.251
		Geography.Regions.Africa.Northern Africa     0.317
		Geography.Regions.Africa.Southern Africa     0.466
		Geography.Regions.Africa.Western Africa      0.202
		Geography.Regions.Americas.Central America   0.4
		Geography.Regions.Americas.North America     0.819
		Geography.Regions.Americas.South America     0.726
		Geography.Regions.Asia.Asia*                 0.785
		Geography.Regions.Asia.Central Asia          0.332
		Geography.Regions.Asia.East Asia             0.788
		Geography.Regions.Asia.North Asia            0.357
		Geography.Regions.Asia.South Asia            0.796
		Geography.Regions.Asia.Southeast Asia        0.478
		Geography.Regions.Asia.West Asia             0.76
		Geography.Regions.Europe.Eastern Europe      0.829
		Geography.Regions.Europe.Europe*             0.788
		Geography.Regions.Europe.Northern Europe     0.83
		Geography.Regions.Europe.Southern Europe     0.621
		Geography.Regions.Europe.Western Europe      0.737
		Geography.Regions.Oceania                    0.681
		History and Society.Business and economics   0.558
		History and Society.Education                0.536
		History and Society.History                  0.414
		History and Society.Military and warfare     0.582
		History and Society.Politics and government  0.549
		History and Society.Society                  0.336
		History and Society.Transportation           0.894
		STEM.Biology                                 0.955
		STEM.Chemistry                               0.467
		STEM.Computing                               0.693
		STEM.Earth and environment                   0.666
		STEM.Engineering                             0.569
		STEM.Libraries & Information                 0.44
		STEM.Mathematics                             0.661
		STEM.Medicine & Health                       0.653
		STEM.Physics                                 0.283
		STEM.STEM*                                   0.916
		STEM.Space                                   0.935
		STEM.Technology                              0.431
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

