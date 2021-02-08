Model Information:
	 - type: GradientBoosting
	 - version: 1.3.0
	 - params: {'random_state': None, 'presort': 'deprecated', 'warm_start': False, 'loss': 'deviance', 'init': None, 'min_impurity_decrease': 0.0, 'ccp_alpha': 0.0, 'labels': ['Culture.Biography.Biography*', 'Culture.Biography.Women', 'Culture.Food and drink', 'Culture.Internet culture', 'Culture.Linguistics', 'Culture.Literature', 'Culture.Media.Books', 'Culture.Media.Entertainment', 'Culture.Media.Films', 'Culture.Media.Media*', 'Culture.Media.Music', 'Culture.Media.Radio', 'Culture.Media.Software', 'Culture.Media.Television', 'Culture.Media.Video games', 'Culture.Performing arts', 'Culture.Philosophy and religion', 'Culture.Sports', 'Culture.Visual arts.Architecture', 'Culture.Visual arts.Comics and Anime', 'Culture.Visual arts.Fashion', 'Culture.Visual arts.Visual arts*', 'Geography.Geographical', 'Geography.Regions.Africa.Africa*', 'Geography.Regions.Africa.Central Africa', 'Geography.Regions.Africa.Eastern Africa', 'Geography.Regions.Africa.Northern Africa', 'Geography.Regions.Africa.Southern Africa', 'Geography.Regions.Africa.Western Africa', 'Geography.Regions.Americas.Central America', 'Geography.Regions.Americas.North America', 'Geography.Regions.Americas.South America', 'Geography.Regions.Asia.Asia*', 'Geography.Regions.Asia.Central Asia', 'Geography.Regions.Asia.East Asia', 'Geography.Regions.Asia.North Asia', 'Geography.Regions.Asia.South Asia', 'Geography.Regions.Asia.Southeast Asia', 'Geography.Regions.Asia.West Asia', 'Geography.Regions.Europe.Eastern Europe', 'Geography.Regions.Europe.Europe*', 'Geography.Regions.Europe.Northern Europe', 'Geography.Regions.Europe.Southern Europe', 'Geography.Regions.Europe.Western Europe', 'Geography.Regions.Oceania', 'History and Society.Business and economics', 'History and Society.Education', 'History and Society.History', 'History and Society.Military and warfare', 'History and Society.Politics and government', 'History and Society.Society', 'History and Society.Transportation', 'STEM.Biology', 'STEM.Chemistry', 'STEM.Computing', 'STEM.Earth and environment', 'STEM.Engineering', 'STEM.Libraries & Information', 'STEM.Mathematics', 'STEM.Medicine & Health', 'STEM.Physics', 'STEM.STEM*', 'STEM.Space', 'STEM.Technology'], 'n_iter_no_change': None, 'n_estimators': 150, 'learning_rate': 0.1, 'center': False, 'min_impurity_split': None, 'multilabel': True, 'validation_fraction': 0.1, 'min_samples_leaf': 1, 'subsample': 1.0, 'population_rates': None, 'min_samples_split': 2, 'scale': False, 'verbose': 0, 'label_weights': {}, 'criterion': 'friedman_mse', 'max_depth': 5, 'max_features': 'log2', 'min_weight_fraction_leaf': 0.0, 'max_leaf_nodes': None, 'tol': 0.0001}
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
	counts (n=56317):
			label                                              n          TP    FP    FN     TN
			---------------------------------------------  -----  ---  -----  ----  ----  -----
			'Culture.Biography.Biography*'                 13202  -->  11399  1803   922  42193
			'Culture.Biography.Women'                       3612  -->   2656   956   320  52385
			'Culture.Food and drink'                        1382  -->    744   638   166  54769
			'Culture.Internet culture'                      2952  -->   2395   557   237  53128
			'Culture.Linguistics'                           1478  -->    918   560   116  54723
			'Culture.Literature'                            4856  -->   3358  1498   460  51001
			'Culture.Media.Books'                           1520  -->   1119   401   128  54669
			'Culture.Media.Entertainment'                   2187  -->   1014  1173   186  53944
			'Culture.Media.Films'                           2685  -->   2224   461   116  53516
			'Culture.Media.Media*'                         12479  -->  10711  1768  1323  42515
			'Culture.Media.Music'                           2597  -->   1937   660   209  53511
			'Culture.Media.Radio'                            257  -->    177    80    27  56033
			'Culture.Media.Software'                        2166  -->   1799   367   263  53888
			'Culture.Media.Television'                      2379  -->   1909   470   124  53814
			'Culture.Media.Video games'                     1458  -->   1337   121    51  54808
			'Culture.Performing arts'                       1418  -->    626   792   106  54793
			'Culture.Philosophy and religion'               3951  -->   1889  2062   422  51944
			'Culture.Sports'                                5217  -->   4501   716   181  50919
			'Culture.Visual arts.Architecture'              2008  -->   1149   859   221  54088
			'Culture.Visual arts.Comics and Anime'          1184  -->    929   255    52  55081
			'Culture.Visual arts.Fashion'                    643  -->    322   321    38  55636
			'Culture.Visual arts.Visual arts*'              4451  -->   2568  1883   403  51463
			'Geography.Geographical'                        4861  -->   3340  1521   807  50649
			'Geography.Regions.Africa.Africa*'              3739  -->   2344  1395   273  52305
			'Geography.Regions.Africa.Central Africa'        539  -->    261   278    49  55729
			'Geography.Regions.Africa.Eastern Africa'        399  -->    210   189    42  55876
			'Geography.Regions.Africa.Northern Africa'      1420  -->    895   525   111  54786
			'Geography.Regions.Africa.Southern Africa'       607  -->    365   242    50  55660
			'Geography.Regions.Africa.Western Africa'        138  -->     94    44    23  56156
			'Geography.Regions.Americas.Central America'    1280  -->    431   849    91  54946
			'Geography.Regions.Americas.North America'      6091  -->   3943  2148   676  49550
			'Geography.Regions.Americas.South America'      1509  -->    905   604    99  54709
			'Geography.Regions.Asia.Asia*'                 10638  -->   8070  2568   830  44849
			'Geography.Regions.Asia.Central Asia'            857  -->    450   407    66  55394
			'Geography.Regions.Asia.East Asia'              2406  -->   1770   636   117  53794
			'Geography.Regions.Asia.North Asia'             3401  -->   2428   973   286  52630
			'Geography.Regions.Asia.South Asia'             1617  -->    982   635    77  54623
			'Geography.Regions.Asia.Southeast Asia'         1451  -->    881   570    91  54775
			'Geography.Regions.Asia.West Asia'              2464  -->   1543   921   221  53632
			'Geography.Regions.Europe.Eastern Europe'       5323  -->   3860  1463   367  50627
			'Geography.Regions.Europe.Europe*'             17596  -->  14028  3568  2176  36545
			'Geography.Regions.Europe.Northern Europe'      3169  -->   1787  1382   279  52869
			'Geography.Regions.Europe.Southern Europe'      5989  -->   4287  1702   706  49622
			'Geography.Regions.Europe.Western Europe'       4301  -->   3004  1297   346  51670
			'Geography.Regions.Oceania'                     1856  -->   1211   645   105  54356
			'History and Society.Business and economics'    2940  -->   1489  1451   310  53067
			'History and Society.Education'                 1605  -->    623   982   134  54578
			'History and Society.History'                   6321  -->   3774  2547   966  49030
			'History and Society.Military and warfare'      4862  -->   3222  1640   544  50911
			'History and Society.Politics and government'   4324  -->   2193  2131   461  51532
			'History and Society.Society'                   4341  -->    968  3373   252  51724
			'History and Society.Transportation'            3161  -->   2712   449   120  53036
			'STEM.Biology'                                  3777  -->   3010   767   179  52361
			'STEM.Chemistry'                                2057  -->   1489   568   310  53950
			'STEM.Computing'                                2613  -->   2125   488   296  53408
			'STEM.Earth and environment'                    1681  -->    873   808   172  54464
			'STEM.Engineering'                              2669  -->   1922   747   167  53481
			'STEM.Libraries & Information'                   500  -->    358   142    30  55787
			'STEM.Mathematics'                               539  -->    312   227    53  55725
			'STEM.Medicine & Health'                        2365  -->   1582   783   263  53689
			'STEM.Physics'                                  1374  -->    851   523   160  54783
			'STEM.STEM*'                                   17980  -->  15850  2130  1204  37133
			'STEM.Space'                                    2120  -->   1921   199    35  54162
			'STEM.Technology'                               4457  -->   3121  1336   618  51242
	rates:
		                                               sample    population
		-------------------------------------------  --------  ------------
		Culture.Biography.Biography*                    0.234         0.12
		Culture.Biography.Women                         0.064         0.015
		Culture.Food and drink                          0.025         0.003
		Culture.Internet culture                        0.052         0.004
		Culture.Linguistics                             0.026         0.008
		Culture.Literature                              0.086         0.015
		Culture.Media.Books                             0.027         0.004
		Culture.Media.Entertainment                     0.039         0.004
		Culture.Media.Films                             0.048         0.012
		Culture.Media.Media*                            0.222         0.055
		Culture.Media.Music                             0.046         0.021
		Culture.Media.Radio                             0.005         0.002
		Culture.Media.Software                          0.038         0.001
		Culture.Media.Television                        0.042         0.009
		Culture.Media.Video games                       0.026         0.003
		Culture.Performing arts                         0.025         0.003
		Culture.Philosophy and religion                 0.07          0.01
		Culture.Sports                                  0.093         0.06
		Culture.Visual arts.Architecture                0.036         0.011
		Culture.Visual arts.Comics and Anime            0.021         0.002
		Culture.Visual arts.Fashion                     0.011         0.001
		Culture.Visual arts.Visual arts*                0.079         0.018
		Geography.Geographical                          0.086         0.021
		Geography.Regions.Africa.Africa*                0.066         0.008
		Geography.Regions.Africa.Central Africa         0.01          0.001
		Geography.Regions.Africa.Eastern Africa         0.007         0.001
		Geography.Regions.Africa.Northern Africa        0.025         0.001
		Geography.Regions.Africa.Southern Africa        0.011         0.001
		Geography.Regions.Africa.Western Africa         0.002         0.001
		Geography.Regions.Americas.Central America      0.023         0.003
		Geography.Regions.Americas.North America        0.108         0.063
		Geography.Regions.Americas.South America        0.027         0.007
		Geography.Regions.Asia.Asia*                    0.189         0.052
		Geography.Regions.Asia.Central Asia             0.015         0.001
		Geography.Regions.Asia.East Asia                0.043         0.012
		Geography.Regions.Asia.North Asia               0.06          0.006
		Geography.Regions.Asia.South Asia               0.029         0.016
		Geography.Regions.Asia.Southeast Asia           0.026         0.006
		Geography.Regions.Asia.West Asia                0.044         0.012
		Geography.Regions.Europe.Eastern Europe         0.095         0.018
		Geography.Regions.Europe.Europe*                0.312         0.081
		Geography.Regions.Europe.Northern Europe        0.056         0.029
		Geography.Regions.Europe.Southern Europe        0.106         0.014
		Geography.Regions.Europe.Western Europe         0.076         0.02
		Geography.Regions.Oceania                       0.033         0.016
		History and Society.Business and economics      0.052         0.01
		History and Society.Education                   0.028         0.008
		History and Society.History                     0.112         0.011
		History and Society.Military and warfare        0.086         0.015
		History and Society.Politics and government     0.077         0.028
		History and Society.Society                     0.077         0.008
		History and Society.Transportation              0.056         0.016
		STEM.Biology                                    0.067         0.034
		STEM.Chemistry                                  0.037         0.002
		STEM.Computing                                  0.046         0.003
		STEM.Earth and environment                      0.03          0.005
		STEM.Engineering                                0.047         0.006
		STEM.Libraries & Information                    0.009         0.001
		STEM.Mathematics                                0.01          0
		STEM.Medicine & Health                          0.042         0.006
		STEM.Physics                                    0.024         0.001
		STEM.STEM*                                      0.319         0.065
		STEM.Space                                      0.038         0.004
		STEM.Technology                                 0.079         0.005
	match_rate (micro=0.052, macro=0.018):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.122
		Culture.Biography.Women                      0.017
		Culture.Food and drink                       0.004
		Culture.Internet culture                     0.007
		Culture.Linguistics                          0.007
		Culture.Literature                           0.019
		Culture.Media.Books                          0.005
		Culture.Media.Entertainment                  0.005
		Culture.Media.Films                          0.012
		Culture.Media.Media*                         0.076
		Culture.Media.Music                          0.019
		Culture.Media.Radio                          0.002
		Culture.Media.Software                       0.006
		Culture.Media.Television                     0.009
		Culture.Media.Video games                    0.004
		Culture.Performing arts                      0.003
		Culture.Philosophy and religion              0.013
		Culture.Sports                               0.055
		Culture.Visual arts.Architecture             0.01
		Culture.Visual arts.Comics and Anime         0.003
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.018
		Geography.Geographical                       0.03
		Geography.Regions.Africa.Africa*             0.01
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.003
		Geography.Regions.Africa.Southern Africa     0.002
		Geography.Regions.Africa.Western Africa      0.001
		Geography.Regions.Americas.Central America   0.003
		Geography.Regions.Americas.North America     0.053
		Geography.Regions.Americas.South America     0.006
		Geography.Regions.Asia.Asia*                 0.057
		Geography.Regions.Asia.Central Asia          0.002
		Geography.Regions.Asia.East Asia             0.011
		Geography.Regions.Asia.North Asia            0.009
		Geography.Regions.Asia.South Asia            0.011
		Geography.Regions.Asia.Southeast Asia        0.005
		Geography.Regions.Asia.West Asia             0.011
		Geography.Regions.Europe.Eastern Europe      0.02
		Geography.Regions.Europe.Europe*             0.116
		Geography.Regions.Europe.Northern Europe     0.021
		Geography.Regions.Europe.Southern Europe     0.024
		Geography.Regions.Europe.Western Europe      0.021
		Geography.Regions.Oceania                    0.013
		History and Society.Business and economics   0.011
		History and Society.Education                0.005
		History and Society.History                  0.026
		History and Society.Military and warfare     0.021
		History and Society.Politics and government  0.023
		History and Society.Society                  0.007
		History and Society.Transportation           0.016
		STEM.Biology                                 0.031
		STEM.Chemistry                               0.007
		STEM.Computing                               0.008
		STEM.Earth and environment                   0.006
		STEM.Engineering                             0.007
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.009
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.087
		STEM.Space                                   0.004
		STEM.Technology                              0.015
		-------------------------------------------  -----
	filter_rate (micro=0.948, macro=0.982):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.878
		Culture.Biography.Women                      0.983
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.993
		Culture.Linguistics                          0.993
		Culture.Literature                           0.981
		Culture.Media.Books                          0.995
		Culture.Media.Entertainment                  0.995
		Culture.Media.Films                          0.988
		Culture.Media.Media*                         0.924
		Culture.Media.Music                          0.981
		Culture.Media.Radio                          0.998
		Culture.Media.Software                       0.994
		Culture.Media.Television                     0.991
		Culture.Media.Video games                    0.996
		Culture.Performing arts                      0.997
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.945
		Culture.Visual arts.Architecture             0.99
		Culture.Visual arts.Comics and Anime         0.997
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.982
		Geography.Geographical                       0.97
		Geography.Regions.Africa.Africa*             0.99
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.998
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.997
		Geography.Regions.Americas.North America     0.947
		Geography.Regions.Americas.South America     0.994
		Geography.Regions.Asia.Asia*                 0.943
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.989
		Geography.Regions.Asia.North Asia            0.991
		Geography.Regions.Asia.South Asia            0.989
		Geography.Regions.Asia.Southeast Asia        0.995
		Geography.Regions.Asia.West Asia             0.989
		Geography.Regions.Europe.Eastern Europe      0.98
		Geography.Regions.Europe.Europe*             0.884
		Geography.Regions.Europe.Northern Europe     0.979
		Geography.Regions.Europe.Southern Europe     0.976
		Geography.Regions.Europe.Western Europe      0.979
		Geography.Regions.Oceania                    0.987
		History and Society.Business and economics   0.989
		History and Society.Education                0.995
		History and Society.History                  0.974
		History and Society.Military and warfare     0.979
		History and Society.Politics and government  0.977
		History and Society.Society                  0.993
		History and Society.Transportation           0.984
		STEM.Biology                                 0.969
		STEM.Chemistry                               0.993
		STEM.Computing                               0.992
		STEM.Earth and environment                   0.994
		STEM.Engineering                             0.993
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.991
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.913
		STEM.Space                                   0.996
		STEM.Technology                              0.985
		-------------------------------------------  -----
	recall (micro=0.735, macro=0.661):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.863
		Culture.Biography.Women                      0.735
		Culture.Food and drink                       0.538
		Culture.Internet culture                     0.811
		Culture.Linguistics                          0.621
		Culture.Literature                           0.692
		Culture.Media.Books                          0.736
		Culture.Media.Entertainment                  0.464
		Culture.Media.Films                          0.828
		Culture.Media.Media*                         0.858
		Culture.Media.Music                          0.746
		Culture.Media.Radio                          0.689
		Culture.Media.Software                       0.831
		Culture.Media.Television                     0.802
		Culture.Media.Video games                    0.917
		Culture.Performing arts                      0.441
		Culture.Philosophy and religion              0.478
		Culture.Sports                               0.863
		Culture.Visual arts.Architecture             0.572
		Culture.Visual arts.Comics and Anime         0.785
		Culture.Visual arts.Fashion                  0.501
		Culture.Visual arts.Visual arts*             0.577
		Geography.Geographical                       0.687
		Geography.Regions.Africa.Africa*             0.627
		Geography.Regions.Africa.Central Africa      0.484
		Geography.Regions.Africa.Eastern Africa      0.526
		Geography.Regions.Africa.Northern Africa     0.63
		Geography.Regions.Africa.Southern Africa     0.601
		Geography.Regions.Africa.Western Africa      0.681
		Geography.Regions.Americas.Central America   0.337
		Geography.Regions.Americas.North America     0.647
		Geography.Regions.Americas.South America     0.6
		Geography.Regions.Asia.Asia*                 0.759
		Geography.Regions.Asia.Central Asia          0.525
		Geography.Regions.Asia.East Asia             0.736
		Geography.Regions.Asia.North Asia            0.714
		Geography.Regions.Asia.South Asia            0.607
		Geography.Regions.Asia.Southeast Asia        0.607
		Geography.Regions.Asia.West Asia             0.626
		Geography.Regions.Europe.Eastern Europe      0.725
		Geography.Regions.Europe.Europe*             0.797
		Geography.Regions.Europe.Northern Europe     0.564
		Geography.Regions.Europe.Southern Europe     0.716
		Geography.Regions.Europe.Western Europe      0.698
		Geography.Regions.Oceania                    0.652
		History and Society.Business and economics   0.506
		History and Society.Education                0.388
		History and Society.History                  0.597
		History and Society.Military and warfare     0.663
		History and Society.Politics and government  0.507
		History and Society.Society                  0.223
		History and Society.Transportation           0.858
		STEM.Biology                                 0.797
		STEM.Chemistry                               0.724
		STEM.Computing                               0.813
		STEM.Earth and environment                   0.519
		STEM.Engineering                             0.72
		STEM.Libraries & Information                 0.716
		STEM.Mathematics                             0.579
		STEM.Medicine & Health                       0.669
		STEM.Physics                                 0.619
		STEM.STEM*                                   0.882
		STEM.Space                                   0.906
		STEM.Technology                              0.7
		-------------------------------------------  -----
	!recall (micro=0.984, macro=0.993):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.979
		Culture.Biography.Women                      0.994
		Culture.Food and drink                       0.997
		Culture.Internet culture                     0.996
		Culture.Linguistics                          0.998
		Culture.Literature                           0.991
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.97
		Culture.Media.Music                          0.996
		Culture.Media.Radio                          1
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.992
		Culture.Sports                               0.996
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.984
		Geography.Regions.Africa.Africa*             0.995
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.998
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.987
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.982
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.998
		Geography.Regions.Asia.North Asia            0.995
		Geography.Regions.Asia.South Asia            0.999
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.993
		Geography.Regions.Europe.Europe*             0.944
		Geography.Regions.Europe.Northern Europe     0.995
		Geography.Regions.Europe.Southern Europe     0.986
		Geography.Regions.Europe.Western Europe      0.993
		Geography.Regions.Oceania                    0.998
		History and Society.Business and economics   0.994
		History and Society.Education                0.998
		History and Society.History                  0.981
		History and Society.Military and warfare     0.989
		History and Society.Politics and government  0.991
		History and Society.Society                  0.995
		History and Society.Transportation           0.998
		STEM.Biology                                 0.997
		STEM.Chemistry                               0.994
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.997
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.995
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.969
		STEM.Space                                   0.999
		STEM.Technology                              0.988
		-------------------------------------------  -----
	precision (micro=0.682, macro=0.548):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.846
		Culture.Biography.Women                      0.647
		Culture.Food and drink                       0.312
		Culture.Internet culture                     0.406
		Culture.Linguistics                          0.703
		Culture.Literature                           0.538
		Culture.Media.Books                          0.577
		Culture.Media.Entertainment                  0.348
		Culture.Media.Films                          0.817
		Culture.Media.Media*                         0.622
		Culture.Media.Music                          0.804
		Culture.Media.Radio                          0.769
		Culture.Media.Software                       0.183
		Culture.Media.Television                     0.757
		Culture.Media.Video games                    0.742
		Culture.Performing arts                      0.411
		Culture.Philosophy and religion              0.383
		Culture.Sports                               0.94
		Culture.Visual arts.Architecture             0.605
		Culture.Visual arts.Comics and Anime         0.666
		Culture.Visual arts.Fashion                  0.396
		Culture.Visual arts.Visual arts*             0.577
		Geography.Geographical                       0.486
		Geography.Regions.Africa.Africa*             0.508
		Geography.Regions.Africa.Central Africa      0.279
		Geography.Regions.Africa.Eastern Africa      0.26
		Geography.Regions.Africa.Northern Africa     0.296
		Geography.Regions.Africa.Southern Africa     0.467
		Geography.Regions.Africa.Western Africa      0.553
		Geography.Regions.Americas.Central America   0.413
		Geography.Regions.Americas.North America     0.763
		Geography.Regions.Americas.South America     0.696
		Geography.Regions.Asia.Asia*                 0.698
		Geography.Regions.Asia.Central Asia          0.26
		Geography.Regions.Asia.East Asia             0.806
		Geography.Regions.Asia.North Asia            0.426
		Geography.Regions.Asia.South Asia            0.878
		Geography.Regions.Asia.Southeast Asia        0.696
		Geography.Regions.Asia.West Asia             0.643
		Geography.Regions.Europe.Eastern Europe      0.652
		Geography.Regions.Europe.Europe*             0.555
		Geography.Regions.Europe.Northern Europe     0.762
		Geography.Regions.Europe.Southern Europe     0.416
		Geography.Regions.Europe.Western Europe      0.687
		Geography.Regions.Oceania                    0.849
		History and Society.Business and economics   0.461
		History and Society.Education                0.558
		History and Society.History                  0.254
		History and Society.Military and warfare     0.493
		History and Society.Politics and government  0.622
		History and Society.Society                  0.277
		History and Society.Transportation           0.862
		STEM.Biology                                 0.893
		STEM.Chemistry                               0.176
		STEM.Computing                               0.294
		STEM.Earth and environment                   0.439
		STEM.Engineering                             0.571
		STEM.Libraries & Information                 0.477
		STEM.Mathematics                             0.219
		STEM.Medicine & Health                       0.47
		STEM.Physics                                 0.166
		STEM.STEM*                                   0.661
		STEM.Space                                   0.857
		STEM.Technology                              0.233
		-------------------------------------------  -----
	!precision (micro=0.99, macro=0.996):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.981
		Culture.Biography.Women                      0.996
		Culture.Food and drink                       0.999
		Culture.Internet culture                     0.999
		Culture.Linguistics                          0.997
		Culture.Literature                           0.995
		Culture.Media.Books                          0.999
		Culture.Media.Entertainment                  0.998
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.992
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       1
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    1
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.995
		Culture.Sports                               0.991
		Culture.Visual arts.Architecture             0.995
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  1
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.993
		Geography.Regions.Africa.Africa*             0.997
		Geography.Regions.Africa.Central Africa      1
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     1
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.977
		Geography.Regions.Americas.South America     0.997
		Geography.Regions.Asia.Asia*                 0.987
		Geography.Regions.Asia.Central Asia          1
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.998
		Geography.Regions.Asia.South Asia            0.993
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.995
		Geography.Regions.Europe.Europe*             0.981
		Geography.Regions.Europe.Northern Europe     0.987
		Geography.Regions.Europe.Southern Europe     0.996
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.994
		History and Society.Business and economics   0.995
		History and Society.Education                0.995
		History and Society.History                  0.996
		History and Society.Military and warfare     0.995
		History and Society.Politics and government  0.986
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.993
		STEM.Chemistry                               1
		STEM.Computing                               0.999
		STEM.Earth and environment                   0.998
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             1
		STEM.Medicine & Health                       0.998
		STEM.Physics                                 1
		STEM.STEM*                                   0.992
		STEM.Space                                   1
		STEM.Technology                              0.998
		-------------------------------------------  -----
	f1 (micro=0.698, macro=0.58):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.855
		Culture.Biography.Women                      0.689
		Culture.Food and drink                       0.395
		Culture.Internet culture                     0.541
		Culture.Linguistics                          0.66
		Culture.Literature                           0.605
		Culture.Media.Books                          0.647
		Culture.Media.Entertainment                  0.398
		Culture.Media.Films                          0.823
		Culture.Media.Media*                         0.721
		Culture.Media.Music                          0.774
		Culture.Media.Radio                          0.727
		Culture.Media.Software                       0.3
		Culture.Media.Television                     0.779
		Culture.Media.Video games                    0.82
		Culture.Performing arts                      0.426
		Culture.Philosophy and religion              0.425
		Culture.Sports                               0.9
		Culture.Visual arts.Architecture             0.588
		Culture.Visual arts.Comics and Anime         0.72
		Culture.Visual arts.Fashion                  0.443
		Culture.Visual arts.Visual arts*             0.577
		Geography.Geographical                       0.569
		Geography.Regions.Africa.Africa*             0.561
		Geography.Regions.Africa.Central Africa      0.354
		Geography.Regions.Africa.Eastern Africa      0.348
		Geography.Regions.Africa.Northern Africa     0.403
		Geography.Regions.Africa.Southern Africa     0.526
		Geography.Regions.Africa.Western Africa      0.611
		Geography.Regions.Americas.Central America   0.371
		Geography.Regions.Americas.North America     0.701
		Geography.Regions.Americas.South America     0.644
		Geography.Regions.Asia.Asia*                 0.727
		Geography.Regions.Asia.Central Asia          0.348
		Geography.Regions.Asia.East Asia             0.769
		Geography.Regions.Asia.North Asia            0.534
		Geography.Regions.Asia.South Asia            0.718
		Geography.Regions.Asia.Southeast Asia        0.649
		Geography.Regions.Asia.West Asia             0.635
		Geography.Regions.Europe.Eastern Europe      0.687
		Geography.Regions.Europe.Europe*             0.654
		Geography.Regions.Europe.Northern Europe     0.648
		Geography.Regions.Europe.Southern Europe     0.526
		Geography.Regions.Europe.Western Europe      0.693
		Geography.Regions.Oceania                    0.738
		History and Society.Business and economics   0.483
		History and Society.Education                0.458
		History and Society.History                  0.356
		History and Society.Military and warfare     0.565
		History and Society.Politics and government  0.559
		History and Society.Society                  0.247
		History and Society.Transportation           0.86
		STEM.Biology                                 0.842
		STEM.Chemistry                               0.284
		STEM.Computing                               0.432
		STEM.Earth and environment                   0.476
		STEM.Engineering                             0.637
		STEM.Libraries & Information                 0.572
		STEM.Mathematics                             0.318
		STEM.Medicine & Health                       0.552
		STEM.Physics                                 0.262
		STEM.STEM*                                   0.755
		STEM.Space                                   0.881
		STEM.Technology                              0.349
		-------------------------------------------  -----
	!f1 (micro=0.987, macro=0.995):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.98
		Culture.Biography.Women                      0.995
		Culture.Food and drink                       0.998
		Culture.Internet culture                     0.997
		Culture.Linguistics                          0.997
		Culture.Literature                           0.993
		Culture.Media.Books                          0.998
		Culture.Media.Entertainment                  0.997
		Culture.Media.Films                          0.998
		Culture.Media.Media*                         0.981
		Culture.Media.Music                          0.995
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.997
		Culture.Media.Television                     0.998
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.998
		Culture.Philosophy and religion              0.993
		Culture.Sports                               0.994
		Culture.Visual arts.Architecture             0.996
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.992
		Geography.Geographical                       0.989
		Geography.Regions.Africa.Africa*             0.996
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      1
		Geography.Regions.Africa.Northern Africa     0.999
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      1
		Geography.Regions.Americas.Central America   0.998
		Geography.Regions.Americas.North America     0.982
		Geography.Regions.Americas.South America     0.998
		Geography.Regions.Asia.Asia*                 0.984
		Geography.Regions.Asia.Central Asia          0.999
		Geography.Regions.Asia.East Asia             0.997
		Geography.Regions.Asia.North Asia            0.996
		Geography.Regions.Asia.South Asia            0.996
		Geography.Regions.Asia.Southeast Asia        0.998
		Geography.Regions.Asia.West Asia             0.996
		Geography.Regions.Europe.Eastern Europe      0.994
		Geography.Regions.Europe.Europe*             0.962
		Geography.Regions.Europe.Northern Europe     0.991
		Geography.Regions.Europe.Southern Europe     0.991
		Geography.Regions.Europe.Western Europe      0.994
		Geography.Regions.Oceania                    0.996
		History and Society.Business and economics   0.995
		History and Society.Education                0.996
		History and Society.History                  0.988
		History and Society.Military and warfare     0.992
		History and Society.Politics and government  0.989
		History and Society.Society                  0.994
		History and Society.Transportation           0.998
		STEM.Biology                                 0.995
		STEM.Chemistry                               0.997
		STEM.Computing                               0.997
		STEM.Earth and environment                   0.997
		STEM.Engineering                             0.998
		STEM.Libraries & Information                 1
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.996
		STEM.Physics                                 0.998
		STEM.STEM*                                   0.98
		STEM.Space                                   0.999
		STEM.Technology                              0.993
		-------------------------------------------  -----
	accuracy (micro=0.976, macro=0.99):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.965
		Culture.Biography.Women                      0.99
		Culture.Food and drink                       0.996
		Culture.Internet culture                     0.995
		Culture.Linguistics                          0.995
		Culture.Literature                           0.987
		Culture.Media.Books                          0.997
		Culture.Media.Entertainment                  0.994
		Culture.Media.Films                          0.996
		Culture.Media.Media*                         0.964
		Culture.Media.Music                          0.991
		Culture.Media.Radio                          0.999
		Culture.Media.Software                       0.995
		Culture.Media.Television                     0.996
		Culture.Media.Video games                    0.999
		Culture.Performing arts                      0.996
		Culture.Philosophy and religion              0.987
		Culture.Sports                               0.988
		Culture.Visual arts.Architecture             0.991
		Culture.Visual arts.Comics and Anime         0.999
		Culture.Visual arts.Fashion                  0.999
		Culture.Visual arts.Visual arts*             0.985
		Geography.Geographical                       0.978
		Geography.Regions.Africa.Africa*             0.992
		Geography.Regions.Africa.Central Africa      0.999
		Geography.Regions.Africa.Eastern Africa      0.999
		Geography.Regions.Africa.Northern Africa     0.997
		Geography.Regions.Africa.Southern Africa     0.999
		Geography.Regions.Africa.Western Africa      0.999
		Geography.Regions.Americas.Central America   0.996
		Geography.Regions.Americas.North America     0.965
		Geography.Regions.Americas.South America     0.995
		Geography.Regions.Asia.Asia*                 0.97
		Geography.Regions.Asia.Central Asia          0.998
		Geography.Regions.Asia.East Asia             0.995
		Geography.Regions.Asia.North Asia            0.993
		Geography.Regions.Asia.South Asia            0.992
		Geography.Regions.Asia.Southeast Asia        0.996
		Geography.Regions.Asia.West Asia             0.992
		Geography.Regions.Europe.Eastern Europe      0.988
		Geography.Regions.Europe.Europe*             0.932
		Geography.Regions.Europe.Northern Europe     0.982
		Geography.Regions.Europe.Southern Europe     0.982
		Geography.Regions.Europe.Western Europe      0.987
		Geography.Regions.Oceania                    0.992
		History and Society.Business and economics   0.989
		History and Society.Education                0.993
		History and Society.History                  0.977
		History and Society.Military and warfare     0.984
		History and Society.Politics and government  0.978
		History and Society.Society                  0.989
		History and Society.Transportation           0.995
		STEM.Biology                                 0.99
		STEM.Chemistry                               0.994
		STEM.Computing                               0.994
		STEM.Earth and environment                   0.995
		STEM.Engineering                             0.995
		STEM.Libraries & Information                 0.999
		STEM.Mathematics                             0.999
		STEM.Medicine & Health                       0.993
		STEM.Physics                                 0.997
		STEM.STEM*                                   0.963
		STEM.Space                                   0.999
		STEM.Technology                              0.987
		-------------------------------------------  -----
	fpr (micro=0.016, macro=0.007):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.021
		Culture.Biography.Women                      0.006
		Culture.Food and drink                       0.003
		Culture.Internet culture                     0.004
		Culture.Linguistics                          0.002
		Culture.Literature                           0.009
		Culture.Media.Books                          0.002
		Culture.Media.Entertainment                  0.003
		Culture.Media.Films                          0.002
		Culture.Media.Media*                         0.03
		Culture.Media.Music                          0.004
		Culture.Media.Radio                          0
		Culture.Media.Software                       0.005
		Culture.Media.Television                     0.002
		Culture.Media.Video games                    0.001
		Culture.Performing arts                      0.002
		Culture.Philosophy and religion              0.008
		Culture.Sports                               0.004
		Culture.Visual arts.Architecture             0.004
		Culture.Visual arts.Comics and Anime         0.001
		Culture.Visual arts.Fashion                  0.001
		Culture.Visual arts.Visual arts*             0.008
		Geography.Geographical                       0.016
		Geography.Regions.Africa.Africa*             0.005
		Geography.Regions.Africa.Central Africa      0.001
		Geography.Regions.Africa.Eastern Africa      0.001
		Geography.Regions.Africa.Northern Africa     0.002
		Geography.Regions.Africa.Southern Africa     0.001
		Geography.Regions.Africa.Western Africa      0
		Geography.Regions.Americas.Central America   0.002
		Geography.Regions.Americas.North America     0.013
		Geography.Regions.Americas.South America     0.002
		Geography.Regions.Asia.Asia*                 0.018
		Geography.Regions.Asia.Central Asia          0.001
		Geography.Regions.Asia.East Asia             0.002
		Geography.Regions.Asia.North Asia            0.005
		Geography.Regions.Asia.South Asia            0.001
		Geography.Regions.Asia.Southeast Asia        0.002
		Geography.Regions.Asia.West Asia             0.004
		Geography.Regions.Europe.Eastern Europe      0.007
		Geography.Regions.Europe.Europe*             0.056
		Geography.Regions.Europe.Northern Europe     0.005
		Geography.Regions.Europe.Southern Europe     0.014
		Geography.Regions.Europe.Western Europe      0.007
		Geography.Regions.Oceania                    0.002
		History and Society.Business and economics   0.006
		History and Society.Education                0.002
		History and Society.History                  0.019
		History and Society.Military and warfare     0.011
		History and Society.Politics and government  0.009
		History and Society.Society                  0.005
		History and Society.Transportation           0.002
		STEM.Biology                                 0.003
		STEM.Chemistry                               0.006
		STEM.Computing                               0.006
		STEM.Earth and environment                   0.003
		STEM.Engineering                             0.003
		STEM.Libraries & Information                 0.001
		STEM.Mathematics                             0.001
		STEM.Medicine & Health                       0.005
		STEM.Physics                                 0.003
		STEM.STEM*                                   0.031
		STEM.Space                                   0.001
		STEM.Technology                              0.012
		-------------------------------------------  -----
	roc_auc (micro=0.967, macro=0.966):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.975
		Culture.Biography.Women                      0.978
		Culture.Food and drink                       0.971
		Culture.Internet culture                     0.985
		Culture.Linguistics                          0.968
		Culture.Literature                           0.97
		Culture.Media.Books                          0.981
		Culture.Media.Entertainment                  0.963
		Culture.Media.Films                          0.983
		Culture.Media.Media*                         0.977
		Culture.Media.Music                          0.98
		Culture.Media.Radio                          0.932
		Culture.Media.Software                       0.987
		Culture.Media.Television                     0.981
		Culture.Media.Video games                    0.988
		Culture.Performing arts                      0.962
		Culture.Philosophy and religion              0.94
		Culture.Sports                               0.978
		Culture.Visual arts.Architecture             0.974
		Culture.Visual arts.Comics and Anime         0.985
		Culture.Visual arts.Fashion                  0.961
		Culture.Visual arts.Visual arts*             0.956
		Geography.Geographical                       0.967
		Geography.Regions.Africa.Africa*             0.967
		Geography.Regions.Africa.Central Africa      0.974
		Geography.Regions.Africa.Eastern Africa      0.957
		Geography.Regions.Africa.Northern Africa     0.97
		Geography.Regions.Africa.Southern Africa     0.965
		Geography.Regions.Africa.Western Africa      0.882
		Geography.Regions.Americas.Central America   0.949
		Geography.Regions.Americas.North America     0.961
		Geography.Regions.Americas.South America     0.969
		Geography.Regions.Asia.Asia*                 0.962
		Geography.Regions.Asia.Central Asia          0.968
		Geography.Regions.Asia.East Asia             0.977
		Geography.Regions.Asia.North Asia            0.968
		Geography.Regions.Asia.South Asia            0.966
		Geography.Regions.Asia.Southeast Asia        0.966
		Geography.Regions.Asia.West Asia             0.968
		Geography.Regions.Europe.Eastern Europe      0.967
		Geography.Regions.Europe.Europe*             0.951
		Geography.Regions.Europe.Northern Europe     0.957
		Geography.Regions.Europe.Southern Europe     0.968
		Geography.Regions.Europe.Western Europe      0.967
		Geography.Regions.Oceania                    0.972
		History and Society.Business and economics   0.953
		History and Society.Education                0.953
		History and Society.History                  0.948
		History and Society.Military and warfare     0.963
		History and Society.Politics and government  0.942
		History and Society.Society                  0.888
		History and Society.Transportation           0.982
		STEM.Biology                                 0.977
		STEM.Chemistry                               0.984
		STEM.Computing                               0.985
		STEM.Earth and environment                   0.963
		STEM.Engineering                             0.976
		STEM.Libraries & Information                 0.968
		STEM.Mathematics                             0.956
		STEM.Medicine & Health                       0.973
		STEM.Physics                                 0.976
		STEM.STEM*                                   0.975
		STEM.Space                                   0.991
		STEM.Technology                              0.971
		-------------------------------------------  -----
	pr_auc (micro=0.74, macro=0.56):
		-------------------------------------------  -----
		Culture.Biography.Biography*                 0.917
		Culture.Biography.Women                      0.679
		Culture.Food and drink                       0.351
		Culture.Internet culture                     0.626
		Culture.Linguistics                          0.628
		Culture.Literature                           0.648
		Culture.Media.Books                          0.68
		Culture.Media.Entertainment                  0.292
		Culture.Media.Films                          0.857
		Culture.Media.Media*                         0.816
		Culture.Media.Music                          0.816
		Culture.Media.Radio                          0.505
		Culture.Media.Software                       0.284
		Culture.Media.Television                     0.758
		Culture.Media.Video games                    0.837
		Culture.Performing arts                      0.328
		Culture.Philosophy and religion              0.381
		Culture.Sports                               0.926
		Culture.Visual arts.Architecture             0.555
		Culture.Visual arts.Comics and Anime         0.673
		Culture.Visual arts.Fashion                  0.247
		Culture.Visual arts.Visual arts*             0.567
		Geography.Geographical                       0.58
		Geography.Regions.Africa.Africa*             0.548
		Geography.Regions.Africa.Central Africa      0.166
		Geography.Regions.Africa.Eastern Africa      0.153
		Geography.Regions.Africa.Northern Africa     0.344
		Geography.Regions.Africa.Southern Africa     0.363
		Geography.Regions.Africa.Western Africa      0.447
		Geography.Regions.Americas.Central America   0.303
		Geography.Regions.Americas.North America     0.772
		Geography.Regions.Americas.South America     0.617
		Geography.Regions.Asia.Asia*                 0.795
		Geography.Regions.Asia.Central Asia          0.249
		Geography.Regions.Asia.East Asia             0.798
		Geography.Regions.Asia.North Asia            0.551
		Geography.Regions.Asia.South Asia            0.771
		Geography.Regions.Asia.Southeast Asia        0.574
		Geography.Regions.Asia.West Asia             0.612
		Geography.Regions.Europe.Eastern Europe      0.743
		Geography.Regions.Europe.Europe*             0.757
		Geography.Regions.Europe.Northern Europe     0.694
		Geography.Regions.Europe.Southern Europe     0.575
		Geography.Regions.Europe.Western Europe      0.704
		Geography.Regions.Oceania                    0.788
		History and Society.Business and economics   0.423
		History and Society.Education                0.414
		History and Society.History                  0.36
		History and Society.Military and warfare     0.589
		History and Society.Politics and government  0.583
		History and Society.Society                  0.155
		History and Society.Transportation           0.875
		STEM.Biology                                 0.876
		STEM.Chemistry                               0.316
		STEM.Computing                               0.413
		STEM.Earth and environment                   0.398
		STEM.Engineering                             0.633
		STEM.Libraries & Information                 0.421
		STEM.Mathematics                             0.137
		STEM.Medicine & Health                       0.558
		STEM.Physics                                 0.204
		STEM.STEM*                                   0.877
		STEM.Space                                   0.913
		STEM.Technology                              0.407
		-------------------------------------------  -----
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'array', 'description': 'The most likely labels predicted by the estimator', 'items': {'type': 'string'}}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Geography.Regions.Africa.Southern Africa': {'type': 'number'}, 'Geography.Regions.Asia.West Asia': {'type': 'number'}, 'Geography.Regions.Africa.Central Africa': {'type': 'number'}, 'Geography.Regions.Americas.Central America': {'type': 'number'}, 'Culture.Media.Video games': {'type': 'number'}, 'Culture.Philosophy and religion': {'type': 'number'}, 'Culture.Biography.Women': {'type': 'number'}, 'STEM.Physics': {'type': 'number'}, 'STEM.Mathematics': {'type': 'number'}, 'Geography.Regions.Asia.East Asia': {'type': 'number'}, 'Culture.Visual arts.Fashion': {'type': 'number'}, 'Culture.Media.Books': {'type': 'number'}, 'Culture.Linguistics': {'type': 'number'}, 'Geography.Regions.Europe.Eastern Europe': {'type': 'number'}, 'Geography.Regions.Africa.Western Africa': {'type': 'number'}, 'STEM.Space': {'type': 'number'}, 'Geography.Regions.Europe.Northern Europe': {'type': 'number'}, 'Culture.Literature': {'type': 'number'}, 'History and Society.Transportation': {'type': 'number'}, 'STEM.Biology': {'type': 'number'}, 'Culture.Media.Media*': {'type': 'number'}, 'Culture.Media.Software': {'type': 'number'}, 'Geography.Regions.Africa.Northern Africa': {'type': 'number'}, 'Geography.Regions.Europe.Western Europe': {'type': 'number'}, 'Culture.Media.Radio': {'type': 'number'}, 'STEM.Medicine & Health': {'type': 'number'}, 'Culture.Biography.Biography*': {'type': 'number'}, 'History and Society.Military and warfare': {'type': 'number'}, 'Culture.Media.Entertainment': {'type': 'number'}, 'Culture.Sports': {'type': 'number'}, 'Geography.Regions.Asia.South Asia': {'type': 'number'}, 'Geography.Regions.Asia.North Asia': {'type': 'number'}, 'Geography.Regions.Asia.Central Asia': {'type': 'number'}, 'STEM.Technology': {'type': 'number'}, 'History and Society.History': {'type': 'number'}, 'STEM.Engineering': {'type': 'number'}, 'STEM.Computing': {'type': 'number'}, 'Geography.Regions.Europe.Southern Europe': {'type': 'number'}, 'Culture.Visual arts.Architecture': {'type': 'number'}, 'Culture.Food and drink': {'type': 'number'}, 'STEM.Chemistry': {'type': 'number'}, 'History and Society.Business and economics': {'type': 'number'}, 'STEM.Libraries & Information': {'type': 'number'}, 'Culture.Visual arts.Comics and Anime': {'type': 'number'}, 'Geography.Regions.Oceania': {'type': 'number'}, 'Culture.Performing arts': {'type': 'number'}, 'History and Society.Education': {'type': 'number'}, 'STEM.Earth and environment': {'type': 'number'}, 'Culture.Visual arts.Visual arts*': {'type': 'number'}, 'Culture.Media.Films': {'type': 'number'}, 'Geography.Regions.Americas.North America': {'type': 'number'}, 'Culture.Media.Music': {'type': 'number'}, 'STEM.STEM*': {'type': 'number'}, 'History and Society.Society': {'type': 'number'}, 'Geography.Regions.Africa.Eastern Africa': {'type': 'number'}, 'Culture.Internet culture': {'type': 'number'}, 'Geography.Geographical': {'type': 'number'}, 'Geography.Regions.Asia.Southeast Asia': {'type': 'number'}, 'Geography.Regions.Africa.Africa*': {'type': 'number'}, 'History and Society.Politics and government': {'type': 'number'}, 'Geography.Regions.Americas.South America': {'type': 'number'}, 'Culture.Media.Television': {'type': 'number'}, 'Geography.Regions.Europe.Europe*': {'type': 'number'}, 'Geography.Regions.Asia.Asia*': {'type': 'number'}}}}}

