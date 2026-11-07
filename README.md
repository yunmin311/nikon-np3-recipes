# Nikon NP3 Recipes

个人维护的 Nikon 自定义 Picture Control 配方库。每个配方一个独立文件夹，内含可直接导入相机的 `.NP3` 文件、参数说明和效果预览。

## 配方

| 文件夹 | 配方 | 色彩方向 | 文件 |
|---|---|---|---|
| [gr-hdf-positive-film](gr-hdf-positive-film/) | GR HDF Positive Film | 选择性鲜明的正片色彩，控制整体偏橙 | [GRHDF_POSFILM.NP3](gr-hdf-positive-film/GRHDF_POSFILM.NP3) |
| [gr-hdf-negative-film](gr-hdf-negative-film/) | GR HDF Negative Film | 自然的负片色彩，收敛绿色与蓝色，青绿阴影 | [GRHDF_NEGFILM.NP3](gr-hdf-negative-film/GRHDF_NEGFILM.NP3) |

两份配方以理光 GR IV / GR IV HDF 的官方资料与成片为视觉参考，并加入轻度机内柔化：锐化 **−1.5**、中间调锐化 **−2.5**、清晰度 **−3.0**。

> HDF 光晕是镜头/滤镜产生的空间扩散，不能写入 NP3。本库配方只负责机内 JPEG 的色彩与影调；光晕需离线处理，或使用 HDF 机型与实体 HDF 滤镜。

## 导入到相机

1. 将 `.NP3` 文件复制到存储卡根目录，或放在 `NIKON/CUSTOMPC` 文件夹。
2. 把卡插入相机的主卡槽。
3. 打开 **照片/视频拍摄菜单 → 管理 Picture Control → 载入/保存 → 从卡复制到相机**。
4. 导入到 C-1 至 C-9 后，在 **设定 Picture Control** 里选择对应配置。

Nikon 手册已明确记载支持 Flexible Color 导入的机型：**Z6III、Z50II、Z5II、Zf、Z8**。其他机型请先查对应手册是否支持 NP3 / Flexible Color。导入后不能在机身上编辑或重命名，这是 Nikon 的固有限制。

## 预览与数据

每个配方文件夹的 `previews/` 包含场景总览、纯色彩对照和 HDF 高光对照；[scene_metrics.csv](scene_metrics.csv) 是 8 个场景等权平均后的 HSV 饱和度与亮度统计。预览图是色彩方向模拟，不是 NX Studio 或相机实拍输出。

## 准确性边界

理光没有公开 Positive Film / Negative Film 的内部曲线和逐项参数，因此这些配方是按官方定义与官方成片进行的视觉近似，不能称为逐参数复制，也不是理光算法本身。不同相机的 JPEG 引擎、白平衡与曝光会造成差异。

## 许可

配方文件可自由下载、使用和修改。预览图包含第三方照片的改编版本，来源、许可和改动说明见 [THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt)；再分发处理图时请保留署名、来源和许可信息。
