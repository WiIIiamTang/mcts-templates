import math
import sys

def uct_score(n, fct: float=math.sqrt(2)) -> float:
    return sys.float_info.max if (n.plays == 0) else (
        (n.score/n.plays)+(fct*math.sqrt(math.log(n.parent.plays)/(n.plays)))
    )
