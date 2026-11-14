# Travel Companion 跨 Agent 适配指南

**核对日期：2026-11-14**

Travel Companion 采用开放的 Agent Skills 文件结构。目标不是为每个平台维护一套不同的人格或旅行方法，而是让不同 Agent 调用同一份核心 Skill；平台适配只处理安装位置、导入包装和宿主能力差异。

> 覆盖说明：AI 产品更新很快。本页记录已核对的主流平台和官方文档，不声称穷尽所有产品，也不把社区安装器支持等同于厂商官方承诺。未核实的能力明确标注为“待验证”。

## 一、唯一核心：Agent Skills 标准

标准结构：

```text
travel-companion/
└── SKILL.md
```

`SKILL.md` 必须有 YAML frontmatter，至少包含：

```yaml
---
name: travel-companion
description: Helps a traveler's existing AI Agent plan and adapt trips, while respecting the host Agent's identity, the traveler's planning style, recommendation independence and user-controlled memories. Use when someone explores, plans, changes, or reflects on a trip.
---
```

`name` 使用小写连字符，并与 Skill 文件夹名一致。可选的 `references/`、`scripts/`、`assets/` 只有在确实需要时再添加。Travel Companion 当前不依赖脚本、外部 API 或平台专属工具。

规范参考：[Agent Skills Specification](https://agentskills.io/specification)。

## 二、面向普通用户的对话式 Agent

| 平台 | 当前适配方式 | 重要限制 |
|---|---|---|
| **Claude.ai（网页端）** | 将 `travel-companion/` 文件夹打成 ZIP，ZIP 内第一层就是该文件夹；在 Customize → Skills → Create skill → Upload a skill 导入。 | 自定义 Skills 需要支持的付费方案并启用 code execution；具体资格以 Claude 帮助中心为准。 |
| **Gemini App（Spark）** | 可上传单独的 `SKILL.md`，或上传 ZIP（ZIP 主目录中直接包含 `SKILL.md`）。 | 目前是 Gemini Spark 功能；需要个人 Google 账号、18 岁以上、Google AI Pro/Ultra 和开启 Keep Activity；地区与客户端范围有限。 |
| **Kimi** | 在 Kimi 对话中发送 GitHub 仓库链接，让 Kimi 安装开源 Skill；Kimi Work 桌面端还支持上传本地 `.md` 或 `.zip`。 | Kimi 网页端和移动端可使用 Skills；本地文件上传以 Kimi Work 桌面端文档为准。 |
| **豆包 / 豆包工作** | 豆包工作有技能入口；如当前客户端提供“上传技能”，优先尝试单独的 `SKILL.md`。也可用本仓库的纯文本提示词版本，让豆包按对话创建个人技能。 | 豆包开放平台开发者上架是另一条流程：需企业资质、ZIP 技能包、平台检测和审核。官方开发文档不能证明普通豆包手机 App 的每个版本都支持直接导入外部 ZIP；不要把开发者上架流程与个人导入混为一谈。 |
| **ChatGPT** | ChatGPT 桌面端可通过 Settings → Import 导入受支持 Agent 的设置和 Skills；当前官方导入文档列出 Claude Code / Claude Cowork 来源。Codex CLI 和 OpenAI Agents / Responses API 支持 Agent Skills 工作流。 | 桌面端导入不是“把 GitHub ZIP 直接上传到普通聊天”。普通 ChatGPT 对话可使用提示词回退版本。 |
| **其他聊天产品** | 若产品没有明确的原生 Skill 导入入口，使用 `prompts/travel-companion.zh-CN.txt`，或将 `SKILL.md` 内容作为自定义指令/新对话的工作方法。 | 提示词回退不等于原生 Skill：不会自动发现、按需加载或跨对话持久保存；记忆和工具能力由宿主平台决定。 |

### Claude.ai 的 ZIP 结构

```text
travel-companion-claude.zip
└── travel-companion/
    └── SKILL.md
```

### Gemini Spark 的 ZIP 结构

```text
travel-companion-gemini.zip
└── SKILL.md
```

这两个 ZIP 的根目录要求不同，不能假定同一个 ZIP 能直接用于所有平台。运行 `python scripts/package-skill.py` 可从仓库中的唯一核心文件生成两种包和单文件版本。

### Kimi

- 网页 / App：可将 GitHub 仓库 URL 发给 Kimi，要求安装这个开源 Skill。
- Kimi Work 桌面端：可上传本地 `.md` 或 `.zip` 文件。
- Kimi Code CLI：使用下方开发 Agent 的目录方式。

### 豆包

请区分三种场景：

1. **豆包手机 App**：不同版本的技能入口和文件导入能力可能不同。若不接受 ZIP，不要反复上传整个仓库压缩包；尝试单独的 `SKILL.md`，或使用纯文本提示词让 Agent 创建个人技能。手机端外部 Skill 导入目前不列为已验证的通用能力。
2. **豆包工作客户端**：使用其当前版本提供的个人技能入口；本仓库提供单文件 Markdown，避免携带不必要的脚本和二进制资源。
3. **豆包开放平台开发者上架**：官方指南要求企业资质认证，上传 ZIP 技能包，包内需提供名称、简介、图标和版本信息，并经过平台检测、评测与审核。ZIP 上限为 16 MB、最多 1024 个文件、单文件解压后不超过 2 MB、总解压量不超过 16 MB。应用插件 Skill 正文建议低于 5,000 tokens；豆包应用插件环境不应假设存在脚本沙箱，外部服务能力要通过合规连接器或注册工具提供。

Travel Companion 本身不需要外部 API、脚本或联网执行，因此适合先以纯 Markdown 方式接入。

## 三、文件系统型开发 Agent

把仓库中的核心 `SKILL.md` 放入对应目录，目录名统一为 `travel-companion`。下表是常见项目级位置；用户级位置通常将相同结构放在用户主目录下。

| Agent | 项目级 Skill 目录 | 用户级 Skill 目录 |
|---|---|---|
| Claude Code | `.claude/skills/travel-companion/` | `~/.claude/skills/travel-companion/` |
| OpenAI Codex CLI | `.agents/skills/travel-companion/` | `~/.agents/skills/travel-companion/` |
| Cursor | `.cursor/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.cursor/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| GitHub Copilot CLI / VS Code | `.github/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.copilot/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| Gemini CLI | `.gemini/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.gemini/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| Qwen Code | `.qwen/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.qwen/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| Kimi Code CLI | `.kimi-code/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.kimi-code/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| OpenCode | `.opencode/skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.config/opencode/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| Cline | `.cline/skills/travel-companion/` | `~/.cline/skills/travel-companion/` |
| OpenClaw | `skills/travel-companion/` 或 `.agents/skills/travel-companion/` | `~/.openclaw/skills/travel-companion/` 或 `~/.agents/skills/travel-companion/` |
| Google Antigravity | `.agents/skills/travel-companion/` | `~/.gemini/config/skills/travel-companion/` |
| Goose | `.agents/skills/travel-companion/`（旧版也可能读取 `.goose/skills/`） | `~/.agents/skills/travel-companion/` |

适配细节与路径可能随 Agent 版本变化。若产品提供原生 Skill 菜单或官方文档，优先遵循其当前说明。不要为了兼容而在同一工作区复制多个同名版本；优先使用该 Agent 已支持的共享 `.agents/skills/` 路径。

### 其他生态 Agent

Windsurf、Amp、Replit、Zed、Roo、Trae、Continue、Devin、Junie 等产品及其他开发 Agent 的支持情况变化较快。部分可通过通用 Skill 安装器映射到各自目录，但“安装器列出”不等于该厂商对每个版本作出官方兼容承诺。

也可以使用社区维护的 `skills` CLI 将同一仓库安装到它识别的多个本机开发 Agent：

```bash
# 先确认仓库能被识别以及 Skill 名称
npx skills add tuxiaoyue/travel-companion --list

# 安装到安装器支持且本机检测到的所有 Agent（用户级）
npx skills add tuxiaoyue/travel-companion --skill travel-companion --agent '*' --global
```

该安装器需要 Node.js（当前文档要求 Node.js 22.20+）。`--agent '*'` 只代表该安装器当前支持并识别的 Agent，不代表市场上每个 Agent。首次使用前请阅读安装器说明并检查目标目录；可用 `--copy` 避免建立符号链接。

可参考：
- [Vercel Skills CLI — commands and installation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Vercel Skills installer — agent mappings](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [GitHub CLI: gh skill install](https://cli.github.com/manual/gh_skill_install)

若要把 Travel Companion 分发到新 Agent，先检查它是否实现 Agent Skills 标准、确认目录路径，再做实际触发测试。没有官方或可复现证据时标记为待验证，不要宣称已适配。

## 四、ChatGPT / OpenAI 细分说明

- **ChatGPT 桌面端**：Settings → Import；官方导入页当前列出 Claude Code 和 Claude Cowork。导入 Skills 后检查工具权限与连接授权。
- **Codex CLI / IDE**：按 Agent Skills 文件目录安装。
- **OpenAI Agents API**：将 Skill 文件夹放进沙箱，并在 session 配置中注册 capability directories。
- **Responses API**：可使用本地或托管 Skill 包；这是开发者 API 工作流，不等于普通 ChatGPT 对话的文件上传入口。

## 五、适配不等于能力凭空出现

Skill 只提供旅行方法、判断规则和协作流程。它不会自动给宿主 Agent 增加：

- 实时网页搜索、航班/铁路/地图数据；
- 餐厅营业时间、实时订位或酒店库存；
- 预订、付款、取消或其他交易权限；
- GPS、后台持续监控、定时通知；
- 持久化私人记忆、跨设备同步或跨 Agent 共享；
- 图像生成、相册管理或手账导出能力。

这些都取决于宿主 Agent 当前可用的工具、账号权限、用户授权和平台存储能力。没有工具时，Agent 必须说明限制并提供可行的人工核验方式，不能编造“已查询”“已预订”或“已保存”。

## 六、每个平台都必须通过的验收

1. 安装后能看到 `travel-companion`，或能按平台方式明确调用。
2. 用户说“帮我规划旅行”时能触发，不需要背诵固定前缀。
3. Agent 保留自己的名字、人格、语气和与用户的关系。
4. 用户可以按时间、结构、联想发散或混合顺序开始，并能随时切换。
5. 计划、用户报告的预订、已核实预订和真实经历不会混淆。
6. 任何平台工具缺失都能如实说明，不伪造实时数据或操作。
7. 推荐不受广告、佣金、赞助和销售转化影响。
8. 用户可以拒绝回访、拒绝上传素材，不因此失去核心旅行规划能力。
9. 个人素材和记忆只按用户意愿处理；不把用户资料用于精准营销。
10. 卸载 Skill 不应破坏宿主 Agent 原有身份、记忆和工作流。

## 官方文档与参考

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Agent Skills / Claude Code / claude.ai](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude: Use Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [OpenAI: Import from another agent](https://learn.chatgpt.com/docs/import)
- [OpenAI: Skills for Agents API / Responses API](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Codex CLI skill installation](https://developers.openai.com/api/reference/cli)
- [Gemini Apps Skills](https://support.google.com/gemini/answer/17094296?hl=en)
- [Gemini CLI Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md)
- [Kimi Skills](https://www.kimi.com/features/skills)
- [Kimi Code CLI Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills)
- [Doubao Skill integration guide](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)
- [Doubao Skill guidelines](https://open.doubao.com/apps-plugin/docs/core-concepts/skill-guidelines)
- [Cursor Skills](https://prod.cursor.com/docs/skills)
- [GitHub Copilot Skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Qwen Code Skills](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/skills.md)
- [OpenCode Skills](https://opencode.ai/docs/skills)
- [Cline Skills](https://github.com/cline/cline/blob/main/docs/customization/skills.mdx)
- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [Antigravity Skills](https://antigravity.google/docs/skills)
- [Goose Skills](https://goose.vcorp.ai/zh-Hans/docs/guides/context-engineering/using-skills/)
