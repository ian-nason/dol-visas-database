"""Generate the per-era column crosswalks (crosswalk_lca.csv, crosswalk_perm.csv).

Reads headers.json (produced by scanning every raw workbook) and emits one
crosswalk row per (era, source_column): its canonical snake_case name, or an
explicit DROP with a reason. The build loads files strictly through these
crosswalks — no ad hoc renames in code. Every source column must be
accounted for; the script fails if any column is unmapped.

Eras:
  lca_2015  FY2015-2016 (40 cols)     perm_2015  FY2015-2019 (125 cols)
  lca_2017  FY2017-2018 (52 cols)     perm_2020  FY2020-2024 old form (154/155)
  lca_2019  FY2019 (260 cols,         perm_2024  FY2024+ new form (135/137)
            worksite groups _1.._10)
  lca_2020  FY2020+ (96-98 cols)
"""
import csv
import json
import re

HEADERS = json.load(open("headers.json"))

ERA_OF_FILE = {}
for f in HEADERS:
    if f.startswith("H-1B_Disclosure_Data_FY15") or f.startswith("H-1B_Disclosure_Data_FY16"):
        ERA_OF_FILE[f] = "lca_2015"
    elif f.startswith("H-1B_Disclosure_Data_FY17") or f.startswith("H-1B_Disclosure_Data_FY2018"):
        ERA_OF_FILE[f] = "lca_2017"
    elif f.startswith("H-1B_Disclosure_Data_FY2019"):
        ERA_OF_FILE[f] = "lca_2019"
    elif f.startswith("LCA_Disclosure"):
        ERA_OF_FILE[f] = "lca_2020"
    elif f.startswith("PERM_Disclosure_Data_New_Form") :
        ERA_OF_FILE[f] = "perm_2024"
    elif f.startswith("PERM_Disclosure_Data_FY2025") or f.startswith("PERM_Disclosure_Data_FY2026"):
        ERA_OF_FILE[f] = "perm_2024"
    elif f.startswith("PERM_Disclosure_Data_FY202") :
        ERA_OF_FILE[f] = "perm_2020"
    elif f.startswith("PERM_Disclosure_Data_FY2024"):
        ERA_OF_FILE[f] = "perm_2020"
    elif f.startswith("PERM"):
        ERA_OF_FILE[f] = "perm_2015"


