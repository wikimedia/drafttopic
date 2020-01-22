Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'warm_start': False, 'center': False, 'criterion': 'friedman_mse', 'label_weights': {}, 'learning_rate': 0.1, 'presort': 'auto', 'scale': False, 'max_leaf_nodes': None, 'verbose': 0, 'population_rates': None, 'n_estimators': 150, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'tol': 0.0001, 'max_features': 'log2', 'init': None, 'max_depth': 5, 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'min_impurity_split': None, 'random_state': None, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'validation_fraction': 0.1, 'min_samples_split': 2, 'multilabel': True, 'n_iter_no_change': None, 'subsample': 1.0}
	Environment:
	 - revscoring_version: '2.6.3'
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
	counts (n=62581):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 26810  -->  25783  1027  1010  34761
			'Culture.Biography.Women'                       6237  -->   4749  1488   765  55579
			'Culture.Food and drink'                        1408  -->   1038   370    90  61083
			'Culture.Internet culture'                      3358  -->   2805   553   161  59062
			'Culture.Linguistics'                           1442  -->    997   445    54  61085
			'Culture.Literature'                            5798  -->   4348  1450   483  56300
			'Culture.Media.Books'                           1580  -->   1215   365    91  60910
			'Culture.Media.Entertainment'                   2139  -->   1052  1087   199  60243
			'Culture.Media.Films'                           2079  -->   1646   433    74  60428
			'Culture.Media.Media*'                         13978  -->  11712  2266  1490  47113
			'Culture.Media.Music'                           2737  -->   2064   673   291  59553
			'Culture.Media.Radio'                           1146  -->    585   561    93  61342
			'Culture.Media.Software'                        2066  -->   1611   455   252  60263
			'Culture.Media.Television'                      2313  -->   1393   920   203  60065
			'Culture.Media.Video games'                     2164  -->   1937   227    38  60379
			'Culture.Performing arts'                       1486  -->    760   726   126  60969
			'Culture.Philosophy and religion'               3384  -->   1776  1608   300  58897
			'Culture.Sports'                                8294  -->   7569   725   332  53955
			'Culture.Visual arts.Architecture'              1832  -->   1293   539   170  60579
			'Culture.Visual arts.Comics and Anime'          1858  -->   1490   368    98  60625
			'Culture.Visual arts.Fashion'                   1345  -->    998   347    75  61161
			'Culture.Visual arts.Visual arts*'              5949  -->   4390  1559   403  56229
			'Geography.Geographical'                        3588  -->   2636   952   339  58654
			'Geography.Regions.Africa.Africa*'              5725  -->   4820   905   302  56554
			'Geography.Regions.Africa.Central Africa'         36  -->      4    32    40  62505
			'Geography.Regions.Africa.Eastern Africa'        976  -->    786   190    40  61565
			'Geography.Regions.Africa.Northern Africa'      2029  -->   1583   446   207  60345
			'Geography.Regions.Africa.Southern Africa'      1189  -->    948   241    59  61333
			'Geography.Regions.Africa.Western Africa'        746  -->    595   151    28  61807
			'Geography.Regions.Americas.Central America'    1346  -->    902   444    74  61161
			'Geography.Regions.Americas.North America'      8393  -->   5811  2582  2064  52124
			'Geography.Regions.Americas.South America'      1645  -->   1266   379   115  60821
			'Geography.Regions.Asia.Asia*'                 11997  -->  10151  1846   891  49693
			'Geography.Regions.Asia.Central Asia'           1204  -->    964   240    83  61294
			'Geography.Regions.Asia.East Asia'              2827  -->   2177   650   224  59530
			'Geography.Regions.Asia.North Asia'             1548  -->   1147   401   205  60828
			'Geography.Regions.Asia.South Asia'             1907  -->   1526   381    66  60608
			'Geography.Regions.Asia.Southeast Asia'         1578  -->   1217   361    68  60935
			'Geography.Regions.Asia.West Asia'              4119  -->   3404   715   305  58157
			'Geography.Regions.Europe.Eastern Europe'       2943  -->   2246   697   263  59375
			'Geography.Regions.Europe.Europe*'             13073  -->  10399  2674  1872  47636
			'Geography.Regions.Europe.Northern Europe'      4032  -->   2669  1363   606  57943
			'Geography.Regions.Europe.Southern Europe'      2835  -->   2132   703   268  59478
			'Geography.Regions.Europe.Western Europe'       4056  -->   3089   967   472  58053
			'Geography.Regions.Oceania'                     2248  -->   1881   367    65  60268
			'History and Society.Business and economics'    3607  -->   2038  1569   425  58549
			'History and Society.Education'                 1992  -->    880  1112   171  60418
			'History and Society.History'                   4707  -->   2350  2357   635  57239
			'History and Society.Military and warfare'      4826  -->   3403  1423   445  57310
			'History and Society.Politics and government'   5550  -->   3482  2068   595  56436
			'History and Society.Society'                   6013  -->   2664  3349   532  56036
			'History and Society.Transportation'            3287  -->   2838   449   140  59154
			'STEM.Biology'                                  2900  -->   2288   612   158  59523
			'STEM.Chemistry'                                1480  -->   1121   359   113  60988
			'STEM.Computing'                                2424  -->   1962   462   318  59839
			'STEM.Earth and environment'                    1704  -->   1131   573   133  60744
			'STEM.Engineering'                              2964  -->   2214   750   228  59389
			'STEM.Libraries & Information'                  1203  -->    847   356    60  61318
			'STEM.Mathematics'                              1172  -->    903   269    56  61353
			'STEM.Medicine & Health'                        2281  -->   1669   612   197  60103
			'STEM.Physics'                                  1560  -->   1120   440   162  60859
			'STEM.STEM*'                                   17878  -->  15778  2100  1018  43685
			'STEM.Space'                                    1746  -->   1594   152    50  60785
			'STEM.Technology'                               4511  -->   3320  1191   561  57509
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.428         0.123
		Culture.Biography.Women                         0.1           0.015
		Culture.Food and drink                          0.022         0.002
		Culture.Internet culture                        0.054         0.004
		Culture.Linguistics                             0.023         0.007
		Culture.Literature                              0.093         0.016
		Culture.Media.Books                             0.025         0.004
		Culture.Media.Entertainment                     0.034         0.004
		Culture.Media.Films                             0.033         0.011
		Culture.Media.Media*                            0.223         0.059
		Culture.Media.Music                             0.044         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.033         0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.011
		Culture.Sports                                  0.133         0.071
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.03          0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.091         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.016         0
		Geography.Regions.Africa.Northern Africa        0.032         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.012         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.134         0.064
		Geography.Regions.Americas.South America        0.026         0.006
		Geography.Regions.Asia.Asia*                    0.192         0.046
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.045         0.011
		Geography.Regions.Asia.North Asia               0.025         0.001
		Geography.Regions.Asia.South Asia               0.03          0.015
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.066         0.011
		Geography.Regions.Europe.Eastern Europe         0.047         0.013
		Geography.Regions.Europe.Europe*                0.209         0.076
		Geography.Regions.Europe.Northern Europe        0.064         0.031
		Geography.Regions.Europe.Southern Europe        0.045         0.013
		Geography.Regions.Europe.Western Europe         0.065         0.019
		Geography.Regions.Oceania                       0.036         0.015
		History and Society.Business and economics      0.058         0.01
		History and Society.Education                   0.032         0.007
		History and Society.History                     0.075         0.011
		History and Society.Military and warfare        0.077         0.014
		History and Society.Politics and government     0.089         0.028
		History and Society.Society                     0.096         0.013
		History and Society.Transportation              0.053         0.015
		STEM.Biology                                    0.046         0.034
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.039         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.047         0.005
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.019         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.025         0.001
		STEM.STEM*                                      0.286         0.069
		STEM.Space                                      0.028         0.006
		STEM.Technology                                 0.072         0.005
	match_rate (micro=0.056, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.143
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.01
		Culture.Media.Media*                         0.078
		Culture.Media.Music                          0.023
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.071
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.08
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.096
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.023
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.028
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.857
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.99
		Culture.Media.Media*                         0.922
		Culture.Media.Music                          0.977
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.92
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.904
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.972
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.791, macro=0.728):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.761
		Culture.Food and drink                       0.737
		Culture.Internet culture                     0.835
		Culture.Linguistics                          0.691
		Culture.Literature                           0.75
		Culture.Media.Books                          0.769
		Culture.Media.Entertainment                  0.492
		Culture.Media.Films                          0.792
		Culture.Media.Media*                         0.838
		Culture.Media.Music                          0.754
		Culture.Media.Radio                          0.51
		Culture.Media.Software                       0.78
		Culture.Media.Television                     0.602
		Culture.Media.Video games                    0.895
		Culture.Performing arts                      0.511
		Culture.Philosophy and religion              0.525
		Culture.Sports                               0.913
		Culture.Visual arts.Architecture             0.706
		Culture.Visual arts.Comics and Anime         0.802
		Culture.Visual arts.Fashion                  0.742
		Culture.Visual arts.Visual arts*             0.738
		Geography.Geographical                       0.735
		Geography.Regions.Africa.Africa*             0.842
		Geography.Regions.Africa.Central Africa      0.111
		Geography.Regions.Africa.Eastern Africa      0.805
		Geography.Regions.Africa.Northern Africa     0.78
		Geography.Regions.Africa.Southern Africa     0.797
		Geography.Regions.Africa.Western Africa      0.798
		Geography.Regions.Americas.Central America   0.67
		Geography.Regions.Americas.North America     0.692
		Geography.Regions.Americas.South America     0.77
		Geography.Regions.Asia.Asia*                 0.846
		Geography.Regions.Asia.Central Asia          0.801
		Geography.Regions.Asia.East Asia             0.77
		Geography.Regions.Asia.North Asia            0.741
		Geography.Regions.Asia.South Asia            0.8
		Geography.Regions.Asia.Southeast Asia        0.771
		Geography.Regions.Asia.West Asia             0.826
		Geography.Regions.Europe.Eastern Europe      0.763
		Geography.Regions.Europe.Europe*             0.795
		Geography.Regions.Europe.Northern Europe     0.662
		Geography.Regions.Europe.Southern Europe     0.752
		Geography.Regions.Europe.Western Europe      0.762
		Geography.Regions.Oceania                    0.837
		History and Society.Business and economics   0.565
		History and Society.Education                0.442
		History and Society.History                  0.499
		History and Society.Military and warfare     0.705
		History and Society.Politics and government  0.627
		History and Society.Society                  0.443
		History and Society.Transportation           0.863
		STEM.Biology                                 0.789
		STEM.Chemistry                               0.757
		STEM.Computing                               0.809
		STEM.Earth and environment                   0.664
		STEM.Engineering                             0.747
		STEM.Libraries & Information                 0.704
		STEM.Mathematics                             0.77
		STEM.Medicine & Health                       0.732
		STEM.Physics                                 0.718
		STEM.STEM*                                   0.883
		STEM.Space                                   0.913
		STEM.Technology                              0.736
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.972
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.995
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.698, macro=0.567):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.827
		Culture.Biography.Women                      0.453
		Culture.Food and drink                       0.553
		Culture.Internet culture                     0.519
		Culture.Linguistics                          0.853
		Culture.Literature                           0.581
		Culture.Media.Books                          0.676
		Culture.Media.Entertainment                  0.349
		Culture.Media.Films                          0.873
		Culture.Media.Media*                         0.629
		Culture.Media.Music                          0.792
		Culture.Media.Radio                          0.421
		Culture.Media.Software                       0.199
		Culture.Media.Television                     0.614
		Culture.Media.Video games                    0.789
		Culture.Performing arts                      0.418
		Culture.Philosophy and religion              0.527
		Culture.Sports                               0.92
		Culture.Visual arts.Architecture             0.729
		Culture.Visual arts.Comics and Anime         0.522
		Culture.Visual arts.Fashion                  0.329
		Culture.Visual arts.Visual arts*             0.659
		Geography.Geographical                       0.755
		Geography.Regions.Africa.Africa*             0.555
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.361
		Geography.Regions.Africa.Northern Africa     0.219
		Geography.Regions.Africa.Southern Africa     0.494
		Geography.Regions.Africa.Western Africa      0.546
		Geography.Regions.Americas.Central America   0.647
		Geography.Regions.Americas.North America     0.555
		Geography.Regions.Americas.South America     0.721
		Geography.Regions.Asia.Asia*                 0.696
		Geography.Regions.Asia.Central Asia          0.339
		Geography.Regions.Asia.East Asia             0.703
		Geography.Regions.Asia.North Asia            0.169
		Geography.Regions.Asia.South Asia            0.919
		Geography.Regions.Asia.Southeast Asia        0.807
		Geography.Regions.Asia.West Asia             0.636
		Geography.Regions.Europe.Eastern Europe      0.692
		Geography.Regions.Europe.Europe*             0.634
		Geography.Regions.Europe.Northern Europe     0.669
		Geography.Regions.Europe.Southern Europe     0.689
		Geography.Regions.Europe.Western Europe      0.649
		Geography.Regions.Oceania                    0.923
		History and Society.Business and economics   0.444
		History and Society.Education                0.537
		History and Society.History                  0.333
		History and Society.Military and warfare     0.566
		History and Society.Politics and government  0.636
		History and Society.Society                  0.376
		History and Society.Transportation           0.849
		STEM.Biology                                 0.912
		STEM.Chemistry                               0.39
		STEM.Computing                               0.292
		STEM.Earth and environment                   0.581
		STEM.Engineering                             0.507
		STEM.Libraries & Information                 0.309
		STEM.Mathematics                             0.261
		STEM.Medicine & Health                       0.591
		STEM.Physics                                 0.187
		STEM.STEM*                                   0.742
		STEM.Space                                   0.871
		STEM.Technology                              0.282
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.997):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.994
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.993
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.983
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.997
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.996
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.989
		History and Society.Society                  0.993
		History and Society.Transportation           0.998
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
	f1 (micro=0.737, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.889
		Culture.Biography.Women                      0.568
		Culture.Food and drink                       0.632
		Culture.Internet culture                     0.64
		Culture.Linguistics                          0.764
		Culture.Literature                           0.655
		Culture.Media.Books                          0.719
		Culture.Media.Entertainment                  0.409
		Culture.Media.Films                          0.83
		Culture.Media.Media*                         0.719
		Culture.Media.Music                          0.772
		Culture.Media.Radio                          0.462
		Culture.Media.Software                       0.318
		Culture.Media.Television                     0.608
		Culture.Media.Video games                    0.838
		Culture.Performing arts                      0.46
		Culture.Philosophy and religion              0.526
		Culture.Sports                               0.916
		Culture.Visual arts.Architecture             0.717
		Culture.Visual arts.Comics and Anime         0.633
		Culture.Visual arts.Fashion                  0.456
		Culture.Visual arts.Visual arts*             0.696
		Geography.Geographical                       0.745
		Geography.Regions.Africa.Africa*             0.669
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.498
		Geography.Regions.Africa.Northern Africa     0.342
		Geography.Regions.Africa.Southern Africa     0.61
		Geography.Regions.Africa.Western Africa      0.649
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.616
		Geography.Regions.Americas.South America     0.745
		Geography.Regions.Asia.Asia*                 0.764
		Geography.Regions.Asia.Central Asia          0.477
		Geography.Regions.Asia.East Asia             0.735
		Geography.Regions.Asia.North Asia            0.276
		Geography.Regions.Asia.South Asia            0.856
		Geography.Regions.Asia.Southeast Asia        0.789
		Geography.Regions.Asia.West Asia             0.719
		Geography.Regions.Europe.Eastern Europe      0.726
		Geography.Regions.Europe.Europe*             0.706
		Geography.Regions.Europe.Northern Europe     0.665
		Geography.Regions.Europe.Southern Europe     0.719
		Geography.Regions.Europe.Western Europe      0.701
		Geography.Regions.Oceania                    0.878
		History and Society.Business and economics   0.497
		History and Society.Education                0.485
		History and Society.History                  0.399
		History and Society.Military and warfare     0.628
		History and Society.Politics and government  0.632
		History and Society.Society                  0.407
		History and Society.Transportation           0.856
		STEM.Biology                                 0.846
		STEM.Chemistry                               0.515
		STEM.Computing                               0.43
		STEM.Earth and environment                   0.619
		STEM.Engineering                             0.604
		STEM.Libraries & Information                 0.43
		STEM.Mathematics                             0.39
		STEM.Medicine & Health                       0.654
		STEM.Physics                                 0.297
		STEM.STEM*                                   0.806
		STEM.Space                                   0.891
		STEM.Technology                              0.408
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.983
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.998
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.971
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.988
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.988
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.945
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.988
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.979
		History and Society.Society                  0.984
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.971
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.028
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.001
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.001
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.004
		Culture.Media.Television                     0.003
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.038
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.01
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.009
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.005
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.975, macro=0.974):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.983
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.979
		Culture.Literature                           0.977
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.968
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.972
		Culture.Media.Software                       0.986
		Culture.Media.Television                     0.977
		Culture.Media.Video games                    0.994
		Culture.Performing arts                      0.978
		Culture.Philosophy and religion              0.952
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.974
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.981
		Geography.Regions.Africa.Central Africa      0.731
		Geography.Regions.Africa.Eastern Africa      0.985
		Geography.Regions.Africa.Northern Africa     0.982
		Geography.Regions.Africa.Southern Africa     0.983
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.979
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.983
		Geography.Regions.Asia.East Asia             0.979
		Geography.Regions.Asia.North Asia            0.984
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.982
		Geography.Regions.Asia.West Asia             0.983
		Geography.Regions.Europe.Eastern Europe      0.984
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.981
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.983
		History and Society.Business and economics   0.963
		History and Society.Education                0.957
		History and Society.History                  0.947
		History and Society.Military and warfare     0.972
		History and Society.Politics and government  0.96
		History and Society.Society                  0.926
		History and Society.Transportation           0.986
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.986
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.977
		STEM.Engineering                             0.981
		STEM.Libraries & Information                 0.978
		STEM.Mathematics                             0.985
		STEM.Medicine & Health                       0.979
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.977
		STEM.Space                                   0.993
		STEM.Technology                              0.976
		-------------------------------------------  -----
	pr_auc (micro=0.784, macro=0.641):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.948
		Culture.Biography.Women                      0.557
		Culture.Food and drink                       0.624
		Culture.Internet culture                     0.751
		Culture.Linguistics                          0.778
		Culture.Literature                           0.729
		Culture.Media.Books                          0.77
		Culture.Media.Entertainment                  0.387
		Culture.Media.Films                          0.873
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.794
		Culture.Media.Radio                          0.404
		Culture.Media.Software                       0.399
		Culture.Media.Television                     0.646
		Culture.Media.Video games                    0.882
		Culture.Performing arts                      0.407
		Culture.Philosophy and religion              0.515
		Culture.Sports                               0.95
		Culture.Visual arts.Architecture             0.747
		Culture.Visual arts.Comics and Anime         0.722
		Culture.Visual arts.Fashion                  0.471
		Culture.Visual arts.Visual arts*             0.738
		Geography.Geographical                       0.797
		Geography.Regions.Africa.Africa*             0.709
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.384
		Geography.Regions.Africa.Northern Africa     0.293
		Geography.Regions.Africa.Southern Africa     0.515
		Geography.Regions.Africa.Western Africa      0.581
		Geography.Regions.Americas.Central America   0.623
		Geography.Regions.Americas.North America     0.638
		Geography.Regions.Americas.South America     0.736
		Geography.Regions.Asia.Asia*                 0.847
		Geography.Regions.Asia.Central Asia          0.388
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.26
		Geography.Regions.Asia.South Asia            0.894
		Geography.Regions.Asia.Southeast Asia        0.794
		Geography.Regions.Asia.West Asia             0.763
		Geography.Regions.Europe.Eastern Europe      0.762
		Geography.Regions.Europe.Europe*             0.781
		Geography.Regions.Europe.Northern Europe     0.731
		Geography.Regions.Europe.Southern Europe     0.762
		Geography.Regions.Europe.Western Europe      0.722
		Geography.Regions.Oceania                    0.888
		History and Society.Business and economics   0.469
		History and Society.Education                0.462
		History and Society.History                  0.362
		History and Society.Military and warfare     0.688
		History and Society.Politics and government  0.659
		History and Society.Society                  0.376
		History and Society.Transportation           0.891
		STEM.Biology                                 0.9
		STEM.Chemistry                               0.54
		STEM.Computing                               0.51
		STEM.Earth and environment                   0.637
		STEM.Engineering                             0.651
		STEM.Libraries & Information                 0.442
		STEM.Mathematics                             0.554
		STEM.Medicine & Health                       0.691
		STEM.Physics                                 0.326
		STEM.STEM*                                   0.904
		STEM.Space                                   0.948
		STEM.Technology                              0.48
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

