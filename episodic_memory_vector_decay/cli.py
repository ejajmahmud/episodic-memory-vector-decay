"""CLI for Episodic Memory Vector Decay."""
import argparse
from .core import EpisodicMemoryDecay

def main():
    parser = argparse.ArgumentParser(description="Episodic Memory Vector Decay CLI")
    parser.add_argument("--demo", action="store_true", help="Run episodic memory decay demo")
    args = parser.parse_args()

    mem = EpisodicMemoryDecay(decay_lambda=0.1)
    mem.store("m1", "Server deploy completed on AWS us-east-1", importance=1.0)
    mem.store("m2", "User asked about lunch recommendations", importance=0.3)

    results = mem.recall("server")
    print(f"Recalled {len(results)} memory items for query 'server':")
    for r in results:
        print(f"  [{r.item_id}] Weight: {r.effective_weight(0.1)} | Content: {r.content}")

if __name__ == "__main__":
    main()