def snake(c: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", c.lower()).strip("_")


# Explicit synonym renames: source column (exact) -> canonical name.
LCA_RENAMES = {
    "CASE_SUBMITTED": "received_date",
    "EMPLOYMENT_START_DATE": "begin_date",
    "EMPLOYMENT_END_DATE": "end_date",
    "PERIOD_OF_EMPLOYMENT_START_DATE": "begin_date",
    "PERIOD_OF_EMPLOYMENT_END_DATE": "end_date",
    "SOC_NAME": "soc_title",
    "NAIC_CODE": "naics_code",
    "TOTAL WORKERS": "total_worker_positions",
    "TOTAL_WORKERS": "total_worker_positions",
    "WILLFUL VIOLATOR": "willful_violator",
    "H-1B_DEPENDENT": "h_1b_dependent",
    "H1B_DEPENDENT": "h_1b_dependent",
    "EMPLOYER_BUSINESS_DBA": "trade_name_dba",
    "EMPLOYER_ADDRESS": "employer_address1",
    "PW_WAGE_SOURCE": "pw_wage_source",
    "PW_SOURCE": "pw_wage_source",
    "PW_WAGE_SOURCE_YEAR": "pw_wage_source_year",
    "PW_SOURCE_YEAR": "pw_wage_source_year",
    "PW_WAGE_SOURCE_OTHER": "pw_wage_source_other",
    "PW_SOURCE_OTHER": "pw_wage_source_other",
    # FY2015-16 single wage value (may contain "X - Y" ranges; the loader
    # splits ranges into from/to)
    "WAGE_RATE_OF_PAY": "wage_rate_of_pay_from",
    "LABOR_CON_AGREE": "agree_to_lc_statement",
    "PUBLIC_DISCLOSURE_LOCATION": "public_disclosure",
    "AGENT_ATTORNEY_LAW_FIRM_BUSINESS_NAME": "lawfirm_name_business_name",
    "PW_NON-OES_YEAR_1": "pw_other_year",
    "PW_OTHER_SOURCE_1": "pw_other_source",
}

PERM_RENAMES = {
    "CASE_RECEIVED_DATE": "received_date",
    "EMP_BUSINESS_NAME": "employer_name",
    "EMP_TRADE_NAME": "employer_trade_name",
    "EMPLOYER_ADDRESS_1": "employer_address1",
    "EMPLOYER_ADDRESS_2": "employer_address2",
    "EMP_ADDR1": "employer_address1",
    "EMP_ADDR2": "employer_address2",
    "EMP_CITY": "employer_city",
    "EMP_STATE": "employer_state",
    "EMPLOYER_STATE_PROVINCE": "employer_state",
    "EMP_POSTCODE": "employer_postal_code",
    "EMP_COUNTRY": "employer_country",
    "EMP_PROVINCE": "employer_province",
    "EMP_PHONE": "employer_phone",
    "EMP_PHONEEXT": "employer_phone_ext",
    "EMP_FEIN": "employer_fein",
    "EMP_NAICS": "naics_code",
    "NAICS_CODE": "naics_code",
    "EMP_NUM_PAYROLL": "employer_num_employees",
    "EMPLOYER_NUM_EMPLOYEES": "employer_num_employees",
    "EMP_YEAR_COMMENCED": "employer_year_established",
    "EMP_YEAR_COMMENCED_BUSINESS": "employer_year_established",
    "EMPLOYER_YR_ESTAB": "employer_year_established",
    "JOB_INFO_JOB_TITLE": "job_title",
    "PW_SOC_CODE": "soc_code",
    "PWD_SOC_CODE": "soc_code",
    "PW_SOC_TITLE": "soc_title",
    "PWD_SOC_TITLE": "soc_title",
    "WAGE_OFFER_FROM_9089": "wage_offer_from",
    "WAGE_OFFER_FROM": "wage_offer_from",
    "JOB_OPP_WAGE_FROM": "wage_offer_from",
    "WAGE_OFFER_TO_9089": "wage_offer_to",
    "WAGE_OFFER_TO": "wage_offer_to",
    "JOB_OPP_WAGE_TO": "wage_offer_to",
    "WAGE_OFFER_UNIT_OF_PAY_9089": "wage_offer_unit_of_pay",
    "WAGE_OFFER_UNIT_OF_PAY": "wage_offer_unit_of_pay",
    "JOB_OPP_WAGE_PER": "wage_offer_unit_of_pay",
    "PW_AMOUNT_9089": "pw_wage",
    "PW_WAGE": "pw_wage",
    "PW_UNIT_OF_PAY_9089": "pw_unit_of_pay",
    "PW_LEVEL_9089": "pw_level",
    "PW_SKILL_LEVEL": "pw_level",
    "PW_TRACK_NUM": "pw_tracking_number",
    "PW_TRACK_NUMBER": "pw_tracking_number",
    "JOB_OPP_PWD_NUMBER": "pw_tracking_number",
    "PW_DETERM_DATE": "pw_determination_date",
    "PW_DETERMINATION_DATE": "pw_determination_date",
    "PW_EXPIRE_DATE": "pw_expiration_date",
    "PW_EXPIRATION_DATE": "pw_expiration_date",
    "PW_SOURCE_NAME_9089": "pw_wage_source",
    "PW_WAGE_SOURCE": "pw_wage_source",
    "PW_SOURCE_NAME_OTHER_9089": "pw_wage_source_other",
    "PW_SOURCE_NAME_OTHER": "pw_wage_source_other",
    "JOB_INFO_WORK_CITY": "worksite_city",
    "WORKSITE_CITY": "worksite_city",
    "PRIMARY_WORKSITE_CITY": "worksite_city",
    "JOB_INFO_WORK_STATE": "worksite_state",
    "WORKSITE_STATE": "worksite_state",
    "PRIMARY_WORKSITE_STATE": "worksite_state",
    "JOB_INFO_WORK_POSTAL_CODE": "worksite_postal_code",
    "WORKSITE_POSTAL_CODE": "worksite_postal_code",
    "PRIMARY_WORKSITE_POSTAL_CODE": "worksite_postal_code",
    "WORKSITE_ADDRESS_1": "worksite_address1",
    "WORKSITE_ADDRESS_2": "worksite_address2",
    "PRIMARY_WORKSITE_ADDR1": "worksite_address1",
    "PRIMARY_WORKSITE_ADDR2": "worksite_address2",
    "PRIMARY_WORKSITE_COUNTY": "worksite_county",
    "JOB_INFO_EDUCATION": "minimum_education",
    "MINIMUM_EDUCATION": "minimum_education",
    "JOB_INFO_EDUCATION_OTHER": "job_education_min_other",
    "JOB_EDUCATION_MIN_OTHER": "job_education_min_other",
    "JOB_INFO_MAJOR": "major_field_of_study",
    "MAJOR_FIELD_OF_STUDY": "major_field_of_study",
    "JOB_INFO_TRAINING": "required_training",
    "REQUIRED_TRAINING": "required_training",
    "JOB_INFO_TRAINING_NUM_MONTHS": "required_training_months",
    "REQUIRED_TRAINING_MONTHS": "required_training_months",
    "FW_INFO_BIRTH_COUNTRY": "foreign_worker_birth_country",
    "FOREIGN_WORKER_BIRTH_COUNTRY": "foreign_worker_birth_country",
    "FOREIGN_WORKER_INFO_EDUCATION": "foreign_worker_education",
    "FOREIGN_WORKER_EDUCATION": "foreign_worker_education",
    "FW_INFO_EDUCATION_OTHER": "foreign_worker_education_other",
    "FOREIGN_WORKER_EDUCATION_OTHER": "foreign_worker_education_other",
    "AGENT_ATTORNEY_FIRM_NAME": "agent_attorney_firm_name",
    "AGENT_FIRM_NAME": "agent_attorney_firm_name",
    "ATTY_AG_LAW_FIRM_NAME": "agent_attorney_firm_name",
    "AGENT_CITY": "agent_attorney_city",
    "AGENT_ATTORNEY_CITY": "agent_attorney_city",
    "ATTY_AG_CITY": "agent_attorney_city",
    "AGENT_STATE": "agent_attorney_state",
    "AGENT_ATTORNEY_STATE_PROVINCE": "agent_attorney_state",
    "ATTY_AG_STATE": "agent_attorney_state",
    "ORIG_CASE_NO": "orig_case_number",
    "JOB_INFO_EXPERIENCE": "required_experience",
    "REQUIRED_EXPERIENCE": "required_experience",
    "JOB_INFO_EXPERIENCE_NUM_MONTHS": "required_experience_months",
    "REQUIRED_EXPERIENCE_MONTHS": "required_experience_months",
    "RI_LAYOFF_IN_PAST_SIX_MONTHS": "layoff_in_past_six_months",
    "LAYOFF_IN_PAST_SIX_MONTHS": "layoff_in_past_six_months",
    "OTHER_REQ_EMP_LAYOFF": "layoff_in_past_six_months",
    "FOREIGN_WORKER_INFO_MAJOR": "foreign_worker_major",
    "FW_INFO_YR_REL_EDU_COMPLETED": "foreign_worker_yrs_ed_comp",
    "FOREIGN_WORKER_YRS_ED_COMP": "foreign_worker_yrs_ed_comp",
    "FOREIGN_WORKER_INFO_INST": "foreign_worker_inst_of_ed",
    "FOREIGN_WORKER_INST_OF_ED": "foreign_worker_inst_of_ed",
    "FW_INFO_REQ_EXPERIENCE": "foreign_worker_req_experience",
    "FOREIGN_WORKER_REQ_EXPERIENCE": "foreign_worker_req_experience",
}

# Curated analytical keep-list for PERM (user-approved trim): canonical
# columns outside this set become documented drops. LCA is kept full-width.
PERM_KEEP = {
    # case
    "case_number", "case_status", "received_date", "decision_date",
    "refile", "orig_file_date", "orig_case_number", "occupation_type",
    # employer
    "employer_name", "employer_trade_name", "employer_address1",
    "employer_address2", "employer_city", "employer_state",
    "employer_postal_code", "employer_country", "employer_province",
    "employer_phone", "employer_fein", "naics_code",
    "employer_num_employees", "employer_year_established",
    # agent/attorney
    "agent_attorney_firm_name", "agent_attorney_city", "agent_attorney_state",
    # job
    "job_title", "soc_code", "soc_title", "minimum_education",
    "job_education_min_other", "major_field_of_study", "required_training",
    "required_training_months", "required_experience",
    "required_experience_months",
    # wages
    "wage_offer_from", "wage_offer_to", "wage_offer_unit_of_pay",
    "pw_wage", "pw_unit_of_pay", "pw_level", "pw_tracking_number",
    "pw_determination_date", "pw_expiration_date", "pw_wage_source",
    "pw_wage_source_other",
    # worksite
    "worksite_address1", "worksite_address2", "worksite_city",
    "worksite_county", "worksite_state", "worksite_postal_code",
    "is_multiple_locations",
    # foreign worker (absent from the FY2024+ new form by source design)
    "country_of_citizenship", "foreign_worker_birth_country",
    "class_of_admission", "foreign_worker_education",
    "foreign_worker_education_other", "foreign_worker_major",
    "foreign_worker_yrs_ed_comp", "foreign_worker_inst_of_ed",
    "foreign_worker_req_experience", "foreign_worker_curr_employed",
    "foreign_worker_exp_with_empl",
    # recruitment/compliance signals
    "us_workers_considered", "professional_occupation",
    "combination_occupation", "schd_a_sheepherder",
    "layoff_in_past_six_months",
}

WORKSITE_GROUP_RE = re.compile(r"^(.*)_([2-9]|10)$")


def build(program: str, renames: dict, out_path: str, keep: set | None = None):
    eras = {}
    for f, era in ERA_OF_FILE.items():
        if not era.startswith(program):
            continue
        cols = HEADERS[f]
        if isinstance(cols, dict):
            raise SystemExit(f"{f} had a header-scan error")
        eras.setdefault(era, {})[f] = cols

    rows = []
    for era in sorted(eras):
        # Union of columns across files in the era (quarters share layouts;
        # small drifts like 96->97 cols merge here)
        seen = {}
        for f, cols in sorted(eras[era].items()):
            for c in cols:
                seen.setdefault(c, f)
        for c in seen:
            if era == "lca_2019" and WORKSITE_GROUP_RE.match(c):
                rows.append((era, c, "", "drop",
                             "secondary worksite group (_2.._10); primary (_1) kept"))
                continue
            if c in renames:
                canonical, kind, note = renames[c], "core", ""
            elif era == "lca_2019" and c.endswith("_1"):
                canonical, kind = snake(c[:-2]), "core"
                note = "primary worksite group mapped to unsuffixed canonical"
            else:
                canonical, kind, note = snake(c), "passthrough", ""
            if keep is not None and canonical not in keep:
                rows.append((era, c, "", "drop",
                             "trimmed: outside curated analytical set"))
            else:
                rows.append((era, c, canonical, kind, note))

    with open(out_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["era", "source_column", "canonical_column", "kind", "note"])
        w.writerows(rows)

    canon = {r[2] for r in rows if r[3] != "drop"}
    dropped = [r for r in rows if r[3] == "drop"]
    print(f"{program}: {len(rows)} source columns -> {len(canon)} canonical "
          f"({len(dropped)} dropped)")
    return canon


canon_lca = build("lca", LCA_RENAMES, "crosswalk_lca.csv")
canon_perm = build("perm", PERM_RENAMES, "crosswalk_perm.csv", keep=PERM_KEEP)
missing_keep = PERM_KEEP - canon_perm
if missing_keep:
    print(f"NOTE: keep-list names matched by no era: {sorted(missing_keep)}")

# Canonical-collision sanity: no canonical name may be produced by two
# different source columns within the SAME FILE (eras can drift internally;
# the loader maps each file by its own header set).
mapping = {}
for path in ("crosswalk_lca.csv", "crosswalk_perm.csv"):
    for r in csv.DictReader(open(path)):
        if r["kind"] != "drop":
            mapping[(r["era"], r["source_column"])] = r["canonical_column"]
for f, era in ERA_OF_FILE.items():
    cols = HEADERS[f]
    seen = {}
    for c in cols:
        canonical = mapping.get((era, c))
        if canonical is None:
            continue
        if canonical in seen:
            raise SystemExit(
                f"COLLISION in {f}: {canonical} from {seen[canonical]} and {c}"
            )
        seen[canonical] = c
print("no within-file canonical collisions")
