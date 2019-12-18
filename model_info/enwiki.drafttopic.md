Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'n_iter_no_change': None, 'max_features': 'log2', 'tol': 0.0001, 'warm_start': False, 'subsample': 1.0, 'multilabel': True, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'presort': 'auto', 'min_samples_split': 2, 'max_depth': 5, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'learning_rate': 0.1, 'init': None, 'random_state': None, 'validation_fraction': 0.1, 'label_weights': {}, 'scale': False, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'verbose': 0, 'loss': 'deviance', 'n_estimators': 150, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'center': False, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.6.2'
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
	counts (n=60052):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16350  -->  12360  3990  1976  41726
			'Culture.Biography.Women'                       4056  -->   1128  2928   503  55493
			'Culture.Food and drink'                        1245  -->    791   454   108  58699
			'Culture.Internet culture'                      2681  -->   1731   950   216  57155
			'Culture.Linguistics'                           1210  -->    656   554   107  58735
			'Culture.Literature'                            4977  -->   2965  2012   639  54436
			'Culture.Media.Books'                           1810  -->    926   884   225  58017
			'Culture.Media.Entertainment'                   1737  -->    339  1398   109  58206
			'Culture.Media.Films'                           2225  -->   1509   716   200  57627
			'Culture.Media.Media*'                         13453  -->  10329  3124  1977  44622
			'Culture.Media.Music'                           2532  -->   1822   710   298  57222
			'Culture.Media.Radio'                           1116  -->    825   291    55  58881
			'Culture.Media.Software'                        1667  -->    789   878   340  58045
			'Culture.Media.Television'                      2008  -->   1047   961   254  57790
			'Culture.Media.Video games'                     1881  -->   1457   424    64  58107
			'Culture.Performing arts'                       1273  -->    623   650   116  58663
			'Culture.Philosophy and religion'               2505  -->   1129  1376   337  57210
			'Culture.Sports'                                5720  -->   4947   773   365  53967
			'Culture.Visual arts.Architecture'              2468  -->   1518   950   266  57318
			'Culture.Visual arts.Comics and Anime'          1384  -->    751   633   122  58546
			'Culture.Visual arts.Fashion'                   1118  -->    662   456    82  58852
			'Culture.Visual arts.Visual arts*'              5691  -->   3139  2552   538  53823
			'Geography.Geographical'                        3224  -->   1809  1415   274  56554
			'Geography.Regions.Africa.Africa*'              5529  -->   3845  1684   266  54257
			'Geography.Regions.Africa.Central Africa'         27  -->      6    21  7355  52670
			'Geography.Regions.Africa.Eastern Africa'       1079  -->    603   476    63  58910
			'Geography.Regions.Africa.Northern Africa'      1228  -->    607   621   108  58716
			'Geography.Regions.Africa.Southern Africa'      1244  -->    743   501    64  58744
			'Geography.Regions.Africa.Western Africa'       1131  -->    765   366    54  58867
			'Geography.Regions.Americas.Central America'    1282  -->    416   866   102  58668
			'Geography.Regions.Americas.North America'      7247  -->   3885  3362   947  51858
			'Geography.Regions.Americas.South America'      1480  -->    702   778   176  58396
			'Geography.Regions.Asia.Asia*'                 10642  -->   7347  3295   978  48432
			'Geography.Regions.Asia.Central Asia'           1125  -->    536   589    56  58871
			'Geography.Regions.Asia.East Asia'              2594  -->   1381  1213   285  57173
			'Geography.Regions.Asia.North Asia'             1317  -->    677   640   169  58566
			'Geography.Regions.Asia.South Asia'             2361  -->   1700   661   131  57560
			'Geography.Regions.Asia.Southeast Asia'         1623  -->    710   913   105  58324
			'Geography.Regions.Asia.West Asia'              2154  -->   1294   860   118  57780
			'Geography.Regions.Europe.Eastern Europe'       2996  -->   1709  1287   319  56737
			'Geography.Regions.Europe.Europe*'             11970  -->   7227  4743  1782  46300
			'Geography.Regions.Europe.Northern Europe'      4083  -->   1666  2417   451  55518
			'Geography.Regions.Europe.Southern Europe'      2233  -->    877  1356   226  57593
			'Geography.Regions.Europe.Western Europe'       3035  -->   1496  1539   404  56613
			'Geography.Regions.Oceania'                     2466  -->   1379  1087    98  57488
			'History and Society.Business and economics'    3248  -->   1127  2121   524  56280
			'History and Society.Education'                 2097  -->    884  1213   241  57714
			'History and Society.History'                   3062  -->    610  2452   288  56702
			'History and Society.Military and warfare'      3819  -->   2334  1485   427  55806
			'History and Society.Politics and government'   4473  -->   1747  2726   450  55129
			'History and Society.Society'                   3850  -->    771  3079   286  55916
			'History and Society.Transportation'            3424  -->   2565   859   259  56369
			'STEM.Biology'                                  2735  -->   1976   759   151  57166
			'STEM.Chemistry'                                1251  -->    686   565   177  58624
			'STEM.Computing'                                1902  -->    949   953   403  57747
			'STEM.Earth and environment'                    1590  -->    807   783   133  58329
			'STEM.Engineering'                              2145  -->   1245   900   194  57713
			'STEM.Libraries & Information'                  1110  -->    514   596    76  58866
			'STEM.Mathematics'                              1026  -->    455   571   112  58914
			'STEM.Medicine & Health'                        1613  -->    851   762   186  58253
			'STEM.Physics'                                  1135  -->    533   602   159  58758
			'STEM.STEM*'                                   15592  -->  12289  3303  1426  43034
			'STEM.Space'                                    1330  -->   1027   303    52  58670
			'STEM.Technology'                               3436  -->   1576  1860   612  56004
	rates:
		              'Culture.Biography.Biography*'    'Culture.Biography.Women'    'Culture.Food and drink'    'Culture.Internet culture'    'Culture.Linguistics'    'Culture.Literature'    'Culture.Media.Books'    'Culture.Media.Entertainment'    'Culture.Media.Films'    'Culture.Media.Media*'    'Culture.Media.Music'    'Culture.Media.Radio'    'Culture.Media.Software'    'Culture.Media.Television'    'Culture.Media.Video games'    'Culture.Performing arts'    'Culture.Philosophy and religion'    'Culture.Sports'    'Culture.Visual arts.Architecture'    'Culture.Visual arts.Comics and Anime'    'Culture.Visual arts.Fashion'    'Culture.Visual arts.Visual arts*'    'Geography.Geographical'    'Geography.Regions.Africa.Africa*'    'Geography.Regions.Africa.Central Africa'    'Geography.Regions.Africa.Eastern Africa'    'Geography.Regions.Africa.Northern Africa'    'Geography.Regions.Africa.Southern Africa'    'Geography.Regions.Africa.Western Africa'    'Geography.Regions.Americas.Central America'    'Geography.Regions.Americas.North America'    'Geography.Regions.Americas.South America'    'Geography.Regions.Asia.Asia*'    'Geography.Regions.Asia.Central Asia'    'Geography.Regions.Asia.East Asia'    'Geography.Regions.Asia.North Asia'    'Geography.Regions.Asia.South Asia'    'Geography.Regions.Asia.Southeast Asia'    'Geography.Regions.Asia.West Asia'    'Geography.Regions.Europe.Eastern Europe'    'Geography.Regions.Europe.Europe*'    'Geography.Regions.Europe.Northern Europe'    'Geography.Regions.Europe.Southern Europe'    'Geography.Regions.Europe.Western Europe'    'Geography.Regions.Oceania'    'History and Society.Business and economics'    'History and Society.Education'    'History and Society.History'    'History and Society.Military and warfare'    'History and Society.Politics and government'    'History and Society.Society'    'History and Society.Transportation'    'STEM.Biology'    'STEM.Chemistry'    'STEM.Computing'    'STEM.Earth and environment'    'STEM.Engineering'    'STEM.Libraries & Information'    'STEM.Mathematics'    'STEM.Medicine & Health'    'STEM.Physics'    'STEM.STEM*'    'STEM.Space'    'STEM.Technology'
		----------  --------------------------------  ---------------------------  --------------------------  ----------------------------  -----------------------  ----------------------  -----------------------  -------------------------------  -----------------------  ------------------------  -----------------------  -----------------------  --------------------------  ----------------------------  -----------------------------  ---------------------------  -----------------------------------  ------------------  ------------------------------------  ----------------------------------------  -------------------------------  ------------------------------------  --------------------------  ------------------------------------  -------------------------------------------  -------------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  ----------------------------------------------  --------------------------------------------  --------------------------------------------  --------------------------------  ---------------------------------------  ------------------------------------  -------------------------------------  -------------------------------------  -----------------------------------------  ------------------------------------  -------------------------------------------  ------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  -----------------------------  ----------------------------------------------  ---------------------------------  -------------------------------  --------------------------------------------  -----------------------------------------------  -------------------------------  --------------------------------------  ----------------  ------------------  ------------------  ------------------------------  --------------------  --------------------------------  --------------------  --------------------------  ----------------  --------------  --------------  -------------------
		sample                                 0.272                        0.068                       0.021                         0.045                    0.02                    0.083                    0.03                             0.029                    0.037                     0.224                    0.042                    0.019                       0.028                         0.033                          0.031                        0.021                                0.042               0.095                                 0.041                                     0.023                            0.019                                 0.095                       0.054                                 0.092                                            0                                        0.018                                         0.02                                          0.021                                        0.019                                           0.021                                         0.121                                         0.025                             0.177                                    0.019                                 0.043                                  0.022                                  0.039                                      0.027                                 0.036                                        0.05                                  0.199                                         0.068                                         0.037                                        0.051                          0.041                                           0.054                              0.035                            0.051                                         0.064                                            0.074                            0.064                                   0.057             0.046               0.021               0.032                           0.026                 0.036                             0.018                 0.017                       0.027             0.019           0.26            0.022                0.057
		population                             0.123                        0.015                       0.002                         0.004                    0.007                   0.016                    0.004                            0.004                    0.011                     0.059                    0.024                    0.002                       0.001                         0.009                          0.003                        0.003                                0.011               0.071                                 0.011                                     0.002                            0.001                                 0.018                       0.024                                 0.008                                            0                                        0                                             0.001                                         0.001                                        0.001                                           0.003                                         0.064                                         0.006                             0.046                                    0.001                                 0.011                                  0.001                                  0.015                                      0.006                                 0.011                                        0.013                                 0.076                                         0.031                                         0.013                                        0.019                          0.015                                           0.01                               0.007                            0.011                                         0.014                                            0.028                            0.013                                   0.015             0.034               0.002               0.003                           0.005                 0.005                             0.001                 0                           0.006             0.001           0.069           0.006                0.005
	match_rate (micro=0.051, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.133
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.085
		Culture.Media.Music                          0.022
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.068
		Culture.Visual arts.Architecture             0.011
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.018
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.123
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.051
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.05
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.004
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.013
		Geography.Regions.Europe.Europe*             0.08
		Geography.Regions.Europe.Northern Europe     0.02
		Geography.Regions.Europe.Southern Europe     0.009
		Geography.Regions.Europe.Western Europe      0.016
		Geography.Regions.Oceania                    0.01
		History and Society.Business and economics   0.013
		History and Society.Education                0.007
		History and Society.History                  0.007
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.019
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.027
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.084
		STEM.Space                                   0.006
		STEM.Technology                              0.013
		-------------------------------------------  -----
	filter_rate (micro=0.949, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.867
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.915
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.932
		Culture.Visual arts.Architecture             0.989
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.982
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.877
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.949
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.95
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.987
		Geography.Regions.Europe.Europe*             0.92
		Geography.Regions.Europe.Northern Europe     0.98
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.99
		History and Society.Business and economics   0.987
		History and Society.Education                0.993
		History and Society.History                  0.993
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.981
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.916
		STEM.Space                                   0.994
		STEM.Technology                              0.987
		-------------------------------------------  -----
	recall (micro=0.628, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.756
		Culture.Biography.Women                      0.278
		Culture.Food and drink                       0.635
		Culture.Internet culture                     0.646
		Culture.Linguistics                          0.542
		Culture.Literature                           0.596
		Culture.Media.Books                          0.512
		Culture.Media.Entertainment                  0.195
		Culture.Media.Films                          0.678
		Culture.Media.Media*                         0.768
		Culture.Media.Music                          0.72
		Culture.Media.Radio                          0.739
		Culture.Media.Software                       0.473
		Culture.Media.Television                     0.521
		Culture.Media.Video games                    0.775
		Culture.Performing arts                      0.489
		Culture.Philosophy and religion              0.451
		Culture.Sports                               0.865
		Culture.Visual arts.Architecture             0.615
		Culture.Visual arts.Comics and Anime         0.543
		Culture.Visual arts.Fashion                  0.592
		Culture.Visual arts.Visual arts*             0.552
		Geography.Geographical                       0.561
		Geography.Regions.Africa.Africa*             0.695
		Geography.Regions.Africa.Central Africa      0.222
		Geography.Regions.Africa.Eastern Africa      0.559
		Geography.Regions.Africa.Northern Africa     0.494
		Geography.Regions.Africa.Southern Africa     0.597
		Geography.Regions.Africa.Western Africa      0.676
		Geography.Regions.Americas.Central America   0.324
		Geography.Regions.Americas.North America     0.536
		Geography.Regions.Americas.South America     0.474
		Geography.Regions.Asia.Asia*                 0.69
		Geography.Regions.Asia.Central Asia          0.476
		Geography.Regions.Asia.East Asia             0.532
		Geography.Regions.Asia.North Asia            0.514
		Geography.Regions.Asia.South Asia            0.72
		Geography.Regions.Asia.Southeast Asia        0.437
		Geography.Regions.Asia.West Asia             0.601
		Geography.Regions.Europe.Eastern Europe      0.57
		Geography.Regions.Europe.Europe*             0.604
		Geography.Regions.Europe.Northern Europe     0.408
		Geography.Regions.Europe.Southern Europe     0.393
		Geography.Regions.Europe.Western Europe      0.493
		Geography.Regions.Oceania                    0.559
		History and Society.Business and economics   0.347
		History and Society.Education                0.422
		History and Society.History                  0.199
		History and Society.Military and warfare     0.611
		History and Society.Politics and government  0.391
		History and Society.Society                  0.2
		History and Society.Transportation           0.749
		STEM.Biology                                 0.722
		STEM.Chemistry                               0.548
		STEM.Computing                               0.499
		STEM.Earth and environment                   0.508
		STEM.Engineering                             0.58
		STEM.Libraries & Information                 0.463
		STEM.Mathematics                             0.443
		STEM.Medicine & Health                       0.528
		STEM.Physics                                 0.47
		STEM.STEM*                                   0.788
		STEM.Space                                   0.772
		STEM.Technology                              0.459
		-------------------------------------------  -----
	!recall (micro=0.982, macro=0.991):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.955
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.988
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.958
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.99
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.877
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.98
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.992
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.995
		History and Society.Transportation           0.995
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.629, macro=0.477):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.701
		Culture.Biography.Women                      0.314
		Culture.Food and drink                       0.461
		Culture.Internet culture                     0.376
		Culture.Linguistics                          0.688
		Culture.Literature                           0.447
		Culture.Media.Books                          0.349
		Culture.Media.Entertainment                  0.273
		Culture.Media.Films                          0.676
		Culture.Media.Media*                         0.529
		Culture.Media.Music                          0.773
		Culture.Media.Radio                          0.631
		Culture.Media.Software                       0.098
		Culture.Media.Television                     0.515
		Culture.Media.Video games                    0.648
		Culture.Performing arts                      0.418
		Culture.Philosophy and religion              0.453
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.587
		Culture.Visual arts.Comics and Anime         0.365
		Culture.Visual arts.Fashion                  0.256
		Culture.Visual arts.Visual arts*             0.51
		Geography.Geographical                       0.738
		Geography.Regions.Africa.Africa*             0.528
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.192
		Geography.Regions.Africa.Northern Africa     0.249
		Geography.Regions.Africa.Southern Africa     0.392
		Geography.Regions.Africa.Western Africa      0.336
		Geography.Regions.Americas.Central America   0.382
		Geography.Regions.Americas.North America     0.673
		Geography.Regions.Americas.South America     0.501
		Geography.Regions.Asia.Asia*                 0.625
		Geography.Regions.Asia.Central Asia          0.303
		Geography.Regions.Asia.East Asia             0.553
		Geography.Regions.Asia.North Asia            0.142
		Geography.Regions.Asia.South Asia            0.83
		Geography.Regions.Asia.Southeast Asia        0.595
		Geography.Regions.Asia.West Asia             0.765
		Geography.Regions.Europe.Eastern Europe      0.57
		Geography.Regions.Europe.Europe*             0.573
		Geography.Regions.Europe.Northern Europe     0.615
		Geography.Regions.Europe.Southern Europe     0.57
		Geography.Regions.Europe.Western Europe      0.576
		Geography.Regions.Oceania                    0.835
		History and Society.Business and economics   0.277
		History and Society.Education                0.429
		History and Society.History                  0.302
		History and Society.Military and warfare     0.535
		History and Society.Politics and government  0.583
		History and Society.Society                  0.335
		History and Society.Transportation           0.715
		STEM.Biology                                 0.905
		STEM.Chemistry                               0.222
		STEM.Computing                               0.163
		STEM.Earth and environment                   0.504
		STEM.Engineering                             0.477
		STEM.Libraries & Information                 0.183
		STEM.Mathematics                             0.089
		STEM.Medicine & Health                       0.516
		STEM.Physics                                 0.129
		STEM.STEM*                                   0.646
		STEM.Space                                   0.841
		STEM.Technology                              0.18
		-------------------------------------------  -----
	!precision (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.989
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.994
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.985
		Culture.Media.Music                          0.993
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.99
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.969
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.99
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.982
		History and Society.Society                  0.99
		History and Society.Transportation           0.996
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 1
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.997
		-------------------------------------------  -----
	f1 (micro=0.621, macro=0.487):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.728
		Culture.Biography.Women                      0.295
		Culture.Food and drink                       0.534
		Culture.Internet culture                     0.475
		Culture.Linguistics                          0.606
		Culture.Literature                           0.511
		Culture.Media.Books                          0.415
		Culture.Media.Entertainment                  0.228
		Culture.Media.Films                          0.677
		Culture.Media.Media*                         0.627
		Culture.Media.Music                          0.745
		Culture.Media.Radio                          0.681
		Culture.Media.Software                       0.162
		Culture.Media.Television                     0.518
		Culture.Media.Video games                    0.706
		Culture.Performing arts                      0.451
		Culture.Philosophy and religion              0.452
		Culture.Sports                               0.886
		Culture.Visual arts.Architecture             0.601
		Culture.Visual arts.Comics and Anime         0.436
		Culture.Visual arts.Fashion                  0.358
		Culture.Visual arts.Visual arts*             0.53
		Geography.Geographical                       0.637
		Geography.Regions.Africa.Africa*             0.601
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.286
		Geography.Regions.Africa.Northern Africa     0.331
		Geography.Regions.Africa.Southern Africa     0.474
		Geography.Regions.Africa.Western Africa      0.449
		Geography.Regions.Americas.Central America   0.351
		Geography.Regions.Americas.North America     0.597
		Geography.Regions.Americas.South America     0.487
		Geography.Regions.Asia.Asia*                 0.656
		Geography.Regions.Asia.Central Asia          0.37
		Geography.Regions.Asia.East Asia             0.543
		Geography.Regions.Asia.North Asia            0.222
		Geography.Regions.Asia.South Asia            0.771
		Geography.Regions.Asia.Southeast Asia        0.504
		Geography.Regions.Asia.West Asia             0.673
		Geography.Regions.Europe.Eastern Europe      0.57
		Geography.Regions.Europe.Europe*             0.588
		Geography.Regions.Europe.Northern Europe     0.491
		Geography.Regions.Europe.Southern Europe     0.465
		Geography.Regions.Europe.Western Europe      0.531
		Geography.Regions.Oceania                    0.67
		History and Society.Business and economics   0.308
		History and Society.Education                0.425
		History and Society.History                  0.24
		History and Society.Military and warfare     0.57
		History and Society.Politics and government  0.468
		History and Society.Society                  0.251
		History and Society.Transportation           0.732
		STEM.Biology                                 0.804
		STEM.Chemistry                               0.316
		STEM.Computing                               0.245
		STEM.Earth and environment                   0.506
		STEM.Engineering                             0.524
		STEM.Libraries & Information                 0.262
		STEM.Mathematics                             0.148
		STEM.Medicine & Health                       0.522
		STEM.Physics                                 0.202
		STEM.STEM*                                   0.71
		STEM.Space                                   0.805
		STEM.Technology                              0.258
		-------------------------------------------  -----
	!f1 (micro=0.983, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.96
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.991
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.935
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.983
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.965
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.987
		History and Society.Society                  0.992
		History and Society.Transportation           0.996
		STEM.Biology                                 0.994
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.976
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.968, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.93
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.982
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.993
		Culture.Media.Media*                         0.946
		Culture.Media.Music                          0.988
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.984
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.877
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.953
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.967
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.99
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.994
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.936
		Geography.Regions.Europe.Northern Europe     0.974
		Geography.Regions.Europe.Southern Europe     0.988
		Geography.Regions.Europe.Western Europe      0.983
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.984
		History and Society.Education                0.992
		History and Society.History                  0.986
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.975
		History and Society.Society                  0.985
		History and Society.Transportation           0.992
		STEM.Biology                                 0.988
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.955
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.018, macro=0.009):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.045
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.012
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.042
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.01
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.123
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.018
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.02
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.008
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.005
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.005
		History and Society.Transportation           0.005
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.032
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.954, macro=0.957):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.933
		Culture.Food and drink                       0.973
		Culture.Internet culture                     0.975
		Culture.Linguistics                          0.957
		Culture.Literature                           0.961
		Culture.Media.Books                          0.97
		Culture.Media.Entertainment                  0.94
		Culture.Media.Films                          0.978
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.983
		Culture.Media.Software                       0.974
		Culture.Media.Television                     0.968
		Culture.Media.Video games                    0.986
		Culture.Performing arts                      0.966
		Culture.Philosophy and religion              0.942
		Culture.Sports                               0.979
		Culture.Visual arts.Architecture             0.972
		Culture.Visual arts.Comics and Anime         0.978
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.951
		Geography.Geographical                       0.958
		Geography.Regions.Africa.Africa*             0.969
		Geography.Regions.Africa.Central Africa      0.649
		Geography.Regions.Africa.Eastern Africa      0.971
		Geography.Regions.Africa.Northern Africa     0.967
		Geography.Regions.Africa.Southern Africa     0.972
		Geography.Regions.Africa.Western Africa      0.98
		Geography.Regions.Americas.Central America   0.955
		Geography.Regions.Americas.North America     0.938
		Geography.Regions.Americas.South America     0.961
		Geography.Regions.Asia.Asia*                 0.957
		Geography.Regions.Asia.Central Asia          0.972
		Geography.Regions.Asia.East Asia             0.965
		Geography.Regions.Asia.North Asia            0.973
		Geography.Regions.Asia.South Asia            0.976
		Geography.Regions.Asia.Southeast Asia        0.96
		Geography.Regions.Asia.West Asia             0.969
		Geography.Regions.Europe.Eastern Europe      0.967
		Geography.Regions.Europe.Europe*             0.934
		Geography.Regions.Europe.Northern Europe     0.94
		Geography.Regions.Europe.Southern Europe     0.956
		Geography.Regions.Europe.Western Europe      0.956
		Geography.Regions.Oceania                    0.962
		History and Society.Business and economics   0.936
		History and Society.Education                0.951
		History and Society.History                  0.902
		History and Society.Military and warfare     0.964
		History and Society.Politics and government  0.927
		History and Society.Society                  0.868
		History and Society.Transportation           0.981
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.981
		STEM.Computing                               0.977
		STEM.Earth and environment                   0.964
		STEM.Engineering                             0.965
		STEM.Libraries & Information                 0.957
		STEM.Mathematics                             0.971
		STEM.Medicine & Health                       0.968
		STEM.Physics                                 0.977
		STEM.STEM*                                   0.958
		STEM.Space                                   0.985
		STEM.Technology                              0.952
		-------------------------------------------  -----
	pr_auc (micro=0.649, macro=0.479):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.795
		Culture.Biography.Women                      0.235
		Culture.Food and drink                       0.544
		Culture.Internet culture                     0.587
		Culture.Linguistics                          0.593
		Culture.Literature                           0.526
		Culture.Media.Books                          0.372
		Culture.Media.Entertainment                  0.161
		Culture.Media.Films                          0.702
		Culture.Media.Media*                         0.688
		Culture.Media.Music                          0.77
		Culture.Media.Radio                          0.741
		Culture.Media.Software                       0.11
		Culture.Media.Television                     0.487
		Culture.Media.Video games                    0.761
		Culture.Performing arts                      0.396
		Culture.Philosophy and religion              0.365
		Culture.Sports                               0.911
		Culture.Visual arts.Architecture             0.656
		Culture.Visual arts.Comics and Anime         0.435
		Culture.Visual arts.Fashion                  0.31
		Culture.Visual arts.Visual arts*             0.532
		Geography.Geographical                       0.688
		Geography.Regions.Africa.Africa*             0.576
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.23
		Geography.Regions.Africa.Northern Africa     0.25
		Geography.Regions.Africa.Southern Africa     0.414
		Geography.Regions.Africa.Western Africa      0.37
		Geography.Regions.Americas.Central America   0.258
		Geography.Regions.Americas.North America     0.651
		Geography.Regions.Americas.South America     0.433
		Geography.Regions.Asia.Asia*                 0.695
		Geography.Regions.Asia.Central Asia          0.306
		Geography.Regions.Asia.East Asia             0.521
		Geography.Regions.Asia.North Asia            0.173
		Geography.Regions.Asia.South Asia            0.798
		Geography.Regions.Asia.Southeast Asia        0.49
		Geography.Regions.Asia.West Asia             0.698
		Geography.Regions.Europe.Eastern Europe      0.589
		Geography.Regions.Europe.Europe*             0.613
		Geography.Regions.Europe.Northern Europe     0.495
		Geography.Regions.Europe.Southern Europe     0.449
		Geography.Regions.Europe.Western Europe      0.529
		Geography.Regions.Oceania                    0.719
		History and Society.Business and economics   0.24
		History and Society.Education                0.346
		History and Society.History                  0.174
		History and Society.Military and warfare     0.588
		History and Society.Politics and government  0.499
		History and Society.Society                  0.2
		History and Society.Transportation           0.772
		STEM.Biology                                 0.86
		STEM.Chemistry                               0.24
		STEM.Computing                               0.174
		STEM.Earth and environment                   0.502
		STEM.Engineering                             0.546
		STEM.Libraries & Information                 0.253
		STEM.Mathematics                             0.1
		STEM.Medicine & Health                       0.509
		STEM.Physics                                 0.176
		STEM.STEM*                                   0.798
		STEM.Space                                   0.848
		STEM.Technology                              0.215
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'History and Society.Business and economics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}}, 'type': 'object'}

