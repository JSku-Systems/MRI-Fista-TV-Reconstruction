# MRI Reconstruction with FISTA–TV and FastAPI Deployment

This project implements a classical compressed‑sensing MRI reconstruction workflow and shows how an exploratory computational imaging pipeline can be organised into a structured software system. Notebook 1 develops the reconstruction method, beginning with controlled phantom experiments and extending to clinical validation using a FISTA–TV solver. Notebook 2 builds on this foundation by packaging the reconstruction logic into a modular software architecture with a programmatic interface, API service, and containerised execution environment.

## Notebook 1 — Compressed Sensing MRI Reconstruction (Phases 1–3)

Notebook 1 implements the classical compressed‑sensing MRI reconstruction pipeline, beginning with controlled phantom experiments and progressing to clinical validation. The workflow starts by constructing a forward model of accelerated MRI using a normalised Shepp–Logan phantom, simulating fully sampled k‑space, applying a Cartesian undersampling pattern, and introducing realistic Rician noise. These controlled experiments provide a reproducible environment for analysing aliasing artefacts and quantifying degradation using PSNR and SSIM.

The reconstruction problem is then formulated as a convex optimisation task combining a masked Fourier acquisition model with an edge‑preserving Total Variation prior. Reconstruction is performed using a FISTA–TV algorithm, which alternates between data‑consistency enforcement and a TV‑based proximal step. Experiments on clean and noisy phantom data demonstrate substantial suppression of aliasing artefacts and stable convergence behaviour, providing a baseline for clinical evaluation that follows.

The third phase applies the pipeline to real single‑coil knee MRI data, using a variable‑density Cartesian mask and a tuned FISTA–TV solver to reconstruct accelerated acquisitions. Quantitative metrics, error maps, and qualitative inspection confirm that the optimised configuration achieves stable convergence and effective artefact suppression under realistic acquisition conditions. Together, these phases establish a complete classical reconstruction workflow that forms the foundation for the deployment architecture developed in Notebook 2.

### Phase 3 Dataset Access

Notebook 1 uses the following dataset:

FLowOak/mri_knee ; Single‑coil knee MRI dataset (HDF5 format), hosted on Hugging Face derived from the fastMRI dataset (Zbontar et al., 2019).

Required file: `file1000254.h5`

This file is not included in this repository due to licensing restrictions.

Download instructions are provided on the dataset’s Hugging Face page:

https://huggingface.co/datasets/FLowOak/mri_knee

### References

**fastMRI (original dataset):**  
Zbontar, J., Knoll, F., Sriram, A., et al.
fastMRI: An Open Dataset and Benchmarks for Accelerated MRI.  
arXiv:1811.08839, 2018.

**FLowOak/mri_knee (derivative dataset):**  
FLowOak.
MRI Knee Dataset (Single‑Coil).  
Hugging Face, 2025.

## Notebook 2 — MRI Software Architecture and Deployment (Phase 4)

Notebook 2 transitions the reconstruction workflow from the exploratory setting of Notebook 1 into a modular software system. The work developed in earlier phases is consolidated into an object‑oriented engine that provides a `reconstruct()` function, giving the optimisation pipeline a clear entry point for use within other Python modules or integration into external applications. This establishes the foundation for a structured implementation that can be reused or extended beyond the notebook environment.

Building on this structure, the notebook introduces a FastAPI service that exposes a `/reconstruct` endpoint for remote execution. Structured Pydantic models handle input validation, and the service is packaged into a Docker container to ensure consistent execution across environments. A Pytest script verifies that the reconstruction engine behaves as expected under controlled conditions. Together, these components enable the reconstruction pipeline to run outside the notebook environment and be incorporated into other systems.

## Platform Notes For Deployment
* Local development, Docker, and cloud deployments use port 8000 (standard FastAPI/Uvicorn).
* Hugging Face Spaces require port 7860.

## Live API (FastAPI) Access

Interactive OpenAPI documentation for the MRI reconstruction microservice:

https://jsku-systems-mri-reconstruction-api.hf.space/docs

## Demo

Below is a short demonstration of interacting with the deployed MRI Reconstruction API using the built‑in Swagger UI. 
The video shows submitting a synthetic k-space payload and receiving the reconstructed magnitude image and runtime.

https://github.com/user-attachments/assets/955386bb-584c-437b-bc57-b356d520cf1b

## License

This project is released under the MIT License.
