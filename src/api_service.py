# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import time

# Import reconstruction engine from standalone module
from compressed_sensing_mri import CompressedSensingMRI


# Pydantic request model
class ReconstructionRequest(BaseModel):
    kspace_real: list      # flattened real part of k-space
    kspace_imag: list      # flattened imaginary part of k-space
    mask: list             # flattened sampling mask (0/1)
    shape: tuple           # original 2D shape (H, W)


# Pydantic response model
class ReconstructionResponse(BaseModel):
    image: list            # reconstructed magnitude image (2D list)
    duration_ms: float     # reconstruction time in milliseconds

# Initialise FastAPI application
app = FastAPI()

# /reconstruct endpoint
@app.post("/reconstruct", response_model=ReconstructionResponse)
def reconstruct_endpoint(payload: ReconstructionRequest):

    # Extract shape and validate dimensions
    try:
        H, W = payload.shape
        expected_len = H * W

        if not (
            len(payload.kspace_real) == expected_len and
            len(payload.kspace_imag) == expected_len and
            len(payload.mask) == expected_len
        ):
            raise ValueError("Input arrays do not match the specified shape.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid shape: {str(e)}")

    # Convert lists to numpy arrays and reshape
    try:
        k_real = np.array(payload.kspace_real, dtype=np.float32).reshape(H, W)
        k_imag = np.array(payload.kspace_imag, dtype=np.float32).reshape(H, W)
        kspace = k_real + 1j * k_imag

        mask = np.array(payload.mask, dtype=np.float32).reshape(H, W)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Array conversion failed: {str(e)}")


    # Instantiate reconstruction engine
    engine = CompressedSensingMRI(mask=mask)


    # Perform reconstruction with timing
    try:
        start = time.time()
        recon = engine.reconstruct(kspace)
        duration_ms = (time.time() - start) * 1000

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Reconstruction failed: {str(e)}")

    # Convert output to Python list for JSON response
    recon_list = recon.tolist()

    return ReconstructionResponse(
        image=recon_list,
        duration_ms=duration_ms
    )