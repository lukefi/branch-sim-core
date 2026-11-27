from typing import Sequence

from bscore.model import ComputationalUnit
from bscore.sim_control import Preprocessing
from bscore.runners import evaluate_sequence


def preprocess_units[T: ComputationalUnit](units: Sequence[T], control: Preprocessing[T]) -> Sequence[T]:
    return evaluate_sequence(units, *control.operations)
