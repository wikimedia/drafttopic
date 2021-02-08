Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'init': None, 'center': False, 'verbose': 0, 'n_estimators': 150, 'criterion': 'friedman_mse', 'multilabel': True, 'max_leaf_nodes': None, 'subsample': 1.0, 'max_depth': 5, 'min_impurity_decrease': 0.0, 'tol': 0.0001, 'label_weights': {}, 'max_features': 'log2', 'presort': 'deprecated', 'warm_start': False, 'loss': 'deviance', 'n_iter_no_change': None, 'min_samples_leaf': 1, 'ccp_alpha': 0.0, 'learning_rate': 0.1, 'validation_fraction': 0.1, 'scale': False, 'min_impurity_split': None, 'min_samples_split': 2, 'random_state': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'population_rates': None, 'min_weight_fraction_leaf': 0.0}
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
	counts (n=60604):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14925  -->  12996  1929  1075  44604
			'Culture.Biography.Women'                       3694  -->   2549  1145   375  56535
			'Culture.Food and drink'                        1403  -->    910   493   120  59081
			'Culture.Internet culture'                      3113  -->   2367   746   253  57238
			'Culture.Linguistics'                           1586  -->   1004   582   127  58891
			'Culture.Literature'                            5267  -->   3744  1523   547  54790
			'Culture.Media.Books'                           1801  -->   1303   498   165  58638
			'Culture.Media.Entertainment'                   2113  -->    768  1345   269  58222
			'Culture.Media.Films'                           2869  -->   2365   504   155  57580
			'Culture.Media.Media*'                         13520  -->  11245  2275  1427  45657
			'Culture.Media.Music'                           2706  -->   2098   608   233  57665
			'Culture.Media.Radio'                            468  -->    186   282    56  60080
			'Culture.Media.Software'                        2099  -->   1441   658   399  58106
			'Culture.Media.Television'                      1918  -->   1364   554   144  58542
			'Culture.Media.Video games'                     2049  -->   1779   270    75  58480
			'Culture.Performing arts'                       1407  -->    729   678   152  59045
			'Culture.Philosophy and religion'               3437  -->   1566  1871   372  56795
			'Culture.Sports'                                5565  -->   4829   736   208  54831
			'Culture.Visual arts.Architecture'              2110  -->   1317   793   246  58248
			'Culture.Visual arts.Comics and Anime'          1616  -->   1254   362    84  58904
			'Culture.Visual arts.Fashion'                   1153  -->    711   442    85  59366
			'Culture.Visual arts.Visual arts*'              5579  -->   3705  1874   471  54554
			'Geography.Geographical'                        4478  -->   2894  1584   590  55536
			'Geography.Regions.Africa.Africa*'              4982  -->   3434  1548   398  55224
			'Geography.Regions.Africa.Central Africa'       1142  -->    766   376    91  59371
			'Geography.Regions.Africa.Eastern Africa'        710  -->    522   188    24  59870
			'Geography.Regions.Africa.Northern Africa'      1411  -->    814   597   137  59056
			'Geography.Regions.Africa.Southern Africa'       884  -->    482   402    59  59661
			'Geography.Regions.Africa.Western Africa'        367  -->    204   163    58  60179
			'Geography.Regions.Americas.Central America'    1303  -->    687   616    72  59229
			'Geography.Regions.Americas.North America'      5367  -->   3054  2313   736  54501
			'Geography.Regions.Americas.South America'      1490  -->    940   550    84  59030
			'Geography.Regions.Asia.Asia*'                 12405  -->   9446  2959  1295  46904
			'Geography.Regions.Asia.Central Asia'           1288  -->    794   494   120  59196
			'Geography.Regions.Asia.East Asia'              2859  -->   2021   838   230  57515
			'Geography.Regions.Asia.North Asia'             3795  -->   2379  1416   514  56295
			'Geography.Regions.Asia.South Asia'             1694  -->   1167   527    97  58813
			'Geography.Regions.Asia.Southeast Asia'         1479  -->    896   583    75  59050
			'Geography.Regions.Asia.West Asia'              2470  -->   1655   815   183  57951
			'Geography.Regions.Europe.Eastern Europe'       6615  -->   4700  1915   733  53256
			'Geography.Regions.Europe.Europe*'             17339  -->  13257  4082  2411  40854
			'Geography.Regions.Europe.Northern Europe'      3501  -->   1963  1538   349  56754
			'Geography.Regions.Europe.Southern Europe'      3601  -->   2348  1253   370  56633
			'Geography.Regions.Europe.Western Europe'       4385  -->   3002  1383   443  55776
			'Geography.Regions.Oceania'                     1755  -->   1101   654   128  58721
			'History and Society.Business and economics'    3580  -->   1880  1700   487  56537
			'History and Society.Education'                 1692  -->    795   897   153  58759
			'History and Society.History'                   5054  -->   2449  2605   705  54845
			'History and Society.Military and warfare'      4517  -->   2691  1826   524  55563
			'History and Society.Politics and government'   4076  -->   1860  2216   438  56090
			'History and Society.Society'                   3867  -->    765  3102   222  56515
			'History and Society.Transportation'            3613  -->   3015   598   186  56805
			'STEM.Biology'                                  3636  -->   2867   769   252  56716
			'STEM.Chemistry'                                1415  -->    885   530   195  58994
			'STEM.Computing'                                2643  -->   1955   688   431  57530
			'STEM.Earth and environment'                    1864  -->    984   880   207  58533
			'STEM.Engineering'                              2988  -->   2158   830   212  57404
			'STEM.Libraries & Information'                  1031  -->    649   382    91  59482
			'STEM.Mathematics'                              1197  -->    823   374    94  59313
			'STEM.Medicine & Health'                        1792  -->    992   800   155  58657
			'STEM.Physics'                                  1412  -->    804   608   187  59005
			'STEM.STEM*'                                   18347  -->  15871  2476  1329  40928
			'STEM.Space'                                    1816  -->   1546   270    66  58722
			'STEM.Technology'                               4718  -->   3024  1694   749  55137
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.246         0.12
		Culture.Biography.Women                         0.061         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.051         0.004
		Culture.Linguistics                             0.026         0.008
		Culture.Literature                              0.087         0.015
		Culture.Media.Books                             0.03          0.004
		Culture.Media.Entertainment                     0.035         0.004
		Culture.Media.Films                             0.047         0.012
		Culture.Media.Media*                            0.223         0.055
		Culture.Media.Music                             0.045         0.021
		Culture.Media.Radio                             0.008         0.002
		Culture.Media.Software                          0.035         0.001
		Culture.Media.Television                        0.032         0.009
		Culture.Media.Video games                       0.034         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.057         0.01
		Culture.Sports                                  0.092         0.06
		Culture.Visual arts.Architecture                0.035         0.011
		Culture.Visual arts.Comics and Anime            0.027         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.092         0.018
		Geography.Geographical                          0.074         0.021
		Geography.Regions.Africa.Africa*                0.082         0.008
		Geography.Regions.Africa.Central Africa         0.019         0.001
		Geography.Regions.Africa.Eastern Africa         0.012         0.001
		Geography.Regions.Africa.Northern Africa        0.023         0.001
		Geography.Regions.Africa.Southern Africa        0.015         0.001
		Geography.Regions.Africa.Western Africa         0.006         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.089         0.063
		Geography.Regions.Americas.South America        0.025         0.007
		Geography.Regions.Asia.Asia*                    0.205         0.052
		Geography.Regions.Asia.Central Asia             0.021         0.001
		Geography.Regions.Asia.East Asia                0.047         0.012
		Geography.Regions.Asia.North Asia               0.063         0.006
		Geography.Regions.Asia.South Asia               0.028         0.016
		Geography.Regions.Asia.Southeast Asia           0.024         0.006
		Geography.Regions.Asia.West Asia                0.041         0.012
		Geography.Regions.Europe.Eastern Europe         0.109         0.018
		Geography.Regions.Europe.Europe*                0.286         0.081
		Geography.Regions.Europe.Northern Europe        0.058         0.029
		Geography.Regions.Europe.Southern Europe        0.059         0.014
		Geography.Regions.Europe.Western Europe         0.072         0.02
		Geography.Regions.Oceania                       0.029         0.016
		History and Society.Business and economics      0.059         0.01
		History and Society.Education                   0.028         0.008
		History and Society.History                     0.083         0.011
		History and Society.Military and warfare        0.075         0.015
		History and Society.Politics and government     0.067         0.028
		History and Society.Society                     0.064         0.008
		History and Society.Transportation              0.06          0.016
		STEM.Biology                                    0.06          0.034
		STEM.Chemistry                                  0.023         0.002
		STEM.Computing                                  0.044         0.003
		STEM.Earth and environment                      0.031         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.017         0.001
		STEM.Mathematics                                0.02          0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.303         0.065
		STEM.Space                                      0.03          0.004
		STEM.Technology                                 0.078         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.125
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.006
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.074
		Culture.Media.Music                          0.02
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.008
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.013
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.048
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.065
		Geography.Regions.Asia.Central Asia          0.003
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.013
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.026
		Geography.Regions.Europe.Europe*             0.113
		Geography.Regions.Europe.Northern Europe     0.022
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.014
		History and Society.Education                0.006
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.02
		History and Society.Society                  0.006
		History and Society.Transportation           0.017
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.006
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.086
		STEM.Space                                   0.005
		STEM.Technology                              0.017
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.875
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.926
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.992
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.987
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.952
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.935
		Geography.Regions.Asia.Central Asia          0.997
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.987
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.974
		Geography.Regions.Europe.Europe*             0.887
		Geography.Regions.Europe.Northern Europe     0.978
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.986
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.98
		History and Society.Society                  0.994
		History and Society.Transportation           0.983
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.914
		STEM.Space                                   0.995
		STEM.Technology                              0.983
		-------------------------------------------  -----
	recall (micro=0.721, macro=0.65):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.69
		Culture.Food and drink                       0.649
		Culture.Internet culture                     0.76
		Culture.Linguistics                          0.633
		Culture.Literature                           0.711
		Culture.Media.Books                          0.723
		Culture.Media.Entertainment                  0.363
		Culture.Media.Films                          0.824
		Culture.Media.Media*                         0.832
		Culture.Media.Music                          0.775
		Culture.Media.Radio                          0.397
		Culture.Media.Software                       0.687
		Culture.Media.Television                     0.711
		Culture.Media.Video games                    0.868
		Culture.Performing arts                      0.518
		Culture.Philosophy and religion              0.456
		Culture.Sports                               0.868
		Culture.Visual arts.Architecture             0.624
		Culture.Visual arts.Comics and Anime         0.776
		Culture.Visual arts.Fashion                  0.617
		Culture.Visual arts.Visual arts*             0.664
		Geography.Geographical                       0.646
		Geography.Regions.Africa.Africa*             0.689
		Geography.Regions.Africa.Central Africa      0.671
		Geography.Regions.Africa.Eastern Africa      0.735
		Geography.Regions.Africa.Northern Africa     0.577
		Geography.Regions.Africa.Southern Africa     0.545
		Geography.Regions.Africa.Western Africa      0.556
		Geography.Regions.Americas.Central America   0.527
		Geography.Regions.Americas.North America     0.569
		Geography.Regions.Americas.South America     0.631
		Geography.Regions.Asia.Asia*                 0.761
		Geography.Regions.Asia.Central Asia          0.616
		Geography.Regions.Asia.East Asia             0.707
		Geography.Regions.Asia.North Asia            0.627
		Geography.Regions.Asia.South Asia            0.689
		Geography.Regions.Asia.Southeast Asia        0.606
		Geography.Regions.Asia.West Asia             0.67
		Geography.Regions.Europe.Eastern Europe      0.711
		Geography.Regions.Europe.Europe*             0.765
		Geography.Regions.Europe.Northern Europe     0.561
		Geography.Regions.Europe.Southern Europe     0.652
		Geography.Regions.Europe.Western Europe      0.685
		Geography.Regions.Oceania                    0.627
		History and Society.Business and economics   0.525
		History and Society.Education                0.47
		History and Society.History                  0.485
		History and Society.Military and warfare     0.596
		History and Society.Politics and government  0.456
		History and Society.Society                  0.198
		History and Society.Transportation           0.834
		STEM.Biology                                 0.789
		STEM.Chemistry                               0.625
		STEM.Computing                               0.74
		STEM.Earth and environment                   0.528
		STEM.Engineering                             0.722
		STEM.Libraries & Information                 0.629
		STEM.Mathematics                             0.688
		STEM.Medicine & Health                       0.554
		STEM.Physics                                 0.569
		STEM.STEM*                                   0.865
		STEM.Space                                   0.851
		STEM.Technology                              0.641
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.993
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.987
		Geography.Regions.Americas.South America     0.999
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.994
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.997
		History and Society.History                  0.987
		History and Society.Military and warfare     0.991
		History and Society.Politics and government  0.992
		History and Society.Society                  0.996
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	precision (micro=0.667, macro=0.523):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.835
		Culture.Biography.Women                      0.614
		Culture.Food and drink                       0.449
		Culture.Internet culture                     0.392
		Culture.Linguistics                          0.704
		Culture.Literature                           0.52
		Culture.Media.Books                          0.527
		Culture.Media.Entertainment                  0.238
		Culture.Media.Films                          0.782
		Culture.Media.Media*                         0.614
		Culture.Media.Music                          0.805
		Culture.Media.Radio                          0.498
		Culture.Media.Software                       0.116
		Culture.Media.Television                     0.722
		Culture.Media.Video games                    0.663
		Culture.Performing arts                      0.381
		Culture.Philosophy and religion              0.423
		Culture.Sports                               0.936
		Culture.Visual arts.Architecture             0.618
		Culture.Visual arts.Comics and Anime         0.566
		Culture.Visual arts.Fashion                  0.279
		Culture.Visual arts.Visual arts*             0.588
		Geography.Geographical                       0.57
		Geography.Regions.Africa.Africa*             0.451
		Geography.Regions.Africa.Central Africa      0.235
		Geography.Regions.Africa.Eastern Africa      0.479
		Geography.Regions.Africa.Northern Africa     0.252
		Geography.Regions.Africa.Southern Africa     0.419
		Geography.Regions.Africa.Western Africa      0.301
		Geography.Regions.Americas.Central America   0.6
		Geography.Regions.Americas.North America     0.741
		Geography.Regions.Americas.South America     0.753
		Geography.Regions.Asia.Asia*                 0.611
		Geography.Regions.Asia.Central Asia          0.195
		Geography.Regions.Asia.East Asia             0.686
		Geography.Regions.Asia.North Asia            0.28
		Geography.Regions.Asia.South Asia            0.875
		Geography.Regions.Asia.Southeast Asia        0.749
		Geography.Regions.Asia.West Asia             0.715
		Geography.Regions.Europe.Eastern Europe      0.493
		Geography.Regions.Europe.Europe*             0.546
		Geography.Regions.Europe.Northern Europe     0.732
		Geography.Regions.Europe.Southern Europe     0.584
		Geography.Regions.Europe.Western Europe      0.645
		Geography.Regions.Oceania                    0.828
		History and Society.Business and economics   0.376
		History and Society.Education                0.59
		History and Society.History                  0.296
		History and Society.Military and warfare     0.497
		History and Society.Politics and government  0.629
		History and Society.Society                  0.296
		History and Society.Transportation           0.808
		STEM.Biology                                 0.864
		STEM.Chemistry                               0.243
		STEM.Computing                               0.219
		STEM.Earth and environment                   0.415
		STEM.Engineering                             0.531
		STEM.Libraries & Information                 0.22
		STEM.Mathematics                             0.167
		STEM.Medicine & Health                       0.576
		STEM.Physics                                 0.144
		STEM.STEM*                                   0.656
		STEM.Space                                   0.764
		STEM.Technology                              0.198
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.982
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.99
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.972
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.979
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.984
		History and Society.Society                  0.993
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.683, macro=0.558):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.852
		Culture.Biography.Women                      0.65
		Culture.Food and drink                       0.531
		Culture.Internet culture                     0.518
		Culture.Linguistics                          0.667
		Culture.Literature                           0.6
		Culture.Media.Books                          0.61
		Culture.Media.Entertainment                  0.288
		Culture.Media.Films                          0.802
		Culture.Media.Media*                         0.706
		Culture.Media.Music                          0.79
		Culture.Media.Radio                          0.442
		Culture.Media.Software                       0.199
		Culture.Media.Television                     0.716
		Culture.Media.Video games                    0.752
		Culture.Performing arts                      0.439
		Culture.Philosophy and religion              0.438
		Culture.Sports                               0.901
		Culture.Visual arts.Architecture             0.621
		Culture.Visual arts.Comics and Anime         0.654
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.624
		Geography.Geographical                       0.606
		Geography.Regions.Africa.Africa*             0.546
		Geography.Regions.Africa.Central Africa      0.348
		Geography.Regions.Africa.Eastern Africa      0.58
		Geography.Regions.Africa.Northern Africa     0.35
		Geography.Regions.Africa.Southern Africa     0.474
		Geography.Regions.Africa.Western Africa      0.39
		Geography.Regions.Americas.Central America   0.561
		Geography.Regions.Americas.North America     0.644
		Geography.Regions.Americas.South America     0.687
		Geography.Regions.Asia.Asia*                 0.678
		Geography.Regions.Asia.Central Asia          0.296
		Geography.Regions.Asia.East Asia             0.696
		Geography.Regions.Asia.North Asia            0.388
		Geography.Regions.Asia.South Asia            0.771
		Geography.Regions.Asia.Southeast Asia        0.67
		Geography.Regions.Asia.West Asia             0.692
		Geography.Regions.Europe.Eastern Europe      0.582
		Geography.Regions.Europe.Europe*             0.637
		Geography.Regions.Europe.Northern Europe     0.635
		Geography.Regions.Europe.Southern Europe     0.616
		Geography.Regions.Europe.Western Europe      0.664
		Geography.Regions.Oceania                    0.714
		History and Society.Business and economics   0.438
		History and Society.Education                0.523
		History and Society.History                  0.367
		History and Society.Military and warfare     0.542
		History and Society.Politics and government  0.529
		History and Society.Society                  0.237
		History and Society.Transportation           0.821
		STEM.Biology                                 0.825
		STEM.Chemistry                               0.35
		STEM.Computing                               0.338
		STEM.Earth and environment                   0.465
		STEM.Engineering                             0.612
		STEM.Libraries & Information                 0.326
		STEM.Mathematics                             0.269
		STEM.Medicine & Health                       0.564
		STEM.Physics                                 0.23
		STEM.STEM*                                   0.746
		STEM.Space                                   0.805
		STEM.Technology                              0.302
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.961
		Geography.Regions.Europe.Northern Europe     0.99
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.988
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.979
		STEM.Space                                   0.999
		STEM.Technology                              0.992
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.986
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.993
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.962
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.986
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.962
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.989
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.981
		Geography.Regions.Europe.Europe*             0.93
		Geography.Regions.Europe.Northern Europe     0.981
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.985
		History and Society.Politics and government  0.977
		History and Society.Society                  0.99
		History and Society.Transportation           0.994
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.985
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.024
		Culture.Biography.Women                      0.007
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.003
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.007
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.011
		Geography.Regions.Africa.Africa*             0.007
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.013
		Geography.Regions.Americas.South America     0.001
		Geography.Regions.Asia.Asia*                 0.027
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.003
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.006
		Geography.Regions.Europe.Southern Europe     0.006
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.003
		History and Society.History                  0.013
		History and Society.Military and warfare     0.009
		History and Society.Politics and government  0.008
		History and Society.Society                  0.004
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.004
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.013
		-------------------------------------------  -----
	roc_auc (micro=0.963, macro=0.965):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.971
		Culture.Internet culture                     0.98
		Culture.Linguistics                          0.968
		Culture.Literature                           0.971
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.955
		Culture.Media.Films                          0.981
		Culture.Media.Media*                         0.973
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.949
		Culture.Media.Software                       0.981
		Culture.Media.Television                     0.977
		Culture.Media.Video games                    0.984
		Culture.Performing arts                      0.963
		Culture.Philosophy and religion              0.935
		Culture.Sports                               0.977
		Culture.Visual arts.Architecture             0.971
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.972
		Culture.Visual arts.Visual arts*             0.959
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.963
		Geography.Regions.Africa.Central Africa      0.975
		Geography.Regions.Africa.Eastern Africa      0.972
		Geography.Regions.Africa.Northern Africa     0.965
		Geography.Regions.Africa.Southern Africa     0.95
		Geography.Regions.Africa.Western Africa      0.958
		Geography.Regions.Americas.Central America   0.961
		Geography.Regions.Americas.North America     0.951
		Geography.Regions.Americas.South America     0.962
		Geography.Regions.Asia.Asia*                 0.955
		Geography.Regions.Asia.Central Asia          0.971
		Geography.Regions.Asia.East Asia             0.97
		Geography.Regions.Asia.North Asia            0.959
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.964
		Geography.Regions.Asia.West Asia             0.968
		Geography.Regions.Europe.Eastern Europe      0.962
		Geography.Regions.Europe.Europe*             0.942
		Geography.Regions.Europe.Northern Europe     0.955
		Geography.Regions.Europe.Southern Europe     0.967
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.951
		History and Society.Education                0.959
		History and Society.History                  0.938
		History and Society.Military and warfare     0.953
		History and Society.Politics and government  0.933
		History and Society.Society                  0.868
		History and Society.Transportation           0.98
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.981
		STEM.Computing                               0.981
		STEM.Earth and environment                   0.958
		STEM.Engineering                             0.973
		STEM.Libraries & Information                 0.967
		STEM.Mathematics                             0.975
		STEM.Medicine & Health                       0.959
		STEM.Physics                                 0.975
		STEM.STEM*                                   0.97
		STEM.Space                                   0.984
		STEM.Technology                              0.964
		-------------------------------------------  -----
	pr_auc (micro=0.725, macro=0.556):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.915
		Culture.Biography.Women                      0.626
		Culture.Food and drink                       0.514
		Culture.Internet culture                     0.6
		Culture.Linguistics                          0.637
		Culture.Literature                           0.656
		Culture.Media.Books                          0.625
		Culture.Media.Entertainment                  0.224
		Culture.Media.Films                          0.858
		Culture.Media.Media*                         0.822
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.252
		Culture.Media.Software                       0.188
		Culture.Media.Television                     0.732
		Culture.Media.Video games                    0.84
		Culture.Performing arts                      0.34
		Culture.Philosophy and religion              0.375
		Culture.Sports                               0.933
		Culture.Visual arts.Architecture             0.605
		Culture.Visual arts.Comics and Anime         0.666
		Culture.Visual arts.Fashion                  0.339
		Culture.Visual arts.Visual arts*             0.659
		Geography.Geographical                       0.638
		Geography.Regions.Africa.Africa*             0.556
		Geography.Regions.Africa.Central Africa      0.326
		Geography.Regions.Africa.Eastern Africa      0.469
		Geography.Regions.Africa.Northern Africa     0.265
		Geography.Regions.Africa.Southern Africa     0.373
		Geography.Regions.Africa.Western Africa      0.295
		Geography.Regions.Americas.Central America   0.526
		Geography.Regions.Americas.North America     0.701
		Geography.Regions.Americas.South America     0.666
		Geography.Regions.Asia.Asia*                 0.757
		Geography.Regions.Asia.Central Asia          0.243
		Geography.Regions.Asia.East Asia             0.722
		Geography.Regions.Asia.North Asia            0.369
		Geography.Regions.Asia.South Asia            0.807
		Geography.Regions.Asia.Southeast Asia        0.659
		Geography.Regions.Asia.West Asia             0.704
		Geography.Regions.Europe.Eastern Europe      0.611
		Geography.Regions.Europe.Europe*             0.722
		Geography.Regions.Europe.Northern Europe     0.682
		Geography.Regions.Europe.Southern Europe     0.653
		Geography.Regions.Europe.Western Europe      0.708
		Geography.Regions.Oceania                    0.757
		History and Society.Business and economics   0.385
		History and Society.Education                0.515
		History and Society.History                  0.311
		History and Society.Military and warfare     0.529
		History and Society.Politics and government  0.547
		History and Society.Society                  0.183
		History and Society.Transportation           0.859
		STEM.Biology                                 0.833
		STEM.Chemistry                               0.336
		STEM.Computing                               0.326
		STEM.Earth and environment                   0.368
		STEM.Engineering                             0.62
		STEM.Libraries & Information                 0.235
		STEM.Mathematics                             0.381
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.148
		STEM.STEM*                                   0.844
		STEM.Space                                   0.844
		STEM.Technology                              0.314
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'STEM.Engineering': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}}}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'type': 'array', 'items': {'type': 'string'}}}, 'title': 'Scikit learn-based classifier score with probability'}

