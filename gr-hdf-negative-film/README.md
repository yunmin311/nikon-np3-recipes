# GR HDF Negative Film

[`GRHDF_NEGFILM.NP3`](GRHDF_NEGFILM.NP3) · 392 字节 NCP / NP3 · Nikon Flexible Color

负片方向：保留肤色和暖光，收敛绿植与蓝色，轻微抬暗部并加少量青绿色阴影。附带与正片版相同的轻度机内柔化。

**状态**：2026-11-06 在 Nikon Z6III 上完成 190 张机内 JPEG 实拍，未发现导入或识别问题；个人样片不公开。完整方法见仓库 [methodology.md](../docs/methodology.md)，色彩分析见 [README](../README.zh-CN.md#色彩分析)。

## 参数摘要

| Picture Control 项 | 值 |
|---|---:|
| Contrast / Highlights / Shadows | +4 / -8 / +1 |
| White Level / Black Level | -5 / -1 |
| Sharpening / Mid-range sharpening | -1.5 / -2.5 |
| Saturation / Clarity | -4 / -3.00 |
| 色彩混合重点 | 橙 +3；黄 -8、绿 -18、蓝 -8 |
| 影调分级重点 | 高光暖中性、阴影少量青绿 |

以上为 Nikon 相对值，不是理光的原始参数。

## CUBE LUT（后期）

[`GRHDF_NEGFILM_sRGB.cube`](GRHDF_NEGFILM_sRGB.cube) · 33×33×33 · sRGB → sRGB

同一套 Negative Film 参数导出的 3D LUT，供后期使用。

- **包含**：色调曲线、Color Blender、Color Grading。
- **不包含**：Sharpening、Mid-range sharpening、Clarity、HDF 光晕。3D LUT 是逐像素色彩变换，无法承载空间柔化。
- **与 NP3 的关系**：参数映射，不是 NP3 的二进制无损转换；CUBE 不模拟机内 JPEG 引擎。
- **使用**：输入 / 输出均为 sRGB；请用于中性素材。已应用 Negative Film NP3 的 JPEG 不需要再次套用。

## Lightroom 预设（后期）

[`GRHDF_NEGFILM_Lightroom.xmp`](GRHDF_NEGFILM_Lightroom.xmp)

同一套 Negative Film 参数映射到 Lightroom 的 Tone Curve、HSL 八色和 Color Grading。

- **导入**：Lightroom Classic → 修改照片 → 预设面板右侧 `+` → **导入预设**。
- **包含**：点曲线、HSL、Color Grading、Saturation、Clarity。
- **不包含**：负锐化（Lightroom 最低为 0）、中间调锐化、HDF 光晕。
- **与 NP3 的关系**：第三种近似，按 Lightroom 的 RAW 管线解释；不是 CUBE 的等价物。

## 导入

1. `.NP3` 复制到存储卡根目录或 `NIKON/CUSTOMPC`。
2. 插卡，进入 **管理 Picture Control → 载入/保存 → 从卡复制到相机**。
3. 导入到 C-1 至 C-9，在 **设定 Picture Control** 中选择。

支持机型：Z6III、Z50II、Z5II、Zf、Z8（以 Nikon 手册为准）。导入后不能在机身编辑或重命名。

## 说明

按理光 GR IV 官方 Negative Film 定义与官方成片做的视觉近似，不是逐参数复制。HDF 光晕不在 NP3 内，需要离线处理或实体 HDF 滤镜。配方文件本身不包含第三方照片。
