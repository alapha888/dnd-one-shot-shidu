# -*- coding: utf-8 -*-
"""Build the 5-page English trial-read PDF for the D&D 2024 SRD-only beginner DM
one-shot pack. English translation of build_pdf.py (same structure, same 5 pages).
All prose is original. Rules are paraphrased from SRD 5.2.1 (CC-BY-4.0) with attribution.
Monster numbers are SRD 5.2.1 stat-block facts (Goblin Minion p.290, Wolf p.364),
re-checked against the official SRD 5.2.1 PDF on 2026-11-07 (Wolf Bite: no save in
5.2.1 — a Medium or smaller target simply has the Prone condition).
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, HRFlowable)

OUT_DIR = os.path.expanduser("~/workspace/independent/dnd-one-shot")
OUT = os.path.join(OUT_DIR, "dnd-one-shot-shidu-en.pdf")

INK = HexColor("#111111")
GREY = HexColor("#555555")
LIGHT = HexColor("#F2F2F2")
RULE = HexColor("#999999")

S = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=18, leading=22,
                            textColor=INK, alignment=TA_LEFT, spaceAfter=3),
    "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10, leading=14,
                               textColor=GREY, spaceAfter=6),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13, leading=17,
                         textColor=INK, spaceBefore=7, spaceAfter=4),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=15,
                         textColor=INK, spaceBefore=6, spaceAfter=2),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14.5,
                           textColor=INK, spaceAfter=3),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=9, leading=13,
                            textColor=GREY, spaceAfter=2),
    "item": ParagraphStyle("item", fontName="Helvetica", fontSize=10, leading=14.5,
                           textColor=INK, leftIndent=16, firstLineIndent=0,
                           bulletIndent=6, spaceAfter=1),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9.5, leading=13.5,
                           textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=9.5, leading=13.5,
                            textColor=INK),
    "cellhead": ParagraphStyle("cellhead", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
                               textColor=INK),
    "box": ParagraphStyle("box", fontName="Helvetica", fontSize=10, leading=14.5,
                          textColor=INK, spaceAfter=2),
    "readaloud": ParagraphStyle("readaloud", fontName="Helvetica", fontSize=10, leading=15,
                                textColor=INK, leftIndent=10, rightIndent=10, spaceAfter=3),
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
        P("First-Time DM One-Shot Adventure Pack &middot; Free Preview", "title"),
        P("5E compatible &middot; SRD 5.2.1 open content only &middot; Written for first-time Dungeon Masters", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("This preview is 5 pages: page 1 is a Session Zero checklist; "
          "pages 2&ndash;3 are quick-reference cards for the rulings a new DM needs in a first fight; "
          "pages 4&ndash;5 are the opening and first encounter of an original one-shot. "
          "Rules are paraphrased from SRD 5.2.1; monster statistics come from the SRD 5.2.1 bestiary; "
          "the adventure, place names, and characters are original.", "body"),
        P("Page 1 &middot; Session Zero Checklist", "h1"),
        P("Before the first session, sit down with your players and settle these 14 items one by one. "
          "Write the answers in your group chat &mdash; when a disagreement comes up later, check the list. "
          "Most new-table arguments are not rules problems; they are things nobody agreed on before play.", "body"),
        P("A. Logistics", "h2"),
        *items([
            "<b>Time and frequency:</b> a fixed evening each week (or every other week), about 3 hours a session. "
            "Late or absent? Say so in the group chat ahead of time.",
            "<b>Where and how:</b> in person or online; physical dice or a dice app; a whiteboard, pen and paper, or a virtual tabletop.",
            "<b>Party size:</b> 3&ndash;5 players suits a new DM best. This adventure is built for four 1st-level characters; "
            "see page 5 for other party sizes.",
            "<b>Absences:</b> an absent player's character is run by the DM as a follower only &mdash; "
            "no scene-stealing, no plot deaths, no lost rewards.",
        ]),
        P("B. Characters", "h2"),
        *items([
            "<b>Character creation:</b> start at 1st level. Ability scores use the standard array (15, 14, 13, 12, 10, 8) "
            "or roll 4d6 and drop the lowest; species and classes from SRD 5.2.1 only "
            "(Character Creation, from p. 19).",
            "<b>Backgrounds and ties:</b> each player writes one sentence of backstory and a tie to at least one other "
            "character (old friend, creditor, fellow villager&hellip;).",
            "<b>Ground rules:</b> no hostile PvP, no stealing from party members, no jokes at a fellow character's expense.",
            "<b>Levelling:</b> reach 2nd level after this adventure, using milestone levelling &mdash; no counting XP per monster.",
        ]),
        P("C. Play Style and Boundaries", "h2"),
        *items([
            "<b>Style mix:</b> agree the balance of combat, exploration, and roleplay up front, so the DM knows what to prepare.",
            "<b>Content boundaries:</b> the limits on horror, gore, and betrayal. Keep an X-Card on the table: anyone who is "
            "uncomfortable taps it &mdash; no explanation needed &mdash; and the scene moves on at once.",
            "<b>Rulings:</b> at the table, the DM's call stands; if you are unsure, note it down and check the SRD after the session &mdash; "
            "never stop play to flip through the book.",
            "<b>Open rolls:</b> the DM rolls in the open; players roll their own dice; a reroll counts only when the DM calls for it.",
            "<b>Character death:</b> settle this with a new table first &mdash; a dead character is replaced, or the party finds a way to "
            "bring them back. Either is fine; agree it now and nobody's feelings get hurt later.",
            "<b>Feedback:</b> after each session, take 5 minutes: one thing each person liked, one thing to improve.",
        ]),
        Spacer(1, 2),
        box("The 10 minutes before play", [
            P("1. Recap the last session (first session: read the page 4 opening aloud) &nbsp; 2. Agree tonight's goal &nbsp; "
              "3. Check character sheets, dice, and snacks &nbsp; 4. Put the X-Card in the middle of the table.", "box"),
        ]),
    ]

# ---------------------------------------------------------------- page 2
def page2():
    return [
        P("Page 2 &middot; First-Fight Quick Card (1): D20 Checks and Combat", "title"),
        P("Rules sources: SRD 5.2.1, Playing the Game (from p. 5), Combat (from p. 13), Damage and Healing (from p. 16). "
          "This page covers only what a new DM actually uses in a first fight.", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("The D20 check, in three steps", "h1"),
        P("<b>1. Roll a d20. &nbsp; 2. Add modifiers</b> (the relevant ability modifier; if proficient, add the proficiency bonus, +2 at 1st level). "
          "<b>3. Compare:</b> ability checks and saving throws against a Difficulty Class (DC); attack rolls against the target's "
          "Armor Class (AC). Meeting the number is a success.", "body"),
        P("Advantage and disadvantage", "h2"),
        P("With Advantage, roll two d20s and take the higher; with Disadvantage, take the lower. "
          "If you have both, they cancel out and you roll one die. Multiple sources of Advantage do not stack.", "body"),
        P("Typical Difficulty Classes (DC)", "h2"),
        data_table(["Difficulty", "DC", "Example"],
                   [["Very Easy", "5", "Push open an unlocked door"],
                    ["Easy", "10", "Find a book in a quiet library"],
                    ["Medium", "15", "Climb a rough stone wall"],
                    ["Hard", "20", "Hear distant footsteps in a storm"],
                    ["Very Hard", "25", "Pry open a rusted iron chest bare-handed"],
                    ["Nearly Impossible", "30", "Track a three-day-old trail by scent"]],
                   [32 * mm, 16 * mm, 122 * mm]),
        P("When unsure what DC to set, pick 10 or 15 &mdash; a new table is better off with more successes than fewer.", "small"),
        P("How an attack roll works", "h1"),
        *items([
            "<b>Pick a target:</b> within the weapon's range or reach, and the attacker can see it.",
            "<b>Roll:</b> d20 + attack bonus (ability modifier + proficiency bonus, if applicable).",
            "<b>Compare to AC:</b> a total equal to or higher than the target's AC hits. A natural 20 always hits and is a critical hit; "
            "a natural 1 always misses.",
            "<b>Roll damage:</b> the weapon's damage dice + the same ability modifier; spells roll as their description says.",
            "<b>Subtract HP:</b> the target loses that many Hit Points. At 0 HP a character falls unconscious &mdash; see page 3.",
        ]),
        P("Critical hit: roll the damage dice twice and add them together; the ability modifier is added only once.", "body"),
        P("Saving throws", "h2"),
        P("The DM names an ability and a DC, for example, &ldquo;Constitution save, DC 12.&rdquo; The player rolls d20 + that ability's "
          "saving throw bonus; meeting the DC succeeds, failing means suffering whatever the spell or effect says.", "body"),
        P("What you can do on your turn", "h2"),
        P("Each turn: <b>one move</b> (up to your Speed, splittable around your action) + <b>one action</b> "
          "(attack, cast a spell, Dash, Disengage, Hide, and so on) + <b>one bonus action</b> (only when a class feature or spell "
          "gives you one) + <b>one reaction</b> (on someone else's turn, such as an opportunity attack).", "body"),
        P("Initiative: when combat starts, everyone rolls d20 + Dexterity modifier, highest first; the DM rolls for the monsters. "
          "On a tie, the DM decides the order.", "body"),
    ]

# ---------------------------------------------------------------- page 3
def page3():
    return [
        P("Page 3 &middot; First-Fight Quick Card (2): Conditions and Falling", "title"),
        P("Rules sources: condition entries in the SRD 5.2.1 Rules Glossary (from p. 176); "
          "falling and dying rules in Damage and Healing (pp. 16&ndash;17). A condition never stacks with itself.", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("Common conditions, one line each", "h1"),
        data_table(["Condition", "Effect (in brief)"],
                   [["Prone", "Moves only by crawling; standing costs half your movement; its attack rolls have Disadvantage; attacks against it have Advantage within 5 ft, Disadvantage beyond."],
                    ["Blinded", "Can't see; attacks against the creature have Advantage; its own attack rolls have Disadvantage; checks relying on sight fail."],
                    ["Deafened", "Can't hear; checks relying on hearing fail."],
                    ["Charmed", "Can't attack the charmer or target it with harmful abilities; the charmer has Advantage on social checks against it."],
                    ["Frightened", "While the source of fear is visible, checks and attack rolls have Disadvantage; can't willingly move toward the source."],
                    ["Restrained", "Speed is 0; attacks against the creature have Advantage; its own attack rolls have Disadvantage; Dexterity saves have Disadvantage."],
                    ["Incapacitated", "Can't take actions or reactions."],
                    ["Invisible", "Can't be seen; attacks against the creature have Disadvantage; its own attack rolls have Advantage."],
                    ["Paralyzed", "Incapacitated, can't move or speak; Strength and Dexterity saves fail automatically; attacks within 5 ft have Advantage and a hit is a critical hit."],
                    ["Stunned", "Incapacitated, can't move, speaks haltingly; Strength and Dexterity saves fail automatically; attacks against the creature have Advantage."],
                    ["Unconscious", "Incapacitated, can't move or speak, drops what it holds and falls Prone; Strength and Dexterity saves fail automatically; attacks within 5 ft have Advantage and a hit is a critical hit."],
                    ["Grappled", "Speed is 0; ends if the grappler is Incapacitated or the target leaves the grappler's reach."]],
                   [30 * mm, 140 * mm]),
        P("At 0 HP and death saving throws", "h1"),
        P("A character at 0 HP falls unconscious. An ally can use an action to make a DC 10 Medicine check to stabilize them, "
          "or restore HP with a healing spell or potion. Each turn, the unconscious character makes a death saving throw "
          "(d20, no modifier): 10 or higher is one success, below 10 one failure; a 20 restores 1 HP; "
          "a 1 counts as two failures. Three successes: stable (stays at 0 HP, stops rolling). Three failures: death. "
          "Damage while unconscious is one failure; damage from a critical hit is two.", "body"),
        P("Damage, resistance, and vulnerability", "h2"),
        P("Damage has a type (slashing, piercing, bludgeoning, fire, and so on). Resistance: damage of that type is halved "
          "(rounded down); Vulnerability: doubled; Immunity: no damage.", "body"),
        Spacer(1, 2),
        box("Three sentences for when you are unsure at the table", [
            P("1. &ldquo;We'll rule it this way for now &mdash; keep playing.&rdquo; Ruling on the spot comes first; "
              "don't let a rulebook search stop the game.<br/>"
              "2. Write the question down and check the SRD after the session.<br/>"
              "3. At the next session, take one minute to tell everyone the correct ruling.", "box"),
        ]),
        P("The hardest part for a new DM is not the rules &mdash; it is the fear of ruling wrong. One wrong call costs nothing; "
          "fix it next session. Players remember tonight's story, not a DC set 5 points too high.", "body"),
    ]

# ---------------------------------------------------------------- page 4
def page4():
    return [
        P("Page 4 &middot; Original Adventure, &ldquo;The Broken Bridge over Firefly Creek&rdquo;: Opening", "title"),
        P("Original story and place names; no official setting names or official art used. All monsters are from SRD 5.2.1. "
          "Built for four 1st-level characters; about 2&ndash;3 hours to play the opening and first encounter.", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("Background (for the DM only &mdash; do not read this to the players)", "h1"),
        P("Grayrock is a village of barely thirty households, living off the mill on Firefly Creek and a caravan "
          "that comes once a week. Three days ago Tam, the village messenger, set out along the creekside trail with a letter "
          "for the next village &mdash; and never came back. Mara, the village head's wife, sent two villagers to look; "
          "all they found was a broken arrow and one bloodied shoe. She suspects the goblins in the brush &mdash; "
          "people have heard movement there after dusk. Her notice at the village gate offers 20 gold pieces for bringing "
          "Tam back, or bringing word of him.", "body"),
        P("Opening narration (read aloud to the players)", "h1"),
        P("&ldquo;Dusk fog creeps along Firefly Creek, and the lamps of Grayrock Village come on one by one. A new notice is pinned "
          "to the board at the village gate, its handwriting hurried, one corner lifting and falling in the wind. Beneath it stands "
          "a grey-haired woman &mdash; Mara, the village head's wife &mdash; watching you with the look of someone counting how many "
          "miles your rations will last.&rdquo;", "readaloud"),
        P("Mara will tell the players: Tam left three days ago along the creekside trail to carry a letter to the next village and "
          "has not returned; 20 gold pieces for bringing him back or bringing word of him; the villagers found only a broken arrow "
          "and one bloodied shoe. The players may ask her about it (roleplay or a check &mdash; either works):", "body"),
        *items([
            "<b>Ask about the goblins (DC 10 History or Investigation):</b> Mara says there are only three or four goblins in the "
            "brush, timid, fond of robbing travellers who walk alone.",
            "<b>Ask about the trail (DC 10 Survival):</b> she points along the creekside trail &mdash; cart ruts, and footprints that "
            "do not belong to any villager.",
            "<b>Ask about the reward:</b> 20 gold pieces, split across the whole party: 5 gold pieces paid up front, 15 on return.",
        ]),
        P("Scene 1: The creekside trail", "h1"),
        P("After half an hour the creek grows louder. Ask for a DC 10 Wisdom "
          "(Perception) or Survival check: success finds a broken arrow, one bloodied shoe, and drag marks into the brush; "
          "failure finds only the broken arrow, and ten more minutes of searching are needed to find the marks. "
          "Following them, the players reach a broken bridge &mdash; half its deck collapsed, knee-deep water below, "
          "something moving in the brush on the far bank.", "body"),
        P("Scene 2: Ambush at the broken bridge (first encounter)", "h1"),
        P("Two goblin minions and a wolf hide in the brush on the far bank, waiting until the players reach the middle of the bridge. "
          "Before combat, the goblins make a Stealth check against each character's passive Perception: a character who does not "
          "notice the enemy can't move or take actions or reactions on their first turn of combat (until that turn ends).", "body"),
        P("Goblin tactics: the minions fight with daggers and flee once their HP is halved; the wolf uses Pack Tactics and goes for "
          "isolated or fallen targets. If the players talk instead of fighting, the goblin chief is not here &mdash; the minions "
          "are cowards, and a DC 12 Intimidation or Persuasion check sends them fleeing, dropping Tam's shoe &mdash; "
          "but the wolf does not negotiate. Statistics are on page 5.", "body"),
        P("Clues after the fight: a torn sack behind the brush holds Tam's mailbag (the letter inside undamaged) and a "
          "crude map pointing to the cellar of the old mill by the creek &mdash; the preview ends here; the mill cellar in "
          "full is in the complete pack.", "body"),
    ]

# ---------------------------------------------------------------- page 5
def page5():
    return [
        P("Page 5 &middot; First-Encounter Stat Cards and DM Notes", "title"),
        P("Monster statistics paraphrased from SRD 5.2.1: Goblin Minion, p. 290; Wolf, p. 364. "
          "Total encounter XP: 100 (25 + 25 + 50) &mdash; easy to medium for four 1st-level characters.", "subtitle"),
        HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6),
        P("Goblin Minion &times; 2", "h1"),
        data_table(["Statistic", "Value"],
                   [["Size / Alignment", "Small Fey (Goblinoid), Chaotic Neutral"],
                    ["AC / HP / Speed", "AC 12; HP 7 (2d6); Speed 30 ft; Initiative +2"],
                    ["Skills / Senses", "Stealth +6; Darkvision 60 ft; Passive Perception 9"],
                    ["Languages / Challenge", "Common, Goblin; CR 1/8 (25 XP)"],
                    ["Dagger (Melee / Ranged)", "Attack +4, reach 5 ft or range 20/60 ft; Hit: 4 (1d4 + 2) piercing damage"],
                    ["Nimble Escape (Bonus Action)", "Takes the Disengage or Hide action"]],
                   [48 * mm, 122 * mm]),
        P("Wolf &times; 1", "h1"),
        data_table(["Statistic", "Value"],
                   [["Size / Alignment", "Medium Beast, Unaligned"],
                    ["AC / HP / Speed", "AC 12; HP 11 (2d8 + 2); Speed 40 ft; Initiative +2"],
                    ["Skills / Senses", "Perception +5, Stealth +4; Darkvision 60 ft; Passive Perception 15"],
                    ["Challenge Rating", "CR 1/4 (50 XP)"],
                    ["Bite (Melee)", "Attack +4, reach 5 ft; Hit: 5 (1d6 + 2) piercing damage; a Medium or smaller target has the Prone condition"],
                    ["Pack Tactics", "Advantage on attack rolls if an ally is within 5 ft of the target and the ally isn't Incapacitated"]],
                   [48 * mm, 122 * mm]),
        P("Scaling for party size", "h1"),
        P("3 players: remove one goblin minion. 5 players: add one goblin minion. 6 players: add two goblin minions and raise "
          "the wolf's HP to 14. Use the statistics above unchanged; do not change attack bonuses.", "body"),
        P("Loot", "h1"),
        P("The goblins carry 12 copper pieces between them and a broken shortbow (sells for 1 silver piece). A wooden crate under "
          "the bridge holds a Potion of Healing (drinking it restores 2d4 + 2 HP) and 15 gold pieces "
          "&mdash; the payment Tam was robbed of. Return it to Mara, or keep it as party funds.", "body"),
        P("DM notes", "h1"),
        *items([
            "<b>Combat drags past 4 rounds:</b> have the remaining goblins flee &mdash; end the first fight while it is still fun.",
            "<b>Players stuck with nothing to do:</b> repeat Mara's clues, or have the wolf move first &mdash; once the enemy acts, the players have something to do.",
            "<b>Someone drops to 0 HP:</b> don't panic; run the death saving throws from page 3. In a first fight, let the wolf turn on someone else.",
            "<b>After the opening:</b> return to Grayrock, turn in the job, and the whole party reaches 2nd level (milestone levelling).",
        ]),
        Spacer(1, 4),
        box("End of preview", [
            P("This preview is a validation item: 5 pages, not yet listed anywhere, with no download statistics, no price, "
              "and no purchase link. The complete pack will contain the mill cellar exploration, the final encounter, "
              "a loot table, and DM notes.", "box"),
        ]),
    ]

PAGES = [page1(), page2(), page3(), page4(), page5()]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(GREY)
    w, h = A4
    # attribution, verbatim from SRD 5.2.1 p.1 Legal Information
    canvas.drawString(42, 34, "This work includes material from the System Reference Document 5.2.1 (\u201cSRD 5.2.1\u201d) by")
    canvas.drawString(42, 25, "Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed")
    canvas.drawString(42, 16, "under the Creative Commons Attribution 4.0 International License, available at")
    canvas.drawString(42, 7, "https://creativecommons.org/licenses/by/4.0/legalcode.")
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(INK)
    canvas.drawRightString(w - 42, 16, f"Free Preview \u00b7 Page {doc.page} / 5")
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=42, rightMargin=42, topMargin=32, bottomMargin=46,
        title="First-Time DM One-Shot Adventure Pack \u00b7 Free Preview",
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
