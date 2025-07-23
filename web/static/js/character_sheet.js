// js/character_sheet.js
const sheetData = {
    abilities: {
        str: { base: 10, race: 0, misc: 0 },
        dex: { base: 20, race: 0, misc: 0 },
        con: { base: 15, race: 0, misc: 0 },
        int: { base: 18, race: 0, misc: 0 },
        wis: { base: 14, race: 0, misc: 0 },
        cha: { base: 20, race: 0, misc: 0 },
    },
    saves: { str: 1, dex: 0, con: 1, int: 0, wis: 0, cha: 1 },
    saveMisc: {},
    skills: {
        acrobatics: { prof: 0, misc: 0 },
        animal_handling: { prof: 0, misc: 0 },
        arcana: { prof: 1, misc: 0 },
        athletics: { prof: 0, misc: 0 },
        deception: { prof: 1, misc: 0 },
        history: { prof: 0, misc: 0 },
        insight: { prof: 0, misc: 0 },
        intimidation: { prof: 1, misc: 0 },
        investigation: { prof: 0, misc: 0 },
        medecine: { prof: 0, misc: 0 },
        nature: { prof: 0, misc: 0 },
        perception: { prof: 1, misc: 0 },
        performance: { prof: 0, misc: 0 },
        persuasion: { prof: 1, misc: 0 },
        religion: { prof: 0, misc: 0 },
        sleight_of_hand: { prof: 0, misc: 0 },
        stealth: { prof: 0, misc: 0 },
        survival: { prof: 0, misc: 0 },
    }
};


// ====== CONFIG / CONSTANTS ===================================================
const USE_MOD_TABLE = false; // flip true to use static lookup
const ABILITY_MOD_TABLE = Object.freeze([
    null,  // 0 unused
    -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, // 1-10
    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, // 11-20
    5, 5, 6, 6, 7, 7, 8, 8, 9, 9, // 21-30
]); // extend if you want >30

// Skill → governing ability map (5e)
const SKILL_ABILITY = Object.freeze({
    acrobatics: 'dex',
    animal_handling: 'wis',
    arcana: 'int',
    athletics: 'str',
    deception: 'cha',
    history: 'int',
    insight: 'wis',
    intimidation: 'cha',
    investigation: 'int',
    medecine: 'wis',
    nature: 'int',
    perception: 'wis',
    performance: 'cha',
    persuasion: 'cha',
    religion: 'int',
    sleight_of_hand: 'dex',
    stealth: 'dex',
    survival: 'wis',
});

// ====== UTILS =================================================================
function toInt(n, d = 0) { n = Number(n); return Number.isFinite(n) ? Math.trunc(n) : d; }
function abilityTotal(obj = {}) { return toInt(obj.base) + toInt(obj.race) + toInt(obj.misc); }

function abilityMod(score) {
    score = toInt(score);
    if (USE_MOD_TABLE) {
        if (score < 1) score = 1;
        if (score >= ABILITY_MOD_TABLE.length) {
            // fall back to formula if beyond table
            return Math.floor((score - 10) / 2);
        }
        return ABILITY_MOD_TABLE[score];
    }
    return Math.floor((score - 10) / 2);
}

function formatMod(n) {
    n = toInt(n);
    return (n >= 0 ? `+${n}` : `${n}`);
}

function profLevel(val) {
    // Accept 0/1/2, bool, strings 'prof','exp'
    if (val === true || val === 'prof' || val === 'p') return 1;
    if (val === 'exp' || val === 'expertise' || val === 2) return 2;
    return toInt(val, 0) > 0 ? 1 : 0;
}

function markForProf(level) {
    switch (level) {
        case 2: return '🔵'; // expertise
        case 1: return '🟢'; // proficient
        default: return '⚪'; // none
    }
}

// Safe query of child element(s) inside a row
function qs(parent, sel) { return parent.querySelector(sel); }

// WIP Role state
const ROLL_STATES = ['normal', 'adv', 'dis'];
const ROLL_STATE_LABEL = { normal: '—', adv: 'A', dis: 'D' };

