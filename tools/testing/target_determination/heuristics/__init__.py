from typing import List

from tools.testing.target_determination.heuristics.correlated_with_historical_failures import (
    CorrelatedWithHistoricalFailures,
)
from tools.testing.target_determination.heuristics.edited_by_pr import EditedByPR
from tools.testing.target_determination.heuristics.historical_edited_files import (
    HistorialEditedFiles,
)

from tools.testing.target_determination.heuristics.interface import (
    AggregatedHeuristics as AggregatedHeuristics,
    HeuristicInterface as HeuristicInterface,
    TestPrioritizations as TestPrioritizations,
)

from tools.testing.target_determination.heuristics.previously_failed_in_pr import (
    PreviouslyFailedInPR,
)
from tools.testing.target_determination.heuristics.profiling import Profiling
from tools.testing.target_determination.heuristics.random_baseline import RandomBaseline

# All currently running heuristics.
# To add a heurstic in trial mode, specify the keywork argument `trial_mode=True`.
HEURISTICS: List[HeuristicInterface] = [
    PreviouslyFailedInPR(),
    EditedByPR(),
    CorrelatedWithHistoricalFailures(),
    HistorialEditedFiles(trial_mode=True),
    Profiling(trial_mode=True),
    RandomBaseline(trial_mode=True),
]
