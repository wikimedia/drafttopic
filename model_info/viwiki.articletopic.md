Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'verbose': 0, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'tol': 0.0001, 'min_weight_fraction_leaf': 0.0, 'init': None, 'subsample': 1.0, 'validation_fraction': 0.1, 'learning_rate': 0.1, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'min_impurity_decrease': 0.0, 'multilabel': True, 'scale': False, 'warm_start': False, 'min_samples_leaf': 1, 'max_depth': 5, 'min_samples_split': 2, 'random_state': None, 'label_weights': {}, 'n_iter_no_change': None, 'center': False, 'population_rates': None, 'loss': 'deviance', 'presort': 'auto', 'max_features': 'log2', 'n_estimators': 150, 'max_leaf_nodes': None}
	Environment:
	 - revscoring_version: '2.6.9'
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
	counts (n=60632):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 14535  -->  13092  1443   656  45441
			'Culture.Biography.Women'                       5097  -->   4149   948   786  54749
			'Culture.Food and drink'                        1403  -->    986   417   151  59078
			'Culture.Internet culture'                      3508  -->   2798   710   261  56863
			'Culture.Linguistics'                           1515  -->   1132   383   101  59016
			'Culture.Literature'                            5452  -->   4196  1256   513  54667
			'Culture.Media.Books'                           1430  -->    994   436   117  59085
			'Culture.Media.Entertainment'                   1921  -->    858  1063   172  58539
			'Culture.Media.Films'                           2613  -->   2060   553   136  57883
			'Culture.Media.Media*'                         13172  -->  11315  1857  1445  46015
			'Culture.Media.Music'                           2809  -->   2364   445   214  57609
			'Culture.Media.Radio'                            299  -->    181   118    40  60293
			'Culture.Media.Software'                        2263  -->   1733   530   342  58027
			'Culture.Media.Television'                      2013  -->   1427   586   139  58480
			'Culture.Media.Video games'                     2159  -->   1954   205    70  58403
			'Culture.Performing arts'                       1395  -->    906   489   140  59097
			'Culture.Philosophy and religion'               3023  -->   1618  1405   299  57310
			'Culture.Sports'                                4112  -->   3634   478   135  56385
			'Culture.Visual arts.Architecture'              1846  -->   1344   502   193  58593
			'Culture.Visual arts.Comics and Anime'          2178  -->   1867   311   118  58336
			'Culture.Visual arts.Fashion'                   1522  -->   1239   283   103  59007
			'Culture.Visual arts.Visual arts*'              6069  -->   4626  1443   480  54083
			'Geography.Geographical'                        3918  -->   2566  1352   565  56149
			'Geography.Regions.Africa.Africa*'              5703  -->   2500  3203   642  54287
			'Geography.Regions.Africa.Central Africa'       1199  -->    327   872   160  59273
			'Geography.Regions.Africa.Eastern Africa'        430  -->    120   310    45  60157
			'Geography.Regions.Africa.Northern Africa'      1463  -->    617   846    92  59077
			'Geography.Regions.Africa.Southern Africa'      1185  -->    486   699    79  59368
			'Geography.Regions.Africa.Western Africa'        668  -->    279   389    71  59893
			'Geography.Regions.Americas.Central America'    1602  -->    206  1396    80  58950
			'Geography.Regions.Americas.North America'      5411  -->   2143  3268   304  54917
			'Geography.Regions.Americas.South America'      2189  -->    821  1368   156  58287
			'Geography.Regions.Asia.Asia*'                 14800  -->   8629  6171  1702  44130
			'Geography.Regions.Asia.Central Asia'           1067  -->    317   750   104  59461
			'Geography.Regions.Asia.East Asia'              5768  -->   2924  2844   433  54431
			'Geography.Regions.Asia.North Asia'             2584  -->   1016  1568   124  57924
			'Geography.Regions.Asia.South Asia'             1974  -->    874  1100    81  58577
			'Geography.Regions.Asia.Southeast Asia'         2650  -->    478  2172    79  57903
			'Geography.Regions.Asia.West Asia'              2118  -->   1096  1022   123  58391
			'Geography.Regions.Europe.Eastern Europe'       4297  -->   1931  2366   188  56147
			'Geography.Regions.Europe.Europe*'             13313  -->   7670  5643  1418  45901
			'Geography.Regions.Europe.Northern Europe'      2836  -->    547  2289   164  57632
			'Geography.Regions.Europe.Southern Europe'      2747  -->   1293  1454   121  57764
			'Geography.Regions.Europe.Western Europe'       4036  -->   1854  2182    94  56502
			'Geography.Regions.Oceania'                     1707  -->    469  1238   189  58736
			'History and Society.Business and economics'    3323  -->   2040  1283   442  56867
			'History and Society.Education'                 1628  -->    934   694   128  58876
			'History and Society.History'                   4370  -->   2141  2229   716  55546
			'History and Society.Military and warfare'      4308  -->   3106  1202   413  55911
			'History and Society.Politics and government'   3218  -->   1658  1560   516  56898
			'History and Society.Society'                   4444  -->   1350  3094   286  55902
			'History and Society.Transportation'            3519  -->   3226   293    93  57020
			'STEM.Biology'                                  6763  -->   6186   577   169  53700
			'STEM.Chemistry'                                1434  -->   1094   340   200  58998
			'STEM.Computing'                                2437  -->   1931   506   346  57849
			'STEM.Earth and environment'                    1712  -->   1129   583   147  58773
			'STEM.Engineering'                              2978  -->   2457   521   138  57516
			'STEM.Libraries & Information'                   493  -->    377   116    58  60081
			'STEM.Mathematics'                               915  -->    715   200    53  59664
			'STEM.Medicine & Health'                        1804  -->   1290   514   145  58683
			'STEM.Physics'                                  1387  -->   1013   374   191  59054
			'STEM.STEM*'                                   20148  -->  18415  1733   988  39496
			'STEM.Space'                                    1563  -->   1427   136    49  59020
			'STEM.Technology'                               4193  -->   3048  1145   641  55798
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.24          0.121
		Culture.Biography.Women                         0.084         0.015
		Culture.Food and drink                          0.023         0.003
		Culture.Internet culture                        0.058         0.004
		Culture.Linguistics                             0.025         0.008
		Culture.Literature                              0.09          0.015
		Culture.Media.Books                             0.024         0.004
		Culture.Media.Entertainment                     0.032         0.004
		Culture.Media.Films                             0.043         0.012
		Culture.Media.Media*                            0.217         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.037         0.001
		Culture.Media.Television                        0.033         0.009
		Culture.Media.Video games                       0.036         0.003
		Culture.Performing arts                         0.023         0.003
		Culture.Philosophy and religion                 0.05          0.01
		Culture.Sports                                  0.068         0.061
		Culture.Visual arts.Architecture                0.03          0.011
		Culture.Visual arts.Comics and Anime            0.036         0.002
		Culture.Visual arts.Fashion                     0.025         0.001
		Culture.Visual arts.Visual arts*                0.1           0.018
		Geography.Geographical                          0.065         0.021
		Geography.Regions.Africa.Africa*                0.094         0.009
		Geography.Regions.Africa.Central Africa         0.02          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.024         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.026         0.003
		Geography.Regions.Americas.North America        0.089         0.064
		Geography.Regions.Americas.South America        0.036         0.007
		Geography.Regions.Asia.Asia*                    0.244         0.053
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.095         0.012
		Geography.Regions.Asia.North Asia               0.043         0.006
		Geography.Regions.Asia.South Asia               0.033         0.017
		Geography.Regions.Asia.Southeast Asia           0.044         0.006
		Geography.Regions.Asia.West Asia                0.035         0.012
		Geography.Regions.Europe.Eastern Europe         0.071         0.018
		Geography.Regions.Europe.Europe*                0.22          0.082
		Geography.Regions.Europe.Northern Europe        0.047         0.029
		Geography.Regions.Europe.Southern Europe        0.045         0.014
		Geography.Regions.Europe.Western Europe         0.067         0.021
		Geography.Regions.Oceania                       0.028         0.017
		History and Society.Business and economics      0.055         0.01
		History and Society.Education                   0.027         0.008
		History and Society.History                     0.072         0.011
		History and Society.Military and warfare        0.071         0.015
		History and Society.Politics and government     0.053         0.016
		History and Society.Society                     0.073         0.008
		History and Society.Transportation              0.058         0.016
		STEM.Biology                                    0.112         0.035
		STEM.Chemistry                                  0.024         0.002
		STEM.Computing                                  0.04          0.003
		STEM.Earth and environment                      0.028         0.005
		STEM.Engineering                                0.049         0.006
		STEM.Libraries & Information                    0.008         0.001
		STEM.Mathematics                                0.015         0
		STEM.Medicine & Health                          0.03          0.006
		STEM.Physics                                    0.023         0.001
		STEM.STEM*                                      0.332         0.066
		STEM.Space                                      0.026         0.004
		STEM.Technology                                 0.069         0.005
	match_rate (micro=0.046, macro=0.016):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.026
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.008
		Culture.Linguistics                          0.008
		Culture.Literature                           0.021
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.056
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.023
		Geography.Geographical                       0.024
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.03
		Geography.Regions.Americas.South America     0.005
		Geography.Regions.Asia.Asia*                 0.066
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.014
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.009
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.008
		Geography.Regions.Europe.Eastern Europe      0.012
		Geography.Regions.Europe.Europe*             0.075
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.011
		Geography.Regions.Oceania                    0.008
		History and Society.Business and economics   0.014
		History and Society.Education                0.007
		History and Society.History                  0.018
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.017
		History and Society.Society                  0.008
		History and Society.Transportation           0.017
		STEM.Biology                                 0.035
		STEM.Chemistry                               0.005
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.083
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.954, macro=0.984):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.992
		Culture.Linguistics                          0.992
		Culture.Literature                           0.979
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.944
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.977
		Geography.Geographical                       0.976
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.97
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.934
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.925
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.986
		History and Society.Education                0.993
		History and Society.History                  0.982
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.983
		History and Society.Society                  0.992
		History and Society.Transportation           0.983
		STEM.Biology                                 0.965
		STEM.Chemistry                               0.995
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.917
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.675, macro=0.615):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.901
		Culture.Biography.Women                      0.814
		Culture.Food and drink                       0.703
		Culture.Internet culture                     0.798
		Culture.Linguistics                          0.747
		Culture.Literature                           0.77
		Culture.Media.Books                          0.695
		Culture.Media.Entertainment                  0.447
		Culture.Media.Films                          0.788
		Culture.Media.Media*                         0.859
		Culture.Media.Music                          0.842
		Culture.Media.Radio                          0.605
		Culture.Media.Software                       0.766
		Culture.Media.Television                     0.709
		Culture.Media.Video games                    0.905
		Culture.Performing arts                      0.649
		Culture.Philosophy and religion              0.535
		Culture.Sports                               0.884
		Culture.Visual arts.Architecture             0.728
		Culture.Visual arts.Comics and Anime         0.857
		Culture.Visual arts.Fashion                  0.814
		Culture.Visual arts.Visual arts*             0.762
		Geography.Geographical                       0.655
		Geography.Regions.Africa.Africa*             0.438
		Geography.Regions.Africa.Central Africa      0.273
		Geography.Regions.Africa.Eastern Africa      0.279
		Geography.Regions.Africa.Northern Africa     0.422
		Geography.Regions.Africa.Southern Africa     0.41
		Geography.Regions.Africa.Western Africa      0.418
		Geography.Regions.Americas.Central America   0.129
		Geography.Regions.Americas.North America     0.396
		Geography.Regions.Americas.South America     0.375
		Geography.Regions.Asia.Asia*                 0.583
		Geography.Regions.Asia.Central Asia          0.297
		Geography.Regions.Asia.East Asia             0.507
		Geography.Regions.Asia.North Asia            0.393
		Geography.Regions.Asia.South Asia            0.443
		Geography.Regions.Asia.Southeast Asia        0.18
		Geography.Regions.Asia.West Asia             0.517
		Geography.Regions.Europe.Eastern Europe      0.449
		Geography.Regions.Europe.Europe*             0.576
		Geography.Regions.Europe.Northern Europe     0.193
		Geography.Regions.Europe.Southern Europe     0.471
		Geography.Regions.Europe.Western Europe      0.459
		Geography.Regions.Oceania                    0.275
		History and Society.Business and economics   0.614
		History and Society.Education                0.574
		History and Society.History                  0.49
		History and Society.Military and warfare     0.721
		History and Society.Politics and government  0.515
		History and Society.Society                  0.304
		History and Society.Transportation           0.917
		STEM.Biology                                 0.915
		STEM.Chemistry                               0.763
		STEM.Computing                               0.792
		STEM.Earth and environment                   0.659
		STEM.Engineering                             0.825
		STEM.Libraries & Information                 0.765
		STEM.Mathematics                             0.781
		STEM.Medicine & Health                       0.715
		STEM.Physics                                 0.73
		STEM.STEM*                                   0.914
		STEM.Space                                   0.913
		STEM.Technology                              0.727
		-------------------------------------------  -----
	!recall (micro=0.988, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.998
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.994
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.963
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.997
		Geography.Regions.Europe.Southern Europe     0.998
		Geography.Regions.Europe.Western Europe      0.998
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.998
		History and Society.History                  0.987
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.694, macro=0.532):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.897
		Culture.Biography.Women                      0.469
		Culture.Food and drink                       0.416
		Culture.Internet culture                     0.398
		Culture.Linguistics                          0.781
		Culture.Literature                           0.558
		Culture.Media.Books                          0.606
		Culture.Media.Entertainment                  0.379
		Culture.Media.Films                          0.799
		Culture.Media.Media*                         0.623
		Culture.Media.Music                          0.831
		Culture.Media.Radio                          0.682
		Culture.Media.Software                       0.147
		Culture.Media.Television                     0.73
		Culture.Media.Video games                    0.69
		Culture.Performing arts                      0.459
		Culture.Philosophy and religion              0.522
		Culture.Sports                               0.96
		Culture.Visual arts.Architecture             0.71
		Culture.Visual arts.Comics and Anime         0.507
		Culture.Visual arts.Fashion                  0.297
		Culture.Visual arts.Visual arts*             0.617
		Geography.Geographical                       0.589
		Geography.Regions.Africa.Africa*             0.245
		Geography.Regions.Africa.Central Africa      0.067
		Geography.Regions.Africa.Eastern Africa      0.159
		Geography.Regions.Africa.Northern Africa     0.27
		Geography.Regions.Africa.Southern Africa     0.29
		Geography.Regions.Africa.Western Africa      0.21
		Geography.Regions.Americas.Central America   0.249
		Geography.Regions.Americas.North America     0.83
		Geography.Regions.Americas.South America     0.495
		Geography.Regions.Asia.Asia*                 0.468
		Geography.Regions.Asia.Central Asia          0.12
		Geography.Regions.Asia.East Asia             0.444
		Geography.Regions.Asia.North Asia            0.512
		Geography.Regions.Asia.South Asia            0.845
		Geography.Regions.Asia.Southeast Asia        0.456
		Geography.Regions.Asia.West Asia             0.746
		Geography.Regions.Europe.Eastern Europe      0.717
		Geography.Regions.Europe.Europe*             0.631
		Geography.Regions.Europe.Northern Europe     0.672
		Geography.Regions.Europe.Southern Europe     0.761
		Geography.Regions.Europe.Western Europe      0.854
		Geography.Regions.Oceania                    0.591
		History and Society.Business and economics   0.441
		History and Society.Education                0.681
		History and Society.History                  0.3
		History and Society.Military and warfare     0.607
		History and Society.Politics and government  0.49
		History and Society.Society                  0.334
		History and Society.Transportation           0.904
		STEM.Biology                                 0.913
		STEM.Chemistry                               0.279
		STEM.Computing                               0.276
		STEM.Earth and environment                   0.559
		STEM.Engineering                             0.668
		STEM.Libraries & Information                 0.354
		STEM.Mathematics                             0.291
		STEM.Medicine & Health                       0.655
		STEM.Physics                                 0.177
		STEM.STEM*                                   0.725
		STEM.Space                                   0.826
		STEM.Technology                              0.25
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.997
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.997
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.996
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.96
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.976
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.994
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.991
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.989
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.996
		History and Society.Education                0.997
		History and Society.History                  0.994
		History and Society.Military and warfare     0.996
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.999
		STEM.Biology                                 0.997
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.994
		STEM.Space                                   1
		STEM.Technology                              0.999
		-------------------------------------------  -----
	f1 (micro=0.664, macro=0.539):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.899
		Culture.Biography.Women                      0.595
		Culture.Food and drink                       0.522
		Culture.Internet culture                     0.531
		Culture.Linguistics                          0.764
		Culture.Literature                           0.647
		Culture.Media.Books                          0.648
		Culture.Media.Entertainment                  0.41
		Culture.Media.Films                          0.793
		Culture.Media.Media*                         0.722
		Culture.Media.Music                          0.836
		Culture.Media.Radio                          0.642
		Culture.Media.Software                       0.247
		Culture.Media.Television                     0.719
		Culture.Media.Video games                    0.783
		Culture.Performing arts                      0.538
		Culture.Philosophy and religion              0.528
		Culture.Sports                               0.92
		Culture.Visual arts.Architecture             0.719
		Culture.Visual arts.Comics and Anime         0.637
		Culture.Visual arts.Fashion                  0.436
		Culture.Visual arts.Visual arts*             0.682
		Geography.Geographical                       0.62
		Geography.Regions.Africa.Africa*             0.314
		Geography.Regions.Africa.Central Africa      0.108
		Geography.Regions.Africa.Eastern Africa      0.203
		Geography.Regions.Africa.Northern Africa     0.329
		Geography.Regions.Africa.Southern Africa     0.34
		Geography.Regions.Africa.Western Africa      0.279
		Geography.Regions.Americas.Central America   0.17
		Geography.Regions.Americas.North America     0.536
		Geography.Regions.Americas.South America     0.427
		Geography.Regions.Asia.Asia*                 0.519
		Geography.Regions.Asia.Central Asia          0.171
		Geography.Regions.Asia.East Asia             0.473
		Geography.Regions.Asia.North Asia            0.445
		Geography.Regions.Asia.South Asia            0.581
		Geography.Regions.Asia.Southeast Asia        0.259
		Geography.Regions.Asia.West Asia             0.611
		Geography.Regions.Europe.Eastern Europe      0.552
		Geography.Regions.Europe.Europe*             0.602
		Geography.Regions.Europe.Northern Europe     0.3
		Geography.Regions.Europe.Southern Europe     0.582
		Geography.Regions.Europe.Western Europe      0.597
		Geography.Regions.Oceania                    0.375
		History and Society.Business and economics   0.513
		History and Society.Education                0.623
		History and Society.History                  0.372
		History and Society.Military and warfare     0.659
		History and Society.Politics and government  0.502
		History and Society.Society                  0.318
		History and Society.Transportation           0.91
		STEM.Biology                                 0.914
		STEM.Chemistry                               0.408
		STEM.Computing                               0.409
		STEM.Earth and environment                   0.605
		STEM.Engineering                             0.738
		STEM.Libraries & Information                 0.484
		STEM.Mathematics                             0.424
		STEM.Medicine & Health                       0.684
		STEM.Physics                                 0.284
		STEM.STEM*                                   0.808
		STEM.Space                                   0.867
		STEM.Technology                              0.373
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.98
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.995
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.991
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.966
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.994
		History and Society.Education                0.997
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.985
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.989):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.995
		Culture.Media.Media*                         0.963
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.995
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.983
		Geography.Regions.Africa.Africa*             0.984
		Geography.Regions.Africa.Central Africa      0.997
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.943
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.986
		Geography.Regions.Asia.North Asia            0.994
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.993
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.938
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.985
		History and Society.Business and economics   0.989
		History and Society.Education                0.994
		History and Society.History                  0.982
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.983
		History and Society.Society                  0.989
		History and Society.Transportation           0.997
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.996
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.012, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.014
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.005
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.002
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.009
		Geography.Geographical                       0.01
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.006
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.037
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.008
		Geography.Regions.Asia.North Asia            0.002
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.003
		Geography.Regions.Europe.Europe*             0.03
		Geography.Regions.Europe.Northern Europe     0.003
		Geography.Regions.Europe.Southern Europe     0.002
		Geography.Regions.Europe.Western Europe      0.002
		Geography.Regions.Oceania                    0.003
		History and Society.Business and economics   0.008
		History and Society.Education                0.002
		History and Society.History                  0.013
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.002
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.002
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.024
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.957, macro=0.961):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.982
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.971
		Culture.Literature                           0.978
		Culture.Media.Books                          0.984
		Culture.Media.Entertainment                  0.971
		Culture.Media.Films                          0.981
		Culture.Media.Media*                         0.978
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.939
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.955
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.978
		Culture.Visual arts.Comics and Anime         0.988
		Culture.Visual arts.Fashion                  0.986
		Culture.Visual arts.Visual arts*             0.972
		Geography.Geographical                       0.968
		Geography.Regions.Africa.Africa*             0.937
		Geography.Regions.Africa.Central Africa      0.954
		Geography.Regions.Africa.Eastern Africa      0.909
		Geography.Regions.Africa.Northern Africa     0.943
		Geography.Regions.Africa.Southern Africa     0.953
		Geography.Regions.Africa.Western Africa      0.963
		Geography.Regions.Americas.Central America   0.913
		Geography.Regions.Americas.North America     0.923
		Geography.Regions.Americas.South America     0.942
		Geography.Regions.Asia.Asia*                 0.91
		Geography.Regions.Asia.Central Asia          0.944
		Geography.Regions.Asia.East Asia             0.946
		Geography.Regions.Asia.North Asia            0.935
		Geography.Regions.Asia.South Asia            0.929
		Geography.Regions.Asia.Southeast Asia        0.909
		Geography.Regions.Asia.West Asia             0.946
		Geography.Regions.Europe.Eastern Europe      0.932
		Geography.Regions.Europe.Europe*             0.922
		Geography.Regions.Europe.Northern Europe     0.915
		Geography.Regions.Europe.Southern Europe     0.934
		Geography.Regions.Europe.Western Europe      0.945
		Geography.Regions.Oceania                    0.912
		History and Society.Business and economics   0.968
		History and Society.Education                0.973
		History and Society.History                  0.948
		History and Society.Military and warfare     0.974
		History and Society.Politics and government  0.957
		History and Society.Society                  0.905
		History and Society.Transportation           0.988
		STEM.Biology                                 0.985
		STEM.Chemistry                               0.988
		STEM.Computing                               0.987
		STEM.Earth and environment                   0.974
		STEM.Engineering                             0.985
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.987
		STEM.Medicine & Health                       0.976
		STEM.Physics                                 0.987
		STEM.STEM*                                   0.98
		STEM.Space                                   0.989
		STEM.Technology                              0.975
		-------------------------------------------  -----
	pr_auc (micro=0.703, macro=0.534):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.941
		Culture.Biography.Women                      0.592
		Culture.Food and drink                       0.473
		Culture.Internet culture                     0.686
		Culture.Linguistics                          0.758
		Culture.Literature                           0.724
		Culture.Media.Books                          0.67
		Culture.Media.Entertainment                  0.365
		Culture.Media.Films                          0.833
		Culture.Media.Media*                         0.817
		Culture.Media.Music                          0.849
		Culture.Media.Radio                          0.459
		Culture.Media.Software                       0.231
		Culture.Media.Television                     0.728
		Culture.Media.Video games                    0.848
		Culture.Performing arts                      0.434
		Culture.Philosophy and religion              0.477
		Culture.Sports                               0.942
		Culture.Visual arts.Architecture             0.714
		Culture.Visual arts.Comics and Anime         0.81
		Culture.Visual arts.Fashion                  0.485
		Culture.Visual arts.Visual arts*             0.733
		Geography.Geographical                       0.64
		Geography.Regions.Africa.Africa*             0.29
		Geography.Regions.Africa.Central Africa      0.04
		Geography.Regions.Africa.Eastern Africa      0.049
		Geography.Regions.Africa.Northern Africa     0.148
		Geography.Regions.Africa.Southern Africa     0.166
		Geography.Regions.Africa.Western Africa      0.132
		Geography.Regions.Americas.Central America   0.092
		Geography.Regions.Americas.North America     0.648
		Geography.Regions.Americas.South America     0.364
		Geography.Regions.Asia.Asia*                 0.569
		Geography.Regions.Asia.Central Asia          0.064
		Geography.Regions.Asia.East Asia             0.43
		Geography.Regions.Asia.North Asia            0.396
		Geography.Regions.Asia.South Asia            0.579
		Geography.Regions.Asia.Southeast Asia        0.219
		Geography.Regions.Asia.West Asia             0.563
		Geography.Regions.Europe.Eastern Europe      0.56
		Geography.Regions.Europe.Europe*             0.685
		Geography.Regions.Europe.Northern Europe     0.408
		Geography.Regions.Europe.Southern Europe     0.57
		Geography.Regions.Europe.Western Europe      0.632
		Geography.Regions.Oceania                    0.348
		History and Society.Business and economics   0.506
		History and Society.Education                0.598
		History and Society.History                  0.333
		History and Society.Military and warfare     0.716
		History and Society.Politics and government  0.462
		History and Society.Society                  0.245
		History and Society.Transportation           0.938
		STEM.Biology                                 0.91
		STEM.Chemistry                               0.444
		STEM.Computing                               0.426
		STEM.Earth and environment                   0.596
		STEM.Engineering                             0.81
		STEM.Libraries & Information                 0.387
		STEM.Mathematics                             0.461
		STEM.Medicine & Health                       0.721
		STEM.Physics                                 0.219
		STEM.STEM*                                   0.922
		STEM.Space                                   0.919
		STEM.Technology                              0.387
		-------------------------------------------  -----
	
	 - score_schema: {'properties': {'probability': {'properties': {'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'items': {'type': 'string'}, 'type': 'array', 'description': 'The most likely labels predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

