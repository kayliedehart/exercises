# Automated unit tests for the feed test harness for Evolution game
import unittest
import xfeed
import species
import trait
import json

#NOTE: Unittests will not run unless the call to the main function is commented out in xfeed's init
class TestXFeed(unittest.TestCase):
  def setUp(self):
    self.tester_xfeed = xfeed.TestHarness()
    self.case_0623_8070_3_in = [
                                 [
                                      [
                                           "id",
                                           1
                                      ],
                                      [
                                           "species",
                                           [
                                                [
                                                     [
                                                          "food",
                                                          0
                                                     ],
                                                     [
                                                          "body",
                                                          0
                                                     ],
                                                     [
                                                          "population",
                                                          2
                                                     ],
                                                     [
                                                          "traits",
                                                          []
                                                     ]
                                                ],
                                                [
                                                     [
                                                          "food",
                                                          2
                                                     ],
                                                     [
                                                          "body",
                                                          1
                                                     ],
                                                     [
                                                          "population",
                                                          2
                                                     ],
                                                     [
                                                          "traits",
                                                          [
                                                               "fat-tissue"
                                                          ]
                                                     ],
                                                     [
                                                          "fat-food",
                                                          1
                                                     ]
                                                ],
                                                [
                                                     [
                                                          "food",
                                                          2
                                                     ],
                                                     [
                                                          "body",
                                                          0
                                                     ],
                                                     [
                                                          "population",
                                                          2
                                                     ],
                                                     [
                                                          "traits",
                                                          [
                                                               "carnivore"
                                                          ]
                                                     ]
                                                ]
                                           ]
                                      ],
                                      [
                                           "bag",
                                           0
                                      ]
                                 ],
                                 1,
                                 [
                                      [
                                           [
                                                "id",
                                                2
                                           ],
                                           [
                                                "species",
                                                [
                                                     [
                                                          [
                                                               "food",
                                                               0
                                                          ],
                                                          [
                                                               "body",
                                                               0
                                                          ],
                                                          [
                                                               "population",
                                                               1
                                                          ],
                                                          [
                                                               "traits",
                                                               []
                                                          ]
                                                     ]
                                                ]
                                           ],
                                           [
                                                "bag",
                                                0
                                           ]
                                      ],
                                      [
                                           [
                                                "id",
                                                3
                                           ],
                                           [
                                                "species",
                                                [
                                                     [
                                                          [
                                                               "food",
                                                               0
                                                          ],
                                                          [
                                                               "body",
                                                               0
                                                          ],
                                                          [
                                                               "population",
                                                               1
                                                          ],
                                                          [
                                                               "traits",
                                                               []
                                                          ]
                                                     ]
                                                ]
                                           ],
                                           [
                                                "bag",
                                                0
                                           ]
                                      ]
                                 ]
                            ]
    self.case_0623_8070_3_out = 0

    self.case_0623_8070_5_in = [
                           [
                                [
                                     "id",
                                     1
                                ],
                                [
                                     "species",
                                     [
                                          [
                                               [
                                                    "food",
                                                    0
                                               ],
                                               [
                                                    "body",
                                                    0
                                               ],
                                               [
                                                    "population",
                                                    1
                                               ],
                                               [
                                                    "traits",
                                                    [
                                                         "carnivore"
                                                    ]
                                               ]
                                          ],
                                          [
                                               [
                                                    "food",
                                                    0
                                               ],
                                               [
                                                    "body",
                                                    0
                                               ],
                                               [
                                                    "population",
                                                    1
                                               ],
                                               [
                                                    "traits",
                                                    [
                                                         "carnivore"
                                                    ]
                                               ]
                                          ],
                                          [
                                               [
                                                    "food",
                                                    2
                                               ],
                                               [
                                                    "body",
                                                    0
                                               ],
                                               [
                                                    "population",
                                                    2
                                               ],
                                               [
                                                    "traits",
                                                    [
                                                         "carnivore"
                                                    ]
                                               ]
                                          ],
                                          [
                                               [
                                                    "food",
                                                    3
                                               ],
                                               [
                                                    "body",
                                                    0
                                               ],
                                               [
                                                    "population",
                                                    3
                                               ],
                                               [
                                                    "traits",
                                                    []
                                               ]
                                          ]
                                     ]
                                ],
                                [
                                     "bag",
                                     0
                                ]
                           ],
                           4,
                           [
                                [
                                     [
                                          "id",
                                          2
                                     ],
                                     [
                                          "species",
                                          [
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         1
                                                    ],
                                                    [
                                                         "population",
                                                         2
                                                    ],
                                                    [
                                                         "traits",
                                                         []
                                                    ]
                                               ],
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         0
                                                    ],
                                                    [
                                                         "population",
                                                         2
                                                    ],
                                                    [
                                                         "traits",
                                                         []
                                                    ]
                                               ]
                                          ]
                                     ],
                                     [
                                          "bag",
                                          0
                                     ]
                                ],
                                [
                                     [
                                          "id",
                                          3
                                     ],
                                     [
                                          "species",
                                          [
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         0
                                                    ],
                                                    [
                                                         "population",
                                                         2
                                                    ],
                                                    [
                                                         "traits",
                                                         []
                                                    ]
                                               ],
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         1
                                                    ],
                                                    [
                                                         "population",
                                                         2
                                                    ],
                                                    [
                                                         "traits",
                                                         [
                                                              "carnivore"
                                                         ]
                                                    ]
                                               ]
                                          ]
                                     ],
                                     [
                                          "bag",
                                          0
                                     ]
                                ],
                                [
                                     [
                                          "id",
                                          4
                                     ],
                                     [
                                          "species",
                                          [
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         0
                                                    ],
                                                    [
                                                         "population",
                                                         1
                                                    ],
                                                    [
                                                         "traits",
                                                         []
                                                    ]
                                               ],
                                               [
                                                    [
                                                         "food",
                                                         0
                                                    ],
                                                    [
                                                         "body",
                                                         0
                                                    ],
                                                    [
                                                         "population",
                                                         1
                                                    ],
                                                    [
                                                         "traits",
                                                         [
                                                              "warning-call",
                                                              "hard-shell"
                                                         ]
                                                    ]
                                               ]
                                          ]
                                     ],
                                     [
                                          "bag",
                                          0
                                     ]
                                ]
                           ]
                      ]
    self.case_0623_8070_5_out = [0, 0, 1]

    self.case_1073_6112_5_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 5],
                                      ["body", 2],
                                      ["population", 5],
                                      ["traits", ["horns"]]
                                    ],
                              [
                                      ["food", 0],
                                      ["body", 2],
                                      ["population", 4],
                                      ["traits", ["carnivore"]]
                                    ]
                                  ]
                              ],
                                  ["bag", 3]
                                ],
                                5, [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 3],
                                        ["body", 2],
                                        ["population", 3],
                                        ["traits", ["burrowing", "horns"]]
                                      ]
                                    ]],
                                    ["bag", 3]
                                  ]
                                ]
                              ]
    self.case_1073_6112_5_out = 'false'

    self.case_1073_6112_6_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 1],
                                      ["body", 2],
                                      ["population", 3],
                                      ["traits", ["carnivore", "horns"]]
                                    ],
                              [
                                      ["food", 0],
                                      ["body", 2],
                                      ["population", 4],
                                      ["traits", ["carnivore", "ambush"]]
                                    ]
                                  ]
                              ],
                                  ["bag", 1]
                                ],
                                5, [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 3],
                                        ["body", 2],
                                        ["population", 7],
                                        ["traits", ["climbing", "ambush"]]
                                      ],
                              [
                                        ["food", 3],
                                        ["body", 2],
                                        ["population", 3],
                                        ["traits", ["fertile", "carnivore"]]
                                      ]
                                    ]],
                                    ["bag", 6]
                                  ],
                              [
                                    ["id", 3],
                                    ["species", [
                                      [
                                        ["food", 0],
                                        ["body", 2],
                                        ["population", 3],
                                        ["traits", ["burrowing", "horns"]]
                                      ],
                              [
                                        ["food", 3],
                                        ["body", 2],
                                        ["population", 5],
                                        ["traits", ["pack-hunting", "long-neck"]]
                                      ]
                                    ]],
                                    ["bag", 3]
                                  ],
                              [
                                    ["id", 4],
                                    ["species", [
                                      [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 7],
                                        ["traits", ["burrowing", "foraging"]]
                                      ],
                              [
                                        ["food", 3],
                                        ["body", 2],
                                        ["population", 3],
                                        ["traits", ["warning-call", "hard-shell"]]
                                      ]
                                    ]],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1073_6112_6_out = '[1, 0, 1]'

    self.case_1073_6112_7_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 1],
                                      ["body", 2],
                                      ["population", 3],
                                      ["traits", ["carnivore", "horns"]]
                                    ],
                                    [
                                      ["food", 1],
                                      ["body", 3],
                                      ["population", 3],
                                      ["traits", ["carnivore", "ambush"]]
                                    ]
                                  ]],
                                  ["bag", 1]
                                ],
                                5, [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["ambush"]]
                                      ],
                              [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["fertile"]]
                                      ]
                                    ]],
                                    ["bag", 6]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", [
                                      [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["horns"]]
                                      ],
                              [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["symbiosis"]]
                                      ]
                                    ]],
                                    ["bag", 3]
                                  ],
                                  [
                                    ["id", 4],
                                    ["species", [
                                      [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["foraging"]]
                                      ],
                              [
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 1],
                                        ["traits", ["long-neck"]]
                                      ]
                                    ]],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1073_6112_7_out = '[1, 0, 0]'

    self.case_1606_4071_1_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 0],
                                        ["body", 0],
                                        ["population", 1],
                                        ["traits",[]]
                                      ],
                                      [
                                        ["food", 0],
                                        ["body", 0],
                                        ["population", 1],
                                        ["traits",[]]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species",
                                      [
                                        [
                                          ["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1606_4071_1_out = '0'

    self.case_1606_4071_4_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 2],
                                        ["body", 5],
                                        ["population", 2],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 3]
                                      ],
                                      [
                                        ["food", 2],
                                        ["body", 2],
                                        ["population", 2],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 0]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species",
                                      [
                                        [
                                          ["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1606_4071_4_out = '[0, 2]'
    self.case_1606_4071_7_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 2],
                                        ["body", 5],
                                        ["population", 2],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 3]
                                      ],
                                      [
                                        ["food", 2],
                                        ["body", 7],
                                        ["population", 7],
                                        ["traits",[]]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species",
                                      [
                                        [
                                          ["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1606_4071_7_out = '[0, 2]'
    self.case_1606_4071_8_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 2],
                                        ["body", 5],
                                        ["population", 2],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 3]
                                      ],
                                      [
                                        ["food", 2],
                                        ["body", 5],
                                        ["population", 3],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 3]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species",
                                      [
                                        [
                                          ["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1606_4071_8_out = '[0, 2]'

    self.case_1606_4071_9_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 7],
                                        ["body", 7],
                                        ["population", 7],
                                        ["traits",[]]
                                      ],
                                      [
                                        ["food", 1],
                                        ["body", 0],
                                        ["population", 7],
                                        ["traits",[]]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species",
                                      [
                                        [
                                          ["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_1606_4071_9_out = '1'

    self.case_1606_4071_10_in = [
                                  [
                                    ["id", 1],
                                    ["species",
                                      [
                                        [
                                          ["food", 2],
                                          ["body", 2],
                                          ["population", 6],
                                          ["traits",[]]
                                        ],
                                        [
                                          ["food", 1],
                                          ["body", 0],
                                          ["population", 7],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ],
                                  10,
                                  [
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 0],
                                            ["body", 0],
                                            ["population", 1],
                                            ["traits",[]]
                                          ]
                                        ]
                                      ],
                                      ["bag", 0]
                                    ]
                                  ]
                                ]
    self.case_1606_4071_10_out =  '1'

    self.case_1606_4071_11_in = [
                                  [
                                    ["id", 1],
                                    ["species",
                                      [
                                        [
                                          ["food", 2],
                                          ["body", 2],
                                          ["population", 6],
                                          ["traits",[]]
                                        ],
                                        [
                                          ["food", 1],
                                          ["body", 3],
                                          ["population", 6],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ],
                                  10,
                                  [
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 0],
                                            ["body", 0],
                                            ["population", 1],
                                            ["traits",[]]
                                          ]
                                        ]
                                      ],
                                      ["bag", 0]
                                    ]
                                  ]
                                ]
    self.case_1606_4071_11_out =  '0'

    self.case_1606_4071_12_in = [
                                  [
                                    ["id", 1],
                                    ["species",
                                      [
                                        [
                                          ["food", 2],
                                          ["body", 2],
                                          ["population", 6],
                                          ["traits",[]]
                                        ],
                                        [
                                          ["food", 2],
                                          ["body", 3],
                                          ["population", 6],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ],
                                  10,
                                  [
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 0],
                                            ["body", 0],
                                            ["population", 1],
                                            ["traits",[]]
                                          ]
                                        ]
                                      ],
                                      ["bag", 0]
                                    ]
                                  ]
                                ]
    self.case_1606_4071_12_out = '1'

    self.case_1606_4071_13_in = [
                                  [
                                    ["id", 1],
                                    ["species",
                                      [
                                        [
                                          ["food", 2],
                                          ["body", 2],
                                          ["population", 6],
                                          ["traits",[]]
                                        ],
                                        [
                                          ["food", 6],
                                          ["body", 2],
                                          ["population", 6],
                                          ["traits",[]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ],
                                  10,
                                  [
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 0],
                                            ["body", 0],
                                            ["population", 1],
                                            ["traits",[]]
                                          ]
                                        ]
                                      ],
                                      ["bag", 0]
                                    ]
                                  ]
                                ]
    self.case_1606_4071_13_out = '0'

    self.case_1606_4071_20_in = [
                                  [
                                    ["id", 1],
                                    ["species",
                                      [
                                        [
                                          ["food", 1],
                                          ["body", 1],
                                          ["population", 3],
                                          ["traits",["carnivore"]]
                                        ],
                                        [
                                          ["food", 2],
                                          ["body", 1],
                                          ["population", 3],
                                          ["traits",["carnivore"]]
                                        ]
                                      ]
                                    ],
                                    ["bag", 0]
                                  ],
                                  10,
                                  [
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 1],
                                            ["body", 1],
                                            ["population", 1],
                                            ["traits",["burrowing"]]
                                          ]
                                        ]
                                      ],
                                      ["bag", 0]
                                    ]
                                  ]
                                ]
    self.case_1606_4071_20_out = 'false'

    self.case_2198_0067_3_in = [
                                [
                                  ["id", 2],
                                  ["species",
                                    [[
                                      ["food", 1],
                                      ["body", 1],
                                      ["population", 5],
                                      ["traits", ["burrowing"]]
                                    ],
                                    [
                                      ["food", 1],
                                      ["body", 1],
                                      ["population", 3],
                                      ["traits", ["foraging"]]
                                    ],
                                    [
                                      ["food", 2],
                                      ["body", 3],
                                      ["population", 7],
                                      ["traits", ["fat-tissue"]],
                                      ["fat-food", 1]
                                    ]
                                  ]],
                                  ["bag", 1]
                                ],
                                10,
                                [
                                  [["id", 1],
                                    ["species", []],
                                    ["bag", 0]]
                                ]
                              ]
    self.case_2198_0067_3_out = '[2, 2]'

    self.case_2198_0067_6_in = [
                                [
                                  ["id", 3],
                                  ["species",
                                    [
                                    [
                                      ["food", 1],
                                      ["body", 1],
                                      ["population", 3],
                                      ["traits", ["herding"]]
                                    ],
                                    [
                                      ["food", 1],
                                      ["body", 4],
                                      ["population", 6],
                                      ["traits", ["carnivore"]]
                                    ],
                                    [
                                      ["food", 1],
                                      ["body", 1],
                                      ["population", 3],
                                      ["traits", ["foraging"]]
                                    ],[
                                      ["food", 1],
                                      ["body", 1],
                                      ["population", 5],
                                      ["traits", ["burrowing"]]
                                    ]
                                  ]],
                                  ["bag", 1]
                                ],
                                10,
                                [
                                  [
                                    ["id", 4],
                                    ["species",
                                      [[
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 6],
                                        ["traits", ["symbiosis"]]
                                      ],
                                      [
                                        ["food", 1],
                                        ["body", 4],
                                        ["population", 5],
                                        ["traits", ["herding"]]
                                      ]
                                    ]],
                                    ["bag", 5]
                                  ],
                                  [
                                    ["id", 5],
                                    ["species",
                                      [[
                                        ["food", 1],
                                        ["body", 5],
                                        ["population", 6],
                                        ["traits", ["scavenger"]]
                                      ],
                                      [
                                        ["food", 1],
                                        ["body", 4],
                                        ["population", 5],
                                        ["traits", ["symbiosis"]]
                                      ],
                                      [
                                        ["food", 5],
                                        ["body", 5],
                                        ["population", 5],
                                        ["traits", ["burrowing"]]
                                      ]
                                    ]],
                                    ["bag", 5]
                                  ],
                                  [
                                    ["id", 6],
                                    ["species",
                                      [[
                                        ["food", 1],
                                        ["body", 2],
                                        ["population", 3],
                                        ["traits", ["symbiosis"]]
                                      ],
                                      [
                                        ["food", 1],
                                        ["body", 5],
                                        ["population", 6],
                                        ["traits", ["foraging"]]
                                      ]
                                    ]],
                                    ["bag", 5]
                                  ]
                                ]
                              ]
    self.case_2198_0067_6_out = '3'

    self.case_2598_8949_1_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 2],
                                      ["body", 2],
                                      ["population", 3],
                                      ["traits", ["carnivore"]]
                                    ]]
                                  ],
                                  ["bag", 1]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 3],
                                        ["population", 4],
                                        ["traits", ["climbing", "burrowing"]]
                                    ]]
                                  ],
                                    ["bag", 2]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 2],
                                        ["population", 2],
                                        ["traits", ["climbing", "burrowing"]]
                                      ]]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_2598_8949_1_out = 'false'

    self.case_2598_8949_2_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 2],
                                      ["body", 2],
                                      ["population", 3],
                                      ["traits", []]
                                    ],
                                    [
                                      ["food", 2],
                                      ["body", 2],
                                      ["population", 5],
                                      ["traits", []]
                                    ]
                                    ]
                                  ],
                                  ["bag", 1]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 3],
                                        ["population", 4],
                                        ["traits", ["climbing", "burrowing"]]
                                    ]]
                                  ],
                                    ["bag", 2]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 2],
                                        ["population", 2],
                                        ["traits", ["climbing", "burrowing"]]
                                      ]]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_2598_8949_2_out = '1'

    self.case_2598_8949_3_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 2],
                                      ["body", 2],
                                      ["population", 3],
                                      ["traits", ["fat-tissue"]]
                                    ],
                                    [
                                      ["food", 2],
                                      ["body", 2],
                                      ["population", 5],
                                      ["traits", []]
                                    ]
                                    ]
                                  ],
                                  ["bag", 1]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 3],
                                        ["population", 4],
                                        ["traits", ["climbing", "carnivore"]]
                                    ]]
                                  ],
                                    ["bag", 2]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", [
                                      [
                                        ["food", 2],
                                        ["body", 2],
                                        ["population", 2],
                                        ["traits", ["climbing", "burrowing"]]
                                      ]]
                                    ],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_2598_8949_3_out = '[0, 2]'

    self.case_3461_8179_1_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 0],
                                      ["body", 0],
                                      ["population", 2],
                                      ["traits", ["carnivore"]]
                                    ],
                                    [
                                      ["food", 4],
                                      ["body", 3],
                                      ["population", 4],
                                      ["traits", ["fat-tissue"]],
                                      ["fat-food", 3]
                                    ]
                                  ]],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", [
                                      [
                                        ["food", 0],
                                        ["body", 1],
                                        ["population", 3],
                                        ["traits", ["climbing"]]
                                      ]
                                    ]],
                                    ["bag", 3]
                                  ]
                                ]
                              ]
    self.case_3461_8179_1_out = 'false'

    self.case_3461_8179_6_in = [
                                [
                                  ["id", 1],
                                  ["species", [
                                    [
                                      ["food", 0],
                                      ["body", 0],
                                      ["population", 2],
                                      ["traits", []]],
                                    [
                                      ["food", 0],
                                      ["body", 0],
                                      ["population", 2],
                                      ["traits", []]],
                                    [
                                      ["food", 3],
                                      ["body", 3],
                                      ["population", 6],
                                      ["traits", ["burrowing"]]],
                                    [
                                      ["food", 3],
                                      ["body", 3],
                                      ["population", 6],
                                      ["traits", []]]
                                  ]],
                                  ["bag", 5]],
                                15,
                                [
                                  [
                                    ["id", 2],
                                    ["species", []],
                                    ["bag", 3]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", []],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_3461_8179_6_out = '2'

    self.case_3830_7214_3_in = [[["id",10],
                                  ["species",[[["food",0],
                                               ["body",1],
                                               ["population",1],
                                               ["traits",[]]]]],
                                  ["bag",10]],
                                 7,
                                 [[["id",11],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",[]]]]],
                                   ["bag",10]],
                                  [["id",12],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",[]]]]],
                                   ["bag",10]]]]
    self.case_3830_7214_3_out = '0'

    self.case_3830_7214_4_in = [[["id",10],
                                ["species",[[["food",1],
                                             ["body",1],
                                             ["population",1],
                                             ["traits",[]]]]],
                                ["bag",10]],
                               7,
                               [[["id",11],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]],
                                [["id",12],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]]]]
    self.case_3830_7214_4_out = None

    self.case_3830_7214_7_in = [[["id",10],
                                ["species",[[["food",1],
                                             ["body",4],
                                             ["population",1],
                                             ["traits",["fat-tissue"]],
                                             ["fat-food",2]]]],
                                ["bag",10]],
                               12,
                               [[["id",11],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]],
                                [["id",12],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]]]]
    self.case_3830_7214_7_out = '[0, 2]'

    self.case_3830_7214_8_in = [[["id",10],
                                ["species",[[["food",1],
                                             ["body",4],
                                             ["population",1],
                                             ["traits",["fat-tissue"]],
                                             ["fat-food",4]]]],
                                ["bag",10]],
                               12,
                               [[["id",11],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]],
                                [["id",12],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",[]]]]],
                                 ["bag",10]]]]
    self.case_3830_7214_8_out = None

    self.case_3830_7214_9_in = [[["id",10],
                                ["species",[[["food",0],
                                               ["body",1],
                                               ["population",1],
                                               ["traits",["carnivore"]]],
                                            [["food",1],
                                             ["body",1],
                                             ["population",1],
                                             ["traits",[]]]]],
                                ["bag",10]],
                               7,
                               [[["id",11],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",["burrowing"]]]]],
                                 ["bag",10]],
                                [["id",12],
                                 ["species",[[["food",1],
                                              ["body",1],
                                              ["population",1],
                                              ["traits",["burrowing"]]]]],
                                 ["bag",10]]]]
    self.case_3830_7214_9_out = 'false'

    self.case_3830_7214_13_in = [[["id",10],
                                  ["species",[[["food",1],
                                               ["body",2],
                                               ["population",1],
                                               ["traits",["fat-tissue"]],
                                               ["fat-food",1]],
                                              [["food",1],
                                               ["body",5],
                                               ["population",1],
                                               ["traits",["fat-tissue"]],
                                               ["fat-food",1]]]],
                                  ["bag",10]],
                                 7,
                                 [[["id",11],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",[]]]]],
                                   ["bag",10]],
                                  [["id",12],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",[]]]]],
                                   ["bag",10]]]]
    self.case_3830_7214_13_out = '[1, 4]'

    self.case_3830_7214_14_in = [[["id",10],
                                  ["species",[[["food",0],
                                               ["body",5],
                                               ["population",1],
                                               ["traits",[]]],
                                              [["food",0],
                                               ["body",2],
                                               ["population",1],
                                               ["traits",[]]]]],
                                  ["bag",10]],
                                 7,
                                 [[["id",11],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",["burrowing"]]]]],
                                   ["bag",10]],
                                  [["id",12],
                                   ["species",[[["food",1],
                                                ["body",1],
                                                ["population",1],
                                                ["traits",["burrowing"]]]]],
                                   ["bag",10]]]]
    self.case_3830_7214_14_out = '0'

    self.case_5223_6080_2_in = [[["id",1],
                                ["species",
                                    [[["food",0],
                                    ["body",4],
                                    ["population",2],
                                    ["traits",
                                      ["carnivore"]]]]],
                                ["bag",0]],
                               10,
                               [[["id",2],
                                 ["species",
                                    [[["food",1],
                                  ["body",3],
                                      ["population",3],
                                  ["traits",
                                      ["herding"]]],
                                   [["food",1],
                                  ["body",2],
                                  ["population",4],
                                  ["traits",
                                      ["carnivore", "ambush"]]]]],
                                 ["bag",0]],

                                 [["id",3],
                                  ["species",
                                    [[["food",0],
                                    ["body",1],
                                    ["population",2],
                                    ["traits",[]]]]],
                                  ["bag",0]]]]
    self.case_5223_6080_2_out = '[0, 0, 1]'

    self.case_5223_6080_3_in = [[["id",1],
                                  ["species",
                                     [[["food",0],
                                     ["body",1],
                                     ["population",1],
                                     ["traits",
                                        ["symbiosis"]]],
                                    [["food",0],
                                     ["body",3],
                                       ["population",1],
                                       ["traits",
                                       ["warning-call"]]]]],
                                  ["bag",0]],
                                  10,
                                  [[["id",2],
                                    ["species",
                                       [[["food",2],
                                     ["body",2],
                                     ["population",2],
                                     ["traits",[]]],
                                    [["food",0],
                                     ["body",1],
                                     ["population",1],
                                     ["traits", []]]]],
                                    ["bag",0]],

                                   [["id",3],
                                    ["species",
                                       [[["food",0],
                                     ["body",1],
                                     ["population",1],
                                     ["traits",[]]]]],
                                    ["bag",0]]]]
    self.case_5223_6080_3_out = '1'

    self.case_6118_3959_1_in = [[["id", 1], ["species", [[["food", 1], ["body", 2], ["population", 4], ["traits", ["fat-tissue", "carnivore"]], ["fat-food", 2]], [["food", 1], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case_6118_3959_1_out = '[0, 0, 0]'

    self.case_6118_3959_2_in = [[["id", 1], ["species",
             [[["food", 2], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 2]],
            [["food", 1], ["body", 2], ["population", 2], ["traits", ["carnivore"]]]]], ["bag", 2]], 10,
            [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case_6118_3959_2_out = '[1, 0, 0]'


    self.case_6118_3959_3_in = [[["id", 1], ["species", [[["food", 1], ["body", 6], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 2]], [["food", 1], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 2, [[["id", 3], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case_6118_3959_3_out = '[0, 2]'

    self.case_6118_3959_4_in = [[["id", 1], ["species", [[["food", 1], ["body", 2], ["population", 5], ["traits", ["carnivore"]]], [["food", 1], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]], [["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 3]], [["id", 3], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 3]]]]
    self.case_6118_3959_4_out = '[0, 0, 0]'

    self.case_6118_3959_5_in = [[["id", 1], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 1]], [["food", 1], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 1]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case_6118_3959_5_out = '[0, 1]'

    self.case_7013_1976_1_in = [
                                [
                                  [
                                    "id",
                                    1
                                  ],
                                  [
                                    "species",
                                    [
                                      [
                                        [
                                          "food",
                                          2
                                        ],
                                        [
                                          "body",
                                          2
                                        ],
                                        [
                                          "population",
                                          3
                                        ],
                                        [
                                          "traits",
                                          []
                                        ]
                                      ],
                                      [
                                        [
                                          "food",
                                          3
                                        ],
                                        [
                                          "body",
                                          4
                                        ],
                                        [
                                          "population",
                                          6
                                        ],
                                        [
                                          "traits",
                                          []
                                        ]
                                      ]
                                    ]
                                  ],
                                  [
                                    "bag",
                                    2
                                  ]
                                ],
                                3,
                                [
                                  [
                                    [
                                      "id",
                                      2
                                    ],
                                    [
                                      "species",
                                      []
                                    ],
                                    [
                                      "bag",
                                      0
                                    ]
                                  ],
                                  [
                                    [
                                      "id",
                                      3
                                    ],
                                    [
                                      "species",
                                      []
                                    ],
                                    [
                                      "bag",
                                      0
                                    ]
                                  ]
                                ]
                              ]
    self.case_7013_1976_1_out = '1'

    self.case_7013_1976_3_in = [[["id", 1], ["species", [[["food", 2], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 3, [[["id", 2], ["species", [[["food", 3], ["body", 4], ["population", 6], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]]]
    self.case_7013_1976_3_out = '[0, 0, 0]'

    self.case_7013_1976_4_in = [
                                [
                                  [
                                    "id",
                                    1
                                  ],
                                  [
                                    "species",
                                    [
                                      [
                                        [
                                          "food",
                                          2
                                        ],
                                        [
                                          "body",
                                          2
                                        ],
                                        [
                                          "population",
                                          3
                                        ],
                                        [
                                          "traits",
                                          [
                                            "carnivore"
                                          ]
                                        ]
                                      ],
                                      [
                                        [
                                          "food",
                                          3
                                        ],
                                        [
                                          "body",
                                          4
                                        ],
                                        [
                                          "population",
                                          6
                                        ],
                                        [
                                          "traits",
                                          [
                                            "carnivore"
                                          ]
                                        ]
                                      ]
                                    ]
                                  ],
                                  [
                                    "bag",
                                    2
                                  ]
                                ],
                                3,
                                [
                                  [
                                    [
                                      "id",
                                      2
                                    ],
                                    [
                                      "species",
                                      []
                                    ],
                                    [
                                      "bag",
                                      0
                                    ]
                                  ],
                                  [
                                    [
                                      "id",
                                      3
                                    ],
                                    [
                                      "species",
                                      []
                                    ],
                                    [
                                      "bag",
                                      0
                                    ]
                                  ]
                                ]
                              ]
    self.case_7013_1976_4_out = 'false'

    self.case_7013_1976_5_in = [[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", []]], [["food", 3], ["body", 4], ["population", 6], ["traits", ["carnivore"]]]]], ["bag", 2]], 3, [[["id", 2], ["species", [[["food", 2], ["body", 3], ["population", 3], ["traits", []]]]], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]]]
    self.case_7013_1976_5_out = '[1, 0, 0]'

    self.case_7391_9951_1_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 5],
                                        ["body", 5],
                                        ["population", 5],
                                        ["traits", []],
                                        ["fat-food", 0]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", []],
                                    ["bag", 0]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", []],
                                    ["bag", 0]
                                  ],
                                  [
                                    ["id", 4],
                                    ["species", []],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_7391_9951_1_out = None

    self.case_7391_9951_2_in = [
                                [
                                  ["id", 1],
                                  ["species",
                                    [
                                      [
                                        ["food", 2],
                                        ["body", 2],
                                        ["population", 4],
                                        ["traits", ["fat-tissue"]],
                                        ["fat-food", 0]
                                      ],
                                      [
                                        ["food", 1],
                                        ["body", 3],
                                        ["population", 5],
                                        ["traits", ["fat-tissue"]],
                                        ["fat-food", 1]
                                      ]
                                    ]
                                  ],
                                  ["bag", 0]
                                ],
                                10,
                                [
                                  [
                                    ["id", 2],
                                    ["species", []],
                                    ["bag", 0]
                                  ],
                                  [
                                    ["id", 3],
                                    ["species", []],
                                    ["bag", 0]
                                  ],
                                  [
                                    ["id", 4],
                                    ["species", []],
                                    ["bag", 0]
                                  ]
                                ]
                              ]
    self.case_7391_9951_2_out = '[1, 2]'

    self.case_7920_7167_4_in = [
                                [["id", 1],
                                ["species", [[["food", 3],
                                   ["body", 5],
                                   ["population", 7],
                                   ["traits", ["carnivore", "scavenger"]]],
                                  [["food", 0],
                                   ["body", 3],
                                   ["population", 6],
                                   ["traits", ["scavenger", "fat-tissue"]],
                                   ["fat-food", 1]],
                                  [["food", 1],
                                   ["body", 4],
                                   ["population", 3],
                                   ["traits", ["fertile", "long-neck", "scavenger"]]]]],
                                ["bag", 3]],

                                12,

                                []]
    self.case_7920_7167_4_out = '[1, 2]'

    self.case_7920_7167_5_in = [
                                [["id", 1],
                                ["species", [
                                      [["food", 1],
                                   ["body", 4],
                                   ["population", 7],
                                   ["traits", ["fertile", "long-neck", "scavenger"]]],
                                   [["food", 0],
                                   ["body", 3],
                                   ["population", 6],
                                   ["traits", ["scavenger"]]],
                                   [["food", 3],
                                   ["body", 5],
                                   ["population", 4],
                                   ["traits", ["carnivore", "scavenger"]]]
                                  ]],
                                ["bag", 3]],

                                12,

                                []]
    self.case_7920_7167_5_out = '0'

    self.case_7920_7167_14_in = [
                                  [["id", 1],
                                  ["species", [[["food", 3],
                                     ["body", 5],
                                     ["population", 7],
                                     ["traits", ["carnivore", "scavenger"]]],
                                    [["food", 0],
                                     ["body", 3],
                                     ["population", 6],
                                     ["traits", ["scavenger", "fat-tissue"]],
                                     ["fat-food", 1]],
                                    [["food", 1],
                                     ["body", 4],
                                     ["population", 3],
                                     ["traits", ["fertile", "long-neck", "scavenger"]]]]],
                                  ["bag", 3]],

                                  12,

                                  []]
    self.case_7920_7167_14_out = '[1, 2]'

    self.case_7920_7167_15_in = [
                                  [["id", 1],
                                  ["species", [
                                        [["food", 1],
                                     ["body", 4],
                                     ["population", 7],
                                     ["traits", ["fertile", "long-neck", "scavenger"]]],
                                     [["food", 0],
                                     ["body", 3],
                                     ["population", 6],
                                     ["traits", ["scavenger"]]],
                                     [["food", 3],
                                     ["body", 5],
                                     ["population", 4],
                                     ["traits", ["carnivore", "scavenger"]]]
                                    ]],
                                  ["bag", 3]],

                                  12,

                                  []]
    self.case_7920_7167_15_out = '0'

    self.case_matthias_1_in = [[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],1,[]]
    self.case_matthias_1_out ='0'

    self.case_matthias_2_in = [[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],1,[]]
    self.case_matthias_2_out = '0'

    self.case_matthias_3_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[]]
    self.case_matthias_3_out = 'false'

    self.case_matthias_4_in = [[["id",2],
                                ["species",
                                [[["food",0],
                                  ["body",3],
                                  ["population",1],
                                  ["traits",["carnivore"]]],
                                [["food",1],
                                  ["body",3],
                                  ["population",1],
                                  ["traits",[]]]]],
                                ["bag",0]], 1,
                              [[["id",100],
                                ["species",[]],
                                ["bag",0]],
                               [["id",3],
                                ["species",
                                  [[["food",0],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",["climbing"]]]]],
                                ["bag",0]],
                               [["id",1],
                                ["species",
                                  [[["food",0],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",[]]],
                                   [["food",1],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",[]]],
                                   [["food",0],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",["carnivore"]]]]],
                                  ["bag",0]]]]
    self.case_matthias_4_out = '[0, 2, 1]'

    self.case_matthias_5_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],
                                        [["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],
                                        1,[[["id",100],["species",[]],["bag",0]],[["id",3],["species",[[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],
                                        [["id",4],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],
                                        [["id",5],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],
                                        [["id",6],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]]]
    self.case_matthias_5_out = '[0, 1, 0]'

    self.case_matthias_6_in = [[["id",7],
                                ["species",
                                  [[["food",0],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",[]]],
                                  [["food",0],
                                    ["body",2],
                                    ["population",3],
                                    ["traits",["fat-tissue"]]],
                                  [["food",1],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",[]]],
                                  [["food",0],
                                    ["body",3],
                                    ["population",1],
                                    ["traits",["carnivore"]]]]],
                                ["bag",0]],
                                2,
                                [[["id",100],
                                  ["species",[]],
                                  ["bag",0]]]]
    self.case_matthias_6_out = '[1, 2]'

    self.case_matthias_7_in = [[["id",8],["species",[[["food",0],["body",2],["population",3],["traits",["fat-tissue"]]],[["food",0],["body",5],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],2,[[["id",100],["species",[]],["bag",0]]]]
    self.case_matthias_7_out = '[1, 2]'

    self.case_matthias_8_in = [[["id",9],["species",[[["food",0],["body",3],["population",2],["traits",["fat-tissue"]]],[["food",0],["body",3],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],2,[]]
    self.case_matthias_8_out = '[1, 2]'

    self.case_matthias_9_in = [[["id",10],["species",[[["food",0],["body",3],["population",3],["traits",["fat-tissue","climbing"]]],[["food",0],["body",3],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],3,[]]
    self.case_matthias_9_out = '[0, 3]'

    self.case_matthias_10_in = [[["id",11],["species",[[["food",3],["body",3],["population",3],["traits",["fat-tissue","climbing"]],["fat-food",2]]]],["bag",0]],3,[]]
    self.case_matthias_10_out = '[0, 1]'

    self.case_matthias_11_in = [[["id",11],["species",[[["food",3],["body",3],["population",3],["traits",["fat-tissue","climbing"]],["fat-food",1]]]],["bag",0]],2,[]]
    self.case_matthias_11_out = '[0, 2]'

    self.case_failing_input = [[["id",11],
                                ["species",
                                  [[["food",3],
                                    ["body",3],
                                    ["population",3],
                                    ["traits",
                                      ["fat-tissue","climbing"]],
                                    ["fat-food",2]]]],
                                ["bag",0]],
                                3,
                                []]
    self.case_failing_output = '[0, 1]'

  def tearDown(self):
    del self.case_0623_8070_3_in
    del self.case_0623_8070_3_out
    del self.case_0623_8070_5_in
    del self.case_0623_8070_5_out

    del self.case_1073_6112_5_in
    del self.case_1073_6112_5_out
    del self.case_1073_6112_6_in
    del self.case_1073_6112_6_out
    del self.case_1073_6112_7_in
    del self.case_1073_6112_7_out

    del self.case_1606_4071_1_in
    del self.case_1606_4071_1_out
    del self.case_1606_4071_4_in
    del self.case_1606_4071_4_out
    del self.case_1606_4071_7_in
    del self.case_1606_4071_7_out
    del self.case_1606_4071_8_in
    del self.case_1606_4071_8_out
    del self.case_1606_4071_9_in
    del self.case_1606_4071_9_out
    del self.case_1606_4071_10_in
    del self.case_1606_4071_10_out
    del self.case_1606_4071_11_in
    del self.case_1606_4071_11_out
    del self.case_1606_4071_12_in
    del self.case_1606_4071_12_out
    del self.case_1606_4071_13_in
    del self.case_1606_4071_13_out
    del self.case_1606_4071_20_in
    del self.case_1606_4071_20_out

    del self.case_2198_0067_3_in
    del self.case_2198_0067_3_out
    del self.case_2198_0067_6_in
    del self.case_2198_0067_6_out

    del self.case_2598_8949_1_in
    del self.case_2598_8949_1_out
    del self.case_2598_8949_2_in
    del self.case_2598_8949_2_out
    del self.case_2598_8949_3_in
    del self.case_2598_8949_3_out

    del self.case_3461_8179_1_in
    del self.case_3461_8179_1_out
    del self.case_3461_8179_6_in
    del self.case_3461_8179_6_out

    del self.case_3830_7214_3_in
    del self.case_3830_7214_3_out
    del self.case_3830_7214_4_in
    del self.case_3830_7214_4_out
    del self.case_3830_7214_7_in
    del self.case_3830_7214_7_out
    del self.case_3830_7214_8_in
    del self.case_3830_7214_8_out
    del self.case_3830_7214_9_in
    del self.case_3830_7214_9_out
    del self.case_3830_7214_13_in
    del self.case_3830_7214_13_out
    del self.case_3830_7214_14_in
    del self.case_3830_7214_14_out

    del self.case_5223_6080_2_in
    del self.case_5223_6080_2_out
    del self.case_5223_6080_3_in
    del self.case_5223_6080_3_out

    del self.case_6118_3959_1_in
    del self.case_6118_3959_1_out
    del self.case_6118_3959_2_in
    del self.case_6118_3959_2_out
    del self.case_6118_3959_3_in
    del self.case_6118_3959_3_out
    del self.case_6118_3959_4_in
    del self.case_6118_3959_4_out
    del self.case_6118_3959_5_in
    del self.case_6118_3959_5_out

    del self.case_7013_1976_1_in
    del self.case_7013_1976_1_out
    del self.case_7013_1976_3_in
    del self.case_7013_1976_3_out
    del self.case_7013_1976_4_in
    del self.case_7013_1976_4_out
    del self.case_7013_1976_5_in
    del self.case_7013_1976_5_out

    del self.case_7391_9951_1_in
    del self.case_7391_9951_1_out
    del self.case_7391_9951_2_in
    del self.case_7391_9951_2_out

    del self.case_7920_7167_4_in
    del self.case_7920_7167_4_out
    del self.case_7920_7167_5_in
    del self.case_7920_7167_5_out
    del self.case_7920_7167_14_in
    del self.case_7920_7167_14_out
    del self.case_7920_7167_15_in
    del self.case_7920_7167_15_out

    del self.case_matthias_1_in
    del self.case_matthias_1_out
    del self.case_matthias_2_in
    del self.case_matthias_2_out
    del self.case_matthias_3_in
    del self.case_matthias_3_out
    del self.case_matthias_4_in
    del self.case_matthias_4_out
    del self.case_matthias_5_in
    del self.case_matthias_5_out
    del self.case_matthias_6_in
    del self.case_matthias_6_out
    del self.case_matthias_7_in
    del self.case_matthias_7_out
    del self.case_matthias_8_in
    del self.case_matthias_8_out
    del self.case_matthias_9_in
    del self.case_matthias_9_out
    del self.case_matthias_10_in
    del self.case_matthias_10_out
    del self.case_matthias_11_in
    del self.case_matthias_11_out

    del self.case_failing_input

  # def test_0623_8070(self):
  #   #this test breaks the sequencing constraints because there is only one hungery species and it's a herbavore
  #   #which is illegal according to the specs.
  #   #self.assertEqual(self.tester_xfeed.testMethod(self.case_0623_8070_3_in), self.case_0623_8070_3_out)
  #   pass

  # def test_1073_6112(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1073_6112_5_in), self.case_1073_6112_5_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1073_6112_6_in), self.case_1073_6112_6_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1073_6112_7_in), self.case_1073_6112_7_out)

  # def test_160_4071(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_1_in), self.case_1606_4071_1_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_4_in), self.case_1606_4071_4_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_7_in), self.case_1606_4071_7_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_8_in), self.case_1606_4071_8_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_9_in), self.case_1606_4071_9_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_10_in), self.case_1606_4071_10_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_11_in), self.case_1606_4071_11_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_12_in), self.case_1606_4071_12_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_13_in), self.case_1606_4071_13_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_1606_4071_20_in), self.case_1606_4071_20_out)

  # def test_2198_0067(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_2198_0067_3_in), self.case_2198_0067_3_out)
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_2198_0067_6_in), self.case_2198_0067_6_out)

  # def test_mattias1(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_1_in), self.case_matthias_1_out)

  # def test_mattias2(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_2_in), self.case_matthias_2_out)

  # def test_mattias3(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_3_in), self.case_matthias_3_out)

  # def test_mattias4(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_4_in), self.case_matthias_4_out)

  # def test_mattias5(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_5_in), self.case_matthias_5_out)

  # def test_mattias6(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_6_in), self.case_matthias_6_out)

  # def test_mattias7(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_7_in), self.case_matthias_7_out)

  # def test_mattias8(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_8_in), self.case_matthias_8_out)

  # def test_mattias9(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_9_in), self.case_matthias_9_out)

  # def test_mattias10(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_10_in), self.case_matthias_10_out)

  # def test_mattias11(self):
  #   self.assertEqual(self.tester_xfeed.testMethod(self.case_matthias_11_in), self.case_matthias_11_out)

  def test_failing_json(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case_failing_input), self.case_failing_output)

if __name__ == '__main__':
    unittest.main()