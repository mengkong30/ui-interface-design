# ui界面设计

**版本 1.0.2 · Codex Skill · 中文说明 · MIT License**

从真实的小屏界面迭代中提炼的 UI 设计技能，帮助设计方向收敛、成套界面统一、图标与组件制作、数据呈现、圆角屏幕适配和页面关系图整理。

它是一组供 AI 助手读取的 Markdown 工作指引，**不是独立应用，也不自带 Figma 连接器、生成模型或自动执行服务**。安装技能本身不会读取 Figma、上传文件或修改设计；使用时是否调用工具，由用户任务、助手行为、已安装工具和宿主权限共同决定。

## 能做什么

- 将“违和、太空、太生硬”等反馈拆解为比例、信息层级、颜色角色和对齐问题。
- 在实际尺寸下检查图标 keyline、面性轮廓、内外圆角和负空间。
- 使用组件与变体维护时间数字、天气、菜单和操作状态。
- 处理数字与单位、图表图例、天气等宽列、头像与操作区的排版。
- 检查大圆角裁切和底部安全距离，整理可维护的页面关系图。
- 区分静态设计、动画预览和实际可交互原型，避免夸大交付状态。

其中手表案例的456×456、80px圆角、32px图标和钴蓝配色仅为一个项目的经验，不是跨设备强制标准。

## 下载与安装

从 [v1.0.2 Release](https://github.com/mengkong30/ui-interface-design/releases/tag/v1.0.2) 下载 `ui-interface-design-v1.0.2.zip`，并可使用同页的 `SHA256SUMS.txt` 核对文件完整性。校验和不能单独证明发布者身份。

将 ZIP 中的 `ui-interface-design` 文件夹解压至个人技能目录。推荐结构：

```text
<技能目录>/
└── ui-interface-design/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    ├── docs/
    └── ...
```

默认目录通常为 Windows 的 `%USERPROFILE%\.codex\skills` 或 macOS/Linux 的 `~/.codex/skills`。若宿主配置了 `CODEX_HOME`，使用其 `skills` 子目录；实际路径以宿主配置为准。不要解压出双层 `ui-interface-design/ui-interface-design`。

也可克隆指定版本到一个尚不存在的技能目录：

```powershell
# Windows PowerShell；目标已存在时先备份，不要直接覆盖
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
git clone --branch v1.0.2 --depth 1 https://github.com/mengkong30/ui-interface-design.git (Join-Path $skillRoot 'ui-interface-design')
```

```bash
# macOS / Linux；目标必须尚不存在
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
git clone --branch v1.0.2 --depth 1 https://github.com/mengkong30/ui-interface-design.git "$skill_root/ui-interface-design"
```

安装后在技能列表中查找 **ui界面设计**。若当前会话尚未发现新技能，重新开启会话或使用宿主提供的刷新机制；不同宿主的发现行为可能不同。

## 使用示例

```text
使用 $ui-interface-design 复查当前界面，保持现有风格，检查文字层级、
图标比例、同类页面一致性和边缘裁切，修复后展示实际导出效果。
```

```text
使用 $ui-interface-design 设计一套智能手表界面。首页只保留时间、日期、
天气、步数、心率和电量。先明确视觉方向，再制作可编辑组件与状态。
```

```text
使用 $ui-interface-design，把当前所有页面重新整理成带页面缩略图的关系图。
加入应用总菜单，区分并列入口、连续操作、返回手势和系统事件。
```

仅需建议时明确“只检查、不修改”；授权编辑时注明目标文件、页面和修改范围。无需提供密码或令牌。

## 配置与依赖

| 场景 | 所需配置 | 结果 |
|---|---|---|
| 设计分析与规范建议 | 能加载技能的助手；用户提供需求或图像 | 建议、结构与验收清单 |
| 编辑 Figma | 另行配置可用的 Figma 工具及文件访问权限 | 可编辑图层、组件与导出 |
| 本地 Figma 桥接 | 用户自行安装可信桥接插件并连接桌面文件 | 支持范围以实时能力为准 |
| 图片概念或天气背景 | 可用的图片生成工具及其权限/额度 | 概念图片或素材 |
| 可交互原型、工程代码 | 另外提供实现工具并明确任务 | 不由本技能自动附带 |

详细步骤见 [配置方案](docs/CONFIGURATION.md)，操作和验收见 [使用说明](docs/USAGE.md)。技能不需要专属 API Key，不捆绑外部插件，也不要求修改宿主的权限策略。

## 文件与维护

- `SKILL.md`：入口与任务路由。
- `references/visual-system.md`：排版、图标、图表和设备边界验收。
- `references/figma-workflow.md`：可编辑交付、工具限制与导航关系图。
- `references/iteration-lessons.md`：参考整合、App 图标分层、批量对齐、历史版保护与数据页构图。
- `references/watch-case.md`：手表案例，通用任务按需读取。
- `agents/openai.yaml`：中文显示名称与默认提示。
- `scripts/validate.py`：离线、只读的包结构校验。

运行 `python scripts/validate.py` 可校验版本一致性、必要文件、元数据与局部链接。它不验证设计质量、工具连通性或法律合规。

升级前备份自定义修改，核对更新说明；固定版本可用于可重复使用。卸载时移除对应技能目录即可，已有设计文件和第三方插件不会随之删除。

## 许可与免责声明

本仓库原创技能文本及配套代码按 [MIT License](LICENSE) 提供。发布包不包含原项目截图、参考图、设计源文件、字体、账号凭据或第三方插件。

**使用前请阅读 [详细免责声明](DISCLAIMER.md)**。AI 结果和工具操作需要人工复核；本技能不保证美观、准确性、无侵权、无障碍达标、跨版本兼容或生产安全。健康界面案例不构成医疗建议或医疗器械验证。免责声明适用范围受适用法律限制，不能排除法律不允许排除的责任。

反馈请提交可公开的最小复现信息和版本号；不要在 Issues 中上传令牌、客户机密或未获授权的设计资料。
