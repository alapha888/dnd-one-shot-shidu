# -*- coding: utf-8 -*-
"""Build the 5-page trial-read PDF for the D&D 2024 SRD-only beginner DM one-shot pack.
All prose is original. Rules are paraphrased from SRD 5.2.1 (CC-BY-4.0) with attribution.
Monster numbers are SRD 5.2.1 stat-block facts (Goblin Minion p.290, Wolf p.364).
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, HRFlowable)

OUT_DIR = os.path.expanduser("~/workspace/independent/dnd-one-shot")
OUT = os.path.join(OUT_DIR, "dnd-one-shot-shidu.pdf")

REG = os.path.join(OUT_DIR, "fonts", "NotoSansSC-Regular.ttf")
BOLD = os.path.join(OUT_DIR, "fonts", "NotoSansSC-Bold.ttf")
pdfmetrics.registerFont(TTFont("NotoSC", REG))
pdfmetrics.registerFont(TTFont("NotoSC-Bold", BOLD))

INK = HexColor("#111111")
GREY = HexColor("#555555")
LIGHT = HexColor("#F2F2F2")
RULE = HexColor("#999999")

ATTRIBUTION = (
    "This work includes material from the System Reference Document 5.2.1 "
    "(\u201cSRD 5.2.1\u201d) by Wizards of the Coast LLC, available at "
    "https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative "
    "Commons Attribution 4.0 International License, available at "
    "https://creativecommons.org/licenses/by/4.0/legalcode."
)

S = {
    "title": ParagraphStyle("title", fontName="NotoSC-Bold", fontSize=19, leading=24,
                            textColor=INK, alignment=TA_LEFT, spaceAfter=4),
    "subtitle": ParagraphStyle("subtitle", fontName="NotoSC", fontSize=10.5, leading=15,
                               textColor=GREY, spaceAfter=8),
    "h1": ParagraphStyle("h1", fontName="NotoSC-Bold", fontSize=13.5, leading=18,
                         textColor=INK, spaceBefore=10, spaceAfter=5),
    "h2": ParagraphStyle("h2", fontName="NotoSC-Bold", fontSize=11.5, leading=16,
                         textColor=INK, spaceBefore=8, spaceAfter=3),
    "body": ParagraphStyle("body", fontName="NotoSC", fontSize=10.5, leading=15.5,
                           textColor=INK, spaceAfter=4),
    "small": ParagraphStyle("small", fontName="NotoSC", fontSize=9.5, leading=14,
                            textColor=GREY, spaceAfter=3),
    "item": ParagraphStyle("item", fontName="NotoSC", fontSize=10.5, leading=15.5,
                           textColor=INK, leftIndent=16, firstLineIndent=0,
                           bulletIndent=6, spaceAfter=2),
    "cell": ParagraphStyle("cell", fontName="NotoSC", fontSize=10, leading=14.5,
                           textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName="NotoSC-Bold", fontSize=10, leading=14.5,
                            textColor=INK),
    "cellhead": ParagraphStyle("cellhead", fontName="NotoSC-Bold", fontSize=10, leading=14,
                               textColor=INK),
    "box": ParagraphStyle("box", fontName="NotoSC", fontSize=10.5, leading=15.5,
                          textColor=INK, spaceAfter=2),
    "readaloud": ParagraphStyle("readaloud", fontName="NotoSC", fontSize=10.5, leading=16,
                                textColor=INK, leftIndent=10, rightIndent=10, spaceAfter=4),
}

def P(text, style="body"):
    return Paragraph(text, S[style])

def items(texts):
    return [Paragraph(t, S["item"], bulletText="[ ]") for t in texts]

def box(title, flowables):
    inner = [Paragraph(f"<b>{title}</b>", S["box"])] + flowables
    t = Table([[inner]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t

def data_table(header, rows, widths):
    data = [[Paragraph(h, S["cellhead"]) for h in header]]
    for r in rows:
        data.append([Paragraph(c, S["cell"]) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, INK),
        ("LINEBELOW", (0, 1), (-1, -2), 0.4, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t

# ---------------------------------------------------------------- page 1
def page1():
    return [
        P("新手 DM 一次性冒险包 · 试读版", "title"),
        P("5E 兼容（5E compatible） · 仅使用 SRD 5.2.1 开放内容 · 写给第一次带团的地下城主", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("这份试读共 5 页：第 1 页是开团前的 Session Zero 清单；第 2–3 页是新手 DM 临场最常用的判定速查卡；"
          "第 4–5 页是一场原创 one-shot 冒险的开场与首场遭遇。全部规则内容转述自 SRD 5.2.1，"
          "怪物数据取自 SRD 5.2.1 怪物图鉴；冒险剧情、地名与人物均为原创。", "body"),
        P("第 1 页 · Session Zero 清单", "h1"),
        P("开团之前，和你的玩家坐下来，把下面这 14 件事逐项定下来。定好的写进群公告，以后有分歧就翻它——"
          "新手团的大多数矛盾，都不是规则问题，而是开团前没说清楚。", "body"),
        P("一、团务", "h2"),
        *items([
            "<b>时间与频率：</b>固定在每周（或隔周）某晚，每次约 3 小时。迟到、请假提前在群里说一声。",
            "<b>地点与工具：</b>面团还是网团；骰子用实体骰还是骰子 App；地图用白板、纸笔还是线上棋盘。",
            "<b>人数：</b>3–5 名玩家最适合新手 DM。本冒险按 4 名 1 级角色设计，人多人少见第 5 页调整办法。",
            "<b>缺席规则：</b>缺席玩家的角色由 DM 临时托管，只跟队、不抢戏、不吃剧情杀；缺席不扣奖励。",
        ]),
        P("二、角色", "h2"),
        *items([
            "<b>角色创建：</b>1 级起步。属性用标准阵列（15、14、13、12、10、8）或 4d6 取最高三颗；"
            "种族与职业只选 SRD 5.2.1 开放的选项（SRD 5.2.1《角色创建》，p. 19 起）。",
            "<b>背景与关系：</b>每人用一句话写背景，并与至少一名队友定一段关系（旧友、债主、同乡……）。",
            "<b>底线：</b>不恶意 PVP，不抢队友战利品，不拿队友角色开玩笑。",
            "<b>升级节奏：</b>跑完本冒险升至 2 级，用里程碑式升级，不逐只怪物算经验。",
        ]),
        P("三、玩法与边界", "h2"),
        *items([
            "<b>风格比例：</b>战斗、探索、扮演各占多少，先说好，DM 才知道该准备什么。",
            "<b>内容边界：</b>恐怖、血腥、背叛情节的上限。桌上放一张 X 卡：任何人不舒服，点一下卡就好，"
            "不用解释，剧情立刻绕开。",
            "<b>规则裁定：</b>现场以 DM 的裁定为准；拿不准的记下来，团后查 SRD，不中途翻书十分钟。",
            "<b>骰子公开：</b>DM 的骰子公开掷，玩家自己掷自己的；重掷只有 DM 喊停时才算。",
            "<b>角色死亡：</b>新手团先谈好——角色死了是换新角色，还是想办法复活；两种都可以，先说好就不伤感情。",
            "<b>团后反馈：</b>每次团后留 5 分钟，每人一句喜欢的、一句想改进的。",
        ]),
        Spacer(1, 4),
        box("开团前 10 分钟", [
            P("① 复述上次剧情（第一次团：直接读第 4 页开场白）　② 确认今晚的目标　"
              "③ 检查角色卡、骰子、零食　④ 把 X 卡放在桌子中央。", "box"),
        ]),
    ]

# ---------------------------------------------------------------- page 2
def page2():
    return [
        P("第 2 页 · 首战速查卡（上）：D20 检定与战斗", "title"),
        P("规则来源：SRD 5.2.1《进行游戏》（p. 5 起）、《战斗》（p. 13 起）、《伤害与治疗》（p. 16 起）。"
          "本页只写新手 DM 第一场战斗真正会用到的部分。", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("D20 检定，三步", "h1"),
        P("<b>1. 掷一颗 d20。　2. 加上调整值</b>（相关属性调整值；如果熟练，再加熟练加值，1 级为 +2）。"
          "<b>3. 比大小：</b>属性检定和豁免检定与难度等级（DC）比；攻击检定与目标的护甲等级（AC）比。等于目标数就算成功。", "body"),
        P("优势与劣势", "h2"),
        P("有优势时掷两颗 d20 取高，有劣势时掷两颗取低。优势与劣势同时存在时互相抵消，只掷一颗。"
          "多个优势不叠加，只取一次最高。", "body"),
        P("常用难度等级（DC）", "h2"),
        data_table(["难度", "DC", "举例"],
                   [["非常简单", "5", "推开一扇没锁的门"],
                    ["简单", "10", "在安静的图书馆里找一本书"],
                    ["中等", "15", "攀爬一段粗糙的石墙"],
                    ["困难", "20", "在暴雨中听清远处的脚步声"],
                    ["非常困难", "25", "徒手撬开生锈的铁箱"],
                    ["几乎不可能", "30", "仅凭气味追踪三天前的足迹"]],
                   [28 * mm, 16 * mm, 126 * mm]),
        P("拿不准定多少 DC 时，先定 10 或 15——新手团宁可让玩家多成功几次。", "small"),
        P("攻击检定流程", "h1"),
        *items([
            "<b>选目标：</b>在武器射程或触及内，且攻击者能看见目标。",
            "<b>掷骰：</b>d20 ＋ 攻击加值（属性调整值 ＋ 熟练加值，如适用）。",
            "<b>比 AC：</b>总和 ≥ 目标 AC 即命中。掷出 20（天生 20）必定命中且为重击；掷出 1（天生 1）必定失手。",
            "<b>掷伤害：</b>武器伤害骰 ＋ 同一属性调整值；法术按法术说明掷骰。",
            "<b>扣血：</b>目标生命值（HP）减去伤害。HP 归 0 时倒地，见第 3 页。",
        ]),
        P("重击：伤害骰掷两遍再相加，属性调整值只加一次。", "body"),
        P("豁免检定", "h2"),
        P("DM 说出属性与 DC，例如“体质豁免，DC 12”。玩家掷 d20 ＋ 该属性的豁免加值，≥ DC 成功，"
          "失败则承受法术或效果写明的后果。", "body"),
        P("一回合能做什么", "h2"),
        P("每回合：<b>1 个移动</b>（最多等于速度，可拆分在动作前后）＋ <b>1 个动作</b>（攻击、施法、疾走、撤离、躲藏等）＋ "
          "<b>1 个附赠动作</b>（只有当职业特性或法术给时才有）＋ <b>1 个反应</b>（在别人回合触发，如借机攻击）。", "body"),
        P("先攻：开战时所有人掷 d20 ＋ 敏捷调整值，按从高到低排序；怪物的先攻由 DM 一起掷。"
          "先攻相同由 DM 决定先后。", "body"),
    ]

# ---------------------------------------------------------------- page 3
def page3():
    return [
        P("第 3 页 · 首战速查卡（下）：状态与倒地", "title"),
        P("规则来源：SRD 5.2.1《规则术语表》（自 p. 176 起）中的状态条目；"
          "倒地与死亡规则见《伤害与治疗》（p. 16–17）。同一状态不与自身叠加。", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("常见状态，一行一个", "h1"),
        data_table(["状态", "效果（简述）"],
                   [["倒地 Prone", "只能爬行移动；起身花费一半移动力；自身攻击检定劣势；5 尺内打它优势，5 尺外打它劣势。"],
                    ["目盲 Blinded", "看不见东西；自身攻击劣势；打它的攻击优势；与视觉相关的检定自动失败。"],
                    ["耳聋 Deafened", "听不见；与听觉相关的检定自动失败。"],
                    ["魅惑 Charmed", "不能攻击魅惑者，也不能以有害能力指定它；魅惑者与它社交互动的检定优势。"],
                    ["恐慌 Frightened", "能看见恐惧来源时，属性检定与攻击检定劣势；不能主动移向恐惧来源。"],
                    ["束缚 Restrained", "速度为 0；打它的攻击优势；自身攻击劣势；敏捷豁免劣势。"],
                    ["失能 Incapacitated", "不能执行动作与反应。"],
                    ["隐形 Invisible", "不被看见；打它的攻击劣势；自身攻击优势。"],
                    ["麻痹 Paralyzed", "失能，不能移动与说话；力量与敏捷豁免自动失败；5 尺内打它优势，命中即重击。"],
                    ["震慑 Stunned", "失能，不能移动，说话断断续续；力量与敏捷豁免自动失败；打它的攻击优势。"],
                    ["昏迷 Unconscious", "失能，不能移动与说话，丢下手中物品并倒地；力量与敏捷豁免自动失败；5 尺内打它优势，命中即重击。"],
                    ["擒抱 Grappled", "速度为 0；擒抱者失能或目标脱离触及则结束。"]],
                   [30 * mm, 140 * mm]),
        P("HP 归 0 与死亡豁免", "h1"),
        P("HP 归 0 的角色倒地昏迷。队友可以用一个动作做一次 DC 10 的医疗检定来稳定伤势，或用治疗法术、治疗药水恢复 HP。"
          "昏迷角色每回合掷一次死亡豁免（d20，无加值）：≥ 10 算一次成功，＜ 10 算一次失败；掷出 20 恢复 1 HP；"
          "掷出 1 算两次失败。三次成功则稳定（保持 0 HP 但不再掷豁免），三次失败则死亡。"
          "昏迷中受到伤害算一次失败，重击造成的伤害算两次失败。", "body"),
        P("伤害、抗性与易伤", "h2"),
        P("伤害有类型（挥砍、穿刺、钝击、火焰等）。抗性：该类型伤害减半（向下取整）；易伤：翻倍；免疫：不受伤害。", "body"),
        Spacer(1, 2),
        box("DM 临场三句话（规则拿不准时）", [
            P("① “先这样判，继续玩。”——现场裁定优先，别让查书打断游戏。<br/>"
              "② 把问题记下来，团后查 SRD。<br/>"
              "③ 下次开团时，用一分钟告诉大家正确的判法。", "box"),
        ]),
        P("新手 DM 最容易卡住的地方不是规则本身，而是怕判错。判错一次没关系，下一团改过来就行——"
          "玩家记住的是今晚的故事，不是你某次 DC 定高了 5 点。", "body"),
    ]

# ---------------------------------------------------------------- page 4
def page4():
    return [
        P("第 4 页 · 原创冒险《萤火溪的断桥》：开场", "title"),
        P("原创剧情与地名，未使用任何官方设定地名与官方美术。怪物均出自 SRD 5.2.1。"
          "适合 4 名 1 级角色，预计 2–3 小时跑完开场与首场遭遇。", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("背景（读给 DM，不读给玩家）", "h1"),
        P("灰岩村是个只有三十户人家的小村子，靠萤火溪边的磨坊和每周一趟的商队过日子。"
          "三天前，村里的信使塔姆沿溪边小径去邻村送信，至今未归。"
          "村长夫人玛拉派了两个村民去找，只找回一支断箭和一只沾血的布鞋。"
          "她怀疑是溪边灌木里的哥布林干的——最近常有人在黄昏后听见灌木里有动静。"
          "玛拉在村口贴了告示：找回塔姆，或带回他的消息，酬劳 20 金币。", "body"),
        P("开场白（读给玩家）", "h1"),
        P("“黄昏的雾贴着萤火溪爬上来，灰岩村的灯火一盏一盏亮起来。村口的告示板上钉着一张新告示，"
          "字迹潦草，边角被风掀起来又落下。告示下面站着一位头发花白的妇人——村长夫人玛拉——"
          "她正盯着你们，那眼神像在数你们兜里的干粮够走几里路。”", "readaloud"),
        P("玛拉会告诉玩家：塔姆三天前沿溪边小径去邻村送信，至今未归；找回他或带回他的消息，酬劳 20 金币；"
          "村民只找回一支断箭和一只沾血的布鞋。玩家可以向她打听（扮演或检定均可）：", "body"),
        *items([
            "<b>问哥布林（DC 10 历史或调查）：</b>玛拉说，灌木里的哥布林只有三五只，胆子小，爱抢落单的行人。",
            "<b>问小径（DC 10 求生）：</b>她指着溪边小径说，路上有车辙，也有不属于村子的脚印。",
            "<b>问报酬：</b>20 金币全队平分，先付 5 金币作定金，回来再付 15 金币。",
        ]),
        P("场景一：溪边小径", "h1"),
        P("沿小径走约半小时，溪水声越来越响。让玩家做一次 DC 10 的感知（察觉）或求生检定："
          "成功则发现草丛里有一支断箭、一只沾血的布鞋，和通向灌木丛的拖拽痕迹；失败则只看到断箭，"
          "需要再花十分钟仔细搜查才能发现拖拽痕迹。顺着痕迹走，玩家来到一座断桥——桥面塌了一半，"
          "桥下是齐膝深的溪水，对岸的灌木丛里有什么东西在动。", "body"),
        P("场景二：断桥伏击（首场遭遇）", "h1"),
        P("两只哥布林杂兵和一只狼藏在对岸灌木里，等玩家走到桥中央再动手。开战前，哥布林做一次隐匿检定，"
          "与每名玩家的被动察觉比较：未察觉到敌人的角色在战斗的第一回合不能移动、不能执行动作，"
          "也不能执行反应（直到其第一回合结束）。", "body"),
        P("哥布林的战术：杂兵先用匕首近战，血量减半就逃跑；狼用群体战术，专挑落单或倒地的目标。"
          "如果玩家大声谈判，哥布林首领不在场——杂兵胆小，DC 12 的威吓或游说检定可以让它们丢下塔姆的布鞋逃走，"
          "但狼不会听谈判。战斗数据见第 5 页。", "body"),
        P("战后线索：灌木丛后的破布口袋里有塔姆的信袋（信完好无损），还有一张潦草的地图，"
          "指向溪边的旧磨坊地窖——试读到此为止，磨坊地窖的完整内容在完整版中。", "body"),
    ]

# ---------------------------------------------------------------- page 5
def page5():
    return [
        P("第 5 页 · 首场遭遇数据卡与 DM 提示", "title"),
        P("怪物数据转述自 SRD 5.2.1：哥布林杂兵（Goblin Minion）p. 290；狼（Wolf）p. 364。"
          "遭遇总经验 100（25 ＋ 25 ＋ 50），对 4 名 1 级角色属于简单至中等难度。", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("哥布林杂兵（Goblin Minion）× 2", "h1"),
        data_table(["属性", "数值"],
                   [["体型 / 阵营", "小型精类（哥布林），混乱中立"],
                    ["护甲等级 / 生命值 / 速度", "AC 12；HP 7（2d6）；速度 30 尺；先攻 ＋2"],
                    ["技能 / 感官", "隐匿 ＋6；黑暗视觉 60 尺；被动察觉 9"],
                    ["语言 / 挑战等级", "通用语、哥布林语；CR 1/8（25 XP）"],
                    ["匕首（近战 / 远程）", "攻击 ＋4，触及 5 尺或射程 20/60 尺；命中：4（1d4＋2）穿刺伤害"],
                    ["灵巧逃脱（附赠动作）", "执行撤离或躲藏动作"]],
                   [42 * mm, 128 * mm]),
        P("狼（Wolf）× 1", "h1"),
        data_table(["属性", "数值"],
                   [["体型 / 阵营", "中型野兽，无阵营"],
                    ["护甲等级 / 生命值 / 速度", "AC 12；HP 11（2d8＋2）；速度 40 尺；先攻 ＋2"],
                    ["技能 / 感官", "察觉 ＋5，隐匿 ＋4；黑暗视觉 60 尺；被动察觉 15"],
                    ["挑战等级", "CR 1/4（50 XP）"],
                    ["啃咬（近战）", "攻击 ＋4，触及 5 尺；命中：5（1d6＋2）穿刺伤害；中型或更小体型的目标倒地"],
                    ["群体战术", "若狼的盟友在目标 5 尺内且未失能，狼的攻击检定具有优势"]],
                   [42 * mm, 128 * mm]),
        P("人数调整", "h1"),
        P("3 名玩家：去掉一只哥布林杂兵。5 名玩家：加一只哥布林杂兵。6 名玩家：加两只哥布林杂兵，"
          "并把狼的 HP 提到 14。调整后仍按上表数据，不改攻击加值。", "body"),
        P("战利品", "h1"),
        P("哥布林身上共 12 枚铜币和一把断掉的短弓（卖 1 银币）。桥下木箱里有一瓶治疗药水"
          "（SRD 5.2.1 魔法物品，饮用恢复 2d4＋2 HP）和 15 金币——这是塔姆被抢的货款，"
          "带回村子交给玛拉，或留作队伍经费。", "body"),
        P("DM 提示", "h1"),
        *items([
            "<b>战斗拖过 4 轮：</b>让剩下的哥布林逃跑——第一场战斗见好就收。",
            "<b>玩家卡住不知道干嘛：</b>复述一遍玛拉的线索，或让狼先动——敌人动起来，玩家就有事做了。",
            "<b>有人 HP 归 0：</b>别慌，按第 3 页的死亡豁免走；第一场战斗可让狼转而攻击别人。",
            "<b>跑完开场：</b>回到灰岩村交任务，全队升至 2 级（里程碑式升级）。",
        ]),
        Spacer(1, 4),
        box("试读结束", [
            P("本试读为验证物：共 5 页，未上架，无下载量统计，不含价格与购买链接。"
              "完整版将包含磨坊地窖的探索、最终遭遇、战利品表与 DM 笔记。", "box"),
        ]),
    ]

PAGES = [page1(), page2(), page3(), page4(), page5()]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("NotoSC", 7)
    canvas.setFillColor(GREY)
    w, h = A4
    # attribution, wrapped to two lines
    canvas.drawString(42, 34, "This work includes material from the System Reference Document 5.2.1 (\u201cSRD 5.2.1\u201d) by")
    canvas.drawString(42, 25, "Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed")
    canvas.drawString(42, 16, "under the Creative Commons Attribution 4.0 International License, available at")
    canvas.drawString(42, 7, "https://creativecommons.org/licenses/by/4.0/legalcode.")
    canvas.setFont("NotoSC-Bold", 8)
    canvas.setFillColor(INK)
    canvas.drawRightString(w - 42, 16, f"试读版 · 第 {doc.page} / 5 页")
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=42, rightMargin=42, topMargin=36, bottomMargin=48,
        title="新手 DM 一次性冒险包 · 试读版",
        author="Muse",
    )
    story = []
    for i, page in enumerate(PAGES):
        if i:
            story.append(PageBreak())
        story.extend(page)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("built", OUT)

if __name__ == "__main__":
    build()
