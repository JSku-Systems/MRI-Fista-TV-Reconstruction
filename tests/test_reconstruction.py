# -*- coding: utf-8 -*-

# Pytest for Compressed Sensing MRI Engine

import numpy as np
from compressed_sensing_mri import CompressedSensingMRI

def test_reconstruction():
    """
    Basic test to ensure the reconstruction engine:
    - accepts valid synthetic k-space input
    - returns an output of the correct shape
    - produces non-zero magnitude values
    """

    # Create a small synthetic test image (8x8)
    H, W = 8, 8
    synthetic_image = np.ones((H, W), dtype=np.float32)

    # Forward FFT to generate synthetic k-space
    kspace = np.fft.fft2(synthetic_image)

    # Undersampling mask (fully sampled for test)
    mask = np.ones((H, W), dtype=np.float32)

    # Instantiate reconstruction engine
    engine = CompressedSensingMRI(mask=mask)


    # Perform reconstruction
    recon = engine.reconstruct(kspace)


    # Assertions: shape, type, non-zero content
    assert recon.shape == (H, W), "Reconstruction returned incorrect shape."
    assert np.isfinite(recon).all(), "Reconstruction contains invalid values."
    assert recon.sum() > 0, "Reconstruction returned all zeros."