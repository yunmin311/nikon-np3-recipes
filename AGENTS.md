# Repository Rules

This repository is **NP3-first**. Its name is `nikon-np3-recipes` and must not be renamed. CUBE LUTs are companion assets, not a reason to change the repository name.

## Recipe completion checklist

Every published NP3 recipe must ship with a companion CUBE LUT and a Lightroom preset:

1. Build the `.NP3` recipe and place it in its own folder.
2. Generate a 33×33×33 sRGB `.cube` LUT from the same parameter set.
3. Name it `<NP3_STEM>_sRGB.cube` and place it in the same recipe folder.
4. Generate a Lightroom Classic `.xmp` from the same parameter set, named `<NP3_STEM>_Lightroom.xmp`, in the same folder.
5. Link the CUBE and the XMP from the recipe README and from both root READMEs.
6. Regenerate both companions whenever NP3 parameters change, and again after successful in-camera testing.
7. Update `CHANGELOG.md` and the bilingual READMEs.

The CUBE contains the tone curve, Color Blender, and Color Grading only. It must not claim to contain sharpening, mid-range sharpening, clarity, or HDF glow. These are spatial or detail operations and cannot be represented by a 3D LUT.

Lightroom cannot load `.cube` directly, so the `.xmp` preset maps the same parameters to Tone Curve, HSL (8 bands), and Color Grading. The XMP is a third approximation, not a CUBE equivalent, and Lightroom's Sharpness floor of 0 cannot express the negative in-camera sharpening. Document that limitation in the recipe README.

## Repository rules

- Keep the repository name `nikon-np3-recipes`.
- Keep `README.md` (English) and `README.zh-CN.md` in sync.
- Never publish personal portraits or personal sample photos.
- State clearly whether a recipe is file-validated only or also validated in-camera.
- Do not describe the CUBE as a lossless conversion of the NP3 binary; it is a parameter-derived approximation.

## Release pipeline

Every successful recipe follows the same pipeline before it is pushed. The full process, with gates and evidence requirements, is in [`docs/release-process.md`](docs/release-process.md).

Order:

1. Write the success criteria before shooting.
2. Keep parameters in one source; build NP3, CUBE, and XMP from that same source.
3. Pass file-level validation: 392 bytes, `NCP` marker, parsed fields matching the parameter table, CUBE `LUT_3D_SIZE 33` with `33³` entries, and a well-formed XMP preset.
4. Run the in-camera test against the agreed criteria.
5. Sync the recipe README, both root READMEs, and `CHANGELOG.md`.
6. Run the automated gate, then commit and push.

```powershell
py tools/check_release.py
```

The gate must report `0 error(s)`. It verifies, for every `gr-*` recipe folder:

- exactly one NP3 file, 392 bytes, `NCP` marker;
- a companion `<NP3_STEM>_sRGB.cube` with `LUT_3D_SIZE 33` and `33³` entries;
- a companion `<NP3_STEM>_Lightroom.xmp` that parses as XML and carries `crs:PresetType="Normal"`;
- README links to all three files, and no broken relative links;
- root README links to all three files;
- a `CHANGELOG.md` entry mentioning the NP3 filename;
- no image files inside the recipe folder.

A failed gate blocks the push. Candidates that fail in-camera testing stay local and are never pushed under the published name.
