# D&D 2024 SRD-only 新手 DM 一次性冒险包 · 试读版 — 核查说明

## 下载试读（免费，5 页 PDF）

- [中文试读 dnd-one-shot-shidu.pdf](https://github.com/alapha888/dnd-one-shot-shidu/releases/download/trial-v1/dnd-one-shot-shidu.pdf) · [英文试读 dnd-one-shot-shidu-en.pdf](https://github.com/alapha888/dnd-one-shot-shidu/releases/download/trial-v1/dnd-one-shot-shidu-en.pdf)（[全部版本见 Release trial-v1](https://github.com/alapha888/dnd-one-shot-shidu/releases/tag/trial-v1)）
- 试读是验证物，不是成品：正在做 7 天下载量测试（目标 ≥20 次下载才做完整版），不含价格、购买链接或销售承诺。

> 本文件为核查说明：记录试读内容结构、规则出处与 SRD 5.2.1 核对情况。

## 文件

| 文件 | 说明 |
| --- | --- |
| `dnd-one-shot-shidu.pdf` | 5 页试读 PDF（A4，黑白打印友好，字体已嵌入子集） |
| `dnd-one-shot-shidu-en.pdf` | 5-page English version of the same preview (A4, Helvetica, same content, same SRD 5.2.1 attribution on every page) |
| `build_pdf.py` | 生成脚本（Python + reportlab；字体见 `fonts/`） |
| `build_pdf_en.py` | English build script (Python + reportlab, built-in Helvetica; no CJK font needed) |
| `fonts/NotoSansSC-Regular.ttf`、`fonts/NotoSansSC-Bold.ttf` | 由系统 Noto Sans CJK SC（OTF/CFF）经 fontTools cu2qu 转换的 TTF 版，仅供本 PDF 嵌入使用 |
| `README-试读.md` | 试读核查说明（与本文件内容相同） |

## 英文版（English version）

- 英文试读与中文试读内容相同、同为 5 页：Session Zero 清单、首战速查卡（上/下）、原创冒险《萤火溪的断桥》开场与首场遭遇数据卡。
- The English preview has the same 5 pages and the same content as the Chinese preview: Session Zero checklist, first-fight quick cards (1/2), and the opening plus first-encounter stat cards of the original adventure "The Broken Bridge over Firefly Creek". Monster statistics (Goblin Minion p. 290, Wolf p. 364) and the DC table were re-checked against the official SRD 5.2.1 PDF on 2026-11-07; the SRD 5.2.1 CC-BY-4.0 attribution appears on every page of both versions.
- 语言说明：完整版定价 $12.99 的目标市场是英文 D&D 玩家；英文试读用于该市场的 7 天下载量测试，中文试读保留供中文读者使用。

## 试读内容结构（5 页）

| 页 | 内容 | 来源 |
| --- | --- | --- |
| 1 | Session Zero 清单（14 项：团务 4、角色 4、玩法与边界 6）＋开团前 10 分钟流程 | 全部原创文字；角色创建规则出处为 SRD 5.2.1《角色创建》（p. 19 起） |
| 2 | 首战速查卡（上）：D20 检定三步、优势/劣势、常用 DC 表、攻击检定流程、重击、豁免检定、回合结构、先攻 | 规则转述自 SRD 5.2.1《进行游戏》（pp. 5–12）、《战斗》（pp. 13–15）、《伤害与治疗》（p. 16）；DC 表数值（5/10/15/20/25/30）与 SRD p. 6–7 的 Typical Difficulty Classes 表一致 |
| 3 | 首战速查卡（下）：12 个常见状态一行一条、HP 归 0 与死亡豁免、伤害抗性/易伤、DM 临场三句话 | 状态效果转述自 SRD 5.2.1《规则术语表》（自 p. 176 起）；倒地与死亡规则见《伤害与治疗》（pp. 16–17） |
| 4 | 原创冒险《萤火溪的断桥》开场：背景、开场白、NPC 玛拉、场景一（溪边小径）、场景二（断桥伏击） | 全部原创文字；地名（灰岩村、萤火溪）与人物（玛拉、塔姆）均为原创，未使用任何官方设定地名；伏击的突袭处理按 SRD 5.2.1《战斗》先攻规则表述 |
| 5 | 首场遭遇数据卡（哥布林杂兵 ×2、狼 ×1）、人数调整、战利品、DM 提示、试读结束说明 | 怪物数据为 SRD 5.2.1 怪物图鉴原文数值：哥布林杂兵（Goblin Minion）p. 290；狼（Wolf）p. 364；治疗药水为 SRD 5.2.1 魔法物品 |

## SRD 合规核查结论

核查来源（2026-11-07 实测下载与提取）：

- 官方 SRD 页面：https://www.dndbeyond.com/srd
- 官方 SRD 5.2.1 PDF：https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf（364 页，2025-04-29 修订版）
- D&D Beyond Creator FAQ：https://www.dndbeyond.com/creator-faq

核查结论：

1. **许可证**：SRD 5.2.1 由 Wizards of the Coast LLC 以 Creative Commons Attribution 4.0 International（CC-BY-4.0）免费提供；一经以 CC 发布即不可撤销（官方 FAQ 原文要点）。
2. **署名文案（官方 PDF p. 1 Legal Information 原文，已逐字核对）**：
   > This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.
   本试读每页页脚均印有该署名全文。
3. **使用边界**：除上述署名外，不得附加其他对 Wizards 或其母公司/关联方的署名；可声明作品“compatible with fifth edition”或“5E compatible”（本试读第 1 页已作此声明）。只有 SRD 5.2.1 本身属于 CC 开放内容，D&D Beyond Basic Rules 不属于 CC，不可用于创作（官方 FAQ 原文要点）——本试读未使用 Basic Rules 独有内容。
4. **开放内容核对**：所用怪物哥布林杂兵、狼均在 SRD 5.2.1 怪物图鉴内（页码见上表），未使用任何非开放怪物（如眼魔、夺心魔等商标怪物，官方 FAQ 明确列为排除项）。未使用官方设定地名与官方美术。全部冒险文字为原创，未复制任何已出版冒险或第三方指南的段落。
5. **规则数值核对**：DC 表、攻击检定（命中 ≥AC、天生 20 重击、天生 1 失手）、重击（伤害骰掷两遍）、死亡豁免、怪物 AC/HP/攻击加值/伤害骰，均已对照官方 SRD 5.2.1 PDF 原文逐项核对。

## 未核实项（待后续步骤核查，本步不猜）

- itch.io 对中国卖家的收款路径与提现方式（本步未做，只记录为待核查）。
- 完整版在 itch.io / DriveThruRPG 等平台的上架规则与分成细节（未核查）。
- SRD 5.2.1 之后的新版本（如未来发布 5.2.2）是否改动本试读引用的规则数值（本次核查以 2025-04-29 修订的 5.2.1 版为准）。

## 本地验证结果

- `pdfinfo`：页数 5，A4（595 × 842 pt）。
- `pdftotext`：每页文字可选中复制；页脚署名行完整。
- 字体：Noto Sans SC Regular / Bold 已嵌入（子集化），黑白打印友好（无彩色底纹，仅浅灰框线）。