function initRollToggle(row) {
    // Skip if already present
    if (row.querySelector('.roll-state-toggle')) return;

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'roll-state-toggle';
    btn.title = 'Toggle roll: normal → advantage → disadvantage';
    btn.textContent = ROLL_STATE_LABEL.normal;
    btn.dataset.state = 'normal';

    btn.addEventListener('click', e => {
        e.stopPropagation();
        cycleRollState(btn);
    });

    // Append at end (after last child)
    row.appendChild(btn);
}

function cycleRollState(btn) {
    const cur = btn.dataset.state || 'normal';
    const idx = ROLL_STATES.indexOf(cur);
    const next = ROLL_STATES[(idx + 1) % ROLL_STATES.length];
    btn.dataset.state = next;
    btn.textContent = ROLL_STATE_LABEL[next];
    // Reflect on parent row for downstream dice roller hooks
    const row = btn.closest('.saving-throw-row, .skill-row');
    if (row) row.dataset.rollState = next;
}


// ====== PB FROM LEVEL ========================================================
export function getPBFromLevel(level) {
    level = toInt(level, 1);
    if (level < 5) return 2;        // 1-4
    if (level < 9) return 3;        // 5-8
    if (level < 13) return 4;       // 9-12
    if (level < 17) return 5;       // 13-16
    return 6;                       // 17-20 (or higher cap)
}

// ===== TOOLTIPS 
function abilityBreakdownStr(abData) {
    const b = toInt(abData?.base, 0);
    const r = toInt(abData?.race, 0);
    const m = toInt(abData?.misc, 0);
    const tot = b + r + m;
    const mod = abilityMod(tot);
    return `${b} (base) + ${r} (race) + ${m} (misc) = ${tot} [mod ${formatMod(mod)}]`;
}

function saveBreakdownStr(abName, abMod, lvl, pb, misc) {
    const parts = [`${formatMod(abMod)} (${abName.toUpperCase()} mod)`];
    if (lvl === 2) parts.push(`${formatMod(pb * 2)} (expertise PBx2)`);
    else if (lvl === 1) parts.push(`${formatMod(pb)} (PB)`);
    if (misc) parts.push(`${formatMod(misc)} (misc)`);
    const tot = abMod + (lvl === 2 ? pb * 2 : lvl === 1 ? pb : 0) + misc;
    return parts.join(' + ') + ` = ${formatMod(tot)}`;
}

function skillBreakdownStr(skillName, abName, abMod, lvl, pb, misc) {
    const parts = [`${formatMod(abMod)} (${abName.toUpperCase()} mod)`];
    if (lvl === 2) parts.push(`${formatMod(pb * 2)} (expertise PBx2)`);
    else if (lvl === 1) parts.push(`${formatMod(pb)} (PB)`);
    if (misc) parts.push(`${formatMod(misc)} (misc)`);
    const tot = abMod + (lvl === 2 ? pb * 2 : lvl === 1 ? pb : 0) + misc;
    return parts.join(' + ') + ` = ${formatMod(tot)}`;
}

function pbBreakdownStr(level, pb){
  // Human-readable explain
  let bracket;
  if (level >= 17) bracket = "17–20";
  else if (level >= 13) bracket = "13–16";
  else if (level >= 9)  bracket = "9–12";
  else if (level >= 5)  bracket = "5–8";
  else bracket = "1–4";
  return `Level ${level} (range ${bracket}) ⇒ Proficiency Bonus ${formatMod(pb)}`;
}



// ====== ABILITY SCORES TILE ===================================================
/**
 * Update all .char-ability-score-card elements under containerSel
 * @param {string|Element} containerSel - selector or element for the ability scores tile
 * @param {Object} abilitiesData - {str:{base,race,misc}, dex:{...}, ...}
 */
