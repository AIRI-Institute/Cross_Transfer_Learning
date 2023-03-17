import json
import os
import pathlib
from collections import defaultdict
from datetime import datetime
from typing import Any

import numpy as np


class ProbingLog(defaultdict):
    def __init__(self, *args, **kwargs):
        super(ProbingLog, self).__init__(ProbingLog, *args, **kwargs)
        self.start_time = ProbingLog.get_time()
        self.results_folder = pathlib.Path(
            pathlib.Path().resolve(), f"tl_results/experiment_{self.start_time}"
        )

    def __repr__(self):
        return repr(dict(self))

    def add(self, key: Any, value: Any):
        if key not in self:
            self[key] = []
        self[key].append(value)

    @staticmethod
    def get_time() -> str:
        return datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

    @staticmethod
    def myconverter(obj: Any) -> Any:
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, datetime):
            return obj.__str__()
        if isinstance(obj, pathlib.PosixPath):
            return obj.__str__()
        return obj

    def save_log(self) -> os.PathLike:
        log_path = pathlib.Path(self.results_folder, "log.json")

        with open(log_path, "w") as outfile:
            json.dump(self, outfile, indent=4, default=ProbingLog.myconverter)
        return log_path
