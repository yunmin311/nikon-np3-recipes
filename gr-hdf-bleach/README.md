# GR HDF Bleach Bypass

[`GRHDF_BLEACH.NP3`](GRHDF_BLEACH.NP3) · 392 bytes NCP / NP3 · Nikon Flexible Color

## 定位

低照度现场光下的 Bleach Bypass 方向。以低饱和、高对比、冷金属阴影和收敛高光为核心，适用于公交车厢、雨天、阴天、混合色温等以现场光为主的人像场景。

## 设计依据

- **主参考**：Ricoh GR IV Bleach Bypass 的官方 Image Control 方向。
- **交叉参考**：Fujifilm ETERNA Bleach Bypass 的影调结构，以及经典 motion-picture bleach-bypass 的低饱和 / 高对比关系。
- **参数平台**：Nikon Flexible Color。所有数值均为 Nikon 相对值；Ricoh 未公开内部曲线，因此配方采用可复现的 Nikon 参数映射。
- **现场校准**：以 2026-11-08 的 230 张 Nikon Z6III 机内 JPEG 实拍为校准集，针对暗调公交车厢 / 雨天现场光优化。

方向参考理光 Bleach Bypass；在官方未公开内部算法的前提下，配方以 Nikon Flexible Color 重新建立影调与色彩关系，并交叉参考富士 ETERNA Bleach Bypass 的低饱和 / 高对比结构。最终版本以 230 张 Z6III 现场实拍完成校准。

## 视觉结构

- **影调**：高对比、深黑位、低中间调饱和度；高光收敛，保留窗光层次。
- **色彩**：整体低饱和；红与橙保留少量暖度，绿色收敛为冷橄榄，蓝色保持克制。
- **阴影**：冷金属 210° 方向，形成 Bleach Bypass 的金属感。
- **色彩支点**：红色把手、绿色出口标识、窗外绿植仍可作为少量色彩锚点。

## 参数摘要

| Picture Control 项 | 值 |
|---|---:|
| Contrast / Highlights / Shadows | +6 / -7 / -1 |
| White Level / Black Level | -7 / -4 |
| Sharpening / Mid-range sharpening | -0.5 / -1.0 |
| Saturation / Clarity | -22 / -1.00 |
| Color Blender | 红 -8、橙 -4、黄 -10、绿 -12、青 -4、蓝 -6、紫 -10、品红 -12 |
| Color Grading | 高光 42°/+3、中间调 30°/+2、阴影 210°/+4 |
| Blending / Balance | 68 / +2 |

以上为 Nikon 相对值；理光未公开对应的原始参数。

## CUBE LUT（后期）

[`GRHDF_BLEACH_sRGB.cube`](GRHDF_BLEACH_sRGB.cube) · 33×33×33 · sRGB → sRGB

同一套 Bleach Bypass 参数导出的 3D LUT，供后期使用。适合把中性照片或 sRGB / Rec.709 视频快速套到 Bleach 方向；可在 Photoshop、Lightroom Classic、DaVinci Resolve 等支持 3D LUT 的软件中加载。

- **包含**：色调曲线、Color Blender、Color Grading。
- **不包含**：Sharpening、Mid-range sharpening、Clarity、HDF 光晕。3D LUT 是逐像素色彩变换，无法承载空间柔化。
- **与 NP3 的关系**：参数映射，不是 NP3 的二进制无损转换。NP3 负责机内 Picture Control，CUBE 负责后期色彩变换；两者共享同一套目标参数，但 CUBE 不模拟机内 JPEG 引擎和空间柔化。
- **使用**：输入 / 输出均为 sRGB；请用于中性素材。已应用 Bleach NP3 的 JPEG 不需要再次套用 LUT。对中性图像 / 视频使用时，强度可按 50–100% 调整。
- **精度**：33³ 网格适合常规后期；需要更高精度时可生成 65³ 版本。

## 实拍验证

2026-11-08 在 Nikon Z6III 上完成 230 张机内 JPEG 实拍，场景为暗调公交车厢 / 雨天现场光，未发现导入或识别问题。个人样片不公开。

整组统计：

| 指标 | 数值 |
|---|---:|
| 平均亮度 | 51.7 |
| 深暗部（L ≤ 20） | 25.5% |
| 高光裁剪 | 0.6% |
| 平均 HSV 饱和度 | 42.6 |

现场观察：

- 暗调与冷金属阴影稳定；窗光受控；红把手和绿窗仍保留少量色彩。
- 低光近景的脸部和深色外套容易偏暗；建议对脸测光并 +0.3 EV 起步。
- 这是 Z6III、机内 JPEG、现场光条件下的校准结果；其他机型、视频模式和白平衡组合仍需单独验证。

## 使用建议

- **曝光**：优先保证脸部曝光；高反差场景 +0.3 到 +0.5 EV 起步，后期以局部提亮为主。
- **白平衡**：荧光 / 阴天优先“白色优先”；钨丝 / 暖窗优先“暖色优先”。
- **适用场景**：低照度、现场光、低饱和高对比；需要暖肤色优先时，可改用 Negative Film 方向。
- **后期**：保留红 / 绿支点与冷金属阴影，局部处理脸部和深色外套。

## 导入

1. `.NP3` 复制到存储卡根目录或 `NIKON/CUSTOMPC`。
2. 插卡，进入 **管理 Picture Control → 载入/保存 → 从卡复制到相机**。
3. 导入到 C-1 至 C-9，在 **设定 Picture Control** 中选择。

支持机型：Z6III、Z50II、Z5II、Zf、Z8（以 Nikon 手册为准）。导入后不能在机身编辑或重命名。

## 边界

- NP3 只记录色彩、影调与机内柔化；HDF 光晕、halation、颗粒和暗角不在文件内。
- 机内 JPEG 引擎、白平衡、曝光和镜头会影响最终结果。
- 个人样片不进入仓库；本配方不包含第三方照片。

## 版本

当前发布版本为 **V1**（2026-11-08 实拍验证）。后续微调版本只有在机身验证通过后才会替换。
