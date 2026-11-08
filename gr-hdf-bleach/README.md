# GR HDF Bleach Bypass

[`GRHDF_BLEACH.NP3`](GRHDF_BLEACH.NP3) · 392 bytes NCP / NP3 · Nikon Flexible Color

漂白旁路方向：低饱和、高对比、冷调金属阴影，保留少量红色和绿色作为色彩支点。适合低光、雨天、公交车厢、混合色温等现场光场景。

**状态**：2026-11-08 在 Nikon Z6III 上完成 230 张机内 JPEG 实拍，未发现导入或识别问题；个人样片不公开。完整方法见仓库 [methodology.md](../docs/methodology.md)。

## 参数摘要

| Picture Control 项 | 值 |
|---|---:|
| Contrast / Highlights / Shadows | +6 / -7 / -1 |
| White Level / Black Level | -7 / -4 |
| Sharpening / Mid-range sharpening | -0.5 / -1.0 |
| Saturation / Clarity | -22 / -1.00 |
| 色彩混合重点 | 红 -8、橙 -4、黄 -10、绿 -12、青 -4、蓝 -6 |
| 影调分级重点 | 高光 42°/+3、中间调 30°/+2、阴影 210°/+4 |
| Blending / Balance | 68 / +2 |

以上为 Nikon 相对值，不是理光的原始参数。

## 导入

1. `.NP3` 复制到存储卡根目录或 `NIKON/CUSTOMPC`。
2. 插卡，进入 **管理 Picture Control → 载入/保存 → 从卡复制到相机**。
3. 导入到 C-1 至 C-9，在 **设定 Picture Control** 中选择。

支持机型：Z6III、Z50II、Z5II、Zf、Z8（以 Nikon 手册为准）。导入后不能在机身编辑或重命名。

## 实拍观察

- 230 张机内 JPEG 平均亮度 51.7，深暗部（L ≤ 20）占 25.5%，高光裁剪 0.6%，平均 HSV 饱和度 42.6。
- 暗调、低饱和、冷金属阴影稳定；窗光受控，红把手和绿窗仍能保留少量色彩。
- 低光近景的脸部和深色外套会偏暗；建议拍摄时对脸测光并 +0.3 EV 起步，不要靠全局提亮暗部。
- 这是独立方向，不是 Positive / Negative Film 的变体；它不保留 Negative Film 的暖调和青绿阴影。

## 说明

基于理光 GR IV Bleach Bypass 的官方方向与 2026-11-08 公交车厢实拍做的视觉近似，不是逐参数复制，也不是理光算法本身。HDF 光晕不在 NP3 内，需要离线处理或实体 HDF 滤镜。配方文件本身不包含第三方或个人照片。
