# Repository Rules

This repository is **NP3-first**. Its name is `nikon-np3-recipes` and must not be renamed. CUBE LUTs are companion assets, not a reason to change the repository name.

## Recipe completion checklist

Every published NP3 recipe must ship with a companion CUBE LUT:

1. Build the `.NP3` recipe and place it in its own folder.
2. Generate a 33×33×33 sRGB `.cube` LUT from the same parameter set.
3. Name it `<NP3_STEM>_sRGB.cube` and place it in the same recipe folder.
4. Link the CUBE from the recipe README and from the root README.
5. Regenerate the CUBE whenever NP3 parameters change, and again after successful in-camera testing.
6. Update `CHANGELOG.md` and the bilingual READMEs.

The CUBE contains the tone curve, Color Blender, and Color Grading only. It must not claim to contain sharpening, mid-range sharpening, clarity, or HDF glow. These are spatial or detail operations and cannot be represented by a 3D LUT.

## Repository rules

- Keep the repository name `nikon-np3-recipes`.
- Keep `README.md` (English) and `README.zh-CN.md` in sync.
- Never publish personal portraits or personal sample photos.
- State clearly whether a recipe is file-validated only or also validated in-camera.
- Do not describe the CUBE as a lossless conversion of the NP3 binary; it is a parameter-derived approximation.
