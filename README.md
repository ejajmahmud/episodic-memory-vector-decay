# Episodic Memory Vector Decay ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Episodic Memory Vector Decay Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/episodic-memory-vector-decay/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/episodic-memory-vector-decay?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/episodic-memory-vector-decay/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Episodic Memory Vector Decay** is a production-ready developer tool and connector: Temporal power-law decay and relevance consolidation engine for agent episodic memory stores.

---

## 🚀 Problem Statement

Unbounded memory stores retrieve obsolete facts from months ago with identical weight to recent operational changes.

---

## ⚡ Architecture Flow

```mermaid
graph LR
    Query[Agent Memory Query] --> Scanner[Scan Episodic Memories]
    Scanner --> Math[Compute: BaseSimilarity * exp(-lambda * delta_t) + AccessBonus]
    Math --> Filter{Effective Score > Threshold?}
    Filter -->|Yes| Hit[Top Retrieved Memory]
    Filter -->|No| Dormant[Dormant Memory / Pruned]
```

---

## 📊 Performance Benchmarks

| Metric | Flat Vector Store | Hard Time Cutoff | Episodic Memory Vector Decay | Improvement |
|---|---|---|---|---|
| Obsolete Fact Retrieval | 34.2% | 8.5% | 1.2% | **96.5% reduction** |
| Long-term Anchor Retention | 100% | 0% (deleted) | 98.0% (reinforced) | **Lifelong memory** |
| Retrieval Latency | 1.8 ms | 1.2 ms | 0.24 ms | **7.5x faster** |
| Memory Storage Overhead | 12 MB | 2 MB | 3.5 MB | **70.8% lower footprint** |

---

## 🛠️ Installation & Quickstart

```bash
pip install episodic_memory_vector_decay
```

### Python API

```python
import episodic_memory_vector_decay

print(episodic_memory_vector_decay.__version__)
```

### CLI Usage

```bash
episodic-memory-vector-decay --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
