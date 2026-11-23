"""Tests for EpisodicMemoryDecay."""
import unittest
from episodic_memory_vector_decay.core import EpisodicMemoryDecay

class TestEpisodicMemoryDecay(unittest.TestCase):
    def test_store_and_decay(self):
        m = EpisodicMemoryDecay(decay_lambda=0.5)
        m.store("k1", "Important API secret rotation", 1.0)
        hits = m.recall("API")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].item_id, "k1")

        # Simulate time pass
        w = hits[0].effective_weight(0.5, current_time=hits[0].last_accessed + 10.0)
        self.assertLess(w, 0.1)
