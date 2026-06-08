# -*- coding: utf-8 -*-

import numpy as np
from skimage.restoration import denoise_tv_chambolle

class CompressedSensingMRI:
    """
    Object-oriented reconstruction engine for compressed sensing MRI.

    Encapsulates:
    - Forward operator A(x): masked FFT
    - Adjoint operator A*(y): masked inverse FFT
    - FISTA-TV reconstruction loop

    Designed for reuse in API endpoints, testing, and deployment.
    """

    def __init__(self, mask, lambda_tv=5e-5, step_size=1.3, n_iters=150, tv_iters=20):
        """
        Parameters
        ----------
        mask : ndarray
            Binary undersampling mask in k-space.
        lambda_tv : float
            Total variation regularisation weight.
        step_size : float
            Gradient descent step size.
        n_iters : int
            Number of FISTA iterations.
        tv_iters : int
            Number of iterations for the TV proximal operator.
        """
        self.mask = mask.astype(np.float32)
        self.lambda_tv = lambda_tv
        self.step_size = step_size
        self.n_iters = n_iters
        self.tv_iters = tv_iters


    # Forward operator A(x): masked FFT
    def A(self, x):
        """Apply masked Fourier transform."""
        k = np.fft.fftshift(np.fft.fft2(x, norm="ortho"))
        return self.mask * k


    # Adjoint operator A*(y): masked inverse FFT
    def A_adj(self, y):
        """Apply adjoint of masked Fourier transform."""
        k = self.mask * y
        x = np.fft.ifft2(np.fft.ifftshift(k), norm="ortho")
        return x


    # Main reconstruction method (FISTA-TV)
    def reconstruct(self, kspace, return_objective=False):
        """
        Perform FISTA-TV reconstruction on undersampled k-space.

        Parameters
        ----------
        kspace : ndarray
            Undersampled complex k-space data.
        return_objective : bool
            If True, return objective values for analysis.

        Returns
        -------
        recon : ndarray
            Reconstructed magnitude image.
        obj_vals : list (optional)
            Objective values per iteration.
        """

        # Initial estimate
        x = np.zeros_like(self.A_adj(kspace))
        y = x.copy()
        t = 1.0

        obj_vals = []

        for i in range(self.n_iters):

            # Gradient of data fidelity term
            grad = self.A_adj(self.A(y) - kspace)
            x_new = y - self.step_size * grad

            # TV proximal operator (magnitude-only)
            x_new = denoise_tv_chambolle(
                np.abs(x_new),
                weight=self.lambda_tv,
                max_num_iter=self.tv_iters
            )

            # FISTA momentum update
            t_new = (1 + np.sqrt(1 + 4 * t**2)) / 2
            y = x_new + ((t - 1) / t_new) * (x_new - x)

            # Update variables
            x = x_new
            t = t_new

            # Optional objective tracking
            if return_objective:
                fidelity = np.linalg.norm(self.A(x) - kspace)**2
                obj_vals.append(fidelity + self.lambda_tv)

        if return_objective:
            return x, obj_vals
        return x