export function loadAbilityScores(containerSel, abilitiesData) {
    const root = (typeof containerSel === 'string') ? document.querySelector(containerSel) : containerSel;
    if (!root) return;

    const cards = root.querySelectorAll('.char-ability-score-card');
    cards.forEach(card => {
        const ab = card.dataset.abilityType;
        if (!ab || !abilitiesData?.[ab]) return;
        const total = abilityTotal(abilitiesData[ab]);
        const mod = abilityMod(total);

        const scoreEl = qs(card, '.char-ability-score');
        const modEl = qs(card, '.char-ability-score-mod');
        if (scoreEl) scoreEl.textContent = total;
        if (modEl) modEl.textContent = formatMod(mod);
    });
}

// ====== SAVING THROWS TILE ====================================================
/**
 * Update Saving Throws.
 * Expects rows: .saving-throw-row[data-ability-type]
 * Cols: <span> marker, .saving-throw-mod span, .saving-throw-ability p (unchanged)
 *
 * @param {string|Element} containerSel - saving throw tile container
 * @param {Object} abilitiesData - same as for loadAbilityScores()
 * @param {number} proficiencyBonus - PB
 * @param {Object} saveProfs - {str:1|2|0,...}
 * @param {Object} [saveMisc] - {str:+/-n,...} optional extra bonus
 */
export function loadSavingThrows(containerSel, abilitiesData, proficiencyBonus, saveProfs, saveMisc = {}) {
    const root = (typeof containerSel === 'string') ? document.querySelector(containerSel) : containerSel;
    if (!root) return;

    const rows = root.querySelectorAll('.saving-throw-row');
    rows.forEach(row => {
        const ab = row.dataset.abilityType;
        if (!ab) return;
        const totalAbScore = abilityTotal(abilitiesData?.[ab] || {});
        const baseMod = abilityMod(totalAbScore);

        const lvl = profLevel(saveProfs?.[ab]);
        const misc = toInt(saveMisc?.[ab], 0);
        const profBonus = lvl === 2 ? proficiencyBonus * 2 : lvl === 1 ? proficiencyBonus : 0;
        const total = baseMod + profBonus + misc;

        const markEl = qs(row, 'span, .save-proficiency-status'); // support markup variations
        const modEl = qs(row, '.saving-throw-mod');
        if (markEl) markEl.textContent = markForProf(lvl);
        if (modEl) modEl.textContent = formatMod(total);
        row.dataset.total = total;

        // Tooltip breakdown
        row.title = saveBreakdownStr(ab, baseMod, lvl, proficiencyBonus, misc);

        // Roll toggle
        initRollToggle(row);
    });
}

// ====== SKILLS TILE ===========================================================
/**
 * Update Skills.
 * Expects rows: .skill-row[data-ability-type][data-skill-name]
 * Cols: span.skill-proficiency-status, span.skill-mod, p.skill-name, p.skill-ability-hint
 *
 * @param {string|Element} containerSel - skills tile container
 * @param {Object} abilitiesData - ability breakdowns
 * @param {number} proficiencyBonus - PB
 * @param {Object} skillData - {skillName:{prof:0|1|2, misc:n}}
 * @param {Object} [skillOverrideAbility] - optional override map skill→ability
 */
export function loadSkills(containerSel, abilitiesData, proficiencyBonus, skillData, skillOverrideAbility = {}) {
    const root = (typeof containerSel === 'string') ? document.querySelector(containerSel) : containerSel;
    if (!root) return;

    const rows = root.querySelectorAll('.skill-row');
    rows.forEach(row => {
        const skillName = row.dataset.skillName;
        // ability: prefer data attr, else override map, else default map
        let ab = row.dataset.abilityType || skillOverrideAbility[skillName] || SKILL_ABILITY[skillName];
        if (!ab) {
            console.warn(`No ability mapping for skill ${skillName}; defaulting INT`);
            ab = 'int';
        }

        const totalAbScore = abilityTotal(abilitiesData?.[ab] || {});
        const baseMod = abilityMod(totalAbScore);

        const skillEntry = skillData?.[skillName] || {};
        const lvl = profLevel(skillEntry.prof);
        const misc = toInt(skillEntry.misc, 0);
        const profBonus = lvl === 2 ? proficiencyBonus * 2 : lvl === 1 ? proficiencyBonus : 0;
        const total = baseMod + profBonus + misc;

        const markEl = qs(row, '.skill-proficiency-status, [clas="skill-proficiency-status"]'); // forgiving selector for your current typo
        const modEl = qs(row, '.skill-mod');
        if (markEl) markEl.textContent = markForProf(lvl);
        if (modEl) modEl.textContent = formatMod(total);
        row.dataset.total = total;

        // Tooltip breakdown
        row.title = skillBreakdownStr(skillName, ab, baseMod, lvl, proficiencyBonus, misc);

        // Roll toggle
        initRollToggle(row);
    });
}

