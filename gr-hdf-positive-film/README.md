# GR HDF Positive Film

[`GRHDF_POSFILM.NP3`](GRHDF_POSFILM.NP3) · 392 字节 NCP / NP3 · Nikon Flexible Color

正片方向：整体色彩鲜明但收住橙色偏色，红橙黄和蓝色作选择性增强，绿植保持自然。附带轻度机内柔化，降低画面微反差，不产生 HDF 式点光源光晕。

**状态**：已导入 Nikon Z6III 使用，2026-11-06 机内 JPEG 直出 10 张；配方结构经 NP3 解析与字节比对。完整方法见仓库 [methodology.md](../docs/methodology.md)，色彩分析见 [README](../README.zh-CN.md#色彩分析)。

## 参数摘要

| Picture Control 项 | 值 |
|---|---:|
| Contrast / Highlights / Shadows | +7 / -8 / 0 |
| White Level / Black Level | -6 / -1 |
| Sharpening / Mid-range sharpening | -1.5 / -2.5 |
| Saturation / Clarity | +24 / -3.00 |
| 色彩混合重点 | 红 +16、橙 +18、黄 +20、蓝 +16；绿 -7 |
| 影调分级重点 | 高光轻暖、阴影微冷 |

以上为 Nikon 相对值，不是理光的原始参数。

## CUBE LUT（后期）

[`GRHDF_POSFILM_sRGB.cube`](GRHDF_POSFILM_sRGB.cube) · 33×33×33 · sRGB → sRGB

同一套 Positive Film 参数导出的 3D LUT，供后期使用。

- **包含**：色调曲线、Color Blender、Color Grading。
- **不包含**：Sharpening、Mid-range sharpening、Clarity、HDF 光晕。3D LUT 是逐像素色彩变换，无法承载空间柔化。
- **与 NP3 的关系**：参数映射，不是 NP3 的二进制无损转换；CUBE 不模拟机内 JPEG 引擎。
- **使用**：输入 / 输出均为 sRGB；请用于中性素材。已应用 Positive Film NP3 的 JPEG 不需要再次套用。

## 导入

1. `.NP3` 复制到存储卡根目录或 `NIKON/CUSTOMPC`。
2. 插卡，进入 **管理 Picture Control → 载入/保存 → 从卡复制到相机**。
3. 导入到 C-1 至 C-9，在 **设定 Picture Control** 中选择。

支持机型：Z6III、Z50II、Z5II、Zf、Z8（以 Nikon 手册为准）。导入后不能在机身编辑或重命名。

## 说明

按理光 GR IV 官方 Positive Film 定义与官方成片做的视觉近似，不是逐参数复制。HDF 光晕不在 NP3 内，需要离线处理或实体 HDF 滤镜。配方文件本身不包含第三方照片。
