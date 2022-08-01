"""
Calculate Georgia's weighted average mark
Subject                       | Mark | Credit Points |
------------------------------+------+---------------+
Probability and Distributions | 65   | 4             |
Statistical Inference         | 81   | 4             |
Regression I                  | 78   | 6             |
Regression II                 | 76   | 6             |
"""
nume = (65*4) + (81 *4) + (78 * 6) + (76 * 6)
deno = 4 + 4 + 6 + 6

print(nume / deno)