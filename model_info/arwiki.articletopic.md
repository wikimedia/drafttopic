Model Information:
	 - type: GradientBoosting
	 - version: 1.2.0
	 - params: {'presort': 'auto', 'scale': False, 'validation_fraction': 0.1, 'init': None, 'min_impurity_split': None, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'max_features': 'log2', 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 150, 'random_state': None, 'min_samples_leaf': 1, 'verbose': 0, 'min_impurity_decrease': 0.0, 'population_rates': None, 'warm_start': False, 'criterion': 'friedman_mse', 'label_weights': {}, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'center': False, 'max_depth': 5, 'multilabel': True, 'loss': 'deviance', 'n_iter_no_change': None, 'subsample': 1.0, 'tol': 0.0001}
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
	counts (n=63484):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 27412  -->  26413   999   810  35262
			'Culture.Biography.Women'                       6109  -->   4448  1661   841  56534
			'Culture.Food and drink'                        1402  -->    862   540   114  61968
			'Culture.Internet culture'                      3375  -->   2717   658   214  59895
			'Culture.Linguistics'                           1451  -->    918   533    94  61939
			'Culture.Literature'                            5705  -->   4158  1547   518  57261
			'Culture.Media.Books'                           1561  -->   1139   422   128  61795
			'Culture.Media.Entertainment'                   2115  -->    967  1148   209  61160
			'Culture.Media.Films'                           2079  -->   1660   419    96  61309
			'Culture.Media.Media*'                         13905  -->  11488  2417  1601  47978
			'Culture.Media.Music'                           2678  -->   1961   717   320  60486
			'Culture.Media.Radio'                           1139  -->    500   639   106  62239
			'Culture.Media.Software'                        1969  -->   1365   604   327  61188
			'Culture.Media.Television'                      2347  -->   1315  1032   248  60889
			'Culture.Media.Video games'                     2242  -->   2011   231    58  61184
			'Culture.Performing arts'                       1539  -->    751   788   150  61795
			'Culture.Philosophy and religion'               3414  -->   1667  1747   343  59727
			'Culture.Sports'                                8825  -->   8069   756   398  54261
			'Culture.Visual arts.Architecture'              1823  -->   1123   700   177  61484
			'Culture.Visual arts.Comics and Anime'          1882  -->   1491   391    91  61511
			'Culture.Visual arts.Fashion'                   1345  -->    936   409    87  62052
			'Culture.Visual arts.Visual arts*'              5876  -->   4146  1730   457  57151
			'Geography.Geographical'                        3699  -->   2611  1088   458  59327
			'Geography.Regions.Africa.Africa*'              6508  -->   5234  1274   471  56505
			'Geography.Regions.Africa.Central Africa'       1122  -->    830   292    46  62316
			'Geography.Regions.Africa.Eastern Africa'        959  -->    654   305    47  62478
			'Geography.Regions.Africa.Northern Africa'      2055  -->   1516   539   221  61208
			'Geography.Regions.Africa.Southern Africa'      1176  -->    863   313    53  62255
			'Geography.Regions.Africa.Western Africa'        723  -->    521   202    49  62712
			'Geography.Regions.Americas.Central America'    1383  -->    843   540    76  62025
			'Geography.Regions.Americas.North America'      8685  -->   5939  2746  2282  52517
			'Geography.Regions.Americas.South America'      1646  -->   1233   413   120  61718
			'Geography.Regions.Asia.Asia*'                 12547  -->  10321  2226   937  50000
			'Geography.Regions.Asia.Central Asia'           1175  -->    808   367    67  62242
			'Geography.Regions.Asia.East Asia'              2792  -->   2019   773   249  60443
			'Geography.Regions.Asia.North Asia'             2432  -->   1676   756   198  60854
			'Geography.Regions.Asia.South Asia'             1901  -->   1456   445    61  61522
			'Geography.Regions.Asia.Southeast Asia'         1567  -->   1121   446    70  61847
			'Geography.Regions.Asia.West Asia'              3827  -->   3044   783   299  59358
			'Geography.Regions.Europe.Eastern Europe'       3528  -->   2533   995   266  59690
			'Geography.Regions.Europe.Europe*'             13723  -->  10685  3038  1984  47777
			'Geography.Regions.Europe.Northern Europe'      4077  -->   2641  1436   648  58759
			'Geography.Regions.Europe.Southern Europe'      2781  -->   1984   797   270  60433
			'Geography.Regions.Europe.Western Europe'       3974  -->   2972  1002   541  58969
			'Geography.Regions.Oceania'                     1988  -->   1560   428    79  61417
			'History and Society.Business and economics'    3633  -->   1960  1673   471  59380
			'History and Society.Education'                 2020  -->    825  1195   175  61289
			'History and Society.History'                   4371  -->   1790  2581   646  58467
			'History and Society.Military and warfare'      4117  -->   2614  1503   436  58931
			'History and Society.Politics and government'   4109  -->   2106  2003   586  58789
			'History and Society.Society'                   4427  -->   1068  3359   322  58735
			'History and Society.Transportation'            3292  -->   2790   502   172  60020
			'STEM.Biology'                                  2971  -->   2173   798   225  60288
			'STEM.Chemistry'                                1427  -->    986   441   145  61912
			'STEM.Computing'                                2321  -->   1666   655   364  60799
			'STEM.Earth and environment'                    1710  -->    988   722   153  61621
			'STEM.Engineering'                              2895  -->   2040   855   224  60365
			'STEM.Libraries & Information'                  1201  -->    783   418    80  62203
			'STEM.Mathematics'                              1172  -->    756   416    58  62254
			'STEM.Medicine & Health'                        2285  -->   1537   748   209  60990
			'STEM.Physics'                                  1511  -->    959   552   206  61767
			'STEM.STEM*'                                   17888  -->  15504  2384  1146  44450
			'STEM.Space'                                    1710  -->   1499   211    55  61719
			'STEM.Technology'                               4312  -->   2806  1506   665  58507
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.432         0.121
		Culture.Biography.Women                         0.096         0.015
		Culture.Food and drink                          0.022         0.003
		Culture.Internet culture                        0.053         0.004
		Culture.Linguistics                             0.023         0.008
		Culture.Literature                              0.09          0.015
		Culture.Media.Books                             0.025         0.004
		Culture.Media.Entertainment                     0.033         0.004
		Culture.Media.Films                             0.033         0.012
		Culture.Media.Media*                            0.219         0.055
		Culture.Media.Music                             0.042         0.021
		Culture.Media.Radio                             0.018         0.002
		Culture.Media.Software                          0.031         0.001
		Culture.Media.Television                        0.037         0.009
		Culture.Media.Video games                       0.035         0.003
		Culture.Performing arts                         0.024         0.003
		Culture.Philosophy and religion                 0.054         0.01
		Culture.Sports                                  0.139         0.061
		Culture.Visual arts.Architecture                0.029         0.011
		Culture.Visual arts.Comics and Anime            0.03          0.002
		Culture.Visual arts.Fashion                     0.021         0.001
		Culture.Visual arts.Visual arts*                0.093         0.018
		Geography.Geographical                          0.058         0.021
		Geography.Regions.Africa.Africa*                0.103         0.009
		Geography.Regions.Africa.Central Africa         0.018         0.001
		Geography.Regions.Africa.Eastern Africa         0.015         0.001
		Geography.Regions.Africa.Northern Africa        0.032         0.001
		Geography.Regions.Africa.Southern Africa        0.019         0.001
		Geography.Regions.Africa.Western Africa         0.011         0.001
		Geography.Regions.Americas.Central America      0.022         0.003
		Geography.Regions.Americas.North America        0.137         0.064
		Geography.Regions.Americas.South America        0.026         0.007
		Geography.Regions.Asia.Asia*                    0.198         0.053
		Geography.Regions.Asia.Central Asia             0.019         0.001
		Geography.Regions.Asia.East Asia                0.044         0.012
		Geography.Regions.Asia.North Asia               0.038         0.006
		Geography.Regions.Asia.South Asia               0.03          0.017
		Geography.Regions.Asia.Southeast Asia           0.025         0.006
		Geography.Regions.Asia.West Asia                0.06          0.012
		Geography.Regions.Europe.Eastern Europe         0.056         0.018
		Geography.Regions.Europe.Europe*                0.216         0.082
		Geography.Regions.Europe.Northern Europe        0.064         0.029
		Geography.Regions.Europe.Southern Europe        0.044         0.014
		Geography.Regions.Europe.Western Europe         0.063         0.021
		Geography.Regions.Oceania                       0.031         0.017
		History and Society.Business and economics      0.057         0.01
		History and Society.Education                   0.032         0.008
		History and Society.History                     0.069         0.011
		History and Society.Military and warfare        0.065         0.015
		History and Society.Politics and government     0.065         0.016
		History and Society.Society                     0.07          0.008
		History and Society.Transportation              0.052         0.016
		STEM.Biology                                    0.047         0.035
		STEM.Chemistry                                  0.022         0.002
		STEM.Computing                                  0.037         0.003
		STEM.Earth and environment                      0.027         0.005
		STEM.Engineering                                0.046         0.006
		STEM.Libraries & Information                    0.019         0.001
		STEM.Mathematics                                0.018         0
		STEM.Medicine & Health                          0.036         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.282         0.066
		STEM.Space                                      0.027         0.004
		STEM.Technology                                 0.068         0.005
	match_rate (micro=0.055, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.137
		Culture.Biography.Women                      0.025
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.02
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.011
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.021
		Culture.Media.Radio                          0.003
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.004
		Culture.Philosophy and religion              0.011
		Culture.Sports                               0.063
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.002
		Culture.Visual arts.Visual arts*             0.021
		Geography.Geographical                       0.023
		Geography.Regions.Africa.Africa*             0.015
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.005
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.082
		Geography.Regions.Americas.South America     0.007
		Geography.Regions.Asia.Asia*                 0.061
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.013
		Geography.Regions.Asia.North Asia            0.007
		Geography.Regions.Asia.South Asia            0.014
		Geography.Regions.Asia.Southeast Asia        0.006
		Geography.Regions.Asia.West Asia             0.014
		Geography.Regions.Europe.Eastern Europe      0.018
		Geography.Regions.Europe.Europe*             0.1
		Geography.Regions.Europe.Northern Europe     0.03
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.024
		Geography.Regions.Oceania                    0.014
		History and Society.Business and economics   0.013
		History and Society.Education                0.006
		History and Society.History                  0.015
		History and Society.Military and warfare     0.017
		History and Society.Politics and government  0.018
		History and Society.Society                  0.007
		History and Society.Transportation           0.017
		STEM.Biology                                 0.029
		STEM.Chemistry                               0.004
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.005
		STEM.Engineering                             0.008
		STEM.Libraries & Information                 0.002
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.008
		STEM.Physics                                 0.004
		STEM.STEM*                                   0.08
		STEM.Space                                   0.005
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.945, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.863
		Culture.Biography.Women                      0.975
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.98
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.989
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.979
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.937
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.979
		Geography.Geographical                       0.977
		Geography.Regions.Africa.Africa*             0.985
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.995
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.918
		Geography.Regions.Americas.South America     0.993
		Geography.Regions.Asia.Asia*                 0.939
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.987
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.986
		Geography.Regions.Asia.Southeast Asia        0.994
		Geography.Regions.Asia.West Asia             0.986
		Geography.Regions.Europe.Eastern Europe      0.982
		Geography.Regions.Europe.Europe*             0.9
		Geography.Regions.Europe.Northern Europe     0.97
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.976
		Geography.Regions.Oceania                    0.986
		History and Society.Business and economics   0.987
		History and Society.Education                0.994
		History and Society.History                  0.985
		History and Society.Military and warfare     0.983
		History and Society.Politics and government  0.982
		History and Society.Society                  0.993
		History and Society.Transportation           0.983
		STEM.Biology                                 0.971
		STEM.Chemistry                               0.996
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.992
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.992
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.92
		STEM.Space                                   0.995
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.765, macro=0.689):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.964
		Culture.Biography.Women                      0.728
		Culture.Food and drink                       0.615
		Culture.Internet culture                     0.805
		Culture.Linguistics                          0.633
		Culture.Literature                           0.729
		Culture.Media.Books                          0.73
		Culture.Media.Entertainment                  0.457
		Culture.Media.Films                          0.798
		Culture.Media.Media*                         0.826
		Culture.Media.Music                          0.732
		Culture.Media.Radio                          0.439
		Culture.Media.Software                       0.693
		Culture.Media.Television                     0.56
		Culture.Media.Video games                    0.897
		Culture.Performing arts                      0.488
		Culture.Philosophy and religion              0.488
		Culture.Sports                               0.914
		Culture.Visual arts.Architecture             0.616
		Culture.Visual arts.Comics and Anime         0.792
		Culture.Visual arts.Fashion                  0.696
		Culture.Visual arts.Visual arts*             0.706
		Geography.Geographical                       0.706
		Geography.Regions.Africa.Africa*             0.804
		Geography.Regions.Africa.Central Africa      0.74
		Geography.Regions.Africa.Eastern Africa      0.682
		Geography.Regions.Africa.Northern Africa     0.738
		Geography.Regions.Africa.Southern Africa     0.734
		Geography.Regions.Africa.Western Africa      0.721
		Geography.Regions.Americas.Central America   0.61
		Geography.Regions.Americas.North America     0.684
		Geography.Regions.Americas.South America     0.749
		Geography.Regions.Asia.Asia*                 0.823
		Geography.Regions.Asia.Central Asia          0.688
		Geography.Regions.Asia.East Asia             0.723
		Geography.Regions.Asia.North Asia            0.689
		Geography.Regions.Asia.South Asia            0.766
		Geography.Regions.Asia.Southeast Asia        0.715
		Geography.Regions.Asia.West Asia             0.795
		Geography.Regions.Europe.Eastern Europe      0.718
		Geography.Regions.Europe.Europe*             0.779
		Geography.Regions.Europe.Northern Europe     0.648
		Geography.Regions.Europe.Southern Europe     0.713
		Geography.Regions.Europe.Western Europe      0.748
		Geography.Regions.Oceania                    0.785
		History and Society.Business and economics   0.539
		History and Society.Education                0.408
		History and Society.History                  0.41
		History and Society.Military and warfare     0.635
		History and Society.Politics and government  0.513
		History and Society.Society                  0.241
		History and Society.Transportation           0.848
		STEM.Biology                                 0.731
		STEM.Chemistry                               0.691
		STEM.Computing                               0.718
		STEM.Earth and environment                   0.578
		STEM.Engineering                             0.705
		STEM.Libraries & Information                 0.652
		STEM.Mathematics                             0.645
		STEM.Medicine & Health                       0.673
		STEM.Physics                                 0.635
		STEM.STEM*                                   0.867
		STEM.Space                                   0.877
		STEM.Technology                              0.651
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.978
		Culture.Biography.Women                      0.985
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.968
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.993
		Culture.Visual arts.Architecture             0.997
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.992
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.958
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.995
		Geography.Regions.Europe.Eastern Europe      0.996
		Geography.Regions.Europe.Europe*             0.96
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.991
		Geography.Regions.Oceania                    0.999
		History and Society.Business and economics   0.992
		History and Society.Education                0.997
		History and Society.History                  0.989
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.99
		History and Society.Society                  0.995
		History and Society.Transportation           0.997
		STEM.Biology                                 0.996
		STEM.Chemistry                               0.998
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.996
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.975
		STEM.Space                                   0.999
		STEM.Technology                              0.989
		-------------------------------------------  -----
	precision (micro=0.678, macro=0.55):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.856
		Culture.Biography.Women                      0.432
		Culture.Food and drink                       0.464
		Culture.Internet culture                     0.461
		Culture.Linguistics                          0.773
		Culture.Literature                           0.553
		Culture.Media.Books                          0.607
		Culture.Media.Entertainment                  0.349
		Culture.Media.Films                          0.858
		Culture.Media.Media*                         0.6
		Culture.Media.Music                          0.751
		Culture.Media.Radio                          0.378
		Culture.Media.Software                       0.147
		Culture.Media.Television                     0.556
		Culture.Media.Video games                    0.736
		Culture.Performing arts                      0.384
		Culture.Philosophy and religion              0.475
		Culture.Sports                               0.891
		Culture.Visual arts.Architecture             0.703
		Culture.Visual arts.Comics and Anime         0.565
		Culture.Visual arts.Fashion                  0.31
		Culture.Visual arts.Visual arts*             0.623
		Geography.Geographical                       0.668
		Geography.Regions.Africa.Africa*             0.457
		Geography.Regions.Africa.Central Africa      0.416
		Geography.Regions.Africa.Eastern Africa      0.315
		Geography.Regions.Africa.Northern Africa     0.219
		Geography.Regions.Africa.Southern Africa     0.533
		Geography.Regions.Africa.Western Africa      0.41
		Geography.Regions.Americas.Central America   0.635
		Geography.Regions.Americas.North America     0.527
		Geography.Regions.Americas.South America     0.729
		Geography.Regions.Asia.Asia*                 0.715
		Geography.Regions.Asia.Central Asia          0.34
		Geography.Regions.Asia.East Asia             0.687
		Geography.Regions.Asia.North Asia            0.547
		Geography.Regions.Asia.South Asia            0.929
		Geography.Regions.Asia.Southeast Asia        0.8
		Geography.Regions.Asia.West Asia             0.655
		Geography.Regions.Europe.Eastern Europe      0.753
		Geography.Regions.Europe.Europe*             0.634
		Geography.Regions.Europe.Northern Europe     0.642
		Geography.Regions.Europe.Southern Europe     0.694
		Geography.Regions.Europe.Western Europe      0.635
		Geography.Regions.Oceania                    0.911
		History and Society.Business and economics   0.405
		History and Society.Education                0.536
		History and Society.History                  0.294
		History and Society.Military and warfare     0.576
		History and Society.Politics and government  0.465
		History and Society.Society                  0.271
		History and Society.Transportation           0.832
		STEM.Biology                                 0.876
		STEM.Chemistry                               0.336
		STEM.Computing                               0.256
		STEM.Earth and environment                   0.528
		STEM.Engineering                             0.526
		STEM.Libraries & Information                 0.26
		STEM.Mathematics                             0.244
		STEM.Medicine & Health                       0.563
		STEM.Physics                                 0.153
		STEM.STEM*                                   0.708
		STEM.Space                                   0.81
		STEM.Technology                              0.232
		-------------------------------------------  -----
	!precision (micro=0.992, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.995
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
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
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.995
		Geography.Geographical                       0.994
		Geography.Regions.Africa.Africa*             0.998
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     1
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.978
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.99
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.998
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.98
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.995
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.993
		History and Society.Military and warfare     0.994
		History and Society.Politics and government  0.992
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.999
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.99
		STEM.Space                                   0.999
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.714, macro=0.595):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.906
		Culture.Biography.Women                      0.543
		Culture.Food and drink                       0.529
		Culture.Internet culture                     0.586
		Culture.Linguistics                          0.696
		Culture.Literature                           0.629
		Culture.Media.Books                          0.663
		Culture.Media.Entertainment                  0.396
		Culture.Media.Films                          0.827
		Culture.Media.Media*                         0.695
		Culture.Media.Music                          0.741
		Culture.Media.Radio                          0.406
		Culture.Media.Software                       0.243
		Culture.Media.Television                     0.558
		Culture.Media.Video games                    0.809
		Culture.Performing arts                      0.43
		Culture.Philosophy and religion              0.482
		Culture.Sports                               0.902
		Culture.Visual arts.Architecture             0.657
		Culture.Visual arts.Comics and Anime         0.659
		Culture.Visual arts.Fashion                  0.429
		Culture.Visual arts.Visual arts*             0.662
		Geography.Geographical                       0.686
		Geography.Regions.Africa.Africa*             0.583
		Geography.Regions.Africa.Central Africa      0.533
		Geography.Regions.Africa.Eastern Africa      0.431
		Geography.Regions.Africa.Northern Africa     0.337
		Geography.Regions.Africa.Southern Africa     0.617
		Geography.Regions.Africa.Western Africa      0.523
		Geography.Regions.Americas.Central America   0.622
		Geography.Regions.Americas.North America     0.595
		Geography.Regions.Americas.South America     0.739
		Geography.Regions.Asia.Asia*                 0.765
		Geography.Regions.Asia.Central Asia          0.455
		Geography.Regions.Asia.East Asia             0.704
		Geography.Regions.Asia.North Asia            0.61
		Geography.Regions.Asia.South Asia            0.84
		Geography.Regions.Asia.Southeast Asia        0.755
		Geography.Regions.Asia.West Asia             0.718
		Geography.Regions.Europe.Eastern Europe      0.735
		Geography.Regions.Europe.Europe*             0.699
		Geography.Regions.Europe.Northern Europe     0.645
		Geography.Regions.Europe.Southern Europe     0.704
		Geography.Regions.Europe.Western Europe      0.687
		Geography.Regions.Oceania                    0.843
		History and Society.Business and economics   0.463
		History and Society.Education                0.464
		History and Society.History                  0.342
		History and Society.Military and warfare     0.604
		History and Society.Politics and government  0.488
		History and Society.Society                  0.255
		History and Society.Transportation           0.84
		STEM.Biology                                 0.797
		STEM.Chemistry                               0.452
		STEM.Computing                               0.378
		STEM.Earth and environment                   0.552
		STEM.Engineering                             0.603
		STEM.Libraries & Information                 0.372
		STEM.Mathematics                             0.354
		STEM.Medicine & Health                       0.613
		STEM.Physics                                 0.247
		STEM.STEM*                                   0.779
		STEM.Space                                   0.842
		STEM.Technology                              0.342
		-------------------------------------------  -----
	!f1 (micro=0.988, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.991
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.998
		Culture.Linguistics                          0.998
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.979
		Culture.Media.Music                          0.994
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.994
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.993
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.999
		Geography.Regions.Americas.North America     0.968
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.986
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.996
		Geography.Regions.Asia.North Asia            0.997
		Geography.Regions.Asia.South Asia            0.998
		Geography.Regions.Asia.Southeast Asia        0.999
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.97
		Geography.Regions.Europe.Northern Europe     0.989
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.996
		History and Society.History                  0.991
		History and Society.Military and warfare     0.993
		History and Society.Politics and government  0.991
		History and Society.Society                  0.994
		History and Society.Transportation           0.997
		STEM.Biology                                 0.993
		STEM.Chemistry                               0.999
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.997
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.983
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.977, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.976
		Culture.Biography.Women                      0.981
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.996
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.96
		Culture.Media.Music                          0.989
		Culture.Media.Radio                          0.997
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.992
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.989
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.993
		Culture.Visual arts.Comics and Anime         0.998
		Culture.Visual arts.Fashion                  0.998
		Culture.Visual arts.Visual arts*             0.987
		Geography.Geographical                       0.986
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.996
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.941
		Geography.Regions.Americas.South America     0.996
		Geography.Regions.Asia.Asia*                 0.973
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.993
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.995
		Geography.Regions.Asia.Southeast Asia        0.997
		Geography.Regions.Asia.West Asia             0.993
		Geography.Regions.Europe.Eastern Europe      0.99
		Geography.Regions.Europe.Europe*             0.945
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.992
		Geography.Regions.Europe.Western Europe      0.986
		Geography.Regions.Oceania                    0.995
		History and Society.Business and economics   0.988
		History and Society.Education                0.992
		History and Society.History                  0.983
		History and Society.Military and warfare     0.987
		History and Society.Politics and government  0.982
		History and Society.Society                  0.988
		History and Society.Transportation           0.995
		STEM.Biology                                 0.987
		STEM.Chemistry                               0.997
		STEM.Computing                               0.993
		STEM.Earth and environment                   0.996
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.998
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.994
		STEM.Physics                                 0.996
		STEM.STEM*                                   0.968
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.022
		Culture.Biography.Women                      0.015
		Culture.Food and drink                       0.002
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.032
		Culture.Media.Music                          0.005
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.004
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.006
		Culture.Sports                               0.007
		Culture.Visual arts.Architecture             0.003
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.008
		Geography.Regions.Africa.Africa*             0.008
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.004
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.001
		Geography.Regions.Americas.North America     0.042
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.004
		Geography.Regions.Asia.North Asia            0.003
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.001
		Geography.Regions.Asia.West Asia             0.005
		Geography.Regions.Europe.Eastern Europe      0.004
		Geography.Regions.Europe.Europe*             0.04
		Geography.Regions.Europe.Northern Europe     0.011
		Geography.Regions.Europe.Southern Europe     0.004
		Geography.Regions.Europe.Western Europe      0.009
		Geography.Regions.Oceania                    0.001
		History and Society.Business and economics   0.008
		History and Society.Education                0.003
		History and Society.History                  0.011
		History and Society.Military and warfare     0.007
		History and Society.Politics and government  0.01
		History and Society.Society                  0.005
		History and Society.Transportation           0.003
		STEM.Biology                                 0.004
		STEM.Chemistry                               0.002
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.002
		STEM.Engineering                             0.004
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.003
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.025
		STEM.Space                                   0.001
		STEM.Technology                              0.011
		-------------------------------------------  -----
	roc_auc (micro=0.971, macro=0.972):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.986
		Culture.Biography.Women                      0.979
		Culture.Food and drink                       0.972
		Culture.Internet culture                     0.984
		Culture.Linguistics                          0.97
		Culture.Literature                           0.973
		Culture.Media.Books                          0.977
		Culture.Media.Entertainment                  0.96
		Culture.Media.Films                          0.985
		Culture.Media.Media*                         0.971
		Culture.Media.Music                          0.978
		Culture.Media.Radio                          0.964
		Culture.Media.Software                       0.982
		Culture.Media.Television                     0.974
		Culture.Media.Video games                    0.991
		Culture.Performing arts                      0.969
		Culture.Philosophy and religion              0.942
		Culture.Sports                               0.981
		Culture.Visual arts.Architecture             0.975
		Culture.Visual arts.Comics and Anime         0.983
		Culture.Visual arts.Fashion                  0.978
		Culture.Visual arts.Visual arts*             0.966
		Geography.Geographical                       0.974
		Geography.Regions.Africa.Africa*             0.977
		Geography.Regions.Africa.Central Africa      0.982
		Geography.Regions.Africa.Eastern Africa      0.975
		Geography.Regions.Africa.Northern Africa     0.98
		Geography.Regions.Africa.Southern Africa     0.978
		Geography.Regions.Africa.Western Africa      0.983
		Geography.Regions.Americas.Central America   0.97
		Geography.Regions.Americas.North America     0.954
		Geography.Regions.Americas.South America     0.976
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.979
		Geography.Regions.Asia.East Asia             0.976
		Geography.Regions.Asia.North Asia            0.971
		Geography.Regions.Asia.South Asia            0.98
		Geography.Regions.Asia.Southeast Asia        0.975
		Geography.Regions.Asia.West Asia             0.981
		Geography.Regions.Europe.Eastern Europe      0.97
		Geography.Regions.Europe.Europe*             0.958
		Geography.Regions.Europe.Northern Europe     0.969
		Geography.Regions.Europe.Southern Europe     0.975
		Geography.Regions.Europe.Western Europe      0.977
		Geography.Regions.Oceania                    0.978
		History and Society.Business and economics   0.958
		History and Society.Education                0.951
		History and Society.History                  0.935
		History and Society.Military and warfare     0.966
		History and Society.Politics and government  0.95
		History and Society.Society                  0.893
		History and Society.Transportation           0.984
		STEM.Biology                                 0.973
		STEM.Chemistry                               0.984
		STEM.Computing                               0.984
		STEM.Earth and environment                   0.97
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.972
		STEM.Mathematics                             0.977
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.982
		STEM.STEM*                                   0.973
		STEM.Space                                   0.99
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.751, macro=0.594):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.953
		Culture.Biography.Women                      0.504
		Culture.Food and drink                       0.482
		Culture.Internet culture                     0.685
		Culture.Linguistics                          0.705
		Culture.Literature                           0.692
		Culture.Media.Books                          0.676
		Culture.Media.Entertainment                  0.367
		Culture.Media.Films                          0.863
		Culture.Media.Media*                         0.783
		Culture.Media.Music                          0.755
		Culture.Media.Radio                          0.296
		Culture.Media.Software                       0.214
		Culture.Media.Television                     0.573
		Culture.Media.Video games                    0.825
		Culture.Performing arts                      0.402
		Culture.Philosophy and religion              0.395
		Culture.Sports                               0.931
		Culture.Visual arts.Architecture             0.668
		Culture.Visual arts.Comics and Anime         0.691
		Culture.Visual arts.Fashion                  0.384
		Culture.Visual arts.Visual arts*             0.705
		Geography.Geographical                       0.727
		Geography.Regions.Africa.Africa*             0.583
		Geography.Regions.Africa.Central Africa      0.452
		Geography.Regions.Africa.Eastern Africa      0.376
		Geography.Regions.Africa.Northern Africa     0.337
		Geography.Regions.Africa.Southern Africa     0.461
		Geography.Regions.Africa.Western Africa      0.48
		Geography.Regions.Americas.Central America   0.546
		Geography.Regions.Americas.North America     0.629
		Geography.Regions.Americas.South America     0.667
		Geography.Regions.Asia.Asia*                 0.841
		Geography.Regions.Asia.Central Asia          0.345
		Geography.Regions.Asia.East Asia             0.732
		Geography.Regions.Asia.North Asia            0.622
		Geography.Regions.Asia.South Asia            0.881
		Geography.Regions.Asia.Southeast Asia        0.756
		Geography.Regions.Asia.West Asia             0.778
		Geography.Regions.Europe.Eastern Europe      0.76
		Geography.Regions.Europe.Europe*             0.772
		Geography.Regions.Europe.Northern Europe     0.691
		Geography.Regions.Europe.Southern Europe     0.735
		Geography.Regions.Europe.Western Europe      0.707
		Geography.Regions.Oceania                    0.867
		History and Society.Business and economics   0.414
		History and Society.Education                0.421
		History and Society.History                  0.273
		History and Society.Military and warfare     0.64
		History and Society.Politics and government  0.467
		History and Society.Society                  0.199
		History and Society.Transportation           0.887
		STEM.Biology                                 0.857
		STEM.Chemistry                               0.466
		STEM.Computing                               0.329
		STEM.Earth and environment                   0.519
		STEM.Engineering                             0.643
		STEM.Libraries & Information                 0.291
		STEM.Mathematics                             0.364
		STEM.Medicine & Health                       0.618
		STEM.Physics                                 0.206
		STEM.STEM*                                   0.879
		STEM.Space                                   0.896
		STEM.Technology                              0.361
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'STEM.STEM*': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

