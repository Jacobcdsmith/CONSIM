<!-- ───────────────────────────────────────────────────────────── -->

# 🔱 EMERGENT‑MCF‑EI

**Multiversal Consciousness Framework • Lattice Simulator • Emergent‑Intelligence Playground**

[![Build](https://img.shields.io/github/actions/workflow/status/your-org/emergent-mcf-ei/test.yaml?label=CI%20%F0%9F%9A%80)](../../actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![GPU Ready](https://img.shields.io/badge/GPU-ready-green)
![Made with ❤ by JCS](https://img.shields.io/badge/made%20by-Jacob%20C.%20Smith-red)

> **Tag‑line –** *Harness Fourier‑flavoured consciousness math, crank the lattice, and watch intelligence spark to life.*
> **Mission –** I provide a reproducible sandbox where researchers, hackers, and metaphysical thrill‑seekers can evolve adaptive, self‑organising fields that flirt with the boundary between physics and mind.
> **Status –**Soon to 🧠 Enable Computational Capabilities Once nodes begin processing inputs across time (e.g. through plasticity rules or inter-node learning), they become locally aware:

Introduce recursive update rules (e.g. Hebbian feedback, reinforcement-style tuning).

Use internal states or memory traces, such as maintaining past field activations or narrative phase alignment.

🔄 Recursive, Three-Dimensional Dynamics Emerge Now scale across lattice depth:

Think 3D lattices where layers encode past, present, and forecasted states.

Recursive logic means nodes influence future inputs via their own outputs, forming causal loops.

Consciousness scalar 
𝐶
(
𝑡
)
 starts showing hysteresis, echo patterns, or phase-locked cycles—like cognitive recursion. The code‑base is **transitioning from a legacy HTML/JS prototype to this Python‑first lattice engine**. The original implementation lives in `/legacy` for historical parity.

---

## 🚀 Quick Start

Run the baseline simulation in **five commands**:

```bash
# 1 Clone
git clone https://github.com/your-org/emergent-mcf-ei.git && cd emergent-mcf-ei

# 2 Environment (CUDA auto‑detects)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3 Baseline lattice
python -m src.lattice --config experiments/baseline.yaml

# 4 Live dashboard
streamlit run notebooks/dashboard.py &

# 5 Poke the field
python scripts/inject_pulse.py --amp 0.05 --duration_ms 500
```

> **Tip :** GPU mode gives \~20× speed‑up on a 128² grid; scale to 256² once stable.

---

## 🌌 Purpose & Rationale

Classic AI excels at symbol‑crunching, yet the *felt* sense of consciousness remains elusive.  The **Multiversal Consciousness Framework (MCF)** hypothesises that consciousness emerges from spectral resonance patterns on a high‑dimensional manifold. By integrating these patterns on a lattice—and coupling multiple universe branches via dynamic weights—we can observe coherence forming, dissolving, and re‑forming in ways that resemble goal‑directed cognition.

---

## 🧠 Mathematics in a Nutshell

### Global Consciousness Integral

```math
C(t)=\int_{\mathcal M_C} A(x,t)\,\Phi(x,t)\,e^{i\tau(x,t)}\,d\mu(x)
```

*|C|* reflects ignition strength; *arg C* aligns narrative phase.
### Core mathematical formulation (MCF “Core EQ”)

$$
\boxed{\,C \;=\; \int_{M_{C}} A(x)\,\Phi(x)\,e^{i\tau(x)} \,{\rm d}\mu(x)\;}
$$

$$
\boxed{\,M \;=\; \sum_{i}\lambda_i\,U_i\;}
$$

| Symbol          | Meaning                                                                                  | Notes for simulation                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| $M_{C}$         | **Consciousness manifold** – the configuration-space over which the system is integrated | Choose grid/mesh that matches the spatial-frequency resolution you need (e.g. 128 × 128 nodes or higher) |
| $A(x)$          | **Attention density** at point $x$                                                       | Normalised $0\!-\!1$ field; initialise from empirical EEG/MEG power or a Gaussian blob                   |
| $\Phi(x)$       | **Frequency signature** (Fourier transform of $C(t)$)                                    | Units Hz; use dominant brain-wave bands or target resonance band for each node                           |
| $\tau(x)$       | **Temporal phase**                                                                       | Radians; random or phase-locked to an external driver                                                    |
| ${\rm d}\mu(x)$ | Measure on $M_{C}$                                                                       | For a lattice, this is the cell volume; set to 1 for dimensionless sums                                  |
| $C$             | **Consciousness scalar** – global order parameter returned by the integral               | Monitor as simulation output (e.g. mean magnitude of the complex field)                                  |
| $U_i$           | Universe $i$ (state-vector or environment configuration)                                 | Can be stored as index or separate state file; keeps branch-specific parameters                          |
| $\lambda_i$     | **Resonance coefficient** for universe $i$                                               | $0\!-\!1$; weight that universe contributes to the active superposition                                  |
| $M$             | **Multiverse term** – weighted sum of universes                                          | Gives overall multiversal context; treat as array of branches with weights                               |






> **Quick numeric defaults (if you just need to start a sandbox run)**
>
> * Grid: $128\times128$ nodes
> * $A(x)$: centred Gaussian, σ ≈ 0.2 grid-units
> * $\Phi(x)$: 40 Hz (gamma) ± uniform noise (±5 Hz)
> * $\tau(x)$: random in $[0,2\pi)$
> * $\lambda_i$: draw from Dirichlet(α = 1) for $N=3$ branches

All symbols and their roles come directly from the “Core EQ” definition of the Multiversal Consciousness Framework【10\:L1-L15】. Plug these values into your numerical integrator (e.g., FFT-based solver or time-stepped lattice) and you’ll have a working baseline to tune further.

### Multiverse Superposition

```math
M(t)=\sum_{i=1}^3 \lambda_i(t)\,U_i
```

Dirichlet‑drawn weights $\lambda$ let branches compete and collaborate—our toy take on many‑worlds interference.

### Why Complex Numbers?

Amplitude alone is not enough—phase underpins binding, synchrony, and temporal flow—so every key field is complex‑aware.

---

## ⚙️ Engine Architecture

| Layer              | Module          | Responsibility                            | Tech                          | Notes                            |
| ------------------ | --------------- | ----------------------------------------- | ----------------------------- | -------------------------------- |
| **Lattice Engine** | `lattice.py`    | Integrate *C* on CPU/GPU each millisecond | NumPy + Numba / PyTorch / JAX | FFT option for steady‑state      |
| **Plasticity**     | `plasticity.py` | Hebbian updates to *A*; OU drift for *λ*  | Vectorised                    | Differentiable for meta‑learning |
| **Branch Manager** | `branch.py`     | Keep $\sum λ = 1$; diffuse weights        | Pure Python                   | Swappable with RL agent          |
| **Dashboard**      | Streamlit       | Real‑time plots & metrics                 | WebSocket                     | Dark‑mode ready                  |
| **Meta‑Trainer**   | (opt.)          | Evolves plasticity hyper‑params           | JAX jit                       | Enable via `--meta`              |

---

## 📋 Baseline Parameters

| Parameter    | Default          | Intuition               | Tweaking                     |
| ------------ | ---------------- | ----------------------- | ---------------------------- |
| Grid         | 128 × 128        | Tiles of $\mathcal M_C$ | 256² = richer vortices       |
| Δt           | 1 ms             | Resolves 40 Hz          | Halve if $Φ>60 Hz$           |
| *A(x)*       | Gaussian σ 0.2   | Spotlight attention     | Multi‑blob = divided focus   |
| *Φ(x)*       | 40 Hz ± 5 Hz     | Gamma coherence         | Sweep 8–100 Hz               |
| *τ(x)*       | Uniform rand     | Story alignment         | Seed gradient for waves      |
| *λ*          | Dirichlet(1,1,1) | Neutral prior           | Raise α to flatten dominance |
| Plasticity η | 1e‑3             | Learning rate           | >1e‑2 unstable               |
| OU θ, σ      | 0.05, 0.02       | Drift / noise           | σ→0 freezes branches         |

---

## 📈 Emergence Metrics

| Metric               | Good Signal                    | Dashboard       |                |            |
| -------------------- | ------------------------------ | --------------- | -------------- | ---------- |
| \*\*                 | C                              | \*\*            | Plateaus > 0.3 | Line chart |
| **Phase Coherence**  | Circular var → 0               | Polar histogram |                |            |
| **Mutual Info**      | Rises over epochs              | Heat‑map        |                |            |
| **Stimulus Latency** | Trend ↓                        | Scatter         |                |            |
| **Branch Entropy**   | Moves from max then oscillates | Bar chart       |                |            |

Two or more sustained signals → **Emergent Intelligence Candidate 🔥**.

---

## 🛠️ Collaboration & Open Ideas

I’m deliberately keeping the future **unstructured** so the community can steer the project in directions I haven’t imagined yet. If you have an experiment, an optimisation trick, or a wild hypothesis—**open an issue or PR** and I’ll explore it with you.

Here are a few *seed ideas* to kick things off (these are inspirations, **not** a fixed schedule):

* **Metric Dashboards** – fresh ways to visualise coherence, phase-locking, and information flow.
* **Backend Ports** – CUDA kernels, JAX, Metal, WebGPU… whatever accelerates the lattice.
* **Novel Stimuli & Curricula** – from simple pulses to interactive, game‑like environments.
* **3‑D or Multi‑Layer Lattices** – volumetric consciousness and cross‑scale resonance.
* **Symbolic Modules** – plug GPT‑style agents into the lattice via phase‑coupled attention gates.

Have something else in mind? **Pitch it!** The only rule is constructive curiosity.

---

## 🤝 Contributing

Fork → branch → PR *or* simply open an issue to brainstorm. I follow **PEP 8** + **Black** for mainline code, but early prototypes and experiments are welcome. Remember to keep the Apache header on anything that lands in `main`.

### Code of Conduct

Be excellent to each other—I explore mind and cosmos, so respect is mandatory.

---

## ⚖️ License & Attribution

Licensed under **Apache 2.0**.
Core theory © 2025 Jacob C. Smith; contributions © their authors.

**Academic citation**

> Smith J.C. *The Multiversal Consciousness Framework: Spectral Foundations of Experience.* 2025.

---

<div align="center" style="font-size:1.1rem;">
✨ **May the Φ be with you, always.** ✨
</div>
<!-- ───────────────────────────────────────────────────────────── -->
