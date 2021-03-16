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
	counts (n=55230):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13830  -->  12129  1701   869  40531
			'Culture.Biography.Women'                       3519  -->   2306  1213   387  51324
			'Culture.Food and drink'                        1408  -->    991   417   111  53711
			'Culture.Internet culture'                      2130  -->   1817   313   163  52937
			'Culture.Linguistics'                           2107  -->   1496   611   143  52980
			'Culture.Literature'                            4764  -->   3395  1369   451  50015
			'Culture.Media.Books'                           1275  -->    996   279    83  53872
			'Culture.Media.Entertainment'                   2102  -->   1162   940   230  52898
			'Culture.Media.Films'                           3089  -->   2784   305    93  52048
			'Culture.Media.Media*'                         11397  -->   9862  1535  1035  42798
			'Culture.Media.Music'                           2693  -->   2222   471   146  52391
			'Culture.Media.Radio'                            239  -->    161    78    42  54949
			'Culture.Media.Software'                        1983  -->   1826   157   197  53050
			'Culture.Media.Television'                      1712  -->   1330   382    97  53421
			'Culture.Media.Video games'                      643  -->    609    34    17  54570
			'Culture.Performing arts'                       1527  -->    934   593   125  53578
			'Culture.Philosophy and religion'               4046  -->   2126  1920   351  50833
			'Culture.Sports'                                3611  -->   2873   738   133  51486
			'Culture.Visual arts.Architecture'              2455  -->   1837   618   246  52529
			'Culture.Visual arts.Comics and Anime'          1147  -->    959   188    53  54030
			'Culture.Visual arts.Fashion'                    601  -->    384   217    24  54605
			'Culture.Visual arts.Visual arts*'              4876  -->   3433  1443   430  49924
			'Geography.Geographical'                        4334  -->   2729  1605   703  50193
			'Geography.Regions.Africa.Africa*'              3798  -->   2395  1403   345  51087
			'Geography.Regions.Africa.Central Africa'        791  -->    478   313   115  54324
			'Geography.Regions.Africa.Eastern Africa'        354  -->    215   139    42  54834
			'Geography.Regions.Africa.Northern Africa'      1474  -->    983   491   109  53647
			'Geography.Regions.Africa.Southern Africa'       578  -->    373   205    49  54603
			'Geography.Regions.Africa.Western Africa'         71  -->     39    32    43  55116
			'Geography.Regions.Americas.Central America'    1367  -->    670   697   146  53717
			'Geography.Regions.Americas.North America'      6463  -->   4667  1796   736  48031
			'Geography.Regions.Americas.South America'      1771  -->   1241   530   127  53332
			'Geography.Regions.Asia.Asia*'                  9516  -->   7300  2216   749  44965
			'Geography.Regions.Asia.Central Asia'            875  -->    631   244    51  54304
			'Geography.Regions.Asia.East Asia'              3238  -->   2639   599   185  51807
			'Geography.Regions.Asia.North Asia'             1326  -->   1085   241   124  53780
			'Geography.Regions.Asia.South Asia'             1733  -->   1192   541    83  53414
			'Geography.Regions.Asia.Southeast Asia'         1716  -->    839   877   179  53335
			'Geography.Regions.Asia.West Asia'              2253  -->   1601   652   128  52849
			'Geography.Regions.Europe.Eastern Europe'       2948  -->   2391   557   166  52116
			'Geography.Regions.Europe.Europe*'             16574  -->  13681  2893  1986  36670
			'Geography.Regions.Europe.Northern Europe'      4108  -->   3057  1051   290  50832
			'Geography.Regions.Europe.Southern Europe'      5331  -->   3850  1481   641  49258
			'Geography.Regions.Europe.Western Europe'       5063  -->   3840  1223   406  49761
			'Geography.Regions.Oceania'                     1871  -->   1103   768   205  53154
			'History and Society.Business and economics'    3041  -->   1820  1221   240  51949
			'History and Society.Education'                 1722  -->    859   863   109  53399
			'History and Society.History'                   5917  -->   3636  2281   714  48599
			'History and Society.Military and warfare'      4042  -->   2504  1538   407  50781
			'History and Society.Politics and government'   4581  -->   2321  2260   514  50135
			'History and Society.Society'                   6679  -->   3044  3635   603  47948
			'History and Society.Transportation'            2451  -->   1975   476    86  52693
			'STEM.Biology'                                  6701  -->   6063   638   146  48383
			'STEM.Chemistry'                                1508  -->   1187   321   139  53583
			'STEM.Computing'                                2429  -->   2092   337   159  52642
			'STEM.Earth and environment'                    1808  -->   1241   567   124  53298
			'STEM.Engineering'                              2475  -->   1726   749   177  52578
			'STEM.Libraries & Information'                   460  -->    354   106    23  54747
			'STEM.Mathematics'                              1057  -->    919   138    32  54141
			'STEM.Medicine & Health'                        1892  -->   1277   615   146  53192
			'STEM.Physics'                                  1525  -->   1080   445   147  53558
			'STEM.STEM*'                                   19559  -->  17742  1817   937  34734
			'STEM.Space'                                    1819  -->   1646   173    42  53369
			'STEM.Technology'                               4295  -->   3267  1028   522  50413
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
		Culture.Visual arts.Architecture             0.013
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.028
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.004
		Geography.Regions.Americas.North America     0.061
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.051
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.012
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.01
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.11
		Geography.Regions.Europe.Northern Europe     0.028
		Geography.Regions.Europe.Southern Europe     0.022
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.006
		History and Society.History                  0.021
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.024
		History and Society.Society                  0.018
		History and Society.Transportation           0.014
		STEM.Biology                                 0.033
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
		Culture.Visual arts.Architecture             0.987
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.972
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.939
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.949
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.988
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.99
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.89
		Geography.Regions.Europe.Northern Europe     0.972
		Geography.Regions.Europe.Southern Europe     0.978
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.979
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.982
		History and Society.Transportation           0.986
		STEM.Biology                                 0.967
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
	recall (micro=0.769, macro=0.718):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.877
		Culture.Biography.Women                      0.655
		Culture.Food and drink                       0.704
		Culture.Internet culture                     0.853
		Culture.Linguistics                          0.71
		Culture.Literature                           0.713
		Culture.Media.Books                          0.781
		Culture.Media.Entertainment                  0.553
		Culture.Media.Films                          0.901
		Culture.Media.Media*                         0.865
		Culture.Media.Music                          0.825
		Culture.Media.Radio                          0.674
		Culture.Media.Software                       0.921
		Culture.Media.Television                     0.777
		Culture.Media.Video games                    0.947
		Culture.Performing arts                      0.612
		Culture.Philosophy and religion              0.525
		Culture.Sports                               0.796
		Culture.Visual arts.Architecture             0.748
		Culture.Visual arts.Comics and Anime         0.836
		Culture.Visual arts.Fashion                  0.639
		Culture.Visual arts.Visual arts*             0.704
		Geography.Geographical                       0.63
		Geography.Regions.Africa.Africa*             0.631
		Geography.Regions.Africa.Central Africa      0.604
		Geography.Regions.Africa.Eastern Africa      0.607
		Geography.Regions.Africa.Northern Africa     0.667
		Geography.Regions.Africa.Southern Africa     0.645
		Geography.Regions.Africa.Western Africa      0.549
		Geography.Regions.Americas.Central America   0.49
		Geography.Regions.Americas.North America     0.722
		Geography.Regions.Americas.South America     0.701
		Geography.Regions.Asia.Asia*                 0.767
		Geography.Regions.Asia.Central Asia          0.721
		Geography.Regions.Asia.East Asia             0.815
		Geography.Regions.Asia.North Asia            0.818
		Geography.Regions.Asia.South Asia            0.688
		Geography.Regions.Asia.Southeast Asia        0.489
		Geography.Regions.Asia.West Asia             0.711
		Geography.Regions.Europe.Eastern Europe      0.811
		Geography.Regions.Europe.Europe*             0.825
		Geography.Regions.Europe.Northern Europe     0.744
		Geography.Regions.Europe.Southern Europe     0.722
		Geography.Regions.Europe.Western Europe      0.758
		Geography.Regions.Oceania                    0.59
		History and Society.Business and economics   0.598
		History and Society.Education                0.499
		History and Society.History                  0.615
		History and Society.Military and warfare     0.619
		History and Society.Politics and government  0.507
		History and Society.Society                  0.456
		History and Society.Transportation           0.806
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.787
		STEM.Computing                               0.861
		STEM.Earth and environment                   0.686
		STEM.Engineering                             0.697
		STEM.Libraries & Information                 0.77
		STEM.Mathematics                             0.869
		STEM.Medicine & Health                       0.675
		STEM.Physics                                 0.708
		STEM.STEM*                                   0.907
		STEM.Space                                   0.905
		STEM.Technology                              0.761
		-------------------------------------------  -----
	!recall (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.993
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
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.997
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.985
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.998
		History and Society.History                  0.986
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.99
		History and Society.Society                  0.988
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.974
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.706, macro=0.568):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.854
		Culture.Biography.Women                      0.564
		Culture.Food and drink                       0.457
		Culture.Internet culture                     0.494
		Culture.Linguistics                          0.661
		Culture.Literature                           0.557
		Culture.Media.Books                          0.672
		Culture.Media.Entertainment                  0.315
		Culture.Media.Films                          0.843
		Culture.Media.Media*                         0.695
		Culture.Media.Music                          0.879
		Culture.Media.Radio                          0.656
		Culture.Media.Software                       0.249
		Culture.Media.Television                     0.792
		Culture.Media.Video games                    0.888
		Culture.Performing arts                      0.432
		Culture.Philosophy and religion              0.452
		Culture.Sports                               0.959
		Culture.Visual arts.Architecture             0.632
		Culture.Visual arts.Comics and Anime         0.652
		Culture.Visual arts.Fashion                  0.541
		Culture.Visual arts.Visual arts*             0.606
		Geography.Geographical                       0.524
		Geography.Regions.Africa.Africa*             0.425
		Geography.Regions.Africa.Central Africa      0.153
		Geography.Regions.Africa.Eastern Africa      0.265
		Geography.Regions.Africa.Northern Africa     0.288
		Geography.Regions.Africa.Southern Africa     0.459
		Geography.Regions.Africa.Western Africa      0.325
		Geography.Regions.Americas.Central America   0.374
		Geography.Regions.Americas.North America     0.767
		Geography.Regions.Americas.South America     0.652
		Geography.Regions.Asia.Asia*                 0.691
		Geography.Regions.Asia.Central Asia          0.4
		Geography.Regions.Asia.East Asia             0.726
		Geography.Regions.Asia.North Asia            0.247
		Geography.Regions.Asia.South Asia            0.872
		Geography.Regions.Asia.Southeast Asia        0.469
		Geography.Regions.Asia.West Asia             0.764
		Geography.Regions.Europe.Eastern Europe      0.768
		Geography.Regions.Europe.Europe*             0.57
		Geography.Regions.Europe.Northern Europe     0.805
		Geography.Regions.Europe.Southern Europe     0.426
		Geography.Regions.Europe.Western Europe      0.647
		Geography.Regions.Oceania                    0.702
		History and Society.Business and economics   0.57
		History and Society.Education                0.645
		History and Society.History                  0.317
		History and Society.Military and warfare     0.526
		History and Society.Politics and government  0.592
		History and Society.Society                  0.319
		History and Society.Transportation           0.883
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.322
		STEM.Computing                               0.435
		STEM.Earth and environment                   0.574
		STEM.Engineering                             0.522
		STEM.Libraries & Information                 0.533
		STEM.Mathematics                             0.38
		STEM.Medicine & Health                       0.614
		STEM.Physics                                 0.18
		STEM.STEM*                                   0.719
		STEM.Space                                   0.874
		STEM.Technology                              0.277
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
		Culture.Media.Media*                         0.992
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
		History and Society.Military and warfare     0.995
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
	f1 (micro=0.729, macro=0.617):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.866
		Culture.Biography.Women                      0.606
		Culture.Food and drink                       0.554
		Culture.Internet culture                     0.626
		Culture.Linguistics                          0.684
		Culture.Literature                           0.625
		Culture.Media.Books                          0.723
		Culture.Media.Entertainment                  0.401
		Culture.Media.Films                          0.871
		Culture.Media.Media*                         0.771
		Culture.Media.Music                          0.851
		Culture.Media.Radio                          0.665
		Culture.Media.Software                       0.392
		Culture.Media.Television                     0.784
		Culture.Media.Video games                    0.917
		Culture.Performing arts                      0.506
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.87
		Culture.Visual arts.Architecture             0.685
		Culture.Visual arts.Comics and Anime         0.733
		Culture.Visual arts.Fashion                  0.586
		Culture.Visual arts.Visual arts*             0.651
		Geography.Geographical                       0.572
		Geography.Regions.Africa.Africa*             0.508
		Geography.Regions.Africa.Central Africa      0.244
		Geography.Regions.Africa.Eastern Africa      0.369
		Geography.Regions.Africa.Northern Africa     0.402
		Geography.Regions.Africa.Southern Africa     0.536
		Geography.Regions.Africa.Western Africa      0.408
		Geography.Regions.Americas.Central America   0.425
		Geography.Regions.Americas.North America     0.744
		Geography.Regions.Americas.South America     0.675
		Geography.Regions.Asia.Asia*                 0.727
		Geography.Regions.Asia.Central Asia          0.514
		Geography.Regions.Asia.East Asia             0.768
		Geography.Regions.Asia.North Asia            0.38
		Geography.Regions.Asia.South Asia            0.769
		Geography.Regions.Asia.Southeast Asia        0.479
		Geography.Regions.Asia.West Asia             0.736
		Geography.Regions.Europe.Eastern Europe      0.789
		Geography.Regions.Europe.Europe*             0.674
		Geography.Regions.Europe.Northern Europe     0.774
		Geography.Regions.Europe.Southern Europe     0.536
		Geography.Regions.Europe.Western Europe      0.698
		Geography.Regions.Oceania                    0.641
		History and Society.Business and economics   0.584
		History and Society.Education                0.562
		History and Society.History                  0.419
		History and Society.Military and warfare     0.569
		History and Society.Politics and government  0.546
		History and Society.Society                  0.375
		History and Society.Transportation           0.843
		STEM.Biology                                 0.909
		STEM.Chemistry                               0.457
		STEM.Computing                               0.578
		STEM.Earth and environment                   0.625
		STEM.Engineering                             0.597
		STEM.Libraries & Information                 0.629
		STEM.Mathematics                             0.529
		STEM.Medicine & Health                       0.643
		STEM.Physics                                 0.287
		STEM.STEM*                                   0.802
		STEM.Space                                   0.889
		STEM.Technology                              0.406
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
		Culture.Media.Music                          0.996
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
		Geography.Regions.Africa.Western Africa      0.999
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
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.988
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
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.978, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.988
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.995
		Culture.Literature                           0.987
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.997
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
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.939
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.984
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.991
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.976
		History and Society.Society                  0.981
		History and Society.Transportation           0.995
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
		STEM.Technology                              0.989
		-------------------------------------------  -----
	fpr (micro=0.014, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.007
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
		Culture.Media.Video games                    0
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.003
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.014
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.015
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.016
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.003
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.051
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.004
		History and Society.Business and economics   0.005
		History and Society.Education                0.002
		History and Society.History                  0.014
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.01
		History and Society.Society                  0.012
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.003
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.026
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.971):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.987
		Culture.Linguistics                          0.975
		Culture.Literature                           0.975
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.972
		Culture.Media.Films                          0.986
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.983
		Culture.Media.Radio                          0.923
		Culture.Media.Software                       0.989
		Culture.Media.Television                     0.982
		Culture.Media.Video games                    0.99
		Culture.Performing arts                      0.971
		Culture.Philosophy and religion              0.95
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.98
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.965
		Geography.Regions.Africa.Africa*             0.968
		Geography.Regions.Africa.Central Africa      0.973
		Geography.Regions.Africa.Eastern Africa      0.958
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.973
		Geography.Regions.Africa.Western Africa      0.832
		Geography.Regions.Americas.Central America   0.966
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.979
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.98
		Geography.Regions.Asia.North Asia            0.986
		Geography.Regions.Asia.South Asia            0.975
		Geography.Regions.Asia.Southeast Asia        0.969
		Geography.Regions.Asia.West Asia             0.975
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.974
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.974
		History and Society.Business and economics   0.965
		History and Society.Education                0.963
		History and Society.History                  0.956
		History and Society.Military and warfare     0.968
		History and Society.Politics and government  0.947
		History and Society.Society                  0.925
		History and Society.Transportation           0.982
		STEM.Biology                                 0.984
		STEM.Chemistry                               0.983
		STEM.Computing                               0.989
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.974
		STEM.Libraries & Information                 0.957
		STEM.Mathematics                             0.987
		STEM.Medicine & Health                       0.974
		STEM.Physics                                 0.981
		STEM.STEM*                                   0.978
		STEM.Space                                   0.99
		STEM.Technology                              0.978
		-------------------------------------------  -----
	pr_auc (micro=0.779, macro=0.62):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.927
		Culture.Biography.Women                      0.601
		Culture.Food and drink                       0.514
		Culture.Internet culture                     0.697
		Culture.Linguistics                          0.717
		Culture.Literature                           0.674
		Culture.Media.Books                          0.735
		Culture.Media.Entertainment                  0.353
		Culture.Media.Films                          0.883
		Culture.Media.Media*                         0.863
		Culture.Media.Music                          0.895
		Culture.Media.Radio                          0.446
		Culture.Media.Software                       0.507
		Culture.Media.Television                     0.819
		Culture.Media.Video games                    0.899
		Culture.Performing arts                      0.426
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.928
		Culture.Visual arts.Architecture             0.704
		Culture.Visual arts.Comics and Anime         0.754
		Culture.Visual arts.Fashion                  0.457
		Culture.Visual arts.Visual arts*             0.679
		Geography.Geographical                       0.603
		Geography.Regions.Africa.Africa*             0.518
		Geography.Regions.Africa.Central Africa      0.143
		Geography.Regions.Africa.Eastern Africa      0.185
		Geography.Regions.Africa.Northern Africa     0.372
		Geography.Regions.Africa.Southern Africa     0.37
		Geography.Regions.Africa.Western Africa      0.227
		Geography.Regions.Americas.Central America   0.38
		Geography.Regions.Americas.North America     0.82
		Geography.Regions.Americas.South America     0.74
		Geography.Regions.Asia.Asia*                 0.796
		Geography.Regions.Asia.Central Asia          0.567
		Geography.Regions.Asia.East Asia             0.779
		Geography.Regions.Asia.North Asia            0.385
		Geography.Regions.Asia.South Asia            0.799
		Geography.Regions.Asia.Southeast Asia        0.44
		Geography.Regions.Asia.West Asia             0.746
		Geography.Regions.Europe.Eastern Europe      0.806
		Geography.Regions.Europe.Europe*             0.785
		Geography.Regions.Europe.Northern Europe     0.809
		Geography.Regions.Europe.Southern Europe     0.617
		Geography.Regions.Europe.Western Europe      0.746
		Geography.Regions.Oceania                    0.665
		History and Society.Business and economics   0.574
		History and Society.Education                0.533
		History and Society.History                  0.42
		History and Society.Military and warfare     0.595
		History and Society.Politics and government  0.557
		History and Society.Society                  0.334
		History and Society.Transportation           0.891
		STEM.Biology                                 0.932
		STEM.Chemistry                               0.435
		STEM.Computing                               0.71
		STEM.Earth and environment                   0.608
		STEM.Engineering                             0.624
		STEM.Libraries & Information                 0.454
		STEM.Mathematics                             0.586
		STEM.Medicine & Health                       0.643
		STEM.Physics                                 0.246
		STEM.STEM*                                   0.907
		STEM.Space                                   0.919
		STEM.Technology                              0.444
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}}}}}

