"""Core Episodic Memory Vector Decay implementation."""
import time
import math
from typing import List, Dict, Any, Optional

class MemoryItem:
    def __init__(self, item_id: str, content: str, importance: float = 1.0):
        self.item_id = item_id
        self.content = content
        self.importance = importance
        self.created_at = time.time()
        self.last_accessed = self.created_at
        self.access_count = 1

    def effective_weight(self, decay_lambda: float = 0.05, current_time: Optional[float] = None) -> float:
        now = current_time or time.time()
        delta_t = max(0.0, now - self.last_accessed)
        decay = math.exp(-decay_lambda * delta_t)
        reinforcement = 1.0 + (0.2 * math.log(self.access_count + 1))
        return round(self.importance * decay * reinforcement, 4)

class EpisodicMemoryDecay:
    def __init__(self, decay_lambda: float = 0.05):
        self.decay_lambda = decay_lambda
        self.memories: Dict[str, MemoryItem] = {}

    def store(self, item_id: str, content: str, importance: float = 1.0) -> MemoryItem:
        item = MemoryItem(item_id, content, importance)
        self.memories[item_id] = item
        return item

    def recall(self, query_keyword: str, min_weight: float = 0.2) -> List[MemoryItem]:
        now = time.time()
        matched = []
        for item in self.memories.values():
            if query_keyword.lower() in item.content.lower():
                w = item.effective_weight(self.decay_lambda, current_time=now)
                if w >= min_weight:
                    item.access_count += 1
                    item.last_accessed = now
                    matched.append(item)

        matched.sort(key=lambda m: m.effective_weight(self.decay_lambda), reverse=True)
        return matched
