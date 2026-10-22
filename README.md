# aimation

面向游戏角色动画制作的技能集合。

## H3 八方向动作提示词

[`h3-eight-direction-actions`](skills/h3-eight-direction-actions/SKILL.md) 用于从一张已审定的 4 列 × 2 行八方向 idle 图，编写 MiniMax H3 / Ref2VA 动作提示词。按需支持 STAND、RUN、ATTACK、MAGIC、DIE 和 HIT。

本次更新包含：

- 对最终完整提示词实际计数，处理 `content[0].text too long`，默认上限 7000 字符。
- 区分海螺网页、官方 API 的秒数与本地工作流的帧数。
- 分别描述 RUN 支撑期与回收期，减少背面和背侧面倒跑。
- 用脸部可见范围、头部轮廓和肩膀遮挡约束四个斜向视图。
- 遇到重复的斜向漂移时，采用逐方向生成、关键帧和合成的后续流程。

## 目录

```text
skills/h3-eight-direction-actions/
├── SKILL.md
├── agents/openai.yaml
├── references/action-blocks.md
├── references/run-direction-lock.md
└── scripts/check_prompt.py
```

## 安装与使用

将完整的 `skills/h3-eight-direction-actions` 文件夹复制到本机 Codex 的技能目录（通常为 `~/.codex/skills/`），保留子目录结构。重新打开会话后，可使用：

```text
$h3-eight-direction-actions 为附件中的八方向 idle 图编写 RUN 动作提示词。
```

同时提供参考图、生成入口和需要的动作。实际时长与输出规格以所用入口支持的选项为准。

## 提示词长度检查

需要 Python 3，无第三方依赖。从仓库根目录执行：

```sh
python skills/h3-eight-direction-actions/scripts/check_prompt.py prompt.txt
python skills/h3-eight-direction-actions/scripts/check_prompt.py prompt.txt --json
```

脚本只读取本地 UTF-8 文本并计数，不会提交生成请求。它也会报告使用 CRLF 换行时的字符数。

## 验证状态与局限

已检查技能结构、资源链接和计数脚本的长度边界。此前用户测试显示动作一致性改善，但四个斜向仍可能漂移。新增的固定视图 / 2D 骨架约束尚未经过实际视频生成验证，不能保证角度完全固定。

请分别验收请求提交、步态、八格朝向、道具归属和循环接缝。重复失败时应调整参考或生成流程，避免不断追加提示词造成超长。
