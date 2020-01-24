Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'min_weight_fraction_leaf': 0.0, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'loss': 'deviance', 'n_estimators': 150, 'max_features': 'log2', 'label_weights': {}, 'warm_start': False, 'validation_fraction': 0.1, 'init': None, 'scale': False, 'random_state': None, 'presort': 'auto', 'tol': 0.0001, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'max_depth': 5, 'min_samples_split': 2, 'subsample': 1.0, 'multilabel': True, 'criterion': 'friedman_mse', 'center': False, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'population_rates': None, 'verbose': 0}
	Environment:
	 - revscoring_version: '2.6.4-mmap'
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
	counts (n=60036):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 16215  -->  13718  2497  1358  42463
			'Culture.Biography.Women'                       4019  -->   2873  1146   784  55233
			'Culture.Food and drink'                        1229  -->    817   412    82  58725
			'Culture.Internet culture'                      2685  -->   1992   693   207  57144
			'Culture.Linguistics'                           1169  -->    749   420    75  58792
			'Culture.Literature'                            5060  -->   3427  1633   584  54392
			'Culture.Media.Books'                           1770  -->   1112   658   217  58049
			'Culture.Media.Entertainment'                   1661  -->    682   979   180  58195
			'Culture.Media.Films'                           2185  -->   1679   506   187  57664
			'Culture.Media.Media*'                         13423  -->  11050  2373  1632  44981
			'Culture.Media.Music'                           2499  -->   1922   577   302  57235
			'Culture.Media.Radio'                           1105  -->    838   267    43  58888
			'Culture.Media.Software'                        1665  -->    910   755   357  58014
			'Culture.Media.Television'                      2032  -->   1310   722   235  57769
			'Culture.Media.Video games'                     1899  -->   1633   266    76  58061
			'Culture.Performing arts'                       1270  -->    783   487   116  58650
			'Culture.Philosophy and religion'               2492  -->   1243  1249   342  57202
			'Culture.Sports'                                5757  -->   5149   608   339  53940
			'Culture.Visual arts.Architecture'              2428  -->   1652   776   292  57316
			'Culture.Visual arts.Comics and Anime'          1448  -->   1055   393   132  58456
			'Culture.Visual arts.Fashion'                   1115  -->    735   380    74  58847
			'Culture.Visual arts.Visual arts*'              5706  -->   4031  1675   591  53739
			'Geography.Geographical'                        3402  -->   2222  1180   304  56330
			'Geography.Regions.Africa.Africa*'              5506  -->   4516   990   260  54270
			'Geography.Regions.Africa.Central Africa'         65  -->      3    62    91  59880
			'Geography.Regions.Africa.Eastern Africa'       1085  -->    826   259    31  58920
			'Geography.Regions.Africa.Northern Africa'      1267  -->    879   388    97  58672
			'Geography.Regions.Africa.Southern Africa'      1215  -->    858   357    52  58769
			'Geography.Regions.Africa.Western Africa'       1110  -->    860   250    71  58855
			'Geography.Regions.Americas.Central America'    1243  -->    747   496    74  58719
			'Geography.Regions.Americas.North America'      7148  -->   4530  2618  1097  51791
			'Geography.Regions.Americas.South America'      1497  -->   1024   473   130  58409
			'Geography.Regions.Asia.Asia*'                 10670  -->   8777  1893   878  48488
			'Geography.Regions.Asia.Central Asia'           1082  -->    795   287    61  58893
			'Geography.Regions.Asia.East Asia'              2586  -->   1860   726   263  57187
			'Geography.Regions.Asia.North Asia'             1337  -->    814   523   177  58522
			'Geography.Regions.Asia.South Asia'             2325  -->   1868   457   127  57584
			'Geography.Regions.Asia.Southeast Asia'         1610  -->   1167   443   103  58323
			'Geography.Regions.Asia.West Asia'              2198  -->   1645   553   138  57700
			'Geography.Regions.Europe.Eastern Europe'       2992  -->   2195   797   265  56779
			'Geography.Regions.Europe.Europe*'             12062  -->   8764  3298  1820  46154
			'Geography.Regions.Europe.Northern Europe'      4062  -->   2537  1525   640  55334
			'Geography.Regions.Europe.Southern Europe'      2316  -->   1481   835   274  57446
			'Geography.Regions.Europe.Western Europe'       3064  -->   1890  1174   393  56579
			'Geography.Regions.Oceania'                     2478  -->   1864   614   130  57428
			'History and Society.Business and economics'    3356  -->   1396  1960   523  56157
			'History and Society.Education'                 2059  -->    948  1111   261  57716
			'History and Society.History'                   3138  -->   1213  1925   470  56428
			'History and Society.Military and warfare'      3829  -->   2544  1285   423  55784
			'History and Society.Politics and government'   4372  -->   2498  1874   472  55192
			'History and Society.Society'                   3804  -->   1282  2522   335  55897
			'History and Society.Transportation'            3427  -->   2810   617   258  56351
			'STEM.Biology'                                  2702  -->   2148   554   127  57207
			'STEM.Chemistry'                                1241  -->    805   436   150  58645
			'STEM.Computing'                                1916  -->   1218   698   423  57697
			'STEM.Earth and environment'                    1542  -->   1020   522   109  58385
			'STEM.Engineering'                              2164  -->   1501   663   188  57684
			'STEM.Libraries & Information'                  1105  -->    595   510    78  58853
			'STEM.Mathematics'                              1077  -->    719   358    81  58878
			'STEM.Medicine & Health'                        1637  -->   1017   620   186  58213
			'STEM.Physics'                                  1152  -->    706   446   159  58725
			'STEM.STEM*'                                   15499  -->  13080  2419  1092  43445
			'STEM.Space'                                    1321  -->   1097   224    67  58648
			'STEM.Technology'                               3389  -->   1967  1422   643  56004
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.27          0.123
		Culture.Biography.Women                         0.067         0.015
		Culture.Food and drink                          0.02          0.002
		Culture.Internet culture                        0.045         0.004
		Culture.Linguistics                             0.019         0.007
		Culture.Literature                              0.084         0.016
		Culture.Media.Books                             0.029         0.004
		Culture.Media.Entertainment                     0.028         0.004
		Culture.Media.Films                             0.036         0.011
		Culture.Media.Media*                            0.224         0.059
		Culture.Media.Music                             0.042         0.024
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.028         0.001
		Culture.Media.Television                        0.034         0.009
		Culture.Media.Video games                       0.032         0.003
		Culture.Performing arts                         0.021         0.003
		Culture.Philosophy and religion                 0.042         0.011
		Culture.Sports                                  0.096         0.071
		Culture.Visual arts.Architecture                0.04          0.011
		Culture.Visual arts.Comics and Anime            0.024         0.002
		Culture.Visual arts.Fashion                     0.019         0.001
		Culture.Visual arts.Visual arts*                0.095         0.018
		Geography.Geographical                          0.057         0.024
		Geography.Regions.Africa.Africa*                0.092         0.008
		Geography.Regions.Africa.Central Africa         0.001         0
		Geography.Regions.Africa.Eastern Africa         0.018         0
		Geography.Regions.Africa.Northern Africa        0.021         0.001
		Geography.Regions.Africa.Southern Africa        0.02          0.001
		Geography.Regions.Africa.Western Africa         0.018         0.001
		Geography.Regions.Americas.Central America      0.021         0.003
		Geography.Regions.Americas.North America        0.119         0.064
		Geography.Regions.Americas.South America        0.025         0.006
		Geography.Regions.Asia.Asia*                    0.178         0.046
		Geography.Regions.Asia.Central Asia             0.018         0.001
		Geography.Regions.Asia.East Asia                0.043         0.011
		Geography.Regions.Asia.North Asia               0.022         0.001
		Geography.Regions.Asia.South Asia               0.039         0.015
		Geography.Regions.Asia.Southeast Asia           0.027         0.006
		Geography.Regions.Asia.West Asia                0.037         0.011
		Geography.Regions.Europe.Eastern Europe         0.05          0.013
		Geography.Regions.Europe.Europe*                0.201         0.076
		Geography.Regions.Europe.Northern Europe        0.068         0.031
		Geography.Regions.Europe.Southern Europe        0.039         0.013
		Geography.Regions.Europe.Western Europe         0.051         0.019
		Geography.Regions.Oceania                       0.041         0.015
		History and Society.Business and economics      0.056         0.01
		History and Society.Education                   0.034         0.007
		History and Society.History                     0.052         0.011
		History and Society.Military and warfare        0.064         0.014
		History and Society.Politics and government     0.073         0.028
		History and Society.Society                     0.063         0.013
		History and Society.Transportation              0.057         0.015
		STEM.Biology                                    0.045         0.034
		STEM.Chemistry                                  0.021         0.002
		STEM.Computing                                  0.032         0.003
		STEM.Earth and environment                      0.026         0.005
		STEM.Engineering                                0.036         0.005
		STEM.Libraries & Information                    0.018         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.027         0.006
		STEM.Physics                                    0.019         0.001
		STEM.STEM*                                      0.258         0.069
		STEM.Space                                      0.022         0.006
		STEM.Technology                                 0.056         0.005
	match_rate (micro=0.053, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.131
		Culture.Biography.Women                      0.024
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.006
		Culture.Linguistics                          0.006
		Culture.Literature                           0.021
		Culture.Media.Books                          0.006
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.081
		Culture.Media.Music                          0.024
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.007
		Culture.Media.Television                     0.01
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.07
		Culture.Visual arts.Architecture             0.012
		Culture.Visual arts.Comics and Anime         0.004
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.024
		Geography.Geographical                       0.021
		Geography.Regions.Africa.Africa*             0.011
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.002
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.06
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.054
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.09
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.013
		Geography.Regions.Europe.Western Europe      0.019
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.008
		History and Society.History                  0.012
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.024
		History and Society.Society                  0.01
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.009
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.002
		STEM.Medicine & Health                       0.007
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.081
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.947, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.869
		Culture.Biography.Women                      0.976
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.994
		Culture.Linguistics                          0.994
		Culture.Literature                           0.979
		Culture.Media.Books                          0.994
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.919
		Culture.Media.Music                          0.976
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.99
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.93
		Culture.Visual arts.Architecture             0.988
		Culture.Visual arts.Comics and Anime         0.996
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.976
		Geography.Geographical                       0.979
		Geography.Regions.Africa.Africa*             0.989
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.998
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.94
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.946
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.91
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.987
		Geography.Regions.Europe.Western Europe      0.981
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.992
		History and Society.History                  0.988
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.976
		History and Society.Society                  0.99
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.991
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.919
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.736, macro=0.667):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.846
		Culture.Biography.Women                      0.715
		Culture.Food and drink                       0.665
		Culture.Internet culture                     0.742
		Culture.Linguistics                          0.641
		Culture.Literature                           0.677
		Culture.Media.Books                          0.628
		Culture.Media.Entertainment                  0.411
		Culture.Media.Films                          0.768
		Culture.Media.Media*                         0.823
		Culture.Media.Music                          0.769
		Culture.Media.Radio                          0.758
		Culture.Media.Software                       0.547
		Culture.Media.Television                     0.645
		Culture.Media.Video games                    0.86
		Culture.Performing arts                      0.617
		Culture.Philosophy and religion              0.499
		Culture.Sports                               0.894
		Culture.Visual arts.Architecture             0.68
		Culture.Visual arts.Comics and Anime         0.729
		Culture.Visual arts.Fashion                  0.659
		Culture.Visual arts.Visual arts*             0.706
		Geography.Geographical                       0.653
		Geography.Regions.Africa.Africa*             0.82
		Geography.Regions.Africa.Central Africa      0.046
		Geography.Regions.Africa.Eastern Africa      0.761
		Geography.Regions.Africa.Northern Africa     0.694
		Geography.Regions.Africa.Southern Africa     0.706
		Geography.Regions.Africa.Western Africa      0.775
		Geography.Regions.Americas.Central America   0.601
		Geography.Regions.Americas.North America     0.634
		Geography.Regions.Americas.South America     0.684
		Geography.Regions.Asia.Asia*                 0.823
		Geography.Regions.Asia.Central Asia          0.735
		Geography.Regions.Asia.East Asia             0.719
		Geography.Regions.Asia.North Asia            0.609
		Geography.Regions.Asia.South Asia            0.803
		Geography.Regions.Asia.Southeast Asia        0.725
		Geography.Regions.Asia.West Asia             0.748
		Geography.Regions.Europe.Eastern Europe      0.734
		Geography.Regions.Europe.Europe*             0.727
		Geography.Regions.Europe.Northern Europe     0.625
		Geography.Regions.Europe.Southern Europe     0.639
		Geography.Regions.Europe.Western Europe      0.617
		Geography.Regions.Oceania                    0.752
		History and Society.Business and economics   0.416
		History and Society.Education                0.46
		History and Society.History                  0.387
		History and Society.Military and warfare     0.664
		History and Society.Politics and government  0.571
		History and Society.Society                  0.337
		History and Society.Transportation           0.82
		STEM.Biology                                 0.795
		STEM.Chemistry                               0.649
		STEM.Computing                               0.636
		STEM.Earth and environment                   0.661
		STEM.Engineering                             0.694
		STEM.Libraries & Information                 0.538
		STEM.Mathematics                             0.668
		STEM.Medicine & Health                       0.621
		STEM.Physics                                 0.613
		STEM.STEM*                                   0.844
		STEM.Space                                   0.83
		STEM.Technology                              0.58
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.986
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.999
		Culture.Literature                           0.989
		Culture.Media.Books                          0.996
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.965
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.994
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
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.979
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.991
		History and Society.Education                0.995
		History and Society.History                  0.992
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.995
		STEM.Biology                                 0.998
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.678, macro=0.53):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.793
		Culture.Biography.Women                      0.43
		Culture.Food and drink                       0.541
		Culture.Internet culture                     0.419
		Culture.Linguistics                          0.788
		Culture.Literature                           0.501
		Culture.Media.Books                          0.406
		Culture.Media.Entertainment                  0.324
		Culture.Media.Films                          0.717
		Culture.Media.Media*                         0.594
		Culture.Media.Music                          0.782
		Culture.Media.Radio                          0.692
		Culture.Media.Software                       0.106
		Culture.Media.Television                     0.586
		Culture.Media.Video games                    0.633
		Culture.Performing arts                      0.475
		Culture.Philosophy and religion              0.475
		Culture.Sports                               0.917
		Culture.Visual arts.Architecture             0.589
		Culture.Visual arts.Comics and Anime         0.416
		Culture.Visual arts.Fashion                  0.298
		Culture.Visual arts.Visual arts*             0.548
		Geography.Geographical                       0.746
		Geography.Regions.Africa.Africa*             0.575
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.397
		Geography.Regions.Africa.Northern Africa     0.341
		Geography.Regions.Africa.Southern Africa     0.485
		Geography.Regions.Africa.Western Africa      0.306
		Geography.Regions.Americas.Central America   0.613
		Geography.Regions.Americas.North America     0.677
		Geography.Regions.Americas.South America     0.662
		Geography.Regions.Asia.Asia*                 0.688
		Geography.Regions.Asia.Central Asia          0.381
		Geography.Regions.Asia.East Asia             0.645
		Geography.Regions.Asia.North Asia            0.157
		Geography.Regions.Asia.South Asia            0.849
		Geography.Regions.Asia.Southeast Asia        0.713
		Geography.Regions.Asia.West Asia             0.776
		Geography.Regions.Europe.Eastern Europe      0.673
		Geography.Regions.Europe.Europe*             0.612
		Geography.Regions.Europe.Northern Europe     0.633
		Geography.Regions.Europe.Southern Europe     0.64
		Geography.Regions.Europe.Western Europe      0.636
		Geography.Regions.Oceania                    0.836
		History and Society.Business and economics   0.315
		History and Society.Education                0.431
		History and Society.History                  0.339
		History and Society.Military and warfare     0.558
		History and Society.Politics and government  0.662
		History and Society.Society                  0.42
		History and Society.Transportation           0.734
		STEM.Biology                                 0.926
		STEM.Chemistry                               0.284
		STEM.Computing                               0.191
		STEM.Earth and environment                   0.618
		STEM.Engineering                             0.529
		STEM.Libraries & Information                 0.202
		STEM.Mathematics                             0.169
		STEM.Medicine & Health                       0.557
		STEM.Physics                                 0.162
		STEM.STEM*                                   0.719
		STEM.Space                                   0.815
		STEM.Technology                              0.209
		-------------------------------------------  -----
	!precision (micro=0.989, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.999
		Culture.Media.Television                     0.997
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.992
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.975
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.991
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.977
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.988
		History and Society.Society                  0.992
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.988
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.701, macro=0.573):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.819
		Culture.Biography.Women                      0.537
		Culture.Food and drink                       0.596
		Culture.Internet culture                     0.536
		Culture.Linguistics                          0.707
		Culture.Literature                           0.576
		Culture.Media.Books                          0.493
		Culture.Media.Entertainment                  0.362
		Culture.Media.Films                          0.742
		Culture.Media.Media*                         0.69
		Culture.Media.Music                          0.776
		Culture.Media.Radio                          0.724
		Culture.Media.Software                       0.178
		Culture.Media.Television                     0.614
		Culture.Media.Video games                    0.729
		Culture.Performing arts                      0.537
		Culture.Philosophy and religion              0.486
		Culture.Sports                               0.905
		Culture.Visual arts.Architecture             0.632
		Culture.Visual arts.Comics and Anime         0.53
		Culture.Visual arts.Fashion                  0.411
		Culture.Visual arts.Visual arts*             0.617
		Geography.Geographical                       0.697
		Geography.Regions.Africa.Africa*             0.676
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.522
		Geography.Regions.Africa.Northern Africa     0.457
		Geography.Regions.Africa.Southern Africa     0.575
		Geography.Regions.Africa.Western Africa      0.438
		Geography.Regions.Americas.Central America   0.607
		Geography.Regions.Americas.North America     0.655
		Geography.Regions.Americas.South America     0.673
		Geography.Regions.Asia.Asia*                 0.749
		Geography.Regions.Asia.Central Asia          0.502
		Geography.Regions.Asia.East Asia             0.68
		Geography.Regions.Asia.North Asia            0.25
		Geography.Regions.Asia.South Asia            0.826
		Geography.Regions.Asia.Southeast Asia        0.719
		Geography.Regions.Asia.West Asia             0.762
		Geography.Regions.Europe.Eastern Europe      0.702
		Geography.Regions.Europe.Europe*             0.665
		Geography.Regions.Europe.Northern Europe     0.629
		Geography.Regions.Europe.Southern Europe     0.64
		Geography.Regions.Europe.Western Europe      0.626
		Geography.Regions.Oceania                    0.792
		History and Society.Business and economics   0.358
		History and Society.Education                0.445
		History and Society.History                  0.361
		History and Society.Military and warfare     0.606
		History and Society.Politics and government  0.613
		History and Society.Society                  0.374
		History and Society.Transportation           0.774
		STEM.Biology                                 0.855
		STEM.Chemistry                               0.395
		STEM.Computing                               0.293
		STEM.Earth and environment                   0.639
		STEM.Engineering                             0.6
		STEM.Libraries & Information                 0.294
		STEM.Mathematics                             0.269
		STEM.Medicine & Health                       0.587
		STEM.Physics                                 0.256
		STEM.STEM*                                   0.776
		STEM.Space                                   0.823
		STEM.Technology                              0.307
		-------------------------------------------  -----
	!f1 (micro=0.986, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.974
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.992
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.997
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.997
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.988
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.992
		History and Society.Education                0.996
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.99
		History and Society.Society                  0.993
		History and Society.Transportation           0.996
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.998
		STEM.Computing                               0.996
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.982
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.975, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.954
		Culture.Biography.Women                      0.982
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.996
		Culture.Literature                           0.985
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.994
		Culture.Media.Media*                         0.957
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.993
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.998
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.992
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.984
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.998
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.957
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.992
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.977
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.985
		History and Society.Education                0.992
		History and Society.History                  0.985
		History and Society.Military and warfare     0.988
		History and Society.Politics and government  0.98
		History and Society.Society                  0.986
		History and Society.Transportation           0.993
		STEM.Biology                                 0.991
		STEM.Chemistry                               0.997
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.998
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.966
		STEM.Space                                   0.998
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.031
		Culture.Biography.Women                      0.014
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.001
		Culture.Literature                           0.011
		Culture.Media.Books                          0.004
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.003
		Culture.Media.Media*                         0.035
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.001
		Culture.Media.Software                       0.006
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
		Geography.Regions.Africa.Central Africa      0.002
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.021
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.005
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.002
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.002
		Geography.Regions.Europe.Eastern Europe      0.005
		Geography.Regions.Europe.Europe*             0.038
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.009
		History and Society.Education                0.005
		History and Society.History                  0.008
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.008
		History and Society.Society                  0.006
		History and Society.Transportation           0.005
		STEM.Biology                                 0.002
		STEM.Chemistry                               0.003
		STEM.Computing                               0.007
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.968, macro=0.968):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.969
		Culture.Biography.Women                      0.974
		Culture.Food and drink                       0.975
		Culture.Internet culture                     0.981
		Culture.Linguistics                          0.975
		Culture.Literature                           0.971
		Culture.Media.Books                          0.976
		Culture.Media.Entertainment                  0.962
		Culture.Media.Films                          0.981
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.982
		Culture.Media.Radio                          0.987
		Culture.Media.Software                       0.977
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.989
		Culture.Performing arts                      0.976
		Culture.Philosophy and religion              0.953
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.975
		Culture.Visual arts.Comics and Anime         0.982
		Culture.Visual arts.Fashion                  0.977
		Culture.Visual arts.Visual arts*             0.965
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.979
		Geography.Regions.Africa.Central Africa      0.686
		Geography.Regions.Africa.Eastern Africa      0.982
		Geography.Regions.Africa.Northern Africa     0.972
		Geography.Regions.Africa.Southern Africa     0.98
		Geography.Regions.Africa.Western Africa      0.986
		Geography.Regions.Americas.Central America   0.975
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.982
		Geography.Regions.Asia.Asia*                 0.974
		Geography.Regions.Asia.Central Asia          0.982
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.977
		Geography.Regions.Asia.South Asia            0.983
		Geography.Regions.Asia.Southeast Asia        0.976
		Geography.Regions.Asia.West Asia             0.98
		Geography.Regions.Europe.Eastern Europe      0.978
		Geography.Regions.Europe.Europe*             0.952
		Geography.Regions.Europe.Northern Europe     0.962
		Geography.Regions.Europe.Southern Europe     0.971
		Geography.Regions.Europe.Western Europe      0.965
		Geography.Regions.Oceania                    0.975
		History and Society.Business and economics   0.943
		History and Society.Education                0.955
		History and Society.History                  0.937
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.949
		History and Society.Society                  0.911
		History and Society.Transportation           0.984
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.979
		STEM.Computing                               0.983
		STEM.Earth and environment                   0.975
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.979
		STEM.Medicine & Health                       0.972
		STEM.Physics                                 0.979
		STEM.STEM*                                   0.971
		STEM.Space                                   0.989
		STEM.Technology                              0.966
		-------------------------------------------  -----
	pr_auc (micro=0.737, macro=0.578):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.886
		Culture.Biography.Women                      0.494
		Culture.Food and drink                       0.548
		Culture.Internet culture                     0.671
		Culture.Linguistics                          0.747
		Culture.Literature                           0.624
		Culture.Media.Books                          0.426
		Culture.Media.Entertainment                  0.32
		Culture.Media.Films                          0.728
		Culture.Media.Media*                         0.788
		Culture.Media.Music                          0.795
		Culture.Media.Radio                          0.743
		Culture.Media.Software                       0.132
		Culture.Media.Television                     0.6
		Culture.Media.Video games                    0.799
		Culture.Performing arts                      0.531
		Culture.Philosophy and religion              0.406
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.661
		Culture.Visual arts.Comics and Anime         0.497
		Culture.Visual arts.Fashion                  0.399
		Culture.Visual arts.Visual arts*             0.652
		Geography.Geographical                       0.741
		Geography.Regions.Africa.Africa*             0.689
		Geography.Regions.Africa.Central Africa      0
		Geography.Regions.Africa.Eastern Africa      0.495
		Geography.Regions.Africa.Northern Africa     0.439
		Geography.Regions.Africa.Southern Africa     0.494
		Geography.Regions.Africa.Western Africa      0.377
		Geography.Regions.Americas.Central America   0.534
		Geography.Regions.Americas.North America     0.724
		Geography.Regions.Americas.South America     0.651
		Geography.Regions.Asia.Asia*                 0.798
		Geography.Regions.Asia.Central Asia          0.532
		Geography.Regions.Asia.East Asia             0.669
		Geography.Regions.Asia.North Asia            0.213
		Geography.Regions.Asia.South Asia            0.843
		Geography.Regions.Asia.Southeast Asia        0.721
		Geography.Regions.Asia.West Asia             0.8
		Geography.Regions.Europe.Eastern Europe      0.731
		Geography.Regions.Europe.Europe*             0.713
		Geography.Regions.Europe.Northern Europe     0.674
		Geography.Regions.Europe.Southern Europe     0.663
		Geography.Regions.Europe.Western Europe      0.623
		Geography.Regions.Oceania                    0.812
		History and Society.Business and economics   0.277
		History and Society.Education                0.366
		History and Society.History                  0.299
		History and Society.Military and warfare     0.624
		History and Society.Politics and government  0.65
		History and Society.Society                  0.339
		History and Society.Transportation           0.819
		STEM.Biology                                 0.893
		STEM.Chemistry                               0.386
		STEM.Computing                               0.243
		STEM.Earth and environment                   0.651
		STEM.Engineering                             0.6
		STEM.Libraries & Information                 0.332
		STEM.Mathematics                             0.294
		STEM.Medicine & Health                       0.604
		STEM.Physics                                 0.306
		STEM.STEM*                                   0.861
		STEM.Space                                   0.862
		STEM.Technology                              0.283
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'items': {'type': 'string'}, 'description': 'The most likely labels predicted by the estimator', 'type': 'array'}}, 'type': 'object'}

