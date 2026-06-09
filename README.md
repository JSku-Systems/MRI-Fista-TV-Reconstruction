# MRI Reconstruction with FISTA–TV and FastAPI Deployment

This repository presents a two‑part project implementing a classical compressed‑sensing MRI reconstruction pipeline and its transition into a modular software architecture.
The work is organised into four phases: Phases 1–3 (reconstruction methods and evaluation) are implemented in Notebook 1, and Phase 4 (software architecture and deployment) is implemented in Notebook 2.

## Notebook 1 — Compressed Sensing MRI Reconstruction (Phases 1–3)

Notebook 1 implements the classical compressed‑sensing MRI reconstruction pipeline, beginning with controlled phantom experiments and progressing to clinical validation. The workflow starts by constructing a forward model of accelerated MRI using a normalised Shepp–Logan phantom, simulating fully sampled k‑space, applying a Cartesian undersampling pattern, and introducing realistic Rician noise. These controlled experiments provide a reproducible environment for analysing aliasing artefacts and quantifying degradation using PSNR and SSIM.

The reconstruction problem is then formulated as a convex optimisation task combining a masked Fourier acquisition model with an edge‑preserving Total Variation prior. Reconstruction is performed using a FISTA–TV algorithm, which alternates between data‑consistency enforcement and a TV‑based proximal step. Experiments on clean and noisy phantom data demonstrate substantial suppression of aliasing artefacts and stable convergence behaviour, establishing a robust baseline for clinical evaluation.

The third phase applies the pipeline to real single‑coil knee MRI data, using a variable‑density Cartesian mask and a tuned FISTA–TV solver to reconstruct accelerated acquisitions. Quantitative metrics, error maps, and qualitative inspection confirm that the optimised configuration achieves stable convergence and effective artefact suppression under realistic acquisition conditions. Together, these phases establish a complete classical reconstruction workflow that forms the foundation for the deployment architecture developed in Notebook 2.

### Phase 3 Dataset Access & Citation

Notebook 1 uses the following dataset:

FLowOak/mri_knee ; Single‑coil knee MRI dataset (HDF5 format), hosted on Hugging Face derived from the fastMRI dataset (Zbontar et al., 2019).

Required file: `file1000254.h5`

This file is not included in this repository due to licensing restrictions.

Download instructions are provided on the dataset’s Hugging Face page:

https://huggingface.co/datasets/FLowOak/mri_knee

**Citations**
fastMRI (original dataset):  
Zbontar, J., Knoll, F., Sriram, A., et al.
fastMRI: An Open Dataset and Benchmarks for Accelerated MRI.  
arXiv:1811.08839, 2018.

FLowOak/mri_knee (derivative dataset):  
FLowOak.
MRI Knee Dataset (Single‑Coil).  
Hugging Face, 2025.
url : https://huggingface.co/datasets/FLowOak/mri_knee

## Notebook 2 — MRI Software Architecture and Deployment (Phase 4)
This notebook implements Phase 4, transitioning the reconstruction pipeline into a modular software component:

* FastAPI service exposing a reconstruction endpoint

* Integration of the FISTA–TV solver into a callable interface

* Pydantic‑based input validation

* Local API testing

* Optional Docker container for reproducible execution

This phase demonstrates how a reconstruction method can be structured for integration, experimentation, or downstream tooling.



