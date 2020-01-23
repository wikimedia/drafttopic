Model Information:
	 - type: GradientBoosting
	 - version: 1.1.0
	 - params: {'criterion': 'friedman_mse', 'init': None, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'multilabel': True, 'max_leaf_nodes': None, 'tol': 0.0001, 'subsample': 1.0, 'max_features': 'log2', 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'verbose': 0, 'scale': False, 'random_state': None, 'center': False, 'learning_rate': 0.1, 'label_weights': {}, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'validation_fraction': 0.1, 'max_depth': 5, 'presort': 'auto', 'loss': 'deviance', 'warm_start': False, 'population_rates': None}
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
	counts (n=62581):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 26810  -->  25647  1163  1202  34569
			'Culture.Biography.Women'                       6237  -->   4592  1645   753  55591
			'Culture.Food and drink'                        1408  -->    981   427    83  61090
			'Culture.Internet culture'                      3358  -->   2723   635   201  59022
			'Culture.Linguistics'                           1442  -->    918   524    67  61072
			'Culture.Literature'                            5798  -->   4266  1532   496  56287
			'Culture.Media.Books'                           1580  -->   1182   398    99  60902
			'Culture.Media.Entertainment'                   2139  -->    997  1142   223  60219
			'Culture.Media.Films'                           2079  -->   1632   447    79  60423
			'Culture.Media.Media*'                         13978  -->  11607  2371  1513  47090
			'Culture.Media.Music'                           2737  -->   2038   699   309  59535
			'Culture.Media.Radio'                           1146  -->    572   574    95  61340
			'Culture.Media.Software'                        2066  -->   1561   505   288  60227
			'Culture.Media.Television'                      2313  -->   1369   944   213  60055
			'Culture.Media.Video games'                     2164  -->   1903   261    43  60374
			'Culture.Performing arts'                       1486  -->    745   741   151  60944
			'Culture.Philosophy and religion'               3384  -->   1675  1709   281  58916
			'Culture.Sports'                                8294  -->   7532   762   354  53933
			'Culture.Visual arts.Architecture'              1832  -->   1229   603   169  60580
			'Culture.Visual arts.Comics and Anime'          1858  -->   1500   358    94  60629
			'Culture.Visual arts.Fashion'                   1345  -->    987   358    84  61152
			'Culture.Visual arts.Visual arts*'              5949  -->   4234  1715   416  56216
			'Geography.Geographical'                        3588  -->   2563  1025   361  58632
			'Geography.Regions.Africa.Africa*'              5725  -->   4743   982   338  56518
			'Geography.Regions.Africa.Central Africa'         36  -->      7    29    34  62511
			'Geography.Regions.Africa.Eastern Africa'        976  -->    741   235    33  61572
			'Geography.Regions.Africa.Northern Africa'      2029  -->   1562   467   226  60326
			'Geography.Regions.Africa.Southern Africa'      1189  -->    957   232    65  61327
			'Geography.Regions.Africa.Western Africa'        746  -->    586   160    36  61799
			'Geography.Regions.Americas.Central America'    1346  -->    887   459    73  61162
			'Geography.Regions.Americas.North America'      8393  -->   5670  2723  2038  52150
			'Geography.Regions.Americas.South America'      1645  -->   1243   402   119  60817
			'Geography.Regions.Asia.Asia*'                 11997  -->   9976  2021   914  49670
			'Geography.Regions.Asia.Central Asia'           1204  -->    928   276    86  61291
			'Geography.Regions.Asia.East Asia'              2827  -->   2075   752   221  59533
			'Geography.Regions.Asia.North Asia'             1548  -->   1096   452   214  60819
			'Geography.Regions.Asia.South Asia'             1907  -->   1480   427    60  60614
			'Geography.Regions.Asia.Southeast Asia'         1578  -->   1166   412    60  60943
			'Geography.Regions.Asia.West Asia'              4119  -->   3337   782   294  58168
			'Geography.Regions.Europe.Eastern Europe'       2943  -->   2167   776   268  59370
			'Geography.Regions.Europe.Europe*'             13073  -->  10254  2819  1842  47666
			'Geography.Regions.Europe.Northern Europe'      4032  -->   2654  1378   622  57927
			'Geography.Regions.Europe.Southern Europe'      2835  -->   2085   750   313  59433
			'Geography.Regions.Europe.Western Europe'       4056  -->   2981  1075   459  58066
			'Geography.Regions.Oceania'                     2248  -->   1859   389    64  60269
			'History and Society.Business and economics'    3607  -->   1932  1675   419  58555
			'History and Society.Education'                 1992  -->    838  1154   187  60402
			'History and Society.History'                   4707  -->   2228  2479   625  57249
			'History and Society.Military and warfare'      4826  -->   3279  1547   472  57283
			'History and Society.Politics and government'   5550  -->   3391  2159   644  56387
			'History and Society.Society'                   6013  -->   2478  3535   556  56012
			'History and Society.Transportation'            3287  -->   2817   470   145  59149
			'STEM.Biology'                                  2900  -->   2238   662   164  59517
			'STEM.Chemistry'                                1480  -->   1106   374   143  60958
			'STEM.Computing'                                2424  -->   1902   522   347  59810
			'STEM.Earth and environment'                    1704  -->   1118   586   163  60714
			'STEM.Engineering'                              2964  -->   2154   810   242  59375
			'STEM.Libraries & Information'                  1203  -->    796   407    60  61318
			'STEM.Mathematics'                              1172  -->    904   268    61  61348
			'STEM.Medicine & Health'                        2281  -->   1635   646   205  60095
			'STEM.Physics'                                  1560  -->   1095   465   165  60856
			'STEM.STEM*'                                   17878  -->  15602  2276  1021  43682
			'STEM.Space'                                    1746  -->   1573   173    56  60779
			'STEM.Technology'                               4511  -->   3208  1303   609  57461
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
		Culture.Biography.Biography*                 0.147
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
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.003
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.01
		Culture.Sports                               0.071
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.02
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.012
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.079
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.055
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.012
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.013
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.014
		Geography.Regions.Europe.Europe*             0.094
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.015
		Geography.Regions.Europe.Western Europe      0.022
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.012
		History and Society.Education                0.006
		History and Society.History                  0.016
		History and Society.Military and warfare     0.018
		History and Society.Politics and government  0.028
		History and Society.Society                  0.015
		History and Society.Transportation           0.015
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.082
		STEM.Space                                   0.006
		STEM.Technology                              0.014
		-------------------------------------------  -----
	filter_rate (micro=0.944, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.853
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
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.997
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.929
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.98
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.988
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.921
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.945
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.988
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.987
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.986
		Geography.Regions.Europe.Europe*             0.906
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.985
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.988
		History and Society.Education                0.994
		History and Society.History                  0.984
		History and Society.Military and warfare     0.982
		History and Society.Politics and government  0.972
		History and Society.Society                  0.985
		History and Society.Transportation           0.985
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.918
		STEM.Space                                   0.994
		STEM.Technology                              0.986
		-------------------------------------------  -----
	recall (micro=0.777, macro=0.711):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.957
		Culture.Biography.Women                      0.736
		Culture.Food and drink                       0.697
		Culture.Internet culture                     0.811
		Culture.Linguistics                          0.637
		Culture.Literature                           0.736
		Culture.Media.Books                          0.748
		Culture.Media.Entertainment                  0.466
		Culture.Media.Films                          0.785
		Culture.Media.Media*                         0.83
		Culture.Media.Music                          0.745
		Culture.Media.Radio                          0.499
		Culture.Media.Software                       0.756
		Culture.Media.Television                     0.592
		Culture.Media.Video games                    0.879
		Culture.Performing arts                      0.501
		Culture.Philosophy and religion              0.495
		Culture.Sports                               0.908
		Culture.Visual arts.Architecture             0.671
		Culture.Visual arts.Comics and Anime         0.807
		Culture.Visual arts.Fashion                  0.734
		Culture.Visual arts.Visual arts*             0.712
		Geography.Geographical                       0.714
		Geography.Regions.Africa.Africa*             0.828
		Geography.Regions.Africa.Central Africa      0.194
		Geography.Regions.Africa.Eastern Africa      0.759
		Geography.Regions.Africa.Northern Africa     0.77
		Geography.Regions.Africa.Southern Africa     0.805
		Geography.Regions.Africa.Western Africa      0.786
		Geography.Regions.Americas.Central America   0.659
		Geography.Regions.Americas.North America     0.676
		Geography.Regions.Americas.South America     0.756
		Geography.Regions.Asia.Asia*                 0.832
		Geography.Regions.Asia.Central Asia          0.771
		Geography.Regions.Asia.East Asia             0.734
		Geography.Regions.Asia.North Asia            0.708
		Geography.Regions.Asia.South Asia            0.776
		Geography.Regions.Asia.Southeast Asia        0.739
		Geography.Regions.Asia.West Asia             0.81
		Geography.Regions.Europe.Eastern Europe      0.736
		Geography.Regions.Europe.Europe*             0.784
		Geography.Regions.Europe.Northern Europe     0.658
		Geography.Regions.Europe.Southern Europe     0.735
		Geography.Regions.Europe.Western Europe      0.735
		Geography.Regions.Oceania                    0.827
		History and Society.Business and economics   0.536
		History and Society.Education                0.421
		History and Society.History                  0.473
		History and Society.Military and warfare     0.679
		History and Society.Politics and government  0.611
		History and Society.Society                  0.412
		History and Society.Transportation           0.857
		STEM.Biology                                 0.772
		STEM.Chemistry                               0.747
		STEM.Computing                               0.785
		STEM.Earth and environment                   0.656
		STEM.Engineering                             0.727
		STEM.Libraries & Information                 0.662
		STEM.Mathematics                             0.771
		STEM.Medicine & Health                       0.717
		STEM.Physics                                 0.702
		STEM.STEM*                                   0.873
		STEM.Space                                   0.901
		STEM.Technology                              0.711
		-------------------------------------------  -----
	!recall (micro=0.983, macro=0.994):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.966
		Culture.Biography.Women                      0.987
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.999
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.996
		Culture.Media.Films                          0.999
		Culture.Media.Media*                         0.969
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.994
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.962
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.963
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.995
		Geography.Regions.Europe.Western Europe      0.992
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.993
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.99
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.977
		STEM.Space                                   0.999
		STEM.Technology                              0.99
		-------------------------------------------  -----
	precision (micro=0.687, macro=0.551):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.8
		Culture.Biography.Women                      0.449
		Culture.Food and drink                       0.559
		Culture.Internet culture                     0.456
		Culture.Linguistics                          0.811
		Culture.Literature                           0.57
		Culture.Media.Books                          0.651
		Culture.Media.Entertainment                  0.312
		Culture.Media.Films                          0.865
		Culture.Media.Media*                         0.624
		Culture.Media.Music                          0.779
		Culture.Media.Radio                          0.411
		Culture.Media.Software                       0.174
		Culture.Media.Television                     0.598
		Culture.Media.Video games                    0.764
		Culture.Performing arts                      0.37
		Culture.Philosophy and religion              0.529
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.72
		Culture.Visual arts.Comics and Anime         0.535
		Culture.Visual arts.Fashion                  0.302
		Culture.Visual arts.Visual arts*             0.644
		Geography.Geographical                       0.738
		Geography.Regions.Africa.Africa*             0.523
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.392
		Geography.Regions.Africa.Northern Africa     0.202
		Geography.Regions.Africa.Southern Africa     0.472
		Geography.Regions.Africa.Western Africa      0.48
		Geography.Regions.Americas.Central America   0.647
		Geography.Regions.Americas.North America     0.552
		Geography.Regions.Americas.South America     0.711
		Geography.Regions.Asia.Asia*                 0.687
		Geography.Regions.Asia.Central Asia          0.323
		Geography.Regions.Asia.East Asia             0.696
		Geography.Regions.Asia.North Asia            0.157
		Geography.Regions.Asia.South Asia            0.924
		Geography.Regions.Asia.Southeast Asia        0.82
		Geography.Regions.Asia.West Asia             0.64
		Geography.Regions.Europe.Eastern Europe      0.681
		Geography.Regions.Europe.Europe*             0.635
		Geography.Regions.Europe.Northern Europe     0.662
		Geography.Regions.Europe.Southern Europe     0.65
		Geography.Regions.Europe.Western Europe      0.647
		Geography.Regions.Oceania                    0.923
		History and Society.Business and economics   0.435
		History and Society.Education                0.503
		History and Society.History                  0.325
		History and Society.Military and warfare     0.543
		History and Society.Politics and government  0.611
		History and Society.Society                  0.349
		History and Society.Transportation           0.843
		STEM.Biology                                 0.907
		STEM.Chemistry                               0.333
		STEM.Computing                               0.268
		STEM.Earth and environment                   0.528
		STEM.Engineering                             0.485
		STEM.Libraries & Information                 0.296
		STEM.Mathematics                             0.245
		STEM.Medicine & Health                       0.576
		STEM.Physics                                 0.181
		STEM.STEM*                                   0.74
		STEM.Space                                   0.856
		STEM.Technology                              0.259
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.994
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.996
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.989
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.999
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         1
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.999
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.992
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            1
		Geography.Regions.Asia.South Asia            0.997
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.997
		Geography.Regions.Europe.Europe*             0.982
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.997
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.994
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.989
		History and Society.Society                  0.992
		History and Society.Transportation           0.998
		STEM.Biology                                 0.992
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.999
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.724, macro=0.6):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.871
		Culture.Biography.Women                      0.558
		Culture.Food and drink                       0.62
		Culture.Internet culture                     0.584
		Culture.Linguistics                          0.713
		Culture.Literature                           0.642
		Culture.Media.Books                          0.696
		Culture.Media.Entertainment                  0.374
		Culture.Media.Films                          0.823
		Culture.Media.Media*                         0.712
		Culture.Media.Music                          0.762
		Culture.Media.Radio                          0.451
		Culture.Media.Software                       0.283
		Culture.Media.Television                     0.595
		Culture.Media.Video games                    0.818
		Culture.Performing arts                      0.426
		Culture.Philosophy and religion              0.511
		Culture.Sports                               0.911
		Culture.Visual arts.Architecture             0.695
		Culture.Visual arts.Comics and Anime         0.643
		Culture.Visual arts.Fashion                  0.428
		Culture.Visual arts.Visual arts*             0.676
		Geography.Geographical                       0.726
		Geography.Regions.Africa.Africa*             0.641
		Geography.Regions.Africa.Central Africa      0.003
		Geography.Regions.Africa.Eastern Africa      0.517
		Geography.Regions.Africa.Northern Africa     0.32
		Geography.Regions.Africa.Southern Africa     0.595
		Geography.Regions.Africa.Western Africa      0.596
		Geography.Regions.Americas.Central America   0.653
		Geography.Regions.Americas.North America     0.608
		Geography.Regions.Americas.South America     0.733
		Geography.Regions.Asia.Asia*                 0.752
		Geography.Regions.Asia.Central Asia          0.455
		Geography.Regions.Asia.East Asia             0.715
		Geography.Regions.Asia.North Asia            0.258
		Geography.Regions.Asia.South Asia            0.843
		Geography.Regions.Asia.Southeast Asia        0.777
		Geography.Regions.Asia.West Asia             0.715
		Geography.Regions.Europe.Eastern Europe      0.707
		Geography.Regions.Europe.Europe*             0.702
		Geography.Regions.Europe.Northern Europe     0.66
		Geography.Regions.Europe.Southern Europe     0.69
		Geography.Regions.Europe.Western Europe      0.688
		Geography.Regions.Oceania                    0.872
		History and Society.Business and economics   0.48
		History and Society.Education                0.458
		History and Society.History                  0.385
		History and Society.Military and warfare     0.603
		History and Society.Politics and government  0.611
		History and Society.Society                  0.378
		History and Society.Transportation           0.85
		STEM.Biology                                 0.834
		STEM.Chemistry                               0.46
		STEM.Computing                               0.4
		STEM.Earth and environment                   0.585
		STEM.Engineering                             0.582
		STEM.Libraries & Information                 0.409
		STEM.Mathematics                             0.372
		STEM.Medicine & Health                       0.639
		STEM.Physics                                 0.288
		STEM.STEM*                                   0.801
		STEM.Space                                   0.878
		STEM.Technology                              0.38
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.994
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.994
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.996
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
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.992
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.989
		History and Society.Society                  0.991
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.999
		STEM.STEM*                                   0.984
		STEM.Space                                   0.999
		STEM.Technology                              0.994
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.961
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.993
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.99
		Culture.Sports                               0.987
		Culture.Visual arts.Architecture             0.994
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.988
		Geography.Geographical                       0.987
		Geography.Regions.Africa.Africa*             0.993
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.944
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.975
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.992
		Geography.Regions.Europe.Europe*             0.949
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.988
		History and Society.Education                0.993
		History and Society.History                  0.984
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.978
		History and Society.Society                  0.983
		History and Society.Transportation           0.995
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.997
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.97
		STEM.Space                                   0.998
		STEM.Technology                              0.988
		-------------------------------------------  -----
	fpr (micro=0.017, macro=0.006):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.034
		Culture.Biography.Women                      0.013
		Culture.Food and drink                       0.001
		Culture.Internet culture                     0.003
		Culture.Linguistics                          0.001
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.004
		Culture.Media.Films                          0.001
		Culture.Media.Media*                         0.031
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.005
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.002
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.007
		Geography.Geographical                       0.006
		Geography.Regions.Africa.Africa*             0.006
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.038
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.004
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.037
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.005
		Geography.Regions.Europe.Western Europe      0.008
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.007
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.008
		History and Society.Politics and government  0.011
		History and Society.Society                  0.01
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.023
		STEM.Space                                   0.001
		STEM.Technology                              0.01
		-------------------------------------------  -----
	roc_auc (micro=0.973, macro=0.971):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.985
		Culture.Biography.Women                      0.98
		Culture.Food and drink                       0.98
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.977
		Culture.Literature                           0.975
		Culture.Media.Books                          0.98
		Culture.Media.Entertainment                  0.965
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.972
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.969
		Culture.Media.Software                       0.985
		Culture.Media.Television                     0.976
		Culture.Media.Video games                    0.993
		Culture.Performing arts                      0.974
		Culture.Philosophy and religion              0.948
		Culture.Sports                               0.982
		Culture.Visual arts.Architecture             0.979
		Culture.Visual arts.Comics and Anime         0.986
		Culture.Visual arts.Fashion                  0.983
		Culture.Visual arts.Visual arts*             0.971
		Geography.Geographical                       0.975
		Geography.Regions.Africa.Africa*             0.98
		Geography.Regions.Africa.Central Africa      0.689
		Geography.Regions.Africa.Eastern Africa      0.982
		Geography.Regions.Africa.Northern Africa     0.982
		Geography.Regions.Africa.Southern Africa     0.981
		Geography.Regions.Africa.Western Africa      0.985
		Geography.Regions.Americas.Central America   0.976
		Geography.Regions.Americas.North America     0.956
		Geography.Regions.Americas.South America     0.981
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.981
		Geography.Regions.Asia.East Asia             0.978
		Geography.Regions.Asia.North Asia            0.983
		Geography.Regions.Asia.South Asia            0.981
		Geography.Regions.Asia.Southeast Asia        0.978
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.98
		Geography.Regions.Europe.Western Europe      0.978
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.958
		History and Society.Education                0.956
		History and Society.History                  0.943
		History and Society.Military and warfare     0.969
		History and Society.Politics and government  0.957
		History and Society.Society                  0.918
		History and Society.Transportation           0.985
		STEM.Biology                                 0.979
		STEM.Chemistry                               0.986
		STEM.Computing                               0.986
		STEM.Earth and environment                   0.976
		STEM.Engineering                             0.98
		STEM.Libraries & Information                 0.977
		STEM.Mathematics                             0.982
		STEM.Medicine & Health                       0.977
		STEM.Physics                                 0.985
		STEM.STEM*                                   0.975
		STEM.Space                                   0.993
		STEM.Technology                              0.973
		-------------------------------------------  -----
	pr_auc (micro=0.769, macro=0.618):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.939
		Culture.Biography.Women                      0.544
		Culture.Food and drink                       0.651
		Culture.Internet culture                     0.716
		Culture.Linguistics                          0.745
		Culture.Literature                           0.703
		Culture.Media.Books                          0.683
		Culture.Media.Entertainment                  0.366
		Culture.Media.Films                          0.849
		Culture.Media.Media*                         0.806
		Culture.Media.Music                          0.808
		Culture.Media.Radio                          0.372
		Culture.Media.Software                       0.306
		Culture.Media.Television                     0.645
		Culture.Media.Video games                    0.892
		Culture.Performing arts                      0.368
		Culture.Philosophy and religion              0.494
		Culture.Sports                               0.941
		Culture.Visual arts.Architecture             0.707
		Culture.Visual arts.Comics and Anime         0.737
		Culture.Visual arts.Fashion                  0.379
		Culture.Visual arts.Visual arts*             0.729
		Geography.Geographical                       0.755
		Geography.Regions.Africa.Africa*             0.679
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.354
		Geography.Regions.Africa.Northern Africa     0.297
		Geography.Regions.Africa.Southern Africa     0.505
		Geography.Regions.Africa.Western Africa      0.525
		Geography.Regions.Americas.Central America   0.61
		Geography.Regions.Americas.North America     0.63
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.828
		Geography.Regions.Asia.Central Asia          0.374
		Geography.Regions.Asia.East Asia             0.746
		Geography.Regions.Asia.North Asia            0.222
		Geography.Regions.Asia.South Asia            0.878
		Geography.Regions.Asia.Southeast Asia        0.81
		Geography.Regions.Asia.West Asia             0.77
		Geography.Regions.Europe.Eastern Europe      0.75
		Geography.Regions.Europe.Europe*             0.768
		Geography.Regions.Europe.Northern Europe     0.705
		Geography.Regions.Europe.Southern Europe     0.746
		Geography.Regions.Europe.Western Europe      0.705
		Geography.Regions.Oceania                    0.902
		History and Society.Business and economics   0.456
		History and Society.Education                0.422
		History and Society.History                  0.338
		History and Society.Military and warfare     0.651
		History and Society.Politics and government  0.639
		History and Society.Society                  0.345
		History and Society.Transportation           0.899
		STEM.Biology                                 0.896
		STEM.Chemistry                               0.551
		STEM.Computing                               0.45
		STEM.Earth and environment                   0.607
		STEM.Engineering                             0.611
		STEM.Libraries & Information                 0.453
		STEM.Mathematics                             0.469
		STEM.Medicine & Health                       0.617
		STEM.Physics                                 0.269
		STEM.STEM*                                   0.884
		STEM.Space                                   0.94
		STEM.Technology                              0.412
		-------------------------------------------  -----
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}, 'type': 'array'}, 'probability': {'properties': {'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}, 'type': 'object'}

