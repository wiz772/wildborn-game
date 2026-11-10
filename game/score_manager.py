import game.persistence.storage as storage
from datetime import datetime, timezone
import copy

class ScoreManager():
    def __init__(self):
        self.scores = storage.get_score_data(storage.get_data_from_json())

    def add_new_score(self, time_elapsed):
        new_score = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "time_elapsed": time_elapsed
        }
        self.scores.append(new_score)

    def save_score(self):
        data = {
            "scores": self.scores
        }
        storage.write_data(data)

    def get_scores(self):
        return copy.deepcopy(self.scores)

    def get_best_time(self):
        return max((score["time_elapsed"] for score in self.scores), default=0)
