# Translation glossary — chaojifeng-video-design (zh → en)

Use these renderings consistently across every file. The goal is an English text that a video
engineer can read and adapt, not a literal gloss.

## Project / people

| Chinese | English |
|---|---|
| 超级峰 | Chaojifeng (the author's handle; keep as proper noun, gloss once as "Super Peak") |
| 视频设计方法论 | video design methodology |
| 风格包 / 包 | style pack / pack |
| 风格画廊 | style gallery |
| 目录工具 | catalog tooling |
| 已确认经验 | confirmed learnings |
| 来源与许可 | sources and licenses |

## The core vocabulary (these carry the method — translate, keep the field name in backticks)

| Chinese | English |
|---|---|
| 主线 / 贯穿线 | through-line / spine |
| 观众变化 (viewer_change) | viewer change — what the audience becomes by the end |
| 导演意图 | directorial intent |
| 分镜 | storyboard / shot list |
| 镜头 | shot |
| 镜号 | shot number |
| 场景 (scene) | scene |
| 节拍 / 故事节拍 | beat / story beat |
| 段落 | section / passage (music: section) |
| 元素使命 | element mission — what an element is responsible for |
| 揭示顺序 (reveal_order) | reveal order |
| 稳定停留 / 阅读窗 | stable dwell / reading window |
| 接力 (handoff) | handoff (how one shot hands off to the next) |
| 焦点 / 焦点实体 | focus / focal entity |
| 景别 | shot size (wide / medium / close) |
| 视角 | camera angle / point of view |
| 运镜 / 相机运动 | camera move |
| 推近 / 拉远 / 横移 / 跟随 | push in / pull back / truck (lateral) / follow |
| 转场 | transition |
| 首帧 / 最密帧 | first frame / densest frame |
| 关系落定 | relationship lands / settles |
| 声画 / 声画节奏 | sound-and-image / sound-image rhythm |
| 声音职责 | sound's job / sound responsibility |
| 主声 / 动机 | lead sound / motif |
| 旁白 / 口播 | voiceover / to-camera narration |
| 台词 / 歌词 | dialogue / lyrics |
| 配乐 | score |
| 音轨 | audio track |
| 音效 | sound effect (SFX) |
| 声音事件表 | audio event map |
| 听审 | listening pass / audition |
| 能量起落 / 包络 | energy rise and fall / envelope |
| 拍点 / 重拍 | downbeat / beat hit |
| 素材 | asset / footage |
| 素材调度 (asset_routing) | asset routing |
| 动效 / 局部动效 | motion / motion effect |
| 功能动效 | feature motion |
| 组合局部布局和动作 (compose) | compose — combine local layouts and motion |
| 场景配方 (recipe) | recipe |
| 自由设计 (free) | free design |
| 画幅 | aspect ratio |
| 时长 | duration |
| 材质 | material / texture |
| 色彩逻辑 | colour logic |
| 调色板 | palette |
| 字体 | type / font |
| 母题 | motif |
| 意象 | imagery |
| 三幕 | three-act |
| 变奏 | variation |
| 收束 / 落款 | ending / sign-off |
| 品牌片 | brand film |
| 知识讲解 | knowledge explainer |
| 资讯 | news brief |
| 产品演示 | product demo |
| 音乐视觉 | music visual |
| 故事 / 故事片 | story / story video |
| 图片成片 | image-driven film |
| 案例 / 参考片 | case / reference film |
| 样片 | sample clip |
| 源 / 来源 (source) | source |
| 上游 | upstream |
| 事实 / 事实边界 | fact / factual boundary |
| 主张 | claim |
| 证据 | evidence |
| 许可 / 授权 | license / permission |
| 使用权 | usage rights |
| 归属 | attribution / ownership |
| 交付 / 交付验收 | delivery / delivery acceptance |
| 验收 | acceptance check |
| 审片 | review (watching the cut) |
| 返修 / 修改 | rework / revision |
| 局部修改 | local revision |
| 计划 (plan) | plan |
| 计划合同 (plan-contract) | plan contract |
| 合同 (contract) | contract |
| 可编辑计划 | editable plan |
| 排程 / 绝对秒 | schedule / absolute seconds |
| 稳定 ID | stable ID |
| 运行记录 | run log |
| 执行记录 | execution record |
| 能力探测 | capability probe |
| 制作 | production |
| 实现 | implementation |
| 渲染器 | renderer |
| 导出 | export |
| 实测 / 测量 | measured / measurement |
| 试片 | test cut |
| 粗剪 | rough cut |
| 草图 | sketch / draft |
| 直接成片 (direct) | direct — one continuous run to the finished film |
| staged | staged — wait at agreed checkpoints |
| 门禁 | gate |
| 返修 | rework |

## Style cards (styles/*/STYLE.md)

Keep `id`, `name`, `aliases`, `category`, and every Chinese style name byte-identical — scripts
and tests resolve packs by those strings (`中国水墨`, `超级峰原有风格`, `基础风格`). Translate only
the prose paragraphs and the column headers where they are descriptive.

## Hard rules (do not translate, do not touch)

1. Anything inside ``` fenced code blocks, and anything inside `inline code`.
2. Commands, flags, script names (`catalog.py`, `stylepacks.py`, `validate_plan.py`,
   `check_delivery.py`, `film_probe.py`, `audio_event_audit.py`, `knowledge_pack.py` …).
3. File paths and link targets (`[text](references/x.md)` → translate only `text`).
4. JSON keys and values, field names: `viewer_change`, `scene.intent`, `reveal_order`,
   `camera.purpose`, `handoff`, `acceptance`, `continuity_key`, `director.entities`,
   `element.id`, `film_probe`, `recipe`, `compose`, `free`, style ids.
5. YAML frontmatter keys and their values (`name:`, `description:` — the description may be
   translated, but `name` stays exactly as it is).
6. Chinese style names, aliases, category strings, test fixtures, and the Chinese word lists in
   `scripts/controlled_lint.py` — that linter lints Chinese copy and stays Chinese.
7. Numbers, units, timings, table column counts, heading levels, list nesting.

## Voice

Write like an experienced director explaining their own method to a colleague: plain, specific,
imperative where the original is imperative. Do not add hype, do not add content that is not in
the source, do not soften a hard rule. Where the Chinese is terse to the point of being cryptic,
expand just enough to be unambiguous and keep the original term in parentheses on first use.
