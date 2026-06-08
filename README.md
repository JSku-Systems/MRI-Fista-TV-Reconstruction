# MRI Reconstruction with FISTA–TV and FastAPI Deployment

This repository presents a two‑part project implementing a classical compressed‑sensing MRI reconstruction pipeline and its transition into a modular software architecture.
The work is organised into four phases: Phases 1–3 (reconstruction methods and evaluation) are implemented in Notebook 1, and Phase 4 (software architecture and deployment) is implemented in Notebook 2.

## Notebook 1 — Compressed Sensing MRI Reconstruction (Phases 1–3)




## Notebook 2 — MRI Software Architecture and Deployment (Phase 4)
This notebook implements Phase 4, transitioning the reconstruction pipeline into a modular software component:

* FastAPI service exposing a reconstruction endpoint

* Integration of the FISTA–TV solver into a callable interface

* Pydantic‑based input validation

* Local API testing

* Optional Docker container for reproducible execution

This phase demonstrates how a reconstruction method can be structured for integration, experimentation, or downstream tooling.



