Model Information:
	 - type: GradientBoosting
	 - version: 1.0
	 - params: {'verbose': 0, 'multilabel': True, 'label_weights': {}, 'scale': False, 'n_iter_no_change': None, 'min_impurity_split': None, 'max_depth': 5, 'random_state': None, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_features': 'log2', 'population_rates': None, 'min_samples_split': 2, 'loss': 'deviance', 'learning_rate': 0.1, 'criterion': 'friedman_mse', 'presort': 'auto', 'min_samples_leaf': 1, 'init': None, 'center': False, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'tol': 0.0001, 'warm_start': False, 'min_weight_fraction_leaf': 0.0, 'subsample': 1.0, 'n_estimators': 150}
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
	counts (n=63017):
			label                                              n          TP    FP     FN     TN
			---------------------------------------------  -----  ---  -----  ----  -----  -----
			'Culture.Biography.Biography*'                 16717  -->  13631  3086   1609  44691
			'Culture.Biography.Women'                       4173  -->   1526  2647    541  58303
			'Culture.Food and drink'                        1323  -->    943   380     94  61600
			'Culture.Internet culture'                      2946  -->   2159   787    208  59863
			'Culture.Linguistics'                           1384  -->    919   465     97  61536
			'Culture.Literature'                            5277  -->   3625  1652    590  57150
			'Culture.Media.Books'                           1919  -->   1200   719    221  60877
			'Culture.Media.Entertainment'                   1876  -->    596  1280    147  60994
			'Culture.Media.Films'                           2307  -->   1762   545    187  60523
			'Culture.Media.Media*'                         14363  -->  11785  2578   1971  46683
			'Culture.Media.Music'                           2677  -->   2143   534    294  60046
			'Culture.Media.Radio'                           1174  -->    926   248     49  61794
			'Culture.Media.Software'                        1798  -->    965   833    401  60818
			'Culture.Media.Television'                      2200  -->   1388   812    246  60571
			'Culture.Media.Video games'                     2078  -->   1783   295     62  60877
			'Culture.Performing arts'                       1334  -->    794   540    120  61563
			'Culture.Philosophy and religion'               2638  -->   1348  1290    377  60002
			'Culture.Sports'                                5843  -->   5186   657    363  56811
			'Culture.Visual arts.Architecture'              2565  -->   1737   828    292  60160
			'Culture.Visual arts.Comics and Anime'          1488  -->    981   507    120  61409
			'Culture.Visual arts.Fashion'                   1188  -->    798   390     72  61757
			'Culture.Visual arts.Visual arts*'              5987  -->   3871  2116    605  56425
			'Geography.Geographical'                        3344  -->   1893  1451    317  59356
			'Geography.Regions.Africa.Africa*'              5693  -->   4344  1349    260  57064
			'Geography.Regions.Africa.Central Africa'         28  -->      8    20  12588  50401
			'Geography.Regions.Africa.Eastern Africa'       1114  -->    665   449     46  61857
			'Geography.Regions.Africa.Northern Africa'      1266  -->    685   581    109  61642
			'Geography.Regions.Africa.Southern Africa'      1288  -->    849   439     58  61671
			'Geography.Regions.Africa.Western Africa'       1152  -->    836   316     55  61810
			'Geography.Regions.Americas.Central America'    1326  -->    511   815    117  61574
			'Geography.Regions.Americas.North America'      7565  -->   4659  2906   1100  54352
			'Geography.Regions.Americas.South America'      1523  -->    747   776    190  61304
			'Geography.Regions.Asia.Asia*'                 11060  -->   8318  2742    986  50971
			'Geography.Regions.Asia.Central Asia'           1163  -->    634   529     69  61785
			'Geography.Regions.Asia.East Asia'              2721  -->   1676  1045    279  60017
			'Geography.Regions.Asia.North Asia'             1361  -->    765   596    182  61474
			'Geography.Regions.Asia.South Asia'             2438  -->   1909   529    129  60450
			'Geography.Regions.Asia.Southeast Asia'         1688  -->    907   781    106  61223
			'Geography.Regions.Asia.West Asia'              2264  -->   1440   824    125  60628
			'Geography.Regions.Europe.Eastern Europe'       3083  -->   1865  1218    358  59576
			'Geography.Regions.Europe.Europe*'             12415  -->   8245  4170   1909  48693
			'Geography.Regions.Europe.Northern Europe'      4244  -->   2051  2193    557  58216
			'Geography.Regions.Europe.Southern Europe'      2320  -->   1023  1297    249  60448
			'Geography.Regions.Europe.Western Europe'       3160  -->   1741  1419    429  59428
			'Geography.Regions.Oceania'                     2537  -->   1647   890    109  60371
			'History and Society.Business and economics'    3430  -->   1470  1960    535  59052
			'History and Society.Education'                 2178  -->   1024  1154    261  60578
			'History and Society.History'                   3217  -->    865  2352    324  59476
			'History and Society.Military and warfare'      3977  -->   2629  1348    422  58618
			'History and Society.Politics and government'   4647  -->   2211  2436    523  57847
			'History and Society.Society'                   4057  -->    916  3141    335  58625
			'History and Society.Transportation'            3604  -->   2950   654    248  59165
			'STEM.Biology'                                  2834  -->   2169   665    162  60021
			'STEM.Chemistry'                                1344  -->    853   491    181  61492
			'STEM.Computing'                                2011  -->   1221   790    433  60573
			'STEM.Earth and environment'                    1683  -->    975   708    135  61199
			'STEM.Engineering'                              2272  -->   1445   827    176  60569
			'STEM.Libraries & Information'                  1159  -->    590   569     83  61775
			'STEM.Mathematics'                              1121  -->    643   478    151  61745
			'STEM.Medicine & Health'                        1737  -->   1066   671    198  61082
			'STEM.Physics'                                  1206  -->    686   520    180  61631
			'STEM.STEM*'                                   16499  -->  13629  2870   1282  45236
			'STEM.Space'                                    1398  -->   1163   235     58  61561
			'STEM.Technology'                               3712  -->   2004  1708    704  58601
	rates:
		              'Culture.Biography.Biography*'    'Culture.Biography.Women'    'Culture.Food and drink'    'Culture.Internet culture'    'Culture.Linguistics'    'Culture.Literature'    'Culture.Media.Books'    'Culture.Media.Entertainment'    'Culture.Media.Films'    'Culture.Media.Media*'    'Culture.Media.Music'    'Culture.Media.Radio'    'Culture.Media.Software'    'Culture.Media.Television'    'Culture.Media.Video games'    'Culture.Performing arts'    'Culture.Philosophy and religion'    'Culture.Sports'    'Culture.Visual arts.Architecture'    'Culture.Visual arts.Comics and Anime'    'Culture.Visual arts.Fashion'    'Culture.Visual arts.Visual arts*'    'Geography.Geographical'    'Geography.Regions.Africa.Africa*'    'Geography.Regions.Africa.Central Africa'    'Geography.Regions.Africa.Eastern Africa'    'Geography.Regions.Africa.Northern Africa'    'Geography.Regions.Africa.Southern Africa'    'Geography.Regions.Africa.Western Africa'    'Geography.Regions.Americas.Central America'    'Geography.Regions.Americas.North America'    'Geography.Regions.Americas.South America'    'Geography.Regions.Asia.Asia*'    'Geography.Regions.Asia.Central Asia'    'Geography.Regions.Asia.East Asia'    'Geography.Regions.Asia.North Asia'    'Geography.Regions.Asia.South Asia'    'Geography.Regions.Asia.Southeast Asia'    'Geography.Regions.Asia.West Asia'    'Geography.Regions.Europe.Eastern Europe'    'Geography.Regions.Europe.Europe*'    'Geography.Regions.Europe.Northern Europe'    'Geography.Regions.Europe.Southern Europe'    'Geography.Regions.Europe.Western Europe'    'Geography.Regions.Oceania'    'History and Society.Business and economics'    'History and Society.Education'    'History and Society.History'    'History and Society.Military and warfare'    'History and Society.Politics and government'    'History and Society.Society'    'History and Society.Transportation'    'STEM.Biology'    'STEM.Chemistry'    'STEM.Computing'    'STEM.Earth and environment'    'STEM.Engineering'    'STEM.Libraries & Information'    'STEM.Mathematics'    'STEM.Medicine & Health'    'STEM.Physics'    'STEM.STEM*'    'STEM.Space'    'STEM.Technology'
		----------  --------------------------------  ---------------------------  --------------------------  ----------------------------  -----------------------  ----------------------  -----------------------  -------------------------------  -----------------------  ------------------------  -----------------------  -----------------------  --------------------------  ----------------------------  -----------------------------  ---------------------------  -----------------------------------  ------------------  ------------------------------------  ----------------------------------------  -------------------------------  ------------------------------------  --------------------------  ------------------------------------  -------------------------------------------  -------------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  ----------------------------------------------  --------------------------------------------  --------------------------------------------  --------------------------------  ---------------------------------------  ------------------------------------  -------------------------------------  -------------------------------------  -----------------------------------------  ------------------------------------  -------------------------------------------  ------------------------------------  --------------------------------------------  --------------------------------------------  -------------------------------------------  -----------------------------  ----------------------------------------------  ---------------------------------  -------------------------------  --------------------------------------------  -----------------------------------------------  -------------------------------  --------------------------------------  ----------------  ------------------  ------------------  ------------------------------  --------------------  --------------------------------  --------------------  --------------------------  ----------------  --------------  --------------  -------------------
		sample                                 0.265                        0.066                       0.021                         0.047                    0.022                   0.084                    0.03                             0.03                     0.037                     0.228                    0.042                    0.019                       0.029                         0.035                          0.033                        0.021                                0.042               0.093                                 0.041                                     0.024                            0.019                                 0.095                       0.053                                 0.09                                             0                                        0.018                                         0.02                                          0.02                                         0.018                                           0.021                                         0.12                                          0.024                             0.176                                    0.018                                 0.043                                  0.022                                  0.039                                      0.027                                 0.036                                        0.049                                 0.197                                         0.067                                         0.037                                        0.05                           0.04                                            0.054                              0.035                            0.051                                         0.063                                            0.074                            0.064                                   0.057             0.045               0.021               0.032                           0.027                 0.036                             0.018                 0.018                       0.028             0.019           0.262           0.022                0.059
		population                             0.123                        0.015                       0.002                         0.004                    0.007                   0.016                    0.004                            0.004                    0.011                     0.059                    0.024                    0.002                       0.001                         0.009                          0.003                        0.003                                0.011               0.071                                 0.011                                     0.002                            0.001                                 0.018                       0.024                                 0.008                                            0                                        0                                             0.001                                         0.001                                        0.001                                           0.003                                         0.064                                         0.006                             0.046                                    0.001                                 0.011                                  0.001                                  0.015                                      0.006                                 0.011                                        0.013                                 0.076                                         0.031                                         0.013                                        0.019                          0.015                                           0.01                               0.007                            0.011                                         0.014                                            0.028                            0.013                                   0.015             0.034               0.002               0.003                           0.005                 0.005                             0.001                 0                           0.006             0.001           0.069           0.006                0.005
	match_rate (micro=0.052, macro=0.02):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.086
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.012
		Culture.Sports                               0.069
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.022
		Geography.Geographical                       0.019
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.2
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.058
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.052
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.009
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.085
		Geography.Regions.Europe.Northern Europe     0.024
		Geography.Regions.Europe.Southern Europe     0.01
		Geography.Regions.Europe.Western Europe      0.018
		Geography.Regions.Oceania                    0.012
		History and Society.Business and economics   0.013
		History and Society.Education                0.008
		History and Society.History                  0.008
		History and Society.Military and warfare     0.016
		History and Society.Politics and government  0.022
		History and Society.Society                  0.008
		History and Society.Transportation           0.016
		STEM.Biology                                 0.028
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.006
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.003
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.083
		STEM.Space                                   0.006
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.98):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.914
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.988
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.978
		Geography.Geographical                       0.981
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.8
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.942
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.948
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.991
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.915
		Geography.Regions.Europe.Northern Europe     0.976
		Geography.Regions.Europe.Southern Europe     0.99
		Geography.Regions.Europe.Western Europe      0.982
		Geography.Regions.Oceania                    0.988
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.992
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.978
		History and Society.Society                  0.992
		History and Society.Transportation           0.984
		STEM.Biology                                 0.972
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.994
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.997
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.917
		STEM.Space                                   0.994
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.688, macro=0.613):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.815
		Culture.Biography.Women                      0.366
		Culture.Food and drink                       0.713
		Culture.Internet culture                     0.733
		Culture.Linguistics                          0.664
		Culture.Literature                           0.687
		Culture.Media.Books                          0.625
		Culture.Media.Entertainment                  0.318
		Culture.Media.Films                          0.764
		Culture.Media.Media*                         0.821
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.789
		Culture.Media.Software                       0.537
		Culture.Media.Television                     0.631
		Culture.Media.Video games                    0.858
		Culture.Performing arts                      0.595
		Culture.Philosophy and religion              0.511
		Culture.Sports                               0.888
		Culture.Visual arts.Architecture             0.677
		Culture.Visual arts.Comics and Anime         0.659
		Culture.Visual arts.Fashion                  0.672
		Culture.Visual arts.Visual arts*             0.647
		Geography.Geographical                       0.566
		Geography.Regions.Africa.Africa*             0.763
		Geography.Regions.Africa.Central Africa      0.286
		Geography.Regions.Africa.Eastern Africa      0.597
		Geography.Regions.Africa.Northern Africa     0.541
		Geography.Regions.Africa.Southern Africa     0.659
		Geography.Regions.Africa.Western Africa      0.726
		Geography.Regions.Americas.Central America   0.385
		Geography.Regions.Americas.North America     0.616
		Geography.Regions.Americas.South America     0.49
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.545
		Geography.Regions.Asia.East Asia             0.616
		Geography.Regions.Asia.North Asia            0.562
		Geography.Regions.Asia.South Asia            0.783
		Geography.Regions.Asia.Southeast Asia        0.537
		Geography.Regions.Asia.West Asia             0.636
		Geography.Regions.Europe.Eastern Europe      0.605
		Geography.Regions.Europe.Europe*             0.664
		Geography.Regions.Europe.Northern Europe     0.483
		Geography.Regions.Europe.Southern Europe     0.441
		Geography.Regions.Europe.Western Europe      0.551
		Geography.Regions.Oceania                    0.649
		History and Society.Business and economics   0.429
		History and Society.Education                0.47
		History and Society.History                  0.269
		History and Society.Military and warfare     0.661
		History and Society.Politics and government  0.476
		History and Society.Society                  0.226
		History and Society.Transportation           0.819
		STEM.Biology                                 0.765
		STEM.Chemistry                               0.635
		STEM.Computing                               0.607
		STEM.Earth and environment                   0.579
		STEM.Engineering                             0.636
		STEM.Libraries & Information                 0.509
		STEM.Mathematics                             0.574
		STEM.Medicine & Health                       0.614
		STEM.Physics                                 0.569
		STEM.STEM*                                   0.826
		STEM.Space                                   0.832
		STEM.Technology                              0.54
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.998
		Culture.Literature                           0.99
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.959
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.989
		Geography.Geographical                       0.995
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.8
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.98
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.981
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.996
		History and Society.History                  0.995
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.996
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.972
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.658, macro=0.508):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.767
		Culture.Biography.Women                      0.37
		Culture.Food and drink                       0.536
		Culture.Internet culture                     0.427
		Culture.Linguistics                          0.757
		Culture.Literature                           0.514
		Culture.Media.Books                          0.411
		Culture.Media.Entertainment                  0.322
		Culture.Media.Films                          0.725
		Culture.Media.Media*                         0.557
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.683
		Culture.Media.Software                       0.098
		Culture.Media.Television                     0.581
		Culture.Media.Video games                    0.688
		Culture.Performing arts                      0.47
		Culture.Philosophy and religion              0.468
		Culture.Sports                               0.915
		Culture.Visual arts.Architecture             0.6
		Culture.Visual arts.Comics and Anime         0.427
		Culture.Visual arts.Fashion                  0.318
		Culture.Visual arts.Visual arts*             0.532
		Geography.Geographical                       0.72
		Geography.Regions.Africa.Africa*             0.569
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.268
		Geography.Regions.Africa.Northern Africa     0.274
		Geography.Regions.Africa.Southern Africa     0.452
		Geography.Regions.Africa.Western Africa      0.358
		Geography.Regions.Americas.Central America   0.402
		Geography.Regions.Americas.North America     0.681
		Geography.Regions.Americas.South America     0.502
		Geography.Regions.Asia.Asia*                 0.654
		Geography.Regions.Asia.Central Asia          0.298
		Geography.Regions.Asia.East Asia             0.606
		Geography.Regions.Asia.North Asia            0.15
		Geography.Regions.Asia.South Asia            0.85
		Geography.Regions.Asia.Southeast Asia        0.653
		Geography.Regions.Asia.West Asia             0.773
		Geography.Regions.Europe.Eastern Europe      0.568
		Geography.Regions.Europe.Europe*             0.592
		Geography.Regions.Europe.Northern Europe     0.617
		Geography.Regions.Europe.Southern Europe     0.587
		Geography.Regions.Europe.Western Europe      0.601
		Geography.Regions.Oceania                    0.847
		History and Society.Business and economics   0.327
		History and Society.Education                0.448
		History and Society.History                  0.352
		History and Society.Military and warfare     0.569
		History and Society.Politics and government  0.606
		History and Society.Society                  0.337
		History and Society.Transportation           0.75
		STEM.Biology                                 0.908
		STEM.Chemistry                               0.252
		STEM.Computing                               0.188
		STEM.Earth and environment                   0.545
		STEM.Engineering                             0.536
		STEM.Libraries & Information                 0.191
		STEM.Mathematics                             0.089
		STEM.Medicine & Health                       0.55
		STEM.Physics                                 0.142
		STEM.STEM*                                   0.69
		STEM.Space                                   0.843
		STEM.Technology                              0.19
		-------------------------------------------  -----
	!precision (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.998
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.99
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.974
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.988
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.972
		Geography.Regions.Europe.Northern Europe     0.984
		Geography.Regions.Europe.Southern Europe     0.993
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.985
		History and Society.Society                  0.99
		History and Society.Transportation           0.997
		STEM.Biology                                 0.992
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.987
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.666, macro=0.535):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.791
		Culture.Biography.Women                      0.368
		Culture.Food and drink                       0.612
		Culture.Internet culture                     0.539
		Culture.Linguistics                          0.707
		Culture.Literature                           0.588
		Culture.Media.Books                          0.496
		Culture.Media.Entertainment                  0.32
		Culture.Media.Films                          0.744
		Culture.Media.Media*                         0.664
		Culture.Media.Music                          0.801
		Culture.Media.Radio                          0.732
		Culture.Media.Software                       0.166
		Culture.Media.Television                     0.605
		Culture.Media.Video games                    0.764
		Culture.Performing arts                      0.525
		Culture.Philosophy and religion              0.489
		Culture.Sports                               0.901
		Culture.Visual arts.Architecture             0.636
		Culture.Visual arts.Comics and Anime         0.518
		Culture.Visual arts.Fashion                  0.432
		Culture.Visual arts.Visual arts*             0.584
		Geography.Geographical                       0.634
		Geography.Regions.Africa.Africa*             0.652
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.37
		Geography.Regions.Africa.Northern Africa     0.363
		Geography.Regions.Africa.Southern Africa     0.536
		Geography.Regions.Africa.Western Africa      0.48
		Geography.Regions.Americas.Central America   0.394
		Geography.Regions.Americas.North America     0.647
		Geography.Regions.Americas.South America     0.496
		Geography.Regions.Asia.Asia*                 0.7
		Geography.Regions.Asia.Central Asia          0.385
		Geography.Regions.Asia.East Asia             0.611
		Geography.Regions.Asia.North Asia            0.237
		Geography.Regions.Asia.South Asia            0.815
		Geography.Regions.Asia.Southeast Asia        0.589
		Geography.Regions.Asia.West Asia             0.698
		Geography.Regions.Europe.Eastern Europe      0.586
		Geography.Regions.Europe.Europe*             0.626
		Geography.Regions.Europe.Northern Europe     0.542
		Geography.Regions.Europe.Southern Europe     0.504
		Geography.Regions.Europe.Western Europe      0.575
		Geography.Regions.Oceania                    0.735
		History and Society.Business and economics   0.371
		History and Society.Education                0.459
		History and Society.History                  0.305
		History and Society.Military and warfare     0.612
		History and Society.Politics and government  0.533
		History and Society.Society                  0.27
		History and Society.Transportation           0.783
		STEM.Biology                                 0.831
		STEM.Chemistry                               0.361
		STEM.Computing                               0.287
		STEM.Earth and environment                   0.562
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.278
		STEM.Mathematics                             0.155
		STEM.Medicine & Health                       0.58
		STEM.Physics                                 0.228
		STEM.STEM*                                   0.752
		STEM.Space                                   0.837
		STEM.Technology                              0.281
		-------------------------------------------  -----
	!f1 (micro=0.985, macro=0.992):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.97
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.974
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.996
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.991
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.889
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.985
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.967
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.994
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.993
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.973, macro=0.986):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.947
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.951
		Culture.Media.Music                          0.99
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.986
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.983
		Geography.Geographical                       0.985
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.8
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.971
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.991
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.994
		Geography.Regions.Europe.Eastern Europe      0.989
		Geography.Regions.Europe.Europe*             0.94
		Geography.Regions.Europe.Northern Europe     0.975
		Geography.Regions.Europe.Southern Europe     0.989
		Geography.Regions.Europe.Western Europe      0.984
		Geography.Regions.Oceania                    0.993
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.987
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.977
		History and Society.Society                  0.985
		History and Society.Transportation           0.993
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.997
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.962
		STEM.Space                                   0.998
		STEM.Technology                              0.986
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.01):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.035
		Culture.Biography.Women                      0.009
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.002
		Culture.Literature                           0.01
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.002
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.041
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.006
		Culture.Visual arts.Architecture             0.005
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.011
		Geography.Geographical                       0.005
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.2
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.02
		Geography.Regions.Americas.South America     0.003
		Geography.Regions.Asia.Asia*                 0.019
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.006
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.009
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.004
		History and Society.History                  0.005
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.009
		History and Society.Society                  0.006
		History and Society.Transportation           0.004
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.028
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.966, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.962
		Culture.Biography.Women                      0.951
		Culture.Food and drink                       0.985
		Culture.Internet culture                     0.983
		Culture.Linguistics                          0.975
		Culture.Literature                           0.973
		Culture.Media.Books                          0.979
		Culture.Media.Entertainment                  0.96
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.986
		Culture.Media.Radio                          0.99
		Culture.Media.Software                       0.979
		Culture.Media.Television                     0.979
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.981
		Culture.Philosophy and religion              0.958
		Culture.Sports                               0.983
		Culture.Visual arts.Architecture             0.981
		Culture.Visual arts.Comics and Anime         0.984
		Culture.Visual arts.Fashion                  0.984
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.964
		Geography.Regions.Africa.Africa*             0.979
		Geography.Regions.Africa.Central Africa      0.585
		Geography.Regions.Africa.Eastern Africa      0.98
		Geography.Regions.Africa.Northern Africa     0.975
		Geography.Regions.Africa.Southern Africa     0.98
		Geography.Regions.Africa.Western Africa      0.988
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.973
		Geography.Regions.Asia.Asia*                 0.969
		Geography.Regions.Asia.Central Asia          0.98
		Geography.Regions.Asia.East Asia             0.975
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.972
		Geography.Regions.Asia.West Asia             0.976
		Geography.Regions.Europe.Eastern Europe      0.976
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.956
		Geography.Regions.Europe.Southern Europe     0.966
		Geography.Regions.Europe.Western Europe      0.97
		Geography.Regions.Oceania                    0.978
		History and Society.Business and economics   0.953
		History and Society.Education                0.964
		History and Society.History                  0.922
		History and Society.Military and warfare     0.976
		History and Society.Politics and government  0.949
		History and Society.Society                  0.894
		History and Society.Transportation           0.986
		STEM.Biology                                 0.978
		STEM.Chemistry                               0.986
		STEM.Computing                               0.98
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.978
		STEM.Medicine & Health                       0.975
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.967
		STEM.Space                                   0.991
		STEM.Technology                              0.962
		-------------------------------------------  -----
	pr_auc (micro=0.707, macro=0.543):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.865
		Culture.Biography.Women                      0.311
		Culture.Food and drink                       0.625
		Culture.Internet culture                     0.676
		Culture.Linguistics                          0.702
		Culture.Literature                           0.642
		Culture.Media.Books                          0.483
		Culture.Media.Entertainment                  0.28
		Culture.Media.Films                          0.797
		Culture.Media.Media*                         0.769
		Culture.Media.Music                          0.844
		Culture.Media.Radio                          0.819
		Culture.Media.Software                       0.108
		Culture.Media.Television                     0.648
		Culture.Media.Video games                    0.876
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.426
		Culture.Sports                               0.924
		Culture.Visual arts.Architecture             0.688
		Culture.Visual arts.Comics and Anime         0.518
		Culture.Visual arts.Fashion                  0.362
		Culture.Visual arts.Visual arts*             0.622
		Geography.Geographical                       0.676
		Geography.Regions.Africa.Africa*             0.675
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.265
		Geography.Regions.Africa.Northern Africa     0.262
		Geography.Regions.Africa.Southern Africa     0.484
		Geography.Regions.Africa.Western Africa      0.469
		Geography.Regions.Americas.Central America   0.307
		Geography.Regions.Americas.North America     0.705
		Geography.Regions.Americas.South America     0.484
		Geography.Regions.Asia.Asia*                 0.746
		Geography.Regions.Asia.Central Asia          0.392
		Geography.Regions.Asia.East Asia             0.603
		Geography.Regions.Asia.North Asia            0.189
		Geography.Regions.Asia.South Asia            0.854
		Geography.Regions.Asia.Southeast Asia        0.576
		Geography.Regions.Asia.West Asia             0.744
		Geography.Regions.Europe.Eastern Europe      0.627
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.574
		Geography.Regions.Europe.Southern Europe     0.516
		Geography.Regions.Europe.Western Europe      0.583
		Geography.Regions.Oceania                    0.794
		History and Society.Business and economics   0.316
		History and Society.Education                0.411
		History and Society.History                  0.229
		History and Society.Military and warfare     0.651
		History and Society.Politics and government  0.571
		History and Society.Society                  0.227
		History and Society.Transportation           0.834
		STEM.Biology                                 0.881
		STEM.Chemistry                               0.372
		STEM.Computing                               0.214
		STEM.Earth and environment                   0.547
		STEM.Engineering                             0.607
		STEM.Libraries & Information                 0.32
		STEM.Mathematics                             0.123
		STEM.Medicine & Health                       0.556
		STEM.Physics                                 0.204
		STEM.STEM*                                   0.843
		STEM.Space                                   0.9
		STEM.Technology                              0.251
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}}