// ====== TOP-LEVEL LOADER ======================================================
/**
 * loadCharSheetTiles(options)
 * options = {
 *   level: 12,                            // <-- REQUIRED for PB autocalc
 *   proficiencyBonusOverride: null,       // if set, uses this instead of level
 *   abilitySel: '.char-ability-score-container',
 *   abilityVerticalSel: '.char-ability-score-container.vertical',
 *   saveSel: '.saving-throw-container',
 *   skillsSel: null, // see notes
 *   data: {}  // same shape as before EXCEPT you can omit data.proficiencyBonus
 * }
 */
export function loadCharSheetTiles(opts) {
    const {
        level = 1,
        proficiencyBonusOverride = null,
        abilitySel = '.char-ability-score-container',
        abilityVerticalSel = '.char-ability-score-container.vertical',
        saveSel = '.saving-throw-container',
        skillsSel = null,
        profCardSel='.char-prof-bonus-card',
        data,
    } = opts || {};
    if (!data) return;

    // Proficiency Bonus
    const pb = proficiencyBonusOverride != null
        ? toInt(proficiencyBonusOverride, 2)
        : (toInt(data.proficiencyBonus, NaN) || getPBFromLevel(level));

    loadProficiencyBonusCard(profCardSel, level, pb);

    // Abilities
    loadAbilityScores(abilitySel, data.abilities);
    const vertEl = document.querySelector(abilityVerticalSel);
    if (vertEl && !vertEl.isSameNode(document.querySelector(abilitySel))) {
        loadAbilityScores(vertEl, data.abilities);
    }

    // Containers
    let saveContainer, skillsContainer;
    if (!skillsSel) {
        const all = document.querySelectorAll(saveSel);
        saveContainer = all[0] || null;
        skillsContainer = all[1] || null;
    } 
    else {
        saveContainer = document.querySelector(saveSel);
        skillsContainer = document.querySelector(skillsSel);
    }

    if (saveContainer) {
        loadSavingThrows(
            saveContainer,
            data.abilities,
            pb,
            data.saves,
            data.saveMisc || {}
        );
    }

    if (skillsContainer) {
        loadSkills(
            skillsContainer,
            data.abilities,
            pb,
            data.skills,
        );
    }
}

export function loadProficiencyBonusCard(cardSel, level, pb){
  const card = (typeof cardSel === 'string') ? document.querySelector(cardSel) : cardSel;
  if (!card) return;
  const span = card.querySelector('.char-prof-bonus');
  if (span) span.textContent = formatMod(pb);
  card.dataset.pb = pb;
  card.title = pbBreakdownStr(level, pb);          // native tooltip fallback
  card.dataset.tooltip = card.title;               // for custom tooltip system
  card.classList.add('tt-host');                   // WIP if using custom tooltip CSS from earlier
}


function syncRollStateAttrs(row, state){
  // clear
  row.removeAttribute('data-state-adv');
  row.removeAttribute('data-state-dis');
  if (state === 'adv') row.setAttribute('data-state-adv', '');
  else if (state === 'dis') row.setAttribute('data-state-dis', '');
  // if using value pattern instead:
  // row.dataset.state = state; // sets data-state="adv"/"dis"/"normal"
}


// ====== DOM READY =============================================================
document.addEventListener("DOMContentLoaded", () => {
    if (typeof sheetData !== 'undefined' && sheetData?.abilities) {
        loadCharSheetTiles({
            level: 12,
            data: sheetData,
            profCardSel: '.char-prof-bonus-card',
        });
    }

    insertChevronsIntoDetailsFA();
});
