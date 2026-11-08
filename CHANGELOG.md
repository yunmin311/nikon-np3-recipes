# Changelog

## 2026-11-08

### Added

- `GRHDF_BLEACH.NP3` — 392-byte GR HDF Bleach Bypass recipe: low saturation, high contrast, cool metallic shadows.
- Bleach Bypass field validation on Nikon Z6III: 230 in-camera JPEGs in a dark bus / rainy available-light setting, no import or recognition issues. Personal samples are not published.
- Root READMEs now list Bleach Bypass as a third, field-calibrated direction.

### Changed

- Recipe badge updated from 2 to 3.
- README validation record adds the 2026-11-08 field set: luma 51.7, deep shadows 25.5%, highlight clipping 0.6%, HSV saturation 42.6.
- Documented Bleach Bypass as an independent field-calibrated direction with its own reference set and Z6III validation; the eight-scene lab analysis remains scoped to the Positive / Negative Film series.

## 2026-11-07

### Added

- Lab 色度分布、色相频率、逐场景饱和度三张分析图。
- 方法论文档 `docs/methodology.md`，补充验证记录与解释边界。
- 英文 `README.md` 与中文 `README.zh-CN.md` 双语版本。
- 仓库 README 的完整结构：配方索引、快速导入、色彩分析、技术规格、验证记录、Roadmap 与许可说明。

### Changed

- `scene_metrics.csv` 移入 `docs/data/`。
- 仓库 About 描述与 topics 更新为 NP3 配方库定位。
- 明确校准原则：保持 Positive Film 高饱和、Negative Film 低饱和，不按单一场景或天气做适配。
- 移除照片前后对比图，只保留 Lab 色度、色相频率和逐场景饱和度分析图。
- 撤回 V2 / V3 负片增饱和实验，正式配方保持原样。

## 2026-10-10

### Added

- GR HDF Positive Film / Negative Film 两份 392 字节 NP3 配方。
- 8 场景高分辨率模拟预览、HDF 高光对照与逐场景 HSV 指标。
- 基于已知可导入 NX Studio 导出模板的构建流程，以及 NP3 解析与字节比对验证。
